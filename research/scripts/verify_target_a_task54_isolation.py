"""Independent reconstruction of the Task 54 G6 isolation certificate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from target_a_task50_g6_certificate import evans
from target_a_task50_interval import Interval, interval_record
from target_a_task52_exact import elimination_resultant
from verify_target_a_task50_interface import verify_interface


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task54" / "certificates" / "g6_spectral_isolation.json"


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    expected_check_keys = {
        "eta_lower_is_strict_lower_bound", "eta_upper_is_strict_upper_bound",
        "rational_strip_ordered", "no_resultant_root_between_eta_lower_and_eta_upper",
        "exactly_two_resultant_roots_in_full_upper_gap",
        "secondary_interval_isolates_one_factor_root",
        "all_four_unsquared_charts_exclude_secondary",
        "task50_c6_root_is_simple_and_unique", "delta6_interval_stays_above_bulk",
        "reduced_contour_distance", "ct_exponential_inequality",
        "ct_full_resolvent_denominator_positive", "ct_full_resolvent_safe_constant",
        "bulk_distance_exceeds_nine_hundredths", "bulk_ct_safe_constant",
    }
    factor_rows = data["candidate_classification"]["factors"]
    resolvent = data["resolvent"]
    preflight = {
        "status_exact": data["status"] == "TASK54_GATE_A_AND_REDUCED_RESOLVENT_PASS",
        "evidence_exact": data["evidence"] == "COMPUTER_ASSISTED_PROVED",
        "stored_intervals_exact": (
            data["c6_interval"]
            == ["7905369311620327/1000000000000000", "988171163952541/125000000000000"]
            and data["candidate_classification"]["secondary_interval"]
            == ["24402145900547/3125000000000", "390434334408753/50000000000000"]
            and data["eta_rational_lower"] == "1951/250"
            and data["eta_rational_upper"] == "1561/200"
            and data["delta6"] == "1/100"
        ),
        "stored_candidate_counts_exact": (
            data["candidate_classification"]["resultant_root_count"] == 2
            and len(factor_rows) == 5
            and sum(row["roots_in_eta_lower_to_eta_upper"] for row in factor_rows) == 0
            and sum(row["roots_in_eta_upper_to_c6_upper"] for row in factor_rows) == 2
        ),
        "stored_theorem_scope_exact": data["theorem"]
        == "c6 is the only physical G6 eigenvalue in (eta,c6], and sigma(H6)\\{c6} is disjoint from [c6-delta6,c6+delta6]",
        "stored_resolvent_constants_exact": resolvent == {
            "contour": "|z-c6|=1/300",
            "contour_radius": "1/300",
            "reduced_complement_spectral_distance": "1/150",
            "reduced_operator_norm_bound": 150,
            "finite_range": 4,
            "absolute_row_sum": 16,
            "theta": "1/40000",
            "weight_perturbation_bound": "16/9999",
            "full_interface_weighted_resolvent_bound": 600,
            "riesz_projection_kernel_constant": 2,
            "reduced_kernel_constant": 1200,
            "bulk_spectral_distance_lower": "291107934860981/3000000000000000",
            "bulk_weighted_resolvent_bound": 12,
            "kernel_decay": "exp(-|i-j|/40000)",
        },
        "stored_checks_exact_and_true": (
            set(data["checks"]) == expected_check_keys and all(data["checks"].values())
        ),
    }
    if not all(preflight.values()):
        raise AssertionError(preflight)
    eta = sp.Rational(1561, 200)
    eta_lower = sp.Rational(1951, 250)
    c6_upper = sp.Rational(7905369311620328, 10**15)
    y = sp.symbols("y")
    secondary = Interval(
        Fraction(780868668817504, 10**14),
        Fraction(780868668817506, 10**14),
    )
    _resultant, elimination = elimination_resultant(6)
    expected_factors = []
    for row in elimination["factors"]:
        polynomial = sp.Poly(sp.sympify(row["polynomial"]), y)
        expected_factors.append({
            **row,
            "roots_in_eta_lower_to_eta_upper": int(polynomial.count_roots(eta_lower, eta)),
            "roots_in_eta_upper_to_c6_upper": int(polynomial.count_roots(eta, c6_upper)),
            "roots_in_secondary_interval": int(
                polynomial.count_roots(sp.Rational(secondary.lo), sp.Rational(secondary.hi))
            ),
        })
    count = sum(
        int(sp.Poly(sp.sympify(row["polynomial"]), y).count_roots(eta, c6_upper))
        for row in elimination["factors"]
    )
    lower_strip_count = sum(
        int(sp.Poly(sp.sympify(row["polynomial"]), y).count_roots(eta_lower, eta))
        for row in elimination["factors"]
    )
    chart_checks = []
    stored_charts = data["candidate_classification"]["secondary_unsquared_charts"]
    for index, rows in enumerate(((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3))):
        matching, _defect, metadata = evans(secondary, gap=6, cofactor_rows=rows)
        expected_chart = {
            "cofactor_rows": list(rows),
            "matching": interval_record(matching.value),
            "matching_excludes_zero": matching.value.excludes_zero(),
            "all_vectors_valid": all(
                row["nonzero_components"] for row in metadata["cofactor_pivots"]
            ),
        }
        chart_checks.append(
            matching.value.excludes_zero()
            and all(row["nonzero_components"] for row in metadata["cofactor_pivots"])
            and stored_charts[index] == expected_chart
        )
    theta = Fraction(data["resolvent"]["theta"])
    perturbation = Fraction(data["resolvent"]["weight_perturbation_bound"])
    checks = {
        **preflight,
        "full_gap_count_rebuilt": count == 2,
        "lower_eta_strip_rebuilt": lower_strip_count == 0,
        "factor_table_rebuilt": factor_rows == expected_factors,
        "eta_lower_bound_rebuilt": (
            Fraction(559, 250) ** 2 < 5
            and Fraction(559, 250) > Fraction(904401, 125000) - 5
        ),
        "eta_upper_bound_rebuilt": (
            Fraction(2237, 1000) ** 2 > 5
            and Fraction(2237, 1000) < Fraction(579121, 80000) - 5
        ),
        "four_chart_unsquared_exclusion_rebuilt": all(chart_checks),
        "task50_physical_root_rebuilt": verify_interface(
            "g6_interface_certificate.json", 6
        )["status"] == "INDEPENDENT_COORDINATE_CHECK_PASS",
        "delta_rebuilt": Fraction(data["delta6"]) == Fraction(1, 100),
        "delta_above_bulk": Fraction(7905369311620327, 10**15) - Fraction(1, 100) > Fraction(1561, 200),
        "theta_rebuilt": theta == Fraction(1, 40000),
        "perturbation_rebuilt": perturbation == Fraction(16, 9999),
        "weighted_bound_rebuilt": 1 / (Fraction(1, 300) - perturbation) < 600,
        "reduced_constants_rebuilt": (
            1 / Fraction(1, 150) == 150
            and Fraction(1, 300) * 600 == 2
            and 600 + 2 / Fraction(1, 300) == 1200
            and 1
            / (Fraction(resolvent["bulk_spectral_distance_lower"]) - perturbation)
            < 12
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


if __name__ == "__main__":
    verify()
    print("TARGET_A_TASK54_ISOLATION_VERIFY_PASS")
