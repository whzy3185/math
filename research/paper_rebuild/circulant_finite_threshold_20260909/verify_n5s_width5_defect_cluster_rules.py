#!/usr/bin/env python3
"""Exact integer certificates for N5S_WIDTH5_DEFECT_CLUSTER_RULES.md."""
from __future__ import annotations
import functools
import numpy as np

SCALES=(16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,6144,8192,12288,16384,24576,32768)


def permute_mask(mask,rot,reflection):
    out=0
    for i in range(5):
        if (mask>>i)&1:
            j=(i+rot)%5 if not reflection else (-i-1+rot)%5
            out |= 1<<j
    return out

D5=[]
for reflection in (False,True):
    for rot in range(5):
        D5.append(tuple(permute_mask(m,rot,reflection) for m in range(32)))
D5=list(dict.fromkeys(D5)); assert len(D5)==10

@functools.lru_cache(maxsize=None)
def canonical(ds):
    return min(tuple(a[d] for d in ds) for a in D5)


def pentagon(mask):
    B=np.zeros((5,5),dtype=np.int64)
    for i in range(5):
        sig=-1 if ((mask>>i)&1) else 1
        j=(i+1)%5
        B[i,j]=B[j,i]=sig
    return B

BLOCKS=[pentagon(m) for m in range(32)]
I5=np.eye(5,dtype=np.int64)


def strip_matrix(ds):
    states=[0]
    for d in ds:
        states.append(states[-1]^d)
    M=np.zeros((5*len(states),5*len(states)),dtype=np.int64)
    for j,state in enumerate(states):
        a=slice(5*j,5*j+5); M[a,a]=BLOCKS[state]
        if j+1<len(states):
            b=slice(5*(j+1),5*(j+2)); M[a,b]=I5; M[b,a]=I5
    return M


def exact_reject(ds):
    M=strip_matrix(ds)
    Q=M@M-8*np.eye(M.shape[0],dtype=np.int64)
    vals,vecs=np.linalg.eigh(Q.astype(float))
    for idx in np.argsort(vals)[::-1][:8]:
        if vals[idx] < -1e-9:
            continue
        v=vecs[:,idx]
        for scale in SCALES:
            w=np.rint(scale*v).astype(np.int64)
            if np.any(w) and int(w@(Q@w))>=0:
                return True
    return False


def check_pair(g,r):
    cands={
        canonical(tuple([31]*r+[d]+[31]*g+[e]+[31]*r))
        for d in range(31) for e in range(31)
    }
    assert len(cands)==121
    survivors=[ds for ds in cands if not exact_reject(ds)]
    assert survivors==[]
    print('pair gap',g,'context',r,'orbits',len(cands),'-> 0')


def check_triple(r):
    cands={
        canonical(tuple([31]*r+[d]+[31]+[e]+[31]+[f]+[31]*r))
        for d in range(31) for e in range(31) for f in range(31)
    }
    assert len(cands)==3151
    survivors=[ds for ds in cands if not exact_reject(ds)]
    assert survivors==[]
    print('triple gaps (1,1), context',r,'orbits',len(cands),'-> 0')


if __name__=='__main__':
    check_pair(1,9)
    check_pair(3,7)
    check_triple(6)
    print('Exact width-five defect-cluster exclusions passed.')
