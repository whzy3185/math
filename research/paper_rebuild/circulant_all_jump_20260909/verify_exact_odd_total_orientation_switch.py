#!/usr/bin/env python3
"""Exact verifier for the finite odd-total orientation switch.

Certificates:
- r=1,...,5: (r+1,r) beats all competitors;
- r=6,7,8: (r,r+1) beats all competitors.

Only SymPy rational arithmetic is used for acceptance.
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


def char_expr(N, m, yy, dd, ee):
    x = (yy-dd-4)/2
    a = (yy+dd-4)/2
    u = U(N-1, x)
    p = U(m-1, a)
    X = T(N, x)
    Y = T(m, a)
    Z = sp.expand(X*Y + (a*x-3)*u*p)
    return sp.expand(4*(Z**2-1+(dd-2)*p**2)+(2-ee))


def relaxed_poly(N, m, gap):
    return sp.Poly(char_expr(N, m, sp.Integer(8)-gap, d, sp.Integer(2)), d)


def bernstein(poly, lo=sp.Rational(0), hi=sp.Rational(1)):
    s = sp.symbols("s")
    tt = lo + (hi-lo)*s
    expr = sp.expand(poly.as_expr().subs(d, 4*tt-2))
    q = sp.Poly(expr, s)
    n = q.degree()
    power = [q.nth(j) for j in range(n+1)]
    return [
        sp.factor(sum(
            power[j]*sp.Rational(comb(k,j), comb(n,j))
            for j in range(k+1)
        ))
        for k in range(n+1)
    ]


def certify_positive(poly, lo=sp.Rational(0), hi=sp.Rational(1), depth=0, maxdepth=15):
    coeff = bernstein(poly, lo, hi)
    if all(c > 0 for c in coeff):
        return [(lo, hi, min(coeff))]
    assert depth < maxdepth
    mid = (lo+hi)/2
    return (certify_positive(poly, lo, mid, depth+1, maxdepth)
            + certify_positive(poly, mid, hi, depth+1, maxdepth))


def endpoint_derivative_certificate(N, m, gap, dd, ee):
    expr = sp.expand(char_expr(N, m, y, dd, ee))
    factors = sp.factor_list(expr)[1]
    y0 = sp.Integer(8)-gap
    for f, multiplicity in factors:
        assert multiplicity == 1
        f = sp.expand(f)
        deg = sp.Poly(f, y).degree()
        cur = f
        for _ in range(deg+1):
            assert sp.factor(cur.subs(y, y0)) > 0
            cur = sp.diff(cur, y)


def early_periodic_side():
    gaps = {
        1: sp.Rational(1,10),
        2: sp.Rational(4,25),
        3: sp.Rational(21,200),
        4: sp.Rational(149,2000),
        5: sp.Rational(27219,500000),
    }
    for r, gap in gaps.items():
        # farther geometry bound when it exists
        if r >= 2:
            assert sp.Rational(10, 4*(r+2)**2) < gap

        poly = relaxed_poly(r+1, r, gap)
        cert = certify_positive(poly)
        assert cert
        endpoint_derivative_certificate(r+1, r, gap, sp.Integer(2), sp.Integer(2))

        # opposite nearest orientation loses already at z=-1
        val = sp.factor(char_expr(r, r+1, sp.Integer(8)-gap,
                                  sp.Integer(-2), sp.Integer(-2)))
        assert val < 0
        print(f"PASS early r={r}, subintervals={len(cert)}")


def late_antiperiodic_side():
    gaps = {
        6: sp.Rational(2067,50000),
        7: sp.Rational(3243,100000),
        8: sp.Rational(2611,100000),
    }
    mus = {
        6: sp.Rational(1,7200),
        7: sp.Rational(1,11000),
        8: sp.Rational(1,17250),
    }

    for r, gap in gaps.items():
        assert sp.Rational(10, 4*(r+2)**2) < gap

        # winning orientation: relaxed seam certificate
        poly = relaxed_poly(r, r+1, gap)
        coeff = bernstein(poly)
        assert all(c > 0 for c in coeff)
        endpoint_derivative_certificate(r, r+1, gap,
                                        sp.Integer(-2), sp.Integer(-2))

        # losing periodic orientation: explicit physical compressed phase.
        dd = sp.Integer(2)-mus[r]
        val = sp.factor(char_expr(r+1, r, sp.Integer(8)-gap, dd, dd))
        assert val < 0
        print(f"PASS late r={r}, min Bernstein={min(coeff)}")


def main():
    early_periodic_side()
    late_antiperiodic_side()
    print("PASS: exact odd-total orientation switch certified through r=8")


if __name__ == "__main__":
    main()
