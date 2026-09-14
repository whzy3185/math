#!/usr/bin/env python3
"""Exact finite audit for the complete period-16, jump-8 periodic class.

Project evidence status: VERIFIED (exact finite computation).
The unique optimizer is certified by a rational separator y0=389/50.
No floating-point spectral acceptance test is used.
"""

from itertools import product
import sympy as sp

P = 16
L = 8
Y0_NUM = 389
Y0_DEN = 50


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


def passes_threshold_moments(q, max_even=14):
    """Necessary conditions for full edge <=8 at z=+/-1."""
    for eps in (1, -1):
        H = H_endpoint(q, eps)
        H2 = H * H
        cur = H2
        prev = sp.trace(cur)
        for e in range(4, max_even + 1, 2):
            cur = cur * H2
            tr = sp.trace(cur)
            if sp.expand(8 * prev - tr) < 0:
                return False
            prev = tr
    return True


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


def first_nonpositive_leading_minor(q, eps):
    """Sylvester certificate that some squared endpoint eigenvalue >=389/50."""
    H = H_endpoint(q, eps)
    M = Y0_NUM * sp.eye(P) - Y0_DEN * (H * H)
    for k in range(1, P + 1):
        det = sp.factor(M[:k, :k].det())
        if det <= 0:
            return k, int(det)
    return None


def main():
    legal = [q for q in product((-1, 1), repeat=P) if prod(q) == 1]
    assert len(legal) == 32768

    orbits = {}
    for q in legal:
        orbits.setdefault(canon(q), []).append(q)
    assert len(orbits) == 1162

    target_list = [-1] * P
    target_list[11] = 1
    target_list[15] = 1
    target = tuple(target_list)
    assert target in orbits

    # Exact necessary-moment filter at threshold 8.
    survivors = [rep for rep in orbits if passes_threshold_moments(rep, 14)]
    assert len(survivors) == 35
    assert target in survivors

    # Target: prove every Bloch fiber lies strictly below y0=389/50.
    # Balanced N=m=2 all-energy single-square identity, relaxed to e=2.
    y = sp.Rational(Y0_NUM, Y0_DEN)
    d, t = sp.symbols("d t", real=True)
    x = (y - d - 4) / 2
    a = (y + d - 4) / 2
    u = sp.chebyshevu(1, x)
    X = sp.chebyshevt(2, x)
    p = sp.chebyshevu(1, a)
    Y = sp.chebyshevt(2, a)
    Z = sp.expand(X * Y + (a * x - 3) * u * p)
    relaxed = sp.expand(4 * (Z**2 - 1 + (d - 2) * p**2))
    poly_t = sp.expand(relaxed.subs(d, 4 * t - 2))
    b = bernstein_coeffs(poly_t, t)
    assert len(b) == 9
    assert all(v > 0 for v in b)

    # Reference inertia at z=-1: y0 I-H^2 is positive definite.
    H = H_endpoint(target, -1)
    M = Y0_NUM * sp.eye(P) - Y0_DEN * (H * H)
    target_minors = [sp.factor(M[:k, :k].det()) for k in range(1, P + 1)]
    assert all(v > 0 for v in target_minors)

    # Every other moment-surviving orbit has an exact endpoint Sylvester obstruction.
    order_hist = {}
    eps_hist = {1: 0, -1: 0}
    for rep in survivors:
        if rep == target:
            continue
        cert = None
        for eps in (1, -1):
            trial = first_nonpositive_leading_minor(rep, eps)
            if trial is not None:
                if cert is None or trial[0] < cert[1]:
                    cert = (eps, trial[0], trial[1])
        assert cert is not None
        eps, order, _ = cert
        eps_hist[eps] += 1
        order_hist[order] = order_hist.get(order, 0) + 1

    assert sum(order_hist.values()) == 34
    assert max(order_hist) == 15
    assert order_hist == {8: 5, 10: 16, 11: 6, 12: 3, 13: 1, 14: 2, 15: 1}
    assert eps_hist == {1: 19, -1: 15}

    print("PASS: 32768 legal words -> 1162 dihedral orbits")
    print("PASS: threshold moments leave exactly 35 candidate orbits")
    print("PASS: target full Bloch edge < 389/50")
    print("PASS: every other candidate has endpoint edge >= 389/50")
    print("PASS: balanced distance-four orbit is the unique full-class optimizer")


if __name__ == "__main__":
    main()
