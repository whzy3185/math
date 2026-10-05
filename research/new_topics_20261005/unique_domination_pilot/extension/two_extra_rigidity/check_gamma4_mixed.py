from itertools import product,combinations
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
X=[0,1];Y=[2,3];U=[(4,5),(6,7)];V=[(8,9),(10,11)];z=12;w=13
fixed=[(X[i],u)for i in range(2)for u in U[i]]+[(Y[j],v)for j in range(2)for v in V[j]]
fixed += [(z,Y[0]),(z,w)]+[(w,x)for x in X]+[(w,v)for pair in V for v in pair]
large=[54,90,108];small=[3,5,6,9,10,17,20,24]
sets=[S for k in range(5)for S in combinations(range(14),k)]
accepted=[];counts={};examples=[]
for masks in product(large,small,large,small):
 edges=list(fixed)
 for i in range(2):
  for j in range(2):
   W=list(V[j])+([z]if j==0 else[])
   free=[(X[i],Y[j])]+[(u,v)for u in U[i]for v in W]
   edges += [e for bit,e in enumerate(free)if masks[2*i+j]>>bit&1]
 assert len(edges)==28 and len({tuple(sorted(e))for e in edges})==28
 N=[1<<v for v in range(14)]
 for a,b in edges:N[a]|=1<<b;N[b]|=1<<a
 dom=[]
 for S in sets:
  cover=0
  for v in S:cover|=N[v]
  if cover==(1<<14)-1:dom.append(S)
 if dom==[(0,1,2,3)]:accepted.append({'masks':masks,'edges':edges})
 else:
  alt=next(S for S in dom if S!=(0,1,2,3));counts[len(alt)]=counts.get(len(alt),0)+1
  examples.append({'masks':masks,'alternative':alt})
r={'candidate_assemblies':576,'accepted_unique':len(accepted),'accepted':accepted,'alternative_sizes':counts,'alternatives':examples,'scope':'All saturated gamma4 mixed-owner opposite-residual candidates after the sharp upper-bound equality reduction.'}
(HERE/'gamma4_mixed_result.json').write_text(json.dumps(r,indent=2)+'\n');print({k:v for k,v in r.items()if k not in ['accepted','alternatives']})
