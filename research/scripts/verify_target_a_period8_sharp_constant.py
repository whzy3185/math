"""Verify the frozen proof of the sharp Target A period-8 spectral constant."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.polys.numberfields import to_number_field


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_POLYNOMIAL = RESEARCH_ROOT / "audit" / "target_a_period8_independent_polynomial.json"
DEFAULT_FLOQUET = RESEARCH_ROOT / "audit" / "period8_floquet_independent_audit.json"
DEFAULT_FAMILY = RESEARCH_ROOT / "audit" / "period8_infinite_family_independent_audit.json"
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
OLD_BOUND = sp.Rational(1561, 200)


class SharpConstantVerificationError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SharpConstantVerificationError(message)


def _read_json(path: Path) -> tuple[bytes, dict[str, Any]]:
    raw = path.read_bytes()
    return raw, json.loads(raw.decode("utf-8"))


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _exact_positive(expression: sp.Expr) -> bool:
    algebraic = to_number_field(sp.simplify(expression)).to_root()
    if algebraic.is_positive is True:
        return True
    return sp.simplify(algebraic > 0) is sp.true


def _reconstruct_P(rows: list[dict[str, Any]], y: sp.Symbol, c: sp.Symbol) -> sp.Expr:
    polynomial = sp.Integer(0)
    seen: set[tuple[int, int]] = set()
    for row in rows:
        degrees = (int(row["y_degree"]), int(row["c_degree"]))
        _require(degrees not in seen, "duplicate P monomial")
        seen.add(degrees)
        polynomial += (
            sp.Rational(str(row["coefficient"]))
            * y ** degrees[0]
            * c ** degrees[1]
        )
    return sp.expand(polynomial)


def _reconstruct_sharp_map(
    rows: list[dict[str, Any]], u: sp.Symbol, t: sp.Symbol
) -> tuple[sp.Expr, list[sp.Expr], sp.Expr]:
    polynomial = sp.Integer(0)
    nonconstant: list[sp.Expr] = []
    constants: list[sp.Expr] = []
    seen: set[tuple[int, int]] = set()
    for row in rows:
        degrees = (int(row["u_degree"]), int(row["t_degree"]))
        _require(degrees not in seen, "duplicate sharp monomial")
        seen.add(degrees)
        coefficient = sp.sympify(row["coefficient"])
        polynomial += coefficient * u ** degrees[0] * t ** degrees[1]
        if degrees == (0, 0):
            constants.append(coefficient)
        else:
            nonconstant.append(coefficient)
    _require(len(constants) == 1, "sharp constant coefficient missing")
    return sp.expand(polynomial), nonconstant, constants[0]


def verify_sharp_constant(
    polynomial_path: Path = DEFAULT_POLYNOMIAL,
    floquet_path: Path = DEFAULT_FLOQUET,
    family_path: Path = DEFAULT_FAMILY,
    result_path: Path = DEFAULT_RESULT,
) -> dict[str, Any]:
    polynomial_raw, polynomial_data = _read_json(polynomial_path)
    floquet_raw, floquet = _read_json(floquet_path)
    family_raw, family = _read_json(family_path)
    result_raw, result = _read_json(result_path)
    _require(
        result.get("status") == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED",
        "sharp result status mismatch",
    )
    _require(
        _sha256(polynomial_raw) == result.get("source_polynomial_sha256"),
        "polynomial dependency SHA mismatch",
    )
    _require(
        _sha256(floquet_raw) == result.get("source_floquet_audit_sha256"),
        "Floquet dependency SHA mismatch",
    )
    _require(
        _sha256(family_raw) == result.get("source_family_audit_sha256"),
        "family dependency SHA mismatch",
    )
    _require(
        polynomial_data.get("status") == "PERIOD8_INDEPENDENT_POLYNOMIAL_FROZEN",
        "polynomial status mismatch",
    )
    _require(
        floquet.get("status") == "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED"
        and family.get("status") == "PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED",
        "audited dependency status mismatch",
    )
    _require(
        family.get("floquet_dependency", {}).get("sha256") == _sha256(floquet_raw)
        and family.get("floquet_dependency", {}).get("polynomial_snapshot_sha256")
        == _sha256(polynomial_raw),
        "transitive dependency mismatch",
    )
    y, c, Y, R = sp.symbols("y c Y R")
    P = _reconstruct_P(polynomial_data["P_independent_coefficient_map"], y, c)
    _require(
        polynomial_data["P_independent_coefficient_map"]
        == floquet["P_independent_coefficient_map"],
        "P coefficient maps disagree",
    )
    eta = sp.sympify(result["eta_squared"]["exact_radical"])
    rho = sp.sympify(result["rho_star"]["exact_radical"])
    _require(sp.simplify(rho**2 - eta) == 0, "rho_star^2 does not equal eta")
    _require(sp.simplify(P.subs({y: eta, c: 2})) == 0, "eta is not an endpoint root")

    endpoint_roots = [sp.simplify(root) for root in sp.solve(P.subs(c, 2), y)]
    _require(len(endpoint_roots) == 4, "endpoint root count mismatch")
    _require(
        all(sp.simplify(eta - root) == 0 or _exact_positive(eta - root) for root in endpoint_roots),
        "eta is not the largest endpoint root",
    )
    eta_minimal = sp.Poly(
        sp.sympify(result["eta_squared"]["minimal_polynomial"], locals={"Y": Y}),
        Y,
    )
    rho_minimal = sp.Poly(
        sp.sympify(result["rho_star"]["minimal_polynomial"], locals={"R": R}),
        R,
    )
    _require(sp.simplify(eta_minimal.as_expr().subs(Y, eta)) == 0, "eta minimal root fails")
    _require(sp.simplify(rho_minimal.as_expr().subs(R, rho)) == 0, "rho minimal root fails")
    _require(
        sp.Poly(sp.minimal_polynomial(eta, Y), Y).as_expr() == eta_minimal.as_expr(),
        "eta polynomial is not minimal",
    )
    _require(
        sp.Poly(sp.minimal_polynomial(rho, R), R).as_expr() == rho_minimal.as_expr(),
        "rho polynomial is not minimal",
    )
    even_relation = sp.sympify(result["rho_star"]["even_polynomial_relation"], locals={"R": R})
    _require(sp.simplify(even_relation.subs(R, rho)) == 0, "rho even relation fails")

    eta_interval = result["eta_squared"]["isolating_interval"]
    eta_lower = sp.Rational(eta_interval["lower"])
    eta_upper = sp.Rational(eta_interval["upper"])
    _require(
        eta_minimal.eval(eta_lower) < 0
        and eta_minimal.eval(eta_upper) > 0
        and int(eta_minimal.count_roots(eta_lower, eta_upper)) == 1,
        "eta isolating interval fails",
    )
    _require(
        _exact_positive(eta - eta_lower) and _exact_positive(eta_upper - eta),
        "eta is outside its isolating interval",
    )

    positivity = result.get("sharp_positivity_certificate", {})
    u, t = sp.symbols("u t")
    mapped, nonconstant, constant = _reconstruct_sharp_map(
        positivity.get("coefficient_map", []), u, t
    )
    substituted = sp.expand(P.subs({y: eta + u, c: 2 - t}))
    _require(sp.expand(mapped - substituted) == 0, "sharp map does not reconstruct substitution")
    _require(sp.simplify(constant) == 0, "sharp constant coefficient is not zero")
    _require(all(_exact_positive(value) for value in nonconstant), "sharp coefficient is not positive")
    coefficient_lookup = {
        (int(row["u_degree"]), int(row["t_degree"])): sp.sympify(row["coefficient"])
        for row in positivity["coefficient_map"]
    }
    _require(
        _exact_positive(coefficient_lookup[(1, 0)])
        and _exact_positive(coefficient_lookup[(0, 1)]),
        "sharp equality condition lacks pure linear terms",
    )
    _require(
        positivity.get("status") == "SHARP_POSITIVITY_CERTIFICATE_PASS"
        and positivity.get("equality_conditions")
        == "u=0 and t=0, equivalently y=eta and c=2",
        "sharp positivity status or equality condition fails",
    )

    band = result.get("band_edge", {})
    _require(
        result.get("c_endpoint") == 2
        and result.get("z_endpoint") == 1
        and band.get("status") == "GLOBAL_BAND_EDGE_UPPER_PASS"
        and band.get("unique_Bloch_parameter") == "z=1",
        "band-edge endpoint or uniqueness fails",
    )

    monotonicity = result.get("top_root_monotonicity", {})
    y0 = sp.sympify(monotonicity["y0"])
    roots_minus = [sp.simplify(root) for root in sp.solve(P.subs(c, -2), y)]
    _require(
        all(sp.simplify(y0 - root) == 0 or _exact_positive(y0 - root) for root in roots_minus),
        "y0 is not the largest c=-2 root",
    )
    expected_y0_value = (c + 2) * (c + 5 - 8 * sp.sqrt(2))
    _require(
        sp.expand(P.subs(y, y0) - expected_y0_value) == 0,
        "P(y0,c) factorization fails",
    )
    derivative_c = sp.diff(P, c)
    c0 = sp.solve(derivative_c, c)[0]
    _require(_exact_positive(c0.subs(y, y0) - 2), "c vertex lower bound fails")
    _require(
        monotonicity.get("status") == "TOP_BAND_MONOTONICITY_PROVED",
        "top-root monotonicity status fails",
    )

    alpha_plus = result.get("alpha_plus", {})
    _require(
        alpha_plus.get("status") == "PLUS_HOLONOMY_EXACT_FINITE_CONSTANT_PROVED"
        and alpha_plus.get("attainment_z") == "z=1"
        and sp.simplify(sp.sympify(alpha_plus["finite_formula_squared"]) - eta) == 0,
        "alpha=+1 finite theorem fails",
    )
    alpha_minus = result.get("alpha_minus", {})
    _require(
        alpha_minus.get("status") == "MINUS_HOLONOMY_FINITE_BAND_EDGE_PROVED"
        and alpha_minus.get("maximizing_c") == "2*cos(pi/L)"
        and alpha_minus.get("strict_below_eta") is True
        and sp.simplify(sp.sympify(alpha_minus["limit"]) - eta) == 0,
        "alpha=-1 finite theorem or limit fails",
    )
    _require(
        _exact_positive(sp.diff(P, y).subs({y: eta, c: 2})),
        "endpoint top root is not simple",
    )

    comparison = result.get("old_rational_bound_comparison", {})
    _require(
        _exact_positive(OLD_BOUND - eta)
        and comparison.get("eta_strictly_below_old_bound") is True
        and comparison.get("old_bound_is_sharp") is False,
        "old rational bound comparison fails",
    )
    _require(
        result.get("checker", {}).get("status") == "TARGET_A_PERIOD8_SHARP_CONSTANT_PASS",
        "checker status field mismatch",
    )
    return {
        "status": "TARGET_A_PERIOD8_SHARP_CONSTANT_PASS",
        "result_sha256": _sha256(result_raw),
        "dependencies_verified": True,
        "largest_endpoint_root_verified": True,
        "sharp_positivity_verified": True,
        "band_edge_uniqueness_verified": True,
        "top_root_monotonicity_verified": True,
        "holonomy_consequences_verified": True,
    }


def main() -> None:
    try:
        report = verify_sharp_constant()
        _require(
            report["status"] == "TARGET_A_PERIOD8_SHARP_CONSTANT_PASS",
            "final sharp checker status failed",
        )
    except Exception as error:
        print(f"Target A period-8 sharp constant verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_SHARP_CONSTANT_FAIL")
        raise SystemExit(1)
    print("TARGET_A_PERIOD8_SHARP_CONSTANT_PASS")


if __name__ == "__main__":
    main()
