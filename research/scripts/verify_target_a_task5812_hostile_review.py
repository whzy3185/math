"""Fail-closed audit for the Task 58.12 hostile manuscript review."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from pypdf import PdfReader

from verify_target_a_task5811_package import verify as verify_package


REPO = Path(__file__).resolve().parents[2]
MAIN = REPO / "research/paper/manuscript_tex_task58"
SUPP = REPO / "research/paper/manuscript_tex_task58_supplement"
REVIEW = REPO / "research/paper/task58/TASK58_HOSTILE_MANUSCRIPT_REVIEW.md"
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


def verify() -> dict[str, int | bool | str]:
    package = verify_package()
    review = REVIEW.read_text(encoding="ascii")
    require("READY_FOR_FINAL_SUBMISSION_AUDIT" in review,
            "hostile-review verdict absent")
    require("Open MAJOR: 0" in review and "Open MINOR: 0" in review,
            "hostile review has an open internal issue")
    for heading in (
        "Headline and scope", "Mathematical logic audit",
        "Four-channel attack review and repairs",
        "Computer-assisted proof boundaries",
        "Stale, draft, and workflow scans", "Length and visual audit",
        "Literature and novelty", "External metadata", "Review verdict",
    ):
        require(heading in review, f"hostile-review section absent: {heading}")
    for repair in (
        "negative unsquared matching branch", "order-40 binary word",
        "continuous Evans orientation", "cross-chart implication",
        "Task 50 local matching", "Task 56 checker",
        "python3 -m pytest -q", "anonymous PDF suppresses", "qquad",
    ):
        require(repair in review, f"attack repair absent from review: {repair}")

    main_files = list(MAIN.rglob("*.tex"))
    supp_files = list(SUPP.rglob("*.tex"))
    main_text = "\n".join(path.read_text(encoding="ascii") for path in main_files)
    supp_text = "\n".join(path.read_text(encoding="ascii") for path in supp_files)
    for marker in (
        "TASK58_DRAFT_STUB", "TODO", "TBD", "FIXME", "PLACEHOLDER",
        "Lorem", "proof to be added",
    ):
        require(marker.lower() not in (main_text + supp_text).lower(),
                f"draft marker remains: {marker}")
    require(r"\footnote" not in main_text, "main-paper author footnote remains")
    for stale in (
        "rank-one squared", "rank one squared", "exact-r cluster",
        "codimension-r complement", "r x r G6", "p<=24", "period 25",
        "period 26", "common liminf theorem", "three-body theorem",
    ):
        require(stale.lower() not in (main_text + supp_text).lower(),
                f"active stale phrase remains: {stale}")
    for workflow in (
        "Task 52", "Task 53", "Task 54", "Task 55", "Task 56", "Task 57",
        "Task58", "Codex", "subagent", "prompt",
    ):
        require(workflow not in main_text, f"workflow trace in main paper: {workflow}")
    require(re.search(r"(?<!\\)qquad", supp_text) is None,
            "visible qquad typo remains")

    anonymous = PdfReader(MAIN / "main_anonymous.pdf")
    anonymous_text = "\n".join(page.extract_text() or "" for page in anonymous.pages)
    require("whzy3185" not in anonymous_text and "e365e155" not in anonymous_text,
            "anonymous PDF leaks identity")
    require(len(PdfReader(MAIN / "main.pdf").pages) <= 45,
            "main paper exceeds page gate")
    require(package["main_figures"] == 3 and package["draft_stubs"] == 0,
            "package and hostile review disagree")
    require(package["archive_status"] == "IMMUTABLE_ARCHIVE_PENDING",
            "archive status changed without a real archive")
    require(git_tree("research/paper/manuscript_tex_pub") == ENGLISH_TREE,
            "historical English manuscript changed")
    require(git_tree("research/paper/manuscript_tex_pub_zh") == CHINESE_TREE,
            "historical Chinese manuscript changed")

    return {
        "open_major": 0,
        "open_minor": 0,
        "verdict": "READY_FOR_FINAL_SUBMISSION_AUDIT",
        "attack_channels": 4,
        "main_pages": package["main_pages"],
        "supplement_pages": package["supplement_pages"],
        "historical_trees_frozen": True,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK5812_HOSTILE_REVIEW_PASS "
        f"major={result['open_major']} minor={result['open_minor']} "
        f"attacks={result['attack_channels']} main={result['main_pages']} "
        f"supplement={result['supplement_pages']} verdict={result['verdict']}"
    )
