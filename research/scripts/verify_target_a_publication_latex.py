"""Verify the publication-grade Target A LaTeX source and build artifacts."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from build_target_a_publication_latex import FROZEN_SHA256, PUB_DIR, verify_frozen_source


class PublicationLatexVerificationError(RuntimeError):
    pass


def check(condition: bool, message: str) -> None:
    if not condition:
        raise PublicationLatexVerificationError(message)


def source_files() -> list[Path]:
    return sorted(path for path in PUB_DIR.rglob("*.tex") if "build" not in path.parts)


def environment_bodies(text: str, environment: str) -> list[str]:
    return re.findall(
        rf"\\begin\{{{environment}\}}(?:\[[^]]*\])?(.*?)\\end\{{{environment}\}}",
        text,
        flags=re.DOTALL,
    )


def verify_lists(text: str) -> None:
    for environment in ("itemize", "enumerate", "description"):
        check(
            text.count(rf"\begin{{{environment}}}") == text.count(rf"\end{{{environment}}}"),
            f"UNBALANCED_LIST:{environment}",
        )
    check(
        not re.search(r"\\end\{itemize\}[ \t]*\n[ \t]+[a-z][a-z-]+\s", text),
        "BROKEN_LIST_TRAILING_FRAGMENT",
    )
    adjacent_singletons = re.search(
        r"\\begin\{itemize\}\s*\\item[^\\]*\\end\{itemize\}\s*"
        r"\\begin\{itemize\}\s*\\item",
        text,
        flags=re.DOTALL,
    )
    check(not adjacent_singletons, "BROKEN_LIST_ADJACENT_SINGLETONS")
    for itemized in environment_bodies(text, "itemize"):
        check(itemized.count(r"\item") != 1, "BROKEN_LIST_SINGLETON")


def verify_publication_latex() -> None:
    verify_frozen_source()
    check(PUB_DIR.is_dir(), "PUBLICATION_TREE_MISSING")
    files = source_files()
    check(files, "PUBLICATION_TEX_MISSING")
    combined = "\n".join(path.read_text(encoding="utf-8") for path in files)
    body_files = [
        path for path in files if path.parent.name in {"sections", "appendices"}
    ]
    body = "\n".join(path.read_text(encoding="utf-8") for path in body_files)
    readme = (PUB_DIR / "README.md").read_text(encoding="utf-8")

    check(r"\sloppy" not in combined, "SLOPPY_FORBIDDEN")
    check(r"\tableofcontents" not in combined, "TOC_FORBIDDEN")
    check(not re.search(r"\\textbf\{(?:Theorem|Lemma|Proposition)", combined), "BOLD_THEOREM_FORBIDDEN")
    check(not re.search(r"\*\*(?:Theorem|Lemma|Proposition|Proof)", combined), "MARKDOWN_STATEMENT_RESIDUE")
    check(not re.search(r"\((?:[A-Z]|\d+)\.\d+\)", body), "MANUAL_EQUATION_NUMBER")
    check(not re.search(r"(?:^|\s)(?:/Users/|/absolute/|/tmp/|file://)", combined), "LOCAL_ABSOLUTE_PATH")
    check(not re.search(r"\bTask\s+\d+\b", body), "TASK_ID_IN_MANUSCRIPT")
    check(r"|\lvert" not in body and r"\rvert|" not in body, "CORRUPTED_NORM_DELIMITERS")
    check(readme.startswith("# Target A publication LaTeX\n\n"), "README_HEADER")
    check('"' not in readme, "README_STRING_LITERAL_RESIDUE")
    check("main_anonymous.tex" in readme and "body.tex" in readme, "README_ENTRYPOINTS")

    listings = environment_bodies(combined, "lstlisting")
    check(len(listings) == 6, f"SHELL_LISTING_COUNT:{len(listings)}")
    for listing in listings:
        check(
            not re.search(r"(?:sqrt\(|rho\(|eta=|direct_sum|product_|==>|<=|>=)", listing),
            "MATH_IN_LISTING",
        )

    displays = "\n".join(environment_bodies(body, "equation"))
    pseudo_math = r"(?:sqrt\(|(?<!\\)rho\(|(?<!\\)eta=|direct_sum|product_|(?<!\\)sum_|==>|<=|>=|emptyset)"
    check(not re.search(pseudo_math, displays), "ASCII_PSEUDO_MATH_IN_DISPLAY")

    theorem_bodies: list[str] = []
    for environment in ("theorem", "proposition", "lemma", "corollary"):
        theorem_bodies.extend(environment_bodies(body, environment))
    check(len(environment_bodies(body, "theorem")) == 6, "MAIN_THEOREM_COUNT")
    check(all(r"\label{" in theorem for theorem in theorem_bodies), "UNLABELED_THEOREM_ENVIRONMENT")
    check(len(environment_bodies(body, "proof")) >= 6, "PROOF_ENVIRONMENTS_MISSING")

    tables = environment_bodies(body, "table")
    check(len(tables) >= 10, "TABLE_COUNT_TOO_SMALL")
    check(all(r"\caption{" in table and r"\label{tab:" in table for table in tables), "TABLE_METADATA_MISSING")
    verify_lists(body)

    labels = set(re.findall(r"\\label\{([^}]+)\}", combined))
    refs = set(re.findall(r"\\(?:ref|eqref|cref|Cref)\{([^}]+)\}", combined))
    check(refs <= labels, f"UNRESOLVED_SOURCE_REFS:{sorted(refs - labels)}")
    check(len(labels) == len(re.findall(r"\\label\{([^}]+)\}", combined)), "DUPLICATE_LABELS")

    bib = (PUB_DIR / "references.bib").read_text(encoding="utf-8")
    bib_keys = set(re.findall(r"@[A-Za-z]+\{([^,]+),", bib))
    citations: set[str] = set()
    for citation_group in re.findall(r"\\cite\{([^}]+)\}", combined):
        citations.update(item.strip() for item in citation_group.split(","))
    check(citations <= bib_keys, f"UNRESOLVED_SOURCE_CITATIONS:{sorted(citations - bib_keys)}")

    allowed_sha_files = {
        "10_computational_verification.tex",
        "12_data_code_availability.tex",
        "14_appendix_computation.tex",
    }
    for path in body_files:
        if path.name not in allowed_sha_files:
            check(not re.search(r"\b[0-9a-f]{40}\b", path.read_text(encoding="utf-8")), f"COMMIT_SHA_IN_MATH_BODY:{path.name}")

    audit_path = PUB_DIR / "build_audit.json"
    check(audit_path.is_file(), "BUILD_AUDIT_MISSING")
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    check(audit.get("status") == "TARGET_A_PUBLICATION_BUILDS_PASS", "BUILD_AUDIT_STATUS")
    builds = audit.get("builds", [])
    check({item.get("variant") for item in builds} == {"generic", "anonymous", "jgt", "sidma"}, "BUILD_VARIANTS")
    for item in builds:
        pdf = PUB_DIR / str(item["pdf"])
        check(pdf.is_file() and pdf.read_bytes().startswith(b"%PDF-"), f"PDF_MISSING:{pdf.name}")
        check(hashlib.sha256(pdf.read_bytes()).hexdigest() == item["pdf_sha256"], f"PDF_HASH:{pdf.name}")
        check(item["exit_code"] == 0, f"BUILD_EXIT:{item['variant']}")
        check(item["overfull_boxes"] == 0, f"OVERFULL_BOX:{item['variant']}")
        check(item["undefined_references"] == 0, f"UNDEFINED_REF:{item['variant']}")
        check(item["undefined_citations"] == 0, f"UNDEFINED_CITATION:{item['variant']}")
        check(item["fatal_errors"] == 0, f"FATAL_LATEX:{item['variant']}")

    canonical_digest = hashlib.sha256(
        (PUB_DIR.parent / "manuscript_md" / "TARGET_A_MANUSCRIPT_V2.md").read_bytes()
    ).hexdigest()
    check(canonical_digest == FROZEN_SHA256, "FINAL_FROZEN_HASH")
    print("TARGET_A_PUBLICATION_SOURCE_STRUCTURE_PASS")
    print("TARGET_A_PUBLICATION_THEOREM_PROOF_PASS")
    print("TARGET_A_PUBLICATION_REFERENCE_CITATION_PASS")
    print("TARGET_A_PUBLICATION_TABLE_LIST_PASS")
    print("TARGET_A_PUBLICATION_BUILD_ARTIFACT_PASS")
    print("TARGET_A_PUBLICATION_LATEX_GATE_PASS")


def main() -> None:
    try:
        verify_publication_latex()
    except Exception as error:
        print(f"Target A publication LaTeX verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PUBLICATION_LATEX_GATE_FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
