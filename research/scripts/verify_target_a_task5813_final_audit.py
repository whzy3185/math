"""Fail-closed final audit for the Task 58 submission package."""

from __future__ import annotations

import re
import subprocess
from collections import Counter
from pathlib import Path

from pypdf import PdfReader

from verify_target_a_task5812_hostile_review import verify as verify_hostile


REPO = Path(__file__).resolve().parents[2]
MAIN = REPO / "research/paper/manuscript_tex_task58"
SUPP = REPO / "research/paper/manuscript_tex_task58_supplement"
CONTROL = REPO / "research/paper/task58"
FINAL_AUDIT = CONTROL / "TASK58_FINAL_MANUSCRIPT_AUDIT.md"
COVER_FACTS = CONTROL / "TASK58_COVER_LETTER_FACTS.md"
HANDOFF = CONTROL / "TASK58_HANDOFF.md"
ENGLISH_TREE = "59e3a8f73a152ef06f994e979b7219a3365efeae"
CHINESE_TREE = "57ae03fb5b90866f84d0d72b414008678e8f5004"
VALIDITY = "8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def compact(text: str) -> str:
    return "".join(text.split())


def git_tree(path: str) -> str:
    output = subprocess.check_output(
        ["git", "ls-tree", "HEAD", path], cwd=REPO, text=True
    ).strip()
    require(output, f"missing frozen tree: {path}")
    return output.split()[2]


def verify() -> dict[str, int | bool | str]:
    hostile = verify_hostile()
    require(hostile["open_major"] == 0, "hostile review not closed")
    for path in (FINAL_AUDIT, COVER_FACTS, HANDOFF):
        require(path.is_file() and len(path.read_text(encoding="ascii")) > 1000,
                f"final deliverable missing or stubbed: {path.name}")
    final_audit = FINAL_AUDIT.read_text(encoding="ascii")
    cover = COVER_FACTS.read_text(encoding="ascii")
    handoff = HANDOFF.read_text(encoding="ascii")
    require("ANONYMOUS_REVIEW_PACKAGE_READY" in final_audit and
            "ANONYMOUS_REVIEW_PACKAGE_READY" in handoff,
            "truthful package status absent")

    tex_paths = list(MAIN.rglob("*.tex"))
    main_tex = "\n".join(path.read_text(encoding="ascii") for path in tex_paths)
    supp_tex = "\n".join(path.read_text(encoding="ascii") for path in SUPP.rglob("*.tex"))
    front = (MAIN / "frontmatter.tex").read_text(encoding="ascii")
    intro = (MAIN / "sections/01_introduction.tex").read_text(encoding="ascii")
    conclusion = (MAIN / "sections/08_concluding.tex").read_text(encoding="ascii")
    for source in (front, intro, conclusion, cover, final_audit):
        c = compact(source)
        require("32" in source and "40" in source and
                (r"n\geq48" in c or "n>=48" in c),
                "classification failure set is inconsistent")
    require(VALIDITY in compact(front), "abstract validity set absent")
    require(VALIDITY in compact(intro), "Introduction validity set absent")
    require(VALIDITY in compact(cover), "cover-facts validity set absent")
    conclusion_compact = compact(conclusion)
    require("n=32" in conclusion_compact and "onsetat$48$" in conclusion_compact,
            "Conclusion first-failure/onset distinction absent")

    labels = re.findall(r"\\label\{([^}]+)\}", main_tex)
    refs = re.findall(r"\\(?:ref|eqref|cref|Cref)\{([^}]+)\}", main_tex)
    require(not [key for key, count in Counter(labels).items() if count > 1],
            "duplicate labels remain")
    require(set(refs) <= set(labels), "undefined references remain")
    bib = (MAIN / "references.bib").read_text(encoding="ascii")
    keys = re.findall(r"@\w+\{([^,]+),", bib)
    citation_groups = re.findall(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}", main_tex)
    citations = {key.strip() for group in citation_groups for key in group.split(",")}
    require(citations <= set(keys), "undefined citation remains")
    require(not [key for key, count in Counter(keys).items() if count > 1],
            "duplicate bibliography key remains")
    dois = [doi.lower() for doi in re.findall(r"doi\s*=\s*\{([^}]+)\}", bib, re.I)]
    require(not [doi for doi, count in Counter(dois).items() if count > 1],
            "duplicate DOI remains")
    require("Suvagiya2026Signed" in citations, "direct predecessor is not cited")

    all_source = main_tex + "\n" + supp_tex
    for marker in (
        "TASK58_DRAFT_STUB", "TODO", "TBD", "FIXME", "PLACEHOLDER",
        "Lorem", "proof to be added",
    ):
        require(marker.lower() not in all_source.lower(),
                f"final source marker remains: {marker}")
    require(r"\footnote" not in main_tex, "main-paper author footnote remains")
    require(re.search(r"(?<!\\)qquad", supp_tex) is None,
            "literal qquad remains")
    for stale in (
        "exact-r cluster", "codimension-r complement", "r x r Feshbach",
        "rank-one squared", "common liminf theorem", "p<=24",
    ):
        require(stale.lower() not in all_source.lower(), f"active stale phrase: {stale}")

    main_reader = PdfReader(MAIN / "main.pdf")
    anonymous_reader = PdfReader(MAIN / "main_anonymous.pdf")
    supp_reader = PdfReader(SUPP / "main.pdf")
    require((len(main_reader.pages), len(anonymous_reader.pages), len(supp_reader.pages))
            == (38, 38, 13), "final page inventory changed")
    require(main_reader.metadata.title ==
            "Spectral Radius Minimization for Signed Squares of Cycles",
            "main PDF title metadata absent")
    require(anonymous_reader.metadata.author == "Anonymous",
            "anonymous PDF author metadata wrong")
    anonymous_text = "\n".join(page.extract_text() or "" for page in anonymous_reader.pages)
    require("whzy3185" not in anonymous_text and "e365e155" not in anonymous_text,
            "anonymous PDF leaks identity")

    manifest = (SUPP / "sections/03_reproducibility.tex").read_text(encoding="ascii")
    path_matches = sorted(set(re.findall(r"research/[A-Za-z0-9_./-]+", supp_tex)))
    require(path_matches, "supplement artifact manifest absent")
    for raw_path in path_matches:
        require((REPO / raw_path.rstrip(".,;:")).exists(),
                f"supplement artifact does not exist: {raw_path}")
    require(re.search(r"(?m)^python3 research/scripts/test_", manifest) is None,
            "pytest file still invoked as plain script")

    for phrase in (
        "Abstract | 153 source words", "Main-text figures | 3",
        "Duplicate labels: 0", "Undefined references: 0",
        "Undefined citations: 0", "IMMUTABLE_ARCHIVE_PENDING",
        "PENDING_USER_METADATA", "final submission audit",
    ):
        require(phrase in final_audit, f"final audit fact absent: {phrase}")
    for phrase in (
        "Mathematical problem", "Direct prior art", "Complete classification",
        "Structural contribution", "Computer-assisted disclosure",
        "Submission package",
    ):
        require(phrase in cover, f"cover-letter fact section absent: {phrase}")
    for path_text in (
        "research/paper/manuscript_tex_task58/main.tex",
        "research/paper/manuscript_tex_task58/main.pdf",
        "research/paper/manuscript_tex_task58/main_anonymous.pdf",
        "research/paper/manuscript_tex_task58/references.bib",
        "research/paper/manuscript_tex_task58_supplement/main.pdf",
    ):
        require(path_text in handoff and (REPO / path_text).exists(),
                f"handoff path absent: {path_text}")
    require("Pull request: none" in handoff and "No PR was created" in handoff,
            "no-PR contract absent")
    require("PENDING_USER_METADATA" in final_audit and
            "IMMUTABLE_ARCHIVE_PENDING" in final_audit,
            "external metadata limitations are hidden")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "main_pages": 38,
        "anonymous_pages": 38,
        "supplement_pages": 13,
        "labels": len(labels),
        "citations": len(citations),
        "figures": 3,
        "stubs": 0,
        "footnotes": 0,
        "archive_status": "IMMUTABLE_ARCHIVE_PENDING",
        "author_metadata": "PENDING_USER_METADATA",
        "verdict": "ANONYMOUS_REVIEW_PACKAGE_READY",
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK5813_FINAL_AUDIT_PASS "
        f"main={result['main_pages']} anonymous={result['anonymous_pages']} "
        f"supplement={result['supplement_pages']} labels={result['labels']} "
        f"citations={result['citations']} figures={result['figures']} "
        f"stubs={result['stubs']} footnotes={result['footnotes']} "
        f"archive={result['archive_status']} author={result['author_metadata']} "
        f"verdict={result['verdict']}"
    )
