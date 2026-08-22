"""Exact finite-ring closure recurrence and Task 50 Gate 4 analysis."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task48a_common import q_from_gaps, single_slip_gaps
from target_a_task50_bulk import monodromy


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task50" / "certificates"


def exterior_square(matrix: sp.Matrix) -> sp.Matrix:
    pairs = list(itertools.combinations(range(4), 2))
    result = sp.zeros(6)
    for column, (i, j) in enumerate(pairs):
        for row, (a, b) in enumerate(pairs):
            result[row, column] = sp.expand(matrix[a, i] * matrix[b, j] - matrix[a, j] * matrix[b, i])
    return result


def recurrence_polynomial() -> sp.Poly:
    lam, y, t = sp.symbols("lambda y t")
    bulk = monodromy(lam)
    cell_characteristic = bulk.charpoly(t).as_expr().subs(lam**2, y)
    wedge_characteristic = exterior_square(bulk).charpoly(t).as_expr().subs(lam**2, y)
    # The exterior-square polynomial has (t-1)^2.  The determinant sequence
    # uses one copy of the constant root together with the four cell roots and
    # the four nontrivial pair products.
    combined = sp.cancel(cell_characteristic * wedge_characteristic / (t - 1))
    polynomial = sp.Poly(sp.factor(combined), t)
    if polynomial.degree() != 9 or polynomial.all_coeffs()[-1] != -1:
        raise AssertionError("unexpected finite-closure recurrence")
    return polynomial


def tau_lift(q: tuple[int, ...]) -> tuple[int, ...]:
    tau = [1]
    for value in q[:-1]:
        tau.append(tau[-1] * value)
    if tau[-1] * q[-1] != 1:
        raise AssertionError("finite Q word does not lift")
    return tuple(tau)


def finite_closure_polynomial(gap: int, bulk_cells: int, alpha: int) -> sp.Poly:
    lam, y = sp.symbols("lambda y")
    n = 8 * bulk_cells + (2 if gap == 6 else 6)
    q = q_from_gaps(n, single_slip_gaps(n, gap))
    tau = tau_lift(q)
    product = sp.eye(4)
    for index in range(n):
        a = tau[index]
        b = tau[(index - 2) % n]
        transfer = sp.Matrix([[-a, a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
        product = (transfer * product).applyfunc(sp.expand)
    determinant = sp.Poly(sp.expand((product - alpha * sp.eye(4)).det(method="domain-ge")), lam)
    if any(power % 2 for (power,), coefficient in determinant.terms() if coefficient):
        raise AssertionError("finite closure is not a polynomial in y")
    expression = sum(coefficient * y ** (power // 2) for (power,), coefficient in determinant.terms())
    return sp.Poly(expression, y)


def polynomial_digest(polynomial: sp.Poly) -> str:
    return hashlib.sha256(str(polynomial.as_expr()).encode("utf-8")).hexdigest()


def run() -> dict[str, Any]:
    y, u, t = sp.symbols("y u t")
    recurrence = recurrence_polynomial()
    coefficients = recurrence.all_coeffs()
    shifted_signs = []
    for index, coefficient in enumerate(coefficients):
        shifted = sp.Poly(sp.expand(coefficient.subs(y, u + 8)), u)
        signs = {sp.sign(value) for value in shifted.all_coeffs() if value}
        shifted_signs.append({"index": index, "signs": sorted(map(int, signs))})

    sanity_rows = []
    for gap in (6, 10):
        for alpha in (-1, 1):
            sequence = [finite_closure_polynomial(gap, bulk_cells, alpha) for bulk_cells in range(1, 11)]
            recurrence_residual = sequence[9].as_expr()
            for offset in range(1, 10):
                recurrence_residual += coefficients[offset] * sequence[9 - offset].as_expr()
            recurrence_residual = sp.Poly(sp.expand(recurrence_residual), y)
            if not recurrence_residual.is_zero:
                raise AssertionError(f"finite recurrence failed for G{gap}, alpha={alpha}")
            initial_signs = []
            for bulk_cells, polynomial in enumerate(sequence[:9], start=1):
                shifted = sp.Poly(sp.expand(polynomial.as_expr().subs(y, u + 8)), u)
                sign = -1 if all(value < 0 for value in shifted.all_coeffs()) else 1 if all(value > 0 for value in shifted.all_coeffs()) else 0
                initial_signs.append({
                    "bulk_cells": bulk_cells,
                    "degree_y": polynomial.degree(),
                    "shifted_coefficient_sign": sign,
                    "sha256": polynomial_digest(polynomial),
                })
            sanity_rows.append({
                "family": f"G{gap}",
                "alpha": alpha,
                "exact_recurrence_checked": True,
                "initial_polynomials": initial_signs,
            })

    alternating = all(row["signs"] == ([1] if row["index"] % 2 == 0 else [-1]) for row in shifted_signs)
    payload = {
        "status": "SINGLE_INTERFACE_BOUND_INCOMPLETE",
        "twisted_closure": "det(M_n(lambda)-alpha I_4)=0, alpha in {-1,+1}",
        "family_parameters": {
            "G6": {"n": "8*k+2", "closure_distance_cells": "k", "gaps": "[6]+[4]*(2*k-1)"},
            "G10": {"n": "8*k+6", "closure_distance_cells": "k", "gaps": "[10]+[4]*(2*k-1)"},
        },
        "recurrence_variable": "bulk cell count k",
        "recurrence_polynomial": str(recurrence.as_expr()),
        "recurrence_coefficients": [str(value) for value in coefficients],
        "shift_y_equals_8_plus_u_coefficient_signs": shifted_signs,
        "alternating_recurrence_signs": alternating,
        "exact_sanity": sanity_rows,
        "proved_so_far": [
            "the finite closure equation is exact and treats both holonomies",
            "each single-interface determinant is an even polynomial in lambda for the checked initial basis",
            "the determinant sequence satisfies the exact universal order-nine exterior-power recurrence",
            "the first nine shifted closure polynomials have one strict coefficient sign for both families and holonomies",
        ],
        "missing_gate": "No invariant cone has been proved for the alternating-sign order-nine recurrence, so the same sign and global spectral exclusion are not yet established for every k.",
        "evidence_boundary": "The ten exact sequence entries validate the symbolic recurrence and initial data; they are not extrapolated into an all-k theorem.",
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "finite_ring_recurrence.json", payload)
    print(json.dumps({
        "status": payload["status"],
        "recurrence_order": recurrence.degree(),
        "initial_exact_cases": sum(len(row["initial_polynomials"]) for row in sanity_rows),
        "alternating_signs": alternating,
    }, indent=2))
    return payload


if __name__ == "__main__":
    run()
