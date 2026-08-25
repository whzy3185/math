"""Submission-package and exact-evidence entry point for Target A."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
MAIN = REPO / "research/paper/manuscript_tex_task59"
SUPP = REPO / "research/paper/manuscript_tex_task59_supplement"
MANIFEST = REPO / "research/proofs/task59/submission_manifest.json"
TITLE = "When Is the Twisted Signing of an Even Cycle Square Spectrally Optimal?"
AUTHORS = "Yicheng Zhao; Jiachen Li"
FROZEN_ENGLISH = "59e3a8f73a152ef06f994e979b7219a3365efeae"
FROZEN_CHINESE = "57ae03fb5b90866f84d0d72b414008678e8f5004"

EXACT_VERIFIERS = [
    "research/scripts/verify_target_a_task50_interface.py",
    "research/scripts/verify_target_a_task51.py",
    "research/scripts/verify_target_a_task53_a2.py",
    "research/scripts/verify_target_a_task53_a3.py",
    "research/scripts/verify_target_a_task55_exact_2r.py",
    "research/scripts/verify_target_a_task55_single_gap.py",
    "research/scripts/verify_target_a_task56_single_gap.py",
    "research/scripts/verify_target_a_task57_uniform_single_gap.py",
    "research/scripts/verify_target_a_minimality_certificate.py",
    "research/scripts/verify_target_a_n32_certificate.py",
    "research/scripts/verify_target_a_task55_small_order_exact.py",
    "research/scripts/verify_target_a_task55_orders_34_46.py",
    "research/scripts/verify_target_a_task54_threshold.py",
]

FOCUSED_TESTS = [
    "research/scripts/test_target_a_task55_exact_2r.py",
    "research/scripts/test_target_a_task55_single_gap.py",
    "research/scripts/test_target_a_task56_single_gap.py",
    "research/scripts/test_target_a_task57_uniform_single_gap.py",
    "research/scripts/test_verify_target_a_minimality_certificate.py",
    "research/scripts/test_verify_target_a_n32_certificate.py",
    "research/scripts/test_target_a_task55_small_order_exact.py",
    "research/scripts/test_target_a_task55_orders_34_46.py",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git_tree(path: str) -> str:
    output = subprocess.check_output(
        ["git", "ls-tree", "HEAD", path], cwd=REPO, text=True
    ).strip()
    require(output, f"missing frozen tree: {path}")
    return output.split()[2]


def source_audit() -> dict[str, int]:
    tex_paths = list(MAIN.rglob("*.tex"))
    main_tex = "\n".join(path.read_text(encoding="ascii") for path in tex_paths)
    supp_tex = "\n".join(
        path.read_text(encoding="ascii") for path in SUPP.rglob("*.tex")
    )
    intro = (MAIN / "sections/01_introduction.tex").read_text(encoding="ascii")
    section6 = (MAIN / "sections/06_finite_rings.tex").read_text(encoding="ascii")

    labels = re.findall(r"\\label\{([^}]+)\}", main_tex)
    refs = re.findall(r"\\(?:ref|eqref|cref|Cref)\{([^}]+)\}", main_tex)
    require(not [key for key, n in Counter(labels).items() if n > 1],
            "duplicate labels")
    require(set(refs) <= set(labels), "undefined cross-reference")

    bib = (MAIN / "references.bib").read_text(encoding="ascii")
    bib_keys = re.findall(r"@\w+\{([^,]+),", bib)
    groups = re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", main_tex)
    citations = {key.strip() for group in groups for key in group.split(",")}
    require(citations <= set(bib_keys), "undefined citation")
    require(len(citations) >= 18, "literature positioning remains too thin")

    require("p_6(y)=" not in intro and "7905369311620327" not in intro,
            "certificate detail remains in the Introduction")
    require("tab:truth-pattern" in intro, "truth-pattern table absent")
    require("Classification of the conjectured equality" in intro,
            "main theorem scope is not qualified")
    require(r"\begin{theorem}[Separated-interface cluster]" not in section6,
            "exact-2r theorem remains in the main line")
    require("Separated-interface cluster" in supp_tex,
            "exact-2r theorem missing from supplement")
    for required in (
        "Yicheng Zhao", "Jiachen Li", "2023213805@cqupt.edu.cn",
        "2023213809@stu.cqupt.edu.cn", "0009-0003-7618-1661",
        "0009-0006-5119-3369",
    ):
        require(required in main_tex, f"identified author field absent: {required}")
    for placeholder in (
        "[AUTHOR NAME]", "[AFFILIATION]", "[DEPARTMENT]", "[INSTITUTION]",
        "[CITY]", "[COUNTRY]", "[EMAIL]", "[ORCID]",
    ):
        require(placeholder not in main_tex + supp_tex,
                f"author placeholder remains: {placeholder}")

    forbidden = ("TODO", "TBD", "FIXME", "Lorem", "proof to be added")
    all_tex = main_tex + "\n" + supp_tex
    for marker in forbidden:
        require(marker.lower() not in all_tex.lower(),
                f"draft marker remains: {marker}")
    require(re.search(r"\\footnote(?:\[|\{)", main_tex) is None,
            "author footnote remains")

    return {
        "labels": len(labels),
        "citations": len(citations),
        "main_exact_occurrences": len(re.findall(r"\bexact\w*", main_tex, re.I)),
    }


def manifest_audit(require_tag: bool) -> dict[str, int]:
    data = json.loads(MANIFEST.read_text(encoding="ascii"))
    require(data["schema"] == "target-a-submission-manifest-v1",
            "manifest schema mismatch")
    require(data["archive_status"] == "IMMUTABLE_ARCHIVE_PENDING",
            "archive status is not truthful")
    files = 0
    for family in data["families"]:
        require(family["logical_role"] and family["producers"] and
                family["verifiers"] and family["independence"],
                f"incomplete family contract: {family['id']}")
        for entry in family["certificates"]:
            path = REPO / entry["path"]
            require(path.is_file(), f"missing certificate: {entry['path']}")
            require(sha256(path) == entry["sha256"],
                    f"certificate digest mismatch: {entry['path']}")
            files += 1
        for raw in family["producers"] + family["verifiers"]:
            require((REPO / raw).is_file(), f"manifest path missing: {raw}")
    if require_tag:
        subprocess.run(
            ["git", "rev-parse", "--verify", f"refs/tags/{data['submission_tag']}"],
            cwd=REPO, check=True, stdout=subprocess.DEVNULL
        )
    return {"families": len(data["families"]), "certificates": files}


def pdf_audit() -> dict[str, int]:
    readers = {
        "main": PdfReader(MAIN / "main.pdf"),
        "anonymous": PdfReader(MAIN / "main_anonymous.pdf"),
        "supplement": PdfReader(SUPP / "main.pdf"),
        "supplement_anonymous": PdfReader(SUPP / "main_anonymous.pdf"),
    }
    require(readers["main"].metadata.title == TITLE, "main PDF title mismatch")
    require(readers["anonymous"].metadata.title == TITLE,
            "anonymous PDF title mismatch")
    require(readers["anonymous"].metadata.author == "Anonymous",
            "anonymous author metadata mismatch")
    require(readers["main"].metadata.author == AUTHORS,
            "identified main author metadata mismatch")
    require(readers["supplement"].metadata.author == AUTHORS,
            "identified supplement author metadata mismatch")
    require(readers["supplement_anonymous"].metadata.author == "Anonymous",
            "anonymous supplement author metadata mismatch")
    anonymous_text = "\n".join(
        page.extract_text() or "" for page in readers["anonymous"].pages
    )
    for leak in (
        "whzy3185", "e365e155", "Yicheng Zhao", "Jiachen Li",
        "2023213805", "2023213809", "0009-0003", "0009-0006",
    ):
        require(leak not in anonymous_text, f"anonymous PDF leak: {leak}")
    anonymous_supp_text = "\n".join(
        page.extract_text() or ""
        for page in readers["supplement_anonymous"].pages
    )
    for leak in ("whzy3185", "e365e155", "target-a-task59", "verify_target_a"):
        require(leak not in anonymous_supp_text,
                f"anonymous supplement leak: {leak}")
    require(all(len(reader.pages) > 0 for reader in readers.values()),
            "empty PDF")
    return {name: len(reader.pages) for name, reader in readers.items()}


def log_audit() -> None:
    logs = list(MAIN.glob("*.log")) + list(SUPP.glob("*.log"))
    for path in logs:
        text = path.read_text(encoding="utf-8", errors="replace")
        require(not re.search(
            r"(LaTeX|Package .*|Overfull|Underfull).*Warning|undefined|multiply defined",
            text, re.I
        ), f"LaTeX warning remains in {path.name}")


def run_full_exact_chain() -> float:
    start = time.monotonic()
    for path in EXACT_VERIFIERS:
        subprocess.run([sys.executable, path], cwd=REPO, check=True)
    subprocess.run(
        [sys.executable, "-m", "pytest", "-q", *FOCUSED_TESTS],
        cwd=REPO, check=True
    )
    return time.monotonic() - start


def verify(*, full: bool = False, require_tag: bool = False) -> dict[str, object]:
    source = source_audit()
    manifest = manifest_audit(require_tag)
    pages = pdf_audit()
    log_audit()
    require(git_tree("research/paper/manuscript_tex_pub") == FROZEN_ENGLISH,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == FROZEN_CHINESE,
            "historical Chinese manuscript changed")
    runtime = run_full_exact_chain() if full else 0.0
    return {
        **source,
        **manifest,
        "pages": pages,
        "full_runtime_seconds": runtime,
        "verdict": "SUBMISSION_READY_MODULO_SUBMITTER_DESIGNATION_AND_ARCHIVE",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--full", action="store_true",
                        help="run every proof-grade verifier and focused test")
    parser.add_argument("--require-tag", action="store_true",
                        help="require the submission tag to resolve")
    args = parser.parse_args()
    result = verify(full=args.full, require_tag=args.require_tag)
    print(
        "TARGET_A_SUBMISSION_PASS "
        f"pages={result['pages']} labels={result['labels']} "
        f"citations={result['citations']} families={result['families']} "
        f"certificates={result['certificates']} "
        f"full_runtime_seconds={result['full_runtime_seconds']:.2f} "
        f"verdict={result['verdict']}"
    )
