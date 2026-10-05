"""Exact, bounded checks for the n=3gamma+2 candidate theorem.

No optimization solver or external code is used. Local patterns are exhaustive;
global checks are on explicit families, not a census of all graphs.
"""
from itertools import combinations
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def adjacency(n,edges):
    assert len(edges)==len(set(tuple(sorted(e))for e in edges))
    closed=[1<<v for v in range(n)]
    for u,v in edges:
        assert 0<=u<n and 0<=v<n and u!=v
        closed[u]|=1<<v;closed[v]|=1<<u
    return closed

def small_dominating_sets(n,edges,k):
    closed=adjacency(n,edges);full=(1<<n)-1;ans=[]
    for size in range(k+1):
        for S in combinations(range(n),size):
            covered=0
            for v in S: covered|=closed[v]
            if covered==full: ans.append(list(S))
    return ans

def local(a,b,bound):
    n=2+a+b;U=list(range(2,2+a));V=list(range(2+a,n))
    fixed=[(0,u)for u in U]+[(1,v)for v in V]
    free=[(0,1)]+[(u,v)for u in U for v in V]
    valid=[];rows=[]
    for mask in range(1<<len(free)):
        edges=fixed+[e for i,e in enumerate(free)if mask>>i&1]
        ds=small_dominating_sets(n,edges,2)
        good=ds==[[0,1]]
        if good:
            valid.append(mask);assert mask.bit_count()<=bound
        rows.append({'mask':mask,'unique_centers':good,
                     'alternative':next((s for s in ds if s!=[0,1]),None)})
    maximum=max(m.bit_count()for m in valid);assert maximum==bound
    return {'private_sizes':[a,b],'n':n,'fixed_edges':fixed,'optional_edge_order':free,
            'patterns':len(rows),'admissible_patterns':len(valid),'maximum_optional_edges':maximum,
            'maximal_masks':[m for m in valid if m.bit_count()==maximum],'certificate':rows}

def family(p,q):
    gamma=p+q;n=3*gamma+2
    X=list(range(p));Y=list(range(p,gamma))
    U=[list(range(gamma+2*i,gamma+2*i+2))for i in range(p)]
    V=[list(range(gamma+2*p+2*j,gamma+2*p+2*j+2))for j in range(q)]
    Z=[3*gamma,3*gamma+1]
    edges=[(X[i],u)for i in range(p)for u in U[i]]
    edges += [(Y[j],v)for j in range(q)for v in V[j]]
    edges += [(u,V[j][0])for pair in U for u in pair for j in range(q)]
    edges += [(z,u)for z in Z for pair in U for u in pair]
    edges += [(z,y)for z in Z for y in Y]
    A=set(X+sum(V,[])+Z);B=set(Y+sum(U,[]))
    assert A|B==set(range(n)) and not A&B
    assert all((u in A and v in B)or(u in B and v in A)for u,v in edges)
    closed=adjacency(n,edges);assert all(c!=(1<<i)for i,c in enumerate(closed))
    seen={0};todo=[0]
    while todo:
        v=todo.pop()
        for w in range(n):
            if closed[v]>>w&1 and w not in seen:seen.add(w);todo.append(w)
    assert len(seen)==n
    full=(1<<n)-1;cover=[0]*(1<<n);minimum=n+1;minimum_sets=[];counts=[0]*(n+1)
    for S in range(1<<n):
        if S:
            bit=S&-S;v=bit.bit_length()-1;cover[S]=cover[S^bit]|closed[v]
        if cover[S]==full:
            k=S.bit_count();counts[k]+=1
            if k<minimum:minimum=k;minimum_sets=[S]
            elif k==minimum:minimum_sets.append(S)
    assert minimum==gamma and minimum_sets==[(1<<gamma)-1]
    assert len(edges)==2*p*q+6*p+4*q
    target=(gamma*gamma+1)//2+5*gamma
    assert len(edges)<=target
    return {'p':p,'q':q,'gamma':gamma,'n':n,'edges':edges,'edge_count':len(edges),
            'bipartition_sizes':[len(A),len(B)],'connected':True,'target':target,
            'unique_minimum_set':list(range(gamma)),'all_subsets_checked':1<<n,
            'dominating_set_counts':counts}

def prior_baseline(rec):
    # Mathematical edge data credited to Erlbacher's CC-BY-4.0 certificate.
    prior=[(0,1),(0,2),(0,12),(0,13),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),
           (3,6),(3,7),(4,8),(4,9),(5,10),(5,11),
           (6,12),(6,13),(7,12),(7,13),(8,12),(8,13),
           (9,12),(9,13),(10,12),(10,13),(11,12),(11,13)]
    # Our X=0,1,2; Y=3; U=4..9; V=10,11; Z=12,13.
    f={0:3,1:4,2:5,3:0,4:6,5:7,6:8,7:9,8:10,9:11,10:1,11:2,12:12,13:13}
    assert {tuple(sorted((f[u],f[v])))for u,v in rec['edges']}==set(prior)
    assert small_dominating_sets(14,prior,4)==[[0,3,4,5]]
    return {'source':'https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/certificate_14_4.json',
            'source_blob':'68119109e82801cb23f9edfa42c78c9228ba02f1',
            'all_28_edges_match_H2_3_1':True,'mapping_from_family_indices':f,
            'minimum_dominating_set':[0,3,4,5],
            'scope':'Reproduces the known example; no new exhaustive all-graph census is asserted.'}

if __name__=='__main__':
    cells=[local(2,2,2),local(2,3,4),local(2,4,6),local(3,3,6)]
    (HERE/'local_patterns.json').write_text(json.dumps(cells,indent=2)+'\n')
    families=[family(p,gamma-p)for gamma in range(2,6)for p in range(1,gamma)]
    prior=prior_baseline(next(r for r in families if(r['p'],r['q'])==(3,1)))
    data={'status':'PASS','local_summary':[{k:v for k,v in r.items()if k!='certificate'}for r in cells],
          'families':families,'prior_n14_baseline':prior,
          'scope':'Complete local cells; explicit families through gamma5. General upper bound is a separate written argument.'}
    (HERE/'exact_results.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','local_cases':[(r['private_sizes'],r['maximum_optional_edges'])for r in cells],
          'family_counts':[(r['gamma'],r['p'],r['q'],r['edge_count'])for r in families],
          'prior_n14_example_reproduced':True},indent=2))
