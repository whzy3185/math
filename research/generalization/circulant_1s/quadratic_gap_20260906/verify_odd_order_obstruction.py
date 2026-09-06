#!/usr/bin/env python3
"""Exact integer verification for ODD_ORDER_ONE_DEFECT_OBSTRUCTION.md."""

from __future__ import annotations

import sympy as sp


def shift_matrix(n: int, alpha: int) -> sp.Matrix:
    T = sp.zeros(n)
    for i in range(n - 1):
        T[i, i + 1] = 1
    T[n - 1, 0] = alpha
    return T


def signed_adjacency(n: int, s: int, alpha: int, anchor: int) -> sp.Matrix:
    T = shift_matrix(n, alpha)
    tau = [anchor * (1 if i % 2 == 0 else -1) for i in range(n)]
    M = sp.diag(*tau)
    return T + T.inv() + M * (T ** s) + (T ** (-s)) * M


CERTIFICATES = {
    (+1, +1): [-1,0,-1,0,-1,0,-1, 1,0,1,0,1,0,1, 1,0,1,0,1,0,1],
    (+1, -1): [-3,-1,-1,0,1,1,3, 3,1,1,0,-1,0,-1, 1,0,1,0,-1,-1,-3],
    (-1, +1): [1,0,1,0,1,0,1, 1,0,1,0,1,0,1, -1,0,-1,0,-1,0,-1],
    (-1, -1): [-3,1,-1,0,1,-1,3, -3,1,-1,0,1,0,1, 1,0,1,0,-1,1,-3],
}


def main() -> None:
    n, s = 21, 7
    for (alpha, anchor), entries in CERTIFICATES.items():
        A = signed_adjacency(n, s, alpha, anchor)
        v = sp.Matrix(entries)
        norm = (v.T * v)[0]
        excess = (v.T * (A * A - 8 * sp.eye(n)) * v)[0]
        assert excess == 2
        assert norm in (12, 48)
        rayleigh = sp.Rational(8 * norm + excess, norm)
        assert rayleigh > 8
        print(
            f"alpha={alpha:+d}, anchor={anchor:+d}: "
            f"norm={norm}, excess={excess}, A^2-Rayleigh={rayleigh}"
        )
    print("odd-order one-defect obstruction certificates passed")


if __name__ == "__main__":
    main()
