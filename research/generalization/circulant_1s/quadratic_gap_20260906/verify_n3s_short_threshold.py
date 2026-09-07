#!/usr/bin/env python3
"""Exact Sylvester certificates for the two short odd N=3s cases.

This script certifies explicit sub-sqrt(8) signings for C_9(1,3) and
C_15(1,5).  It uses the Hamilton-gauge finite model

    A = T + T^{-1} + M_tau T^s + T^{-s} M_tau,
    T^N = alpha I,

and checks positive definiteness of C = 8 I - A^2 by Sylvester's criterion.
All displayed leading principal minors are exact integers.

Together with the analytic antiperiodic alternating construction for even s
and N3S_GLOBAL_OBSTRUCTION.md for odd s>=7, these two certificates complete
the threshold classification on the resonance line N=3s.
"""

from __future__ import annotations

import sympy as sp


CASES = {
    (9, 3): {
        "tau": (-1, +1, -1, -1, +1, -1, +1, -1, +1),
        "alpha": +1,
        "expected_minors": (4, 16, 60, 209, 722, 2508, 5746, 15993, 47304),
    },
    (15, 5): {
        "tau": (+1, -1, +1, -1, +1, -1, +1, -1, -1, +1, -1, +1, -1, +1, -1),
        "alpha": +1,
        "expected_minors": (
            4, 16, 60, 225, 840, 2911, 10082, 34080, 118048,
            408588, 1166430, 3383853, 6382980, 4663008, 8636544,
        ),
    },
}


def adjacency(N: int, s: int, tau: tuple[int, ...], alpha: int) -> sp.Matrix:
    A = sp.zeros(N, N)
    for i in range(N):
        for step, coeff in (
            (+1, 1),
            (-1, 1),
            (+s, tau[i]),
            (-s, tau[(i - s) % N]),
        ):
            d = i + step
            j = d % N
            wrap = alpha if (d < 0 or d >= N) else 1
            A[i, j] += coeff * wrap
    assert A == A.T
    return A


def leading_principal_minors(C: sp.Matrix) -> tuple[int, ...]:
    return tuple(
        int(C[:k, :k].det(method="domain-ge"))
        for k in range(1, C.rows + 1)
    )


def main() -> None:
    for (N, s), data in CASES.items():
        A = adjacency(N, s, data["tau"], data["alpha"])
        C = 8 * sp.eye(N) - A * A
        minors = leading_principal_minors(C)
        assert minors == data["expected_minors"]
        assert all(d > 0 for d in minors)

        q = tuple(data["tau"][i] * data["tau"][(i + 1) % N] for i in range(N))
        defects = tuple(i for i, x in enumerate(q) if x == +1)

        print(f"C_{N}(1,{s}): alpha={data['alpha']}, positive Q defects={defects}")
        print(f"  leading principal minors: {minors}")
        print("  Sylvester: 8I-A^2 is positive definite, hence rho(A)^2 < 8")

    print("short N=3s threshold certificates passed")


if __name__ == "__main__":
    main()
