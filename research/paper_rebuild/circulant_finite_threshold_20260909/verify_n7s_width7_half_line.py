#!/usr/bin/env python3
"""Exact certificate for N7S_WIDTH7_HALF_LINE_RIGIDITY.md."""
from __future__ import annotations
import functools
import numpy as np

SCALES=(16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,6144,8192,12288,16384,24576,32768)
EXPECTED_REPS=(0,1,3,5,7,9,11,15,19,21,23,27,31,43,47,55,63)
EXPECTED_CERTS={
0:(616,252),1:(448,266),3:(404,234),5:(344,267),7:(328,261),
9:(228,270),11:(220,256),15:(260,266),19:(152,263),21:(62,266),
23:(98,261),27:(176,265),31:(94,264),43:(20,610),55:(14,590),
}


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


def exact_witness(M):
    Q=M@M-8*np.eye(M.shape[0],dtype=np.int64)
    vals,vecs=np.linalg.eigh(Q.astype(float))
    for idx in np.argsort(vals)[::-1][:8]:
        if vals[idx] < -1e-9:
            continue
        v=vecs[:,idx]
        for scale in SCALES:
            w=np.rint(scale*v).astype(np.int64)
            if not np.any(w):
                continue
            q=int(w@(Q@w)); n=int(w@w)
            if n>0 and q>=0:
                return q,n
    return None


def main():
    reps=sorted({canonical((d,))[0] for d in range(127)})
    assert tuple(reps)==EXPECTED_REPS
    survivors=[]; certs={}
    for d in reps:
        word=tuple([127]*3+[d]+[127]*14)
        wit=exact_witness(strip_matrix(word))
        if wit is None:
            survivors.append(d)
        else:
            certs[d]=wit
    assert survivors==[47,63]
    assert certs==EXPECTED_CERTS

    v47=np.array([-1,-1,-1,-1,-1,1,1],dtype=np.int64)
    v63=np.array([1,-1,1,-1,1,-1,1],dtype=np.int64)
    assert np.array_equal(BLOCKS[80]@v47,2*v47)
    assert np.array_equal(BLOCKS[64]@v63,-2*v63)

    print('width-seven half-line: 17 defect orbits -> [47,63]')
    print('all exact rejection pairs reproduced')


if __name__=='__main__':
    main()
