#!/usr/bin/env python3
"""Exact residual certificates for N5S_BASE_15_17_GLOBAL_OBSTRUCTION.md.

The previously proved gap-2/4 and gap-6--14 local lemmas are separate
certificates.  This script verifies the new 14-column single-defect lemma and
exhausts the cyclic residual gap patterns left after those local rules.

Floating eigensolvers only propose integer Rayleigh witnesses.  A branch is
rejected only after exact int64 arithmetic verifies
    w^T(M^2-8I)w >= 0.
"""
from __future__ import annotations
import functools
import numpy as np

SCALES=(16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,6144,8192,12288,16384)
BAD_REPS=(0,1,3,5,7,11,15)
SINGLE_EXPECT={0:(660,270),1:(312,258),3:(310,252),5:(120,262),7:(98,226),11:(11,9295),15:(8,270)}


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


def signs(mask):
    return np.array([-1 if (mask>>r)&1 else 1 for r in range(5)],dtype=np.int64)


def pentagon(mask):
    B=np.zeros((5,5),dtype=np.int64)
    e=signs(mask)
    for r in range(5):
        q=(r+1)%5
        B[r,q]=B[q,r]=e[r]
    return B


BLOCKS=[pentagon(m) for m in range(32)]
I5=np.eye(5,dtype=np.int64)


def states_from_deltas(eta0,ds):
    out=[eta0]; cur=eta0
    for d in ds:
        cur ^= d
        out.append(cur)
    return out


def strip_matrix(ds):
    states=states_from_deltas(0,ds)
    M=np.zeros((5*len(states),5*len(states)),dtype=np.int64)
    for j,state in enumerate(states):
        a=slice(5*j,5*j+5)
        M[a,a]=BLOCKS[state]
        if j+1<len(states):
            b=slice(5*(j+1),5*(j+2))
            M[a,b]=I5; M[b,a]=I5
    return M


def exact_witness_matrix(M):
    Q=M@M-8*np.eye(M.shape[0],dtype=np.int64)
    vals,vecs=np.linalg.eigh(Q.astype(float))
    for idx in np.argsort(vals)[::-1][:6]:
        if vals[idx] < -1e-9:
            continue
        v=vecs[:,idx]
        for scale in SCALES:
            w=np.rint(scale*v).astype(np.int64)
            if not np.any(w):
                continue
            q=int(w@(Q@w)); n=int(w@w)
            if n>0 and q>=0:
                return q,n,w
    return None


def exact_reject_strip(ds):
    return exact_witness_matrix(strip_matrix(ds)) is not None


def check_single_defect_14():
    got={}
    for d in BAD_REPS:
        ds=tuple([31]*5+[d]+[31]*7)
        w=exact_witness_matrix(strip_matrix(ds))
        assert w is not None
        got[d]=(w[0],w[1])
    assert got==SINGLE_EXPECT
    print('14-column single-defect witnesses:',got)


def seam_mask(eta_last,eta0,q):
    a=signs(eta_last); b=signs(eta0); out=0
    for r in range(5):
        phi=int(a[r]*b[(r+1)%5]*q[r]*q[(r+1)%5])
        if phi==-1:
            out |= 1<<r
    return out


def full_A(s,states,q):
    N=5*s
    A=np.zeros((N,N),dtype=np.int64)
    def idx(j,r): return j+r*s
    for j,m in enumerate(states):
        e=signs(m)
        for r in range(5):
            u=idx(j,r); v=idx(j,(r+1)%5)
            A[u,v]=A[v,u]=e[r]
    for j in range(s-1):
        for r in range(5):
            u=idx(j,r); v=idx(j+1,r)
            A[u,v]=A[v,u]=1
    for r in range(5):
        u=idx(s-1,r); v=idx(0,(r+1)%5)
        A[u,v]=A[v,u]=q[r]
    return A


def check_r2(s,G,h):
    count=0
    for alpha in (1,-1):
        q=np.ones(5,dtype=np.int64)
        if alpha==-1:
            q[4]=-1
        for eta0 in range(32):
            for d in range(31):
                for e in range(31):
                    ds=tuple([d]+[31]*h+[e]+[31]*(G-1))
                    st=states_from_deltas(eta0,ds)
                    if seam_mask(st[-1],st[0],q)!=31:
                        continue
                    count += 1
                    assert exact_witness_matrix(full_A(s,st,q)) is not None
    assert count==1920
    print('r=2 residual',s,(G,h),'full cyclic candidates',count)


def local_r3_survivors(G):
    out=[]
    for d1 in BAD_REPS:
        for d2 in range(31):
            for d3 in range(31):
                ds=tuple([d1,31,d2,31,d3]+[31]*(G-1))
                # Each is a proper (s-1)-column principal open strip.
                if exact_reject_strip(ds[:-1]):
                    continue
                if exact_reject_strip(ds[1:]):
                    continue
                out.append((d1,d2,d3))
    return out


def expand_d5(triples):
    return {tuple(a[d] for d in tri) for tri in triples for a in D5}


def check_r3(s,G,expected_canonical,expected_expanded,expected_full):
    tris=local_r3_survivors(G)
    assert len(tris)==expected_canonical
    exp=expand_d5(tris)
    assert len(exp)==expected_expanded
    count=0
    for d1,d2,d3 in exp:
        ds=tuple([d1,31,d2,31,d3]+[31]*(G-1))
        for alpha in (1,-1):
            q=np.ones(5,dtype=np.int64)
            if alpha==-1:
                q[4]=-1
            for eta0 in range(32):
                st=states_from_deltas(eta0,ds)
                if seam_mask(st[-1],st[0],q)!=31:
                    continue
                count += 1
                assert exact_witness_matrix(full_A(s,st,q)) is not None
    assert count==expected_full
    print('r=3 residual',s,'canonical',len(tris),'expanded',len(exp),'full',count)


if __name__=='__main__':
    check_single_defect_14()
    check_r2(15,12,1)
    check_r2(15,10,3)
    check_r3(15,10,10,50,100)
    check_r2(17,14,1)
    check_r2(17,12,3)
    check_r3(17,12,2,10,40)
    print('All exact residual s=15,17 cyclic obstruction certificates passed.')
