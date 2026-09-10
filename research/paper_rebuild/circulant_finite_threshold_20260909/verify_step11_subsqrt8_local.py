#!/usr/bin/env python3
"""Exact certificates for ODD_RESONANCE_STEP11_THRESHOLD.md.

Floating point is not used for acceptance.  Every PSD/PD assertion is checked
by exact SymPy LDL over the rationals.
"""

from collections import deque
import numpy as np
import sympy as sp

SMALL_DETS = {
    7: 198542354710744646733800591160528965128,
    9: 48537546289326974482796577064517737666501709538432,
    11: 8431528717945196619704965506489933748444911718619217528033864,
    13: 1347032891519196209768694990441713139707122120299552652026241225001964664,
    15: 209465313694967800022162339333057752681888819639940779892042386917708086880013123584,
    17: 32248803804806512732626264860337508296200192468837035466855251667015901045281842241991056567032,
}
LOCAL_DETS = {
    "neg": 58357331759813608134646848,
    "pos": 1526739500502872793417814448,
}
K5_DET = 64811885930109544285440000


def matrix_A(N, modified_k5=False):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    tau = [1 if i % 2 == 0 else -1 for i in range(N)]
    if modified_k5:
        assert N == 55
        tau[40] *= -1
        tau[41] *= -1
    for i, sig in enumerate(tau):
        j = (i + 11) % N
        A[i, j] = A[j, i] = sig
    return A


def positive_ldl(Q):
    _, D = Q.LDLdecomposition(hermitian=False)
    pivots = [sp.factor(D[i, i]) for i in range(D.rows)]
    assert all(p > 0 for p in pivots)
    return pivots


def decomposition(k):
    N = 11 * k
    A = matrix_A(N)
    K = 8 * np.eye(N, dtype=np.int64) - A @ A
    p = [(2 * j) % N for j in range(N)]
    M = K[np.ix_(p, p)]
    base, exc = [], []
    for i in range(N):
        for j in range(i + 1, N):
            val = int(M[i, j])
            if val == 0:
                continue
            d = min((j - i) % N, (i - j) % N)
            if d in (1, 11):
                assert abs(val) == 1
                base.append((i, j, -val))
            else:
                exc.append((i, j, val))
    a = (N - 11) // 2
    assert exc == [(0, N - 6, -2), (a, a + 5, 2)]
    assert len(base) == 2 * N
    return N, M, base, exc


def ball_edges(N, base, seeds, radius):
    adj = [[] for _ in range(N)]
    for i, j, sig in base:
        adj[i].append(j)
        adj[j].append(i)
    dist = {v: 0 for v in seeds}
    q = deque(seeds)
    while q:
        u = q.popleft()
        if dist[u] >= radius:
            continue
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    verts = set(dist)
    edges = [e for e in base if e[0] in verts and e[1] in verts]
    return verts, edges


def local_matrix(edges, ex):
    verts = sorted(set(v for e in edges for v in e[:2]) | set(ex[:2]))
    pos = {v: i for i, v in enumerate(verts)}
    Q = sp.zeros(len(verts))
    for i, j, sig in edges:
        a, b = pos[i], pos[j]
        Q[a, a] += 1
        Q[b, b] += 1
        Q[a, b] -= sig
        Q[b, a] -= sig
    i, j, val = ex
    a, b = pos[i], pos[j]
    Q[a, b] += val
    Q[b, a] += val
    return Q


def check_modified_k5():
    N = 55
    A = matrix_A(N, modified_k5=True)
    Q = sp.Matrix((8 * np.eye(N, dtype=np.int64) - A @ A).tolist())
    positive_ldl(Q)
    assert int(Q.det()) == K5_DET


def check_small(k):
    N, M, _, _ = decomposition(k)
    Q = sp.Matrix(M.tolist())
    positive_ldl(Q)
    assert int(Q.det()) == SMALL_DETS[k]


def check_large(k):
    N, _, base, exc = decomposition(k)
    neg, pos = exc
    vn, en = ball_edges(N, base, neg[:2], 4)
    vp, ep = ball_edges(N, base, pos[:2], 4)
    assert len(vn) == 69 and len(en) == 116
    assert len(vp) == 70 and len(ep) == 120
    assert {tuple(sorted(e[:2])) for e in en}.isdisjoint(
        {tuple(sorted(e[:2])) for e in ep}
    )
    Qn = local_matrix(en, neg)
    Qp = local_matrix(ep, pos)
    positive_ldl(Qn)
    positive_ldl(Qp)
    assert int(Qn.det()) == LOCAL_DETS["neg"]
    assert int(Qp.det()) == LOCAL_DETS["pos"]


if __name__ == "__main__":
    check_modified_k5()
    for k in (7, 9, 11, 13, 15, 17):
        check_small(k)
    # The local pattern is stable; checking several later odd lengths also
    # guards the seam/reindex bookkeeping independently of the proof.
    for k in range(19, 42, 2):
        check_large(k)
    print("Exact step-eleven threshold certificates passed.")
