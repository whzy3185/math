"""Exact comparison with a previously published graph certificate.

The edge data below are mathematical data transcribed from John Erlbacher's
CC-BY-4.0 public certificate. This checker is newly written and imports no
third-party code.
"""
from itertools import combinations
from pathlib import Path
from hashlib import sha256
import json

HERE = Path(__file__).resolve().parent
PILOT = HERE.parent.parent
SOURCE = ('https://github.com/demonstrandum-research/artifacts/blob/'
          '94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/'
          'problems/p2-factory/kills/koch-narayan/certificate_13_4.json')
E = [(0,6),(1,7),(2,8),(3,8),(4,9),(5,9),
     (0,10),(2,10),(3,10),(4,10),(5,10),
     (1,11),(2,11),(3,11),(4,11),(5,11),
     (0,12),(1,12),(2,12),(3,12),(4,12),(5,12)]
f = {'x0':8,'x1':9,'y0':0,'y1':1,'b00':2,'b01':3,
     'b10':4,'b11':5,'a00':10,'a01':6,'a10':11,'a11':7,'z':12}

def main():
    data = json.loads((PILOT/'candidate13.json').read_text())
    assert set(f)==set(data['labels']) and set(f.values())==set(range(13))
    image = {tuple(sorted((f[a],f[b]))) for a,b in data['edges']}
    assert len(E)==len(set(E))==22 and image==set(E)
    N = [{i} for i in range(13)]
    for a,b in E:
        assert 0<=a<6<=b<13
        N[a].add(b); N[b].add(a)
    assert all(len(s)>1 for s in N)
    counts={}; minimum=None; witness=[]
    for k in range(14):
        c=0
        for S in combinations(range(13),k):
            if len(set().union(*(N[i] for i in S)))==13:
                c+=1
                if minimum is None: minimum=k
                if k==minimum: witness.append(S)
        counts[k]=c
    assert minimum==4 and witness==[(0,1,8,9)]
    r={'status':'PASS','source_url':SOURCE,
       'source_git_blob':'9daa667811f7fc18fc9304c88f81cbf22cf1effe',
       'mapping_from_local_labels_to_prior_integer_labels':f,
       'all_22_edges_match':True,'all_8192_vertex_subsets_tested':True,
       'gamma':minimum,'minimum_dominating_sets':witness,
       'dominating_set_counts':counts,
       'local_certificate_sha256':sha256((PILOT/'candidate13.json').read_bytes()).hexdigest()}
    (HERE/'isomorphism_result.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__':
    main()
