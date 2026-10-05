"""Exact checks for the row-modification obstruction and template arithmetic.

The all-graph stability estimate remains an analytic theorem, not a deduction
from this bounded construction check.
"""
from itertools import product, combinations
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent

def template(p,q):
    g=p+q;n=3*g+1;z=3*g
    X=list(range(p));Y=list(range(p,g))
    # Vertices of each center/private triple use consecutive indices.
    fixed=[(3*i,3*i+j)for i in range(g)for j in(1,2)]
    E=set(tuple(sorted(e))for e in fixed)
    E.update(tuple(sorted((3*i+j,3*h+1)))for i in X for j in(1,2)for h in Y)
    E.update(tuple(sorted((z,3*i+j)))for i in X for j in(1,2))
    E.update(tuple(sorted((z,3*h)))for h in Y)
    return n,E

def neighborhoods(n,E):
    N=[{v}for v in range(n)]
    for u,v in E:
        assert 0<=u<v<n
        N[u].add(v);N[v].add(u)
    return N

def connected(N):
    seen={0};todo=[0]
    while todo:
        u=todo.pop()
        for v in N[u]-seen:seen.add(v);todo.append(v)
    return len(seen)==len(N)

def modification(k,s):
    n,H=template(k,k);g=2*k;z=3*g;E=set(H)
    for i in range(s):
        for h in range(k,2*k):
            E.remove(tuple(sorted((3*i+1,3*h+1))))
            E.add(tuple(sorted((3*i,3*h))))
        E.remove(tuple(sorted((z,3*i+1))))
    assert len(E)==g*(g+7)//2-s
    N=neighborhoods(n,E);NH=neighborhoods(n,H)
    assert all(len(a)>1 for a in N) and connected(N)
    A={3*i for i in range(k)}|{3*h+j for h in range(k,2*k)for j in(1,2)}|{z}
    B=set(range(n))-A
    assert all((u in A)!=(v in A)for u,v in E)
    forced=[]
    for i in range(k):
        v=3*i+1 if i<s else 3*i
        expected={3*i,3*i+1}if i<s else {3*i,3*i+1,3*i+2}
        assert N[v]==expected;forced.append(sorted(expected))
    for h in range(k,2*k):
        assert N[3*h+2]=={3*h,3*h+2};forced.append([3*h,3*h+2])
    assert len(forced)==g and sum(map(len,forced))==len(set().union(*map(set,forced)))
    # The verified disjoint closed neighborhoods prove every dominating set
    # has >=gamma vertices, and every gamma-set chooses one from each.
    solutions=[];candidates=0
    for S in product(*forced):
        candidates+=1
        if len(set().union(*(N[v]for v in S)))==n:solutions.append(sorted(S))
    D=[3*i for i in range(g)];assert solutions==[D]
    # Additional unrestricted check on the smallest orders.
    unrestricted=None
    if k<=3:
        masks=[sum(1<<v for v in a)for a in N];full=(1<<n)-1;all_solutions=[];unrestricted=0
        for size in range(g+1):
            for S in combinations(range(n),size):
                unrestricted+=1;covered=0
                for v in S:covered|=masks[v]
                if covered==full:all_solutions.append(list(S))
        assert all_solutions==[D]
    degrees=sorted(len(a)-1 for a in N);target=sorted(len(a)-1 for a in NH)
    expected=sorted([1]*(k+s)+[2]*(k-s)+[3+s]*k+[k+2]*(2*k)+[2*k+1-s]*k+[3*k-s])
    assert degrees==expected
    l1=sum(abs(a-b)for a,b in zip(degrees,target));assert l1==2*s*(k+1)
    identity=len(E^H);assert identity==s*(2*k+1)
    return {'k':k,'s':s,'gamma':g,'n':n,'edge_count':len(E),'edge_deficit':s,
            'connected':True,'bipartite':True,'no_isolates':True,'unique_minimum_set':D,
            'closed_neighborhood_product_candidates':candidates,
            'additional_unrestricted_subsets_checked':unrestricted,
            'degree_sequence':degrees,'target_degree_sequence':target,'sorted_degree_L1':l1,
            'unlabelled_edit_lower_bound':l1//2,'identity_edit_upper_bound':identity,
            'edges':sorted(E)}

def check_templates():
    count=0;maximum_ratio=0
    for g in range(2,41):
        a=(g+1)//2;b=g//2;n,target=template(a,b)
        for p in range(g):
            q=g-p;d=p-q;B=d*(d-1)//2;h=abs(p-a)
            assert h*h<=B
            _,E=template(p,q);actual=len(E^target)
            assert actual==h*(2*g-2*h+3)
            assert actual<=h*(2*g-2*h+11)
            count+=1
        tmin=(g-2)//2
        if g>=4:assert g+7<=12*tmin
    return {'gamma_range':[2,40],'all_p_with_q_positive':count,
            'imbalance_and_single_owner_inequalities':True,
            'template_identity_distance':'h(2gamma-2h+3)',
            'proof_degree_sum_upper_bound_verified':True}

if __name__=='__main__':
    cases=[modification(k,s)for k in range(2,7)for s in range(1,k)]
    out={'status':'PASS','scope':'Explicit obstruction families and balancing-template arithmetic; not an all-graph computation.',
         'obstruction_cases':cases,'template_arithmetic':check_templates()}
    (HERE/'exact_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'PASS','family_parameters':[(r['k'],r['s'])for r in cases],
                     'unrestricted_small_subset_checks':sum(r['additional_unrestricted_subsets_checked']or 0 for r in cases),
                     'template_arithmetic':out['template_arithmetic']},indent=2))
