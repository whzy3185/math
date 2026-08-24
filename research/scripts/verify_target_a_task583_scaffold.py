"""Fail-closed audit for the Task 58.3 clean manuscript scaffold."""

from __future__ import annotations

import subprocess
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/manuscript_tex_task58"
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


def verify() -> dict[str, bool | int]:
    required = {
        "main.tex", "main_anonymous.tex", "publication-preamble.tex",
        "frontmatter.tex", "body.tex", "README.md", "references.bib",
        "sections/01_introduction.tex", "sections/02_switching_reference.tex",
        "sections/03_gaps_charges_sectors.tex", "sections/04_elementary_g6.tex",
        "sections/05_single_gap.tex", "sections/06_finite_rings.tex",
        "sections/07_finite_completion.tex", "sections/08_concluding.tex",
        "sections/09_data_code_availability.tex",
        "appendices/appendix_a_g6_certification.tex",
        "appendices/appendix_b_finite_classification.tex",
        "figures/figure_cycle_switching.tex",
        "figures/figure_reference_slips.tex",
        "figures/figure_patch_localization.tex", "main.pdf",
    }
    missing = sorted(name for name in required if not (ROOT / name).is_file())
    require(not missing, f"missing scaffold files: {missing}")

    tex_files = sorted(ROOT.rglob("*.tex"))
    text = "\n".join(path.read_text(encoding="ascii") for path in tex_files)
    sections = sorted((ROOT / "sections").glob("*.tex"))
    appendices = sorted((ROOT / "appendices").glob("*.tex"))
    figures = sorted((ROOT / "figures").glob("*.tex"))
    require(len(sections) == 9, "expected eight numbered sections plus availability")
    require(sum("\\section{" in path.read_text(encoding="ascii") for path in sections) == 8,
            "numbered section count changed")
    availability = (ROOT / "sections/09_data_code_availability.tex").read_text(encoding="ascii")
    require("\\section*{Data and Code Availability}" in availability,
            "availability section must be unnumbered")
    require(len(appendices) == 2, "expected exactly two appendices")
    require(len(figures) == 3, "expected exactly three figure sources")
    draft_stubs = text.count("% TASK58_DRAFT_STUB")
    require(0 <= draft_stubs <= 34, "draft-stub count cannot exceed baseline")
    draft_paragraphs = text.count("\\TaskDraftStub") - 1
    require(0 <= draft_paragraphs <= 31,
            "draft paragraph count cannot exceed baseline")
    require("\\footnote" not in text, "footnotes are forbidden")
    for stale in (
        "exact-r", "codimension-r", "rank-r", "PENDING_INDEPENDENT_CHECKER_PASS",
        "every even n>=32", "all even n>=32",
    ):
        require(stale.lower() not in text.lower(), f"stale claim present: {stale}")

    body = (ROOT / "body.tex").read_text(encoding="ascii")
    require(body.count("\\input{sections/") == 9, "section include count changed")
    require(body.count("\\input{appendices/") == 2, "appendix include count changed")
    require(body.count("\\appendix") == 1, "appendix switch count changed")
    preamble = (ROOT / "publication-preamble.tex").read_text(encoding="ascii")
    for environment in ("theorem", "proposition", "lemma", "corollary", "definition", "remark"):
        require(f"{{{environment}}}" in preamble, f"missing environment: {environment}")
    require("\\documentclass[11pt]{article}" in (ROOT / "main.tex").read_text(encoding="ascii"),
            "stable article setup absent")
    current_bib = (ROOT / "references.bib").read_text(encoding="ascii")
    baseline_bib = (REPO / "research/paper/manuscript_tex_pub/references.bib").read_text(
        encoding="ascii"
    )
    key_pattern = re.compile(r"@\w+\{([^,]+),")
    require(set(key_pattern.findall(baseline_bib)) <= set(key_pattern.findall(current_bib)),
            "a baseline bibliography key was removed")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "clean_scaffold": True,
        "numbered_sections": 8,
        "appendices": 2,
        "figure_sources": 3,
        "baseline_draft_stubs": 34,
        "draft_stubs": draft_stubs,
        "compiled_pdf": True,
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK583_SCAFFOLD_VERIFY_PASS "
        f"sections={result['numbered_sections']} appendices={result['appendices']} "
        f"figures={result['figure_sources']} "
        f"stubs={result['draft_stubs']}/{result['baseline_draft_stubs']}"
    )
