"""Fail-closed audit for Task 58.8, the single-gap hierarchy."""

from __future__ import annotations

import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
SECTION = ROOT / "sections/05_single_gap.tex"
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
    require("% TASK58_DRAFT_STUB" not in section, "Section 5 remains stubbed")
    require(section.count(r"\subsection{") == 4, "Section 5 subsection count changed")
    for token in (
        r"D_g=\{-4j:j\geq0\}\cup\{g+4j:j\geq0\}",
        r"H_g=A_g^2", r"E(g)=\sup\operatorname{Spec}(H_g)",
        r"E(4)=\eta", r"E(6)=c_6",
        r"\frac{\langlev,H_gv\rangle}{\langlev,v\rangle}=\frac{\|A_gv\|^2}{\|v\|^2}",
        "988671163952541", "125000000000000",
        r">c_6+\frac1{250}",
    ):
        require(token in c, f"single-gap setup absent: {token}")
    require("Gap \\(g=4\\)" in section and "not an abnormal interface" in section,
            "gap-four scope boundary absent")
    require("other \\(\\tau\\)-lift" in section and "reverse orientation" in section,
            "lift/orientation quantifier absent")

    expected_rows = {
        "1": ("812/97", "5598897096603523"),
        "2": ("866/109", "484843129173031"),
        "3": ("3114/393", "702232566651387"),
        "5": ("764/96", "587568260556064"),
        "7": ("768/97", "98897096603523"),
        "8": ("19672/2487", "174815250030533"),
    }
    for gap, (quotient, delta) in expected_rows.items():
        require(f"{gap}&\\({quotient}\\)&\\({delta}\\)" in section,
                f"small-gap row {gap} absent")
    require("Every entry in the last column is positive" in section,
            "small-gap strictness deduction absent")
    require("174815250030533" in section and
            "310875000000000000" in section,
            "minimum exact margin absent")
    require("no outgoing coordinate is omitted" in section,
            "full image-window boundary absent")

    for token in (
        r"v_*=(4,0,7,8,8,9,1,7,3,6,1,4,1,2)",
        r"\|v_*\|^2=391", r"\|A_9v_*\|^2=3102",
        r"\|A_{10}v_*\|^2=3094",
        r"\|A_gv_*\|^2=3094\quad(g\geq11)",
        r"E(g)\geq\frac{3094}{391}=\frac{182}{23}",
        "10563229091557", "2875000000000000",
    ):
        require(token in c, f"large-gap witness fact absent: {token}")
    require("only when \\(g=9\\) or \\(g=10\\)" in section and
            "every \\(g\\geq11\\)" in section,
            "finite-propagation tail partition absent")
    require("notasampleofthosegaps" in c,
            "infinite-tail proof boundary absent")

    for token in (
        r"E(4)=\eta<c_6=E(6)",
        r"E(g)>c_6+\frac1{250}",
    ):
        require(token in c, f"hierarchy theorem formula absent: {token}")
    require("For both \\(\\tau\\)-lifts and both interface orientations" in section,
            "theorem quantifier absent")
    require("uniquely minimizes the squared spectral edge among abnormal positive" in section,
            "single-gap uniqueness absent")
    require("makesnoclaimaboutarbitrarymulti-gapconfigurations" in c,
            "multi-gap nonclaim absent")
    require("no optimality is claimed for the size of that margin" in section,
            "margin-optimality nonclaim absent")
    for forbidden in ("A.4", "A.5", "A.6", "computer search shows"):
        require(forbidden not in section, f"forbidden Section 5 content: {forbidden}")
    require(r"\footnote" not in section, "footnotes are forbidden")

    all_tex = "\n".join(path.read_text(encoding="ascii") for path in ROOT.rglob("*.tex"))
    draft_stubs = all_tex.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 16, "draft-stub count exceeds Section 5 baseline")
    reader = PdfReader(ROOT / "main.pdf")
    section_five_page = section_six_page = None
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if section_five_page is None and "Optimality Among Single-Gap Interfaces" in text:
            section_five_page = page_number
        if section_six_page is None and "Phase Slips on Finite Rings" in text:
            section_six_page = page_number
    require(section_five_page is not None and section_six_page is not None,
            "Section 5/6 page anchors absent")
    require(section_six_page - section_five_page <= 3, "Section 5 exceeds page budget")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "subsections": 4,
        "small_gap_rows": 6,
        "baseline_draft_stubs": 16,
        "draft_stubs": draft_stubs,
        "section_five_page": section_five_page,
        "section_six_page": section_six_page,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK588_SECTION5_VERIFY_PASS "
        f"subsections={result['subsections']} rows={result['small_gap_rows']} "
        f"pages={result['section_five_page']}..{result['section_six_page']} "
        f"stubs={result['draft_stubs']}/{result['baseline_draft_stubs']}"
    )
