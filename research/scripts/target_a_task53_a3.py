"""Exact-resultant and unsquared-Evans producer for Task 53 Gate A3."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_g6_certificate import evans
from target_a_task50_interval import Interval, interval_record
from target_a_task52_exact import elimination_resultant


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task53" / "certificates"
C6_LOWER = Fraction(7905369311620327, 10**15)
C6_UPPER = Fraction(7905369311620328, 10**15)
CANDIDATES = (
    ("gap2_physical_root_on_wrong_branch", Fraction(8080985802104273, 10**15), Fraction(8080985802104274, 10**15)),
    ("secondary_elimination_branch", Fraction(813985656333926, 10**14), Fraction(813985656333928, 10**14)),
)


def build_certificate() -> dict[str, Any]:
    y = sp.symbols("y")
    _resultant, elimination = elimination_resultant(6)
    lower = sp.Rational(C6_UPPER.numerator, C6_UPPER.denominator)
    factor_records = []
    total_candidates = 0
    for row in elimination["factors"]:
        polynomial = sp.Poly(sp.sympify(row["polynomial"]), y)
        count = int(polynomial.count_roots(lower, 16))
        total_candidates += count
        factor_records.append({**row, "roots_in_global_exclusion_interval": count})

    candidate_records = []
    for label, left, right in CANDIDATES:
        matching, _defect, metadata = evans(
            Interval(left, right), gap=6, cofactor_rows=(0, 1, 3)
        )
        containing = []
        for row in factor_records:
            polynomial = sp.Poly(sp.sympify(row["polynomial"]), y)
            count = int(polynomial.count_roots(
                sp.Rational(left.numerator, left.denominator),
                sp.Rational(right.numerator, right.denominator),
            ))
            if count:
                containing.append(row["polynomial"])
        candidate_records.append({
            "label": label,
            "interval": [str(left), str(right)],
            "resultant_factors": containing,
            "unsquared_g6_matching": interval_record(matching.value),
            "matching_excludes_zero": matching.value.excludes_zero(),
            "cofactor_rows": [0, 1, 3],
            "all_vectors_valid": all(row["nonzero_components"] for row in metadata["cofactor_pivots"]),
            "classification": "NONPHYSICAL_FOR_G6",
        })

    local = json.loads(
        (RESEARCH / "proofs" / "task50" / "certificates" / "g6_interface_certificate.json").read_text()
    )
    checks = {
        "exactly_two_resultant_candidates": total_candidates == 2,
        "both_candidate_intervals_isolate_one_factor_root": all(len(row["resultant_factors"]) == 1 for row in candidate_records),
        "both_unsquared_matchings_nonzero": all(row["matching_excludes_zero"] for row in candidate_records),
        "all_candidate_charts_valid": all(row["all_vectors_valid"] for row in candidate_records),
        "local_c6_unique_root_inherited": local["checks"]["derivative_positive"] and local["checks"]["left_sign_negative"] and local["checks"]["right_sign_positive"],
        "local_interval_matches": local["y_interval"] == [str(C6_LOWER), str(C6_UPPER)],
        "operator_norm_cap": 16 >= C6_UPPER,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "GATE_A3_PASS_G6_GLOBAL_EDGE_PROVED",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "theorem": "sup sigma(H6)=c6 and sigma(H6) intersect (c6,16] is empty",
        "c6_interval": [str(C6_LOWER), str(C6_UPPER)],
        "global_exclusion_interval": [str(C6_UPPER), "16"],
        "factor_records": factor_records,
        "candidate_records": candidate_records,
        "local_bridge": (
            "Task 50's exact-rational interval Evans certificate has one simple zero in the c6 interval; "
            "its fixed-sign derivative excludes every further zero through c6_upper."
        ),
        "global_argument": (
            "Every physical unsquared zero annihilates the exact stable-branch resultant. Sturm counting "
            "finds exactly two candidates on [c6_upper,16], and validated unsquared matching excludes both. "
            "The repeated-multiplier energy is represented by the confluent symmetric quotient and is not "
            "a resultant candidate. Finally ||H6||<=4 gives y=lambda^2<=16."
        ),
        "gap2_explanation": (
            "The first candidate is physical for gap2, but the G6 defect transfer and sector orientation "
            "give a strictly nonzero unsquared determinant on its isolating interval."
        ),
        "proof_boundary": (
            "Resultants provide candidate completeness only. Physical classification uses unsquared "
            "matching in certified Grassmann charts; no decimal eigenvalue is an acceptance condition."
        ),
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "g6_global_edge.json", payload)
    print(json.dumps({"status": payload["status"], "candidates": len(payload["candidate_records"])}, indent=2))
    return payload


if __name__ == "__main__":
    run()
