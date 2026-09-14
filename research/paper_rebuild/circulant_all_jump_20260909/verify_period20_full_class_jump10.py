#!/usr/bin/env python3
"""Exact finite audit for the complete period-20, jump-10 periodic class.

Project evidence status: VERIFIED (exact finite computation).
The four-defect word with positive flux sites {0,2,4,6} is separated from
all competitors by the rational squared-energy threshold 31/4.
"""

from itertools import product
import sympy as sp

P = 20
L = 10


def reverse_bits(x, p):
    y = 0
    for i in range(p):
        if (x >> i) & 1:
            y |= 1 << (p - 1 - i)
    return y


def rotate_bits(x, p, k):
    mask = (1 << p) - 1
    k %= p
    return ((x >> k) | ((x & ((1 << k) - 1)) << (p - k))) & mask


def canon_int(x, p):
    y = reverse_bits(x, p)
    best = 1 << p
    for k in range(p):
        best = min(best, rotate_bits(x, p, k), rotate_bits(y, p, k))
    return best


def int_to_q(x, p):
    return tuple(1 if (x >> i) & 1 else -1 for i in range(p))


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


def first_nonpositive_leading_minor(q, eps):
    H = H_endpoint(q, eps)
    M = 31 * sp.eye(P) - 4 * (H * H)
    for k in range(1, P + 1):
        det = sp.factor(M[:k, :k].det())
        if det <= 0:
            return k, int(det)
    return None


def palindromic_to_c(poly, z, c):
    poly = sp.Poly(poly, z)
    deg = poly.degree()
    assert deg % 2 == 0
    n = deg // 2
    coeff = [poly.nth(i) for i in range(deg + 1)]
    assert all(coeff[i] == coeff[deg - i] for i in range(deg + 1))
    S = [sp.Integer(2), c]
    for k in range(2, n + 1):
        S.append(sp.expand(c * S[-1] - S[-2]))
    out = coeff[n]
    for k in range(1, n + 1):
        out += coeff[n + k] * S[k]
    return sp.factor(out)


def symbolic_H(q, z):
    tau = lift(q)
    H = sp.zeros(P)
    for i in range(P - 1):
        H[i, i + 1] = H[i + 1, i] = 1
    H[P - 1, 0] = z
    H[0, P - 1] = 1 / z
    for j in range(L):
        H[j, j + L] = tau[j] + tau[j + L] / z
        H[j + L, j] = tau[j] + tau[j + L] * z
    return H


def main():
    # Bit-level dihedral orbit reduction of the 2^19 legal flux words.
    reps = set()
    for x in range(1 << P):
        if x.bit_count() % 2 == 0:
            reps.add(canon_int(x, P))
    assert len(reps) == 13648
    orbits = [int_to_q(x, P) for x in reps]

    target_list = [-1] * P
    for j in (0, 2, 4, 6):
        target_list[j] = 1
    target = tuple(target_list)
    assert target in orbits

    # Threshold-eight moments leave a small exact candidate set.
    survivors = [q for q in orbits if passes_threshold_moments(q, 14)]
    assert len(survivors) == 160
    assert target in survivors

    # Exact all-phase target certificate at y0=31/4.
    z, c = sp.symbols("z c")
    H = symbolic_H(target, z)
    M = sp.Rational(31, 4) * sp.eye(P) - H * H
    det = sp.factor(M.det(method="domain-ge"))
    num, den = sp.together(det).as_numer_denom()
    factors = sp.factor_list(num)[1]
    assert den == 2**40 * z**20
    assert len(factors) == 2
    A, multA = factors[0]
    B, multB = factors[1]
    assert multA == multB == 2
    if sp.degree(A, z) > sp.degree(B, z):
        A, B = B, A
    assert sp.degree(A, z) == 4
    assert sp.degree(B, z) == 16

    a = palindromic_to_c(A, z, c)
    b = palindromic_to_c(B, z, c)
    assert a == 16*c**2 + 16*c - 101
    expected_b = (
        65536*c**8 - 557056*c**7 - 352256*c**6 + 12687360*c**5
        - 14124032*c**4 - 95754624*c**3 + 158253152*c**2
        + 239702152*c - 451466285
    )
    assert sp.expand(b - expected_b) == 0
    assert sp.count_roots(b, -2, 2) == 0

    # Reference-fiber Sylvester positivity.
    H1 = H_endpoint(target, 1)
    Mint = 31 * sp.eye(P) - 4 * (H1 * H1)
    target_minors = [sp.factor(Mint[:k, :k].det()) for k in range(1, P + 1)]
    assert all(v > 0 for v in target_minors)

    # Every other moment-survivor lies at or above 31/4 at an endpoint.
    order_hist = {}
    eps_hist = {1: 0, -1: 0}
    for q in survivors:
        if q == target:
            continue
        cert = None
        for eps in (1, -1):
            trial = first_nonpositive_leading_minor(q, eps)
            if trial is not None:
                if cert is None or trial[0] < cert[1]:
                    cert = (eps, trial[0], trial[1])
        assert cert is not None
        eps, order, _ = cert
        eps_hist[eps] += 1
        order_hist[order] = order_hist.get(order, 0) + 1

    assert sum(order_hist.values()) == 159
    assert max(order_hist) == 19
    assert order_hist == {
        10: 10, 11: 24, 12: 87, 13: 16, 14: 15,
        15: 2, 16: 2, 18: 1, 19: 2,
    }
    assert eps_hist == {1: 92, -1: 67}

    print("PASS: 524288 legal words -> 13648 dihedral orbits")
    print("PASS: threshold moments leave exactly 160 candidates")
    print("PASS: four-defect target full Bloch edge < 31/4")
    print("PASS: every competing candidate has endpoint edge >= 31/4")
    print("PASS: four-defect word is the unique full-class period-20 optimizer")


if __name__ == "__main__":
    main()
