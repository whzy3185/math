#!/usr/bin/env python3
"""Exact Bernstein certificates for L=6,8,10,12 endpoint locking.

All arithmetic used in the acceptance tests is SymPy exact rational/integer
arithmetic. Floating values are printed only for readability.
"""

import sympy as sp

Y, MU, X, Z = sp.symbols("Y MU X Z")


def U(n, t):
    if n == -1:
        return sp.Integer(0)
    return sp.chebyshevu(n, t)


def endpoint_polynomial(r):
    t = (Y - 6) / 2
    return sp.expand(
        U(r - 2, t) * (Y**2 - 8 * Y + 6)
        - U(r - 3, t) * (Y - 2)
        - 2
    )


def G(r, y, d):
    t = (y - d - 4) / 2
    u = U(r - 2, t)
    w = U(r - 3, t)
    A = (y**2 - 9*y + 14 - d**2 - d) * (y**2 - 7*y + 6 - d**2 + d)
    B = -(d + y - 4) * (y**2 - 8*y + 4 - d**2)
    C = d**2 + 2*d*y - 4*d + y**2 - 8*y + 6
    return sp.expand(u**2 * A + u*w * B + C)


def comparison_quotient(r):
    numerator = sp.expand(G(r, Y, 2 - MU) - G(r, Y, 2))
    q = sp.cancel(numerator / MU)
    assert sp.expand(numerator - MU*q) == 0
    return sp.expand(q)


def bernstein_coefficients_on_rectangle(expr, ylo, yhi):
    # MU = 4 X and Y = ylo + (yhi-ylo) Z, with X,Z in [0,1].
    mapped = sp.expand(expr.subs({MU: 4*X, Y: ylo + (yhi-ylo)*Z}))
    poly = sp.Poly(mapped, X, Z)
    nx = poly.degree(X)
    nz = poly.degree(Z)
    out = {}
    for k in range(nx + 1):
        for ell in range(nz + 1):
            value = sp.Rational(0)
            for i in range(k + 1):
                for j in range(ell + 1):
                    aij = poly.coeff_monomial(X**i * Z**j)
                    if aij:
                        value += (
                            aij
                            * sp.binomial(k, i) / sp.binomial(nx, i)
                            * sp.binomial(ell, j) / sp.binomial(nz, j)
                        )
            out[(k, ell)] = sp.factor(value)
    return nx, nz, out


# Rational endpoint isolating intervals. Each has width 10^-6.
INTERVALS = {
    3: (sp.Rational(1557743, 200000), sp.Rational(1947179, 250000)),
    4: (sp.Rational(7887839, 1000000), sp.Rational(49299, 6250)),
    5: (sp.Rational(3965319, 500000), sp.Rational(7930639, 1000000)),
    6: (sp.Rational(3976457, 500000), sp.Rational(1590583, 200000)),
}

# Simple integer lower bounds smaller than the exact minimum Bernstein coefficient.
LOWER_BOUNDS = {3: 46, 4: 98, 5: 168, 6: 257}


def main():
    for r in (3, 4, 5, 6):
        lo, hi = INTERVALS[r]
        p = endpoint_polynomial(r)
        plo = sp.factor(p.subs(Y, lo))
        phi = sp.factor(p.subs(Y, hi))
        assert plo < 0 < phi

        q = comparison_quotient(r)
        nx, nz, coeffs = bernstein_coefficients_on_rectangle(q, lo, hi)
        min_key = min(coeffs, key=lambda key: coeffs[key])
        min_coeff = coeffs[min_key]
        assert min_coeff > LOWER_BOUNDS[r] > 0

        print(f"r={r}, L={2*r}")
        print(f"  endpoint interval = [{lo}, {hi}]")
        print(f"  p(lo)={plo} < 0 < p(hi)={phi}")
        print(f"  Bernstein bidegree = ({nx},{nz})")
        print(f"  minimum coefficient at {min_key} = {min_coeff}")
        print(f"  certified simple lower bound > {LOWER_BOUNDS[r]}")


if __name__ == "__main__":
    main()
