#!/usr/bin/env python3
"""Exact certificates for N5S_COMPLETE_THRESHOLD_CLASSIFICATION.md.

This verifier checks the two finite ingredients in the uniform long-even-gap
proof:
  * the 128-to-1 nineteen-complement half-line rigidity lemma;
  * the explicit parametric integer witnesses for the three hard relative
    defect types.

Floating eigenvectors are used only in the first item to propose integer
Rayleigh witnesses.  A branch is rejected only after exact int64 evaluation
of w^T(M^2-8I)w >= 0.
"""
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


def check_half_line():
    cands={
        canonical(tuple([x,d]+[31]*19))
        for x in range(32) for d in range(31)
    }
    assert len(cands)==128
    survivors=[ds for ds in cands if not exact_reject(ds)]
    expected=tuple([31,15]+[31]*19)
    assert survivors==[expected]
    print('nineteen-complement half-line rigidity: 128 -> 1')


def check_stabilizer_orbits():
    stab=[a for a in D5 if a[15]==15]
    assert len(stab)==2
    weight4={m for m in range(31) if m.bit_count()==4}
    assert weight4=={15,23,27,29,30}
    unseen=set(weight4); orbits=[]
    while unseen:
        m=min(unseen)
        orb={a[m] for a in stab}
        orbits.append(orb); unseen-=orb
    assert {frozenset(o) for o in orbits}=={
        frozenset({15}),frozenset({23,30}),frozenset({27,29})
    }
    print('relative weight-four defect orbits:',orbits)


v=np.array([1,-1,1,-1,1],dtype=np.int64)
p=-13*v
qv=5*v

LEFT=[
    (-4,2,-4,2,-4),
    (13,3,8,3,13),
    (-17,10,-13,10,-17),
    (7,-3,7,-3,7),
    (-14,12,-13,12,-14),
    (6,-5,6,-5,6),
    (-13,13,-13,13,-13),
    (5,-5,6,-5,5),
]
RIGHT={
15: LEFT,
23:[
    (-2,4,-2,4,-4),
    (-3,-8,-3,-13,13),
    (-10,13,-10,17,-17),
    (3,-7,3,-7,7),
    (-12,13,-12,14,-14),
    (5,-6,5,-6,6),
    (-13,13,-13,13,-13),
    (5,-6,5,-5,5),
],
27:[
    (-4,2,-4,4,-2),
    (8,3,13,-13,-3),
    (-13,10,-17,17,-10),
    (7,-3,7,-7,3),
    (-13,12,-14,14,-12),
    (6,-5,6,-6,5),
    (-13,13,-13,13,-13),
    (6,-5,5,-5,5),
],
}
LEFT=[np.array(z,dtype=np.int64) for z in LEFT]
RIGHT={e:[np.array(z,dtype=np.int64) for z in zs] for e,zs in RIGHT.items()}


def hard_witness(g,e):
    assert g>=14 and g%2==0 and e in RIGHT
    L=g+5
    cols=[p.copy() if j%2==0 else qv.copy() for j in range(L)]
    for j in range(8):
        cols[j]=LEFT[j].copy()
        cols[L-1-j]=RIGHT[e][j].copy()
    return np.concatenate(cols)


def check_parametric_witnesses():
    for e in (15,23,27):
        for g in range(14,102,2):
            ds=tuple([31,15]+[31]*g+[e,31])
            M=strip_matrix(ds)
            Q=M@M-8*np.eye(M.shape[0],dtype=np.int64)
            w=hard_witness(g,e)
            assert int(w@(Q@w))==4
            assert int(w@w)==485*g+2177
    print('parametric hard-family witnesses: q=4, norm=485g+2177')


if __name__=='__main__':
    check_half_line()
    check_stabilizer_orbits()
    check_parametric_witnesses()
    print('Uniform N=5s even-gap certificates passed.')
