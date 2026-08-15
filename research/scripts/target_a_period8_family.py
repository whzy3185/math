"""Symbolically verify the stronger period-8 infinite counterexample family."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp


TAU = (1, 1, -1, 1, -1, -1, 1, -1)


def floquet_symbol(z: sp.Symbol) -> sp.Matrix:
    period = len(TAU)
    matrix = sp.zeros(period)
    for i in range(period):
        for delta, coefficient in (
            (-2, TAU[(i - 2) % period]),
            (-1, 1),
            (1, 1),
            (2, TAU[i]),
        ):
            target = i + delta
            residue = target % period
            cell_shift = (target - residue) // period
            matrix[i, residue] += coefficient * z**cell_shift
    return matrix


def polynomial_y_c(y: sp.Symbol, c: sp.Symbol) -> sp.Expr:
    return (
        y**4
        - 16 * y**3
        + (80 - 2 * c) * y**2
        + (-128 + 16 * c) * y
        + c**2
        - 13 * c
        + 38
    )


def verify_family() -> dict[str, Any]:
    x, y, z, c, u = sp.symbols("x y z c u")
    determinant = sp.factor((x * sp.eye(8) - floquet_symbol(z)).det())
    polynomial = polynomial_y_c(y, c)
    determinant_identity = sp.simplify(
        determinant - polynomial.subs({y: x**2, c: z + z**-1})
    ) == 0

    bound = sp.Rational(1561, 200)
    shifted = sp.Poly(sp.expand(polynomial.subs({y: bound + u, c: 2})), u)
    shifted_coefficients = shifted.all_coeffs()
    shifted_positive = all(coefficient > 0 for coefficient in shifted_coefficients)
    vertex = sp.expand(y**2 - 8 * y + sp.Rational(13, 2))
    vertex_at_bound = vertex.subs(y, bound)
    vertex_right_of_interval = bool(vertex_at_bound > 2)
    vertex_increasing = bool(bound > 4)

    # Taylor lower bound at n=32 using 9<pi^2<10.
    cosine_sum_lower = (
        sp.Rational(2)
        - sp.Rational(50, 512)
        + sp.Rational(17 * 81, 24 * 256**2)
        - sp.Rational(65 * 1000, 720 * 256**3)
    )
    threshold_rational_lower = 4 + 2 * cosine_sum_lower
    if threshold_rational_lower != sp.Rational(1178731111, 150994944):
        raise AssertionError("threshold rational lower bound changed")
    threshold_above_bound = bool(threshold_rational_lower > bound)
    q = tuple(TAU[i] * TAU[(i + 1) % 8] for i in range(8))
    result = (
        determinant_identity
        and shifted_positive
        and vertex_right_of_interval
        and vertex_increasing
        and threshold_above_bound
    )
    return {
        "result": result,
        "decision": "INFINITE_COUNTEREXAMPLE_FAMILY_SYMBOLICALLY_VERIFIED" if result else "FAILED",
        "triangle_flux_period": list(TAU),
        "quadrilateral_flux_period": list(q),
        "defect_residues_mod_4": [0],
        "floquet_characteristic_polynomial": str(polynomial),
        "determinant_identity_verified": determinant_identity,
        "rational_uniform_bound_on_rho_squared": str(bound),
        "c_vertex": str(vertex),
        "c_vertex_at_bound": str(vertex_at_bound),
        "c_vertex_right_of_interval": vertex_right_of_interval,
        "c_vertex_increasing_for_y_above_bound": vertex_increasing,
        "shift_at_c_2": str(shifted.as_expr()),
        "shift_coefficients": [str(coefficient) for coefficient in shifted_coefficients],
        "shift_coefficients_positive": shifted_positive,
        "threshold_squared_rational_lower_at_n32": str(threshold_rational_lower),
        "threshold_lower_exceeds_uniform_bound": threshold_above_bound,
        "threshold_argument": (
            "Use cos(t)>1-t^2/2+t^4/24-t^6/720 for 0<t<1, "
            "9<pi^2<10, and monotonicity of rho_-(n)^2."
        ),
        "family": "every n divisible by 8 with n>=32, for alpha=+1 or -1",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify_family()
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    raise SystemExit(0 if report["result"] else 1)


if __name__ == "__main__":
    main()
