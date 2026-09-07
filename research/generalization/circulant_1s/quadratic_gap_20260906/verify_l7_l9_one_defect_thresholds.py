#!/usr/bin/env python3
"""Exact certificates for the L=7 and L=9 one-defect thresholds.

The short sub-eight cases use exact rational LDL on C=8I-A^2.
The long side uses fixed 2L-column seam windows.  Floating eigenvectors are
only witness proposers; acceptance is exact integer arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import numpy as np


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


def exact_ldl_pivots(C: np.ndarray) -> list[Fraction]:
    n = C.shape[0]
    Lm = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    D = [Fraction(0) for _ in range(n)]
    for i in range(n):
        Lm[i][i] = Fraction(1)
        di = Fraction(int(C[i, i]))
        for k in range(i):
            di -= Lm[i][k] * Lm[i][k] * D[k]
        D[i] = di
        assert di != 0
        for j in range(i + 1, n):
            x = Fraction(int(C[j, i]))
            for k in range(i):
                x -= Lm[j][k] * Lm[i][k] * D[k]
            Lm[j][i] = x / di
    return D


def seam_window(L: int, s: int, epsilon: int, alpha: int) -> np.ndarray:
    N = L * s
    A = adjacency(N, s, epsilon, alpha)
    cols = list(range(s - L, s)) + list(range(L))
    verts = [j + a * s for j in cols for a in range(L)]
    B = A[np.ix_(verts, verts)]
    assert B.shape == (2 * L * L, 2 * L * L)
    return B


def exact_short_side(L: int, short_s: tuple[int, ...]) -> None:
    for s in short_s:
        A = adjacency(L * s, s, -1, +1)
        C = 8 * np.eye(L * s, dtype=np.int64) - A @ A
        pivots = exact_ldl_pivots(C)
        assert all(p > 0 for p in pivots)
        print(f"L={L}, s={s}: exact LDL positive; min pivot={min(pivots)}")


def exact_long_side(L: int, denominator: int, scale: int = 3000) -> None:
    s0 = 2 * L + 1
    for epsilon in (+1, -1):
        for alpha in (+1, -1):
            B0 = seam_window(L, s0, epsilon, alpha)
            # Structural regression: the same local matrix recurs for later odd s.
            for s in (s0 + 2, s0 + 4):
                assert np.array_equal(B0, seam_window(L, s, epsilon, alpha))

            K = B0 @ B0 - 8 * np.eye(B0.shape[0], dtype=np.int64)
            vals, vecs = np.linalg.eigh(K.astype(float))
            w = np.rint(scale * vecs[:, int(np.argmax(vals))]).astype(np.int64)
            q = int(w @ (K @ w))
            norm = int(w @ w)
            assert q > 0 and norm > 0
            assert denominator * q >= norm
            print(
                f"L={L}, sector=({epsilon:+d},{alpha:+d}): "
                f"q={q}, norm={norm}, margin >= 1/{denominator}"
            )



def main() -> None:
    exact_short_side(7, (3, 5, 7, 9, 11, 13))
    exact_long_side(7, 142)

    exact_short_side(9, (3, 5, 7, 9, 11, 13, 15, 17))
    exact_long_side(9, 652)

    print("L=7 and L=9 one-defect threshold certificates passed")


if __name__ == "__main__":
    main()
