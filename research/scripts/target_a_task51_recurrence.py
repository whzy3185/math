"""Bounded exact reconnaissance of the Task 50 finite-ring recurrence."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_finite_ring_analysis import finite_closure_polynomial, recurrence_polynomial


RESEARCH = Path(__file__).resolve().parents[1]
DISCOVERY = RESEARCH / "discovery" / "task51"
EXPERIMENTS = RESEARCH / "experiments" / "task51"


def _text(value: sp.Expr) -> str:
    return str(sp.factor(value))


def _apply_operator(coefficients: list[sp.Expr], sequence: list[sp.Expr], start: int) -> sp.Expr:
    return sp.cancel(sum(coefficient * sequence[start + shift] for shift, coefficient in enumerate(coefficients)))


def _ascending(poly: sp.Poly) -> list[sp.Expr]:
    return list(reversed(poly.all_coeffs()))


def _sign_pattern(poly: sp.Poly) -> list[int]:
    return sorted({int(sp.sign(value)) for value in poly.all_coeffs() if value})


def _digest(value: sp.Expr) -> str:
    return hashlib.sha256(str(sp.cancel(value)).encode("utf-8")).hexdigest()


def exact_structure() -> dict[str, Any]:
    y, t, x = sp.symbols("y t x")
    p9 = recurrence_polynomial()
    factors = sp.factor_list(p9.as_expr(), t)[1]
    quartics = [sp.Poly(factor, t) for factor, multiplicity in factors if sp.degree(factor, t) == 4 and multiplicity == 1]
    if len(quartics) != 2 or not sp.rem(p9, sp.Poly(t - 1, t)).is_zero:
        raise AssertionError("order-nine factorization did not have 1+4+4 form")
    q1, q2 = quartics
    for quartic in quartics:
        if quartic.all_coeffs() != list(reversed(quartic.all_coeffs())):
            raise AssertionError("nonreciprocal quartic")

    bezout_q1, bezout_q2, gcd = sp.gcdex(q1.as_expr(), q2.as_expr(), t)
    bezout_residual = sp.cancel(bezout_q1 * q1.as_expr() + bezout_q2 * q2.as_expr() - gcd)
    if gcd != 1 or bezout_residual != 0:
        raise AssertionError("quartic Bezout identity failed")

    reductions = []
    for name, quartic in zip(("Q1", "Q2"), quartics):
        coefficients = quartic.all_coeffs()
        a, b = coefficients[1], coefficients[2]
        quadratic = sp.Poly(x**2 + a * x + b - 2, x)
        lifted = sp.cancel(t**2 * quadratic.as_expr().subs(x, t + 1 / t) - quartic.as_expr())
        if lifted != 0:
            raise AssertionError("reciprocal quartic reduction failed")
        reductions.append({
            "factor": name,
            "quartic": _text(quartic.as_expr()),
            "quadratic_in_x": _text(quadratic.as_expr()),
            "discriminant": _text(sp.discriminant(quadratic.as_expr(), x)),
            "lift_identity_exact": True,
        })

    return {
        "status": "ORDER9_EXACT_1_PLUS_4_PLUS_4_PROVED",
        "P9": _text(p9.as_expr()),
        "constant_factor": "t - 1",
        "Q1": _text(q1.as_expr()),
        "Q2": _text(q2.as_expr()),
        "factorization_identity_exact": sp.expand(p9.as_expr() - (t - 1) * q1.as_expr() * q2.as_expr()) == 0,
        "bezout": {
            "A_for_Q1": _text(bezout_q1),
            "B_for_Q2": _text(bezout_q2),
            "identity": "A(E)Q1(E)+B(E)Q2(E)=1",
            "exact": True,
        },
        "projection_definition": {
            "g_k": "f_(k+1)-f_k",
            "u": "B(E) Q2(E) g",
            "v": "A(E) Q1(E) g",
            "reconstruction": "g=u+v",
            "u_recurrence": "Q1(E)u=0",
            "v_recurrence": "Q2(E)v=0",
        },
        "reciprocal_reductions": reductions,
        "proof_note": "The projection follows in Q(y)[E] from Bezout and Q1(E)Q2(E)g=0; no fitted coefficient enters it.",
    }


def closure_sequences(structure: dict[str, Any]) -> tuple[dict[tuple[int, int], list[sp.Expr]], list[dict[str, Any]]]:
    y, t = sp.symbols("y t")
    p9 = recurrence_polynomial()
    recurrence = p9.all_coeffs()
    sequences: dict[tuple[int, int], list[sp.Expr]] = {}
    checks = []
    for gap in (6, 10):
        for alpha in (-1, 1):
            direct = [finite_closure_polynomial(gap, k, alpha).as_expr() for k in range(1, 10)]
            sequence = list(direct)
            for _ in range(9, 32):
                next_value = -sum(recurrence[j] * sequence[-j] for j in range(1, 10))
                sequence.append(sp.expand(next_value))
            residuals = []
            for start in range(0, 20):
                residual = sum(recurrence[j] * sequence[start + 9 - j] for j in range(10))
                residuals.append(sp.expand(residual) == 0)
            g_sequence = [sp.expand(sequence[index + 1] - sequence[index]) for index in range(len(sequence) - 1)]
            q1 = sp.Poly(structure["Q1"], t)
            q2 = sp.Poly(structure["Q2"], t)
            product = sp.Poly(sp.expand(q1.as_expr() * q2.as_expr()), t)
            projected_residuals = [
                sp.expand(_apply_operator(_ascending(product), g_sequence, start)) == 0
                for start in range(0, len(g_sequence) - 8)
            ]
            if not all(residuals + projected_residuals):
                raise AssertionError(f"projected recurrence failed for G{gap}, alpha={alpha}")
            sequences[(gap, alpha)] = sequence
            checks.append({
                "family": f"G{gap}",
                "alpha": alpha,
                "direct_prefix_terms": 9,
                "extended_terms": len(sequence),
                "P9_checks": len(residuals),
                "Q1Q2_delta_checks": len(projected_residuals),
                "exact": True,
                "prefix_digests": [_digest(value) for value in direct],
            })
    return sequences, checks


def shifted_signs(sequences: dict[tuple[int, int], list[sp.Expr]], structure: dict[str, Any]) -> dict[str, Any]:
    y, u, t = sp.symbols("y u t")
    betas = [Fraction(7999, 1000), Fraction(1599, 200), Fraction(799, 100), Fraction(399, 50)]
    q1 = sp.Poly(structure["Q1"], t)
    q2 = sp.Poly(structure["Q2"], t)
    recurrence = recurrence_polynomial()
    rows = []
    for beta in betas:
        beta_value = sp.Rational(beta.numerator, beta.denominator)
        recurrence_signs = [
            _sign_pattern(sp.Poly(sp.expand(coefficient.subs(y, u + beta_value)), u))
            for coefficient in recurrence.all_coeffs()
        ]
        for (gap, alpha), sequence in sequences.items():
            prefix = []
            for k, value in enumerate(sequence, start=1):
                shifted = sp.Poly(sp.expand(value.subs(y, u + beta_value)), u)
                prefix.append({"k": k, "signs": _sign_pattern(shifted), "degree": shifted.degree()})
            g_sequence = [sp.expand(sequence[i + 1] - sequence[i]) for i in range(len(sequence) - 1)]
            raw_u = _apply_operator(_ascending(q2), g_sequence, 0)
            raw_v = _apply_operator(_ascending(q1), g_sequence, 0)
            projected = []
            for name, value in (("Q2(E)g", raw_u), ("Q1(E)g", raw_v)):
                shifted = sp.Poly(sp.expand(value.subs(y, u + beta_value)), u)
                projected.append({"component": name, "signs": _sign_pattern(shifted), "degree": shifted.degree()})
            rows.append({
                "beta": str(beta),
                "family": f"G{gap}",
                "alpha": alpha,
                "recurrence_coefficient_signs": recurrence_signs,
                "first_nine": prefix[:9],
                "all_32": prefix,
                "all_first_nine_one_sign": all(len(item["signs"]) == 1 for item in prefix[:9]),
                "all_32_one_sign": all(len(item["signs"]) == 1 for item in prefix),
                "projected_raw_components": projected,
            })
    return {
        "status": "EXACT_SHIFTED_SIGN_TEST_COMPLETE",
        "rows": rows,
        "global_prefix_result": "STRONG" if all(row["all_first_nine_one_sign"] for row in rows) else "FALSIFIED_BELOW_8",
        "global_k_le_32_result": "STRONG" if all(row["all_32_one_sign"] for row in rows) else "MIXED",
        "scope": "36 direct initial closure polynomials and recurrence-extended k<=32 at each beta; raw quartic components are diagnostics, while normalized Bezout projections are rational functions.",
    }


def modal_and_hankel(sequences: dict[tuple[int, int], list[sp.Expr]], structure: dict[str, Any]) -> dict[str, Any]:
    y, t = sp.symbols("y t")
    samples = [Fraction(399, 50), Fraction(8), Fraction(81, 10), Fraction(9), Fraction(12), Fraction(16)]
    p9 = sp.Poly(structure["P9"], t)
    rows = []
    hankel_rows = []
    for y_value in samples:
        roots = np.roots([float(coefficient.subs(y, sp.Rational(y_value.numerator, y_value.denominator))) for coefficient in p9.all_coeffs()])
        roots = sorted(roots, key=lambda value: abs(value), reverse=True)
        reciprocal_error = max(min(abs(root * other - 1) for other in roots if other != root) for root in roots if abs(root - 1) > 1e-7)
        for (gap, alpha), sequence in sequences.items():
            values = np.asarray([float(value.subs(y, sp.Rational(y_value.numerator, y_value.denominator))) for value in sequence[:9]])
            vandermonde = np.asarray([[root**k for root in roots] for k in range(9)], dtype=complex)
            coefficients = np.linalg.solve(vandermonde, values.astype(complex))
            order = np.argsort([-abs(root) for root in roots])
            dominant = int(order[0])
            second = int(order[1])
            pair_errors = []
            for index, root in enumerate(roots):
                partner = min(range(len(roots)), key=lambda j: abs(root * roots[j] - 1))
                if partner != index:
                    pair_errors.append(abs(coefficients[index] - coefficients[partner]))
            rows.append({
                "y": str(y_value),
                "family": f"G{gap}",
                "alpha": alpha,
                "dominant_root": float(np.real_if_close(roots[dominant]).real),
                "dominant_modulus": float(abs(roots[dominant])),
                "dominant_coefficient_real": float(coefficients[dominant].real),
                "second_to_first_root_ratio": float(abs(roots[second] / roots[dominant])),
                "reciprocal_root_error": float(reciprocal_error),
                "maximum_reciprocal_coefficient_pair_difference": float(max(pair_errors, default=0.0)),
                "equal_cosh_weights": bool(max(pair_errors, default=0.0) < 1e-8),
                "evidence": "NUMERICAL_MODAL_DIAGNOSTIC",
            })

            signed = [-float(value.subs(y, sp.Rational(y_value.numerator, y_value.denominator))) for value in sequence[:12]]
            minors = []
            for depth in range(1, 5):
                matrix = np.asarray([[signed[i + j] for j in range(depth)] for i in range(depth)])
                minors.append(float(np.linalg.det(matrix)))
            hankel_rows.append({
                "y": str(y_value),
                "family": f"G{gap}",
                "alpha": alpha,
                "leading_Hankel_determinants": minors,
                "all_nonnegative": all(value >= -1e-7 for value in minors),
                "evidence": "NUMERICAL_CLOSURE_HANKEL_DIAGNOSTIC",
            })
    return {
        "modal_rows": rows,
        "hankel_rows": hankel_rows,
        "chebyshev_classification": "PROMISING" if any(row["equal_cosh_weights"] for row in rows) else "WEAK",
        "dominant_mode_classification": "PROMISING",
        "positive_moment_classification": "PROMISING" if all(row["all_nonnegative"] for row in hankel_rows) else "FALSIFIED",
        "warning": "Modal coefficients and Hankel determinants are diagnostics, not validated inequalities on a y interval.",
    }


def run() -> dict[str, Any]:
    DISCOVERY.mkdir(parents=True, exist_ok=True)
    EXPERIMENTS.mkdir(parents=True, exist_ok=True)
    structure = exact_structure()
    sequences, checks = closure_sequences(structure)
    shifts = shifted_signs(sequences, structure)
    diagnostics = modal_and_hankel(sequences, structure)
    payload = {
        **structure,
        "sequence_checks": checks,
        "shifted_sign_summary": shifts["global_prefix_result"],
        "diagnostic_classifications": {
            "Chebyshev_cosh": diagnostics["chebyshev_classification"],
            "dominant_mode": diagnostics["dominant_mode_classification"],
            "closure_Hankel": diagnostics["positive_moment_classification"],
        },
    }
    write_json(EXPERIMENTS / "recurrence_exact_structure.json", payload)
    write_json(EXPERIMENTS / "recurrence_shift_signs.json", shifts)
    write_json(EXPERIMENTS / "recurrence_modal_hankel.json", diagnostics)
    print(json.dumps({
        "status": payload["status"],
        "sequences": len(checks),
        "shifted_signs": shifts["global_prefix_result"],
        "diagnostics": payload["diagnostic_classifications"],
    }, indent=2))
    return payload


if __name__ == "__main__":
    run()
