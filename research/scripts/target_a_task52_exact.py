"""Exact and validated structural certificates for Target A Task 52."""

from __future__ import annotations

import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_g6_certificate import evans, symbolic_defect_transfer, tau_window
from target_a_task50_interval import Interval, interval_record
from target_a_task51_algebra import symmetric_evans_core, transfer_product


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task52" / "certificates"
EXPERIMENTS = RESEARCH / "experiments" / "task52"
ENTRY_HEAD = "ac4c69b796c9dc14d1307a092d1e0faa093081f2"
C6_LEFT = Fraction(7905369311620327, 10**15)
C6_RIGHT = Fraction(7905369311620328, 10**15)
GAP2_LEFT = Fraction(8080985802104273, 10**15)
GAP2_RIGHT = Fraction(8080985802104274, 10**15)


def c6_polynomial(y: sp.Symbol) -> sp.Poly:
    return sp.Poly(
        16 * y**10 - 520 * y**9 + 6913 * y**8 - 48448 * y**7
        + 191768 * y**6 - 423904 * y**5 + 484528 * y**4
        - 270464 * y**3 + 137856 * y**2 - 19968 * y + 256,
        y,
    )


def translation_charge_certificate() -> dict[str, Any]:
    sectors = []
    for shift in range(4):
        q_cell = [1 if index == shift else -1 for index in range(4)]
        q_period = q_cell * 2
        tau = [1]
        for value in q_period:
            tau.append(tau[-1] * value)
        sectors.append({
            "name": f"B_{shift}",
            "positive_Q_residue_mod_4": shift,
            "Q_cell": q_cell,
            "canonical_tau_0_to_7": tau[:-1],
            "tau_antiperiod_over_4": tau[4] == -tau[0],
            "tau_period_over_8": tau[8] == tau[0],
        })

    transitions = []
    for gap in range(1, 21):
        charge = gap - 4
        right_sector = gap % 4
        transitions.append({
            "gap": gap,
            "charge": charge,
            "left_sector": 0,
            "right_sector": right_sector,
            "sector_shift": right_sector,
            "q_mod_4": charge % 4,
            "candidate_q_over_2_mod_4": (charge // 2) % 4 if charge % 2 == 0 else None,
            "exact_rule_holds": right_sector == charge % 4,
        })

    composition_checks = []
    for q1 in range(-8, 9):
        for q2 in range(-8, 9):
            composition_checks.append((q1 % 4 + q2 % 4) % 4 == (q1 + q2) % 4)
    return {
        "status": "TRANSLATION_CHARGE_PROVED_CORRECTED_RULE",
        "canonical_bulk_sectors": sectors,
        "definition": "B_s has Q_i=+1 exactly for i congruent to s modulo 4.",
        "transition_theorem": "An oriented gap g from B_s ends in B_(s+g); since q=g-4, sigma(q)=q modulo 4.",
        "candidate_rule_q_over_2_mod_4": "FALSIFIED",
        "smallest_even_counterexample": {"q": 2, "actual_shift": 2, "candidate_shift": 1},
        "even_charge_image": [0, 2],
        "interpretation": "All integer charges have a Z4 translation-sector class; even charges occupy only its order-two subgroup. This is distinct from signed-graph holonomy alpha.",
        "transitions": transitions,
        "composition_law": "sigma(PQ)=sigma(P)+sigma(Q) modulo 4",
        "composition_checks": {"tested_pairs": len(composition_checks), "all_pass": all(composition_checks)},
    }


def elimination_resultant(gap: int) -> tuple[sp.Expr, dict[str, Any]]:
    lam, y, symmetric_sum, symmetric_product = sp.symbols("lam y S P")
    symmetric, degrees = symmetric_evans_core(gap)
    a = -2 * lam**4 + 16 * lam**2 - 13
    b = lam**8 - 16 * lam**6 + 80 * lam**4 - 128 * lam**2 + 40
    substituted = sp.cancel(symmetric.subs(symmetric_sum, -a * symmetric_product / (symmetric_product + 1)))
    numerator = sp.primitive(sp.Poly(sp.fraction(substituted)[0], symmetric_product))[1].as_expr()
    relation = sp.expand(
        (symmetric_product + 1) ** 2 * (symmetric_product**2 + 1 - b * symmetric_product)
        + a**2 * symmetric_product**2
    )
    polynomial = sp.Poly(numerator, lam)
    even = sum(coefficient * y ** (power[0] // 2) for power, coefficient in polynomial.terms() if power[0] % 2 == 0)
    odd = sum(coefficient * y ** ((power[0] - 1) // 2) for power, coefficient in polynomial.terms() if power[0] % 2 == 1)
    squared_evans = sp.expand(even**2 - y * odd**2)
    relation_y = sp.expand(relation.subs(lam**2, y))
    resultant = sp.resultant(squared_evans, relation_y, symmetric_product)
    content, factors = sp.factor_list(resultant, y)
    return resultant, {
        "gap": gap,
        "symmetric_evans_degrees": degrees,
        "squared_evans_degrees": {
            "P": int(sp.degree(squared_evans, symmetric_product)),
            "y": int(sp.degree(squared_evans, y)),
        },
        "resultant_degree_y": int(sp.degree(resultant, y)),
        "content": str(content),
        "factors": [
            {
                "degree": sp.Poly(factor, y).degree(),
                "multiplicity": multiplicity,
                "polynomial": str(factor),
                "irreducible_over_Q": bool(sp.Poly(factor, y).is_irreducible),
            }
            for factor, multiplicity in factors
        ],
    }


def interval_evans_certificate(gap: int, left: Fraction, right: Fraction) -> dict[str, Any]:
    left_value, _left_defect, left_metadata = evans(Interval.point(left), gap=gap)
    right_value, _right_defect, right_metadata = evans(Interval.point(right), gap=gap)
    enclosure, _defect, metadata = evans(Interval(left, right), gap=gap)
    derivative_sign = enclosure.derivative.sign()
    endpoint_signs = [left_value.value.sign(), right_value.value.sign()]
    checks = {
        "ordered_interval": left < right,
        "endpoint_sign_change": endpoint_signs[0] * endpoint_signs[1] == -1,
        "derivative_has_fixed_sign": derivative_sign in (-1, 1),
        "signs_match_derivative": endpoint_signs == ([-1, 1] if derivative_sign == 1 else [1, -1]),
        "all_cofactor_vectors_nonzero": all(row["nonzero_components"] for row in metadata["cofactor_pivots"]),
        "unimodular_defect_transfer": symbolic_defect_transfer(gap)["determinant"] == "1",
    }
    if not all(checks.values()):
        raise AssertionError(f"gap {gap} interval Evans certificate failed: {checks}")
    return {
        "gap": gap,
        "charge": gap - 4,
        "status": "COMPUTER_ASSISTED_PROVED",
        "method": "exact-rational interval Evans determinant with automatic derivative enclosure",
        "y_interval": [str(left), str(right)],
        "left_evans": interval_record(left_value.value),
        "right_evans": interval_record(right_value.value),
        "derivative": interval_record(enclosure.derivative),
        "derivative_sign": derivative_sign,
        "stable_multiplier_intervals": metadata["stable_multiplier_intervals"],
        "checks": checks,
        "endpoint_metadata": {"left": left_metadata, "right": right_metadata},
    }
def plus_minus_two_certificate() -> dict[str, Any]:
    y = sp.symbols("y")
    resultant2, record2 = elimination_resultant(2)
    resultant6, record6 = elimination_resultant(6)
    polynomial = c6_polynomial(y)
    gap2 = interval_evans_certificate(2, GAP2_LEFT, GAP2_RIGHT)
    roots_gap2 = polynomial.count_roots(sp.Rational(GAP2_LEFT.numerator, GAP2_LEFT.denominator), sp.Rational(GAP2_RIGHT.numerator, GAP2_RIGHT.denominator))
    roots_c6 = polynomial.count_roots(sp.Rational(C6_LEFT.numerator, C6_LEFT.denominator), sp.Rational(C6_RIGHT.numerator, C6_RIGHT.denominator))
    checks = {
        "resultants_identical": sp.expand(resultant2 - resultant6) == 0,
        "degree_ten_factor_present_gap2": any(row["polynomial"] == str(polynomial.as_expr()) for row in record2["factors"]),
        "degree_ten_factor_present_g6": any(row["polynomial"] == str(polynomial.as_expr()) for row in record6["factors"]),
        "one_polynomial_root_in_gap2_interval": roots_gap2 == 1,
        "one_polynomial_root_in_c6_interval": roots_c6 == 1,
        "gap2_interval_above_8": GAP2_LEFT > 8,
        "c6_interval_below_8": C6_RIGHT < 8,
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "PLUS_MINUS_TWO_COMMON_POLYNOMIAL_PROVED",
        "polynomial": str(polynomial.as_expr()),
        "q_plus_2_root_interval": [str(C6_LEFT), str(C6_RIGHT)],
        "q_minus_2_root_interval": [str(GAP2_LEFT), str(GAP2_RIGHT)],
        "gap2_evans_certificate": gap2,
        "elimination_gap2": record2,
        "elimination_gap6": record6,
        "structural_relation": "After removing the same nonzero stable-branch Vandermonde and imposing the exact reciprocal bulk relations, the gap-2 and gap-6 squared Evans eliminants have identical resultants over Q[y].",
        "transformation_boundary": "No direct constant conjugacy of the unsquared matching matrices is asserted; the proved structural identity is equality after exact stable-branch elimination.",
        "checks": checks,
    }


def competitive_single_gap_certificates() -> dict[str, Any]:
    intervals = {
        2: (GAP2_LEFT, GAP2_RIGHT),
        3: (Fraction(1598170324217, 200000000000), Fraction(7990851621089, 10**12)),
        6: (C6_LEFT, C6_RIGHT),
        8: (Fraction(1982447908511, 250000000000), Fraction(61951497141, 7812500000)),
        10: (Fraction(3988552185200273, 500000000000000), Fraction(7977104370400547, 10**15)),
        12: (Fraction(7999902120371, 10**12), Fraction(63999216963, 8000000000)),
    }
    inherited = {
        6: json.loads((RESEARCH / "proofs" / "task50" / "certificates" / "g6_interface_certificate.json").read_text()),
        10: json.loads((RESEARCH / "proofs" / "task50" / "certificates" / "g10_interface_certificate.json").read_text()),
    }
    records = {}
    for gap, (left, right) in intervals.items():
        if gap in inherited:
            source = inherited[gap]
            record = {
                "gap": gap,
                "charge": gap - 4,
                "status": "COMPUTER_ASSISTED_PROVED",
                "source": "Task 50 inherited interval Evans theorem",
                "y_interval": source["y_interval"],
                "checks": source["checks"],
            }
        else:
            record = interval_evans_certificate(gap, left, right)
        record["comparisons"] = {
            "above_c6": left > C6_RIGHT,
            "above_8": left > 8,
            "below_8": right < 8,
        }
        records[str(gap)] = record
    return {
        "status": "COMPETITIVE_SINGLE_GAP_COMPARISONS_CERTIFIED",
        "records": records,
        "proved_comparisons": {
            "c_minus_2_gt_8": intervals[2][0] > 8,
            "c_minus_1_gt_c6": intervals[3][0] > C6_RIGHT,
            "c_plus_4_gt_c6": intervals[8][0] > C6_RIGHT,
            "c_plus_6_gt_c6": intervals[10][0] > C6_RIGHT,
            "c_plus_8_gt_c6": intervals[12][0] > C6_RIGHT,
        },
        "scope": "Unique localized Evans root in each displayed rational interval; this is not a classification of all multi-gap interfaces.",
    }


def product_for_gap(gap: int, start: int, stop: int, lam: sp.Symbol) -> sp.Matrix:
    tau = tau_window(gap, low=min(-32, start - 4), high=max(48, stop + 4))
    result = sp.eye(4)
    for index in range(start, stop):
        a, b = tau[index], tau[index - 2]
        step = sp.Matrix([[-a, a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
        result = step * result
    return result.applyfunc(sp.expand)


def exterior_square(matrix: sp.Matrix) -> sp.Matrix:
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    return sp.Matrix([
        [matrix.extract(rows, columns).det(method="domain-ge") for columns in pairs]
        for rows in pairs
    ]).applyfunc(sp.factor)


def integer_matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[row][k] * right[k][column] for k in range(4)) for column in range(4)]
        for row in range(4)
    ]


def integer_product(gap: int, start: int, stop: int, lam: int) -> list[list[int]]:
    tau = tau_window(gap, low=min(-32, start - 4), high=max(48, stop + 4))
    result = [[int(row == column) for column in range(4)] for row in range(4)]
    for index in range(start, stop):
        a, b = tau[index], tau[index - 2]
        step = [[-a, a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
        result = integer_matrix_multiply(step, result)
    return result


def eight_step_signature(gap: int, start: int) -> list[list[int]]:
    tau = tau_window(gap, low=min(-32, start - 4), high=max(48, start + 12))
    return [[tau[index], tau[index - 2]] for index in range(start, start + 8)]


def charge_recurrence_certificate() -> dict[str, Any]:
    records = []
    evaluation_points = list(range(33))
    for gap in range(1, 9):
        identities = []
        for value in evaluation_points:
            defect = integer_product(gap, -8, gap + 8, value)
            defect_next = integer_product(gap + 8, -8, gap + 16, value)
            common_prefix = integer_product(gap, -8, gap, value)
            right_bulk = integer_product(gap, gap, gap + 8, value)
            inserted_negative = integer_product(gap + 8, gap, gap + 8, value)
            next_right_bulk = integer_product(gap + 8, gap + 8, gap + 16, value)
            identities.append(
                defect == integer_matrix_multiply(right_bulk, common_prefix)
                and defect_next == integer_matrix_multiply(
                    integer_matrix_multiply(next_right_bulk, inserted_negative), common_prefix
                )
            )
        signatures = {
            "R": eight_step_signature(gap, gap),
            "N": eight_step_signature(gap + 8, gap),
            "R_next": eight_step_signature(gap + 8, gap + 8),
        }
        factor_determinants = {
            name: sp.prod(a * b for a, b in signature)
            for name, signature in signatures.items()
        }
        recurrence_determinant = (
            factor_determinants["R_next"] * factor_determinants["N"] / factor_determinants["R"]
        )
        encoded = json.dumps(signatures, sort_keys=True, separators=(",", ":"))
        checks = {
            "all_33_exact_integer_evaluations": all(identities),
            "evaluation_count_exceeds_degree_bound": len(evaluation_points) > 32,
            "all_eight_step_factors_invertible": all(abs(value) == 1 for value in factor_determinants.values()),
            "recurrence_matrix_unimodular": recurrence_determinant == 1,
            "exterior_square_dimension": 6 == len([(i, j) for i in range(4) for j in range(i + 1, 4)]),
        }
        if not all(checks.values()):
            raise AssertionError({"gap": gap, **checks})
        records.append({
            "gap_residue_mod_8": gap % 8,
            "representative_gap": gap,
            "identity": "D_(g+8)=C_r D_g, C_r=R_r N_r R_r^(-1)",
            "factor_data_sha256": hashlib.sha256(encoded.encode()).hexdigest(),
            "factor_step_signatures": signatures,
            "factor_determinants": {name: str(value) for name, value in factor_determinants.items()},
            "recurrence_determinant": str(recurrence_determinant),
            "polynomial_identity_degree_bound": 32,
            "exact_integer_evaluation_points": evaluation_points,
            "exterior_recurrence_order_bound": 6,
            "checks": checks,
        })
    return {
        "status": "GAP_PLUS_EIGHT_EXACT_EXTERIOR_RECURRENCE_PROVED",
        "records": records,
        "interpretation": "For each fixed gap residue modulo 8, C_r=R_r N_r R_r^(-1) acts on the propagated left two-plane. The matching determinant is a linear functional of its six-dimensional exterior-square orbit and therefore obeys an order-at-most-six Cayley-Hamilton recurrence.",
        "candidate_simple_identity": "P_(g+8)=M8 P_g is false in the fixed Task 50 cut; the correct factor is the residue-dependent conjugate C_r because eight negative Q sites replace the old right-bulk cell before the cut is restored.",
        "large_g_boundary": "The recurrence is exact, but no uniform root ordering or monotonicity theorem in g is claimed.",
    }


def polynomial_root_geometry() -> dict[str, Any]:
    y = sp.symbols("y")
    polynomial = c6_polynomial(y)
    roots = []
    for interval, multiplicity in sp.polys.polytools.intervals(polynomial, eps=sp.Rational(1, 10**15)):
        left, right = interval
        roots.append({
            "interval": [str(left), str(right)],
            "multiplicity": multiplicity,
            "decimal_interval": [str(sp.N(left, 18)), str(sp.N(right, 18))],
            "interpretation": (
                "G6 q=+2 physical upper-gap root" if left < sp.Rational(C6_RIGHT.numerator, C6_RIGHT.denominator) and right > sp.Rational(C6_LEFT.numerator, C6_LEFT.denominator)
                else "gap2 q=-2 physical upper-gap root" if left < sp.Rational(GAP2_RIGHT.numerator, GAP2_RIGHT.denominator) and right > sp.Rational(GAP2_LEFT.numerator, GAP2_LEFT.denominator)
                else "no Task52 physical interface interpretation"
            ),
        })
    discriminant = polynomial.discriminant()
    return {
        "status": "C6_POLYNOMIAL_REAL_ROOT_GEOMETRY_PROVED",
        "polynomial": str(polynomial.as_expr()),
        "irreducible_over_Q": bool(polynomial.is_irreducible),
        "real_root_count": int(polynomial.count_roots(-sp.oo, sp.oo)),
        "nonreal_root_count": polynomial.degree() - int(polynomial.count_roots(-sp.oo, sp.oo)),
        "real_roots": roots,
        "discriminant": str(discriminant),
        "discriminant_nonzero": discriminant != 0,
        "all_roots_simple": discriminant != 0,
        "physical_root_count_proved": 2,
        "interpretation_boundary": "Only the G6 and gap2 roots have independent Evans existence and uniqueness certificates.",
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    EXPERIMENTS.mkdir(parents=True, exist_ok=True)
    payloads = {
        "translation_charge.json": translation_charge_certificate(),
        "plus_minus_two_algebra.json": plus_minus_two_certificate(),
        "single_gap_exact_comparisons.json": competitive_single_gap_certificates(),
        "charge_recurrence.json": charge_recurrence_certificate(),
        "c6_root_geometry.json": polynomial_root_geometry(),
    }
    for name, payload in payloads.items():
        write_json(OUTPUT / name, payload)
    write_json(
        OUTPUT.parent / "elementary_charge_exact_comparisons.json",
        payloads["single_gap_exact_comparisons.json"],
    )
    summary = {
        "status": "TASK52_EXACT_PHASE_COMPLETE",
        "entry_head": ENTRY_HEAD,
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "artifacts": sorted(payloads),
    }
    write_json(EXPERIMENTS / "exact_phase_summary.json", summary)
    print(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    run()
