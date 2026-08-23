"""Independent acceptance checker for Task 53 Gate A2."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

from target_a_task50_interval import Interval
from target_a_task53_grassmann import (
    evaluate_physical_section,
    factor_records,
    physical_section,
    relevant_sections,
    selected_sections,
    squared_elimination,
)


RESEARCH = Path(__file__).resolve().parents[1]
CERTIFICATE = RESEARCH / "proofs" / "task53" / "certificates" / "g6_grassmann_atlas.json"
LOWER = sp.Rational(7905369311620328, 10**15)
BRIDGE = Interval(Fraction(79157, 10**4), Fraction(79159, 10**4))


def verify(path: Path = CERTIFICATE) -> dict[str, bool]:
    data = json.loads(path.read_text(encoding="utf-8"))
    y = sp.symbols("y")
    sections = relevant_sections((0, 1, 3))
    independent = []
    for section in sections:
        numerator, _denominator = physical_section(section)
        factors = factor_records(squared_elimination(numerator), LOWER, sp.Integer(16))
        hits = [row for row in factors if row["roots_in_task_interval"]]
        independent.append(len(hits) == 1 and hits[0]["polynomial"] == "3*y**2 - 24*y + 2")
    bridge_sections = selected_sections((0, 1, 2), (0, 1), (0, 2))
    bridge_nonzero = [evaluate_physical_section(section, BRIDGE).excludes_zero() for section in bridge_sections]
    checks = {
        "artifact_has_two_planes_per_chart": all(len(chart["plane_records"]) == 2 for chart in data["atlas"]),
        "independent_candidate_reconstruction": all(independent),
        "candidate_interval_exact": sp.Poly(3 * y**2 - 24 * y + 2, y).count_roots(
            sp.Rational(BRIDGE.lo.numerator, BRIDGE.lo.denominator),
            sp.Rational(BRIDGE.hi.numerator, BRIDGE.hi.denominator),
        ) == 1,
        "bridge_reconstructed": all(bridge_nonzero),
        "three_chart_cover": len(data["atlas"]) == 3,
        "chart_names_bound": [chart["name"] for chart in data["atlas"]] == [
            "outer-left-013", "bridge-012", "outer-right-013"
        ],
        "chart_rows_bound": [
            [row["cofactor_rows"] for row in chart["plane_records"]] for chart in data["atlas"]
        ] == [[[0, 1, 3], [0, 1, 3]], [[0, 1, 2], [0, 1, 2]], [[0, 1, 3], [0, 1, 3]]],
        "branch_selector_bound": data["branch_selector"] == "larger_t_smaller_P",
        "normalization_is_explicit": all(
            row["normalized_chart_lower_bound"] == "1"
            for chart in data["atlas"] for row in chart["plane_records"]
        ),
        "no_uncovered_points": data["uncovered_points"] == [],
        "g6_cut_bound": data["status"] == "GATE_A2_PASS" and "cut [-8,14)" in data["physical_matching"],
        "artifact_checks_true": all(data["checks"].values()),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return checks


def main() -> None:
    verify()
    print("TARGET_A_TASK53_A2_VERIFY_PASS")


if __name__ == "__main__":
    main()
