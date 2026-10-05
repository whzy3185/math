"""Read-only independent reconstruction of finite premises in the six-page note.

No primary graph constructor or verifier is imported. The old census is not
re-enumerated; its saved output is tested against the new analytic restrictions.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from collections import Counter
import json
ROOT=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent

def lift(n,edges):
    return 2*n+1, (set(edges) | {tuple(sorted((a,n+b))) for a,b in edges} |
                     {tuple(sorted((b,n+a))) for a,b in edges} |
                     {(n+v,2*n) for v in range(n)})
n,edges=2,{(0,1)}
graphs={2:(n,edges)}
for stage in range(3,7):
    n,edges=lift(n,edges);graphs[stage]=(n,edges)
assert [graphs[s][0] for s in range(2,7)]==[2,5,11,23,47]
assert len(edges)==236
adj=[0]*n
for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
# Exact coloring as printed, starting from the recursively labelled five-cycle.
pairs=[set(I) for I in combinations(range(5),2) if tuple(I) not in graphs[3][1]]
colors=[(I|{10},F(1,5)) for I in pairs]+[(I|{v+5 for v in I},F(3,10)) for I in pairs]+[(set(range(5,10)),F(2,5))]
assert len(colors)==11 and sum(w for I,w in colors)==F(29,10)
assert all(not any(a in I and b in I for a,b in graphs[4][1]) for I,w in colors)
coverage=[sum((w for I,w in colors if v in I),F(0)) for v in range(11)]
assert coverage==[F(1)]*11
# Reconstruct layer identities directly from edges.
X=set(range(11))|set(range(23,34));Y=set(range(11,22))|set(range(34,45));Z={22,45,46}
base={v:v-offset for offset in [0,11,23,34] for v in range(offset,offset+11)}
assert not any(a in Y and b in Y for a,b in edges)
assert not any(a in X and b in {22,45} or b in X and a in {22,45} for a,b in edges)
assert (22,45) not in edges
assert all(tuple(sorted((base[a],base[b]))) in graphs[4][1] for a,b in edges if a in base and b in base)
# Verify the supplied table row-by-row, without executing its generator.
cert=json.loads((ROOT/'mycielski_k5_nine_profiles/witness_alpha_certificate.json').read_text())
vertices=[0,1,2,3,4,5,6,7,11,12,15,19,21,22,26,32,33,41,45,46]
W=sum(1<<v for v in vertices)
assert cert['witness_vertices']==vertices and cert['witness_mask']==W
rows=cert['states']; table=dict(rows)
assert len(rows)==len(table)==190 and table[0]==0 and table[W]==6
for U,value in rows:
    assert U&~W==0
    if U:
        v=(U&-U).bit_length()-1
        a=U^(1<<v);b=a&~adj[v]
        assert a<U and b<U and value==max(table[a],1+table[b])
reachable=set()
def visit(U):
    if U in reachable:return
    reachable.add(U)
    if U:
        v=(U&-U).bit_length()-1;a=U^(1<<v)
        visit(a);visit(a&~adj[v])
visit(W)
assert reachable==set(table)
# Independent branch order: greatest induced degree, breaking ties by label.
@lru_cache(None)
def alternate(U):
    if not U:return 0
    v=max((i for i in range(n) if U>>i&1),key=lambda i:(adj[i]&U).bit_count())
    T=U^(1<<v)
    return max(alternate(T),1+alternate(T&~adj[v]))
assert alternate(W)==6 and alternate.cache_info().currsize==328
six=set(vertices)&Y
assert sorted(six)==cert['independent_six_set'] and len(six)==6
assert not any(a in six and b in six for a,b in edges)
# Both generations are twin-free, as used in the automorphism argument.
for stage in range(3,7):
    order,E=graphs[stage];neigh=[set() for _ in range(order)]
    for a,b in E:neigh[a].add(b);neigh[b].add(a)
    assert len({frozenset(S) for S in neigh})==order
    if stage>=4:
        assert [i for i,S in enumerate(neigh) if len(S)==max(map(len,neigh))]==[order-1]
# Reconcile the new equality restrictions with every old output set.
data=json.loads((ROOT/'mycielski_strengthening/complete_orbits.json').read_text())
seen=set();counts=Counter()
for orbit in data['orbits']:
    members=orbit['orbit'];assert len(set(members))==10
    assert orbit['orbit_size']==10 and orbit['stabilizer_size']==1
    for M in members:
        assert M not in seen;seen.add(M)
        S={v for v in range(n) if M>>v&1}
        assert len(S)==20 and Z<=S and len(S&X)==11 and len(S&Y)==6
        counts[(len(S&set(range(23))),len(S&set(range(23,46))),int(46 in S))]+=1
assert len(data['orbits'])==199 and len(seen)==1990
assert counts=={(13,6,1):1090,(14,5,1):830,(15,4,1):70}
result={'status':'PASS','M6_order':n,'M6_edges':len(edges),'coloring_total':'29/10','coloring_support':11,'supplied_least_label_states':len(table),'independent_max_degree_states':alternate.cache_info().currsize,'witness_alpha':6,'new_equality_restrictions_checked_on_labelled_sets':len(seen),'census_orbits':199,'layer_counts':{'/'.join(map(str,k)):v for k,v in sorted(counts.items())},'scope':'Finite integration replay; universal upper proof reviewed analytically; existing census completeness audit retained, not rerun'}
(OUT/'integration_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
