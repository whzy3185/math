#!/usr/bin/env python3
"""Exact certificates for the L=13 one-defect threshold.

Positive side:
- s=3: exact LDL on the full 39x39 threshold matrix;
- s=5,7,...,27: exact rational LDL on the 52x52 endpoint Schur matrix.

Negative side:
- for all odd s>=29 a fixed 28-column seam window is independent of s;
- a floating eigensolver only proposes an integer witness;
- exact integer arithmetic verifies a 1/940 Rayleigh excess in all sectors.
"""

from __future__ import annotations

from fractions import Fraction
import numpy as np
import sympy as sp


L0 = 13


def adjacency(N: int, s: int, epsilon: int, alpha: int) -> np.ndarray:
    tau = np.array([epsilon * (1 if i % 2 == 0 else -1) for i in range(N)], dtype=np.int64)
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for step, coeff in (
            (+1, 1), (-1, 1), (+s, int(tau[i])), (-s, int(tau[(i - s) % N]))
        ):
            d = i + step
            j = d % N
            wrap = alpha if (d < 0 or d >= N) else 1
            A[i, j] += coeff * wrap
    assert np.array_equal(A, A.T)
    return A


def exact_ldl_dense(M: sp.Matrix) -> list[sp.Rational]:
    n = M.rows
    Lm = sp.zeros(n)
    D = [sp.Rational(0) for _ in range(n)]
    for i in range(n):
        Lm[i, i] = 1
        di = M[i, i]
        for k in range(i):
            di -= Lm[i, k] ** 2 * D[k]
        di = sp.cancel(di)
        assert di != 0
        D[i] = di
        for j in range(i + 1, n):
            x = M[j, i]
            for k in range(i):
                x -= Lm[j, k] * Lm[i, k] * D[k]
            Lm[j, i] = sp.cancel(x / di)
    return D


def chord_block(L: int, epsilon: int, alpha: int) -> sp.Matrix:
    B = sp.zeros(L)
    for a in range(L - 1):
        sign = epsilon * ((-1) ** a)
        B[a, a + 1] = sign
        B[a + 1, a] = sign
    sign = epsilon * alpha
    B[L - 1, 0] = sign
    B[0, L - 1] = sign
    return B


def signed_shift(L: int, alpha: int) -> sp.Matrix:
    S = sp.zeros(L)
    for a in range(L - 1):
        S[a, a + 1] = 1
    S[L - 1, 0] = alpha
    return S


def endpoint_matrix(L: int, s: int, epsilon: int, alpha: int) -> sp.Matrix:
    assert s % 2 == 1 and s >= 5
    r = (s - 1) // 2
    B = chord_block(L, epsilon, alpha)
    G = 6 * sp.eye(L) - B * B

    D = [sp.eye(L)]
    dm1 = sp.zeros(L)
    d0 = D[0]
    for _ in range(1, r + 1):
        d1 = G * d0 - dm1
        D.append(d1)
        dm1, d0 = d0, d1

    He = D[r] * D[r - 1].inv()
    Je = D[r - 1].inv()
    Ho = D[r - 1] * D[r - 2].inv()
    Jo = D[r - 2].inv()

    P = -signed_shift(L, alpha).T
    M = sp.zeros(L)
    M[0, 0] = -2 * epsilon
    M[1, L - 1] = -2 * epsilon * alpha
    Z = sp.zeros(L)

    return sp.Matrix.vstack(
        sp.Matrix.hstack(He, -Je + M, Z, P),
        sp.Matrix.hstack(-Je + M.T, He, P.T, Z),
        sp.Matrix.hstack(Z, P, Ho, -Jo),
        sp.Matrix.hstack(P.T, Z, -Jo, Ho),
    )


def exact_short_positive() -> None:
    # s=3 is below the endpoint-reduction r>=2 range.
    A3 = sp.Matrix(adjacency(39, 3, -1, +1).tolist())
    C3 = 8 * sp.eye(39) - A3 * A3
    p3 = exact_ldl_dense(C3)
    assert all(p > 0 for p in p3)
    print("L=13,s=3: full exact LDL positive")

    for s in range(5, 28, 2):
        E = endpoint_matrix(13, s, -1, +1)
        pivots = exact_ldl_dense(E)
        assert all(p > 0 for p in pivots)
        print(f"L=13,s={s}: endpoint exact LDL positive; min~{float(min(pivots)):.12g}")

    E29 = endpoint_matrix(13, 29, -1, +1)
    p29 = exact_ldl_dense(E29)
    assert sum(p < 0 for p in p29) == 1
    print("L=13,s=29: endpoint exact LDL has exactly one negative pivot")


def seam_window(s: int, epsilon: int, alpha: int) -> np.ndarray:
    N = 13 * s
    A = adjacency(N, s, epsilon, alpha)
    cols = list(range(s - 14, s)) + list(range(14))
    verts = [j + a * s for j in cols for a in range(13)]
    B = A[np.ix_(verts, verts)]
    assert B.shape == (364, 364)
    return B


def exact_long_obstruction() -> None:
    for epsilon in (+1, -1):
        for alpha in (+1, -1):
            B29 = seam_window(29, epsilon, alpha)
            for s in (31, 33):
                assert np.array_equal(B29, seam_window(s, epsilon, alpha))

            K = B29 @ B29 - 8 * np.eye(364, dtype=np.int64)
            vals, vecs = np.linalg.eigh(K.astype(float))
            w = np.rint(256 * vecs[:, -1]).astype(np.int64)
            q = int(w @ (K @ w))
            norm = int(w @ w)
            assert q == 70
            assert norm == 65756
            assert 940 * q >= norm
            print(
                f"sector ({epsilon:+d},{alpha:+d}): q={q}, norm={norm}, "
                "exact excess >=1/940"
            )


def main() -> None:
    exact_short_positive()
    exact_long_obstruction()
    print("L=13 one-defect threshold certificates passed")


if __name__ == "__main__":
    main()
