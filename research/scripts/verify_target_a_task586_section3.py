"""Fail-closed audit for Task 58.6, the gap/charge/sector section."""

from __future__ import annotations

import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
SECTION = ROOT / "sections/03_gaps_charges_sectors.tex"
ENGLISH_TREE = "59e3a8f73a152ef06f994e979b7219a3365efeae"
CHINESE_TREE = "57ae03fb5b90866f84d0d72b414008678e8f5004"


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


def verify() -> dict[str, int | bool]:
    section = SECTION.read_text(encoding="ascii")
    c = compact(section)
    lower = section.lower()
    require("% TASK58_DRAFT_STUB" not in section, "Section 3 remains stubbed")
    require(section.count(r"\subsection{") == 3, "Section 3 subsection count changed")
    for token in (
        r"D(Q)=\{i\in\mathbbZ/n\mathbbZ:Q_i=+1\}",
        r"g_j=x_{j+1}-x_j", r"q_j=g_j-4",
        r"\sum_{j=1}^dg_j=n", r"\sum_{j=1}^dq_j=n-4d",
        r"\prod_{i=0}^{n-1}Q_i=(-1)^{n-d}",
        r"\sum_{j=1}^dq_j\equivn\pmod8",
    ):
        require(token in c, f"gap/charge formula absent: {token}")
    require("since\\(n\\)iseven,\\(d\\)iseven" in c,
            "even-order liftability implication absent")
    require(r"D(Q)=\varnothing" in c and "nocyclicgaplist" in c,
            "defect-free boundary absent")
    require("Hamiltonholonomy\\(\\alpha\\)doesnotoccurinthisargument" in c,
            "holonomy independence absent")

    for token in (
        r"(B_s)_i=+1\quad\Longleftrightarrow\quadi\equivs\pmod4",
        r"\sigma_{\mathrm{sec}}(q)=q\pmod4",
        r"B_{s+\sigma_{\mathrm{sec}}(q)}",
        r"\sigma_{\mathrm{sec}}(q_1+\cdots+q_k)",
        r"\sum_jq_j\equivn\pmod4",
    ):
        require(token in c, f"sector formula absent: {token}")
    sector_position = section.index(r"\sigma_{\mathrm{sec}}(q)=q\pmod4")
    composition_position = section.index(r"\subsection{Composition")
    preview_position = section.index("For later use, a gap of length six")
    require(sector_position < composition_position < preview_position,
            "sector law must precede composition and G6 preview")
    require(
        "The modulo-eight charge closure and the modulo-four translation-sector law"
        in section,
        "explicit mod-eight/mod-four distinction absent",
    )
    require("encode different constraints and will be used separately" in section,
            "separate-use sentence absent")
    require("total charges\n\\(2,4,6\\)" in section and "sector shifts \\(2,0,2\\)" in section,
            "one/two/three gap preview absent")
    require("No spectral comparison is asserted at this stage." in section,
            "G6 scope boundary absent")
    for forbidden in ("transfer matrix", "evans", "spectrally optimal", "c_6"):
        require(forbidden not in lower, f"forbidden Section 3 content: {forbidden}")
    require(r"\footnote" not in section, "footnotes are forbidden")

    all_tex = "\n".join(path.read_text(encoding="ascii") for path in ROOT.rglob("*.tex"))
    draft_stubs = all_tex.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 24, "draft-stub count exceeds Section 3 baseline")

    reader = PdfReader(ROOT / "main.pdf")
    section_three_page = section_four_page = None
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if section_three_page is None and "Gaps, Charges, and Translation Sectors" in text:
            section_three_page = page_number
        if section_four_page is None and "The Elementary Six-Gap Phase Slip" in text:
            section_four_page = page_number
    require(section_three_page is not None and section_four_page is not None,
            "Section 3/4 page anchors absent")
    require(section_four_page - section_three_page <= 2, "Section 3 is no longer short")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "subsections": 3,
        "baseline_draft_stubs": 24,
        "draft_stubs": draft_stubs,
        "section_three_page": section_three_page,
        "section_four_page": section_four_page,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK586_SECTION3_VERIFY_PASS "
        f"subsections={result['subsections']} "
        f"pages={result['section_three_page']}..{result['section_four_page']} "
        f"stubs={result['draft_stubs']}/{result['baseline_draft_stubs']}"
    )
