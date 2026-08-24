"""Fail-closed audit for Task 58.7, the elementary G6 proof."""

from __future__ import annotations

import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
CONTROL = REPO / "research/paper/task58"
SECTION = ROOT / "sections/04_elementary_g6.tex"
SPLIT = CONTROL / "TASK58_G6_MAIN_APPENDIX_SPLIT.md"
THEOREM_MAP = CONTROL / "TASK58_THEOREM_TO_SECTION_MAP.md"
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
    split = SPLIT.read_text(encoding="ascii")
    theorem_map = THEOREM_MAP.read_text(encoding="ascii")
    c = compact(section)
    lower = section.lower()
    require("% TASK58_DRAFT_STUB" not in section, "Section 4 remains stubbed")
    require(section.count(r"\subsection{") == 4, "Section 4 subsection count changed")

    for token in (
        r"D_6=\{-4j:j\geq0\}\cup\{6+4j:j\geq0\}",
        r"Q_i^{(6)}=+1", r"H_6=A_6^2", r"\|A_6\|\leq4",
        r"0\leqH_6\leq16I",
        r"\operatorname{Spec}_{\mathrm{ess}}(H_6)=\operatorname{Spec}(H_{\mathrm{ref}})",
        r"\sup\operatorname{Spec}_{\mathrm{ess}}(H_6)=\eta",
    ):
        require(token in c, f"operator/essential formula absent: {token}")
    require("Weyl's criterion" in section and "Fredholm" in section,
            "both half-line essential-spectrum inclusions are not visible")
    require("isolated eigenvalue\nof finite multiplicity" in section,
            "discreteness above eta absent")
    require(r"u_\pm=\frac12\left(u\pm\lambda^{-1}A_6u\right)" in c,
            "H-to-A branch decomposition absent")
    require("two multipliers inside and\ntwo outside the unit circle" in section,
            "2+2 hyperbolic split absent")
    require("exponential decay" in section and "individual sites" in section,
            "tail localization bridge absent")

    for token in (
        "16y^{10}", "-520y^9", "-19968y+256",
        "7905369311620327", "7905369311620328",
        r"D_6(\lambda)U_L(\lambda)\capS_R(\lambda)\neq\{0\}",
        r"E_6(\lambda)=\det[D_6(\lambda)u_1,D_6(\lambda)u_2,s_1,s_2]=0",
        r"+\sqrt{c_6}\in\operatorname{Spec}(A_6)",
        r"c_6\in\operatorname{Spec}(H_6)",
    ):
        require(token in c, f"physical-matching formula absent: {token}")
    interval_position = section.index("7905369311620327")
    decimal_position = section.index("7.905369311620327")
    require(interval_position < decimal_position, "c6 is oriented by decimal before exact definition")
    existence_position = section.index("opposite endpoint signs")
    elimination_position = section.index("To identify its square")
    require(existence_position < elimination_position,
            "physical existence must precede algebraic identification")
    require("an elimination\nroot is not declared physical" in section,
            "resultant/physical boundary absent")
    require("adjugate would vanish" in section and "positive eigenspace" in section,
            "simple-zero to simple-eigenspace bridge absent")

    for phrase in (
        "complete finite list of algebraic candidate intervals",
        "genuine unsquared determinant is bounded away\nfrom zero",
        "second coordinate reconstruction",
        "chart transitions and the sole repeated\nmultiplier",
        "no\nfloating-point sign is used",
    ):
        require(phrase in section, f"candidate-completeness boundary absent: {phrase}")
    require(r"\sup\operatorname{Spec}(H_6)=c_6" in c, "global G6 edge absent")

    for token in (
        r"Q_{6-i}^{(6)}=Q_i^{(6)}",
        r"\tau_{7-i}^{(6)}=-\tau_i^{(6)}",
        r"(Ku)_i=(-1)^iu_{9-i}",
        r"K^2=-I", r"KA_6=-A_6K", r"KH_6=H_6K",
        r"\dim\ker(H_6-c_6)=2",
    ):
        require(token in c, f"rank-two symmetry formula absent: {token}")
    require("Both summands are one-dimensional" in section,
            "simple unsquared partner deduction absent")
    require("it is not simple" in section and "rank two" in section,
            "squared multiplicity boundary absent")
    for forbidden in ("kramers", "simple eigenvalue of \\(h_6\\)", "resultant proves"):
        require(forbidden not in lower, f"forbidden G6 wording: {forbidden}")

    for heading in (
        "Section 4: material that stays in the main text",
        "Appendix A: exact mathematical certification",
        "Separate reproducibility supplement",
        "Mandatory logic gates",
    ):
        require(heading in split, f"G6 split heading absent: {heading}")
    for gate in ("Existence framework", "Discreteness", "Realization", "Maximality", "Rank two"):
        require(gate in split, f"G6 logic gate absent: {gate}")
    require("resultant proves" in split.lower() and "forbidden" in split.lower(),
            "resultant shortcut is not prohibited")
    quote = chr(96)
    for claim in ("T4.0", "T4.1", "T4.2"):
        line = next(line for line in theorem_map.splitlines()
                    if quote + claim + quote in line)
        require(quote + "App A" + quote in line and quote + "App B" + quote not in line,
                f"{claim} appendix placement is inconsistent")

    all_tex = "\n".join(path.read_text(encoding="ascii") for path in ROOT.rglob("*.tex"))
    draft_stubs = all_tex.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 20, "draft-stub count exceeds Section 4 baseline")
    reader = PdfReader(ROOT / "main.pdf")
    section_four_page = section_five_page = None
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if section_four_page is None and "The Elementary Six-Gap Phase Slip" in text:
            section_four_page = page_number
        if section_five_page is None and "Optimality Among Single-Gap Interfaces" in text:
            section_five_page = page_number
    require(section_four_page is not None and section_five_page is not None,
            "Section 4/5 page anchors absent")
    require(section_five_page - section_four_page <= 6, "Section 4 exceeds page budget")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "subsections": 4,
        "logic_gates": 5,
        "baseline_draft_stubs": 20,
        "draft_stubs": draft_stubs,
        "section_four_page": section_four_page,
        "section_five_page": section_five_page,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK587_SECTION4_VERIFY_PASS "
        f"subsections={result['subsections']} gates={result['logic_gates']} "
        f"pages={result['section_four_page']}..{result['section_five_page']} "
        f"stubs={result['draft_stubs']}/{result['baseline_draft_stubs']}"
    )
