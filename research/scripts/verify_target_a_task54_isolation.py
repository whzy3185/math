"""Independent reconstruction of the Task 54 G6 isolation certificate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from target_a_task50_g6_certificate import evans
from target_a_task50_interval import Interval
from target_a_task52_exact import elimination_resultant


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task54" / "certificates" / "g6_spectral_isolation.json"


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    eta = sp.Rational(1561, 200)
    c6_upper = sp.Rational(7905369311620328, 10**15)
    y = sp.symbols("y")
    _resultant, elimination = elimination_resultant(6)
    count = sum(
        int(sp.Poly(sp.sympify(row["polynomial"]), y).count_roots(eta, c6_upper))
        for row in elimination["factors"]
    )
    secondary = Interval(
        Fraction(780868668817504, 10**14),
        Fraction(780868668817506, 10**14),
    )
    chart_checks = []
    for rows in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
        matching, _defect, metadata = evans(secondary, gap=6, cofactor_rows=rows)
        chart_checks.append(
            matching.value.excludes_zero()
            and all(row["nonzero_components"] for row in metadata["cofactor_pivots"])
        )
    theta = Fraction(data["resolvent"]["theta"])
    perturbation = Fraction(data["resolvent"]["weight_perturbation_bound"])
    checks = {
        "full_gap_count_rebuilt": count == 2,
        "four_chart_unsquared_exclusion_rebuilt": all(chart_checks),
        "delta_rebuilt": Fraction(data["delta6"]) == Fraction(1, 100),
        "delta_above_bulk": Fraction(7905369311620327, 10**15) - Fraction(1, 100) > Fraction(1561, 200),
        "theta_rebuilt": theta == Fraction(1, 40000),
        "perturbation_rebuilt": perturbation == Fraction(16, 9999),
        "weighted_bound_rebuilt": 1 / (Fraction(1, 300) - perturbation) < 600,
        "stored_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


if __name__ == "__main__":
    verify()
    print("TARGET_A_TASK54_ISOLATION_VERIFY_PASS")
