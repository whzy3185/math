#!/usr/bin/env python3
"""Exact rational certificates for ODD_RESONANCE_STEP9_THRESHOLD.md."""

from collections import deque
import numpy as np
import sympy as sp

SMALL_DETS = {
    5: 5778082039393928857600,
    7: 31457372231947501970186116635000,
    9: 56393166545984053083524808491473067473032,
    11: 87405434664864892313642576876982893413875798493048,
}
LOCAL_DETS = {
    "neg": 4755725738737168,
    "pos": 169914513354912,
}


def matrix_A(N):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    for i in range(N):
        j = (i + 9) % N
        A[i, j] = A[j, i] = 1 if i % 2 == 0 else -1
    return A


def positive_ldl(Q):
    _, D = Q.LDLdecomposition(hermitian=False)
    pivots = [sp.factor(D[i, i]) for i in range(D.rows)]
    assert all(p > 0 for p in pivots)
    return pivots


def decomposition(k):
    N = 9 * k
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
            if d in (1, 9):
                assert abs(val) == 1
                base.append((i, j, -val))
            else:
                exc.append((i, j, val))
    a = (N - 9) // 2
    assert exc == [(0, N - 5, -2), (a, a + 4, 2)]
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
    return verts, [e for e in base if e[0] in verts and e[1] in verts]


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


def check_small(k):
    N, M, _, _ = decomposition(k)
    Q = sp.Matrix(M.tolist())
    positive_ldl(Q)
    assert int(Q.det()) == SMALL_DETS[k]


def check_large(k):
    N, M, base, exc = decomposition(k)
    neg, pos = exc
    vn, en = ball_edges(N, base, neg[:2], 3)
    vp, ep = ball_edges(N, base, pos[:2], 3)
    assert len(vn) == 44 and len(en) == 72
    assert len(vp) == 43 and len(ep) == 68
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
    for k in (5, 7, 9, 11):
        check_small(k)
    for k in range(13, 102, 2):
        check_large(k)
    print("Exact step-nine threshold certificates passed for odd 5<=k<=101.")
