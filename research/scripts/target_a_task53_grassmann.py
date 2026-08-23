"""Exact Grassmann coordinates shared by the Task 53 A2/A3 certificates."""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable

import sympy as sp

from target_a_task50_interval import Interval, interval_sqrt
from target_a_task51_algebra import transfer_product


PAIRS = tuple((i, j) for i in range(4) for j in range(i + 1, 4))
DEFAULT_COFACTOR_ROWS = (0, 1, 3)


def cofactor_vector(
    matrix: sp.Matrix,
    eigenvalue: sp.Expr,
    rows: tuple[int, int, int] = DEFAULT_COFACTOR_ROWS,
) -> sp.Matrix:
    shifted = matrix - eigenvalue * sp.eye(4)
    return sp.Matrix([
        (-1) ** excluded
        * shifted.extract(rows, [j for j in range(4) if j != excluded]).det(method="domain-ge")
        for excluded in range(4)
    ])


def symmetric_plucker_sections(
    matrix: sp.Matrix,
    *,
    left: bool,
    rows: tuple[int, int, int] = DEFAULT_COFACTOR_ROWS,
) -> dict[tuple[int, int], sp.Expr]:
    """Return wedge sections divided by the stable-root Vandermonde."""
    lam, z1, z2, symmetric_sum, symmetric_product = sp.symbols("lambda z1 z2 S P")
    vectors = []
    for root in (z1, z2):
        if left:
            vector = (root**3 * cofactor_vector(matrix, 1 / root, rows)).applyfunc(sp.cancel)
        else:
            vector = cofactor_vector(matrix, root, rows)
        vectors.append(vector)
    sections = {}
    for i, j in PAIRS:
        quotient = sp.cancel(
            (vectors[0][i] * vectors[1][j] - vectors[0][j] * vectors[1][i]) / (z1 - z2)
        )
        symmetric, remainder, mapping = sp.symmetrize(quotient, [z1, z2], formal=True)
        if remainder != 0:
            raise AssertionError("Plucker section did not symmetrize")
        sections[(i, j)] = sp.expand(symmetric.subs({
            mapping[0][0]: symmetric_sum,
            mapping[1][0]: symmetric_product,
        }))
    return sections


def bulk_relations() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    lam, product = sp.symbols("lambda P")
    a = -2 * lam**4 + 16 * lam**2 - 13
    b = lam**8 - 16 * lam**6 + 80 * lam**4 - 128 * lam**2 + 40
    relation = sp.expand((product + 1) ** 2 * (product**2 + 1 - b * product) + a**2 * product**2)
    return a, b, relation


def physical_section(section: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    lam, symmetric_sum, product = sp.symbols("lambda S P")
    a, _b, _relation = bulk_relations()
    reduced = sp.cancel(section.subs(symmetric_sum, -a * product / (product + 1)))
    numerator, denominator = sp.fraction(reduced)
    return sp.expand(numerator), sp.expand(denominator)


def squared_elimination(numerator: sp.Expr) -> sp.Expr:
    lam, y, product = sp.symbols("lambda y P")
    _a, _b, relation = bulk_relations()
    primitive = sp.primitive(sp.Poly(numerator, product))[1].as_expr()
    polynomial = sp.Poly(primitive, lam)
    even = sum(c * y ** (n[0] // 2) for n, c in polynomial.terms() if n[0] % 2 == 0)
    odd = sum(c * y ** ((n[0] - 1) // 2) for n, c in polynomial.terms() if n[0] % 2)
    squared = sp.expand(even**2 - y * odd**2)
    return sp.factor(sp.resultant(squared, sp.expand(relation.subs(lam**2, y)), product))


def _fraction(value: sp.Rational) -> Fraction:
    return Fraction(int(value.p), int(value.q))


def interval_polynomial(expr: sp.Expr, variable: sp.Symbol, value: Interval) -> Interval:
    result = Interval.point(0)
    for coefficient in sp.Poly(expr, variable).all_coeffs():
        result = result * value + _fraction(coefficient)
    return result


def interval_bivariate(expr: sp.Expr, first: sp.Symbol, first_value: Interval, second: sp.Symbol, second_value: Interval) -> Interval:
    result = Interval.point(0)
    for coefficient in sp.Poly(expr, first).all_coeffs():
        result = result * first_value + interval_polynomial(coefficient, second, second_value)
    return result


def physical_branch(interval: Interval) -> tuple[Interval, Interval, Interval]:
    """Enclose lambda, S, P for the unique stable reciprocal pair."""
    y = sp.symbols("y")
    a = -2 * y**2 + 16 * y - 13
    b = y**4 - 16 * y**3 + 80 * y**2 - 128 * y + 40
    delta_factors = (
        y**2 - 12 * y + 34,
        y**2 - 4 * y + 2,
        y**4 - 16 * y**3 + 76 * y**2 - 96 * y + 16,
    )
    a_value = interval_polynomial(a, y, interval)
    b_value = interval_polynomial(b, y, interval)
    delta = Interval.point(1)
    for factor in delta_factors:
        delta = delta * interval_polynomial(factor, y, interval)
    t_large = (b_value - 2 + interval_sqrt(delta)) / 2
    product = 2 / (t_large + interval_sqrt(t_large**2 - 4))
    symmetric_sum = -a_value * product / (product + 1)
    return interval_sqrt(interval), symmetric_sum, product


def evaluate_physical_section(section: sp.Expr, interval: Interval) -> Interval:
    lam, symmetric_sum, product = sp.symbols("lambda S P")
    numerator, denominator = physical_section(section)
    lam_value, _sum_value, product_value = physical_branch(interval)
    numerator_value = interval_bivariate(numerator, lam, lam_value, product, product_value)
    denominator_value = interval_bivariate(denominator, lam, lam_value, product, product_value)
    return numerator_value / denominator_value


def factor_records(resultant: sp.Expr, left: sp.Rational, right: sp.Rational) -> list[dict[str, object]]:
    y = sp.symbols("y")
    records = []
    for factor, multiplicity in sp.factor_list(resultant, y)[1]:
        polynomial = sp.Poly(factor, y)
        records.append({
            "polynomial": str(factor),
            "degree": int(polynomial.degree()),
            "multiplicity": int(multiplicity),
            "roots_in_task_interval": int(polynomial.count_roots(left, right)),
        })
    return records


def relevant_sections(rows: tuple[int, int, int] = DEFAULT_COFACTOR_ROWS) -> tuple[sp.Expr, sp.Expr]:
    return selected_sections(rows, (2, 3), (0, 1))


def selected_sections(
    rows: tuple[int, int, int],
    right_pair: tuple[int, int],
    left_pair: tuple[int, int],
) -> tuple[sp.Expr, sp.Expr]:
    lam = sp.symbols("lambda")
    right = transfer_product(6, 14, 22, lam)
    left = transfer_product(6, -16, -8, lam)
    return (
        symmetric_plucker_sections(right, left=False, rows=rows)[right_pair],
        symmetric_plucker_sections(left, left=True, rows=rows)[left_pair],
    )


def exact_matrix_rows(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]


def all_true(values: Iterable[bool]) -> bool:
    return all(bool(value) for value in values)
