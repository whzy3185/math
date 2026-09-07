#!/usr/bin/env python3
"""Regression for the exact 4L endpoint reduction of one-defect C_(Ls)(1,s).

The analytic reduction is in ONE_DEFECT_ENDPOINT_REDUCTION.md.  This script
performs two checks:

1. reconstruct the complete threshold matrix 8I-A^2 from the claimed block
   pattern and compare it entry-by-entry over the integers;
2. construct the 4L endpoint Schur matrix from matrix continuants and compare
   its negative inertia / determinant sign with the full threshold matrix.

The second check uses floating linear algebra only as a regression; the
reduction itself is an exact Schur-complement theorem.
"""

from __future__ import annotations

import numpy as np


def adjacency(N: int, s: int, epsilon: int, alpha: int) -> np.ndarray:
    tau = np.array([epsilon * (1 if i % 2 == 0 else -1) for i in range(N)], dtype=np.int64)
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for step, coeff in (
            (+1, 1),
            (-1, 1),
            (+s, int(tau[i])),
            (-s, int(tau[(i - s) % N])),
        ):
            d = i + step
            j = d % N
            wrap = alpha if (d < 0 or d >= N) else 1
            A[i, j] += coeff * wrap
    assert np.array_equal(A, A.T)
    return A


def column_order(L: int, s: int) -> list[int]:
    return [j + a * s for j in range(s) for a in range(L)]


def threshold_in_columns(L: int, s: int, epsilon: int, alpha: int) -> tuple[np.ndarray, np.ndarray]:
    A = adjacency(L * s, s, epsilon, alpha)
    order = column_order(L, s)
    Ap = A[np.ix_(order, order)]
    Cp = 8 * np.eye(L * s, dtype=np.int64) - Ap @ Ap
    return Ap, Cp


def signed_shift(L: int, alpha: int) -> np.ndarray:
    S = np.zeros((L, L), dtype=np.int64)
    for a in range(L - 1):
        S[a, a + 1] = 1
    S[L - 1, 0] = alpha
    return S


def predicted_threshold(L: int, s: int, epsilon: int, alpha: int, B: np.ndarray) -> np.ndarray:
    C = np.zeros((L * s, L * s), dtype=np.int64)
    I = np.eye(L, dtype=np.int64)
    G = 6 * I - B @ B

    def put(j: int, k: int, X: np.ndarray) -> None:
        C[j * L : (j + 1) * L, k * L : (k + 1) * L] += X

    for j in range(s):
        put(j, j, G)
    for j in range(s - 2):
        put(j, j + 2, -I)
        put(j + 2, j, -I)

    S = signed_shift(L, alpha)
    P = -S.T
    M = np.zeros((L, L), dtype=np.int64)
    M[0, 0] = -2 * epsilon
    M[1, L - 1] = -2 * epsilon * alpha

    put(0, s - 2, P)
    put(s - 2, 0, P.T)
    put(1, s - 1, P)
    put(s - 1, 1, P.T)
    put(0, s - 1, M)
    put(s - 1, 0, M.T)
    return C


def continuants(G: np.ndarray, nmax: int) -> list[np.ndarray]:
    """Return [D_0,...,D_nmax] as float matrices."""
    L = G.shape[0]
    D = [np.eye(L, dtype=float)]
    if nmax == 0:
        return D
    Dm1 = np.zeros((L, L), dtype=float)
    D0 = D[0]
    for _n in range(1, nmax + 1):
        D1 = G.astype(float) @ D0 - Dm1
        D.append(D1)
        Dm1, D0 = D0, D1
    return D


def endpoint_matrix(L: int, s: int, epsilon: int, alpha: int, B: np.ndarray) -> np.ndarray:
    assert s % 2 == 1 and s >= 5
    r = (s - 1) // 2
    G = 6 * np.eye(L, dtype=float) - B.astype(float) @ B.astype(float)
    D = continuants(G, r)

    He = D[r] @ np.linalg.inv(D[r - 1])
    Je = np.linalg.inv(D[r - 1])
    Ho = D[r - 1] @ np.linalg.inv(D[r - 2])
    Jo = np.linalg.inv(D[r - 2])

    S = signed_shift(L, alpha).astype(float)
    P = -S.T
    M = np.zeros((L, L), dtype=float)
    M[0, 0] = -2 * epsilon
    M[1, L - 1] = -2 * epsilon * alpha

    Z = np.zeros((L, L), dtype=float)
    rows = [
        [He, -Je + M, Z, P],
        [-Je + M.T, He, P.T, Z],
        [Z, P, Ho, -Jo],
        [P.T, Z, -Jo, Ho],
    ]
    return np.block(rows)


def inertia(M: np.ndarray, tol: float = 1e-7) -> tuple[int, int, int]:
    vals = np.linalg.eigvalsh((M + M.T) / 2)
    neg = int(np.sum(vals < -tol))
    pos = int(np.sum(vals > tol))
    zero = len(vals) - neg - pos
    return neg, zero, pos


def main() -> None:
    cases = (
        (3, 5), (3, 7),
        (5, 9), (5, 11),
        (7, 13), (7, 15),
        (9, 17), (9, 19),
    )

    for L, s in cases:
        for epsilon, alpha in ((-1, +1), (+1, +1), (-1, -1)):
            Ap, C = threshold_in_columns(L, s, epsilon, alpha)
            B = Ap[0:L, 0:L]
            Cpred = predicted_threshold(L, s, epsilon, alpha, B)
            assert np.array_equal(C, Cpred)

            Sred = endpoint_matrix(L, s, epsilon, alpha, B)
            i_full = inertia(C.astype(float))
            i_red = inertia(Sred)
            assert i_full[0] == i_red[0]
            assert i_full[1] == i_red[1]

            sign_full = np.linalg.slogdet(C.astype(float))[0]
            sign_red = np.linalg.slogdet(Sred)[0]
            assert sign_full == sign_red

            print(
                f"L={L:2d}, s={s:2d}, eps={epsilon:+d}, alpha={alpha:+d}: "
                f"inertia(full)={i_full}, inertia(endpoint)={i_red}, "
                f"det-sign={int(sign_full):+d}"
            )

    print("one-defect endpoint reduction regression passed")


if __name__ == "__main__":
    main()
