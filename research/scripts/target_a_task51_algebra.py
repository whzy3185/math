"""Exact Evans elimination for the G6 interface constant."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_g6_certificate import tau_window


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task51" / "certificates"
C6_LEFT = Fraction(7905369311620327, 10**15)
C6_RIGHT = Fraction(7905369311620328, 10**15)


def transfer_product(gap: int, start: int, stop: int, lam: sp.Symbol) -> sp.Matrix:
    tau = tau_window(gap)
    result = sp.eye(4)
    for index in range(start, stop):
        a, b = tau[index], tau[index - 2]
        step = sp.Matrix([[-a, a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
        result = step * result
    return result


def cofactor_vector(matrix: sp.Matrix, eigenvalue: sp.Expr) -> sp.Matrix:
    shifted = matrix - eigenvalue * sp.eye(4)
    rows = [0, 1, 2]
    return sp.Matrix([
        (-1) ** excluded * shifted.extract(rows, [column for column in range(4) if column != excluded]).det(method="domain-ge")
        for excluded in range(4)
    ])


def symmetric_evans_core(gap: int) -> tuple[sp.Expr, dict[str, int]]:
    lam, z1, z2, symmetric_sum, symmetric_product = sp.symbols("lam z1 z2 S P")
    start, stop = -8, gap + 8
    left = transfer_product(gap, start - 8, start, lam)
    right = transfer_product(gap, stop, stop + 8, lam)
    defect = transfer_product(gap, start, stop, lam)
    left_vectors = [(z**3 * cofactor_vector(left, 1 / z)).applyfunc(sp.cancel) for z in (z1, z2)]
    right_vectors = [cofactor_vector(right, z) for z in (z1, z2)]
    determinant = sp.factor(sp.Matrix.hstack(
        defect * left_vectors[0], defect * left_vectors[1], right_vectors[0], right_vectors[1]
    ).det(method="domain-ge"))
    quotient = sp.cancel(determinant / (z1 - z2) ** 2)
    symmetric, remainder, mapping = sp.symmetrize(quotient, [z1, z2], formal=True)
    if remainder != 0:
        raise AssertionError("Evans core is not symmetric in the two stable branches")
    symmetric = sp.expand(symmetric.subs({mapping[0][0]: symmetric_sum, mapping[1][0]: symmetric_product}))
    return symmetric, {
        "degree_lambda": int(sp.degree(symmetric, lam)),
        "degree_S": int(sp.degree(symmetric, symmetric_sum)),
        "degree_P": int(sp.degree(symmetric, symmetric_product)),
        "term_count": len(sp.Poly(symmetric, lam, symmetric_sum, symmetric_product).terms()),
    }


def eliminate_g6() -> dict[str, Any]:
    lam, y, S, P = sp.symbols("lam y S P")
    symmetric, degrees = symmetric_evans_core(6)
    y_lam = lam**2
    a = -2 * y_lam**2 + 16 * y_lam - 13
    b = y_lam**4 - 16 * y_lam**3 + 80 * y_lam**2 - 128 * y_lam + 40
    # Reciprocal roots z1,z2,1/z1,1/z2 give
    # S(P+1)+aP=0 and P^2+S^2+1-bP=0.
    substituted = sp.cancel(symmetric.subs(S, -a * P / (P + 1)))
    numerator = sp.primitive(sp.Poly(sp.fraction(substituted)[0], P))[1].as_expr()
    product_relation = sp.expand((P + 1) ** 2 * (P**2 + 1 - b * P) + a**2 * P**2)

    polynomial_lambda = sp.Poly(numerator, lam)
    even = sum(coefficient * y ** (power // 2) for (power,), coefficient in polynomial_lambda.terms() if power % 2 == 0)
    odd = sum(coefficient * y ** ((power - 1) // 2) for (power,), coefficient in polynomial_lambda.terms() if power % 2 == 1)
    squared_evans = sp.expand(even**2 - y * odd**2)
    product_relation_y = sp.expand(product_relation.subs(lam**2, y))
    resultant = sp.resultant(squared_evans, product_relation_y, P)
    content, factors = sp.factor_list(resultant, y)

    factor_records = []
    left = sp.Rational(C6_LEFT.numerator, C6_LEFT.denominator)
    right = sp.Rational(C6_RIGHT.numerator, C6_RIGHT.denominator)
    selected = None
    for factor, multiplicity in factors:
        polynomial = sp.Poly(factor, y)
        roots_in_interval = int(polynomial.count_roots(left, right))
        record = {
            "degree": polynomial.degree(),
            "multiplicity": multiplicity,
            "polynomial": str(factor),
            "roots_in_c6_interval": roots_in_interval,
            "irreducible_over_Q": bool(polynomial.is_irreducible),
        }
        factor_records.append(record)
        if roots_in_interval:
            if selected is not None:
                raise AssertionError("more than one resultant factor meets the c6 interval")
            selected = record
    if selected is None or selected["degree"] != 10 or selected["roots_in_c6_interval"] != 1:
        raise AssertionError("degree-ten c6 factor was not uniquely isolated")
    candidate = sp.Poly(
        16*y**10 - 520*y**9 + 6913*y**8 - 48448*y**7 + 191768*y**6
        - 423904*y**5 + 484528*y**4 - 270464*y**3 + 137856*y**2 - 19968*y + 256,
        y,
    )
    if sp.Poly(selected["polynomial"], y).monic() != candidate.monic():
        raise AssertionError("exact factor does not match the Task 48A candidate")
    return {
        "status": "C6_DEGREE10_EVANS_POLYNOMIAL_PROVED",
        "symmetric_evans_degrees": degrees,
        "symmetric_variables": {"S": "z1+z2", "P": "z1*z2"},
        "reciprocal_relations": ["S(P+1)+aP=0", "P^2+S^2+1-bP=0"],
        "elimination": {
            "squared_evans_degree_P": int(sp.degree(squared_evans, P)),
            "squared_evans_degree_y": int(sp.degree(squared_evans, y)),
            "product_relation_degree_P": int(sp.degree(product_relation_y, P)),
            "resultant_degree_y": int(sp.degree(resultant, y)),
            "content": str(content),
            "factors": factor_records,
        },
        "c6_polynomial": str(candidate.as_expr()),
        "c6_interval": [str(C6_LEFT), str(C6_RIGHT)],
        "unique_root_in_interval": True,
        "irreducible_degree": 10,
        "logical_bridge": "Task 50 proves distinct positive stable roots and an Evans zero in the interval, so P>0 and z1!=z2. Every such zero annihilates the exact resultant. Exactly one irreducible factor has a root in the interval, hence c6 is its unique interval root.",
        "PSLQ_used_for_acceptance": False,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    c6 = eliminate_g6()
    # G10 uses the same exact construction, but its larger elimination is not
    # escalated after the G6 theorem has closed and the Task 51 growth stop is met.
    payload = {
        "c6": c6,
        "c10": {
            "status": "OPEN_SYMBOLIC_GROWTH_STOP",
            "attempt": "exact transfer and symmetric-Evans construction available",
            "reason": "No low-degree candidate survived Task 48A validation; an unbounded resultant is prohibited.",
        },
        "charge_recurrence": "PROMISING_PERIOD8_INSERTION_RELATION_NOT_ELIMINATED",
        "trace_map": "PROMISING_EXTERIOR_TRACE_COORDINATES_NOT_CLOSED",
    }
    write_json(OUTPUT / "c6_exact_evans_elimination.json", payload)
    print(json.dumps({"status": c6["status"], "degree": c6["irreducible_degree"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()
