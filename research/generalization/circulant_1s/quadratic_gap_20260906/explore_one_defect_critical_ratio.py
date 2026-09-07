#!/usr/bin/env python3
"""Numerical explorer for the large-L canonical one-defect threshold.

This script uses the exact 4L endpoint reduction but evaluates the continuously
extended continuant functions in floating arithmetic.  It is exploration only;
no printed limit is theorem evidence.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.linalg import eigh
from scipy.optimize import brentq


def chord_block(L: int, epsilon: int = -1, alpha: int = +1) -> np.ndarray:
    B = np.zeros((L, L), dtype=float)
    for a in range(L - 1):
        sign = epsilon * ((-1) ** a)
        B[a, a + 1] = B[a + 1, a] = sign
    B[L - 1, 0] = B[0, L - 1] = epsilon * alpha
    return B


def signed_shift(L: int, alpha: int = +1) -> np.ndarray:
    S = np.zeros((L, L), dtype=float)
    for a in range(L - 1):
        S[a, a + 1] = 1.0
    S[L - 1, 0] = float(alpha)
    return S


def scalar_hj(g: float, n: float) -> tuple[float, float]:
    """Return D_n/D_(n-1) and 1/D_(n-1), continuously in n."""
    if abs(g - 2.0) < 1e-11:
        return (n + 1.0) / n, 1.0 / n

    eta = math.acosh(g / 2.0)
    if n * eta > 35.0:
        H = math.exp(eta) * (
            1.0 - math.exp(-2.0 * (n + 1.0) * eta)
        ) / (1.0 - math.exp(-2.0 * n * eta))
        J = 2.0 * math.sinh(eta) * math.exp(-n * eta) / (
            1.0 - math.exp(-2.0 * n * eta)
        )
    else:
        H = math.sinh((n + 1.0) * eta) / math.sinh(n * eta)
        J = math.sinh(eta) / math.sinh(n * eta)
    return H, J


def endpoint_matrix(L: int, r: float) -> np.ndarray:
    epsilon, alpha = -1, +1
    B = chord_block(L, epsilon, alpha)
    G = 6.0 * np.eye(L) - B @ B
    g, U = np.linalg.eigh(G)

    he = np.empty(L)
    je = np.empty(L)
    ho = np.empty(L)
    jo = np.empty(L)
    for i, gg in enumerate(g):
        he[i], je[i] = scalar_hj(float(gg), r)
        ho[i], jo[i] = scalar_hj(float(gg), r - 1.0)

    He = (U * he) @ U.T
    Je = (U * je) @ U.T
    Ho = (U * ho) @ U.T
    Jo = (U * jo) @ U.T

    P = -signed_shift(L, alpha).T
    M = np.zeros((L, L))
    M[0, 0] = -2 * epsilon
    M[1, L - 1] = -2 * epsilon * alpha
    Z = np.zeros((L, L))

    return np.block(
        [
            [He, -Je + M, Z, P],
            [-Je + M.T, He, P.T, Z],
            [Z, P, Ho, -Jo],
            [P.T, Z, -Jo, Ho],
        ]
    )


def smallest_endpoint_eigenvalue(L: int, r: float) -> float:
    E = endpoint_matrix(L, r)
    return float(
        eigh(
            E,
            subset_by_index=[0, 0],
            eigvals_only=True,
            check_finite=False,
        )[0]
    )


def critical_ratio(L: int) -> float:
    root = brentq(
        lambda r: smallest_endpoint_eigenvalue(L, r),
        1.0 * L,
        1.12 * L,
        xtol=2e-9,
        rtol=1e-10,
        maxiter=40,
    )
    return (2.0 * root + 1.0) / L


def main() -> None:
    rows = []
    for L in (51, 75, 101, 151, 201):
        value = critical_ratio(L)
        rows.append((L, value))
        print(f"L={L:3d}  c_L={value:.12f}")

    # Exploratory fits only.
    fit_rows = rows[-4:]
    X = np.array([[1.0, 1.0 / L, 1.0 / (L * L)] for L, _ in fit_rows])
    y = np.array([v for _, v in fit_rows])
    c1 = np.linalg.lstsq(X, y, rcond=None)[0]
    print("fit c+a/L+b/L^2:", c1)

    X2 = np.array([[1.0, 1.0 / (L * L), 1.0 / (L**4)] for L, _ in fit_rows])
    c2 = np.linalg.lstsq(X2, y, rcond=None)[0]
    print("fit c+b/L^2+d/L^4:", c2)
    print("Observed c_infty ~", c2[0])


if __name__ == "__main__":
    main()
