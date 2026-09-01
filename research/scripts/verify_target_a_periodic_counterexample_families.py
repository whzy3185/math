"""Exact Floquet certificates for the auxiliary periodic counterexample families."""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


FAMILIES = {
    10: {
        "tau": (1, 1, -1, 1, -1, -1, 1, -1, 1, -1),
        "start": 50,
        "cap": Fraction(198, 25),
        "mode": "concave_endpoints",
    },
    12: {
        "tau": (1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1),
        "start": 60,
        "cap": Fraction(143, 18),
        "mode": "convex_vertex_right",
    },
    14: {
        "tau": (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1),
        "start": 112,
        "cap": Fraction(399, 50),
        "mode": "concave_endpoints",
    },
    18: {
        "tau": (1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1),
        "start": 54,
        "cap": Fraction(5782, 729),
        "mode": "concave_endpoints",
    },
    22: {
        "tau": (1, -1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1),
        "start": 66,
        "cap": Fraction(8662, 1089),
        "mode": "concave_endpoints",
    },
}


def floquet_matrix(tau: tuple[int, ...], z: sp.Symbol) -> sp.Matrix:
    period = len(tau)
    matrix = sp.zeros(period)
    for output in range(period):
        for displacement, coefficient in (
            (-2, tau[(output - 2) % period]),
            (-1, 1),
            (1, 1),
            (2, tau[output]),
        ):
            source = output + displacement
            cell, residue = divmod(source, period)
            matrix[output, residue] += coefficient * z**cell
    return matrix


def laurent_to_c(expression: sp.Expr, z: sp.Symbol, c: sp.Symbol) -> sp.Expr:
    coefficients: dict[int, sp.Expr] = {}
    for term in sp.Add.make_args(sp.expand(expression)):
        powers = term.as_powers_dict()
        exponent = int(powers.get(z, 0))
        coefficients[exponent] = coefficients.get(exponent, 0) + term / z**exponent
    if not all(sp.simplify(coefficients.get(k, 0) - coefficients.get(-k, 0)) == 0 for k in coefficients):
        raise AssertionError("Floquet determinant is not reciprocal in z")
    chebyshev = {0: sp.Integer(2), 1: c}
    for degree in range(2, max(abs(key) for key in coefficients) + 1):
        chebyshev[degree] = sp.expand(c * chebyshev[degree - 1] - chebyshev[degree - 2])
    return sp.factor(
        coefficients.get(0, 0)
        + sum(coefficients.get(k, 0) * chebyshev[k] for k in range(1, max(abs(key) for key in coefficients) + 1))
    )


def threshold_lower(n: int) -> Fraction:
    return Fraction(8) - Fraction(200, n * n)


def family_certificate(period: int, data: dict[str, object]) -> dict[str, object]:
    x, y, z, c, u = sp.symbols("x y z c u")
    tau = data["tau"]
    determinant = sp.factor((x * sp.eye(period) - floquet_matrix(tau, z)).det())
    if sp.simplify(determinant.subs(x, -x) - determinant) != 0:
        raise AssertionError(f"period {period}: characteristic polynomial is not even")
    polynomial = laurent_to_c(determinant.subs(x**2, y), z, c)
    cap = sp.Rational(data["cap"].numerator, data["cap"].denominator)
    endpoint_polynomials = {
        endpoint: sp.Poly(sp.expand(polynomial.subs({y: cap + u, c: endpoint})), u)
        for endpoint in (-2, 2)
    }
    endpoint_positive = all(
        all(coefficient > 0 for coefficient in item.all_coeffs())
        for item in endpoint_polynomials.values()
    )
    if not endpoint_positive:
        raise AssertionError(f"period {period}: endpoint positivity failed")

    mode = data["mode"]
    if mode == "concave_endpoints":
        curvature = sp.diff(polynomial, c, 2)
        if curvature != -2:
            raise AssertionError(f"period {period}: expected concavity")
        global_certificate = "concave_in_c; endpoints_positive"
    elif mode == "convex_vertex_right":
        vertex = -sp.diff(polynomial, c).subs(c, 0) / 2
        derivative = sp.diff(vertex, y)
        derivative_shift = sp.Poly(sp.expand(derivative.subs(y, cap + u)), u)
        if not (
            sp.simplify(vertex.subs(y, cap) - 2) > 0
            and all(coefficient > 0 for coefficient in derivative_shift.all_coeffs())
        ):
            raise AssertionError("period 12: vertex location proof failed")
        global_certificate = "convex_in_c; vertex_above_2; endpoint_c_equals_2_positive"
    else:
        raise AssertionError("unknown positivity mode")

    start = int(data["start"])
    if not (Fraction(data["cap"]) <= threshold_lower(start)):
        raise AssertionError(f"period {period}: threshold comparison failed")
    return {
        "period": period,
        "start": start,
        "cap": str(data["cap"]),
        "floquet_polynomial": str(polynomial),
        "c_degree": sp.degree(polynomial, c),
        "global_positivity_certificate": global_certificate,
        "endpoint_shift_polynomials": {str(key): str(value.as_expr()) for key, value in endpoint_polynomials.items()},
        "threshold_lower_at_start": str(threshold_lower(start)),
    }


def verify() -> dict[str, object]:
    certificates = [family_certificate(period, data) for period, data in FAMILIES.items()]
    return {
        "status": "PERIODIC_FAMILY_FLOQUET_VERIFY_PASS",
        "families": certificates,
    }


if __name__ == "__main__":
    print(verify())
