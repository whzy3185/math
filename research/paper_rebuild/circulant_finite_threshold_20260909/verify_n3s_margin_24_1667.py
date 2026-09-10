#!/usr/bin/env python3
"""Exact finite certificates for the upgraded odd N=3s margin 24/1667.

The floating eigensolver is used ONLY to propose integer directions.  A branch
is pruned/certified only when exact int64 quadratic forms satisfy

    1667 * w^T(M^2-8I)w >= 24 * w^T w > 0.

The script checks:
  * the nine-column open-strip local rule;
  * the full C_27(1,9) Hamilton-gauge population after exact prefix pruning.

The C_21(1,7) base has the independently proved stronger exact margin 18/131.
"""
from __future__ import annotations
import itertools
import numpy as np

NUM = 24
DEN = 1667
STATES = list(itertools.product((+1, -1), repeat=3))
SCALES = (32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,6144,8192)
LOCAL_COUNTS = (8,56,152,440,488,1016,656,1064,128)
PREFIX_COUNTS = LOCAL_COUNTS[:-1]


def triangle(state):
    B=np.zeros((3,3),dtype=np.int64)
    for sign,(i,j) in zip(state,((0,1),(1,2),(2,0))):
        B[i,j]=B[j,i]=sign
    return B

TRIANGLES=[triangle(s) for s in STATES]


def open_strip(word):
    k=len(word); M=np.zeros((3*k,3*k),dtype=np.int64)
    I3=np.eye(3,dtype=np.int64)
    for j,idx in enumerate(word):
        M[3*j:3*j+3,3*j:3*j+3]=TRIANGLES[idx]
        if j+1<k:
            M[3*j:3*j+3,3*(j+1):3*(j+2)]=I3
            M[3*(j+1):3*(j+2),3*j:3*j+3]=I3
    return M


def seam(alpha):
    S=np.zeros((3,3),dtype=np.int64)
    S[0,1]=1; S[1,2]=1; S[2,0]=alpha
    return S


def cycle_strip(word,alpha):
    M=open_strip(word); S=seam(alpha); k=len(word)
    M[3*(k-1):3*k,0:3]=S
    M[0:3,3*(k-1):3*k]=S.T
    assert np.array_equal(M,M.T)
    return M


def exact_margin_witness(M):
    K=M@M-8*np.eye(M.shape[0],dtype=np.int64)
    vals,vecs=np.linalg.eigh(K.astype(float))
    target=NUM/DEN
    for eig_index in np.argsort(vals)[::-1][:6]:
        # Proposal filter only; acceptance below is exact integer arithmetic.
        if vals[eig_index] <= target+1e-10:
            continue
        direction=vecs[:,eig_index]
        for scale in SCALES:
            w=np.rint(scale*direction).astype(np.int64)
            if not np.any(w):
                continue
            q=int(w@(K@w)); norm=int(w@w)
            if q>0 and DEN*q >= NUM*norm:
                return w,q,norm
    return None


def complement(index):
    assert STATES[7-index] == tuple(-x for x in STATES[index])
    return 7-index


def local_rule():
    survivors=[(i,) for i in range(8)]; counts=[8]
    for length in range(2,10):
        nxt=[]
        for prefix in survivors:
            for state in range(8):
                word=prefix+(state,)
                if exact_margin_witness(open_strip(word)) is None:
                    nxt.append(word)
        survivors=nxt; counts.append(len(survivors))
    assert tuple(counts)==LOCAL_COUNTS
    assert len(survivors)==128
    for word in survivors:
        for j in range(1,7):
            assert word[j+1]==complement(word[j])
    return counts


def c27_base():
    survivors=[(i,) for i in range(8)]; counts=[8]
    for length in range(2,9):
        nxt=[]
        for prefix in survivors:
            for state in range(8):
                word=prefix+(state,)
                if exact_margin_witness(open_strip(word)) is None:
                    nxt.append(word)
        survivors=nxt; counts.append(len(survivors))
    assert tuple(counts)==PREFIX_COUNTS
    assert len(survivors)==1064
    full=0
    for alpha in (+1,-1):
        for prefix in survivors:
            for state in range(8):
                cert=exact_margin_witness(cycle_strip(prefix+(state,),alpha))
                assert cert is not None
                full+=1
    assert full==17024
    assert 2*(8**9)==268_435_456
    return counts,full


if __name__=="__main__":
    lc=local_rule()
    pc,full=c27_base()
    assert 18*1667 > 24*131  # C21 stronger margin 18/131.
    print("local survivor counts:",lc)
    print("C27 prefix counts:",pc)
    print("C27 exact cyclic candidates:",full)
    print("uniform certified margin: 24/1667")
    print("upgraded odd N=3s certificate passed")
