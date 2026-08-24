"""Structural audit for the verified Task 58.1 literature deliverables."""

from __future__ import annotations

from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/task58"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify() -> dict[str, bool]:
    matrix = (ROOT / "TASK58_DIRECT_LITERATURE_MATRIX.md").read_text(encoding="utf-8")
    novelty = (ROOT / "TASK58_NOVELTY_POSITIONING.md").read_text(encoding="utf-8")
    normalized_novelty = " ".join(novelty.split()).lower()
    for group in (
        "A. Direct Prior Art", "B. Signed-Spectral Neighbors",
        "C. Spectral Complete-Classification Analogues",
        "D. Computer-Assisted Graph Classification Analogues",
    ):
        require(group in matrix, f"literature group absent: {group}")
    for field in (
        "Mathematical object", "Switching / computation", "Risk",
        "Safe wording", "Verification",
    ):
        require(field.lower() in matrix.lower(), f"matrix field absent: {field}")
    require("arXiv:2607.18334" in matrix and "**HIGH**" in matrix, "direct predecessor not high risk")
    require(
        "Conjecture 3" in matrix
        and ("resolv" in matrix.lower() and "disprov" in matrix.lower()),
        "conjecture positioning absent",
    )
    require(matrix.count("https://doi.org/") >= 15, "too few verified DOI links")
    require(matrix.count("arxiv.org") >= 15, "too few full-text/arXiv links")
    for sentence in (
        "complete resolution and disproof",
        "To the best of our knowledge",
        "We resolve and disprove Conjecture 3",
        "The computation itself is the novelty",
        "WATCHLIST",
    ):
        require(sentence.lower() in normalized_novelty, f"novelty contract absent: {sentence}")
    require("no previous work gives" in normalized_novelty, "narrow novelty sentence absent")
    require("all real edge signings" in normalized_novelty, "novelty object not narrow enough")
    require("JGT" in matrix and "not used as novelty evidence" in matrix, "narrative/direct boundary absent")
    return {
        "four_literature_groups": True,
        "direct_predecessor_prominent": True,
        "metadata_and_sources_present": True,
        "safe_and_unsafe_wording_present": True,
        "narrow_novelty_positioning": True,
        "watchlist_recorded": True,
    }


if __name__ == "__main__":
    require(all(verify().values()), "Task58.1 literature audit failed")
    print("TARGET_A_TASK581_LITERATURE_VERIFY_PASS")
