"""Fail-closed audit for the Task 58.4 abstract and Introduction."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from pypdf import PdfReader


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
CONTROL = REPO / "research/paper/task58"
ENGLISH_TREE = "59e3a8f73a152ef06f994e979b7219a3365efeae"
CHINESE_TREE = "57ae03fb5b90866f84d0d72b414008678e8f5004"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def git_tree(path: str) -> str:
    output = subprocess.check_output(
        ["git", "ls-tree", "HEAD", path], cwd=REPO, text=True
    ).strip()
    require(output, f"missing frozen tree: {path}")
    return output.split()[2]


def compact(text: str) -> str:
    return "".join(text.split())


def verify() -> dict[str, int | bool]:
    front = (ROOT / "frontmatter.tex").read_text(encoding="ascii")
    intro = (ROOT / "sections/01_introduction.tex").read_text(encoding="ascii")
    audit = (CONTROL / "TASK58_INTRO_CLAIM_AUDIT.md").read_text(encoding="ascii")
    combined = front + "\n" + intro
    require("\r" not in combined and "\x00" not in combined, "control character in prose")

    match = re.search(
        r"\\begin\{abstract\}(.*?)\\end\{abstract\}", front, flags=re.DOTALL
    )
    require(match is not None, "abstract missing")
    abstract = match.group(1).strip()
    abstract_words = len(abstract.split())
    require(150 <= abstract_words <= 190, f"abstract word count {abstract_words}")
    require(abstract.count(".  ") + int(abstract.endswith(".")) == 6,
            "abstract must follow the locked six-sentence logic")
    for forbidden in (
        "exact-2r", "moment", "p<=24", "Grassmann", "JSON", "hash", "test",
        "Task 58", "96 rows", "64 records",
    ):
        require(forbidden.lower() not in abstract.lower(),
                f"abstract contains forbidden detail: {forbidden}")

    c = compact(intro)
    require(intro.count(r"\begin{theorem}") == 2, "Introduction theorem count changed")
    require(len(re.findall(r"^% P(?:[1-9]|1[01])$", intro, flags=re.MULTILINE)) == 11,
            "Introduction paragraph markers changed")
    require(r"m_n<\rho_-(n)" in c, "classification comparison type changed")
    require("n=32,\\quadn=40,\\quad\\text{or}\\quadn\\geq48" in c,
            "failure classification absent")
    require("8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46" in c,
            "validity set absent")
    require(r"\theta_n=\rho_-(n)^2" in c, "theta/rho type relation absent")
    require("7905369311620327" in intro and "7905369311620328" in intro,
            "c6 isolating interval absent")
    for term in ("16y^{10}", "-520y^9", "-19968y+256"):
        require(term in c, f"c6 polynomial term absent: {term}")
    require(r"\dim\ker(H_6-c_6)=2" in c, "rank-two statement absent")
    require(r"E(g)>c_6+\frac1{250}" in c, "single-gap separation absent")
    require(r"\sum_jq_j\equivn\pmod8" in c, "mod-eight closure absent")
    require(r"\sigma_{\mathrm{sec}}(q)=q\pmod4" in c, "mod-four sector absent")
    require(r"n\geq240" in c and r"48\leqn<240" in c, "tail/bridge boundary absent")
    require(r"\cite[Conjecture~3]{Suvagiya2026Signed}" in intro,
            "direct predecessor not prominent")
    require("resolving and disproving the conjecture" in intro,
            "direct predecessor wording changed")
    require("Tothebestofourknowledge" in c and "fixedcirculantfamily" in c,
            "cautious novelty sentence absent")
    for key in (
        "GoedgebeurSchaudt2018", "DeVosSamal2011", "LinNing2021",
        "GoedgebeurRendersWienerZamfirescu2024",
    ):
        require(key in intro, f"methodological citation absent: {key}")

    require("% TASK58_DRAFT_STUB" not in combined, "front matter or Introduction still stubbed")
    all_tex = "\n".join(path.read_text(encoding="ascii") for path in ROOT.rglob("*.tex"))
    draft_stubs = all_tex.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 32, "draft-stub count cannot exceed post-Introduction baseline")
    require(r"\footnote" not in all_tex, "footnotes are forbidden")
    for forbidden in (
        "exact-2r", "p<=24", "Grassmann", "internal path", "Task 58",
        "all even n>=32", "every even n>=32",
    ):
        require(forbidden.lower() not in combined.lower(),
                f"Introduction contains forbidden wording: {forbidden}")
    require(len(audit.strip()) >= 2500 and "Overclaim risk" in audit,
            "Introduction claim audit incomplete")

    reader = PdfReader(ROOT / "main.pdf")
    section_two_page = None
    for page_number, page in enumerate(reader.pages, 1):
        if "Switching Coordinates and the Reference Phase" in (page.extract_text() or ""):
            section_two_page = page_number
            break
    require(section_two_page is not None and section_two_page <= 5,
            "Introduction exceeds the five-page budget")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "abstract_words": abstract_words,
        "abstract_sentences": 6,
        "introduction_paragraphs": 11,
        "introduction_theorems": 2,
        "section_two_page": section_two_page,
        "baseline_draft_stubs": 32,
        "draft_stubs": draft_stubs,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK584_INTRO_VERIFY_PASS "
        f"abstract_words={result['abstract_words']} "
        f"paragraphs={result['introduction_paragraphs']} "
        f"theorems={result['introduction_theorems']} "
        f"section2_page={result['section_two_page']} "
        f"stubs={result['draft_stubs']}"
    )
