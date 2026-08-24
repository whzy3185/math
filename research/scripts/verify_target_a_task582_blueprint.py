"""Fail-closed audit for the Task 58.2 manuscript blueprint."""

from __future__ import annotations

import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "research/paper/task58"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(name: str) -> str:
    path = ROOT / name
    require(path.is_file(), f"missing blueprint artifact: {name}")
    text = path.read_text(encoding="utf-8")
    require(len(text.strip()) >= 500, f"stub blueprint artifact: {name}")
    return text


def verify() -> dict[str, bool]:
    blueprint = read("TASK58_MANUSCRIPT_MASTER_BLUEPRINT.md")
    theorem_map = read("TASK58_THEOREM_TO_SECTION_MAP.md")
    maps = read("TASK58_NARRATIVE_AND_DEPENDENCY_MAPS.md")
    b = " ".join(blueprint.split()).lower()

    require("spectral radius minimization for signed squares of cycles" in b, "title absent")
    require("edge signing" in b and "c_n^2" in b, "title ambiguity note absent")
    require(b.count("theorem box") >= 2, "two introduction theorem boxes absent")
    for token in (
        "complete classification", "reference and single-gap spectral hierarchy",
        "degree-ten", "isolating interval", "e(4)", "e(6)", "1/250",
        "dim ker", "10", "11", "introduction", "page", "appendix",
        "supplement", "figure 1", "figure 2", "figure 3", "grayscale", "tikz",
    ):
        require(token in b, f"blueprint omits {token}")
    for section in (
        "switching coordinates and the reference phase",
        "gaps, charges, and translation sectors",
        "the elementary six-gap phase slip",
        "optimality among single-gap interfaces",
        "phase slips on finite rings",
        "finite completion of the classification",
        "concluding remarks",
    ):
        require(section in b, f"section absent: {section}")
    require("45" in b and "28--34" in b, "page budget absent")
    require("p<=24" in b and "omit" in b, "period frontier deletion absent")
    require("moment" in b and "omit" in b, "moment deletion absent")
    require("multi-gap" in b and "omit" in b, "multi-gap deletion absent")

    inventory = (REPO / "research/paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md").read_text(encoding="utf-8")
    claims = set(re.findall(r"`((?:T[1-8]|A|C)\.\d+)`", inventory))
    require(len(claims) == 46, "canonical claim count changed")
    placement_rows = [line for line in theorem_map.splitlines() if line.startswith("| `")]
    for claim in claims:
        require(
            sum(f"`{claim}`" in line.split("|", 3)[1] for line in placement_rows) == 1,
            f"theorem map count for {claim}",
        )
    for label in (
        "MAIN_THEOREM", "SUPPORTING_THEOREM", "PROPOSITION", "LEMMA",
        "APPENDIX_ONLY", "SUPPLEMENT_ONLY", "OMIT_FIRST_SUBMISSION",
    ):
        require(label in theorem_map, f"theorem-map label absent: {label}")
    for claim in ("A.1", "A.2", "A.3", "A.4", "A.5", "A.6", "C.9"):
        line = next((line for line in theorem_map.splitlines() if f"`{claim}`" in line), "")
        require("OMIT_FIRST_SUBMISSION" in line, f"deleted claim not omitted: {claim}")
    line = next((line for line in theorem_map.splitlines() if "`T6.3`" in line), "")
    require("SUPPORTING_THEOREM" in line or "APPENDIX_ONLY" in line, "exact2r placement wrong")

    m = " ".join(maps.split()).lower()
    require("narrative reveal" in m and "mathematical dependency" in m, "two maps absent")
    require("surprising complete answer" in m and "structural explanation" in m, "narrative map wrong")
    for token in (
        "candidate attainment", "finite", "reference", "g6", "patch", "ims",
        "48", "complete classification",
    ):
        require(token in m, f"dependency map omits {token}")
    require("eventual" in m and "onset" in m, "eventual/onset boundary absent")
    require("not" in m and "infographic" in m, "map publication prohibition absent")

    return {
        "master_blueprint_complete": True,
        "two_intro_boxes": True,
        "eight_section_flow": True,
        "all_46_claims_mapped_once": True,
        "first_submission_deletions_enforced": True,
        "narrative_and_dependency_maps_separate": True,
        "page_and_figure_budget_present": True,
    }


if __name__ == "__main__":
    require(all(verify().values()), "Task58.2 blueprint audit failed")
    print("TARGET_A_TASK582_BLUEPRINT_VERIFY_PASS claims=46")
