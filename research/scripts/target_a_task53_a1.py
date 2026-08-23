"""Exact producer for Task 53 Gate A1 global bulk hyperbolicity."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task53" / "certificates"
C6_UPPER = sp.Rational(7905369311620328, 10**15)


def build_certificate() -> dict[str, Any]:
    y, z, w = sp.symbols("y z w")
    a = -2 * y**2 + 16 * y - 13
    b = y**4 - 16 * y**3 + 80 * y**2 - 128 * y + 40
    chi = sp.Poly(z**4 + a * z**3 + b * z**2 + a * z + 1, z)
    reduced = sp.Poly(w**2 + a * w + b - 2, w)
    lifted = sp.expand(z**2 * reduced.as_expr().subs(w, z + 1 / z))
    discriminant_w = sp.factor(sp.discriminant(reduced.as_expr(), w))
    plus_endpoint = sp.factor(reduced.as_expr().subs(w, 2))
    minus_endpoint = sp.factor(reduced.as_expr().subs(w, -2))
    discriminant_z = sp.factor(sp.discriminant(chi.as_expr(), z))

    eta = 4 + sp.sqrt(10 + 2 * sp.sqrt(5))
    critical = 4 + sp.sqrt(627) / 6
    repeated_w = sp.simplify(-a.subs(y, critical) / 2)
    base = sp.factor((-a - 4).subs(y, C6_UPPER))
    square_margin = sp.factor(((-a - 4) ** 2 - discriminant_w).subs(y, C6_UPPER))

    interval_checks = {
        "c6_upper_above_eta": bool(C6_UPPER > eta),
        "c6_upper_below_critical": bool(C6_UPPER < critical),
        "critical_below_16": bool(critical < 16),
        "w_roots_real_at_c6_upper": bool(discriminant_w.subs(y, C6_UPPER) > 0),
        "smaller_w_root_above_2_base": bool(base > 0),
        "smaller_w_root_above_2_square": bool(square_margin > 0),
        "critical_repeated_w_above_2": bool(repeated_w > 2),
    }

    factors = sp.factor_list(discriminant_z, y)[1]
    critical_records = []
    left, right = C6_UPPER, sp.Integer(16)
    for factor, multiplicity in factors:
        polynomial = sp.Poly(factor, y)
        count = int(polynomial.count_roots(left, right))
        critical_records.append({
            "factor": str(factor),
            "multiplicity_in_z_discriminant": int(multiplicity),
            "degree": int(polynomial.degree()),
            "roots_in_closed_task_interval": count,
        })

    checks = {
        "reciprocal_coefficients": chi.all_coeffs() == list(reversed(chi.all_coeffs())),
        "palindromic_reduction": sp.Poly(lifted, z) == chi,
        "w_discriminant": discriminant_w == -12 * y**2 + 96 * y + 17,
        "plus_endpoint_is_eta_polynomial": sp.Poly(plus_endpoint, y) == sp.Poly(sp.minpoly(eta, y), y),
        "minus_endpoint_factorization": minus_endpoint == (y**2 - 12 * y + 34) * (y**2 - 4 * y + 2),
        "z_discriminant_complete": discriminant_z == (
            (y**2 - 12 * y + 34)
            * (y**2 - 4 * y + 2)
            * (12 * y**2 - 96 * y - 17) ** 2
            * plus_endpoint
        ),
        "only_one_discriminant_root_in_interval": sum(row["roots_in_closed_task_interval"] for row in critical_records) == 1,
        "critical_energy_exact": sp.simplify(discriminant_w.subs(y, critical)) == 0,
        "critical_w_exact": repeated_w == sp.Rational(95, 12),
        **interval_checks,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    return {
        "status": "GATE_A1_PASS",
        "evidence": "PROVED",
        "energy_interval": [str(C6_UPPER), "16"],
        "characteristic_polynomial": str(chi.as_expr()),
        "reciprocal_reduction": str(reduced.as_expr()),
        "w_discriminant": str(discriminant_w),
        "w_plus_2_polynomial": str(plus_endpoint),
        "w_minus_2_polynomial": str(minus_endpoint),
        "z_discriminant": str(discriminant_z),
        "eta": str(eta),
        "critical_energy": str(critical),
        "critical_energy_decimal": str(sp.N(critical, 30)),
        "critical_repeated_w": str(repeated_w),
        "critical_records": critical_records,
        "root_geometry": [
            {
                "interval": f"[{C6_UPPER}, {critical})",
                "w_type": "two distinct real roots, both greater than 2",
                "z_type": "four distinct positive real reciprocal roots",
                "stable_dimension": 2,
                "unstable_dimension": 2,
            },
            {
                "interval": f"{{{critical}}}",
                "w_type": "double root 95/12",
                "z_type": "one stable and one unstable positive root, each algebraic multiplicity two",
                "stable_dimension": 2,
                "unstable_dimension": 2,
            },
            {
                "interval": f"({critical}, 16]",
                "w_type": "nonreal conjugate pair",
                "z_type": "reciprocal-conjugate quadruple off the unit circle",
                "stable_dimension": 2,
                "unstable_dimension": 2,
            },
        ],
        "unit_circle_argument": (
            "For |z|=1, w=z+z^-1 lies in [-2,2]. At c6_upper both real w roots exceed 2. "
            "No root can enter [-2,2] before the sole w-discriminant event because the endpoint "
            "polynomials have no root above eta. At the event w=95/12; afterwards w is nonreal."
        ),
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "bulk_global_hyperbolicity.json", payload)
    print(json.dumps({"status": payload["status"], "critical": payload["critical_energy"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()
