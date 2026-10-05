"""Independent local-cell and attainment checks for n=3 gamma+2.
Checks domination by intersecting every closed neighborhood, not by the
primary union-cover routine. No primary code imports.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent

def closed(n,edges):
    A=[{v} for v in range(n)]
    for u,v in edges:
        assert u!=v and 0<=u<n and 0<=v<n
        A[u].add(v);A[v].add(u)
    return [sum(1<<u for u in row) for row in A]

def dom(S,neighborhoods):return all(S&C for C in neighborhoods)

def local(a,b,expected):
    n=a+b+2;U=range(2,2+a);V=range(2+a,n)
    fixed={(0,u) for u in U}|{(1,v) for v in V};optional=[(0,1)]+[(u,v) for u in U for v in V]
    good=[];maximum=-1
    tests=[sum(1<<v for v in vs) for size in range(3) for vs in combinations(range(n),size)]
    for code in range(1<<len(optional)):
        edges=fixed|{e for i,e in enumerate(optional) if code>>i&1};N=closed(n,edges)
        ds=[S for S in tests if dom(S,N)]
        old=expected['certificate'][code]
        valid=ds==[3]
        assert old['mask']==code and old['unique_centers']==valid
        if old['alternative'] is not None:
            alt=sum(1<<v for v in old['alternative']);assert alt!=3 and alt in ds
        else:assert valid
        if valid:good.append(code);maximum=max(maximum,code.bit_count())
    winners=[m for m in good if m.bit_count()==maximum]
    assert len(good)==expected['admissible_patterns'] and maximum==expected['maximum_optional_edges'] and winners==expected['maximal_masks']
    return {'a':a,'b':b,'patterns':1<<len(optional),'admissible':len(good),'maximum_optional':maximum,'maximal_masks':winners}

def family(p,q):
    gamma=p+q;n=3*gamma+2
    X=set(range(p));Y=set(range(p,gamma));Z={3*gamma,3*gamma+1}
    U=[{gamma+2*i,gamma+2*i+1} for i in range(p)]
    V=[{gamma+2*p+2*j,gamma+2*p+2*j+1} for j in range(q)]
    Uall=set().union(*U);active={min(vs) for vs in V};Vall=set().union(*V)
    L=X|Vall|Z;R=Y|Uall
    edges=set()
    for u in L:
        for v in R:
            okay=(u in X and v in U[u]) or (u in Vall and v in Y and u in V[v-p]) or (u in active and v in Uall) or (u in Z and v in Uall|Y)
            if okay:edges.add(tuple(sorted((u,v))))
    assert L|R==set(range(n)) and not L&R
    N=closed(n,edges);assert all(mask!=(1<<v) for v,mask in enumerate(N))
    seen={0};todo=[0]
    while todo:
        v=todo.pop()
        for w in range(n):
            if N[v]>>w&1 and w not in seen:seen.add(w);todo.append(w)
    assert len(seen)==n
    counts=Counter();minimum=n+1;winners=[]
    for S in range(1<<n):
        if dom(S,N):
            size=S.bit_count();counts[size]+=1
            if size<minimum:minimum=size;winners=[S]
            elif size==minimum:winners.append(S)
    assert minimum==gamma and winners==[(1<<gamma)-1]
    assert len(edges)==2*p*q+6*p+4*q
    return {'p':p,'q':q,'gamma':gamma,'n':n,'edges':sorted(edges),'edge_count':len(edges),'bipartition_sizes':[len(L),len(R)],'minimum':minimum,'minimum_masks':winners,'dominating_set_counts':[counts[i] for i in range(n+1)],'all_subsets_checked':1<<n}

def run():
    start=time.time();raw=json.loads((HERE.parent/'local_patterns.json').read_text());old=json.loads((HERE.parent/'exact_results.json').read_text())
    locals=[]
    for a,b in [(2,2),(2,3),(2,4),(3,3)]:locals.append(local(a,b,next(r for r in raw if r['private_sizes']==[a,b])))
    families=[]
    for gamma in range(2,6):
        for p in range(1,gamma):
            r=family(p,gamma-p);s=next(v for v in old['families'] if (v['p'],v['q'])==(p,gamma-p))
            assert r['edges']==sorted(tuple(sorted(e)) for e in s['edges'])
            for name in ['edge_count','bipartition_sizes','dominating_set_counts','all_subsets_checked']:assert r[name]==s[name]
            families.append(r)
    assert sum(r['patterns'] for r in locals)==1696
    assert len(families)==10
    assert next(r for r in families if(r['p'],r['q'])==(2,2))['bipartition_sizes']==[8,6]
    assert next(r for r in families if(r['p'],r['q'])==(3,1))['bipartition_sizes']==[7,7]
    # Direct construction must meet the sharp formula at every small balanced pair.
    for gamma in range(2,6):
        r=next(r for r in families if(r['p'],r['q'])==((gamma+1)//2,gamma//2))
        assert r['edge_count']==(gamma*gamma+1)//2+5*gamma
    # Validate the stored prior-graph isomorphism against the explicitly quoted edge data.
    prior={(0,1),(0,2),(0,12),(0,13),(1,6),(1,7),(1,8),(1,9),(1,10),(1,11),(3,6),(3,7),(4,8),(4,9),(5,10),(5,11),(6,12),(6,13),(7,12),(7,13),(8,12),(8,13),(9,12),(9,13),(10,12),(10,13),(11,12),(11,13)}
    f={int(k):v for k,v in old['prior_n14_baseline']['mapping_from_family_indices'].items()}
    r=next(r for r in families if(r['p'],r['q'])==(3,1))
    assert sorted(f)==list(range(14)) and sorted(f.values())==list(range(14))
    assert {tuple(sorted((f[u],f[v]))) for u,v in r['edges']}==prior
    N=closed(14,prior);ds=[S for S in range(1<<14) if S.bit_count()<=4 and dom(S,N)]
    assert ds==[sum(1<<v for v in [0,3,4,5])]
    out={'status':'PASS','local_cells':locals,'family_count':10,'families':families,'prior_n14_edge_map_and_unique_set':True,'seconds':time.time()-start,'method':'Fresh edge reconstruction and closed-neighborhood intersection tests. Every local pattern, every subset in each H2 graph, and stored metadata checked without importing primary code.'}
    (HERE/'independent_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'local_patterns':1696,'local_summary':locals,'families':[(r['p'],r['q'],r['edge_count']) for r in families],'seconds':out['seconds']},indent=2))
if __name__=='__main__':run()
