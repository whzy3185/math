from itertools import combinations
import json
from pathlib import Path
# Source Case 1+2 construction with gamma=4, four added C vertices.
labels=['x1','x2','y1','y2','b11','b12','b21','b22','a11','a12','a21','a22','c1','c2','c3','c4']
idx={v:i for i,v in enumerate(labels)}
edges=set()
def add(a,b):edges.add(tuple(sorted((idx[a],idx[b]))))
for i in [1,2]:
 for j in [1,2]:add('x'+str(i),'b'+str(i)+str(j));add('y'+str(i),'a'+str(i)+str(j))
Y=['a11','a12','a21','a22']
for b in ['b11','b21']:
 for a in Y:add(b,a)
for c in ['c1','c2','c3','c4']:
 add(c,'x1')
 for a in Y:add(c,a)
N=[1<<i for i in range(16)]
for i,j in edges:N[i]|=1<<j;N[j]|=1<<i
ans=[]
for k in range(5):
 good=[]
 for S in combinations(range(16),k):
  cover=0
  for i in S:cover|=N[i]
  if cover==65535:good.append(S)
 ans.append({'k':k,'dominating_sets':[list(S) for S in good]})
 if good:break
r={'n':16,'edges':len(edges),'gamma':4,'minimum_sets_by_label':[[labels[i] for i in S] for S in good], 'source_printed_bound':31,'bounds_check':'Literal formula failure; likely indexing typo, not evidence against a repaired extremal conjecture','bipartition':[['x1','x2']+Y,['y1','y2','b11','b12','b21','b22','c1','c2','c3','c4']],'edge_list':[[labels[i],labels[j]] for i,j in sorted(edges)],'exhaustive_sizes_checked':[x['k'] for x in ans]}
p=Path(__file__).parent/'domination_formula_check.json';p.write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
