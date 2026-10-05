"""Bounded exact checks of the analytically reduced delta=2 equality cases.

No graph package, external checker, or numerical solver is used. This is not
an unrestricted graph census: each reduction is stated in RIGIDITY_THEOREM.md.
"""
from itertools import product,combinations,permutations
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent

def normalize(E):return {tuple(sorted(e))for e in E}
def closed(n,E):
    assert len(E)==len(normalize(E))
    N=[1<<v for v in range(n)]
    for u,v in E: N[u]|=1<<v;N[v]|=1<<u
    return N

def ds(n,E,g):
    N=closed(n,E);full=(1<<n)-1;out=[]
    for k in range(g+1):
        for S in combinations(range(n),k):
            cover=0
            for v in S:cover|=N[v]
            if cover==full:out.append(S)
    return out

def dominates(n,E,S):
    N=closed(n,E);cover=0
    for v in S:cover|=N[v]
    return cover==(1<<n)-1

def skeleton(p,q):
    g=p+q;n=3*g+2;X=list(range(p));Y=list(range(p,g))
    U=[(g+2*i,g+2*i+1)for i in range(p)]
    V=[(g+2*p+2*j,g+2*p+2*j+1)for j in range(q)]
    Z=[3*g,3*g+1]
    fixed=[(X[i],u)for i in range(p)for u in U[i]]+[(Y[j],v)for j in range(q)for v in V[j]]
    return g,n,X,Y,U,V,Z,fixed

def twins(p,q):
    g,n,X,Y,U,V,Z,E=skeleton(p,q)
    E += [(u,V[j][0])for pair in U for u in pair for j in range(q)]
    E += [(z,u)for z in Z for pair in U for u in pair]+[(z,y)for z in Z for y in Y]
    return n,E

def check_same(p,q):
    g,n,X,Y,U,V,Z,fixed=skeleton(p,q);D=tuple(range(g));records=[];accepted=[]
    if q==1:
        W=list(V[0])+Z
        fixed += [(Y[0],z)for z in Z]
        patterns=product(range(4),repeat=p)
        for omitted in patterns:
            E=fixed+[(u,w)for i in range(p)for u in U[i]for k,w in enumerate(W)if k!=omitted[i]]
            dom=ds(n,E,g);good=dom==[D]
            assert good==(len(set(omitted))==1)
            if good:
                missing=W[omitted[0]];active=[w for w in W if w!=missing]
                f={v:v for v in range(n)}
                f[missing]=V[0][1];f[active[0]]=V[0][0];f[active[1]]=Z[0];f[active[2]]=Z[1]
                assert normalize([(f[u],f[v])for u,v in E])==normalize(twins(p,q)[1])
                accepted.append({'parameters':omitted,'edges':E,'map_to_twins':f})
            records.append({'parameters':omitted,'unique':good,'alternative':next((s for s in dom if s!=D),None)})
    else:
        fixed += [(z,u)for z in Z for pair in U for u in pair]+[(z,y)for z in Z for y in Y]
        for choices in product(range(2),repeat=p*q):
            E=fixed+[(u,V[j][choices[i*q+j]])for i in range(p)for u in U[i]for j in range(q)]
            dom=ds(n,E,g);good=dom==[D]
            expected=all(len({choices[i*q+j]for i in range(p)})==1 for j in range(q))
            assert good==expected
            if good:
                f={v:v for v in range(n)}
                for j in range(q):
                    if choices[j]:f[V[j][0]],f[V[j][1]]=V[j][1],V[j][0]
                assert normalize([(f[u],f[v])for u,v in E])==normalize(twins(p,q)[1])
                accepted.append({'parameters':choices,'edges':E,'map_to_twins':f})
            records.append({'parameters':choices,'unique':good,'alternative':next((s for s in dom if s!=D),None)})
    return {'p':p,'q':q,'gamma':g,'patterns':len(records),'accepted_count':len(accepted),'accepted':accepted,'records':records}

def canonical_bipartite(n,E):
    """Exact isomorphism code, used only at n=8."""
    assert n==8
    adj=[set()for _ in range(n)]
    for u,v in E:adj[u].add(v);adj[v].add(u)
    color={0:0};todo=[0]
    while todo:
        u=todo.pop()
        for v in adj[u]:
            if v in color:assert color[v]!=color[u]
            else:color[v]=1-color[u];todo.append(v)
    assert len(color)==n
    A=[v for v in range(n)if color[v]==0];B=[v for v in range(n)if color[v]==1]
    if len(A)>len(B):A,B=B,A
    orientations=[(A,B)]+([(B,A)]if len(A)==len(B)else[])
    best=None
    for L,R in orientations:
        for l in permutations(L):
            for r in permutations(R):
                code=sum(1<<(i*len(r)+j)for i,u in enumerate(l)for j,v in enumerate(r)if v in adj[u])
                if best is None or code<best:best=code
    return f'{len(A)}x{len(B)}:{best}'

def check_gamma2():
    U=[2,3,4];V=[5,6,7];fixed=[(0,u)for u in U]+[(1,v)for v in V]
    free=[(0,1)]+[(u,v)for u in U for v in V]
    winners=[]
    for mask in range(1<<10):
        if mask.bit_count()<6:continue
        E=fixed+[e for bit,e in enumerate(free)if mask>>bit&1]
        if ds(8,E,2)==[(0,1)]:
            assert mask.bit_count()==6
            winner={'mask':mask,'edges':E,'canonical':canonical_bipartite(8,E)}
            cross=[e for bit,e in enumerate(free[1:],start=1)if mask>>bit&1]
            rd=[sum(u in e for e in cross)for u in U];cd=[sum(v in e for e in cross)for v in V]
            if mask&1:
                assert sorted(rd)==sorted(cd)==[1,2,2]
                lowu=U[rd.index(1)];lowv=V[cd.index(1)];assert (lowu,lowv)in cross
                assert all((u,v)in cross for u in U if u!=lowu for v in V if v!=lowv)
                winner['type']='F1_center_edge_C4_plus_K2'
            else:
                assert sorted(rd)==[0,3,3]or sorted(cd)==[0,3,3]
                winner['type']='F0_no_center_edge_K23'
            winners.append(winner)
    assert len(winners)==15
    counts={}
    for r in winners:counts[r['canonical']]=counts.get(r['canonical'],0)+1
    assert sorted(counts.values())==[6,9]
    n,E=twins(1,1);assert ds(n,E,2)==[(0,1)]
    code=canonical_bipartite(n,E);assert code not in counts
    types=[]
    for name,edges in [('H2_1_1',E),('F0',fixed+[(u,v)for u in U[:2]for v in V]),('F1',fixed+[(0,1)]+[(u,v)for u in U[:2]for v in V[:2]]+[(U[2],V[2])])]:
        N=closed(8,edges);assert ds(8,edges,2)==[(0,1)]
        types.append({'name':name,'n':8,'edges':edges,'canonical':canonical_bipartite(8,edges),'degree_sequence':sorted(x.bit_count()-1 for x in N),'unique_minimum':[0,1]})
    return {'balanced_optional_patterns':1024,'balanced_maximal_unique_patterns':15,'balanced_orbit_sizes':sorted(counts.values()),'total_isomorphism_classes':3,'types':types,'balanced_winners':winners}

def check_mixed_small():
    out=[]
    for q in [1,2]:
        p=2;g,n,X,Y,U,V,Z,fixed=skeleton(p,q);z,w=Z
        fixed += [(z,Y[0]),(z,w)]+[(w,x)for x in X]+[(w,v)for pair in V for v in pair]
        small=[3,5,6,9,10,17,20,24];large=[54,90,108]
        orders=[large if j==0 else small for i in range(p)for j in range(q)]
        witnesses=[]
        for masks in product(*orders):
            E=list(fixed);active=[]
            for i in range(p):
                for j in range(q):
                    W=list(V[j])+([z]if j==0 else[])
                    free=[(X[i],Y[j])]+[(u,v)for u in U[i]for v in W]
                    chosen=[e for b,e in enumerate(free)if masks[i*q+j]>>b&1];E+=chosen
                    if j==0:active.append({v for v in W if all((u,v)in chosen for u in U[i])})
            common=active[0]&active[1];assert common
            c=min(common);S=tuple(sorted([w,c]+Y[1:]));assert len(S)==g-1 and dominates(n,E,S)
            # Recheck all subsets up to gamma; the explicit smaller witness is the main certificate.
            assert ds(n,E,g)!=[tuple(range(g))]
            witnesses.append({'patterns':masks,'dominating_set':S})
        out.append({'gamma':g,'p':p,'q':q,'saturated_candidates':len(witnesses),'all_have_gamma_minus_one_witness':True,'witnesses':witnesses})
    return out

def check_multi_witnesses():
    out=[]
    for p,q in [(2,2),(2,3),(3,2)]:
        g,n,X,Y,U,V,Z,fixed=skeleton(p,q);z,w=Z
        resid=[(z,y)for y in Y]+[(z,u)for pair in U for u in pair]+[(w,x)for x in X]+[(w,v)for pair in V for v in pair]+[(z,w)]
        deletions=[None]+(list(range(len(resid)))if p==q else[])
        rows=[]
        for deletion in deletions:
            E=fixed+[e for k,e in enumerate(resid)if k!=deletion]
            found=None
            for x in X:
                for y in Y:
                    S=tuple(sorted((set(range(g))-{x,y})|{z,w}))
                    if dominates(n,E,S):found=S;break
                if found:break
            assert found is not None
            rows.append({'missing_edge':None if deletion is None else resid[deletion],'alternative_gamma_set':found})
        out.append({'gamma':g,'p':p,'q':q,'patterns':rows,'scope':'Witness holds already without optional cell edges; adding any such edges preserves it.'})
    return out

if __name__=='__main__':
    same=[check_same(p,q)for p,q in[(1,1),(2,1),(2,2),(3,1),(3,2)]]
    data={'status':'PASS','scope':'Analytically reduced equality patterns, not an unrestricted census; global completeness is proved separately.',
          'same_side':same,'gamma2_exception_catalog':check_gamma2(),'mixed_opposite':check_mixed_small(),'multi_opposite_sparse_witnesses':check_multi_witnesses()}
    (HERE/'rigidity_certificate.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'status':'PASS','same_side_patterns':sum(r['patterns']for r in same),'same_side_accepted':[(r['gamma'],r['p'],r['q'],r['accepted_count'])for r in same],
        'gamma2_isomorphism_classes':3,'mixed_opposite_candidates':[r['saturated_candidates']for r in data['mixed_opposite']]},indent=2))
