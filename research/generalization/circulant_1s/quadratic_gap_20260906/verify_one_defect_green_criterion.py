#!/usr/bin/env python3
"""Regression for the exact rank-four / 2x2 Green criterion.

The theorem is analytic in ONE_DEFECT_RANK4_GREEN_CRITERION.md.  This script
checks representative finite matrices:

- C = 8I-A^2;
- C0 = (4I-X^2)+(4I-Y^2) is positive;
- K=C0-C has exactly the two claimed undirected weight -2 defect edges;
- reflection reduces the dangerous Birman-Schwinger matrix to 2x2;
- lambda_max(G_-) < 1/2 exactly when the full threshold is positive in the
  tested cases.

Floating linear algebra here is regression only, not theorem evidence.
"""

from __future__ import annotations

import numpy as np


def adjacency(N: int, s: int, epsilon: int = -1, alpha: int = +1) -> np.ndarray:
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


def split_xy(N: int, s: int) -> tuple[np.ndarray, np.ndarray]:
    A = adjacency(N, s)
    X = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for step in (+1, -1):
            d = i + step
            j = d % N
            X[i, j] += 1  # alpha=+1 in this verifier
    Y = A - X
    assert np.array_equal(X, X.T)
    assert np.array_equal(Y, Y.T)
    return X, Y


def green_minus(C0: np.ndarray, s: int) -> np.ndarray:
    N = C0.shape[0]
    p, q, r, t = 0, s - 1, s, N - 1
    U = np.zeros((N, 2), dtype=float)
    U[p, 0] = 1 / np.sqrt(2)
    U[q, 0] = -1 / np.sqrt(2)
    U[r, 1] = 1 / np.sqrt(2)
    U[t, 1] = -1 / np.sqrt(2)
    Z = np.linalg.solve(C0.astype(float), U)
    Gm = U.T @ Z
    return (Gm + Gm.T) / 2


def main() -> None:
    cases = (
        (5, 9, True),
        (5, 11, False),
        (7, 13, True),
        (7, 15, False),
        (9, 17, True),
        (9, 19, False),
        (13, 27, True),
        (13, 29, False),
    )

    for L, s, expected_positive in cases:
        N = L * s
        X, Y = split_xy(N, s)
        A = X + Y
        C0 = (
            4 * np.eye(N, dtype=np.int64) - X @ X
            + 4 * np.eye(N, dtype=np.int64) - Y @ Y
        )
        C = 8 * np.eye(N, dtype=np.int64) - A @ A
        K = C0 - C

        expected = np.zeros_like(K)
        expected[0, s - 1] = expected[s - 1, 0] = -2
        expected[s, N - 1] = expected[N - 1, s] = -2
        assert np.array_equal(K, expected)

        # Reflection R(i)=s-1-i mod N preserves C0.
        perm = np.array([(s - 1 - i) % N for i in range(N)], dtype=int)
        assert np.array_equal(C0, C0[np.ix_(perm, perm)])

        min_c0 = float(np.linalg.eigvalsh(C0.astype(float))[0])
        assert min_c0 > 1e-9

        Gm = green_minus(C0, s)
        bs = float(np.linalg.eigvalsh(Gm)[-1])
        min_c = float(np.linalg.eigvalsh(C.astype(float))[0])

        if expected_positive:
            assert bs < 0.5
            assert min_c > 0
        else:
            assert bs > 0.5
            assert min_c < 0

        print(
            f"L={L:2d}, s={s:2d}: lambda_max(G-)={bs:.12f}, "
            f"min(C)={min_c:.12e}, min(C0)={min_c0:.6g}"
        )

    print("rank-four / 2x2 Green criterion regression passed")


if __name__ == "__main__":
    main()
