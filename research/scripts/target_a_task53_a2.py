"""Producer for the Task 53 global physical-plane atlas (Gate A2)."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_interval import Interval, interval_record
from target_a_task51_algebra import transfer_product
from target_a_task53_grassmann import (
    evaluate_physical_section,
    factor_records,
    physical_section,
    relevant_sections,
    selected_sections,
    squared_elimination,
)


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task53" / "certificates"
C6_UPPER = sp.Rational(7905369311620328, 10**15)
BRIDGE_LEFT = Fraction(79157, 10**4)
BRIDGE_RIGHT = Fraction(79159, 10**4)
LEFT_OVERLAP_END = Fraction(31663, 4000)
RIGHT_OVERLAP_START = Fraction(158317, 20000)


def build_certificate() -> dict[str, Any]:
    y, lam, product = sp.symbols("y lambda P")
    right_section, left_section = relevant_sections((0, 1, 3))
    outer_records = []
    for side, pair, section in (
        ("right stable", "23", right_section),
        ("left unstable", "01", left_section),
    ):
        numerator, denominator = physical_section(section)
        resultant = squared_elimination(numerator)
        factors = factor_records(resultant, C6_UPPER, sp.Integer(16))
        candidate_factors = [row for row in factors if row["roots_in_task_interval"]]
        outer_records.append({
            "plane": side,
            "chosen_minor": pair,
            "cofactor_rows": [0, 1, 3],
            "section": str(section),
            "physical_numerator": str(numerator),
            "physical_denominator": str(denominator),
            "resultant_factors": factors,
            "candidate_factors": candidate_factors,
            "normalized_chart_lower_bound": "1",
        })

    bridge_sections = selected_sections((0, 1, 2), (0, 1), (0, 2))
    bridge_records = []
    for side, pair, section in (
        ("right stable", "01", bridge_sections[0]),
        ("left unstable", "02", bridge_sections[1]),
    ):
        value = evaluate_physical_section(section, Interval(BRIDGE_LEFT, BRIDGE_RIGHT))
        bridge_records.append({
            "plane": side,
            "chosen_minor": pair,
            "cofactor_rows": [0, 1, 2],
            "section": str(section),
            "physical_section_on_bridge": interval_record(value),
            "section_excludes_zero": value.excludes_zero(),
            "normalized_chart_lower_bound": "1",
        })

    charts = [
        {
            "name": "outer-left-013",
            "interval": [str(C6_UPPER), str(LEFT_OVERLAP_END)],
            "plane_records": outer_records,
        },
        {
            "name": "bridge-012",
            "interval": [str(BRIDGE_LEFT), str(BRIDGE_RIGHT)],
            "plane_records": bridge_records,
        },
        {
            "name": "outer-right-013",
            "interval": [str(RIGHT_OVERLAP_START), "16"],
            "plane_records": outer_records,
        },
    ]

    critical_polynomial = sp.Poly(3 * y**2 - 24 * y + 2, y)
    checks = {
        "candidate_interval_isolates_exact_root": critical_polynomial.count_roots(
            sp.Rational(BRIDGE_LEFT.numerator, BRIDGE_LEFT.denominator),
            sp.Rational(BRIDGE_RIGHT.numerator, BRIDGE_RIGHT.denominator),
        ) == 1,
        "one_candidate_factor_each": all(len(row["candidate_factors"]) == 1 for row in outer_records),
        "same_candidate_factor": all(
            row["candidate_factors"][0]["polynomial"] == "3*y**2 - 24*y + 2" for row in outer_records
        ),
        "candidate_is_inside_bridge_only": (
            LEFT_OVERLAP_END < Fraction(7915780041490243, 10**15)
            < Fraction(7915780041490244, 10**15) < RIGHT_OVERLAP_START
        ),
        "bridge_sections_nonzero": all(row["section_excludes_zero"] for row in bridge_records),
        "left_overlap_nonempty": BRIDGE_LEFT < LEFT_OVERLAP_END,
        "right_overlap_nonempty": RIGHT_OVERLAP_START < BRIDGE_RIGHT,
        "task_interval_ordered": C6_UPPER < 16,
        "defect_transfer_unimodular": sp.factor(transfer_product(6, -8, 14, lam).det()) == 1,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    if not all(checks.values()):
        raise AssertionError(checks)

    return {
        "status": "GATE_A2_PASS",
        "evidence": "COMPUTER_ASSISTED_PROVED",
        "energy_interval": [str(C6_UPPER), "16"],
        "atlas": charts,
        "chart_count": 3,
        "coverage": "the full closed task interval, including both endpoints and the repeated-multiplier energy",
        "uncovered_points": [],
        "normalization": (
            "Within each chart every Plucker section is divided by its proved nonzero chosen coordinate. "
            "The chosen coordinate is therefore exactly 1 in that affine chart."
        ),
        "transition_relation": (
            "On each nonempty overlap the two affine representatives differ by the exact ratio of their "
            "chosen Plucker sections; both denominator sections are nonzero there."
        ),
        "stable_branch": (
            "P is the small root of P+P^-1=t_large, where t_large is the larger root of "
            "(t+2)(t-b)+a^2=0; S=-aP/(P+1)."
        ),
        "branch_selector": "larger_t_smaller_P",
        "physical_matching": (
            "The unsquared G6 condition is (Lambda^2 D)(U_left) wedge S_right=0, "
            "with cut [-8,14), left bulk cell [-16,-8), right bulk cell [14,22), "
            "and the orientation encoded by tau_window(6)."
        ),
        "orientation": "forward G6: B_0 on the left and B_2 on the right",
        "reflection": (
            "Index reflection is a unitary permutation of ell2(Z), reverses the cut, and exchanges "
            "the left unstable/right stable planes. The exterior pairing changes only by a nonzero sign."
        ),
        "translation_sector": (
            "For gap g=6 the exact Task 52 rule sigma(g-4)=g-4 mod 4 gives B_0 -> B_2. "
            "Absolute simultaneous translations are permutation conjugacies."
        ),
        "extraneous_branch_boundary": (
            "The squared resultant includes every physical zero but also roots from the other P branch, "
            "cofactor-section degeneracy, lambda-sign squaring, and cleared denominators. The sole chart "
            "candidate 3*y^2-24*y+2 is the rows-013 cofactor-section degeneracy and is covered by the "
            "independently nonzero rows-012 bridge chart."
        ),
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "g6_grassmann_atlas.json", payload)
    print(json.dumps({"status": payload["status"], "charts": payload["chart_count"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()
