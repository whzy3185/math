from itertools import combinations
from pathlib import Path
import json
rows=[]
for p,q in [(1,1),(2,1),(1,2),(2,2),(3,2),(3,3)]:
 X=[f'x{i}'for i in range(p)];Y=[f'y{j}'for j in range(q)]
 U=[f'u{i}_{t}'for i in range(p)for t in (0,1)];V=[f'v{j}_{t}'for j in range(q)for t in (0,1)];names=X+Y+U+V+['z'];idx={v:i for i,v in enumerate(names)};N=[1<<i for i in range(len(names))];E=set()
 def edge(u,v):
  a,b=idx[u],idx[v];E.add(tuple(sorted((a,b))));N[a]|=1<<b;N[b]|=1<<a
 for i in range(p):
  for t in (0,1):
   edge(f'x{i}',f'u{i}_{t}');edge('z',f'u{i}_{t}')
   for j in range(q):edge(f'u{i}_{t}',f'v{j}_0')
 for j in range(q):
  edge('z',f'y{j}')
  for t in (0,1):edge(f'y{j}',f'v{j}_{t}')
 allmask=(1<<len(names))-1;count=0;good=[]
 for k in range(p+q+1):
  for S in combinations(range(len(names)),k):
   count+=1;dom=0
   for v in S:dom|=N[v]
   if dom==allmask:good.append(S)
 assert good==[tuple(range(p+q))]
 assert len(E)==2*p*q+4*p+3*q
 rows.append({'p':p,'q':q,'n':len(names),'e':len(E),'gamma':p+q,'unique_minimum':True,'subsets_through_gamma_checked':count,'balanced_attains_sharp_bound':len(E)==(p+q)*(p+q+7)//2})
print(json.dumps(rows,indent=2));Path(__file__).with_name('small_family_results.json').write_text(json.dumps(rows,indent=2))
