#!/usr/bin/env python3
"""Exact finite certificates for sqrt(6)-boundary minimizer rigidity.

The only floating-point operation is an eigensolver used to *propose* integer
negative quadratic-form witnesses. A class is rejected only after the exact
integer inequality z^T(6I-A^2)z<0 has been checked. Surviving classes are
accepted only after exact SymPy characteristic-polynomial factorization of
6I-A^2.

Checks:
  * (12,4): all 2^13 Hamilton-gauge switching classes; exactly 2 survive;
  * (16,3): all 2^17 Hamilton-gauge switching classes; exactly 32 survive,
    with 16 in each Hamilton holonomy;
  * (16,5): obtained bijectively from (16,3) by multiplier 5 mod 16;
  * (20,8): the analytic mixed-channel recurrence has exactly two solutions,
    and both have the known equality characteristic polynomial.
"""

from collections import Counter
import numpy as np
import sympy as sp

x = sp.symbols("x")


def hamilton_gauge_A(N, s, alpha, tau):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = alpha
    for i, sign in enumerate(tau):
        j = (i + s) % N
        A[i, j] = A[j, i] = sign
    return A


def integer_negative_witness(K):
    """Return an exact integer z with z^T K z < 0, or None.

    Floating point is used only to propose z. Rejection is governed solely by
    the exact integer quadratic form below.
    """
    vals, vecs = np.linalg.eigh(K.astype(float))
    if vals[0] >= -1e-10:
        return None
    u = vecs[:, 0]
    for scale in (4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048):
        z = np.rint(scale * u).astype(np.int64)
        if not np.any(z):
            continue
        q = int(z @ K @ z)
        if q < 0:
            return z
    return None


def exhaustive_survivors(N, s):
    I = np.eye(N, dtype=np.int64)
    survivors = []
    rejected = 0
    for alpha in (-1, 1):
        for mask in range(1 << N):
            tau = tuple(1 if (mask >> i) & 1 else -1 for i in range(N))
            A = hamilton_gauge_A(N, s, alpha, tau)
            K = 6 * I - A @ A
            z = integer_negative_witness(K)
            if z is not None:
                # Exact branch-acceptance inequality.
                assert int(z @ K @ z) < 0
                rejected += 1
                continue
            survivors.append((alpha, tau, A, K))
    assert rejected + len(survivors) == 2 ** (N + 1)
    return survivors


def certify_survivors_12_4():
    survivors = exhaustive_survivors(12, 4)
    assert len(survivors) == 2
    assert Counter(alpha for alpha, *_ in survivors) == Counter({-1: 2})

    expected_A = (x**2 - 6) ** 2 * (x**4 - 6*x**2 + 6) ** 2
    expected_K = x**4 * (x**2 - 6*x + 6) ** 4
    words = set()
    for alpha, tau, A, K in survivors:
        pA = sp.factor(sp.Matrix(A.tolist()).charpoly(x).as_expr())
        pK = sp.factor(sp.Matrix(K.tolist()).charpoly(x).as_expr())
        assert sp.expand(pA - expected_A) == 0
        assert sp.expand(pK - expected_K) == 0
        words.add(tau)
    assert len(words) == 2
    print("(12,4): exactly 2 labelled switching classes")


def certify_survivors_16_3():
    survivors = exhaustive_survivors(16, 3)
    assert len(survivors) == 32
    assert Counter(alpha for alpha, *_ in survivors) == Counter({-1: 16, 1: 16})

    expected_A = x**2 * (x - 2) * (x + 2) * (x**2 - 6) ** 4 * (x**2 - 2) ** 2
    expected_K = x**8 * (x - 6) ** 2 * (x - 4) ** 4 * (x - 2) ** 2
    for alpha, tau, A, K in survivors:
        M = sp.Matrix(A.tolist())
        B = M * M - 4 * sp.eye(16)
        twos = [
            (i, j)
            for i in range(16)
            for j in range(i + 1, 16)
            if abs(int(B[i, j])) == 2
        ]
        assert len(twos) == 2
        pA = sp.factor(M.charpoly(x).as_expr())
        pK = sp.factor(sp.Matrix(K.tolist()).charpoly(x).as_expr())
        assert sp.expand(pA - expected_A) == 0
        assert sp.expand(pK - expected_K) == 0
    print("(16,3): exactly 32 labelled switching classes, 16 for each holonomy")

    # Multiplication by 5 sends {+-1,+-3} to {+-1,+-5} modulo 16.
    image = {(5 * d) % 16 for d in (1, -1, 3, -3)}
    target = {d % 16 for d in (1, -1, 5, -5)}
    assert image == target
    print("(16,5): exactly 32 classes by the multiplier-5 graph isomorphism")


def certify_20_8_recurrence():
    N, s = 20, 8
    # The t=2 component theorem forces original Hamilton holonomy alpha=-1.
    h = [1] * N
    h[N - 1] = -1

    words = []
    for c0 in (-1, 1):
        c = [None] * N
        c[0] = c0
        for i in range(N - 1):
            c[i + 1] = -h[i] * h[(i + s) % N] * c[i]
        # Exact cyclic consistency of the mixed-channel recurrence.
        assert c[0] == -h[N - 1] * h[(N - 1 + s) % N] * c[N - 1]
        words.append(tuple(c))

    assert words[1] == tuple(-z for z in words[0])
    expected_A = (x**2 - 6) ** 2 * (
        x**8 - 14*x**6 + 66*x**4 - 114*x**2 + 41
    ) ** 2
    for tau in words:
        A = sp.Matrix(hamilton_gauge_A(N, s, -1, tau).tolist())
        pA = sp.factor(A.charpoly(x).as_expr())
        assert sp.expand(pA - expected_A) == 0
    print("(20,8): recurrence leaves exactly 2 equality classes")


def main():
    certify_survivors_12_4()
    certify_survivors_16_3()
    certify_20_8_recurrence()
    print("All sqrt(6)-boundary minimizer-rigidity certificates passed.")


if __name__ == "__main__":
    main()
