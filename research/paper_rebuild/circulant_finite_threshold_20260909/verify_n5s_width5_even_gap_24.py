#!/usr/bin/env python3
"""Exact certificate for N5S_WIDTH5_EVEN_GAP_24_RULE.md.

Floating eigenvectors are used only to propose integer Rayleigh witnesses.
A branch is pruned only after exact integer arithmetic verifies

    w^T (M^2 - 8 I) w >= 0,  w != 0.

Thus numerical error can retain extra branches but cannot falsely reject a
sub-threshold strip.
"""
from __future__ import annotations
import functools
import numpy as np

SCALES = (
    16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,
    2048,3072,4096,6144,8192,12288,16384,
)
EXPECTED = {
    2: ((121,12),(336,61),(1880,8),(256,0)),
    4: ((121,12),(336,57),(1752,1),(32,0)),
}


def permute_mask(mask: int, rot: int, reflection: bool) -> int:
    out = 0
    for i in range(5):
        if (mask >> i) & 1:
            j = (i + rot) % 5 if not reflection else (-i - 1 + rot) % 5
            out |= 1 << j
    return out


D5 = []
for reflection in (False, True):
    for rot in range(5):
        D5.append(tuple(permute_mask(m, rot, reflection) for m in range(32)))
D5 = list(dict.fromkeys(D5))
assert len(D5) == 10


@functools.lru_cache(maxsize=None)
def canonical(ds: tuple[int, ...]) -> tuple[int, ...]:
    return min(tuple(a[d] for d in ds) for a in D5)


def pentagon(mask: int) -> np.ndarray:
    B = np.zeros((5, 5), dtype=np.int64)
    for i in range(5):
        sig = -1 if ((mask >> i) & 1) else 1
        j = (i + 1) % 5
        B[i, j] = B[j, i] = sig
    return B


BLOCKS = [pentagon(m) for m in range(32)]
I5 = np.eye(5, dtype=np.int64)


def strip_matrix(ds: tuple[int, ...]) -> np.ndarray:
    states = [0]
    for d in ds:
        states.append(states[-1] ^ d)
    L = len(states)
    M = np.zeros((5 * L, 5 * L), dtype=np.int64)
    for j, state in enumerate(states):
        a = slice(5 * j, 5 * j + 5)
        M[a, a] = BLOCKS[state]
        if j + 1 < L:
            b = slice(5 * (j + 1), 5 * (j + 2))
            M[a, b] = I5
            M[b, a] = I5
    return M


def exact_reject(ds: tuple[int, ...]) -> bool:
    M = strip_matrix(ds)
    Q = M @ M - 8 * np.eye(M.shape[0], dtype=np.int64)
    vals, vecs = np.linalg.eigh(Q.astype(float))
    for idx in np.argsort(vals)[::-1][:6]:
        if vals[idx] < -1e-9:
            continue
        v = vecs[:, idx]
        for scale in SCALES:
            w = np.rint(scale * v).astype(np.int64)
            if not np.any(w):
                continue
            q = int(w @ (Q @ w))
            norm = int(w @ w)
            if norm > 0 and q >= 0:
                return True
    return False


def central(g: int):
    candidates = {
        canonical(tuple([d1] + [31] * g + [d2]))
        for d1 in range(31) for d2 in range(31)
    }
    survivors = [x for x in candidates if not exact_reject(x)]
    return candidates, survivors


def extend(words, side: str):
    candidates = set()
    for ds in words:
        for d in range(32):
            nd = (d,) + ds if side == "left" else ds + (d,)
            candidates.add(canonical(nd))
    survivors = [x for x in candidates if not exact_reject(x)]
    return candidates, survivors


def check(g: int):
    stages = []
    c, s = central(g)
    stages.append((len(c), len(s)))
    c, s = extend(s, "left")
    stages.append((len(c), len(s)))
    c, s = extend(s, "right")
    stages.append((len(c), len(s)))
    c, s = extend(s, "left")
    stages.append((len(c), len(s)))
    assert tuple(stages) == EXPECTED[g]
    assert not s
    print("g =", g, "stages =", stages)


if __name__ == "__main__":
    check(2)
    check(4)
    print("Exact embedded even-gap 2/4 exclusion passed.")
