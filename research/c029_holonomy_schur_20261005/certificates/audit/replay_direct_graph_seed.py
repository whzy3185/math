"""Independent direct-graph finite replay; no repository modules are imported.

This uses sparse scalar Gaussian/Schur elimination on the full signed graph,
rather than the four-site response recurrence used by the analytic verifier.
All computations and acceptance tests use exact rational arithmetic.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def direct_core(n, trailing_blocks=1):
    b = [1, 1, -1, 1, -1, -1, 1, -1]
    adj = [dict() for _ in range(n)]
    for v in range(n):
        for d, sign in ((1, 1), (2, -1 if v == n-1 else b[v % 8])):
            w = (v+d) % n
            adj[v][w] = adj[w][v] = sign
    assert all(len(row) == 4 for row in adj)
    keep = [0, 1] + list(range(n-4*trailing_blocks, n))
    kept_size = len(keep)
    eliminated_size = n-kept_size
    order = list(range(2, n-4*trailing_blocks)) + keep
    pos = {v: i for i, v in enumerate(order)}
    a = [dict() for _ in range(n)]
    for v in range(n):
        row = {v: F(198, 25)}
        for w, c in adj[v].items():
            for u, d in adj[w].items():
                row[u] = row.get(u, F(0)) - c*d
        i = pos[v]
        a[i] = {pos[u]: z for u, z in row.items() if pos[u] >= i and z}
    pivots = []
    for i in range(eliminated_size):
        pivot = a[i].get(i, F(0))
        assert pivot > 0, (n, i, pivot)
        pivots.append(pivot)
        ns = sorted(j for j, value in a[i].items() if j > i and value)
        for jj, j in enumerate(ns):
            left = a[i][j] / pivot
            for k in ns[jj:]:
                value = a[j].get(k, F(0)) - left*a[i][k]
                if value:
                    a[j][k] = value
                else:
                    a[j].pop(k, None)
        a[i].clear()
    core = [[a[min(i,j)].get(max(i,j), F(0))
             for j in range(eliminated_size,n)] for i in range(eliminated_size,n)]
    return core, pivots


def positive(a):
    a = [row[:] for row in a]
    pivots = []
    for i in range(len(a)):
        pivot = a[i][i]
        pivots.append(pivot)
        if pivot <= 0:
            return False, pivots
        for j in range(i+1,len(a)):
            for k in range(j,len(a)):
                a[j][k] = a[k][j] = a[j][k] - a[i][j]*a[i][k]/pivot
    return True, pivots


def run():
    results = {}
    for n in range(50,107,8):
        core, inner_pivots = direct_core(n)
        ok, pivots = positive(core)
        assert ok
        results[str(n)] = {
            'positive': ok,
            'positive_interior_scalar_pivots': len(inner_pivots),
            'positive_core_scalar_pivots': len(pivots),
        }
        if n == 106:
            shifted = [[core[i][j] - (F(1,50) if i == j else 0)
                        for j in range(6)] for i in range(6)]
            margin_ok, margin_pivots = positive(shifted)
            assert margin_ok
            cert = json.loads((Path(__file__).parents[1] / 'analytic/r2_exact_certificate.json').read_text())
            expected = [[F(z) for z in row] for row in cert['certificates']['seed_106_core']]
            assert core == expected
            results[str(n)].update({
                'margin_1over50': margin_ok,
                'equal_to_response_recurrence_core': True,
                'margin_pivots': [str(z) for z in margin_pivots],
            })
    q=F(2,3)
    theta=F(4,9)
    a=F(1,30000)
    b=F(1,2500)
    r=F(1,10**10)
    def bound(h):
        return 24*b*b*q**(2*h)/(1-q*q) + 48*a*q**h + 576*r*theta**h
    assert bound(0) == F(251089,156250000)
    assert bound(0) < F(1,500)
    assert bound(38) < F(1,10**9)
    out = {
        'status': 'PASS',
        'method': 'direct signed graph, exact sparse scalar Schur elimination',
        'finite_graphs': results,
        'tail_B0': str(bound(0)),
        'tail_B0_lt_1over500': True,
        'tail_B38_lt_1over1billion': True,
        'uniform_core_margin': str(F(1,50)-F(2,500)),
    }
    path = Path(__file__).with_name('direct_graph_seed_replay.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'finite_graphs'},indent=2))


if __name__ == '__main__':
    run()
