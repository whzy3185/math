from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
D=json.loads((Path(__file__).resolve().parent/'m6_candidates.json').read_text());ms=D['candidate_masks'];n=len(D['adj']);C=np.array([[(m>>i)&1 for i in range(n)] for m in ms],float)
for k in range(1,16):
 r=linprog(-np.ones(n),A_ub=C,b_ub=k*np.ones(len(ms)),bounds=(0,1),method='highs')
 print(k,-r.fun,'fractional',sum((r.x>1e-8)&(r.x<1-1e-8)),flush=True)
