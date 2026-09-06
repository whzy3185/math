#!/usr/bin/env python3
"""Seam-safe numerical exploration of odd finite orders.

This script is exploratory only.  It uses the same quasiperiodic Hamilton
model as the exact finite certificates:

    A = T + T^{-1} + M_tau T^s + T^{-s} M_tau,
    T^N = alpha I.

It is intended to map arithmetic resonances and candidate defect words after
the exact C_21(1,7) obstruction.  No printed row is a theorem unless it is
separately certified in a proof note.
"""

from __future__ import annotations

import itertools
import math
import numpy as np


def shift_matrix(n: int, alpha: int) -> np.ndarray:
    T = np.zeros((n, n), dtype=float)
    for i in range(n - 1):
        T[i, i + 1] = 1.0
    T[n - 1, 0] = float(alpha)
    return T


def adjacency(n: int, s: int, tau: np.ndarray, alpha: int) -> np.ndarray:
    T = shift_matrix(n, alpha)
    M = np.diag(tau.astype(float))
    Ts = np.linalg.matrix_power(T, s)
    Tms = np.linalg.matrix_power(T.T, s)  # T^{-s}; alpha=+/-1
    A = T + T.T + M @ Ts + Tms @ M
    assert np.max(np.abs(A - A.T)) < 1e-12
    return A


def rho2(n: int, s: int, tau: np.ndarray, alpha: int) -> float:
    vals = np.linalg.eigvalsh(adjacency(n, s, tau, alpha))
    return float(np.max(np.abs(vals)) ** 2)


def tau_from_q(q: np.ndarray, anchor: int) -> np.ndarray:
    n = len(q)
    tau = np.empty(n, dtype=int)
    tau[0] = anchor
    for i in range(n - 1):
        tau[i + 1] = q[i] * tau[i]
    assert q[n - 1] * tau[n - 1] == tau[0]
    return tau


def best_k_defects(n: int, s: int, k: int) -> tuple[float, tuple]:
    """Exhaustively scan Q words with exactly k positive defects.

    Intended only for small n/k.  Product(Q)=+1 requires k odd when n is odd.
    """
    assert n % 2 == 1 and k % 2 == 1
    best = (float("inf"), ())
    for defects in itertools.combinations(range(n), k):
        q = -np.ones(n, dtype=int)
        q[list(defects)] = 1
        for anchor in (+1, -1):
            tau = tau_from_q(q, anchor)
            for alpha in (+1, -1):
                value = rho2(n, s, tau, alpha)
                if value < best[0]:
                    best = (value, (defects, anchor, alpha))
    return best


def one_defect(n: int, s: int) -> tuple[float, tuple[int, int]]:
    best = (float("inf"), (0, 0))
    for anchor in (+1, -1):
        tau = np.array([anchor * ((-1) ** i) for i in range(n)], dtype=int)
        for alpha in (+1, -1):
            value = rho2(n, s, tau, alpha)
            if value < best[0]:
                best = (value, (anchor, alpha))
    return best


def main() -> None:
    print("one-defect short odd chord-cycle scan")
    for chord_cycle_length in (3, 5, 7, 9, 11):
        print(f"L={chord_cycle_length}")
        for s in (5, 7, 9, 11, 13, 15, 17, 19):
            n = chord_cycle_length * s
            value, sector = one_defect(n, s)
            mark = " ABOVE 8" if value >= 8.0 else ""
            print(
                f"  s={s:2d} N={n:3d} rho^2={value:.12f} "
                f"sector={sector}{mark}"
            )

    print()
    print("small repaired examples (numerical only)")
    for n, s, k in ((19, 9, 5), (23, 11, 5), (21, 7, 3), (21, 7, 5)):
        value, data = best_k_defects(n, s, k)
        print(f"  (N,s,k)=({n},{s},{k}) best rho^2={value:.12f} data={data}")


if __name__ == "__main__":
    main()
