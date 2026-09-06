#!/usr/bin/env python3
"""Exact local certificate for the one-defect family on C_(3s)(1,s).

The theorem proved in N3S_ONE_DEFECT_LOCAL_OBSTRUCTION.md is uniform for odd
s>=7.  The proof note shows that, after ordering the six columns

    s-3, s-2, s-1, 0, 1, 2

and the three vertices j, j+s, j+2s inside each column, the induced 18x18
signed adjacency matrix is independent of the magnitude of odd s (for each
fixed anchor/holonomy sector).

This verifier:
1. builds the seam-safe finite Hamilton-gauge matrix;
2. checks the 18x18 block is literally stable for several odd s;
3. verifies an integer Rayleigh witness in each of the four sectors.

All certificate arithmetic is integer arithmetic.  The eigenvalue printout is
for scale intuition only and is not used in the proof.
"""

from __future__ import annotations

import numpy as np


WITNESSES = {
    (+1, +1): [-1, 1, 1, 1, 0, -1, -3, 1, 3, -3, 3, 1, 1, -1, 0, -1, 1, 1],
    (+1, -1): [-1, -1, 1, -1, 0, 1, -3, -1, 3, -3, -3, 1, -1, -1, 0, -1, -1, 1],
    (-1, +1): [1, -1, -1, 1, 0, -1, 3, -1, -3, -3, 3, 1, -1, 1, 0, -1, 1, 1],
    (-1, -1): [1, 1, -1, -1, 0, 1, 3, 1, -3, -3, -3, 1, 1, 1, 0, -1, -1, 1],
}


def shift_matrix(n: int, alpha: int) -> np.ndarray:
    T = np.zeros((n, n), dtype=np.int64)
    for i in range(n - 1):
        T[i, i + 1] = 1
    T[n - 1, 0] = alpha
    return T


def adjacency(s: int, anchor: int, alpha: int) -> np.ndarray:
    n = 3 * s
    T = shift_matrix(n, alpha)
    tau = np.array([anchor * (1 if i % 2 == 0 else -1) for i in range(n)], dtype=np.int64)
    M = np.diag(tau)
    Ts = np.linalg.matrix_power(T, s)
    Tms = np.linalg.matrix_power(T.T, s)
    A = T + T.T + M @ Ts + Tms @ M
    assert np.array_equal(A, A.T)
    return A


def window_indices(s: int) -> list[int]:
    columns = (s - 3, s - 2, s - 1, 0, 1, 2)
    return [j + a * s for j in columns for a in range(3)]


def local_block(s: int, anchor: int, alpha: int) -> np.ndarray:
    A = adjacency(s, anchor, alpha)
    idx = window_indices(s)
    return A[np.ix_(idx, idx)]


def main() -> None:
    templates = {}

    for sector, entries in WITNESSES.items():
        anchor, alpha = sector
        B = local_block(7, anchor, alpha)
        templates[sector] = B
        w = np.array(entries, dtype=np.int64)
        norm = int(w @ w)
        excess = int(w @ ((B @ B - 8 * np.eye(18, dtype=np.int64)) @ w))

        assert norm == 48
        assert excess == 2
        # Exact Rayleigh value: (8*48+2)/48 = 193/24.
        assert 24 * (8 * norm + excess) == 193 * norm

        rho2 = float(np.max(np.abs(np.linalg.eigvalsh(B.astype(float)))) ** 2)
        print(
            f"sector anchor={anchor:+d}, alpha={alpha:+d}: "
            f"norm={norm}, excess={excess}, local rho^2≈{rho2:.12f}"
        )

    # Regression only: the proof of stability for all odd s>=7 is structural
    # and is written in the companion note.  These checks protect the indexing.
    for s in (9, 11, 13, 15, 17):
        for sector, template in templates.items():
            assert np.array_equal(local_block(s, *sector), template)

    print("local blocks stable on regression sample")
    print("exact theorem margin: rho(A)^2 >= 193/24 = 8 + 1/24")
    print("N=3s one-defect local obstruction certificate passed")


if __name__ == "__main__":
    main()
