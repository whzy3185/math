#!/usr/bin/env python3
"""Exact certificate for N5S_WIDTH5_LOCAL_COMPLEMENT_RULE.md.

A floating eigensolver ONLY proposes integer directions.  A prefix is rejected
only after exact int64 arithmetic proves

    w^T (M^2 - 8 I) w >= 0,  w != 0.

Hence floating error can retain extra branches but cannot falsely prune one.
"""
from __future__ import annotations

import functools
import itertools
import numpy as np

SCALES = (
    16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,
    2048,3072,4096,6144,8192,12288,16384,
)
PREFIX_COUNTS = (1,7,33,130,548,1867,3870,10080)


def parity(x: int) -> int:
    return x.bit_count() & 1


def permute_mask(mask: int, rot: int, reflection: bool) -> int:
    out = 0
    for i in range(5):
        if (mask >> i) & 1:
            j = (i + rot) % 5 if not reflection else (-i - 1 + rot) % 5
            out |= 1 << j
    return out


def build_actions():
    actions = []
    # A C5 vertex switching changes the five edge bits by an even-parity mask.
    for sw in (m for m in range(32) if parity(m) == 0):
        for reflection in (False, True):
            for rot in range(5):
                actions.append(tuple(
                    permute_mask(m ^ sw, rot, reflection) for m in range(32)
                ))
    # Remove accidental duplicates: exactly 16*10 = 160 remain.
    actions = list(dict.fromkeys(actions))
    assert len(actions) == 160
    # Global complementation is another spectral-radius-preserving involution.
    actions += [tuple(a[m ^ 31] for m in range(32)) for a in actions]
    assert len(actions) == 320
    return np.array(actions, dtype=np.uint8)


ACTIONS = build_actions()


@functools.lru_cache(maxsize=None)
def canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    """One representative under the 320 global row actions.

    The uint64 encoding is exact through length 12 (at most 60 bits).  Length
    13 occurs only in the final 32-candidate step; use literal tuple order there
    to avoid a 65-bit overflow.
    """
    L = len(word)
    if L <= 12:
        arr = ACTIONS[:, np.array(word, dtype=np.int64)]
        code = np.zeros(320, dtype=np.uint64)
        for j in range(L):
            code = (code << np.uint64(5)) | arr[:, j].astype(np.uint64)
        idx = int(np.argmin(code))
        return tuple(int(x) for x in arr[idx])
    best = None
    for a in ACTIONS:
        w = tuple(int(a[m]) for m in word)
        if best is None or w < best:
            best = w
    assert best is not None
    return best


def pentagon(mask: int) -> np.ndarray:
    B = np.zeros((5,5), dtype=np.int64)
    for i in range(5):
        sign = -1 if ((mask >> i) & 1) else 1
        j = (i + 1) % 5
        B[i,j] = B[j,i] = sign
    return B


BLOCKS = [pentagon(m) for m in range(32)]


def strip_matrix(word: tuple[int, ...]) -> np.ndarray:
    L = len(word)
    M = np.zeros((5*L,5*L), dtype=np.int64)
    I5 = np.eye(5, dtype=np.int64)
    for j,state in enumerate(word):
        M[5*j:5*j+5, 5*j:5*j+5] = BLOCKS[state]
        if j + 1 < L:
            M[5*j:5*j+5, 5*j+5:5*j+10] = I5
            M[5*j+5:5*j+10, 5*j:5*j+5] = I5
    return M


def exact_reject(word: tuple[int, ...]) -> bool:
    """Return True only with an exact integer Rayleigh certificate rho^2>=8."""
    M = strip_matrix(word)
    Q = M @ M - 8*np.eye(M.shape[0], dtype=np.int64)
    vals, vecs = np.linalg.eigh(Q.astype(float))
    for eig_index in np.argsort(vals)[::-1][:6]:
        if vals[eig_index] < -1e-9:
            continue
        direction = vecs[:,eig_index]
        for scale in SCALES:
            w = np.rint(scale*direction).astype(np.int64)
            if not np.any(w):
                continue
            q = int(w @ (Q @ w))
            norm = int(w @ w)
            if norm > 0 and q >= 0:
                return True
    return False


def extend_and_prune(words, side: str, require_bad_pair=False):
    candidates = set()
    for prefix in words:
        for state in range(32):
            word = prefix + (state,) if side == "right" else (state,) + prefix
            word = canonical(word)
            if require_bad_pair:
                # At length 9, the target transitions are 3--4 and 4--5.
                if word[3] ^ word[4] == 31:
                    continue
                if word[4] ^ word[5] == 31:
                    continue
            candidates.add(word)
    survivors = [w for w in candidates if not exact_reject(w)]
    return candidates, survivors


def main():
    # Global complementation plus switching/dihedral row symmetry is transitive
    # on one-column states, so start from the all-positive representative.
    survivors = [(0,)]
    counts = [1]
    for L in range(2,9):
        _, survivors = extend_and_prune(survivors, "right")
        counts.append(len(survivors))
        print("prefix", L, "survivors", len(survivors))
    assert tuple(counts) == PREFIX_COUNTS

    # Only length-nine words with the central two transitions both bad matter.
    cand9, bad9 = extend_and_prune(
        survivors, "right", require_bad_pair=True
    )
    assert len(cand9) == 7392
    assert len(bad9) == 71
    assert all((w[3]^w[4]).bit_count() == 4 for w in bad9)
    assert all((w[4]^w[5]).bit_count() == 4 for w in bad9)
    print("length 9 central-double-bad:", len(cand9), "->", len(bad9))

    cand10, s10 = extend_and_prune(bad9, "right")
    assert (len(cand10), len(s10)) == (2272, 204)
    cand11, s11 = extend_and_prune(s10, "left")
    assert (len(cand11), len(s11)) == (6528, 135)
    cand12, s12 = extend_and_prune(s11, "right")
    assert (len(cand12), len(s12)) == (4320, 1)
    cand13, s13 = extend_and_prune(s12, "left")
    assert len(cand13) == 32
    assert len(s13) == 0

    print("extensions: 204 -> 135 -> 1 -> 0")
    print("Exact width-five thirteen-column complement rule passed.")


if __name__ == "__main__":
    main()
