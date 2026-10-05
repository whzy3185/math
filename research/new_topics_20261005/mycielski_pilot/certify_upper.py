"""Build independently checkable rational LP / binary split certificates."""
from pathlib import Path
from fractions import Fraction as F
import json,time,math
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
D=json.loads((P/'m6_candidates.json').read_text());MASKS=D['candidate_masks'];N=len(D['adj']);ALL=(1<<N)-1
C=np.array([[(m>>i)&1 for i in range(N)] for m in MASKS],float)
START=time.monotonic();nodes=0

def encode(f): return [f.numerator,f.denominator]

def bound_certificate(k,ones,zeros):
 global nodes
 nodes+=1
 assert nodes<=10000 and time.monotonic()-START<90,'Bounded pilot limit reached'
 U=ALL&~(ones|zeros);free=[v for v in range(N) if U>>v&1]
 rhs=[k-(m&ones).bit_count() for m in MASKS]
 for j,b in enumerate(rhs):
  if b<0:return {'type':'conflict','row':j},None
 if not free:return {'type':'trivial','bound':ones.bit_count()},None
 r=linprog(-np.ones(len(free)),A_ub=C[:,free],b_ub=np.array(rhs,float),bounds=(0,1),method='highs')
 assert r.success,r.message
 y={j:F(float(-v)).limit_denominator(1000000) for j,v in enumerate(r.ineqlin.marginals) if v< -1e-9}
 # Correct tiny dual rounding errors with nonnegative bound multipliers.
 z={}
 for v in free:
  covered=sum((a for j,a in y.items() if MASKS[j]>>v&1),F(0))
  extra=max(F(0),1-covered)
  if extra:z[v]=extra
 bound=F(ones.bit_count())+sum((a*rhs[j] for j,a in y.items()),F(0))+sum(z.values(),F(0))
 cert={'type':'dual','y':[[j,*encode(a)] for j,a in y.items()],'z':[[v,*encode(a)] for v,a in z.items()],'bound':encode(bound)}
 return cert,(r.x,free,bound)

def tree(k,target,ones=0,zeros=0):
 cert,extra=bound_certificate(k,ones,zeros)
 if extra is None:
  assert cert['type']=='conflict' or cert['bound']<target
  return cert
 x,free,bound=extra
 if bound<target:return cert
 fractional=[(min(float(v),1-float(v)),i) for i,v in enumerate(x) if 1e-7<v<1-1e-7]
 assert fractional,('Unexcluded integer point',k,target,bound)
 _,j=max(fractional);v=free[j]
 return {'type':'split','vertex':v,'zero':tree(k,target,ones,zeros|(1<<v)),'one':tree(k,target,ones|(1<<v),zeros)}

out={'graph':'M6 with recursive original/clone/apex labeling','target_hall_ratio':[10,3],'certificates':{}}
for k in [1,3,4,5,6,7,8,9,10,11,12,13,14]:
 target=(10*k)//3+1
 before=nodes
 out['certificates'][str(k)]={'forbidden_size':target,'tree':tree(k,target)}
 print('k',k,'nodes',nodes-before,'total',nodes,'elapsed',time.monotonic()-START,flush=True)
 (P/'upper_certificates.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print('COMPLETE nodes',nodes,'elapsed',time.monotonic()-START)
