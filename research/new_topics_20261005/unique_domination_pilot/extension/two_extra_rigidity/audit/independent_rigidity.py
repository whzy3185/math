"""Independent delta=2 equality audit.
Fresh reduced-pattern generation, exact domination, and unrestricted graph
isomorphism by degree-refined bijection backtracking. No primary imports.
"""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent

def normalized(E):return {tuple(sorted(e)) for e in E}
def adjacency(n,E):
    A=[set() for _ in range(n)]
    for u,v in E:assert u!=v;A[u].add(v);A[v].add(u)
    return A

def dom(S,A):return all(v in S or A[v]&S for v in range(len(A)))
def small_sets(A,g):
    return [tuple(S) for k in range(g+1) for S in combinations(range(len(A)),k) if dom(set(S),A)]

def isomorphism(A,B):
    n=len(A)
    if len(B)!=n or sorted(map(len,A))!=sorted(map(len,B)):return None
    colorsA=list(map(len,A));colorsB=list(map(len,B))
    for _ in range(n):
        sigA=[(colorsA[v],tuple(sorted(colorsA[u] for u in A[v]))) for v in range(n)]
        sigB=[(colorsB[v],tuple(sorted(colorsB[u] for u in B[v]))) for v in range(n)]
        keys={s:i for i,s in enumerate(sorted(set(sigA+sigB)))}
        na=[keys[s] for s in sigA];nb=[keys[s] for s in sigB]
        if Counter(na)!=Counter(nb):return None
        if na==colorsA and nb==colorsB:break
        colorsA,colorsB=na,nb
    mapping={};used=set()
    def visit():
        if len(mapping)==n:return dict(mapping)
        options=[]
        for v in range(n):
            if v in mapping:continue
            candidates=[w for w in range(n) if w not in used and colorsA[v]==colorsB[w] and all((u in A[v])==(wu in B[w]) for u,wu in mapping.items())]
            if not candidates:return None
            options.append((len(candidates),v,candidates))
        _,v,candidates=min(options,key=lambda row:(row[0],-len(A[row[1]]),row[1]))
        for w in candidates:
            mapping[v]=w;used.add(w);result=visit()
            if result is not None:return result
            used.remove(w);del mapping[v]
        return None
    result=visit()
    if result is not None:
        assert sorted(result)==list(range(n)) and sorted(result.values())==list(range(n))
        assert all((v in A[u])==(result[v] in B[result[u]]) for u in range(n) for v in range(n))
    return result

def base(p,q):
    g=p+q;n=3*g+2;X=list(range(p));Y=list(range(p,g))
    U=[list(range(g+2*i,g+2*i+2)) for i in range(p)]
    V=[list(range(g+2*p+2*j,g+2*p+2*j+2)) for j in range(q)]
    Z=[3*g,3*g+1]
    E={(x,u) for x,us in zip(X,U) for u in us}|{(y,v) for y,vs in zip(Y,V) for v in vs}
    return g,n,X,Y,U,V,Z,E

def twins(p,q):
    g,n,X,Y,U,V,Z,E=base(p,q)
    E|={(u,vs[0]) for us in U for u in us for vs in V}
    E|={(z,u) for z in Z for us in U for u in us}|{(z,y) for z in Z for y in Y}
    return adjacency(n,normalized(E))

def local(a,b):
    n=2+a+b;U=list(range(2,2+a));V=list(range(2+a,n));fixed={(0,u) for u in U}|{(1,v) for v in V}
    free=[(0,1)]+[(u,v) for u in U for v in V];valid=[]
    for code in range(1<<len(free)):
        E=fixed|{e for i,e in enumerate(free) if code>>i&1}
        if small_sets(adjacency(n,E),2)==[(0,1)]:valid.append((code,E))
    top=max(code.bit_count() for code,E in valid)
    return [(code,E) for code,E in valid if code.bit_count()==top]

def same_patterns(p,q):
    g,n,X,Y,U,V,Z,E0=base(p,q);target=twins(p,q);records=[];accepted=0
    if q==1:
        W=V[0]+Z;E0|={(Y[0],z) for z in Z};choices=product(range(4),repeat=p)
    else:
        E0|={(z,u) for z in Z for us in U for u in us}|{(z,y) for z in Z for y in Y};choices=product(range(2),repeat=p*q)
    for pattern in choices:
        E=set(E0)
        if q==1:E|={(u,w) for i,us in enumerate(U) for u in us for a,w in enumerate(W) if a!=pattern[i]}
        else:E|={(u,V[j][pattern[i*q+j]]) for i,us in enumerate(U) for u in us for j in range(q)}
        A=adjacency(n,normalized(E));ds=small_sets(A,g);good=ds==[tuple(range(g))]
        predicted=len(set(pattern))==1 if q==1 else all(len({pattern[i*q+j] for i in range(p)})==1 for j in range(q))
        assert good==predicted
        row={'choices':pattern,'unique_minimum':good}
        if good:
            mapping=isomorphism(A,target);assert mapping is not None
            row['full_graph_isomorphism']=mapping;accepted+=1
        else:
            alt=next(S for S in ds if S!=tuple(range(g)));row['alternative']=alt;assert len(alt)<=g
        records.append(row)
    return {'p':p,'q':q,'gamma':g,'patterns':len(records),'accepted':accepted,'records':records}

def mixed(q,small,large):
    p=2;g,n,X,Y,U,V,Z,E0=base(p,q);z,w=Z
    E0|={(z,Y[0]),(z,w)}|{(w,x) for x in X}|{(w,v) for vs in V for v in vs}
    palettes=[large if j==0 else small for i in range(p) for j in range(q)];records=[]
    for selections in product(*palettes):
        E=set(E0)
        for i in range(p):
            for j in range(q):
                code,_=selections[i*q+j];W=V[j]+([z] if j==0 else[])
                options=[(X[i],Y[j])]+[(u,v) for u in U[i] for v in W]
                E|={e for bit,e in enumerate(options) if code>>bit&1}
        E=normalized(E);A=adjacency(n,E);W=set(V[0]+[z]);common=set.intersection(*(W&A[u] for us in U for u in us));assert common
        c=min(common);S={w,c}|set(Y[1:]);assert len(S)==g-1 and dom(S,A)
        ds=small_sets(A,g-1);assert ds
        records.append({'patterns':[x[0] for x in selections],'explicit_smaller_set':sorted(S),'minimum_size':min(map(len,ds))})
    return {'gamma':g,'p':p,'q':q,'patterns':len(records),'all_rejected_by_smaller_set':True,'records':records}

def sparse_residual_checks():
    records=[]
    for p,q in [(2,2),(3,3),(4,4),(2,3),(3,2),(3,4),(4,3)]:
        g,n,X,Y,U,V,Z,E=base(p,q);z,w=Z
        residual={(z,y) for y in Y}|{(z,u) for us in U for u in us}|{(w,x) for x in X}|{(w,v) for vs in V for v in vs}|{(z,w)}
        deletions=[None]+(sorted(residual) if p==q else[])
        for missing in deletions:
            A=adjacency(n,normalized(E|(residual-({missing} if missing else set()))));options=[]
            for x in X:
                for y in Y:
                    S=(set(range(g))-{x,y})|{z,w}
                    if dom(S,A):options.append(sorted(S))
            assert options
            if p!=q:assert len(options)==p*q
            records.append({'p':p,'q':q,'missing_edge':missing,'replacement':options[0]})
    return records

def run():
    start=time.time();raw=json.loads((HERE.parent/'rigidity_certificate.json').read_text())
    small=local(2,2);large=local(2,3);balanced=local(3,3)
    assert len(small)==8 and len(large)==3 and len(balanced)==15
    n=8;fixed={(0,u) for u in [2,3,4]}|{(1,v) for v in [5,6,7]}
    F0=adjacency(n,fixed|{(u,v) for u in [2,3] for v in [5,6,7]})
    F1=adjacency(n,fixed|{(0,1),(4,7)}|{(u,v) for u in [2,3] for v in [5,6]})
    named={'H2':twins(1,1),'F0':F0,'F1':F1}
    assert all(small_sets(A,2)==[(0,1)] for A in named.values())
    assert all(isomorphism(A,B) is None for (a,A),(b,B) in combinations(named.items(),2))
    classifications=Counter();balanced_records=[]
    for code,E in balanced:
        A=adjacency(8,E);matches=[name for name,B in named.items() if isomorphism(A,B) is not None]
        assert len(matches)==1 and matches[0]!='H2';classifications[matches[0]]+=1
        balanced_records.append({'mask':code,'full_graph_class':matches[0]})
    assert classifications=={'F0':6,'F1':9}
    # The independent full private-pair skeleton search from gamma2/3 supplies
    # complete equality graphs, independent of all later star reductions.
    catalog=[];catalog_classes={2:Counter(),3:Counter()}
    for line in (HERE/'boundary_equality_catalog.txt').read_text().splitlines():
        g,same,p,n,code=map(int,line.split());E={pair for bit,pair in enumerate(combinations(range(n),2)) if code>>bit&1};A=adjacency(n,E)
        if g==2:
            names=[name for name,B in named.items() if isomorphism(A,B) is not None];assert len(names)==1;name=names[0]
        else:
            assert isomorphism(A,twins(2,1)) is not None;name='H2(2,1)'
        catalog_classes[g][name]+=1;catalog.append({'gamma':g,'same_side':bool(same),'p':p,'class':name,'edgecode':code})
    assert catalog_classes[2]=={'H2':4,'F0':6,'F1':9} and catalog_classes[3]=={'H2(2,1)':4}
    same=[same_patterns(p,q) for p,q in [(1,1),(2,1),(2,2),(3,1),(3,2)]]
    assert sum(x['patterns'] for x in same)==164 and all(x['accepted']==4 for x in same)
    for record in same:
        old=next(x for x in raw['same_side'] if(x['p'],x['q'])==(record['p'],record['q']))
        assert record['patterns']==old['patterns'] and record['accepted']==old['accepted_count']
        assert [list(x['choices']) for x in record['records']]==[x['parameters'] for x in old['records']]
        assert [x['unique_minimum'] for x in record['records']]==[x['unique'] for x in old['records']]
    mix=[mixed(q,small,large) for q in [1,2]];assert [x['patterns'] for x in mix]==[9,576]
    sparse=sparse_residual_checks();assert len(sparse)==64
    result={'status':'PASS','balanced_gamma2':balanced_records,'balanced_classes':dict(classifications),'complete_small_skeleton_catalog':catalog,'complete_small_skeleton_class_counts':{str(g):dict(c) for g,c in catalog_classes.items()},'same_side':same,'mixed':mix,'sparse_residual_replacements':sparse,'seconds':time.time()-start,'isomorphism_method':'Complete unrestricted graph-vertex bijection search with degree/color refinement and exact adjacency/nonadjacency checks. No fixed centers or prescribed bipartition maps are required.','scope':'Finite reduced checks supplement the general equality proof; no primary code imports.'}
    (HERE/'independent_result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','balanced_patterns':15,'balanced_classes':dict(classifications),'small_catalog_counts':result['complete_small_skeleton_class_counts'],'same_side_patterns':164,'mixed_patterns':[x['patterns'] for x in mix],'residual_witness_checks':len(sparse),'seconds':result['seconds']},indent=2))
if __name__=='__main__':run()
