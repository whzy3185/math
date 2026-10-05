from itertools import combinations
from pathlib import Path
import json
out=[]
for r in (2,3):
 names=['x','y']+['u0','u1']+[f'v{j}' for j in range(r)]
 fixed=[('x','u0'),('x','u1')]+[('y',f'v{j}') for j in range(r)]
 free=[('x','y')]+[(f'u{i}',f'v{j}')for i in range(2)for j in range(r)]
 rows=[]
 for mask in range(1<<len(free)):
  E=fixed+[e for i,e in enumerate(free)if mask>>i&1];adj={v:set()for v in names}
  for u,v in E:adj[u].add(v);adj[v].add(u)
  d=[]
  for size in range(3):
   for S in combinations(names,size):
    K=set(S)
    if all(v in K or adj[v]&K for v in names):d.append(list(S))
  unique=d==[['x','y']]
  if unique:assert mask.bit_count()<=2*r-2
  rows.append({'mask':mask,'free_count':mask.bit_count(),'unique_xy':unique,'dominating_sets_of_size_at_most_two':d})
 ok=[row for row in rows if row['unique_xy']]
 rec={'private_sizes':[2,r],'n':len(names),'fixed_edges':fixed,'free_edges_in_bit_order':free,'all_patterns':len(rows),'unique_patterns':len(ok),'max_free_edges':max(row['free_count']for row in ok),'maximal_masks':[row['mask']for row in ok if row['free_count']==2*r-2],'patterns':rows};out.append(rec)
 print({k:v for k,v in rec.items()if k!='patterns'})
p=Path(__file__).parent;(p/'local_cells_certificate.json').write_text(json.dumps(out,indent=2))
