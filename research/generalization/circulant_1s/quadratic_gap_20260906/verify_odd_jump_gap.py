#!/usr/bin/env python3
"""Verification helpers for ODD_JUMP_SHARP_GAP.md.

This script is not a substitute for the analytic proof.  It checks the exact
Chebyshev derivative identity for a finite list of odd jumps and numerically
verifies the unique critical point, the O(s^-3) phase window, and the sharp
gap bounds.
"""

from __future__ import annotations

import math
import sympy as sp


def derivative(theta: float, s: int) -> float:
    return math.sin(2.0 * theta) - s * math.sin(2.0 * s * theta)


def gap_at(theta: float, s: int) -> float:
    return 4.0 * (math.sin(theta) ** 2 + math.cos(s * theta) ** 2)


def critical_phase(s: int, iterations: int = 100) -> float:
    assert s >= 3 and s % 2 == 1
    lo = math.pi / (4.0 * s)
    hi = math.pi / (2.0 * s)
    assert derivative(lo, s) < 0.0
    assert derivative(hi, s) > 0.0
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        if derivative(mid, s) < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def exact_chebyshev_checks() -> None:
    c = sp.symbols("c")
    for s in range(3, 16, 2):
        p = 4 - 2 * c + 2 * sp.chebyshevt(s, c)
        rhs = -2 + 2 * s * sp.chebyshevu(s - 1, c)
        assert sp.expand(sp.diff(p, c) - rhs) == 0


def numerical_checks() -> None:
    rows = []
    for s in list(range(3, 32, 2)) + [51, 101, 201]:
        theta = critical_phase(s)
        eps = math.pi / (2.0 * s) - theta
        g = gap_at(theta, s)
        lower = 4.0 * math.sin(
            math.pi / (2.0 * s) - math.pi**2 / (4.0 * s**3)
        ) ** 2
        upper = 4.0 * math.sin(math.pi / (2.0 * s)) ** 2

        assert 0.0 < eps <= math.pi**2 / (4.0 * s**3) * (1 + 1e-12)
        assert lower <= g * (1 + 1e-12)
        assert g <= upper * (1 + 1e-12)
        assert g > 4.0 / (1.0 + s * s) * (1 - 1e-12)

        rows.append((s, theta, eps, g, s * s * g))

    for row in rows:
        print(
            f"s={row[0]:3d} theta={row[1]:.15g} "
            f"epsilon={row[2]:.6e} gap={row[3]:.15g} "
            f"s^2 gap={row[4]:.12f}"
        )


def formal_asymptotic_check() -> None:
    """Check the coefficients recorded as the next refinement target."""
    t = sp.symbols("t", positive=True)
    a = -sp.pi / 2
    b = sp.pi / 2 + sp.pi**3 / 12

    theta = sp.pi * t / 2 + a * t**3 + b * t**5

    # If s=1/t, then 2 s theta = pi + 2 a t^2 + 2 b t^4.
    crit = sp.sin(2 * theta) + sp.sin(2 * a * t**2 + 2 * b * t**4) / t
    crit_series = sp.series(crit, t, 0, 5).removeO().expand()
    assert sp.expand(crit_series) == 0

    # cos(s theta)^2 = sin(a t^2 + b t^4)^2.
    gap = 4 * (
        sp.sin(theta) ** 2 + sp.sin(a * t**2 + b * t**4) ** 2
    )
    series = sp.series(gap, t, 0, 6).removeO().expand()
    target = (
        sp.pi**2 * t**2
        - (sp.pi**2 + sp.pi**4 / 12) * t**4
    )
    assert sp.expand(series - target) == 0


if __name__ == "__main__":
    exact_chebyshev_checks()
    formal_asymptotic_check()
    numerical_checks()
    print("odd-jump sharp-gap verification passed")
