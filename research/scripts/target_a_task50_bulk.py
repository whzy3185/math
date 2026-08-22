"""Exact symbolic and rational certificates for Task 50 bulk hyperbolicity."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task50" / "certificates"
TAU = (1, 1, -1, 1, -1, -1, 1, -1)


def text(value: sp.Expr | Fraction) -> str:
    return str(value).replace("**", "^")


def transfer(index: int, lam: sp.Symbol) -> sp.Matrix:
    a = TAU[index % 8]
    b = TAU[(index - 2) % 8]
    return sp.Matrix([[-a, a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])


def monodromy(lam: sp.Symbol) -> sp.Matrix:
    product = sp.eye(4)
    for index in range(8):
        product = transfer(index, lam) * product
    return sp.simplify(product)


def rational(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def interval_certificate(name: str, left: Fraction, right: Fraction, q_slow: Fraction) -> dict[str, Any]:
    y = sp.symbols("y")
    h = 2 * y**2 - 16 * y + 13
    discriminant = -12 * y**2 + 96 * y + 17
    l, r = rational(left), rational(right)
    q = rational(q_slow)
    q_fast = sp.Rational(1, 8)

    h_left = sp.factor(h.subs(y, l))
    d_left = sp.factor(discriminant.subs(y, l))
    d_right = sp.factor(discriminant.subs(y, r))
    slow_threshold = sp.factor(q + 1 / q)
    slow_margin_base = sp.factor(h_left - 2 * slow_threshold)
    slow_square_margin = sp.factor(slow_margin_base**2 - d_left)
    fast_threshold = sp.factor(q_fast + 1 / q_fast)
    fast_margin_base = sp.factor(2 * fast_threshold - h_left)
    fast_square_margin = sp.factor(d_right - fast_margin_base**2)

    checks = {key: bool(value) for key, value in {
        "ordered_interval": l < r,
        "inside_eta_8": sp.Rational(781, 100) < l and r < 8,
        "h_increasing": 4 * l - 16 > 0,
        "discriminant_decreasing": 96 - 24 * l < 0,
        "discriminant_positive": d_right > 0,
        "slow_base_positive": slow_margin_base > 0,
        "slow_square_margin_positive": slow_square_margin > 0,
        "fast_base_positive": fast_margin_base > 0,
        "fast_square_margin_positive": fast_square_margin > 0,
        "q_fast_below_q_slow": 0 < q_fast < q < 1,
    }.items()}
    if not all(checks.values()):
        raise AssertionError(f"{name} rational hyperbolicity certificate failed: {checks}")
    return {
        "family": name,
        "y_interval": [str(l), str(r)],
        "q_fast": str(q_fast),
        "q_slow": str(q),
        "unstable_lower_bounds": [str(1 / q), str(1 / q_fast)],
        "h_left": str(h_left),
        "discriminant_left": str(d_left),
        "discriminant_right": str(d_right),
        "slow_test": {
            "target_w": str(slow_threshold),
            "positive_base": str(slow_margin_base),
            "squared_margin": str(slow_square_margin),
            "conclusion": "w_minus > q_slow + q_slow^(-1)",
        },
        "fast_test": {
            "target_w": str(fast_threshold),
            "positive_base": str(fast_margin_base),
            "squared_margin": str(fast_square_margin),
            "conclusion": "w_plus > q_fast + q_fast^(-1)",
        },
        "root_structure": "four distinct positive real roots; two stable and two reciprocal unstable roots",
        "checks": checks,
    }


def run() -> dict[str, Any]:
    lam, y, z, w = sp.symbols("lambda y z w")
    matrix = monodromy(lam)
    characteristic = sp.Poly(matrix.charpoly(z).as_expr(), z)
    expected = sp.Poly(
        z**4
        + (-2 * y**2 + 16 * y - 13) * z**3
        + (y**4 - 16 * y**3 + 80 * y**2 - 128 * y + 40) * z**2
        + (-2 * y**2 + 16 * y - 13) * z
        + 1,
        z,
    )
    even_characteristic = sp.Poly(characteristic.as_expr().subs(lam**2, y), z)
    if even_characteristic != expected:
        raise AssertionError("exact M8 characteristic polynomial mismatch")

    a = -2 * y**2 + 16 * y - 13
    b = y**4 - 16 * y**3 + 80 * y**2 - 128 * y + 40
    reduced = sp.expand(w**2 + a * w + b - 2)
    lifted_reduction = sp.cancel(z**2 * reduced.subs(w, z + 1 / z))
    if sp.expand(lifted_reduction - expected.as_expr()) != 0:
        raise AssertionError("palindromic reduction mismatch")
    discriminant = sp.factor(a**2 - 4 * (b - 2))
    if discriminant != -12 * y**2 + 96 * y + 17:
        raise AssertionError("reduced discriminant mismatch")

    # eta < 781/100 follows from sqrt(5)<1129/500 and
    # 10+2*(1129/500)<(381/100)^2.
    eta_checks = {key: bool(value) for key, value in {
        "sqrt5_upper": sp.Rational(1129, 500) ** 2 > 5,
        "outer_radicand_upper": 10 + 2 * sp.Rational(1129, 500) < sp.Rational(381, 100) ** 2,
    }.items()}
    if not all(eta_checks.values()):
        raise AssertionError("eta rational upper bound failed")

    certificates = {
        "status": "BULK_HYPERBOLICITY_PROVED",
        "tau_cell": list(TAU),
        "M8_entries": [[text(sp.factor(value)) for value in matrix.row(row)] for row in range(4)],
        "characteristic_polynomial": text(expected.as_expr()),
        "palindromic_reduction": text(reduced),
        "reduced_discriminant": text(discriminant),
        "w_branches": [
            "(2*y^2-16*y+13-sqrt(-12*y^2+96*y+17))/2",
            "(2*y^2-16*y+13+sqrt(-12*y^2+96*y+17))/2",
        ],
        "eta_upper_bound": "eta < 781/100",
        "eta_checks": eta_checks,
        "G6": interval_certificate("G6", Fraction(1581, 200), Fraction(3953, 500), Fraction(9, 25)),
        "G10": interval_certificate("G10", Fraction(7977, 1000), Fraction(3989, 500), Fraction(4, 15)),
        "proof_boundary": "All checks use exact symbolic or rational arithmetic; no floating root is an acceptance input.",
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "bulk_symbolic.json", {
        "tau_cell": certificates["tau_cell"],
        "M8_entries": certificates["M8_entries"],
        "characteristic_polynomial": certificates["characteristic_polynomial"],
        "palindromic_reduction": certificates["palindromic_reduction"],
        "reduced_discriminant": certificates["reduced_discriminant"],
    })
    write_json(OUTPUT / "bulk_hyperbolicity_certificates.json", certificates)
    print(json.dumps({
        "status": certificates["status"],
        "G6_interval": certificates["G6"]["y_interval"],
        "G10_interval": certificates["G10"]["y_interval"],
        "q6": certificates["G6"]["q_slow"],
        "q10": certificates["G10"]["q_slow"],
    }, indent=2))
    return certificates


if __name__ == "__main__":
    run()
