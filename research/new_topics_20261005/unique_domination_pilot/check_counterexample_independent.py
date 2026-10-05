"""Read-only graph verifier: independent set-based full powerset enumeration."""
from pathlib import Path
from itertools import combinations
import json
p=Path(__file__).parent
r=json.loads((p/'candidate13.json').read_text())
V=set(r['labels']); pairs=[frozenset(e) for e in r['edges']]
assert len(V)==13 and all(len(e)==2 and e<=V for e in pairs)
assert len(set(pairs))==len(pairs)==22
adj={v:set() for v in V}
for e in pairs:
 u,v=tuple(e);adj[u].add(v);adj[v].add(u)
assert all(adj[v] for v in V)
colors={next(iter(V)):0};queue=list(colors)
for u in queue:
 for v in adj[u]:
  if v not in colors:colors[v]=1-colors[u];queue.append(v)
  assert colors[v]!=colors[u]
assert set(colors)==V
counts=[];mins=[]
for k in range(14):
 sets=[]
 for S in combinations(sorted(V),k):
  chosen=set(S)
  if all(v in chosen or bool(adj[v]&chosen) for v in V):sets.append(list(S))
 counts.append(len(sets))
 if sets and not mins:mins=sets;gamma=k
assert gamma==4 and mins==[['x0','x1','y0','y1']]
g=gamma;a=(g+1)//2;b=g//2;tail=max(0,13-3*g-2*a-b+1)
source_bound=2*g+2*a*b+min(13-3*g,2*a-b+1)*(2*a+1)+sum(2*a+1+(i+1)//2 for i in range(1,tail+1))
assert tail==0 and source_bound==21<22
out={'status':'PASS','n':len(V),'e':len(pairs),'connected':True,'bipartite':True,'no_isolated_vertices':True,'gamma':gamma,'minimum_dominating_sets':mins,'all_subsets_checked':sum(__import__('math').comb(13,k) for k in range(14)),'dominating_subset_counts_by_size':counts,'source_bound':source_bound,'source_tail':tail}
(p/'independent_check_result.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
