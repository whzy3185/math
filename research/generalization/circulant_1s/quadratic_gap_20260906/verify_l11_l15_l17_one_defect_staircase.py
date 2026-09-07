#!/usr/bin/env python3
"""Exact certification for the L=11,15,17,19 one-defect staircase theorems.

Positive side: exact rational LDL on the full s=3 threshold and on the exact
4L endpoint Schur matrices for all subsequent favorable odd s through the last
positive value.

Negative side: exact endpoint inertia at the first failed point when needed,
and fixed seam-window integer Rayleigh witnesses for the infinite tails.
Floating eigensolvers only propose integer vectors; acceptance is exact.
"""

from __future__ import annotations

import numpy as np
import sympy as sp


def adjacency(N: int, s: int, epsilon: int, alpha: int) -> np.ndarray:
    tau = np.array(
        [epsilon * (1 if i % 2 == 0 else -1) for i in range(N)],
        dtype=np.int64,
    )
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


def exact_ldl(M: sp.Matrix) -> list[sp.Rational]:
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
        B[a, a + 1] = B[a + 1, a] = sign
    B[L - 1, 0] = B[0, L - 1] = epsilon * alpha
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


def exact_positive_side(L: int, last_s: int) -> None:
    A3 = sp.Matrix(adjacency(3 * L, 3, -1, +1).tolist())
    C3 = 8 * sp.eye(3 * L) - A3 * A3
    assert all(p > 0 for p in exact_ldl(C3))

    for s in range(5, last_s + 1, 2):
        pivots = exact_ldl(endpoint_matrix(L, s, -1, +1))
        assert all(p > 0 for p in pivots)
    print(f"L={L}: favorable sector exact-positive through s={last_s}")


def endpoint_negative_all_sectors(L: int, s: int) -> None:
    for epsilon in (+1, -1):
        for alpha in (+1, -1):
            pivots = exact_ldl(endpoint_matrix(L, s, epsilon, alpha))
            assert sum(1 for p in pivots if p < 0) == 1
    print(f"L={L}, s={s}: every sector has one negative endpoint direction")


def seam_window(L: int, s: int, half_width: int, epsilon: int, alpha: int) -> np.ndarray:
    A = adjacency(L * s, s, epsilon, alpha)
    cols = list(range(s - half_width, s)) + list(range(half_width))
    verts = [j + a * s for j in cols for a in range(L)]
    return A[np.ix_(verts, verts)]


def exact_seam_margin(
    L: int,
    first_s: int,
    half_width: int,
    denominator: int,
) -> None:
    scales = (64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048)
    for epsilon in (+1, -1):
        for alpha in (+1, -1):
            B = seam_window(L, first_s, half_width, epsilon, alpha)
            assert np.array_equal(
                B,
                seam_window(L, first_s + 2, half_width, epsilon, alpha),
            )
            K = B @ B - 8 * np.eye(B.shape[0], dtype=np.int64)
            _, vecs = np.linalg.eigh(K.astype(float))
            direction = vecs[:, -1]

            found = False
            for scale in scales:
                w = np.rint(scale * direction).astype(np.int64)
                q = int(w @ (K @ w))
                norm = int(w @ w)
                if q > 0 and denominator * q >= norm:
                    found = True
                    break
            assert found
    print(
        f"L={L}: fixed seam window certifies rho^2 >= 8 + 1/{denominator} "
        f"for all odd s >= {first_s}"
    )


def main() -> None:
    exact_positive_side(11, 21)
    endpoint_negative_all_sectors(11, 23)
    exact_seam_margin(11, 25, 12, 192)

    exact_positive_side(15, 31)
    exact_seam_margin(15, 33, 16, 695)

    exact_positive_side(17, 35)
    endpoint_negative_all_sectors(17, 37)
    exact_seam_margin(17, 37, 18, 1368)

    exact_positive_side(19, 39)
    endpoint_negative_all_sectors(19, 41)
    exact_seam_margin(19, 41, 20, 2062)

    print("L=11,15,17,19 staircase certificates passed")


if __name__ == "__main__":
    main()
