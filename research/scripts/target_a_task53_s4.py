"""Exact stop certificate for the Task 53 c6 weighted-automaton pilot."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task53" / "certificates"


def build_certificate() -> dict[str, Any]:
    grammar = json.loads((RESEARCH / "experiments" / "task52" / "c6_low_energy_grammar.json").read_text())
    moments = json.loads((RESEARCH / "experiments" / "task52" / "c6_weighted_moments.json").read_text())
    eta = 4 + sp.sqrt(10 + 2 * sp.sqrt(5))
    c6_lower = sp.Rational(7905369311620327, 10**15)
    checks = {
        "inherited_state_count": grammar["overlap_automaton"]["nodes"] == 105,
        "inherited_edge_count": grammar["overlap_automaton"]["edges"] == 164,
        "five_existing_forms": sorted(moments["forms"]) == ["F1", "F2", "F3", "F4", "F5"],
        "reference_cycle_present": grammar["period_eight_bulk_cycle_present"] is True,
        "eta_strictly_below_c6": eta < c6_lower,
        "no_deeper_moments": moments["deeper_moment_generation"] == "STOPPED_AT_M6_BY_TASK_RULE",
    }
    checks = {key: bool(value) for key, value in checks.items()}
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "CURRENT_LOCAL_GRAMMAR_INSUFFICIENT",
        "evidence": "PROVED_OBSTRUCTION_TO_STATED_SIGN_CONVENTION",
        "automaton": {"states": 105, "edges": 164, "window_length": 11},
        "forms": ["F1", "F2", "F3", "F4", "F5"],
        "obstruction": (
            "On the period-eight reference cycle every squared Bloch value y satisfies y<=eta<c6. "
            "Therefore F_k=M_(k+1)-c6*M_k is strictly negative for k=1,...,5. For any nonzero "
            "a_k>=0 the total cycle weight sum_k a_k F_k is strictly negative, while every potential "
            "coboundary telescopes to zero around the cycle. Hence the requested edgewise nonnegative "
            "certificate cannot exist on the current automaton with these W_k and signs."
        ),
        "lp_decision": (
            "A normalized nonnegative-coefficient LP is infeasible by the exact reference-cycle "
            "obstruction; the all-zero coefficient vector is vacuous and was excluded."
        ),
        "next_design_requirement": (
            "A future grammar must separate the reference cycle or introduce a calibrated reference "
            "term before a coboundary certificate can encode rigidity at c6."
        ),
        "M7_M8_generated": False,
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "c6_automaton_pilot.json", payload)
    print(json.dumps({"status": payload["status"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()
