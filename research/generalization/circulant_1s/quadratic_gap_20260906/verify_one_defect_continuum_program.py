#!/usr/bin/env python3
"""Audit for ONE_DEFECT_CONTINUUM_CRITICAL_PROGRAM.md.

Exact/integer part:
- construct the standard row gauge;
- verify P'^L=-I;
- verify
    G' = 4I + P'^2 + (P'^T)^2 - 2(E_m,m+1+E_m+1,m)
  entry-by-entry for representative odd L.

Numerical/Observed part:
- use the real-length hyperbolic continuant continuation;
- solve the 2x2 Green crossing for selected L;
- regress the c_L values recorded in the note.

The root table is numerical evidence only.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq


def chord_block(L: int) -> np.ndarray:
    B = np.zeros((L, L), dtype=np.int64)
    epsilon = -1
    alpha = +1
    for a in range(L - 1):
        sign = epsilon * ((-1) ** a)
        B[a, a + 1] = B[a + 1, a] = sign
    B[L - 1, 0] = B[0, L - 1] = epsilon * alpha
    return B


def signed_shift(L: int) -> np.ndarray:
    S = np.zeros((L, L), dtype=np.int64)
    for a in range(L - 1):
        S[a, a + 1] = 1
    S[L - 1, 0] = 1
    return S


def standard_row_gauge(L: int):
    B = chord_block(L)
    G = 6 * np.eye(L, dtype=np.int64) - B @ B
    P = -signed_shift(L).T

    perm = [(2 * k) % L for k in range(L)]
    Gp = G[np.ix_(perm, perm)]
    Pp = P[np.ix_(perm, perm)]

    d = np.ones(L, dtype=np.int64)
    for k in range(L - 1):
        c = int(Gp[k, k + 1])
        assert abs(c) == 1
        d[k + 1] = -d[k] * c
    D = np.diag(d)
    return D @ Gp @ D, D @ Pp @ D


def exact_row_identity() -> None:
    for L in range(3, 32, 2):
        G, P = standard_row_gauge(L)
        m = (L - 1) // 2
        R = np.zeros((L, L), dtype=np.int64)
        R[m, m + 1] = R[m + 1, m] = 1

        PL = np.linalg.matrix_power(P, L)
        assert np.array_equal(PL, -np.eye(L, dtype=np.int64))

        rhs = (
            4 * np.eye(L, dtype=np.int64)
            + P @ P
            + P.T @ P.T
            - 2 * R
        )
        assert np.array_equal(G, rhs)
    print("exact row-gauge identities passed for odd L=3,...,31")


def endpoint_components(L: int):
    G, P = standard_row_gauge(L)
    vals, U = np.linalg.eigh(G.astype(float))
    return vals, U, P.astype(float)


def hj_real(vals: np.ndarray, m: float):
    eta = np.arccosh(np.maximum(vals / 2.0, 1.0))
    h = np.empty_like(vals)
    j = np.empty_like(vals)
    small = eta < 1e-8
    h[small] = m / (m - 1.0)
    j[small] = 1.0 / (m - 1.0)
    e = eta[~small]
    den = -np.expm1(-2.0 * (m - 1.0) * e)
    h[~small] = np.exp(e) * (-np.expm1(-2.0 * m * e)) / den
    j[~small] = (
        np.exp(-(m - 2.0) * e)
        * (-np.expm1(-2.0 * e))
        / den
    )
    return h, j


def endpoint_base_real(L: int, r: float, comp):
    vals, U, P = comp
    he, je = hj_real(vals, r + 1.0)
    ho, jo = hj_real(vals, r)

    def ud(x):
        return (U * x) @ U.T

    He, Je, Ho, Jo = ud(he), ud(je), ud(ho), ud(jo)
    Z = np.zeros((L, L))
    return np.block(
        [
            [He, -Je, Z, P],
            [-Je, He, P.T, Z],
            [Z, P, Ho, -Jo],
            [P.T, Z, -Jo, Ho],
        ]
    )


def green_lambda(L: int, r: float, comp) -> float:
    S0 = endpoint_base_real(L, r, comp)
    W = np.zeros((4 * L, 2))
    q = 1.0 / math.sqrt(2.0)
    W[0, 0] = q
    W[L, 0] = -q
    W[1, 1] = q
    W[2 * L - 1, 1] = -q
    Z = np.linalg.solve(S0, W)
    Gm = (W.T @ Z + Z.T @ W) / 2.0
    return float(eigh(Gm, eigvals_only=True)[-1])


def critical_c(L: int) -> float:
    comp = endpoint_components(L)
    f = lambda r: green_lambda(L, r, comp) - 0.5
    root = brentq(f, 0.95 * L, 1.15 * L, xtol=1e-9, rtol=1e-11)
    return (2.0 * root + 1.0) / L


def numerical_root_regression() -> None:
    targets = {
        13: 2.0814188208,
        21: 2.0915846092,
        31: 2.0947584792,
        51: 2.0964173204,
        101: 2.0971338227,
        201: 2.0973163958,
    }
    for L, target in targets.items():
        c = critical_c(L)
        assert abs(c - target) < 5e-9
        print(f"L={L:3d}: continuous critical c_L={c:.10f}")
    print("continuous critical-root numerical regression passed")


def main() -> None:
    exact_row_identity()
    numerical_root_regression()


if __name__ == "__main__":
    main()
