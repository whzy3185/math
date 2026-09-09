#!/usr/bin/env python3
"""Exact integer sanity checks for ODD_RESONANCE_STEP3_SUBSQRT8.md.

For odd k, N=3k, constructs the Hamilton-seam/chord-alternating signing and
checks the exact entries of K=8I-A^2 after multiplication-by-2 reindexing:
  * diag 4;
  * all base C_N(1,3) off-diagonals are +/-1;
  * exactly one extra off-diagonal entry -2, at {0,N-2};
  * the three absorbing length-two paths are edge-disjoint and have negative
    signed path product.

This script is only a finite sanity audit. The theorem itself is the analytic
all-k argument in the companion Markdown proof.
"""

import numpy as np


def matrix_A(N):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    for i in range(N):
        j = (i + 3) % N
        A[i, j] = A[j, i] = 1 if i % 2 == 0 else -1
    return A


def check(k):
    assert k >= 3 and k % 2 == 1
    N = 3 * k
    A = matrix_A(N)
    K = 8 * np.eye(N, dtype=np.int64) - A @ A

    p = [(2 * j) % N for j in range(N)]
    M = K[np.ix_(p, p)]

    assert np.all(np.diag(M) == 4)

    exceptional = []
    base_edges = set()
    for i in range(N):
        for j in range(i + 1, N):
            val = int(M[i, j])
            if val == 0:
                continue
            d = min((j - i) % N, (i - j) % N)
            if d in (1, 3):
                assert abs(val) == 1
                base_edges.add((i, j))
            else:
                exceptional.append((i, j, val))

    assert exceptional == [(0, N - 2, -2)]
    assert len(base_edges) == 2 * N

    u, v = 0, N - 2
    paths = [(u, 1, v), (u, N - 3, v), (u, N - 1, v)]
    used = set()
    for a, w, b in paths:
        e1 = tuple(sorted((a, w)))
        e2 = tuple(sorted((w, b)))
        assert e1 in base_edges and e2 in base_edges
        assert e1 not in used and e2 not in used
        used.add(e1)
        used.add(e2)
        sigma1 = -int(M[a, w])
        sigma2 = -int(M[w, b])
        assert sigma1 * sigma2 == -1

    # Exact channel table in the original labels.
    B = A @ A - 4 * np.eye(N, dtype=np.int64)
    for x in range(N):
        expected2 = 1 if x <= N - 4 else -1
        assert int(B[x, (x + 2) % N]) == expected2

        expected4 = 2 if x == N - 4 else 0
        assert int(B[x, (x + 4) % N]) == expected4

        expected6 = -1 if x <= N - 4 else 1
        assert int(B[x, (x + 6) % N]) == expected6


if __name__ == "__main__":
    for k in range(3, 102, 2):
        check(k)
    print("Exact step-three decomposition sanity checks passed for odd 3<=k<=101.")
