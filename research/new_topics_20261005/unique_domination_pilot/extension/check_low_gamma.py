"""Fresh exhaustive equality checks after the audited global reduction.

This tests all graph patterns on the reduced gamma=2 and gamma=3 skeletons.
The existing upper-bound proof is needed to justify coverage of equality graphs.
"""
from itertools import combinations, product
from pathlib import Path
import json

def domsets(n, edges, gamma):
    closed=[1<<v for v in range(n)]
    for u,v in edges:
        closed[u]|=1<<v; closed[v]|=1<<u
    full=(1<<n)-1
    ans=[]
    for k in range(gamma+1):
        for S in combinations(range(n),k):
            covered=0
            for v in S: covered|=closed[v]
            if covered==full: ans.append(S)
    return ans

def run(p):
    # X=0..p-1; y=p; U_i starts at p+1+2i; W is the final 3 vertices.
    gamma=p+1; n=3*gamma+1; y=p
    U=[(p+1+2*i,p+2+2*i) for i in range(p)]
    W=list(range(3*p+1,3*p+4))
    fixed=[(i,u) for i in range(p) for u in U[i]]+[(y,w) for w in W]
    free=[(i,y) for i in range(p)]+[(u,w) for i in range(p) for u in U[i] for w in W]
    D=tuple(range(gamma)); target=gamma*(gamma+7)//2
    top=0; winners=[]; admissible=0; total=1<<len(free)
    # All patterns are generated. Dominating-set checks for subextremal edge
    # counts are unnecessary for the equality certificate.
    tested=0
    for mask in range(total):
        count=len(fixed)+mask.bit_count()
        if count<target: continue
        tested+=1
        edges=fixed+[e for i,e in enumerate(free) if mask>>i&1]
        ds=domsets(n,edges,gamma)
        if ds==[D]:
            admissible+=1; top=max(top,count)
            assert count==target
            omitted=[]
            assert all((i,y) not in edges for i in range(p))
            for i in range(p):
                empty=[w for w in W if all((u,w) not in edges for u in U[i])]
                assert len(empty)==1
                w0=empty[0]
                assert all((u,w) in edges for u in U[i] for w in W if w!=w0)
                omitted.append(w0)
            assert len(set(omitted))==1
            winners.append({'mask':mask,'edges':edges,'omitted_private_column':omitted[0]})
    assert top==target and len(winners)==3
    return {'gamma':gamma,'n':n,'target_edges':target,'fixed_edges':fixed,
            'free_edges_in_bit_order':free,'all_patterns_generated':total,
            'patterns_at_or_above_target_exhaustively_checked':tested,
            'accepted_patterns':winners,'all_are_same_omitted_column':True}

if __name__=='__main__':
    data={'status':'PASS','scope':'Equality candidates after the audited global reduction; not an unrestricted graph census.',
          'cases':[run(1),run(2)]}
    out=Path(__file__).with_name('low_gamma_certificate.json')
    out.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
