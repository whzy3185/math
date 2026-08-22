"""Fail-closed verifier for the Target A Task 51 artifact package."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[1]
ROOT = RESEARCH.parent
TASK51 = RESEARCH / "experiments" / "task51"
BASELINE = "82895863a59f8014d547544a7b3bb18aaa0cc8e5"


def load(name: str):
    return json.loads((TASK51 / name).read_text(encoding="utf-8"))


def main() -> None:
    checks = {
        "order9": load("recurrence_exact_structure.json")["status"] == "ORDER9_EXACT_1_PLUS_4_PLUS_4_PROVED",
        "charge": load("charge_conservation.json")["status"] == "EXACT_CHARGE_CONSERVATION_PROVED",
        "gap2": load("single_charge_summary.json")["q_minus_2_conclusion"] == "LOCALIZED_LEVEL_ABOVE_8",
        "three_g6": load("multi_slip_summary.json")["three_G6_beats_G10"] is True,
        "moments": load("higher_moment_motifs.json")["status"] == "M4_M5_M6_EXACT_LOCAL_MOTIF_EXPANSIONS_PROVED",
        "crystallization_open": load("local_rayleigh_debruijn.json")["classification"] == "WEAK",
        "c6_exact": json.loads((RESEARCH / "proofs" / "task51" / "certificates" / "c6_exact_evans_elimination.json").read_text())["c6"]["status"] == "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED",
        "manuscript_freeze": subprocess.run([
            "git", "diff", "--quiet", BASELINE, "--",
            "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh",
        ], cwd=ROOT).returncode == 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    output = {"status": "TARGET_A_TASK51_VERIFY_PASS", "checks": checks}
    target = RESEARCH / "reproducibility" / "task51"
    target.mkdir(parents=True, exist_ok=True)
    (target / "verification.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(output["status"])


if __name__ == "__main__":
    main()
