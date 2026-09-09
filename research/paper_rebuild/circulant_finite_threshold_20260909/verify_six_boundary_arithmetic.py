#!/usr/bin/env python3
"""Exact finite sanity checks for SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md.

The theorem itself is analytic.  This script checks, over a large finite range,
that:
  * C_q(1,t) has twins exactly on q=2t+2;
  * C_q(1,t) has a triangle exactly on t=2, q=2t+1, or q=3t;
  * the original parity-support graph reduces to copies of C_q(1,t).

No floating point arithmetic is used.
"""

from math import gcd


def conn(q, t):
    return {1 % q, (-1) % q, t % q, (-t) % q}


def twin_periods(q, t):
    S = conn(q, t)
    return [a for a in range(1, q) if {(x + a) % q for x in S} == S]


def has_triangle(q, t):
    S = conn(q, t)
    # A triangle through 0 exists iff a,b in S and b-a in S.
    return any(((b - a) % q) in S for a in S for b in S if a != b)


def parity_neighbours(N, s, v):
    return {
        (v + 2) % N,
        (v - 2) % N,
        (v + 2 * s) % N,
        (v - 2 * s) % N,
    }


def reduced_neighbours(q, t, v):
    return {
        (v + 1) % q,
        (v - 1) % q,
        (v + t) % q,
        (v - t) % q,
    }


def check_reduction(N, s):
    d = gcd(N, 2)
    q = N // d
    t = min(s, q - s)

    if d == 1:
        inv2 = pow(2, -1, N)
        for v in range(N):
            lhs = {(inv2 * w) % N for w in parity_neighbours(N, s, v)}
            rv = (inv2 * v) % N
            assert lhs == reduced_neighbours(q, t, rv)
    else:
        # Check the even component; the odd component is its translate.
        for v in range(q):
            ov = 2 * v
            lhs = {(w // 2) % q for w in parity_neighbours(N, s, ov)}
            assert lhs == reduced_neighbours(q, t, v)


for q in range(5, 501):
    for t in range(2, (q - 1) // 2 + 1):
        if not (2 <= t < q / 2):
            continue
        twins = bool(twin_periods(q, t))
        assert twins == (q == 2 * t + 2), (q, t, twin_periods(q, t))

        tri = has_triangle(q, t)
        predicted = (t == 2 or q == 2 * t + 1 or q == 3 * t)
        assert tri == predicted, (q, t, tri, predicted)

for N in range(5, 301):
    for s in range(2, (N - 1) // 2 + 1):
        if not (2 * s < N):
            continue
        if N in (2 * s + 2, 4 * s):
            continue
        q = N // gcd(N, 2)
        t = min(s, q - s)
        if 2 <= t < q / 2:
            check_reduction(N, s)

print("six-boundary arithmetic checks passed for q<=500 and N<=300")
