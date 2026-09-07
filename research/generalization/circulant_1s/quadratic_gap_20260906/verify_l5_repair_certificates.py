#!/usr/bin/env python3
"""Exact positive-definiteness certificates for three `N=5s` signings.

The block model uses width-five signed pentagons.  SymPy performs exact
rational LDL^T decomposition of C=8I-A^2.  The proof decision is the exact
positivity of every diagonal pivot; the printed floating eigenvalues are only
optional orientation and are not used.
"""

from __future__ import annotations

import sympy as sp


def pentagon(state: tuple[int, int, int, int, int]) -> sp.Matrix:
    B = sp.zeros(5)
    for i, sign in enumerate(state):
        j = (i + 1) % 5
        B[i, j] = B[j, i] = sign
    return B


def seam(alpha: int) -> sp.Matrix:
    S = sp.zeros(5)
    for a in range(4):
        S[a, a + 1] = 1
    S[4, 0] = alpha
    return S


def adjacency(word: tuple[tuple[int, int, int, int, int], ...], alpha: int) -> sp.Matrix:
    s = len(word)
    A = sp.zeros(5 * s)

    for j, state in enumerate(word):
        B = pentagon(state)
        for a in range(5):
            for b in range(5):
                A[5 * j + a, 5 * j + b] = B[a, b]

        if j + 1 < s:
            for a in range(5):
                A[5 * j + a, 5 * (j + 1) + a] = 1
                A[5 * (j + 1) + a, 5 * j + a] = 1

    S = seam(alpha)
    for a in range(5):
        for b in range(5):
            A[5 * (s - 1) + a, b] = S[a, b]
            A[b, 5 * (s - 1) + a] = S[a, b]

    assert A == A.T
    return A


CASES = (
    (
        3,
        +1,
        (
            (-1, +1, -1, +1, -1),
            (+1, -1, +1, -1, +1),
            (-1, +1, -1, +1, -1),
        ),
        sp.Rational(2872, 1207),
    ),
    (
        5,
        -1,
        (
            (-1, +1, +1, -1, -1),
            (+1, -1, -1, +1, +1),
            (-1, -1, +1, -1, -1),
            (+1, +1, -1, +1, +1),
            (-1, -1, +1, -1, -1),
        ),
        sp.Rational(4809344936, 1946220357),
    ),
    (
        7,
        -1,
        (
            (-1, -1, -1, -1, +1),
            (+1, +1, +1, +1, -1),
            (-1, -1, -1, -1, +1),
            (-1, +1, +1, +1, -1),
            (+1, -1, -1, -1, +1),
            (-1, +1, -1, +1, +1),
            (+1, -1, +1, -1, -1),
        ),
        sp.Rational(280732937573368, 1166862995234035),
    ),
)


def main() -> None:
    for s, alpha, word, expected_last in CASES:
        assert len(word) == s
        A = adjacency(word, alpha)
        C = 8 * sp.eye(5 * s) - A * A
        _, D = C.LDLdecomposition(hermitian=True)
        pivots = [sp.factor(D[i, i]) for i in range(D.rows)]
        assert all(p.is_positive for p in pivots)
        assert pivots[-1] == expected_last
        print(
            f"C_{5*s}(1,{s}): exact LDL positive, "
            f"last pivot={pivots[-1]}"
        )

    print("all L=5 repair certificates passed")


if __name__ == "__main__":
    main()
