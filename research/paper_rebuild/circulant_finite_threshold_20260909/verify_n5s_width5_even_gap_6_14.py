#!/usr/bin/env python3
"""Exact finite certificate for N5S_WIDTH5_EVEN_GAP_6_14_RULE.md."""
from __future__ import annotations
import functools
import numpy as np

SCALES=(16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,6144,8192,12288,16384)
EXPECTED={
    6:((121,12),(336,53),(1624,0)),
    8:((121,12),(336,40),(1220,0)),
    10:((121,12),(336,35),(1060,0)),
    12:((121,12),(336,19),(572,0)),
    14:((121,12),(336,14),(412,0)),
}

def permute_mask(mask,rot,reflection):
    out=0
    for i in range(5):
        if (mask>>i)&1:
            j=(i+rot)%5 if not reflection else (-i-1+rot)%5
            out|=1<<j
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
    for d in ds: states.append(states[-1]^d)
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
    for idx in np.argsort(vals)[::-1][:6]:
        if vals[idx] < -1e-9: continue
        v=vecs[:,idx]
        for scale in SCALES:
            w=np.rint(scale*v).astype(np.int64)
            if np.any(w) and int(w@(Q@w))>=0:
                return True
    return False

def central(g):
    cands={canonical(tuple([d]+[31]*g+[e])) for d in range(31) for e in range(31)}
    return cands,[x for x in cands if not exact_reject(x)]

def extend(words,side):
    cands=set()
    for ds in words:
        for x in range(32):
            nd=(x,)+ds if side=='left' else ds+(x,)
            cands.add(canonical(nd))
    return cands,[x for x in cands if not exact_reject(x)]

def check(g):
    stages=[]
    c,s=central(g); stages.append((len(c),len(s)))
    c,s=extend(s,'left'); stages.append((len(c),len(s)))
    c,s=extend(s,'right'); stages.append((len(c),len(s)))
    assert tuple(stages)==EXPECTED[g]
    assert not s
    print(g,stages)

if __name__=='__main__':
    for g in (6,8,10,12,14): check(g)
    print('Exact even-gap 6--14 exclusions passed.')
