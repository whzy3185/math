#!/usr/bin/env python3
"""Numerical exploration of the second-order even phase slip.

This script uses the exact reduced threshold matrix C_s(xi) from the analytic
proof and is evidence only.  It is not used in EVEN_GLOBAL_PI2_THEOREM.md.

Conjectured limits:
    r^2 phi_r -> pi/(4 sqrt(2))
    r^4 (e_r - g_(2r)) -> pi^2/32
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import minimize_scalar


def threshold_matrix(r: int, phi: float) -> np.ndarray:
    """Return C_s(xi)=8I-K_s(xi) for s=2r and xi=e^{i phi}."""
    s = 2 * r
    xi = np.exp(1j * phi)
    h = 2.0 * math.cos(phi)
    n = 2 * s
    C = np.zeros((n, n), dtype=np.complex128)

    # E-chain indices: 0,...,s-1; O-chain indices: s,...,2s-1.
    for j in range(s):
        C[j, j] = 4.0 - h if j < r else 4.0 + h
        C[s + j, s + j] = 4.0 + h if j < r else 4.0 - h

    for base in (0, s):
        for j in range(s - 1):
            C[base + j, base + j + 1] = -1.0
            C[base + j + 1, base + j] = -1.0

    # Seam terms.
    C[0, s - 1] = -np.conjugate(xi)
    C[s - 1, 0] = -xi
    C[s, s + s - 1] = np.conjugate(xi)
    C[s + s - 1, s] = xi

    # Cross-chain defect terms.
    C[0, s + r - 1] = -2.0
    C[s + r - 1, 0] = -2.0
    C[r, s + s - 1] = 2.0 * np.conjugate(xi)
    C[s + s - 1, r] = 2.0 * xi

    return C


def least_gap(r: int, phi: float) -> float:
    return float(np.linalg.eigvalsh(threshold_matrix(r, phi))[0])


def optimize_phase(r: int) -> tuple[float, float, float]:
    endpoint = least_gap(r, 0.0)
    # The observed optimizer is O(r^-2); the interval below is deliberately
    # wider than the conjectured constant.
    upper = 1.25 / (r * r)
    result = minimize_scalar(
        lambda x: least_gap(r, x),
        bounds=(0.0, upper),
        method="bounded",
        options={"xatol": 1e-14},
    )
    return float(result.x), endpoint, float(result.fun)


def main() -> None:
    target_phase = math.pi / (4.0 * math.sqrt(2.0))
    target_gain = math.pi**2 / 32.0
    print(f"target r^2 phi = {target_phase:.15f}")
    print(f"target r^4 gain = {target_gain:.15f}")
    print()

    for r in (10, 20, 40, 80, 120, 160, 240):
        phi, endpoint, global_gap = optimize_phase(r)
        scaled_phase = r * r * phi
        scaled_gain = r**4 * (endpoint - global_gap)
        scaled_gap = 4.0 * r * r * global_gap
        print(
            f"r={r:3d}  r^2 phi={scaled_phase:.12f}  "
            f"r^4 gain={scaled_gain:.12f}  "
            f"4 r^2 gap={scaled_gap:.12f}"
        )


if __name__ == "__main__":
    main()
