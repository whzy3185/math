#!/usr/bin/env python3
"""Numerical regression for the second-order even phase-slip theorem.

This script is evidence/audit only; the proof is analytic in
EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md.

It checks the effective boundary-layer law

    r^4 (gap_r(z/r^2) - endpoint_r)
      -> z^2 - (pi/(2 sqrt(2))) z

and the optimizing constants

    r^2 phi_r -> pi/(4 sqrt(2)),
    r^4 (endpoint_r - global_r) -> pi^2/32.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.optimize import minimize_scalar


def threshold_matrix(r: int, phi: float) -> np.ndarray:
    s = 2 * r
    xi = np.exp(1j * phi)
    h = 2.0 * math.cos(phi)
    n = 2 * s
    C = np.zeros((n, n), dtype=np.complex128)

    for j in range(s):
        C[j, j] = 4.0 - h if j < r else 4.0 + h
        C[s + j, s + j] = 4.0 + h if j < r else 4.0 - h

    for base in (0, s):
        for j in range(s - 1):
            C[base + j, base + j + 1] = -1.0
            C[base + j + 1, base + j] = -1.0

    C[0, s - 1] = -np.conjugate(xi)
    C[s - 1, 0] = -xi
    C[s, 2 * s - 1] = np.conjugate(xi)
    C[2 * s - 1, s] = xi

    C[0, s + r - 1] = -2.0
    C[s + r - 1, 0] = -2.0
    C[r, 2 * s - 1] = 2.0 * np.conjugate(xi)
    C[2 * s - 1, r] = 2.0 * xi
    return C


def least_gap(r: int, phi: float) -> float:
    return float(np.linalg.eigvalsh(threshold_matrix(r, phi))[0])


def optimize(r: int) -> tuple[float, float, float]:
    endpoint = least_gap(r, 0.0)
    result = minimize_scalar(
        lambda x: least_gap(r, x),
        bounds=(0.0, 1.25 / (r * r)),
        method="bounded",
        options={"xatol": 1e-14},
    )
    return float(result.x), endpoint, float(result.fun)


def main() -> None:
    a = math.pi / (2.0 * math.sqrt(2.0))
    z_star = a / 2.0
    gain_star = math.pi**2 / 32.0

    print(f"effective linear coefficient a = {a:.15f}")
    print(f"target z* = pi/(4 sqrt(2)) = {z_star:.15f}")
    print(f"target gain = pi^2/32 = {gain_star:.15f}")
    print()

    print("boundary-layer parabola")
    for r in (20, 40, 80, 120):
        endpoint = least_gap(r, 0.0)
        row = []
        for z in (0.25, z_star, 0.75):
            value = r**4 * (least_gap(r, z / r**2) - endpoint)
            target = z * z - a * z
            row.append((z, value, target, value - target))
        print(f"r={r}")
        for z, value, target, residual in row:
            print(
                f"  z={z:.12f}  scaled={value:.12f}  "
                f"target={target:.12f}  residual={residual:.3e}"
            )

    print()
    print("optimized phase and gain")
    for r in (10, 20, 40, 80, 120, 160):
        phi, endpoint, global_gap = optimize(r)
        print(
            f"r={r:3d}  "
            f"r^2 phi={r*r*phi:.12f}  "
            f"r^4 gain={r**4*(endpoint-global_gap):.12f}"
        )


if __name__ == "__main__":
    main()
