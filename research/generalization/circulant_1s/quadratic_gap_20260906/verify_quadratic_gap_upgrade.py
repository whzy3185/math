#!/usr/bin/env python3
"""Exact/symbolic checks for the 2026-09-06 quadratic-gap upgrade.

This script is an audit companion, not a replacement for the analytic proof.
It verifies:
  * the denominator factorization behind the two-Chebyshev decomposition;
  * the exact y-derivative generating-function identity;
  * the Pell-square kernel coefficients to a declared finite order;
  * an exact Sturm certificate disproving the phase-zero conjecture at s=10.

The Sturm certificate uses rational coefficients only.
"""

from __future__ import annotations

import sympy as sp


w, t, y, h = sp.symbols("w t y h")


def continuant(j: int, d: sp.Expr) -> sp.Expr:
    """D_j(d), with D_-1=0, D_0=1, D_j=d D_{j-1}-D_{j-2}."""
    if j == -1:
        return sp.Integer(0)
    if j < -1:
        raise ValueError("continuant index must be >= -1")
    prev = sp.Integer(0)
    cur = sp.Integer(1)
    for _ in range(1, j + 1):
        prev, cur = cur, sp.expand(d * cur - prev)
    return cur


def q_polynomial(r: int, h_value: sp.Rational) -> sp.Poly:
    """Exact q_r(y,h) from Proposition B of EVEN_JUMP_THEOREM_AND_PROOF.md."""
    dm = y - 4 - h_value
    dp = y - 4 + h_value

    a = continuant(r - 1, dm)
    b = continuant(r - 1, dp)
    c0 = continuant(r - 2, dm)
    d0 = continuant(r - 2, dp)
    e = continuant(r, dm)
    f = continuant(r, dp)

    q = (
        (e * f) ** 2
        - 12 * a * b * e * f
        + 38 * a**2 * b**2
        - 12 * a * b * c0 * d0
        + c0**2 * d0**2
        + (4 * h_value - 10) * b**2
        - (4 * h_value + 10) * a**2
        + 4 * a * b * (h_value**2 - 4)
        - (h_value**2 - 2)
    )
    return sp.Poly(sp.expand(q), y, domain=sp.QQ)


def check_factorization() -> None:
    delta = sp.symbols("delta")
    A = 1 - 6 * w + w**2
    xp = 6 + t / 2 + delta / 2
    xm = 6 + t / 2 - delta / 2

    lhs = A**2 - t * w * (1 + w) ** 2
    rhs = (1 - xp * w + w**2) * (1 - xm * w + w**2)
    remainder = sp.expand(lhs - rhs).subs(delta**2, t * (t + 32))
    assert sp.expand(remainder) == 0


def check_derivative_identity() -> None:
    A = 1 - 6 * w + w**2
    dm = y - 4 - h
    dp = y - 4 + h
    P = (
        1
        - dm * dp * w
        + (dm**2 + dp**2 - 2) * w**2
        - dm * dp * w**3
        + w**4
    )
    S_general = (1 - w**2) * A / P

    lhs = sp.diff(S_general, y).subs(y, 8)
    t_at_h = 4 - h**2
    P8 = sp.expand(A**2 - t_at_h * w * (1 + w) ** 2)
    S8 = (1 - w**2) * A / P8
    kernel = (1 - w) / ((1 + w) * A)
    rhs = 8 * w * kernel * S8**2

    assert sp.factor(lhs - rhs) == 0


def pell_numbers(n: int) -> list[int]:
    vals = [0, 1]
    while len(vals) <= n:
        vals.append(2 * vals[-1] + vals[-2])
    return vals[: n + 1]


def check_pell_kernel(order: int = 20) -> None:
    A = 1 - 6 * w + w**2
    kernel = (1 - w) / ((1 + w) * A)
    coeffs = [sp.expand(sp.series(kernel, w, 0, order + 1).removeO()).coeff(w, k)
              for k in range(order)]
    pell = pell_numbers(order + 1)
    expected = [sp.Integer(pell[k + 1] ** 2) for k in range(order)]
    assert coeffs == expected


def check_exact_phase_slip() -> None:
    # s=10, so r=5.
    r = 5
    h_endpoint = sp.Rational(2, 1)
    h_interior = sp.Rational(19997, 10000)
    separator = sp.Rational(317, 40)  # 7.925 exactly

    q_endpoint = q_polynomial(r, h_endpoint)
    q_interior = q_polynomial(r, h_interior)

    # Exact Sturm counts over QQ.  At h=2 there is no squared eigenvalue above
    # 7.925, whereas at the interior phase there is exactly one.
    endpoint_above = sp.count_roots(q_endpoint.as_expr(), separator, sp.oo)
    interior_above = sp.count_roots(q_interior.as_expr(), separator, sp.oo)

    assert endpoint_above == 0
    assert interior_above == 1

    print("exact phase-slip certificate:")
    print(f"  roots q_5(y,2) above 317/40      = {endpoint_above}")
    print(f"  roots q_5(y,19997/10000) above = {interior_above}")


def main() -> None:
    check_factorization()
    check_derivative_identity()
    check_pell_kernel()
    check_exact_phase_slip()
    print("all declared quadratic-gap upgrade checks passed")


if __name__ == "__main__":
    main()
