"""Fail-closed structural checker for the canonical Task 57 proof package."""

from __future__ import annotations

import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
PACKAGE = REPO / "research" / "paper" / "proof_completion"

ROOT_FILES = (
    "BASELINE.md",
    "TARGET_A_FINAL_CLAIM_INVENTORY_V2.md",
    "TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md",
    "TARGET_A_FINAL_PROOF_DEPENDENCY_GRAPH.md",
    "TARGET_A_FINAL_COMPUTER_ASSISTED_THEOREM_TABLE.md",
    "TARGET_A_STALE_RANK_CLAIM_AUDIT.md",
    "TARGET_A_FINAL_NOTATION.md",
    "TARGET_A_JGT_PROOF_ARCHITECTURE.md",
    "TARGET_A_JGT_THEOREM_HIERARCHY.md",
    "TARGET_A_PROOF_COMPLETION_SYNTHESIS.md",
)

THEOREM_DIRECTORIES = (
    "01_even_order_classification",
    "02_small_order_34_46",
    "03_reference_phase",
    "04_charge_sector",
    "05_g6_edge",
    "06_single_gap",
    "07_exact_2r",
    "08_residue_ims",
    "09_moments_periodic",
)

UNIVERSAL_FILES = (
    "THEOREM_STATEMENT.md",
    "PROOF_OVERVIEW.md",
    "FULL_PROOF.md",
    "DEPENDENCIES.md",
    "COMPUTER_ASSISTED_BOUNDARY.md",
    "REFEREE_CHECKLIST.md",
)

BOUND_CERTIFICATES = (
    "research/proofs/task51/certificates/c6_exact_evans_elimination.json",
    "research/proofs/task53/certificates/g6_global_edge.json",
    "research/proofs/task53/certificates/p24_c6_frontier.json",
    "research/proofs/task54/TARGET_A_TASK54_EVENTUAL_THRESHOLD_CERTIFICATE.json",
    "research/proofs/task55/certificates/exact_2r_cluster.json",
    "research/proofs/task55/certificates/small_order_exact_classification.json",
    "research/proofs/task57/certificates/uniform_single_gap_separation.json",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    require(path.is_file(), f"missing file: {path}")
    text = path.read_text(encoding="utf-8")
    require(len(text.strip()) >= 120, f"stub proof artifact: {path}")
    return text


def claim_ids(text: str) -> set[str]:
    return set(re.findall(r"(?<![A-Za-z0-9_])(?:T[1-8]|A|C)\.\d+(?![A-Za-z0-9_])", text))


def verify(package: Path = PACKAGE) -> dict[str, bool]:
    roots = {name: read(package / name) for name in ROOT_FILES}
    theorem_text = {}
    for directory in THEOREM_DIRECTORIES:
        theorem_text[directory] = {
            name: read(package / directory / name) for name in UNIVERSAL_FILES
        }

    inventory_ids = claim_ids(roots["TARGET_A_FINAL_CLAIM_INVENTORY_V2.md"])
    matrix_ids = claim_ids(roots["TARGET_A_FINAL_CLAIM_EVIDENCE_MATRIX_V2.md"])
    require(len(inventory_ids) >= 20, "claim inventory is too small")
    require(inventory_ids <= matrix_ids, "claim-evidence matrix omits inventory IDs")

    dag = roots["TARGET_A_FINAL_PROOF_DEPENDENCY_GRAPH.md"]
    require(not re.search(r"\bTask\s*[0-9]+\b", dag, re.IGNORECASE), "canonical DAG uses Task labels")
    require(re.search(r"exact(?:-|\s+|\s+`)2r`?", dag.lower()) is not None, "DAG omits exact-2r")

    notation = roots["TARGET_A_FINAL_NOTATION.md"]
    for token in (
        "A_sigma", "H_sigma=A_sigma^2", "Q", "tau", "g", "q", "B_s", "eta", "c6",
        "rho_-", "m_n", "alpha", "D", "ell",
    ):
        require(token in notation, f"notation omits {token}")

    even = "\n".join(theorem_text["01_even_order_classification"].values())
    for token in ("n=32", "n=40", "48", "240", "34", "46"):
        require(token in even, f"even-order package omits {token}")
    require(re.search(r"does not\s+classify", even.lower()) is not None, "even-order scope boundary omitted")

    small = "\n".join(theorem_text["02_small_order_34_46"].values())
    for token in ("64", "terminal_unresolved=0", "holonomy", "soundness", "completeness"):
        require(token.lower() in small.lower(), f"small-order completeness omits {token}")

    reference = "\n".join(theorem_text["03_reference_phase"].values())
    require("4+sqrt(10+2sqrt(5))" in reference.replace(" ", ""), "eta formula omitted")

    charge = "\n".join(theorem_text["04_charge_sector"].values())
    for token in ("q=g-4", "modulo four", "sum"):
        require(token.lower() in charge.lower(), f"charge package omits {token}")

    g6 = "\n".join(theorem_text["05_g6_edge"].values())
    for token in ("sup sigma(H_6)=c_6", "K^2=-I", "KA=-AK", "dimension two"):
        require(token.lower() in g6.lower(), f"G6 package omits {token}")

    single = "\n".join(theorem_text["06_single_gap"].values())
    for token in ("c_6+1/250", "182/23", "g=8", "strict"):
        require(token.lower() in single.lower(), f"single-gap package omits {token}")

    exact_2r = "\n".join(theorem_text["07_exact_2r"].values())
    for token in ("exactly `2r`", "codimension-`2r`", "2r x 2r", "multiplicity"):
        require(token.lower() in exact_2r.lower(), f"exact-2r package omits {token}")

    residue = "\n".join(theorem_text["08_residue_ims"].values())
    require(
        "limsup" in residue
        and re.search(r"(?:no|nor)\s+(?:matching\s+)?lower bound", residue.lower()) is not None,
        "residue scope overclaimed",
    )

    periodic = "\n".join(theorem_text["09_moments_periodic"].values())
    require("p<=24" in periodic.replace(" ", ""), "bounded periodic scope omitted")
    require("not" in periodic.lower() and "all-period" in periodic.lower(), "periodic boundary omitted")

    machine_table = roots["TARGET_A_FINAL_COMPUTER_ASSISTED_THEOREM_TABLE.md"]
    for token in ("producer", "checker", "certificate", "arithmetic"):
        require(token in machine_table.lower(), f"computer table omits {token}")

    stale = roots["TARGET_A_STALE_RANK_CLAIM_AUDIT.md"]
    for token in ("CURRENT CORRECT", "HISTORICAL SUPERSEDED", "MUST UPDATE BEFORE MANUSCRIPT"):
        require(token in stale, f"stale audit omits {token}")

    for relative in BOUND_CERTIFICATES:
        require((REPO / relative).is_file(), f"bound certificate missing: {relative}")

    # Local Markdown links must resolve. Web links and anchors are excluded.
    for path in package.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
            clean = target.split("#", 1)[0]
            if not clean or "://" in clean or clean.startswith("mailto:"):
                continue
            if "/" not in clean and "." not in clean:
                continue
            require((path.parent / clean).resolve().exists(), f"broken link in {path}: {target}")

    return {
        "root_artifacts_complete": True,
        "nine_universal_packages_complete": True,
        "claim_matrix_covers_inventory": True,
        "canonical_DAG_has_no_task_dependencies": True,
        "notation_contract_complete": True,
        "finite_state_completeness_explained": True,
        "uniform_single_gap_corollary_present": True,
        "exact_2r_scope_present": True,
        "residue_and_periodic_boundaries_present": True,
        "certificate_paths_exist": True,
        "local_links_resolve": True,
    }


if __name__ == "__main__":
    require(all(verify().values()), "Task 57 proof package failed")
    print("TARGET_A_TASK57_PROOF_PACKAGE_VERIFY_PASS")
