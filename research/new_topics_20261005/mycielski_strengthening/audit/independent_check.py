"""Independent exact checker for M6 Hall equality classification.
Uses fresh edge-set construction, two MIS algorithms, exact rational duals,
and the independently enumerated representative list. No primary code imports.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations
from collections import Counter
import hashlib,json
HERE=Path(__file__).resolve().parent;SRC=HERE.parent

def myc(n,edges):
    e=set(edges)
    for u,v in edges:e.add(tuple(sorted((u,n+v))));e.add(tuple(sorted((v,n+u))))
    e.update((n+v,2*n) for v in range(n))
    return 2*n+1,e

def adj(n,edges):
    a=[set() for _ in range(n)]
    for u,v in edges:a[u].add(v);a[v].add(u)
    return a

def mask(s):return sum(1<<v for v in s)
def indsets(a):
    out=[]
    def rec(P,I):
        if not P:out.append(frozenset(I));return
        v=min(P);rest=P-{v}
        rec(rest,I);rec(rest-a[v],I|{v})
    rec(set(range(len(a))),set());return out

def maximal(a):
    V=set(range(len(a)));co=[V-{v}-a[v] for v in V];out=[]
    def rec(R,P,X):
        if not P and not X:out.append(mask(R));return
        u=max(P|X,key=lambda v:len(P&co[v]))
        for v in sorted(P-co[u]):
            rec(R|{v},P&co[v],X&co[v]);P.remove(v);X.add(v)
    rec(set(),V,set());return sorted(out)

def closure_mis(a):
    n=len(a);V=set(range(n));IS=indsets(a);N={};ms=[];indcount=len(IS)
    for I in IS:
        nei=set().union(*(a[v] for v in I))
        N[mask(nei)]=nei
        if I|nei==V:ms.append(mask(I)|(1<<(2*n)))
        indcount+=1<<(n-len(nei))
    for U in N.values():
        J={v for v in V if a[v]<=U}
        ms.append(mask(J)|mask({n+v for v in V-U}))
    assert len(ms)==len(set(ms))
    return sorted(ms),len(IS),len(N),len(ms)-len(N),indcount

def rat(a,b):
    assert type(a) is int and type(b) is int and b>0
    return F(a,b)

def run():
    n=2;e={(0,1)};levels=[]
    for j in range(5):
        levels.append((n,set(e),adj(n,e)))
        if j!=4:n,e=myc(n,e)
    assert [z[0] for z in levels]==[2,5,11,23,47]
    a=levels[-1][2];FULL=(1<<47)-1
    assert all(not(a[u]&a[v]) for u,v in e)
    mis=maximal(a)
    generated,i5,d5,m5,i6=closure_mis(levels[-2][2])
    assert mis==generated and (i5,d5,m5,len(mis),i6)==(7407,778,79,857,39473983)
    for I in mis:
        assert all(not(mask(a[v])&I) for v in range(47) if I>>v&1)
        assert all(mask(a[v])&I for v in range(47) if not(I>>v&1))
    known=json.loads((SRC.parent/'mycielski_pilot/m6_candidates.json').read_text())
    assert known['adj']==[mask(x) for x in a] and known['candidate_masks']==mis
    # Check the general compression identity and independence-count formula for
    # all 75 labelled nonempty simple graphs with at most four vertices.
    tested=0
    for n0 in range(1,5):
        pairs=list(combinations(range(n0),2))
        for code in range(1<<len(pairs)):
            E={pair for k,pair in enumerate(pairs) if code>>k&1};A=adj(n0,E)
            m,E2=myc(n0,E);AA=adj(m,E2)
            got,_,_,_,count=closure_mis(A)
            assert got==maximal(AA) and count==len(indsets(AA))
            tested+=1
    assert tested==75
    data=json.loads((SRC/'strengthening_certificates.json').read_text())
    cases={'non20_k3':(3,10,0,0),'non20_k9':(9,30,0,0),'non20_k12':(12,40,0,0),'apex_required':(6,20,0,1<<46)}
    assert set(data['certificates'])==set(cases);stats=Counter();bounds={}
    def tree(node,k,T,O,Z):
        assert O&Z==0 and (O|Z)&~FULL==0
        U=FULL&~(O|Z);kind=node['type'];stats[kind]+=1
        if kind=='split':
            v=node['vertex'];assert type(v) is int and 0<=v<47 and U>>v&1
            tree(node['zero'],k,T,O,Z|1<<v);tree(node['one'],k,T,O|1<<v,Z);return
        # This package contains only split and exact-dual nodes.
        assert kind=='dual'
        coverage={v:F(0) for v in range(47) if U>>v&1};upper=F(O.bit_count());seen=set()
        for row,num,den in node['y']:
            assert type(row) is int and 0<=row<len(mis) and row not in seen;seen.add(row)
            weight=rat(num,den);assert weight>=0
            upper+=weight*(k-(mis[row]&O).bit_count())
            for v in coverage:
                if mis[row]>>v&1:coverage[v]+=weight
        seen=set()
        for v,num,den in node['z']:
            assert v in coverage and v not in seen;seen.add(v)
            weight=rat(num,den);assert weight>=0;coverage[v]+=weight;upper+=weight
        assert all(x>=1 for x in coverage.values())
        assert upper==rat(*node['bound']) and upper<T
    for name,(k,T,O,Z) in cases.items():
        row=data['certificates'][name]
        assert (row['k'],row['forbidden_size'],row['ones'],row['zeros'])==(k,T,O,Z)
        before=sum(stats.values());tree(row['tree'],k,T,O,Z);bounds[name]=sum(stats.values())-before
    assert stats=={'split':9,'dual':13}
    # Derive the group independently by checking all 120 permutations of C5.
    base=levels[1][2];group=[]
    for p in permutations(range(5)):
        if all((v in base[u])==(p[v] in base[p[u]]) for u in range(5) for v in range(5)):
            p=list(p)
            for _ in range(3):
                n0=len(p);p=p+[n0+v for v in p]+[2*n0]
            group.append(p)
    assert len(group)==10
    for n0,_,A in levels[1:]:
        assert len({frozenset(row) for row in A})==n0
        if n0>5:assert len(A[-1])>max(map(len,A[:-1]))
    for p in group:
        assert sorted(p)==list(range(47))
        assert all((v in a[u])==(p[v] in a[p[u]]) for u in range(47) for v in range(47))
    G={tuple(p) for p in group};assert all(tuple(p[q[v]] for v in range(47)) in G for p in group for q in group)
    def image(S,p):return mask(p[v] for v in range(47) if S>>v&1)
    reps=[int(s) for s in (HERE/'independent_representatives.txt').read_text().split()]
    assert reps==sorted(set(reps))
    assert reps==[int(s) for s in (SRC/'complete_orbit_representatives.txt').read_text().split()]
    supplied=json.loads((SRC/'complete_orbits.json').read_text());assert len(supplied['orbits'])==len(reps)==199
    assert {tuple(p) for p in supplied['permutations']}==G
    allW=set();layer=Counter();sizes=Counter();stabilizers=Counter()
    for W,row in zip(reps,supplied['orbits']):
        orbit={image(W,p) for p in group}
        assert W==row['representative']==min(orbit)
        assert sorted(orbit)==row['orbit'] and len(orbit)==row['orbit_size']
        assert allW.isdisjoint(orbit);allW|=orbit
        stab=sum(image(W,p)==W for p in group);assert len(orbit)*stab==10
        assert row['stabilizer_size']==stab and row['apex'] is True
        degrees=Counter((mask(a[v])&W).bit_count() for v in range(47) if W>>v&1)
        assert row['degree_distribution']=={str(k):v for k,v in degrees.items()}
        assert row['edge_count']==sum(k*v for k,v in degrees.items())//2
        for S in orbit:assert S.bit_count()==20 and max((S&I).bit_count() for I in mis)==6
        A=W&((1<<23)-1);B=(W>>23)&((1<<23)-1)
        assert W>>46==1
        assert row['A']==[v for v in range(23) if A>>v&1] and row['B']==[v for v in range(23) if B>>v&1]
        layer[(A.bit_count(),B.bit_count(),1)]+=1;sizes[len(orbit)]+=1;stabilizers[stab]+=1
    assert len(allW)==1990 and layer=={(13,6,1):109,(14,5,1):83,(15,4,1):7}
    assert sizes=={10:199} and stabilizers=={1:199}
    assert supplied['orbit_count']==199 and supplied['labelled_subset_count']==1990
    out={'status':'PASS','independent_sets_M5':i5,'neighborhood_unions_M5':d5,'maximal_independent_sets_M5':m5,'maximal_independent_sets_M6':len(mis),'independent_sets_M6_from_identity':i6,'small_graph_identity_tests':tested,'certificate_node_types':dict(stats),'certificate_nodes_by_case':bounds,'ambient_automorphism_order':10,'representatives':len(reps),'labelled_extremizers':len(allW),'layer_orbit_counts':{str(k):v for k,v in sorted(layer.items())},'orbit_sizes':dict(sizes),'stabilizers':dict(stabilizers),'representatives_sha256':hashlib.sha256((HERE/'independent_representatives.txt').read_bytes()).hexdigest(),'all_1990_subsets_checked_against_all_857_MIS':True,'complete_enumeration':'Independent C++ maximum subset-zeta transform and recursive capacity propagation; its full representative list exactly matches primary output.'}
    (HERE/'independent_check_result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run()
