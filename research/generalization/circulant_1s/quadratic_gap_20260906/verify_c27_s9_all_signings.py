#!/usr/bin/env python3
"""Exact pruned exhaustive obstruction for every signing of C_27(1,9).

After Hamilton gauge and width-three reordering, an arbitrary chord signing is
an arbitrary word of 9 signed-triangle states (8^9 possibilities), together
with Hamilton holonomy alpha=+/-1.

The proof uses quantitative exact pruning.  A floating eigensolver only
PROPOSES an integer vector; a prefix or full cycle is certified only when
integer arithmetic verifies

    70 * w^T (M^2 - 8 I) w >= w^T w > 0.

Using the 1/70 target leaves 1,064 length-8 prefixes.  Their 8 extensions in
both holonomy sectors give 17,024 final cyclic checks.  Together with the
exactly pruned prefixes, this covers all

    2*8^9 = 268,435,456

Hamilton-gauge representatives and proves rho(A)^2 >= 8 + 1/70.
"""

from __future__ import annotations

import itertools
import numpy as np


STATES = list(itertools.product((+1, -1), repeat=3))
SCALES = (32, 48, 64, 96, 128, 192, 256, 384, 512)
EXPECTED_PREFIX_COUNTS = (8, 56, 152, 440, 488, 1016, 656, 1064)
MARGIN_DENOMINATOR = 70


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
    for j, index in enumerate(word):
        M[3 * j : 3 * j + 3, 3 * j : 3 * j + 3] = TRIANGLES[index]
        if j + 1 < k:
            M[3 * j : 3 * j + 3, 3 * (j + 1) : 3 * (j + 2)] = I3
            M[3 * (j + 1) : 3 * (j + 2), 3 * j : 3 * j + 3] = I3
    return M


def seam(alpha: int) -> np.ndarray:
    S = np.zeros((3, 3), dtype=np.int64)
    S[0, 1] = 1
    S[1, 2] = 1
    S[2, 0] = alpha
    return S


def cycle_strip(word: tuple[int, ...], alpha: int) -> np.ndarray:
    M = open_strip(word)
    S = seam(alpha)
    k = len(word)
    M[3 * (k - 1) : 3 * k, 0:3] = S
    M[0:3, 3 * (k - 1) : 3 * k] = S.T
    assert np.array_equal(M, M.T)
    return M


def exact_margin_witness(M: np.ndarray):
    K = M @ M - 8 * np.eye(M.shape[0], dtype=np.int64)
    vals, vecs = np.linalg.eigh(K.astype(float))
    for eig_index in np.argsort(vals)[::-1][:4]:
        if vals[eig_index] <= 1.0 / MARGIN_DENOMINATOR + 1e-8:
            continue
        direction = vecs[:, eig_index]
        for scale in SCALES:
            w = np.rint(scale * direction).astype(np.int64)
            if not np.any(w):
                continue
            q = int(w @ (K @ w))
            norm = int(w @ w)
            if q > 0 and MARGIN_DENOMINATOR * q >= norm:
                return w, q, norm
    return None


def main() -> None:
    survivors = [(i,) for i in range(8)]
    counts = [8]
    prefix_pruned = 0

    for length in range(2, 9):
        next_survivors = []
        for prefix in survivors:
            for state in range(8):
                word = prefix + (state,)
                if exact_margin_witness(open_strip(word)) is None:
                    next_survivors.append(word)
                else:
                    prefix_pruned += 1
        survivors = next_survivors
        counts.append(len(survivors))

    assert tuple(counts) == EXPECTED_PREFIX_COUNTS
    assert len(survivors) == 1064

    full_checked = 0
    for alpha in (+1, -1):
        for prefix in survivors:
            for state in range(8):
                word = prefix + (state,)
                cert = exact_margin_witness(cycle_strip(word, alpha))
                assert cert is not None
                full_checked += 1

    assert full_checked == 2 * 1064 * 8
    assert 2 * (8 ** 9) == 268_435_456

    print(f"prefix survivor counts: {counts}")
    print(f"exactly pruned prefix extensions: {prefix_pruned}")
    print(f"full cyclic candidates checked exactly: {full_checked}")
    print("Hamilton-gauge population covered: 2*8^9 = 268435456")
    print("uniform theorem: rho(A)^2 >= 8 + 1/70")
    print("C_27(1,9) all-signing obstruction passed")


if __name__ == "__main__":
    main()
