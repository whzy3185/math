"""Fail-closed audit for Task 58.5, Section 2 and Figure 1."""

from __future__ import annotations

import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
SECTION = ROOT / "sections/02_switching_reference.tex"
FIGURE = ROOT / "figures/figure_cycle_switching.tex"
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
    figure = FIGURE.read_text(encoding="ascii")
    c = compact(section)
    require("% TASK58_DRAFT_STUB" not in section, "Section 2 remains stubbed")
    require("% TASK58_DRAFT_STUB" not in figure, "Figure 1 remains stubbed")
    require(section.count(r"\subsection{") == 4, "Section 2 subsection count changed")

    for token in (
        r"a_i'=\varepsilon_ia_i\varepsilon_{i+1}",
        r"b_i'=\varepsilon_ib_i\varepsilon_{i+2}",
        r"\alpha=\prod_{i=0}^{n-1}a_i",
        r"\tau_i=a_ia_{i+1}b_i",
        r"b_{n-2}=\alpha\tau_{n-2}",
        r"b_{n-1}=\alpha\tau_{n-1}",
        r"u_{j+n}=\alphau_j",
        r"Q_i=\tau_i\tau_{i+1}",
        r"(Q,\tau_0,\alpha)",
        r"A_{-\tau}=-DA_\tauD",
        r"H_{-\tau}=DH_\tauD",
    ):
        require(token in c, f"switching/flux formula absent: {token}")
    require("reducedpair\\((Q,\\alpha)\\)representstwoswitchingclasses" in c,
            "two-lift quotient boundary absent")
    require("unsquaredspectraofthetwoliftsarereflectedthroughzero" in c.lower(),
            "unsquared lift boundary absent")

    for token in (
        r"Q_i=-1", r"\alpha=-1", r"\tau_i=(-1)^i",
        r"\rho(A_\tau)^2", r"4\cos^2\frac{\pi}{n}",
        r"4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}",
        r"m_n\leq\rho_-(n)", r"B(\vartheta)^2",
    ):
        require(token in c, f"candidate-attainment formula absent: {token}")

    for token in (
        r"\tau_{i-4}\tau_{i-2}u_{i-4}",
        r"(\tau_{i-3}+\tau_{i-2})u_{i-3}",
        r"u_{i-2}", r"(\tau_{i-2}+\tau_{i-1})u_{i-1}",
        r"4u_i", r"(\tau_{i-1}+\tau_i)u_{i+1}",
        r"u_{i+2}", r"(\tau_i+\tau_{i+1})u_{i+3}",
        r"\tau_i\tau_{i+2}u_{i+4}",
    ):
        require(token in c, f"range-four coefficient absent: {token}")

    require(r"\tau_{\mathrm{ref}}=(+,+,-,+,-,-,+,-)" in c,
            "reference tau word absent")
    require(r"Q_{\mathrm{ref}}=(+,-,-,-,+,-,-,-)" in c,
            "reference Q word absent")
    require(r"4\mathbbZ" in c and r"s+4\mathbbZ" in c, "reference sectors absent")
    require(r"\eta=4+\sqrt{10+2\sqrt5}" in c, "reference edge absent")
    require(r"\sup_{|z|=1}\rho\bigl(A_{\mathrm{ref}}(z)\bigr)^2=\eta<8" in c,
            "reference-edge theorem absent")
    require("equalityoccursonlyat\\(z=1\\)" in c, "unique Bloch maximizer absent")
    require("unperturbedreferencebulk,notanabnormalinterface" in c,
            "gap-four boundary absent")
    require("P(y,c)" not in section and "8\\times8" in section,
            "full quartic printed or fiber dimension absent")
    require("c_6" not in section, "G6 edge leaked into Section 2")
    require(r"\footnote" not in section + figure, "footnotes are forbidden")

    require(r"\begin{tikzpicture}" in figure and r"\end{tikzpicture}" in figure,
            "Figure 1 is not TikZ")
    require(figure.count(r"\begin{scope}") == 2, "Figure 1 must have two panels")
    require(r"\begin{figure}" not in figure and r"\caption" not in figure,
            "Figure source owns a float or caption")
    require("color=" not in figure and "fill=white" in figure,
            "Figure 1 is not monochrome")

    all_tex = "\n".join(path.read_text(encoding="ascii") for path in ROOT.rglob("*.tex"))
    draft_stubs = all_tex.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 27, "draft-stub count exceeds Section 2 baseline")

    reader = PdfReader(ROOT / "main.pdf")
    section_two_page = section_three_page = None
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if section_two_page is None and "Switching Coordinates and the Reference Phase" in text:
            section_two_page = page_number
        if section_three_page is None and "Gaps, Charges, and Translation Sectors" in text:
            section_three_page = page_number
    require(section_two_page is not None and section_three_page is not None,
            "Section 2/3 page anchors absent")
    require(section_three_page - section_two_page <= 4, "Section 2 exceeds page budget")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "subsections": 4,
        "figure_panels": 2,
        "baseline_draft_stubs": 27,
        "draft_stubs": draft_stubs,
        "section_two_page": section_two_page,
        "section_three_page": section_three_page,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK585_SECTION2_VERIFY_PASS "
        f"subsections={result['subsections']} panels={result['figure_panels']} "
        f"pages={result['section_two_page']}..{result['section_three_page']} "
        f"stubs={result['draft_stubs']}/{result['baseline_draft_stubs']}"
    )
