from pathlib import Path
import json,time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_array
P=Path(__file__).resolve().parent
D=json.loads((P/'m6_candidates.json').read_text());n=len(D['adj']);masks=D['candidate_masks']
C=np.array([[(m>>j)&1 for j in range(n)] for m in masks],dtype=np.float64)
out=[]
for k in range(4,16):
 start=time.monotonic()
 r=milp(-np.ones(n),integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=LinearConstraint(csc_array(C),-np.inf*np.ones(len(masks)),k*np.ones(len(masks))),options={'time_limit':8.0,'mip_rel_gap':0.0})
 row={'k':k,'status':int(r.status),'message':r.message,'elapsed_seconds':time.monotonic()-start}
 if r.x is not None:
  bits=np.rint(r.x).astype(int);mask=sum(int(v)<<i for i,v in enumerate(bits))
  alpha=max((mask&m).bit_count() for m in masks)
  assert alpha<=k
  row.update({'vertices':mask.bit_count(),'alpha_exact_from_complete_MIS':alpha,'witness_mask':mask,'witness_vertices':[i for i in range(n) if (mask>>i)&1],'ratio':mask.bit_count()/alpha,'solver_dual_bound':float(r.mip_dual_bound),'solver_gap':float(r.mip_gap),'solver_nodes':int(r.mip_node_count)})
 out.append(row);(P/'bounded_milp_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
