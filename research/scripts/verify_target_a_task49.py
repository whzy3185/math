"""Fail-closed acceptance verifier for Target A Task 49."""

from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[1]
ROOT = RESEARCH.parent
TASK49 = RESEARCH / "experiments" / "task49"
REPRO = RESEARCH / "reproducibility" / "task49"
BASELINE = "8ecbc6ab5ee1dcf519c92927fc2713e1989f40aa"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def csv_rows(path: Path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def unchanged(*paths: str) -> bool:
    return subprocess.run(
        ["git", "diff", "--quiet", BASELINE, "--", *paths], cwd=ROOT, check=False
    ).returncode == 0


def run() -> None:
    uniform = load(TASK49 / "uniform_and_crossing_summary.json")
    require(uniform["uniform_bound_gate"] == "UNIFORM_BOUND_TEMPLATE_FOUND", "uniform gate failed")
    require(uniform["two_interface_classification"] == "TWO_TAIL_BOUND_SUPPORTED", "two-tail gate failed")
    expected_onsets = {"G6": 50, "G10": 94, "TWO_SYMMETRIC": 52, "TWO_SHIFTED": 60}
    require(
        {key: value["first_exact_crossing"] for key, value in uniform["crossing_onsets"].items()} == expected_onsets,
        "threshold onset mismatch",
    )

    interface = load(TASK49 / "interface_mechanism" / "summary.json")
    require(interface["gate"] == "INTERFACE_MECHANISM_READY_FOR_PROOF", "interface gate failed")
    require(interface["splitting_precision_digits"] == 160, "precision ladder incomplete")
    require(interface["finite_matrix_evans_crosschecks_pass"], "finite-matrix Evans mismatch")
    require(interface["cut_invariant"] and interface["orientation_invariant"], "representation mismatch")
    require(interface["equivalent_stable_unstable_matching"], "equivalent matching missing")
    require(interface["localization"]["classification"] == "LOCALIZATION_ROBUST", "localization gate failed")

    p24 = load(REPRO / "p24_independent" / "summary.json")
    require(p24["status"] == "P24_AUDIT_PASS", "p24 audit failed")
    require(
        p24["totals"] == {
            "legal_dihedral_orbits": 370100,
            "moment": 369916,
            "strict": 183,
            "equality": 1,
            "lower": 0,
            "unresolved": 0,
            "consumed": 370100,
        },
        "p24 partition mismatch",
    )
    require(p24["destructive_accounting_remaining"] == 0, "p24 accounting not destructive")

    hankel = load(REPRO / "hankel_independent" / "summary.json")
    require(hankel["status"] == "HANKEL_AUDIT_PASS", "Hankel audit failed")
    require(hankel["independently_checked"] == 184 and hankel["target_survives"], "Hankel target mismatch")

    require(len(csv_rows(TASK49 / "figure_data" / "figure1_threshold_crossings.csv")) == 35, "figure 1 data incomplete")
    require(load(TASK49 / "figure_data" / "metadata.json")["status"] == "TASK49_STORY_DATA_READY", "figure metadata failed")
    inventory = (TASK49 / "TARGET_A_JCTB_FACT_INVENTORY.md").read_text(encoding="utf-8")
    require(inventory.count("| 1 |") >= 1 and "| 24 |" in inventory, "fact inventory incomplete")

    required_reports = [
        TASK49 / "UNIFORM_BOUND_RECONNAISSANCE.md",
        TASK49 / "TARGET_A_THRESHOLD_CROSSING_ATLAS.md",
        TASK49 / "TARGET_A_FLOQUET_PHASE_AND_MOD16.md",
        TASK49 / "TARGET_A_TASK49_SYNTHESIS.md",
        RESEARCH / "review" / "task49" / "TARGET_A_P24_INDEPENDENT_AUDIT.md",
        RESEARCH / "review" / "task49" / "TARGET_A_HANKEL_INDEPENDENT_AUDIT.md",
        RESEARCH / "proofs" / "task49" / "TARGET_A_INTERFACE_PROOF_BLUEPRINT.md",
    ]
    require(all(path.exists() and path.stat().st_size > 500 for path in required_reports), "required report missing")
    require(
        unchanged("research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh"),
        "formal manuscript freeze failed",
    )
    print("TARGET_A_TASK49_VERIFY_PASS")


if __name__ == "__main__":
    run()
