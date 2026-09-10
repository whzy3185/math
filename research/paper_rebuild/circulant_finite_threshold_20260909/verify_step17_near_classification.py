#!/usr/bin/env python3
"""Exact certificates for ODD_RESONANCE_STEP17_NEAR_CLASSIFICATION.md."""

from collections import deque
import numpy as np
import sympy as sp

BASE_DETS = {
    9: 14515909660668351009683318712690479467173632461251542314345941502418804539392,
    11: 7492688793090569582564673800444737469151727278364707741193439534177466505946471336223647393400,
    13: 1790558664127079268604134543407240067983781936156338217991028943805500745920632781738041741663509291246243074952,
    15: 359500068543753471128877144761874214766696369741112968277913985433803897042182306477110866507366486440308567777925633255124585600,
    17: 67546510399825407661203323360067075501650647238200944763176564802007271032943793924756110194913954386721922113614655973379735941264038668273325832,
}
K7_DET = 2965591063002674643944833344304548941451919837762075140600
LOCAL_DETS = {
    "neg": 1298197880264878128887655318684082374017286144,
    "pos": 23317294279084925351390808058137339284684800,
}
K19_UNION_DET = 2240939829741199510432570344342121777520575243070525763176968864061624897220596058066905989120


def matrix_A(N, modified_k7=False):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    tau = [1 if i % 2 == 0 else -1 for i in range(N)]
    if modified_k7:
        assert N == 119
        tau[98] *= -1
        tau[99] *= -1
    for i, sig in enumerate(tau):
        j = (i + 17) % N
        A[i, j] = A[j, i] = sig
    return A


def positive_ldl(Q):
    _, D = Q.LDLdecomposition(hermitian=False)
    pivots = [sp.factor(D[i, i]) for i in range(D.rows)]
    assert all(p > 0 for p in pivots)
    return pivots


def decomposition(k):
    N = 17 * k
    A = matrix_A(N)
    K = 8 * np.eye(N, dtype=np.int64) - A @ A
    p = [(2 * j) % N for j in range(N)]
    M = K[np.ix_(p, p)]
    base, exc = [], []
    seen = set()
    for i in range(N):
        for d in (1, 17):
            j = (i + d) % N
            e = tuple(sorted((i, j)))
            if e in seen:
                continue
            seen.add(e)
            val = int(M[e[0], e[1]])
            assert abs(val) == 1
            base.append((e[0], e[1], -val))
    for i in range(N):
        for j in range(i + 1, N):
            val = int(M[i, j])
            if val == 0:
                continue
            d = min((j - i) % N, (i - j) % N)
            if d not in (1, 17):
                exc.append((i, j, val))
    a = (N - 17) // 2
    assert exc == [(0, N - 9, -2), (a, a + 8, 2)]
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


def local_matrix(verts, edges, exceptions):
    verts = sorted(verts)
    pos = {v: i for i, v in enumerate(verts)}
    Q = sp.zeros(len(verts))
    for i, j, sig in edges:
        a, b = pos[i], pos[j]
        Q[a, a] += 1
        Q[b, b] += 1
        Q[a, b] -= sig
        Q[b, a] -= sig
    for i, j, val in exceptions:
        a, b = pos[i], pos[j]
        Q[a, b] += val
        Q[b, a] += val
    return Q


def check_k7():
    A = matrix_A(119, modified_k7=True)
    Q = sp.Matrix((8 * np.eye(119, dtype=np.int64) - A @ A).tolist())
    positive_ldl(Q)
    assert int(Q.det()) == K7_DET


def check_base(k):
    _, M, _, _ = decomposition(k)
    Q = sp.Matrix(M.tolist())
    positive_ldl(Q)
    assert int(Q.det()) == BASE_DETS[k]


def check_k19_union():
    N, _, base, exc = decomposition(19)
    v1, _ = ball_edges(N, base, exc[0][:2], 5)
    v2, _ = ball_edges(N, base, exc[1][:2], 5)
    verts = v1 | v2
    edges = [e for e in base if e[0] in verts and e[1] in verts]
    assert len(verts) == 225 and len(edges) == 398
    Q = local_matrix(verts, edges, exc)
    positive_ldl(Q)
    assert int(Q.det()) == K19_UNION_DET


def check_large(k):
    N, _, base, exc = decomposition(k)
    v1, e1 = ball_edges(N, base, exc[0][:2], 5)
    v2, e2 = ball_edges(N, base, exc[1][:2], 5)
    assert len(v1) == 116 and len(e1) == 200
    assert len(v2) == 115 and len(e2) == 196
    assert {tuple(sorted(e[:2])) for e in e1}.isdisjoint(
        {tuple(sorted(e[:2])) for e in e2}
    )
    Q1 = local_matrix(v1, e1, [exc[0]])
    Q2 = local_matrix(v2, e2, [exc[1]])
    positive_ldl(Q1)
    positive_ldl(Q2)
    assert int(Q1.det()) == LOCAL_DETS["neg"]
    assert int(Q2.det()) == LOCAL_DETS["pos"]


if __name__ == "__main__":
    check_k7()
    for k in (9, 11, 13, 15, 17):
        check_base(k)
    check_k19_union()
    for k in (21, 23, 25):
        check_large(k)
    print("Exact step-seventeen positive-side certificates passed; k=5 remains open.")
