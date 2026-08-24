"""Fail-closed audit for Task 58.9, finite-ring phase slips."""

from __future__ import annotations

import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
CONTROL = REPO / "research/paper/task58"
SECTION = ROOT / "sections/06_finite_rings.tex"
FIGURE2 = ROOT / "figures/figure_reference_slips.tex"
FIGURE3 = ROOT / "figures/figure_patch_localization.tex"
DECISION = CONTROL / "TASK58_EXACT2R_LENGTH_DECISION.md"
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
    decision = DECISION.read_text(encoding="ascii")
    figure2 = FIGURE2.read_text(encoding="ascii")
    figure3 = FIGURE3.read_text(encoding="ascii")
    require("% TASK58_DRAFT_STUB" not in section, "Section 6 remains stubbed")
    require(section.count(r"\subsection{") == 5, "Section 6 subsection count changed")

    for token in (
        r"\mathcalG_2(k)=[6,4^{\,2k-1}]",
        r"\mathcalG_4(k)=[6,4^{\,k-1},6,4^{\,k-1}]",
        r"\mathcalG_6(k)=[6,4^a,6,4^b,6,4^c]",
        r"D_2(n)=n", r"D_4(n)=n/2",
        r"D_6(n)=6+4\left\lfloor\frac{2k-3}{3}\right\rfloor",
        r"\prod_iQ_i=(-1)^{n-2k}=1",
    ):
        require(token in c, f"residue construction absent: {token}")
    require("both cyclic \\(\\tau\\)-lifts exist" in section,
            "two cyclic lifts are not covered")
    require("mod-eight charge check is separate" in section and
            "translation-sector check" in section,
            "charge/sector legality checks are conflated")
    require("either Hamilton holonomy \\(\\alpha=\\pm1\\)" in section,
            "both holonomies absent")
    require("exponents are nonnegative" in section, "residue exponent boundary absent")

    for token in (
        r"2(R+4)<D",
        "both \\(\\tau\\)-lifts", "both interface orientations",
        "both Hamilton\nholonomies", "cyclic wraparound", "proper arc",
        "Unwrapping a\nproper arc", "Move it outside every interface support",
    ):
        require(token in section or token in c, f"patch coverage absent: {token}")
    require("measured in ring sites, not period-eight cells" in section,
            "core-separation units absent")
    require("equality of all coefficients needed by the range-four quadratic form" in section,
            "patch equality is too weak")

    for token in (
        r"H=\sum_j\chi_jH\chi_j+\frac12\sum_j[\chi_j,[\chi_j,H]]",
        r"C_R=\sum_kf_R(k)^2=\frac{2R^2+1}{3R}",
        r"S_d(R):=\sum_j(\chi_j(a)-\chi_j(b))^2",
        r"\frac{240R-342}{R(2R^2+1)}",
        r"\leq\frac{120}{R^2}",
        r"\rho(A)^2\leqc_6+\frac{240R-342}{R(2R^2+1)}",
    ):
        require(token in c, f"IMS formula absent: {token}")
    require("uniform operator-norm estimate" in section,
            "IMS remainder is misstated as an attained error")
    require("controls the full finite-ring spectral top" in section,
            "IMS cap scope absent")

    require(r"\limsup_{k\to\infty}m_{8k+s}^2\leqc_6" in c,
            "residue limsup absent")
    require("neither a lower bound nor a limit or common liminf" in section,
            "limsup nonclaim absent")
    for token in (
        r"\theta_n>8-\frac{200}{n^2}",
        "240&\\(1561/200\\)&\\(2303/288\\)",
        "242&\\(257368059342729114019/32519875000000000000\\)",
        "244&\\(14532080076773342617/1829625000000000000\\)",
        "246&\\(2591140328128938813/324125000000000000\\)",
        r"\mathcalE(R)-\mathcalE(R+1)",
        r"m_n<\rho_-(n)",
        r"\text{foreveryeven}n\geq240",
    ):
        require(token in c, f"analytic-tail fact absent: {token}")
    require("donotdecrease" in c and "strictlyincreases" in c,
            "residue monotonicity boundary absent")
    require("exact-\\(2r\\) count nor the rank-two multiplicity is used" in section,
            "analytic tail depends on structural refinement")
    require("does not locate the sharp beginning at \\(48\\)" in section,
            "eventual-tail/onset boundary absent")

    require(section.count(r"\begin{theorem}") == 1,
            "Section 6 must contain one exact-2r theorem")
    for token in (
        r"r\in\{1,2,3\}", r"D\geq1040",
        r"\mathbf1_{[c_6-1/400,\,c_6+1/400]}(H)=2r",
    ):
        require(token in c, f"exact-2r overview fact absent: {token}")
    require("either \\(\\tau\\)-lift, either orientations, and either" in section,
            "exact-2r scope incomplete")
    require("counted with multiplicity; no individual simplicity" in section,
            "exact-2r multiplicity boundary absent")
    require("not used in\nProposition" in section and "onset of continuous failure at \\(48\\)" in section,
            "exact-2r nondependency absent")
    for forbidden in ("3505", "9/25", "N_{\\exp}", "Feshbach", "Schur-complement"):
        require(forbidden not in section, f"supplement-only exact-2r detail leaked: {forbidden}")

    for figure in (figure2, figure3):
        require("% TASK58_DRAFT_STUB" not in figure, "Figure 2 or 3 remains stubbed")
        require(r"\begin{tikzpicture}" in figure and r"\begin{figure}" not in figure,
                "Figure 2/3 source ownership wrong")
        require("rounded corners" not in figure, "decorative text box remains in Figure 2/3")
    require("mod8" in figure2 and "q_{\\rm tot}" in figure2,
            "Figure 2 charge/sector content absent")
    for phrase in ("interface core", "enlarged support", "seam outside support",
                   "identified infinite G6 line patch"):
        require(phrase in figure3, f"Figure 3 label absent: {phrase}")

    for phrase in (
        "one theorem statement", "one proof-overview paragraph",
        "rank two", "2r", "not used", "onset",
        "Projected essential paper             34--38 pages",
        "no more than 45 pages",
    ):
        require(phrase in decision, f"exact-2r length decision incomplete: {phrase}")

    all_tex = "\n".join(path.read_text(encoding="ascii") for path in ROOT.rglob("*.tex"))
    draft_stubs = all_tex.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 9, "draft-stub count exceeds Section 6 baseline")
    reader = PdfReader(ROOT / "main.pdf")
    section_six_page = section_seven_page = None
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if section_six_page is None and "Phase Slips on Finite Rings" in text:
            section_six_page = page_number
        if section_seven_page is None and "Finite Completion of the Classi" in text:
            section_seven_page = page_number
    require(section_six_page is not None and section_seven_page is not None,
            "Section 6/7 page anchors absent")
    require(section_seven_page - section_six_page <= 5, "Section 6 exceeds page budget")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "subsections": 5,
        "figures": 2,
        "baseline_draft_stubs": 9,
        "draft_stubs": draft_stubs,
        "section_six_page": section_six_page,
        "section_seven_page": section_seven_page,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK589_SECTION6_VERIFY_PASS "
        f"subsections={result['subsections']} figures={result['figures']} "
        f"pages={result['section_six_page']}..{result['section_seven_page']} "
        f"stubs={result['draft_stubs']}/{result['baseline_draft_stubs']}"
    )
