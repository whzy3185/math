#!/usr/bin/env python3
"""Exact certificates for L=5 one-defect threshold on C_(5s)(1,s).

Short positive cases s=3,5,7,9:
  epsilon=-1, alpha=+1, and exact rational LDL shows 8I-A^2 > 0.

Long negative side s>=11:
  a fixed ten-column seam window is independent of s for each
  (epsilon,alpha), and a stored integer witness verifies

      34 * w^T (B^2-8I) w >= w^T w > 0.

All acceptance decisions are exact integer/rational arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
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


def exact_ldl_pivots(C: np.ndarray) -> list[Fraction]:
    n = C.shape[0]
    L = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    D = [Fraction(0) for _ in range(n)]
    for i in range(n):
        L[i][i] = Fraction(1)
        di = Fraction(int(C[i, i]))
        for k in range(i):
            di -= L[i][k] * L[i][k] * D[k]
        D[i] = di
        assert di != 0
        for j in range(i + 1, n):
            x = Fraction(int(C[j, i]))
            for k in range(i):
                x -= L[j][k] * L[i][k] * D[k]
            L[j][i] = x / di
    return D


def seam_window(s: int, epsilon: int, alpha: int) -> np.ndarray:
    N = 5 * s
    A = adjacency(N, s, epsilon, alpha)
    cols = list(range(s - 5, s)) + list(range(5))
    verts = [j + a * s for j in cols for a in range(5)]
    B = A[np.ix_(verts, verts)]
    assert B.shape == (50, 50)
    return B


WITNESSES = {
    (+1, +1): (-8,-7,8,7,-8, -8,-3,10,3,-8, -26,-19,24,19,-26, -21,0,22,0,-21, -53,-24,38,24,-53, -53,-53,24,38,-24, -21,-21,0,22,0, -26,-26,19,24,-19, -8,-8,3,10,-3, -8,-8,7,8,-7),
    (+1, -1): (-8,7,8,-7,-8, 8,-3,-10,3,8, -26,19,24,-19,-26, 21,0,-22,0,21, -53,24,38,-24,-53, -53,53,24,-38,-24, 21,-21,0,22,0, -26,26,19,-24,-19, 8,-8,-3,10,3, -8,8,7,-8,-7),
    (-1, +1): (8,7,-8,-7,8, -8,-3,10,3,-8, 26,19,-24,-19,26, -21,0,22,0,-21, 53,24,-38,-24,53, -53,-53,24,38,-24, 21,21,0,-22,0, -26,-26,19,24,-19, 8,8,-3,-10,3, -8,-8,7,8,-7),
    (-1, -1): (-8,7,8,-7,-8, -8,3,10,-3,-8, -26,19,24,-19,-26, -21,0,22,0,-21, -53,24,38,-24,-53, 53,-53,-24,38,24, 21,-21,0,22,0, 26,-26,-19,24,19, 8,-8,-3,10,3, 8,-8,-7,8,7),
}


def main() -> None:
    expected_min = {
        3: Fraction(2872, 1207),
        5: Fraction(5534344, 3695961),
        7: Fraction(1076085176, 1260574219),
        9: Fraction(6825469384, 26186660017),
    }

    for s in (3, 5, 7, 9):
        A = adjacency(5 * s, s, -1, +1)
        C = 8 * np.eye(5 * s, dtype=np.int64) - A @ A
        pivots = exact_ldl_pivots(C)
        assert all(p > 0 for p in pivots)
        assert min(pivots) == expected_min[s]
        print(f"s={s}: exact LDL positive; min pivot={min(pivots)}")

    # Structural regression: the local matrices stabilize literally for all
    # tested odd s>=11 in each sector.
    for epsilon in (+1, -1):
        for alpha in (+1, -1):
            B11 = seam_window(11, epsilon, alpha)
            for s in (13, 15, 21):
                assert np.array_equal(B11, seam_window(s, epsilon, alpha))

            w = np.array(WITNESSES[(epsilon, alpha)], dtype=np.int64)
            K = B11 @ B11 - 8 * np.eye(50, dtype=np.int64)
            q = int(w @ (K @ w))
            norm = int(w @ w)
            assert q == 752
            assert norm == 25532
            assert 34 * q >= norm
            print(
                f"(epsilon,alpha)=({epsilon:+d},{alpha:+d}): "
                f"q={q}, norm={norm}, exact excess >=1/34"
            )

    print("L=5 one-defect threshold certificates passed")


if __name__ == "__main__":
    main()
