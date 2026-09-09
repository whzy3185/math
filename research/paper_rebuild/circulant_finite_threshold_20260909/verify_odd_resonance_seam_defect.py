#!/usr/bin/env python3
"""Exact integer sanity audit for ODD_RESONANCE_SEAM_DEFECT_FRAMEWORK.md.

Checks the two-seam-defect decomposition for odd 5<=s<=31 and odd
3<=k<=31. This finite sweep is not the proof; the companion Markdown note
contains the all-parameter channel calculation.
"""

import numpy as np


def matrix_A(N, s):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    for i in range(N):
        j = (i + s) % N
        A[i, j] = A[j, i] = 1 if i % 2 == 0 else -1
    return A


def check(k, s):
    assert k >= 3 and k % 2 == 1
    assert s >= 5 and s % 2 == 1
    N = k * s
    A = matrix_A(N, s)
    K = 8 * np.eye(N, dtype=np.int64) - A @ A
    p = [(2 * j) % N for j in range(N)]
    M = K[np.ix_(p, p)]

    assert np.all(np.diag(M) == 4)
    base = 0
    exceptional = []
    for i in range(N):
        for j in range(i + 1, N):
            val = int(M[i, j])
            if val == 0:
                continue
            d = min((j - i) % N, (i - j) % N)
            if d in (1, s):
                assert abs(val) == 1
                base += 1
            else:
                exceptional.append((i, j, val))

    assert base == 2 * N
    a = (N - s) // 2
    expected = [
        (0, N - (s + 1) // 2, -2),
        (a, (N - 1) // 2, 2),
    ]
    assert exceptional == expected, (k, s, exceptional, expected)


if __name__ == "__main__":
    for s in range(5, 32, 2):
        for k in range(3, 32, 2):
            check(k, s)
    print("Exact two-seam-defect sanity sweep passed.")
