#!/usr/bin/env python3
"""Exact certificates for r=3,5,6,7 fixed-period balanced optimality.

This script uses SymPy rational arithmetic only.  Floating-point output, if
printed, is descriptive and is never used as an acceptance condition.
"""

from math import comb
import sympy as sp


d, t, y = sp.symbols("d t y")


def U(n, x):
    if n == -1:
        return sp.Integer(0)
    if n == 0:
        return sp.Integer(1)
    a, b = sp.Integer(1), 2*x
    if n == 1:
        return sp.expand(b)
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


def balanced_relaxed(r, y0):
    x = (y0 - d - 4) / 2
    a = (y0 + d - 4) / 2
    u = U(r - 1, x)
    p = U(r - 1, a)
    X = T(r, x)
    Y = T(r, a)
    Z = sp.expand(X*Y + (a*x - 3)*u*p)
    return sp.Poly(sp.expand(4*(Z**2 - 1 + (d - 2)*p**2)), d)


def bernstein_coefficients(poly):
    q = sp.Poly(sp.expand(poly.as_expr().subs(d, 4*t - 2)), t)
    n = q.degree()
    power = [q.nth(j) for j in range(n + 1)]
    return [
        sp.factor(sum(
            power[j] * sp.Rational(comb(k, j), comb(n, j))
            for j in range(k + 1)
        ))
        for k in range(n + 1)
    ]


def endpoint_polynomial(r):
    dd = sp.Integer(2)
    x = (y - dd - 4) / 2
    a = (y + dd - 4) / 2
    u = U(r - 1, x)
    p = U(r - 1, a)
    X = T(r, x)
    Y = T(r, a)
    Z = sp.expand(X*Y + (a*x - 3)*u*p)
    return sp.Poly(sp.expand(4*(Z**2 - 1)), y)


def check_layer(r, gap):
    y0 = sp.Integer(8) - gap
    poly = balanced_relaxed(r, y0)
    bern = bernstein_coefficients(poly)
    assert poly.degree() == 4*r
    assert len(bern) == 4*r + 1
    assert all(b > 0 for b in bern)

    ep = endpoint_polynomial(r)
    fac = sp.factor_list(ep.as_expr())[1]
    assert len(fac) == 2
    for f, multiplicity in fac:
        assert multiplicity == 1
        f = sp.expand(f)
        assert sp.Poly(f, y).degree() == 2*r
        current = f
        for _ in range(2*r + 1):
            assert sp.factor(current.subs(y, y0)) > 0
            current = sp.diff(current, y)

    return min(bern)


def main():
    layers = {
        3: sp.Rational(4, 25),
        5: sp.Rational(7, 100),
        6: sp.Rational(13, 250),
        7: sp.Rational(1, 25),
    }

    # elementary competitor separators D_{r+1} < pi^2/[4(r+1)^2] < 10/[4(r+1)^2]
    for r, gap in layers.items():
        assert sp.Rational(10, 4*(r+1)**2) < gap
        minimum = check_layer(r, gap)
        print(f"PASS r={r}: min Bernstein coefficient = {minimum}")

    print("PASS: all residual exact fixed-period certificates verified")


if __name__ == "__main__":
    main()
