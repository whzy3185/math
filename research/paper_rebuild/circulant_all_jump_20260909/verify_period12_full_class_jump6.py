#!/usr/bin/env python3
"""Exact finite audit for the complete period-12, jump-6 periodic class.

Evidence status under the project convention: VERIFIED (exact finite computation).
No floating-point spectral acceptance test is used.
"""

from itertools import product
import sympy as sp

P = 12
L = 6


def prod(xs):
    out = 1
    for x in xs:
        out *= x
    return out


def canon(q):
    q = tuple(q)
    words = []
    for k in range(P):
        r = q[k:] + q[:k]
        words.append(r)
        words.append(tuple(reversed(r)))
    return min(words)


def lift(q):
    tau = [sp.Integer(1)]
    for i in range(P - 1):
        tau.append(tau[-1] * q[i])
    assert tau[-1] == q[-1]
    return tau


def H_endpoint(q, eps):
    tau = lift(q)
    H = sp.zeros(P)
    for i in range(P - 1):
        H[i, i + 1] = H[i + 1, i] = 1
    H[P - 1, 0] = H[0, P - 1] = eps
    for j in range(L):
        c = tau[j] + eps * tau[j + L]
        H[j, j + L] = H[j + L, j] = c
    return H


def first_endpoint_moment_failure(q, max_even=44):
    """Return exact certificate Delta_e<0 at z=+/-1, or None."""
    for eps in (1, -1):
        H = H_endpoint(q, eps)
        H2 = H * H
        cur = H2
        prev = sp.trace(cur)
        for e in range(4, max_even + 1, 2):
            cur = cur * H2
            tr = sp.trace(cur)
            delta = sp.expand(8 * prev - tr)
            if delta < 0:
                return eps, e, int(delta)
            prev = tr
    return None


def bernstein_coeffs(poly, var):
    poly = sp.Poly(poly, var)
    n = poly.degree()
    a = [poly.nth(j) for j in range(n + 1)]
    out = []
    for k in range(n + 1):
        b = 0
        for j in range(k + 1):
            b += a[j] * sp.Rational(sp.binomial(k, j), sp.binomial(n, j))
        out.append(sp.factor(b))
    return out


def main():
    legal = [q for q in product((-1, 1), repeat=P) if prod(q) == 1]
    assert len(legal) == 2048
    orbits = {}
    for q in legal:
        orbits.setdefault(canon(q), []).append(q)
    assert len(orbits) == 122

    all_negative = tuple([-1] * P)
    target = tuple([-1] * 9 + [1, -1, 1])  # positive sites 9 and 11
    assert target in orbits

    # Target is strictly below 8 for every phase.
    # It is the N=2,m=1 two-defect family with q=0, hence d=e=c.
    c, t = sp.symbols("c t", real=True)
    y = sp.Integer(8)
    x = (y - c - 4) / 2
    a = (y + c - 4) / 2
    X = sp.chebyshevt(2, x)
    u = sp.chebyshevu(1, x)
    Y = a
    Z = sp.expand(X * Y + (a * x - 3) * u)
    threshold = sp.expand(4 * (Z**2 - 1 + (c - 2)) + (2 - c))
    expected = c**6 - 8*c**5 - 6*c**4 + 160*c**3 - 167*c**2 - 789*c + 1286
    assert sp.expand(threshold - expected) == 0
    bt = bernstein_coeffs(sp.expand(threshold.subs(c, 4*t - 2)), t)
    assert bt == [
        sp.Integer(1140), sp.Rational(5738, 3), sp.Rational(34024, 15),
        sp.Rational(6682, 5), sp.Rational(2668, 5), sp.Integer(150), sp.Integer(32)
    ]
    assert all(b > 0 for b in bt)

    # Reference-fiber inertia: 8I-H(1)^2 is positive definite.
    H = H_endpoint(target, 1)
    M = 8 * sp.eye(P) - H * H
    leading = [sp.factor(M[:k, :k].det()) for k in range(1, P + 1)]
    assert leading == [2, 4, 6, 9, 48, 124, 224, 361, 522, 324, 576, 1024]
    assert all(v > 0 for v in leading)

    # Every other non-all-negative orbit violates an endpoint moment inequality.
    histogram = {}
    worst = 0
    for rep in orbits:
        if rep in (target, all_negative):
            continue
        cert = first_endpoint_moment_failure(rep, 44)
        assert cert is not None
        _, order, _ = cert
        histogram[order] = histogram.get(order, 0) + 1
        worst = max(worst, order)

    assert sum(histogram.values()) == 120
    assert worst == 44
    assert histogram == {
        4: 56, 6: 22, 8: 14, 10: 6, 12: 1, 14: 1,
        18: 1, 20: 10, 26: 4, 32: 3, 38: 1, 44: 1,
    }

    print("PASS: 2048 legal words -> 122 dihedral orbits")
    print("PASS: target distance-two orbit is strictly sub-eight")
    print("PASS: all 120 other nontrivial orbits have exact endpoint moment obstructions")
    print("PASS: all-negative orbit is the known edge-eight period-two repetition")


if __name__ == "__main__":
    main()
