#!/usr/bin/env python3
"""Exact certificate for N7S_WIDTH7_ARBITRARY_EXTERIOR_HALF_LINE.md.

A floating eigensolver is used only to propose integer directions.  An orbit is
rejected only after exact int64 arithmetic verifies

    w^T (M^2 - 8 I) w >= 0,  w != 0.
"""

from __future__ import annotations
import numpy as np

SCALES = (8,12,16,24,32,48,64,96,128,192,256,384,512,768,
          1024,1536,2048,3072,4096)

EXPECTED = {
    (23,125),
    (31,117),(31,119),
    (43,87),(43,94),(43,95),(43,125),
    (47,87),(47,95),(47,117),(47,119),(47,123),
    (55,94),(55,95),(55,122),(55,123),(55,125),
    (63,87),(63,94),(63,95),(63,107),(63,111),(63,119),
    (127,47),(127,63),
}


def permute_mask(mask: int, rot: int, reflection: bool) -> int:
    out = 0
    for i in range(7):
        if (mask >> i) & 1:
            j = (i + rot) % 7 if not reflection else (-i - 1 + rot) % 7
            out |= 1 << j
    return out


D7 = [(r, f) for f in (False, True) for r in range(7)]


def canonical_pair(x: int, d: int) -> tuple[int,int]:
    return min(
        (permute_mask(x, r, f), permute_mask(d, r, f))
        for r, f in D7
    )


def representatives():
    reps = set()
    for x in range(128):
        for d in range(127):
            reps.add(canonical_pair(x, d))
    assert len(reps) == 1282
    return sorted(reps)


def cycle_block(mask: int) -> np.ndarray:
    B = np.zeros((7,7), dtype=np.int64)
    for i in range(7):
        sig = -1 if ((mask >> i) & 1) else 1
        j = (i + 1) % 7
        B[i,j] = B[j,i] = sig
    return B


def strip_matrix(transitions: tuple[int,...]) -> np.ndarray:
    states = [0]
    for d in transitions:
        states.append(states[-1] ^ d)
    L = len(states)
    M = np.zeros((7*L, 7*L), dtype=np.int64)
    I = np.eye(7, dtype=np.int64)
    for j, state in enumerate(states):
        M[7*j:7*j+7, 7*j:7*j+7] = cycle_block(state)
        if j + 1 < L:
            M[7*j:7*j+7, 7*j+7:7*j+14] = I
            M[7*j+7:7*j+14, 7*j:7*j+7] = I
    return M


def exact_reject(x: int, d: int) -> bool:
    M = strip_matrix((x, d) + (127,)*14)
    Q = M @ M - 8*np.eye(M.shape[0], dtype=np.int64)
    vals, vecs = np.linalg.eigh(Q.astype(float))
    for eig_index in np.argsort(vals)[::-1][:8]:
        if vals[eig_index] < -1e-7:
            continue
        v = vecs[:, eig_index]
        for scale in SCALES:
            w = np.rint(scale*v).astype(np.int64)
            if not np.any(w):
                continue
            q = int(w @ (Q @ w))
            if q >= 0:
                return True
    return False


def main():
    survivors = []
    rejected = 0
    for x, d in representatives():
        if exact_reject(x, d):
            rejected += 1
        else:
            survivors.append((x,d))
    assert rejected == 1257
    assert set(survivors) == EXPECTED
    assert len(survivors) == 25
    print("1282 D7 orbits -> 25 exact survivors")
    print(survivors)
    print("Exact arbitrary-exterior width-seven half-line certificate passed.")


if __name__ == "__main__":
    main()
