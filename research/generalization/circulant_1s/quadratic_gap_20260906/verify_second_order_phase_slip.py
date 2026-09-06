#!/usr/bin/env python3
"""Numerical regression for the even phase-slip asymptotics.

This script is evidence/audit only.  The analytic statements are in
EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md and
EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md.

Leading boundary-layer law:

    r^4 (gap_r(z/r^2) - endpoint_r)
      -> z^2 - (pi/(2 sqrt(2))) z.

Refined optimizer/gain laws:

    r^2 phi_r
      = pi/(4 sqrt(2)) - 3 pi/(16 r) + o(1/r),

    r^4 (endpoint_r-global_r)
      = pi^2/32 - 3 pi^2/(32 sqrt(2) r) + o(1/r).
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


def fitted_scaled_optimizer(r: int) -> tuple[float, float]:
    """Fit the scaled gap to a quadratic in z near the first minimum.

    This is usually more stable than using the raw minimizing phase because
    the physical phase is O(r^-2) while the spectral gain is O(r^-4).
    """
    endpoint = least_gap(r, 0.0)
    zs = np.linspace(0.42, 0.68, 9)
    ys = np.array(
        [r**4 * (least_gap(r, float(z) / r**2) - endpoint) for z in zs]
    )
    c2, c1, c0 = np.polyfit(zs, ys, 2)
    z_opt = -c1 / (2.0 * c2)
    scaled_gain = -np.polyval([c2, c1, c0], z_opt)
    return float(z_opt), float(scaled_gain)


def main() -> None:
    a = math.pi / (2.0 * math.sqrt(2.0))
    z_star = a / 2.0
    gain_star = math.pi**2 / 32.0
    phase_corr = -3.0 * math.pi / 16.0
    gain_corr = -3.0 * math.pi**2 / (32.0 * math.sqrt(2.0))

    print(f"a = pi/(2 sqrt(2)) = {a:.15f}")
    print(f"leading z* = pi/(4 sqrt(2)) = {z_star:.15f}")
    print(f"leading gain = pi^2/32 = {gain_star:.15f}")
    print(f"1/r phase correction = -3pi/16 = {phase_corr:.15f}")
    print(f"1/r gain correction = {gain_corr:.15f}")
    print()

    print("boundary-layer parabola")
    for r in (20, 40, 80, 120):
        endpoint = least_gap(r, 0.0)
        for z in (0.25, z_star, 0.75):
            value = r**4 * (least_gap(r, z / r**2) - endpoint)
            target = z * z - a * z
            print(
                f"r={r:3d}  z={z:.12f}  scaled={value:.12f}  "
                f"leading={target:.12f}  residual={value-target:.3e}"
            )

    print()
    print("quadratic-fit optimizer: refined targets")
    for r in (20, 40, 80, 120, 160):
        z_fit, gain_fit = fitted_scaled_optimizer(r)
        z_target = z_star + phase_corr / r
        gain_target = gain_star + gain_corr / r
        print(
            f"r={r:3d}  "
            f"z_fit={z_fit:.12f}  z_target={z_target:.12f}  "
            f"gain_fit={gain_fit:.12f}  gain_target={gain_target:.12f}"
        )

    print()
    print("raw optimizer (less well conditioned)")
    for r in (10, 20, 40, 80, 120, 160):
        phi, endpoint, global_gap = optimize(r)
        print(
            f"r={r:3d}  "
            f"r^2 phi={r*r*phi:.12f}  "
            f"r^4 gain={r**4*(endpoint-global_gap):.12f}"
        )


if __name__ == "__main__":
    main()
