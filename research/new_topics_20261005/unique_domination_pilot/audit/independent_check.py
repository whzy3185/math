"""Independent finite checks for the n=3gamma+1 unique-domination result.

Uses adjacency bitsets and closed-neighborhood unions, rather than the primary
local checker. Imports no primary verification code or optimization package.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent


def graph(n,edges):
    adj=[0]*n
    assert len(edges)==len(set(tuple(sorted(e)) for e in edges))
    for u,v in edges:
        assert 0<=u<n and 0<=v<n and u!=v
        adj[u]|=1<<v
        adj[v]|=1<<u
    return adj


def dominating_masks(adj,limit):
    n=len(adj);full=(1<<n)-1
    closed=[a|(1<<i) for i,a in enumerate(adj)]
    for size in range(limit+1):
        for vertices in combinations(range(n),size):
            covered=0;chosen=0
            for v in vertices:
                covered|=closed[v];chosen|=1<<v
            if covered==full:
                yield chosen


def check_cells():
    supplied=json.loads((SOURCE/'local_cells_certificate.json').read_text())
    result=[]
    valid_max={}
    for r in (2,3):
        # x=0, y=1, U={2,3}, V={4,...,3+r}.
        n=4+r
        fixed=[(0,2),(0,3)]+[(1,v) for v in range(4,n)]
        free=[(0,1)]+[(u,v) for u in (2,3) for v in range(4,n)]
        valid=[];rows=[]
        for choice in range(1<<len(free)):
            edges=fixed+[e for i,e in enumerate(free) if choice>>i&1]
            dom=list(dominating_masks(graph(n,edges),2))
            unique=dom==[3]
            if unique:
                valid.append(choice)
                assert choice.bit_count()<=2*r-2
            rows.append({'mask':choice,'unique_xy':unique,'dominating_masks_at_most_two':dom})
        primary=next(rec for rec in supplied if rec['private_sizes']==[2,r])
        assert len(rows)==primary['all_patterns']
        labels=['x','y','u0','u1']+[f'v{j}' for j in range(r)]
        for row,other in zip(rows,primary['patterns']):
            assert row['mask']==other['mask']
            assert row['unique_xy']==other['unique_xy']
            other_masks=[sum(1<<labels.index(v) for v in ds) for ds in other['dominating_sets_of_size_at_most_two']]
            assert row['dominating_masks_at_most_two']==other_masks
        maximum=max(c.bit_count() for c in valid)
        maximizers=[c for c in valid if c.bit_count()==maximum]
        assert maximum==2*r-2
        assert len(valid)==(14 if r==2 else 58)
        assert maximizers==primary['maximal_masks']
        valid_max[r]=maximizers
        result.append({'private_sizes':[2,r],'patterns':len(rows),'valid_unique_patterns':len(valid),
                       'max_free_edges':maximum,'maximizing_masks':maximizers,
                       'all_domination_lists_match_primary_certificate':True})
    return result,valid_max


def h_family(p,q):
    # X followed by Y, then paired U vertices, paired V vertices, and z.
    gamma=p+q
    x=list(range(p));y=list(range(p,gamma))
    U=[(gamma+2*i,gamma+2*i+1) for i in range(p)]
    V=[(gamma+2*p+2*j,gamma+2*p+2*j+1) for j in range(q)]
    z=3*gamma
    edges=[]
    for i in range(p):
        edges.extend((x[i],u) for u in U[i])
        edges.extend((z,u) for u in U[i])
    for j in range(q):
        edges.extend((y[j],v) for v in V[j])
        edges.append((z,y[j]))
        edges.extend((u,V[j][0]) for pair in U for u in pair)
    return graph(z+1,edges),edges


def check_saved_counterexample():
    data=json.loads((SOURCE/'candidate13.json').read_text())
    labels=data['labels'];n=len(labels)
    edges=[(labels.index(u),labels.index(v)) for u,v in data['edges']]
    adj=graph(n,edges)
    full=(1<<n)-1
    assert n==13 and len(edges)==22
    assert all(adj)
    color={0:0};queue=[0]
    while queue:
        v=queue.pop()
        for w in range(n):
            if adj[v]>>w&1:
                if w in color:
                    assert color[w]!=color[v]
                else:
                    color[w]=1-color[v];queue.append(w)
    assert len(color)==n
    # Check all 2^13 subsets, including every larger set, independently.
    closed=[a|(1<<i) for i,a in enumerate(adj)]
    coverage=[0]*(1<<n)
    counts=Counter();min_masks=[];minimum=n+1
    for S in range(1<<n):
        if S:
            bit=S&-S;v=bit.bit_length()-1
            coverage[S]=coverage[S^bit]|closed[v]
        if coverage[S]==full:
            size=S.bit_count();counts[size]+=1
            if size<minimum:
                minimum=size;min_masks=[S]
            elif size==minimum:
                min_masks.append(S)
    assert minimum==4 and len(min_masks)==1
    expected=sum(1<<labels.index(v) for v in ['x0','x1','y0','y1'])
    assert min_masks==[expected]
    return {'n':n,'edges':len(edges),'simple':True,'connected':True,'bipartite':True,
            'all_subsets_checked':1<<n,'gamma':minimum,'number_of_minimum_dominating_sets':1,
            'minimum_dominating_set':[labels[i] for i in range(n) if expected>>i&1],
            'dominating_set_size_distribution':dict(sorted(counts.items()))}


def check_gamma4_equality(valid_cells):
    # Independently enumerate all saturated local-pattern candidates at p=q=2.
    p=q=2;gamma=4;n=13;z=12
    X=[0,1];Y=[2,3];U=[(4,5),(6,7)];V=[(8,9),(10,11)]
    fixed=[]
    for i in range(p):
        fixed.extend((X[i],u) for u in U[i])
        fixed.extend((z,u) for u in U[i])
    for j in range(q):
        fixed.extend((Y[j],v) for v in V[j])
        fixed.append((z,Y[j]))
    accepted=[]
    for patterns in product(valid_cells,repeat=p*q):
        edges=list(fixed)
        for index,(i,j) in enumerate(product(range(p),range(q))):
            free=[(X[i],Y[j])]+[(u,v) for u in U[i] for v in V[j]]
            edges.extend(e for bit,e in enumerate(free) if patterns[index]>>bit&1)
        assert len(edges)==22
        adj=graph(n,edges)
        alternative=False
        for S in dominating_masks(adj,gamma):
            if S!=15:
                alternative=True;break
        if not alternative:
            accepted.append(patterns)
    expected=[]
    # Six-cell column stars have masks 10 (V0) and 20 (V1).
    for choices in product((10,20),repeat=q):
        expected.append(tuple(choices)*p)
    assert sorted(accepted)==sorted(expected)
    return {'gamma':4,'saturated_local_candidates_checked':len(valid_cells)**(p*q),
            'unique_minimum_candidates':len(accepted),'accepted_cell_patterns':[list(v) for v in accepted],
            'all_are_consistent_column_star_family':True}


def run():
    cells,max_cells=check_cells()
    counter=check_saved_counterexample()
    family=[]
    for gamma in range(2,7):
        p=(gamma+1)//2;q=gamma//2
        adj,edges=h_family(p,q)
        dom=list(dominating_masks(adj,gamma))
        assert dom==[(1<<gamma)-1]
        assert len(edges)==gamma*(gamma+7)//2
        family.append({'gamma':gamma,'p':p,'q':q,'n':len(adj),'edges':len(edges),'unique_minimum_verified':True})
    equality=check_gamma4_equality(max_cells[2])
    result={'status':'PASS','local_cells':cells,'counterexample':counter,'balanced_family_checks':family,
            'gamma4_equality_replay':equality,
            'source_bound_n13_gamma4':21,'exact_counterexample_edges':22,
            'input_sha256':{name:sha256((SOURCE/name).read_bytes()).hexdigest() for name in ['candidate13.json','local_cells_certificate.json']},
            'scope':'Finite checks supplement the separately audited all-gamma mathematical proof; no novelty assertion'}
    (HERE/'independent_check_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    run()
