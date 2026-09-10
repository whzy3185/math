#!/usr/bin/env python3
"""Exact positive-side certificates for ODD_RESONANCE_STEP15_NEAR_CLASSIFICATION.md."""

from collections import deque
import numpy as np
import sympy as sp

SMALL_DETS = {
    9: 29245809126400346085098954358334266552911234352814393414526937002488,
    11: 81345420562709807947141505074935918169325573548550037178098091486387968952830846792,
    13: 162521835310602873945303957432859962422579081241254071361556594492099339038312172488240807040047224,
    15: 293804017270487835611162286466320538777943101838852071037075676365802812233712833302287545180173427118677957140744,
    17: 510683970816354646530633036895217853290955435153117124541465070106856490524072524819498061323926375744552520079062894287446875000,
    19: 872488811110783040085698329295180035174154225756377199094999455714249783071274359877825226852699703364096334509183149674930571596815483736822600,
}
LOCAL_DETS = {
    "neg": 3778167212446958262349168881634331311931392,
    "pos": 105402599868300324129777428804783514283081728,
}
K7_DET = 1849301460651035605088456882195255546256126182948864


def matrix_A(N, modified_k7=False):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    tau = [1 if i % 2 == 0 else -1 for i in range(N)]
    if modified_k7:
        assert N == 105
        tau[86] *= -1
        tau[87] *= -1
    for i, sig in enumerate(tau):
        j = (i + 15) % N
        A[i, j] = A[j, i] = sig
    return A


def positive_ldl(Q):
    _, D = Q.LDLdecomposition(hermitian=False)
    pivots = [sp.factor(D[i, i]) for i in range(D.rows)]
    assert all(p > 0 for p in pivots)
    return pivots


def decomposition(k):
    N = 15 * k
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
            if d in (1, 15):
                assert abs(val) == 1
                base.append((i, j, -val))
            else:
                exc.append((i, j, val))
    a = (N - 15) // 2
    assert exc == [(0, N - 8, -2), (a, a + 7, 2)]
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


def check_modified_k7():
    N = 105
    A = matrix_A(N, modified_k7=True)
    Q = sp.Matrix((8 * np.eye(N, dtype=np.int64) - A @ A).tolist())
    positive_ldl(Q)
    assert int(Q.det()) == K7_DET


def check_small(k):
    N, M, _, _ = decomposition(k)
    Q = sp.Matrix(M.tolist())
    positive_ldl(Q)
    assert int(Q.det()) == SMALL_DETS[k]


def check_large(k):
    N, _, base, exc = decomposition(k)
    neg, pos = exc
    vn, en = ball_edges(N, base, neg[:2], 5)
    vp, ep = ball_edges(N, base, pos[:2], 5)
    assert len(vn) == 109 and len(en) == 188
    assert len(vp) == 110 and len(ep) == 192
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
    check_modified_k7()
    for k in (9, 11, 13, 15, 17, 19):
        check_small(k)
    for k in (21, 23, 25, 27):
        check_large(k)
    print("Exact step-fifteen positive-side certificates passed; k=5 remains open.")
