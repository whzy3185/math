#!/usr/bin/env python3
"""Exact integer certificates for ODD_RESONANCE_STEP5_SUBSQRT8.md.

Checks:
  * the all-k two-exception decomposition for odd k;
  * stability and positive Sylvester minors of the 10- and 19-vertex local
    absorbers for odd k>=7;
  * disjointness of the two allocated local edge sets for odd k>=7;
  * the 25 exact leading principal minors for k=5.

No floating-point branch acceptance is used.
"""

from collections import deque
import numpy as np
import sympy as sp


def matrix_A(N):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    for i in range(N):
        j = (i + 5) % N
        A[i, j] = A[j, i] = 1 if i % 2 == 0 else -1
    return A


def decomposition(k):
    assert k >= 3 and k % 2 == 1
    N = 5 * k
    A = matrix_A(N)
    K = 8 * np.eye(N, dtype=np.int64) - A @ A
    p = [(2 * j) % N for j in range(N)]
    M = K[np.ix_(p, p)]

    assert np.all(np.diag(M) == 4)
    base = []
    exceptional = []
    for i in range(N):
        for j in range(i + 1, N):
            val = int(M[i, j])
            if val == 0:
                continue
            d = min((j - i) % N, (i - j) % N)
            if d in (1, 5):
                assert abs(val) == 1
                base.append((i, j, -val))  # signed-Laplacian edge sign sigma
            else:
                exceptional.append((i, j, val))

    a = (N - 5) // 2
    assert exceptional == [(0, N - 3, -2), (a, a + 2, 2)]
    assert len(base) == 2 * N
    return N, M, base, exceptional


def ball_edges(N, base, seeds, radius):
    adj = [[] for _ in range(N)]
    for idx, (i, j, sig) in enumerate(base):
        adj[i].append((j, idx))
        adj[j].append((i, idx))

    dist = {v: 0 for v in seeds}
    q = deque(seeds)
    while q:
        u = q.popleft()
        if dist[u] >= radius:
            continue
        for v, _ in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)

    verts = set(dist)
    edges = [e for e in base if e[0] in verts and e[1] in verts]
    return verts, edges


def exact_local_matrix(edges, exceptional):
    verts = sorted(
        set(v for e in edges for v in e[:2])
        | set(exceptional[:2])
    )
    pos = {v: i for i, v in enumerate(verts)}
    Q = sp.zeros(len(verts))
    for i, j, sig in edges:
        a, b = pos[i], pos[j]
        Q[a, a] += 1
        Q[b, b] += 1
        Q[a, b] -= sig
        Q[b, a] -= sig
    i, j, val = exceptional
    a, b = pos[i], pos[j]
    Q[a, b] += val
    Q[b, a] += val
    return verts, Q


def leading_minors(Q):
    return [int(Q[:r, :r].det()) for r in range(1, Q.rows + 1)]


NEG_TARGET = [4, 11, 18, 13, 13, 21, 36, 27, 18, 12]
POS_TARGET = [
    1, 1, 2, 5, 13, 34, 89, 269, 818, 2521, 5601, 18533,
    41560, 130852, 301184, 929024, 1162752, 732444, 420480,
]
K5_TARGET = [
    4, 16, 60, 225, 840, 3136, 11704, 43681, 163020, 608400,
    2109120, 7311616, 24747008, 83759104, 282174464, 866853120,
    2660537664, 7809976464, 22923102260, 45930833425,
    137043447130, 386860210844, 1086784172626, 2676007398625,
    4179320749384,
]


def check_large(k):
    N, M, base, exc = decomposition(k)
    neg, pos = exc
    vn, en = ball_edges(N, base, neg[:2], 1)
    vp, ep = ball_edges(N, base, pos[:2], 2)

    assert len(vn) == 10
    assert len(vp) == 19
    assert {tuple(sorted(e[:2])) for e in en}.isdisjoint(
        {tuple(sorted(e[:2])) for e in ep}
    )

    _, Qn = exact_local_matrix(en, neg)
    _, Qp = exact_local_matrix(ep, pos)
    assert leading_minors(Qn) == NEG_TARGET
    assert leading_minors(Qp) == POS_TARGET
    assert all(z > 0 for z in NEG_TARGET + POS_TARGET)


def check_k5():
    N, M, base, exc = decomposition(5)
    assert N == 25
    Q = sp.Matrix(M.tolist())
    assert leading_minors(Q) == K5_TARGET
    assert all(z > 0 for z in K5_TARGET)


if __name__ == "__main__":
    check_k5()
    for k in range(7, 102, 2):
        check_large(k)
    print("Exact step-five local/Sylvester certificates passed for odd 5<=k<=101.")
