"""Verify the generated Target A LaTeX source tree and PDF artifact."""

from __future__ import annotations

import sys
from pathlib import Path

from build_target_a_latex import APPENDICES, CITATIONS, SECTIONS


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
TEX_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex"


class LatexVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise LatexVerificationError(message)


def verify_latex_tree() -> None:
    main_path = TEX_DIR / "main.tex"
    bib_path = TEX_DIR / "references.bib"
    pdf_path = TEX_DIR / "main.pdf"
    _check(main_path.is_file(), "VERIFY_LATEX_MAIN_MISSING")
    _check(bib_path.is_file(), "VERIFY_LATEX_BIB_MISSING")
    _check(pdf_path.is_file(), "VERIFY_LATEX_PDF_MISSING")
    _check(pdf_path.read_bytes().startswith(b"%PDF-"), "VERIFY_LATEX_PDF_HEADER_FAIL")

    main = main_path.read_text(encoding="utf-8")
    bib = bib_path.read_text(encoding="utf-8")
    for stem in SECTIONS:
        relative = Path("sections") / f"{stem.lower()}.tex"
        _check((TEX_DIR / relative).is_file(), f"VERIFY_LATEX_SECTION_MISSING:{stem}")
        input_name = relative.with_suffix("").as_posix()
        _check(rf"\input{{{input_name}}}" in main, f"VERIFY_LATEX_SECTION_INPUT:{stem}")
    for stem in APPENDICES:
        relative = Path("appendices") / f"{stem.lower()}.tex"
        _check((TEX_DIR / relative).is_file(), f"VERIFY_LATEX_APPENDIX_MISSING:{stem}")
        input_name = relative.with_suffix("").as_posix()
        _check(rf"\input{{{input_name}}}" in main, f"VERIFY_LATEX_APPENDIX_INPUT:{stem}")

    for key in CITATIONS.values():
        _check(rf"\bibitem{{{key}}}" in main, f"VERIFY_LATEX_BIBITEM_MISSING:{key}")
        _check("{" + key + "," in bib, f"VERIFY_LATEX_BIB_ENTRY_MISSING:{key}")

    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((TEX_DIR / "sections").glob("*.tex"))
    )
    for anchor in (
        "Theorem A (smallest counterexample)",
        "Theorem F (low-period frontier)",
        "1561/200",
        "4+sqrt(10+2sqrt(5))",
        "17,929,600",
    ):
        _check(anchor in combined, f"VERIFY_LATEX_CONTENT_MISSING:{anchor}")
    lower = combined.lower()
    for forbidden in ("todo", "proof omitted", "left to the author"):
        _check(forbidden not in lower, f"VERIFY_LATEX_FORBIDDEN:{forbidden}")

    print("TARGET_A_LATEX_SOURCE_TREE_PASS")
    print("TARGET_A_LATEX_BIBLIOGRAPHY_PASS")
    print("TARGET_A_LATEX_CONTENT_PASS")
    print("TARGET_A_LATEX_PDF_ARTIFACT_PASS")


def main() -> None:
    try:
        verify_latex_tree()
    except Exception as error:
        print(f"Target A LaTeX verification failed: {error}", file=sys.stderr)
        print("TARGET_A_LATEX_GATE_FAIL")
        raise SystemExit(1)
    print("TARGET_A_LATEX_GATE_PASS")


if __name__ == "__main__":
    main()
