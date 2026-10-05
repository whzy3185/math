"""Exact independent verification of Mycielski recurrences and MIS compression."""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json
from explore_counts import myc, independent_sets, candidates
P=Path(__file__).resolve().parent

def alpha_function(adj):
 @lru_cache(None)
 def alpha(S):
  if not S:return 0
  b=S&-S;v=b.bit_length()-1;T=S^b
  return max(alpha(T),1+alpha(T&~adj[v]))
 return alpha

def maximal_independent_bk(adj):
 n=len(adj);full=(1<<n)-1;comp=[full&~(a|(1<<i)) for i,a in enumerate(adj)];out=[]
 def bk(R,P,X):
  if not P and not X:out.append(R);return
  PX=P|X
  if PX:
   vs=[i for i in range(n) if PX>>i&1];u=max(vs,key=lambda i:(P&comp[i]).bit_count());ext=P&~comp[u]
  else:ext=P
  while ext:
   b=ext&-ext;ext^=b;v=b.bit_length()-1
   bk(R|b,P&comp[v],X&comp[v]);P^=b;X|=b
 bk(0,full,0)
 return sorted(out)

cases=0
for n in range(1,5):
 edges=[(i,j) for i in range(n) for j in range(i)]
 for e in range(1<<len(edges)):
  adj=[0]*n
  for j,(a,b) in enumerate(edges):
   if e>>j&1:adj[a]|=1<<b;adj[b]|=1<<a
  new=myc(adj);ag=alpha_function(adj);am=alpha_function(new);ind=list(independent_sets(adj));full=(1<<n)-1
  assert candidates(adj)[1]==maximal_independent_bk(new)
  neighborhoods={}
  for I in ind:
   N=0
   for v in range(n):
    if I>>v&1:N|=adj[v]
   neighborhoods[I]=N
  for S in range(1<<len(new)):
   A=S&full;B=(S>>n)&full;eps=(S>>(2*n))&1
   F=max(I.bit_count()+(B&~neighborhoods[I]).bit_count() for I in ind if I&~A==0)
   assert am(S)==max(F,eps+ag(A))
   cases+=1
D=json.loads((P/'m6_candidates.json').read_text())
mis=maximal_independent_bk(D['adj'])
assert mis==D['candidate_masks']
for I in mis:
 assert all(not(D['adj'][v]&I) for v in range(47) if I>>v&1)
 assert all(D['adj'][v]&I for v in range(47) if not(I>>v&1))
report={'induced_subsets_checked':cases,'graph_scope':'All simple graphs on 1,2,3,4 vertices, every induced subset of their Mycielskians','m6_mis_count':len(mis),'independent_bron_kerbosch_match':True,'m6_mis_size_distribution':dict(sorted(Counter(I.bit_count() for I in mis).items()))}
if (P/'bounded_milp_results.json').exists():
 rows=json.loads((P/'bounded_milp_results.json').read_text());checked=[]
 for row in rows:
  if 'witness_mask' not in row:continue
  W=row['witness_mask'];a=max((W&I).bit_count() for I in mis)
  assert a==row['alpha_exact_from_complete_MIS']
  checked.append({'k':row['k'],'vertices':W.bit_count(),'alpha':a,'mask':W})
 report['witnesses_checked']=checked
(P/'structural_verification.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
