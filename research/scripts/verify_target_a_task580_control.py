"""Fail-closed audit for the Task 58.0 manuscript control layer."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
CONTROL = REPO / "research" / "paper" / "task58"
APPROVED = "20eb153560df30980ff5ee842246579af40faae5"

REQUIRED = (
    "TASK58_FIRST_SUBMISSION_SCOPE.md",
    "TASK58_SOURCE_IMPORT_MAP.md",
    "TASK58_MATHEMATICAL_CONTRACT.md",
    "TASK58_STALE_CLAIM_BLACKLIST.md",
    "TASK58_JGT_VISUAL_STYLE_CONTRACT.md",
    "TASK58_CURRENT_HANDOFF.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(name: str, control: Path = CONTROL) -> str:
    path = control / name
    require(path.is_file(), f"missing Task58 control file: {name}")
    text = path.read_text(encoding="utf-8")
    require(len(text.strip()) >= 200, f"stub Task58 control file: {name}")
    return text


def git_output(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=REPO, text=True, capture_output=True, check=True
    ).stdout.strip()


def verify(control: Path = CONTROL, check_git: bool = True) -> dict[str, bool]:
    docs = {name: read(name, control) for name in REQUIRED}
    scope = docs["TASK58_FIRST_SUBMISSION_SCOPE.md"]
    source_map = docs["TASK58_SOURCE_IMPORT_MAP.md"]
    contract = docs["TASK58_MATHEMATICAL_CONTRACT.md"]
    blacklist = docs["TASK58_STALE_CLAIM_BLACKLIST.md"]
    visual = docs["TASK58_JGT_VISUAL_STYLE_CONTRACT.md"]
    handoff = docs["TASK58_CURRENT_HANDOFF.md"]

    for category in (
        "MAIN_MANUSCRIPT_IMPORT",
        "STATEMENT_OVERVIEW_ONLY",
        "SUPPLEMENT_ONLY",
        "DO_NOT_IMPORT_FIRST_SUBMISSION",
    ):
        require(category in scope, f"scope omits {category}")
    for removed in (
        "p<=24", "moment", "multi-gap", "reference graph", "period 25",
        "period 26", "interaction", "common liminf", "correction history",
    ):
        require(removed.lower() in scope.lower(), f"scope omission absent: {removed}")

    inventory = (REPO / "research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md").read_text(encoding="utf-8")
    claim_ids = set(re.findall(r"`((?:T[1-8]|A|C)\.\d+)`", inventory))
    require(len(claim_ids) == 46, f"unexpected canonical claim count: {len(claim_ids)}")
    missing = sorted(claim for claim in claim_ids if claim not in source_map)
    require(not missing, f"source import map omits claims: {missing}")
    for heading in (
        "claim id", "evidence", "main", "appendix", "supplement",
        "computer", "forbidden", "notes",
    ):
        require(heading in source_map.lower(), f"source map field absent: {heading}")

    for token in (
        "theta_n", "m_n<rho_-(n)", "q_i=-1", "alpha=-1", "eta",
        "mod 8", "mod 4", "1/250", "sigma_ess(h_6)", "dim ker(h_6-c_6)=2",
        "2r", "limsup", "n>=240", "48<=n<240", "64",
    ):
        require(token.lower() in contract.lower(), f"math contract omits {token}")
    for hazard in (
        "rank-one", "exact-r", "codimension-r", "r x r", "common limit",
        "unrestricted liminf", "all-period", "period 25", "period 26",
        "p<=24", "interaction coefficient", "three-body", "script observed",
        "ai", "agent",
    ):
        require(hazard.lower() in blacklist.lower(), f"blacklist omits {hazard}")
    for token in (
        "black-and-white", "tikz", "no footnotes", "45", "three main figures",
        "no infographic", "no software", "no decorative", "supplement",
    ):
        require(token.lower() in visual.lower(), f"visual contract omits {token}")

    require(APPROVED in handoff, "handoff omits approved checkpoint")
    require("task 58.0" in handoff.lower(), "handoff phase mismatch")
    require("task 58.1" in handoff.lower(), "handoff next task mismatch")
    require("not yet created" in handoff.lower(), "handoff manuscript state mismatch")

    if check_git:
        require(git_output("branch", "--show-current") == "agent/target-a-discovery-snapshot", "wrong branch")
        ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", APPROVED, "HEAD"], cwd=REPO
        ).returncode
        require(ancestry == 0, "approved checkpoint ancestry failed")
        trees = {
            "research/paper/manuscript_tex_pub": "59e3a8f73a152ef06f994e979b7219a3365efeae",
            "research/paper/manuscript_tex_pub_zh": "57ae03fb5b90866f84d0d72b414008678e8f5004",
        }
        for path, expected in trees.items():
            fields = git_output("ls-tree", "HEAD", path).split()
            require(len(fields) >= 3 and fields[2] == expected, f"frozen tree changed: {path}")

    return {
        "six_control_files_complete": True,
        "four_level_scope_complete": True,
        "all_46_claims_mapped": True,
        "mathematical_contract_complete": True,
        "stale_blacklist_complete": True,
        "visual_contract_complete": True,
        "handoff_complete": True,
        "approved_ancestry": True,
        "historical_manuscripts_frozen": True,
    }


if __name__ == "__main__":
    require(all(verify().values()), "Task58.0 control audit failed")
    print("TARGET_A_TASK580_CONTROL_VERIFY_PASS claims=46")
