#!/usr/bin/env python3
"""Exact rational LDL certificates for N7S_POSITIVE_BASES_19_23.md.

The file name is retained for history; the certificate now covers the six new
horizontal bases s=19,21,23,25,27,29.
"""

import numpy as np
import sympy as sp

CASES = {
    (133,19): ([110,111,116,117], 6881113906591271314868115580534177008571456256473620931470387912),
    (147,21): ([3,4,128,129], 2052458732243546448194681401672407273703693170869317348327038263943800),
    (161,23): ([43,44,116,117], 24907296132626454444572251848041426045840481567809677574423420267114852501384),
    (175,25): ([47,48,76,77], 1758165770944445569752092124506721227335573274962881828944710512735671046378917175416),
    (189,27): ([51,52,82,83], 15677991793916311788147429358354018134700963356176700551533154605289188209355018145946009600),
    (203,29): ([55,56,88,89], 139031874687624227325008974504113378822083728002061895279031442154489015618584145360970870352248832),
}


def matrix_A(N, s, flips):
    A = np.zeros((N,N), dtype=np.int64)
    for i in range(N-1):
        A[i,i+1] = A[i+1,i] = 1
    A[N-1,0] = A[0,N-1] = -1
    tau = np.array([1 if i % 2 == 0 else -1 for i in range(N)], dtype=np.int64)
    for i in flips:
        tau[i] *= -1
    for i, sig in enumerate(tau):
        j = (i+s) % N
        A[i,j] = A[j,i] = int(sig)
    return A


def check_case(N, s, flips, expected_det):
    A = matrix_A(N,s,flips)
    K = sp.Matrix((8*np.eye(N,dtype=np.int64) - A@A).tolist())
    _, D = K.LDLdecomposition(hermitian=False)
    pivots = [sp.factor(D[i,i]) for i in range(N)]
    assert all(p > 0 for p in pivots)
    det = int(K.det())
    assert det == expected_det
    print((N,s), "positive LDL pivots:", len(pivots), "det=", det)


def main():
    for (N,s),(flips,det) in CASES.items():
        check_case(N,s,flips,det)
    print("All six N=7s positive-base exact certificates passed.")


if __name__ == "__main__":
    main()
