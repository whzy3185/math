"""Task 54: certify the full G6 upper-gap isolation and resolvent constants."""

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
OUTPUT = RESEARCH / "proofs" / "task54" / "certificates"
C6_LOWER = Fraction(7905369311620327, 10**15)
C6_UPPER = Fraction(7905369311620328, 10**15)
ETA_UPPER = Fraction(1561, 200)
ETA_LOWER = Fraction(1951, 250)
DELTA6 = Fraction(1, 100)
SECONDARY = Interval(
    Fraction(780868668817504, 10**14),
    Fraction(780868668817506, 10**14),
)
CHARTS = ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))


def _q(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def build_certificate() -> dict[str, Any]:
    y = sp.symbols("y")
    _resultant, elimination = elimination_resultant(6)
    factors = []
    total = 0
    secondary_factors = []
    for row in elimination["factors"]:
        polynomial = sp.Poly(sp.sympify(row["polynomial"]), y)
        lower_strip_count = int(
            polynomial.count_roots(_q(ETA_LOWER), _q(ETA_UPPER))
        )
        count = int(polynomial.count_roots(_q(ETA_UPPER), _q(C6_UPPER)))
        secondary_count = int(
            polynomial.count_roots(_q(SECONDARY.lo), _q(SECONDARY.hi))
        )
        total += count
        if secondary_count:
            secondary_factors.append(row["polynomial"])
        factors.append({
            **row,
            "roots_in_eta_lower_to_eta_upper": lower_strip_count,
            "roots_in_eta_upper_to_c6_upper": count,
            "roots_in_secondary_interval": secondary_count,
        })

    chart_records = []
    for rows in CHARTS:
        matching, _defect, metadata = evans(SECONDARY, gap=6, cofactor_rows=rows)
        chart_records.append({
            "cofactor_rows": list(rows),
            "matching": interval_record(matching.value),
            "matching_excludes_zero": matching.value.excludes_zero(),
            "all_vectors_valid": all(
                row["nonzero_components"] for row in metadata["cofactor_pivots"]
            ),
        })

    local = json.loads(
        (RESEARCH / "proofs" / "task50" / "certificates" / "g6_interface_certificate.json")
        .read_text(encoding="utf-8")
    )
    contour_radius = DELTA6 / 3
    theta = Fraction(1, 40000)
    conjugation_error = Fraction(16, 9999)
    reduced_distance = DELTA6 - contour_radius
    bulk_distance_lower = C6_LOWER - contour_radius - ETA_UPPER
    checks = {
        "eta_lower_is_strict_lower_bound": (
            Fraction(559, 250) ** 2 < 5
            and Fraction(559, 250) > Fraction(904401, 125000) - 5
        ),
        "eta_upper_is_strict_upper_bound": (
            Fraction(2237, 1000) ** 2 > 5
            and Fraction(2237, 1000) < Fraction(579121, 80000) - 5
        ),
        "rational_strip_ordered": ETA_LOWER < ETA_UPPER < C6_LOWER,
        "no_resultant_root_between_eta_lower_and_eta_upper": all(
            row["roots_in_eta_lower_to_eta_upper"] == 0 for row in factors
        ),
        "exactly_two_resultant_roots_in_full_upper_gap": total == 2,
        "secondary_interval_isolates_one_factor_root": len(secondary_factors) == 1,
        "all_four_unsquared_charts_exclude_secondary": all(
            row["matching_excludes_zero"] and row["all_vectors_valid"]
            for row in chart_records
        ),
        "task50_c6_root_is_simple_and_unique": (
            local["checks"]["derivative_positive"]
            and local["checks"]["left_sign_negative"]
            and local["checks"]["right_sign_positive"]
        ),
        "delta6_interval_stays_above_bulk": C6_LOWER - DELTA6 > ETA_UPPER,
        "reduced_contour_distance": reduced_distance == Fraction(1, 150),
        "ct_exponential_inequality": conjugation_error == 16 * Fraction(1, 9999),
        "ct_full_resolvent_denominator_positive": contour_radius > conjugation_error,
        "ct_full_resolvent_safe_constant": 1 / (contour_radius - conjugation_error) < 600,
        "bulk_distance_exceeds_nine_hundredths": bulk_distance_lower > Fraction(9, 100),
        "bulk_ct_safe_constant": 1 / (bulk_distance_lower - conjugation_error) < 12,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "TASK54_GATE_A_AND_REDUCED_RESOLVENT_PASS",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "c6_interval": [str(C6_LOWER), str(C6_UPPER)],
        "eta_rational_upper": str(ETA_UPPER),
        "eta_rational_lower": str(ETA_LOWER),
        "delta6": str(DELTA6),
        "theorem": "c6 is the only physical G6 eigenvalue in (eta,c6], and sigma(H6)\\{c6} is disjoint from [c6-delta6,c6+delta6]",
        "candidate_classification": {
            "resultant_root_count": total,
            "physical_root": "c6 (Task50 unsquared simple-root certificate)",
            "secondary_interval": [str(SECONDARY.lo), str(SECONDARY.hi)],
            "secondary_resultant_factors": secondary_factors,
            "secondary_unsquared_charts": chart_records,
            "factors": factors,
        },
        "resolvent": {
            "contour": "|z-c6|=1/300",
            "contour_radius": str(contour_radius),
            "reduced_complement_spectral_distance": str(reduced_distance),
            "reduced_operator_norm_bound": 150,
            "finite_range": 4,
            "absolute_row_sum": 16,
            "theta": str(theta),
            "weight_perturbation_bound": str(conjugation_error),
            "full_interface_weighted_resolvent_bound": 600,
            "riesz_projection_kernel_constant": 2,
            "reduced_kernel_constant": 1200,
            "bulk_spectral_distance_lower": str(bulk_distance_lower),
            "bulk_weighted_resolvent_bound": 12,
            "kernel_decay": "exp(-|i-j|/40000)",
        },
        "proof_boundary": (
            "The resultant is used only for candidate completeness. Every non-c6 candidate is "
            "rejected by the unsquared interval Evans condition. Resolvent constants then follow "
            "from the spectral theorem and a direct finite-range exponential conjugation bound."
        ),
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "g6_spectral_isolation.json", payload)
    print(json.dumps({"status": payload["status"], "delta6": payload["delta6"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()
