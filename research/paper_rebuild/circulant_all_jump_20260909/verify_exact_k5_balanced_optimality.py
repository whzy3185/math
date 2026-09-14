#!/usr/bin/env python3
"""Exact certificate for EXACT_MINIMAL_PERIOD_OPTIMALITY_K5.md.

Uses SymPy exact rational arithmetic only.  No floating-point value is used
as an acceptance condition.
"""

from math import comb
import sympy as sp


def U(n, x):
    if n == -1:
        return sp.Integer(0)
    if n == 0:
        return sp.Integer(1)
    a, b = sp.Integer(1), 2*x
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, sp.expand(2*x*b - a)
    return b


def T(n, x):
    if n == 0:
        return sp.Integer(1)
    if n == 1:
        return x
    a, b = sp.Integer(1), x
    for _ in range(2, n + 1):
        a, b = b, sp.expand(2*x*b - a)
    return b


def relaxed_balanced_polynomial(r, y, d):
    x = (y - d - 4) / 2
    a = (y + d - 4) / 2
    u = U(r - 1, x)
    p = U(r - 1, a)
    X = T(r, x)
    Y = T(r, a)
    Z = sp.expand(X*Y + (a*x - 3)*u*p)
    return sp.Poly(sp.expand(4*(Z**2 - 1 + (d - 2)*p**2)), d)


def bernstein_coefficients(poly, d):
    t = sp.symbols("t")
    q = sp.Poly(sp.expand(poly.as_expr().subs(d, 4*t - 2)), t)
    n = q.degree()
    power = [q.nth(j) for j in range(n + 1)]
    out = []
    for k in range(n + 1):
        out.append(sp.factor(sum(
            power[j] * sp.Rational(comb(k, j), comb(n, j))
            for j in range(k + 1)
        )))
    return out


def endpoint_polynomial(r, y):
    d = sp.Integer(2)
    x = (y - d - 4) / 2
    a = (y + d - 4) / 2
    u = U(r - 1, x)
    p = U(r - 1, a)
    X = T(r, x)
    Y = T(r, a)
    Z = sp.expand(X*Y + (a*x - 3)*u*p)
    return sp.Poly(sp.expand(4*(Z**2 - 1)), y)


def main():
    d, y = sp.symbols("d y")
    r = 8
    y0 = sp.Rational(255, 32)

    poly = relaxed_balanced_polynomial(r, y0, d)
    assert poly.degree() == 32
    bern = bernstein_coefficients(poly, d)
    assert len(bern) == 33
    assert all(b > 0 for b in bern)

    expected_min = sp.Rational(
        2118132998931575580037811628419985641741174001788817920001,
        1461501637330902918203684832716283019655932542976,
    )
    assert min(bern) == expected_min

    ep = endpoint_polynomial(r, y)
    fac = sp.factor_list(ep.as_expr())[1]
    assert len(fac) == 2
    for f, exponent in fac:
        assert exponent == 1
        f = sp.expand(f)
        deg = sp.Poly(f, y).degree()
        assert deg == 16
        g = f
        for _ in range(deg + 1):
            assert sp.factor(g.subs(y, y0)) > 0
            g = sp.diff(g, y)

    # Elementary competitor comparison D_9 < 1/32 is reduced to pi^2 < 10:
    # D_9 < pi^2/324 < 10/324 = 5/162 < 1/32.
    assert sp.Rational(5, 162) < sp.Rational(1, 32)

    print("PASS: all 33 Bernstein coefficients are positive")
    print("minimum coefficient =", expected_min)
    print("PASS: both endpoint factors and all derivatives are positive at 255/32")
    print("PASS: 5/162 < 1/32")


if __name__ == "__main__":
    main()
