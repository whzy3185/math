"""Controlled exact search for the Task 53 plus/minus-two structural relation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task51_algebra import symmetric_evans_core
from target_a_task52_exact import elimination_resultant


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task53" / "certificates"


def primitive_core(gap: int) -> sp.Expr:
    lam, symmetric_sum, product = sp.symbols("lambda S P")
    symmetric, _degrees = symmetric_evans_core(gap)
    a = -2 * lam**4 + 16 * lam**2 - 13
    substituted = sp.cancel(symmetric.subs(symmetric_sum, -a * product / (product + 1)))
    return sp.primitive(sp.Poly(sp.fraction(substituted)[0], product))[1].as_expr()


def equal_up_to_scalar(left: sp.Expr, right: sp.Expr, variables: tuple[sp.Symbol, ...]) -> bool:
    left_poly = sp.Poly(left, *variables)
    right_poly = sp.Poly(right, *variables)
    if left_poly.monoms() != right_poly.monoms():
        return False
    left_lc, right_lc = left_poly.LC(), right_poly.LC()
    return sp.expand(left_lc * right - right_lc * left) == 0


def build_certificate() -> dict[str, Any]:
    lam, product = sp.symbols("lambda P")
    core2 = primitive_core(2)
    core6 = primitive_core(6)
    searches = []
    for lambda_sign in (1, -1):
        for reciprocal in (False, True):
            transformed = core2.subs(lam, lambda_sign * lam)
            if reciprocal:
                degree = sp.degree(transformed, product)
                transformed = sp.expand(product**degree * transformed.subs(product, 1 / product))
            searches.append({
                "lambda_sign": lambda_sign,
                "P_reciprocal": reciprocal,
                "equal_up_to_nonzero_scalar": equal_up_to_scalar(core6, transformed, (lam, product)),
            })
    resultant2, record2 = elimination_resultant(2)
    resultant6, record6 = elimination_resultant(6)
    checks = {
        "complete_small_transformation_search": len(searches) == 4,
        "no_direct_core_identity_found": not any(row["equal_up_to_nonzero_scalar"] for row in searches),
        "resultants_identical": sp.expand(resultant2 - resultant6) == 0,
        "factor_records_identical": record2["factors"] == record6["factors"],
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "PLUS_MINUS_TWO_ELIMINATION_EQUALITY_ONLY",
        "evidence": "PROVED",
        "gap2_core": str(core2),
        "gap6_core": str(core6),
        "tested_exact_transformations": searches,
        "common_resultant_factors": record2["factors"],
        "proved_statement": (
            "After exact stable-branch substitution, lambda-sign squaring, and elimination of P, "
            "gap2 and gap6 have identical resultants over Q[y]."
        ),
        "not_proved": (
            "No unsquared conjugacy, inverse duality, or spectral-curve isomorphism was found. "
            "The equality may still be a projection coincidence."
        ),
        "s3_decision": "RECURRENCE_ROUTE_WEAK: elimination equality supplies no branch-preserving map for a uniform gap hierarchy.",
        "checks": checks,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payload = build_certificate()
    write_json(OUTPUT / "plus_minus_two_structure.json", payload)
    print(json.dumps({"status": payload["status"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()
