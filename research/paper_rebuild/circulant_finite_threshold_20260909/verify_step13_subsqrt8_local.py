#!/usr/bin/env python3
"""Exact certificates for ODD_RESONANCE_STEP13_THRESHOLD.md."""

from collections import deque
import numpy as np
import sympy as sp

SMALL_DETS = {
    7: 777822683438738293824269088964559041231880192,
    9: 40178111447360478660721529323877341901237465003508791537664,
    11: 834670184595986161898253528412539880891529504123995209158656633956804984,
    13: 14656605269736600831818047041457539635031211796660386607258337268810764502635306436552,
    15: 243585933444252138485512585640693612321567484386234437066272326258045709008024992175761023618919552,
    17: 3963174854812045796053420102968566538099459483102725723763065164924888915802214672795545687441379572817116286024,
}
LOCAL_DETS = {
    "neg": 24571566789956681668333404160,
    "pos": 727573024226645153483653120,
}
K5_DET = 268663021725556297527269942728


def matrix_A(N, modified_k5=False):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    tau = [1 if i % 2 == 0 else -1 for i in range(N)]
    if modified_k5:
        assert N == 65
        tau[54] *= -1
        tau[55] *= -1
    for i, sig in enumerate(tau):
        j = (i + 13) % N
        A[i, j] = A[j, i] = sig
    return A


def positive_ldl(Q):
    _, D = Q.LDLdecomposition(hermitian=False)
    pivots = [sp.factor(D[i, i]) for i in range(D.rows)]
    assert all(p > 0 for p in pivots)
    return pivots


def decomposition(k):
    N = 13 * k
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
            if d in (1, 13):
                assert abs(val) == 1
                base.append((i, j, -val))
            else:
                exc.append((i, j, val))
    a = (N - 13) // 2
    assert exc == [(0, N - 7, -2), (a, a + 6, 2)]
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
    N = 65
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
    assert len(vn) == 76 and len(en) == 128
    assert len(vp) == 75 and len(ep) == 124
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
    for k in range(19, 40, 2):
        check_large(k)
    print("Exact step-thirteen threshold certificates passed.")
