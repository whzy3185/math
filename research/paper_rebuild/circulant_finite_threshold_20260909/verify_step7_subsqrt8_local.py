#!/usr/bin/env python3
"""Exact certificates for ODD_RESONANCE_STEP7_THRESHOLD.md.

For odd k:
  * checks the two-exception signed-Laplacian decomposition;
  * for k>=9 checks disjoint radius-two local absorbers and their exact
    Sylvester-minor lists;
  * for k=5,7 performs a full exact Sylvester positivity test on K=8I-A^2.

No floating-point branch acceptance is used.
"""

from collections import deque
import numpy as np
import sympy as sp

NEG_TARGET = [
    4,15,41,149,257,514,1661,2238,1522,926,926,926,1852,
    4630,7408,14816,32064,64320,143896,143420,234860,326300,334960,
]
POS_TARGET = [
    1,1,2,5,13,34,89,233,610,1832,5536,16936,52130,95889,
    308833,671461,1296585,3966311,8547891,17810059,
    49673831,56657395,32920956,16015428,
]


def matrix_A(N):
    A = np.zeros((N, N), dtype=np.int64)
    for i in range(N - 1):
        A[i, i + 1] = A[i + 1, i] = 1
    A[N - 1, 0] = A[0, N - 1] = -1
    for i in range(N):
        j = (i + 7) % N
        A[i, j] = A[j, i] = 1 if i % 2 == 0 else -1
    return A


def decomposition(k):
    assert k >= 5 and k % 2 == 1
    N = 7 * k
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
            if d in (1, 7):
                assert abs(val) == 1
                base.append((i, j, -val))
            else:
                exceptional.append((i, j, val))

    a = (N - 7) // 2
    assert exceptional == [(0, N - 4, -2), (a, a + 3, 2)]
    assert len(base) == 2 * N
    return N, M, base, exceptional


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


def exact_local_matrix(edges, exceptional):
    verts = sorted(set(v for e in edges for v in e[:2]) | set(exceptional[:2]))
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
    return Q


def leading_minors(Q):
    return [int(Q[:r, :r].det()) for r in range(1, Q.rows + 1)]


def check_large(k):
    N, M, base, exc = decomposition(k)
    neg, pos = exc
    vn, en = ball_edges(N, base, neg[:2], 2)
    vp, ep = ball_edges(N, base, pos[:2], 2)
    assert len(vn) == 23
    assert len(vp) == 24
    assert {tuple(sorted(e[:2])) for e in en}.isdisjoint(
        {tuple(sorted(e[:2])) for e in ep}
    )
    Qn = exact_local_matrix(en, neg)
    Qp = exact_local_matrix(ep, pos)
    assert leading_minors(Qn) == NEG_TARGET
    assert leading_minors(Qp) == POS_TARGET
    assert all(z > 0 for z in NEG_TARGET + POS_TARGET)


def check_small(k, expected_det):
    N, M, base, exc = decomposition(k)
    Q = sp.Matrix(M.tolist())
    mins = leading_minors(Q)
    assert len(mins) == N
    assert all(z > 0 for z in mins)
    assert mins[-1] == expected_det


if __name__ == "__main__":
    check_small(5, 210822313025982584)
    check_small(7, 4439255509339435940222344)
    for k in range(9, 102, 2):
        check_large(k)
    print("Exact step-seven threshold certificates passed for odd 5<=k<=101.")
