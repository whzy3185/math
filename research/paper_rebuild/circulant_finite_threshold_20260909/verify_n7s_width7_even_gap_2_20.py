#!/usr/bin/env python3
"""Exact finite certificate for N7S_WIDTH7_EVEN_GAP_2_20_RULE.md."""
from __future__ import annotations
import functools
import numpy as np

SCALES=(16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,6144,8192,12288,16384)
GAPS=tuple(range(2,22,2))


def permute_mask(mask,rot,reflection):
    out=0
    for i in range(7):
        if (mask>>i)&1:
            j=(i+rot)%7 if not reflection else (-i-1+rot)%7
            out |= 1<<j
    return out

D7=[]
for reflection in (False,True):
    for rot in range(7):
        D7.append(tuple(permute_mask(m,rot,reflection) for m in range(128)))
D7=list(dict.fromkeys(D7)); assert len(D7)==14

@functools.lru_cache(maxsize=None)
def canonical(word):
    return min(tuple(a[d] for d in word) for a in D7)


def heptagon(mask):
    B=np.zeros((7,7),dtype=np.int64)
    for i in range(7):
        sig=-1 if ((mask>>i)&1) else 1
        j=(i+1)%7
        B[i,j]=B[j,i]=sig
    return B

BLOCKS=[heptagon(m) for m in range(128)]
I7=np.eye(7,dtype=np.int64)


def strip_matrix(word):
    states=[0]
    for d in word:
        states.append(states[-1]^d)
    M=np.zeros((7*len(states),7*len(states)),dtype=np.int64)
    for j,state in enumerate(states):
        a=slice(7*j,7*j+7); M[a,a]=BLOCKS[state]
        if j+1<len(states):
            b=slice(7*(j+1),7*(j+2)); M[a,b]=I7; M[b,a]=I7
    return M


def exact_reject(word):
    M=strip_matrix(word)
    Q=M@M-8*np.eye(M.shape[0],dtype=np.int64)
    vals,vecs=np.linalg.eigh(Q.astype(float))
    for idx in np.argsort(vals)[::-1][:8]:
        if vals[idx] < -1e-9:
            continue
        direction=vecs[:,idx]
        for scale in SCALES:
            w=np.rint(scale*direction).astype(np.int64)
            if not np.any(w):
                continue
            if int(w@(Q@w))>=0:
                return True
    return False


def check(g):
    cands={
        canonical(tuple([127]*3+[d]+[127]*g+[e]+[127]*3))
        for d in range(127) for e in range(127)
    }
    assert len(cands)==1265
    survivors=[word for word in cands if not exact_reject(word)]
    assert survivors==[]
    print('gap',g,': 1265 -> 0')


if __name__=='__main__':
    for g in GAPS:
        check(g)
    print('Exact width-seven even-gap 2--20 exclusions passed.')
