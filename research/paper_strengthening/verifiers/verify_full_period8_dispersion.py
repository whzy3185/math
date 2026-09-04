#!/usr/bin/env python3
"""Independent symbolic audit of all period-eight squared bands."""

import sympy as sp


def main():
    X, y, c = sp.symbols("X y c", real=True)
    polynomial = (
        y**4
        - 16 * y**3
        + (80 - 2 * c) * y**2
        + (-128 + 16 * c) * y
        + c**2
        - 13 * c
        + 38
    )
    shifted = X**4 - (16 + 2 * c) * X**2 + c**2 + 19 * c + 38
    assert sp.expand(polynomial.subs(y, X + 4) - shifted) == 0

    w_plus = 8 + c + sp.sqrt(26 - 3 * c)
    w_minus = 8 + c - sp.sqrt(26 - 3 * c)
    for w in (w_plus, w_minus):
        assert sp.simplify(w**2 - (16 + 2 * c) * w + c**2 + 19 * c + 38) == 0

    branches = (
        4 + sp.sqrt(w_plus),
        4 + sp.sqrt(w_minus),
        4 - sp.sqrt(w_minus),
        4 - sp.sqrt(w_plus),
    )
    for branch in branches:
        assert sp.simplify(polynomial.subs(y, branch)) == 0

    # Exact endpoint factorizations; both have four simple squared roots.
    at_minus_two = sp.factor(polynomial.subs(c, -2), extension=sp.sqrt(2))
    expected_minus_two = sp.prod(
        y - root for root in (6 + sp.sqrt(2), 6 - sp.sqrt(2),
                              2 + sp.sqrt(2), 2 - sp.sqrt(2))
    )
    assert sp.expand(at_minus_two - expected_minus_two) == 0
    assert sp.discriminant(polynomial.subs(c, -2), y) == 2**20
    assert sp.discriminant(polynomial.subs(c, 2), y) == 8_192_000

    # Algebraic endpoint simplifications used in the band intervals.
    assert sp.expand((2 + sp.sqrt(2)) ** 2 - (6 + 4 * sp.sqrt(2))) == 0
    assert sp.expand((2 - sp.sqrt(2)) ** 2 - (6 - 4 * sp.sqrt(2))) == 0

    # Both W branches are strictly increasing.  The manuscript supplies the
    # interval inequalities proving positivity and disjointness.
    assert sp.simplify(
        sp.diff(w_plus, c) - (1 - sp.Rational(3, 2) / sp.sqrt(26 - 3 * c))
    ) == 0
    assert sp.simplify(
        sp.diff(w_minus, c) - (1 + sp.Rational(3, 2) / sp.sqrt(26 - 3 * c))
    ) == 0

    eta = 4 + sp.sqrt(10 + 2 * sp.sqrt(5))
    central_gap_square = 4 - sp.sqrt(10 + 2 * sp.sqrt(5))
    assert sp.simplify(branches[0].subs(c, 2) - eta) == 0
    assert sp.simplify(branches[3].subs(c, 2) - central_gap_square) == 0

    print("FULL_PERIOD8_DISPERSION_SYMBOLIC_AUDIT_PASS")


if __name__ == "__main__":
    main()
