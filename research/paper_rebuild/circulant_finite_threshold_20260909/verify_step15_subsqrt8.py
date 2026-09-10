#!/usr/bin/env python3
"""Exact certificates for ODD_RESONANCE_STEP15_NEAR_CLASSIFICATION.md.

All acceptance is exact rational LDL.  Floating point is not used.
"""
from collections import deque
import numpy as np
import sympy as sp

SMALL_DETS = {
    9: 29245809126400346085098954358334266552911234352814393414526937002488,
    11: 81345420562709807947141505074935918169325573548550037178098091486387968952830846792,
    13: 162521835310602873945303957432859962422579081241254071361556594492099339038312172488240807040047224,
    15: 293804017270487835611162286466320538777943101838852071037075676365802812233712833302287545180173427118677957140744,
    17: 510683970816354646530633036895217853290955435153117124541465070106856490524072524819498061323926375744552520079062894287446875000,
    19: 872488811110783040085698329295180035174154225756377199094999455714249783071274359877825226852699703364096334509183149674930571596815483736822600,
}
K7_DET = 1849301460651035605088456882195255546256126182948864
LOCAL_DETS = {
    "neg": 3778167212446958262349168881634331311931392,
    "pos": 105402599868300324129777428804783514283081728,
}


def matrix_A(k, modified_k7=False):
    N = 15*k
    A = np.zeros((N,N), dtype=np.int64)
    for i in range(N-1):
        A[i,i+1]=A[i+1,i]=1
    A[N-1,0]=A[0,N-1]=-1
    tau=[1 if i%2==0 else -1 for i in range(N)]
    if modified_k7:
        assert k==7
        tau[86]*=-1; tau[87]*=-1
    for i,sig in enumerate(tau):
        j=(i+15)%N
        A[i,j]=A[j,i]=sig
    return A


def positive_ldl(Q):
    _,D=Q.LDLdecomposition(hermitian=False)
    piv=[sp.factor(D[i,i]) for i in range(D.rows)]
    assert all(p>0 for p in piv)
    return piv


def decomposition(k):
    N=15*k
    A=matrix_A(k)
    K=8*np.eye(N,dtype=np.int64)-A@A
    p=[(2*j)%N for j in range(N)]
    M=K[np.ix_(p,p)]
    base=[]; exc=[]
    for i in range(N):
        for j in range(i+1,N):
            val=int(M[i,j])
            if val==0: continue
            d=min((j-i)%N,(i-j)%N)
            if d in (1,15):
                assert abs(val)==1
                base.append((i,j,-val))
            else:
                exc.append((i,j,val))
    a=(N-15)//2
    assert exc==[(0,N-8,-2),(a,a+7,2)]
    return N,M,base,exc


def ball_edges(N,base,seeds,radius):
    adj=[[] for _ in range(N)]
    for i,j,sig in base:
        adj[i].append(j); adj[j].append(i)
    dist={v:0 for v in seeds}; q=deque(seeds)
    while q:
        u=q.popleft()
        if dist[u]>=radius: continue
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1; q.append(v)
    V=set(dist)
    return V,[e for e in base if e[0] in V and e[1] in V]


def local_matrix(edges,ex):
    V=sorted(set(v for e in edges for v in e[:2])|set(ex[:2]))
    pos={v:i for i,v in enumerate(V)}
    Q=sp.zeros(len(V))
    for i,j,sig in edges:
        a,b=pos[i],pos[j]
        Q[a,a]+=1;Q[b,b]+=1
        Q[a,b]-=sig;Q[b,a]-=sig
    i,j,val=ex; a,b=pos[i],pos[j]
    Q[a,b]+=val;Q[b,a]+=val
    return Q


def check_full(k, modified=False, expected=None):
    A=matrix_A(k, modified)
    Q=sp.Matrix((8*np.eye(15*k,dtype=np.int64)-A@A).tolist())
    piv=positive_ldl(Q)
    if expected is not None:
        assert int(sp.prod(piv))==expected


def check_large(k):
    N,_,base,exc=decomposition(k)
    sets=[]
    for ex,key,nv,ne in [(exc[0],"neg",109,188),(exc[1],"pos",110,192)]:
        V,E=ball_edges(N,base,ex[:2],5)
        assert len(V)==nv and len(E)==ne
        sets.append({tuple(sorted(e[:2])) for e in E})
        Q=local_matrix(E,ex)
        piv=positive_ldl(Q)
        assert int(sp.prod(piv))==LOCAL_DETS[key]
    assert sets[0].isdisjoint(sets[1])


if __name__=="__main__":
    check_full(7, True, K7_DET)
    for k,d in SMALL_DETS.items():
        check_full(k, False, d)
    for k in range(21,42,2):
        check_large(k)
    print("Exact step-fifteen certificates passed; k=5 remains open.")
