#!/usr/bin/env python3
"""Exact finite certificate for the nine-column signed-triangle strip rule.

A column state is one of the 8 signed adjacency matrices of a triangle.  An
open strip has diagonal triangle blocks and identity matchings between
neighboring columns.

The script recursively extends words.  Whenever the open strip already has
operator norm squared > 8, a floating eigensolver is used only to PROPOSE a
small integer vector.  The pruning decision is made solely by the exact
integer check

    w^T (M^2 - 8 I) w > 0.

A successful run proves the following finite lemma:

If a 9-column open strip has norm squared <= 8, then for positions 1,...,6
(0-based transitions) its triangle states satisfy B_(j+1) = -B_j.

Moreover every word violating this conclusion has an exact local witness with
Rayleigh excess at least 1/1038.
"""

from __future__ import annotations

import itertools
import numpy as np


STATES = list(itertools.product((+1, -1), repeat=3))
EXPECTED_COUNTS = (8, 56, 152, 440, 488, 704, 656, 968, 128)
SCALES = (8, 12, 16, 24, 32, 48, 64, 96)


def triangle(state: tuple[int, int, int]) -> np.ndarray:
    B = np.zeros((3, 3), dtype=np.int64)
    for sign, (i, j) in zip(state, ((0, 1), (1, 2), (2, 0))):
        B[i, j] = B[j, i] = sign
    return B


TRIANGLES = [triangle(state) for state in STATES]


def open_strip(word: tuple[int, ...]) -> np.ndarray:
    k = len(word)
    M = np.zeros((3 * k, 3 * k), dtype=np.int64)
    I3 = np.eye(3, dtype=np.int64)
    for j, state_index in enumerate(word):
        M[3 * j : 3 * j + 3, 3 * j : 3 * j + 3] = TRIANGLES[state_index]
        if j + 1 < k:
            M[3 * j : 3 * j + 3, 3 * (j + 1) : 3 * (j + 2)] = I3
            M[3 * (j + 1) : 3 * (j + 2), 3 * j : 3 * j + 3] = I3
    return M


def exact_positive_witness(M: np.ndarray):
    """Return exact integer certificate q>0, or None if proposer fails."""
    K = M @ M - 8 * np.eye(M.shape[0], dtype=np.int64)
    vals, vecs = np.linalg.eigh(K.astype(float))
    for eig_index in np.argsort(vals)[::-1][:3]:
        if vals[eig_index] <= 1e-10:
            continue
        direction = vecs[:, eig_index]
        for scale in SCALES:
            w = np.rint(scale * direction).astype(np.int64)
            if not np.any(w):
                continue
            q = int(w @ (K @ w))
            norm = int(w @ w)
            if q > 0:
                # Uniform exact margin q/norm >= 1/1038.
                assert 1038 * q >= norm
                return w, q, norm
    return None


def complement(index: int) -> int:
    # With the lexicographic STATES ordering, sign reversal is index 7-i.
    assert STATES[7 - index] == tuple(-x for x in STATES[index])
    return 7 - index


def main() -> None:
    survivors = [(i,) for i in range(8)]
    counts = [len(survivors)]
    pruned = 0

    for length in range(2, 10):
        next_survivors = []
        for prefix in survivors:
            for state in range(8):
                word = prefix + (state,)
                cert = exact_positive_witness(open_strip(word))
                if cert is None:
                    next_survivors.append(word)
                else:
                    pruned += 1
        survivors = next_survivors
        counts.append(len(survivors))

    assert tuple(counts) == EXPECTED_COUNTS
    assert len(survivors) == 128

    # Every unpruned 9-word has exact sign reversal in the six middle
    # transitions: 1->2, ..., 6->7.
    for word in survivors:
        for j in range(1, 7):
            assert word[j + 1] == complement(word[j])

    print(f"survivor counts by length: {counts}")
    print(f"exactly pruned extensions: {pruned}")
    print("9-column survivors: 128")
    print("forced middle rule: B_(j+1) = -B_j for j=1,...,6")
    print("uniform forbidden-word margin: rho^2 >= 8 + 1/1038")
    print("signed-triangle strip local rule passed")


if __name__ == "__main__":
    main()
