"""Fail-closed audit for Task 58.10, finite completion of the classification."""

from __future__ import annotations

import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
CONTROL = REPO / "research/paper/task58"
SECTION = ROOT / "sections/07_finite_completion.tex"
SPLIT = CONTROL / "TASK58_FINITE_MAIN_APPENDIX_SPLIT.md"
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
    c = compact(section)
    require("% TASK58_DRAFT_STUB" not in section, "Section 7 remains stubbed")
    require(section.count(r"\subsection{") == 5, "Section 7 subsection count changed")
    for phrase in (
        "mathematical reduction", "finite exact object",
        "independent machine verification", "mathematical consequence",
    ):
        require(phrase in section, f"four-stage contract absent: {phrase}")
    for token in (
        r"\rho(A)^2=\lambda_{\max}(A^2)",
        r"pI-qA^2\succ0", r"\rho(A)^2<p/q",
    ):
        require(token in c, f"certificate implication absent: {token}")
    require("Floating-point calculations may suggest" in section and
            "make no accepting decision" in section,
            "floating/exact boundary absent")
    for forbidden in ("JSON", "schema", "hash", "checker CLI", "PASS",
                      "tamper", "terminal_unresolved"):
        require(forbidden not in section, f"implementation detail leaked: {forbidden}")

    for token in (
        r"\rho(A_\sigma)^2\geq\theta_n",
        r"m_n=\rho_-(n)",
        r"1561I_{32}-200A_{32}^2\succ0",
        r"\frac{1561}{200}<\frac{11896117236720419}{1523321182060814}<\theta_{32}",
        r"m_{32}<\rho_-(32)",
    ):
        require(token in c, f"orders 8--32 fact absent: {token}")
    require("candidate-attainment" in section or "candidate attainment" in section,
            "attainment direction absent")
    require("first\nfailing order" in section, "first failure at 32 absent")
    require("reduced \\((Q,\\alpha)\\) quotient" in section and
            "identical squared spectra" in section,
            "safe lift quotient boundary absent")

    for token in (
        r"M_W=C_W^{\mathsfT}C_W=P_SA^2P_S",
        r"v^{\mathsfT}M_Wv>b_n\,v^{\mathsfT}v",
        r"a_nI-M_W\succ0",
        r"b_nI-M_W\not\succ0",
        r"(s,\varepsilon)\longmapsto(s',\varepsilon+b_L)",
        r"\prod_iQ_i=1",
        r"2(1+1+3+7+10+10)=64",
    ):
        require(token in c, f"finite-state completeness fact absent: {token}")
    require("Conversely, reading any liftable cyclic" in section,
            "de Bruijn completeness direction absent")
    require("not a sampled subset" in section, "finite-state domain is presented as sample")
    require("Both holonomies are then checked" in section,
            "both holonomies absent")
    require("no terminal remains unresolved" in section,
            "terminal closure absent")
    for n in ("34", "36", "38", "42", "44", "46"):
        require(n in section, f"recovery order absent: {n}")

    for token in (
        "1000100010001000100010001000100010001000",
        r"15541I_{40}-2000A_{40}^2",
        r"\frac{15541}{2000}<\frac{63}{8}",
        r"m_{40}<\rho_-(40)",
    ):
        require(token in c, f"order-40 witness absent: {token}")
    require("logically separate from the six lower-bound decisions" in section,
            "order-40 boundary absent")

    for token in (
        r"\frac{238-48}{2}+1=96",
        r"t_nI-A_n^2\succ0",
        r"t_n<8-\frac{200}{n^2}",
        r"\rho(A_n)^2<t_n<8-\frac{200}{n^2}<\theta_n",
    ):
        require(token in c, f"96-order bridge fact absent: {token}")
    require("every even order from \\(48\\) through \\(238\\) fails" in section,
            "bridge consequence absent")
    require("rebuilds each full signed matrix" in section and
            "different ordering" in section,
            "independent bridge verification absent")

    require(section.count(r"\bottomrule") >= 1 and "Proof mechanism" in section,
            "classification table absent")
    require(r"m_n<\rho_-(n)" in c and r"n=32,\quadn=40,\quad\text{or}\quadn\geq48" in c,
            "final iff absent")
    require("disjoint union" in section, "exhaustive partition absent")
    require("finite classification determines" in section,
            "finite classification wording absent")
    require("phase-slip argument explains" in section,
            "eventual mechanism wording absent")
    require("continuous onset \\(48\\)" in section and
            "finite bridge together\nwith the analytic tail" in section,
            "sharp onset dependency absent")

    for heading in (
        "Section 7: material that stays in the main text",
        "Appendix B: complete mathematical detail",
        "Separate reproducibility supplement",
        "Mandatory proof boundaries",
    ):
        require(heading in split, f"finite split heading absent: {heading}")
    require("producer search may discover" in split and "Its output is not a proof" in split,
            "producer/proof boundary absent")
    for phrase in ("96-order exact bridge", "64 terminal", "Order 40",
                   "Final disjoint synthesis"):
        require(phrase in split, f"finite split fact absent: {phrase}")

    all_tex = "\n".join(path.read_text(encoding="ascii") for path in ROOT.rglob("*.tex"))
    draft_stubs = all_tex.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 4, "draft-stub count exceeds Section 7 baseline")
    reader = PdfReader(ROOT / "main.pdf")
    section_seven_page = section_eight_page = None
    for page_number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        if section_seven_page is None and "Finite Completion of the Classi" in text:
            section_seven_page = page_number
        if section_eight_page is None and "Concluding Remarks" in text:
            section_eight_page = page_number
    require(section_seven_page is not None and section_eight_page is not None,
            "Section 7/8 page anchors absent")
    require(section_eight_page - section_seven_page <= 6, "Section 7 exceeds page budget")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "subsections": 5,
        "terminal_records": 64,
        "bridge_orders": 96,
        "baseline_draft_stubs": 4,
        "draft_stubs": draft_stubs,
        "section_seven_page": section_seven_page,
        "section_eight_page": section_eight_page,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK5810_SECTION7_VERIFY_PASS "
        f"subsections={result['subsections']} terminals={result['terminal_records']} "
        f"bridge={result['bridge_orders']} "
        f"pages={result['section_seven_page']}..{result['section_eight_page']} "
        f"stubs={result['draft_stubs']}/{result['baseline_draft_stubs']}"
    )
