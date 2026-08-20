"""Verify the Chinese manuscript against the frozen English publication source."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
ENGLISH_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub"
CHINESE_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub_zh"
BODY_PARTS = ("sections", "appendices")
ENVIRONMENTS = (
    "equation",
    "theorem",
    "proposition",
    "lemma",
    "proof",
    "table",
    "lstlisting",
)


class ChineseLatexVerificationError(RuntimeError):
    pass


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ChineseLatexVerificationError(message)


def source_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.tex")
        if not any(part in {"build", "tmp"} for part in path.parts)
    )


def body_text(root: Path) -> str:
    files = [path for path in source_files(root) if path.parent.name in BODY_PARTS]
    return "\n".join(path.read_text(encoding="utf-8") for path in files)


def environment_bodies(text: str, environment: str) -> list[str]:
    return re.findall(
        rf"\\begin\{{{environment}\}}(?:\[[^]]*\])?(.*?)\\end\{{{environment}\}}",
        text,
        flags=re.DOTALL,
    )


def normalized_equation(equation: str) -> str:
    equation = re.sub(r"\\text\{[^{}]*\}", r"\\text{TEXT}", equation)
    equation = equation.replace(r"\\sum", r"\sum")
    equation = re.sub(r"[.,;，。]\s*$", "", equation.strip())
    return re.sub(r"\s+", "", equation)


def citation_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        keys.update(item.strip() for item in group.split(","))
    return keys


def verify_target_a_chinese_latex() -> None:
    check(ENGLISH_DIR.is_dir(), "ENGLISH_PUBLICATION_TREE_MISSING")
    check(CHINESE_DIR.is_dir(), "CHINESE_PUBLICATION_TREE_MISSING")
    english_body = body_text(ENGLISH_DIR)
    chinese_body = body_text(CHINESE_DIR)
    chinese_sources = "\n".join(
        path.read_text(encoding="utf-8") for path in source_files(CHINESE_DIR)
    )

    check(re.search(r"[\u4e00-\u9fff]", chinese_body) is not None, "CHINESE_TEXT_MISSING")
    check(r"\usepackage{xeCJK}" in chinese_sources, "XECJK_MISSING")
    check("Songti SC" in chinese_sources and "STHeiti" in chinese_sources, "CHINESE_FONTS")
    check("a4paper" in chinese_sources, "A4_LAYOUT_MISSING")
    check(r"\sloppy" not in chinese_sources, "SLOPPY_FORBIDDEN")
    check(
        not re.search(r"(?:^|\s)(?:/Users/|/absolute/|/tmp/|file://)", chinese_sources),
        "LOCAL_ABSOLUTE_PATH",
    )

    for environment in ENVIRONMENTS:
        english_items = environment_bodies(english_body, environment)
        chinese_items = environment_bodies(chinese_body, environment)
        check(
            len(english_items) == len(chinese_items),
            f"ENVIRONMENT_COUNT:{environment}:{len(english_items)}:{len(chinese_items)}",
        )

    english_equations = [
        normalized_equation(item) for item in environment_bodies(english_body, "equation")
    ]
    chinese_equations = [
        normalized_equation(item) for item in environment_bodies(chinese_body, "equation")
    ]
    check(english_equations == chinese_equations, "EQUATION_SEQUENCE_CHANGED")
    check(
        environment_bodies(english_body, "lstlisting")
        == environment_bodies(chinese_body, "lstlisting"),
        "CODE_LISTINGS_CHANGED",
    )

    english_labels = set(re.findall(r"\\label\{([^}]+)\}", english_body))
    chinese_labels = set(re.findall(r"\\label\{([^}]+)\}", chinese_body))
    check(english_labels == chinese_labels, "LABEL_SET_CHANGED")
    check(citation_keys(english_body) == citation_keys(chinese_body), "CITATION_SET_CHANGED")
    check(
        (ENGLISH_DIR / "references.bib").read_bytes()
        == (CHINESE_DIR / "references.bib").read_bytes(),
        "BIBLIOGRAPHY_METADATA_CHANGED",
    )

    labels = set(re.findall(r"\\label\{([^}]+)\}", chinese_sources))
    refs = set(re.findall(r"\\(?:ref|eqref|cref|Cref)\{([^}]+)\}", chinese_sources))
    check(refs <= labels, f"UNRESOLVED_SOURCE_REFS:{sorted(refs - labels)}")
    bib_keys = set(
        re.findall(
            r"@[A-Za-z]+\{([^,]+),",
            (CHINESE_DIR / "references.bib").read_text(encoding="utf-8"),
        )
    )
    check(
        citation_keys(chinese_sources) <= bib_keys,
        "UNRESOLVED_SOURCE_CITATIONS",
    )

    audit_path = CHINESE_DIR / "build_audit.json"
    check(audit_path.is_file(), "BUILD_AUDIT_MISSING")
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    check(
        audit.get("status") == "TARGET_A_CHINESE_PUBLICATION_BUILD_PASS",
        "BUILD_AUDIT_STATUS",
    )
    pdf = CHINESE_DIR / str(audit.get("pdf"))
    check(pdf.is_file() and pdf.read_bytes().startswith(b"%PDF-"), "PDF_MISSING")
    check(hashlib.sha256(pdf.read_bytes()).hexdigest() == audit.get("pdf_sha256"), "PDF_HASH")
    check(audit.get("page_format") == "A4", "PDF_PAGE_FORMAT")
    check(audit.get("exit_code") == 0, "BUILD_EXIT")
    check(audit.get("overfull_boxes") == 0, "OVERFULL_BOX")
    check(audit.get("undefined_references") == 0, "UNDEFINED_REFERENCE")
    check(audit.get("undefined_citations") == 0, "UNDEFINED_CITATION")
    check(audit.get("fatal_errors") == 0, "FATAL_LATEX")

    english_pdf_hash = hashlib.sha256((ENGLISH_DIR / "main.pdf").read_bytes()).hexdigest()
    check(audit.get("english_source_pdf_sha256") == english_pdf_hash, "ENGLISH_PDF_CHANGED")

    print("TARGET_A_CHINESE_MATH_STRUCTURE_PASS")
    print("TARGET_A_CHINESE_LABEL_CITATION_PASS")
    print("TARGET_A_CHINESE_LISTING_BIBLIOGRAPHY_PASS")
    print("TARGET_A_CHINESE_BUILD_ARTIFACT_PASS")
    print("TARGET_A_CHINESE_LATEX_GATE_PASS")


def main() -> None:
    try:
        verify_target_a_chinese_latex()
    except Exception as error:
        print(f"Target A Chinese LaTeX verification failed: {error}", file=sys.stderr)
        print("TARGET_A_CHINESE_LATEX_GATE_FAIL")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
