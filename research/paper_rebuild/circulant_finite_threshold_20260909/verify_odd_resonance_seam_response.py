#!/usr/bin/env python3
"""Exact sanity checks for ODD_RESONANCE_SEAM_RESPONSE.md."""

import sympy as sp


def matrix_A(N, s):
    A = sp.zeros(N)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    for i in range(N):
        j = (i + s) % N
        A[i, j] = A[j, i] = 1 if i % 2 == 0 else -1
    return A


def reindex_by_two(M):
    N = M.rows
    p = [(2 * j) % N for j in range(N)]
    return M.extract(p, p)


def decompose(k, s):
    N = k * s
    A = matrix_A(N, s)
    K = reindex_by_two(8 * sp.eye(N) - A * A)
    L = 4 * sp.eye(N)
    exc = []
    for i in range(N):
        for j in range(i + 1, N):
            val = K[i, j]
            if val == 0:
                continue
            d = min((j - i) % N, (i - j) % N)
            if d in (1, s):
                assert abs(val) == 1
                L[i, j] = L[j, i] = val
            else:
                exc.append((i, j, int(val)))
    a = (N - s) // 2
    assert exc == [
        (0, N - (s + 1) // 2, -2),
        (a, (N - 1) // 2, 2),
    ]
    return A, K, L, exc


def unit(N, i):
    e = sp.zeros(N, 1)
    e[i] = 1
    return e


def check(k, s):
    N = k * s
    _, K, L, exc = decompose(k, s)
    u, v, _ = exc[0]
    p, q, _ = exc[1]
    dm = unit(N, u) - unit(N, v)
    rm = unit(N, u) + unit(N, v)
    dp = unit(N, p) - unit(N, q)
    rp = unit(N, p) + unit(N, q)
    H = L + dm * dm.T + rp * rp.T
    U = rm.row_join(dp)
    assert K == H - U * U.T

    # L is positive definite: exact LDL is a direct sanity check of the
    # negative-cycle proof in the note.
    _, DL = L.LDLdecomposition(hermitian=False)
    assert all(DL[i, i] > 0 for i in range(N))

    # Use exact solves rather than forming H^{-1} explicitly.
    X = H.inv() * U
    R = sp.simplify(U.T * X)
    S = sp.eye(2) - R
    det_identity = sp.factor(K.det() - H.det() * S.det())
    assert det_identity == 0

    _, DK = K.LDLdecomposition(hermitian=False)
    k_positive = all(DK[i, i] > 0 for i in range(N))
    s_positive = S[0, 0] > 0 and sp.factor(S.det()) > 0
    assert k_positive == s_positive
    print((k, s), "det(I-R)=", sp.factor(S.det()), "positive=", k_positive)


if __name__ == "__main__":
    for pair in ((5, 5), (5, 11), (7, 11), (7, 15), (9, 15)):
        check(*pair)
    print("Exact seam-response checks passed.")
