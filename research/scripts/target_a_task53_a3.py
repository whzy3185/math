"""Exact-resultant and unsquared-Evans producer for Task 53 Gate A3."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp
import numpy as np

from target_a_task47_common import write_json
from target_a_task50_g6_certificate import evans
from target_a_task50_g6_certificate import tau_window
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


def anticommuting_symmetry_certificate() -> dict[str, Any]:
    records = []
    for dimension in (58, 90, 138):
        low = (10 - dimension) // 2
        high = 9 - low
        tau = tau_window(6, low=low - 4, high=high + 4)
        adjacency = np.zeros((dimension, dimension), dtype=np.int64)
        symmetry = np.zeros((dimension, dimension), dtype=np.int64)
        for index in range(low, high + 1):
            row = index - low
            for distance, sign in ((1, 1), (2, tau[index])):
                target = index + distance
                if target <= high:
                    adjacency[row, target - low] = sign
                    adjacency[target - low, row] = sign
            symmetry[row, 9 - index - low] = -1 if index % 2 else 1
        square = adjacency @ adjacency
        compact = lambda matrix: json.dumps(matrix.tolist(), separators=(",", ":")).encode()
        records.append({
            "dimension": dimension,
            "index_interval": [low, high],
            "A_sha256": hashlib.sha256(compact(adjacency)).hexdigest(),
            "K_sha256": hashlib.sha256(compact(symmetry)).hexdigest(),
            "K_squared_is_minus_identity": bool(np.array_equal(
                symmetry @ symmetry, -np.eye(dimension, dtype=np.int64)
            )),
            "K_anticommutes_with_A": bool(np.array_equal(
                symmetry @ adjacency, -(adjacency @ symmetry)
            )),
            "K_commutes_with_H": bool(np.array_equal(
                symmetry @ square, square @ symmetry
            )),
        })
    def q_infinite(index: int) -> int:
        left = index <= 0 and index % 4 == 0
        right = index >= 6 and (index - 6) % 4 == 0
        return 1 if left or right else -1

    # The two tails are period four. Together with the five core sites, these
    # representatives prove Q_(6-i)=Q_i for every integer i.
    q_representatives = list(range(-4, 10))
    q_checks = [q_infinite(6 - index) == q_infinite(index) for index in q_representatives]
    tau = tau_window(6, low=-8, high=16)
    tau_anchor = tau[7] == -tau[0]
    return {
        "operator": "(Ku)_i=(-1)^i u_(9-i)",
        "q_reflection_identity": "Q_(6-i)=Q_i",
        "tau_reflection_identity": "tau_(7-i)=-tau_i",
        "q_identity_domain_partition": "i<=0 and i>=6 are period-4 tails; 1<=i<=5 is checked individually",
        "q_identity_representatives": q_representatives,
        "q_identity_representative_checks": q_checks,
        "tau_identity_anchor": {"index": 0, "tau_7": tau[7], "minus_tau_0": -tau[0]},
        "tau_identity_proof": "Q_(6-i)=Q_i plus tau_7=-tau_0 propagates tau_(7-i)=-tau_i by induction in both directions",
        "tau_identity_exact": all(q_checks) and tau_anchor,
        "window_records": records,
        "spectral_consequence": (
            "K maps every A-eigenvector at lambda to one at -lambda. The simple positive "
            "G6 Evans root therefore has a simple negative partner, and the corresponding "
            "H=A^2 eigenspace at c6 has rank exactly 2."
        ),
    }


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
    symmetry = anticommuting_symmetry_certificate()
    checks = {
        "exactly_two_resultant_candidates": total_candidates == 2,
        "both_candidate_intervals_isolate_one_factor_root": all(len(row["resultant_factors"]) == 1 for row in candidate_records),
        "both_unsquared_matchings_nonzero": all(row["matching_excludes_zero"] for row in candidate_records),
        "all_candidate_charts_valid": all(row["all_vectors_valid"] for row in candidate_records),
        "local_c6_unique_root_inherited": local["checks"]["derivative_positive"] and local["checks"]["left_sign_negative"] and local["checks"]["right_sign_positive"],
        "local_interval_matches": local["y_interval"] == [str(C6_LOWER), str(C6_UPPER)],
        "operator_norm_cap": 16 >= C6_UPPER,
        "negative_spectrum_bridge": (
            symmetry["tau_identity_exact"]
            and all(
                row["K_squared_is_minus_identity"]
                and row["K_anticommutes_with_A"]
                and row["K_commutes_with_H"]
                for row in symmetry["window_records"]
            )
        ),
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
            "Task 50's positive-lambda exact-rational interval Evans certificate has one simple zero in the c6 interval; "
            "its fixed-sign derivative excludes every further zero through c6_upper."
        ),
        "negative_spectrum_bridge": symmetry,
        "squared_level_multiplicity": 2,
        "global_argument": (
            "Every physical unsquared zero annihilates the exact stable-branch resultant. Sturm counting "
            "finds exactly two candidates on [c6_upper,16], and validated unsquared matching excludes both. "
            "The repeated-multiplier energy is represented by the confluent symmetric quotient and is not "
            "a resultant candidate. The exact anticommuting symmetry K supplies the negative-lambda "
            "chart and pairs the simple positive root with a simple negative root. Finally "
            "||A6||<=4 gives y=lambda^2<=16."
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
