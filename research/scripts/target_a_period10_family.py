"""Symbolically verify the period-10 infinite counterexample family."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import sympy as sp


TAU = (1, 1, -1, 1, -1, -1, 1, -1, 1, -1)


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
        y**5
        - 20 * y**4
        + 142 * y**3
        - (426 + c) * y**2
        + (485 + 10 * c) * y
        - c**2
        - 9 * c
        - 114
    )


def verify_family() -> dict[str, Any]:
    x, y, z, c, u = sp.symbols("x y z c u")
    determinant = sp.factor((x * sp.eye(10) - floquet_symbol(z)).det())
    polynomial = polynomial_y_c(y, c)
    determinant_identity = sp.simplify(
        determinant - polynomial.subs({y: x**2, c: z + z**-1})
    ) == 0

    bound = sp.Rational(198, 25)
    endpoint_data = []
    endpoints_positive = True
    for endpoint in (-2, 2):
        shifted = sp.Poly(sp.expand(polynomial.subs({y: bound + u, c: endpoint})), u)
        coefficients = shifted.all_coeffs()
        positive = all(coefficient > 0 for coefficient in coefficients)
        endpoints_positive = endpoints_positive and positive
        endpoint_data.append(
            {
                "c": endpoint,
                "shifted_polynomial": str(shifted.as_expr()),
                "coefficients": [str(coefficient) for coefficient in coefficients],
                "all_coefficients_positive": positive,
            }
        )

    concavity = sp.diff(polynomial, c, 2) == -2
    q = tuple(TAU[i] * TAU[(i + 1) % 10] for i in range(10))
    result = determinant_identity and endpoints_positive and concavity
    return {
        "result": result,
        "decision": "INFINITE_COUNTEREXAMPLE_FAMILY_SYMBOLICALLY_VERIFIED" if result else "FAILED",
        "triangle_flux_period": list(TAU),
        "quadrilateral_flux_period": list(q),
        "defect_residues_mod_10": [i for i, value in enumerate(q) if value == 1],
        "floquet_characteristic_polynomial": str(polynomial),
        "determinant_identity_verified": determinant_identity,
        "second_derivative_in_c": str(sp.diff(polynomial, c, 2)),
        "concave_on_c_interval": concavity,
        "rational_uniform_bound_on_rho_squared": str(bound),
        "endpoint_shift_certificates": endpoint_data,
        "threshold_argument": (
            "For n>=50, rho_-(n)^2 is increasing; at n=50, "
            "cos(t)>1-t^2/2 and pi^2<10 give rho_-(50)^2>198/25."
        ),
        "family": "every n divisible by 10 with n>=50, for alpha=+1 or -1",
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
