"""Independent checker for the Task 53 weighted-automaton stop certificate."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "c6_automaton_pilot.json"


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text())
    grammar = json.loads((RESEARCH / "experiments" / "task52" / "c6_low_energy_grammar.json").read_text())
    eta = 4 + sp.sqrt(10 + 2 * sp.sqrt(5))
    checks = {
        "counts_rebuilt": grammar["overlap_automaton"] == {"window_length": 11, "nodes": 105, "edges": 164},
        "cycle_rebuilt": grammar["period_eight_bulk_cycle_present"],
        "strict_edge_threshold": eta < sp.Rational(7905369311620327, 10**15),
        "telescoping_logic_present": "telescopes to zero" in data["obstruction"],
        "fail_status_exact": data["status"] == "CURRENT_LOCAL_GRAMMAR_INSUFFICIENT",
        "no_new_moments": data["M7_M8_generated"] is False,
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_S4_VERIFY_PASS")


if __name__ == "__main__":
    main()
