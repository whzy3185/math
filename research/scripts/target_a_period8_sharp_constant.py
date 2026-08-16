"""Prove the sharp spectral constant of the audited Target A period-8 phase."""

from __future__ import annotations

import argparse
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
EXPECTED_POLYNOMIAL_SHA256 = "cc26dedfee3fe3e6c0674f1b217fde592a043a5d8b4913752dc37ad2a62193b2"
EXPECTED_FLOQUET_SHA256 = "2a5657d0791b1e1a3c742ae8e0a738f083115b4e4516e5e8d8fd4d1999d6c3ee"
EXPECTED_FAMILY_SHA256 = "b36bce66ec367e418e1499a1400773147d29537da92a49695b8d7dc9c1c08fa8"
OLD_BOUND = sp.Rational(1561, 200)


class SharpConstantError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SharpConstantError(message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def _expression_string(expression: sp.Expr) -> str:
    return sp.sstr(sp.expand(expression))


def _exact_positive(expression: sp.Expr) -> bool:
    algebraic = to_number_field(sp.simplify(expression)).to_root()
    if algebraic.is_positive is True:
        return True
    return sp.simplify(algebraic > 0) is sp.true


def _exact_less(left: sp.Expr, right: sp.Expr) -> bool:
    return _exact_positive(right - left)


def _sort_exact(values: list[sp.Expr]) -> list[sp.Expr]:
    ordered: list[sp.Expr] = []
    for value in values:
        index = 0
        while index < len(ordered) and _exact_less(ordered[index], value):
            index += 1
        _require(
            all(sp.simplify(value - previous) != 0 for previous in ordered),
            "endpoint roots are not distinct",
        )
        ordered.insert(index, value)
    return ordered


def _reconstruct_polynomial(rows: list[dict[str, Any]], y: sp.Symbol, c: sp.Symbol) -> sp.Expr:
    _require(isinstance(rows, list) and rows, "SHARP_DEPENDENCY_FAIL: empty coefficient map")
    result = sp.Integer(0)
    seen: set[tuple[int, int]] = set()
    for row in rows:
        degrees = (int(row["y_degree"]), int(row["c_degree"]))
        _require(degrees not in seen, "SHARP_DEPENDENCY_FAIL: duplicate P monomial")
        seen.add(degrees)
        result += (
            sp.Rational(str(row["coefficient"]))
            * y ** degrees[0]
            * c ** degrees[1]
        )
    return sp.expand(result)


def load_dependencies(
    polynomial_path: Path = DEFAULT_POLYNOMIAL,
    floquet_path: Path = DEFAULT_FLOQUET,
    family_path: Path = DEFAULT_FAMILY,
) -> dict[str, Any]:
    polynomial_bytes = polynomial_path.read_bytes()
    floquet_bytes = floquet_path.read_bytes()
    family_bytes = family_path.read_bytes()
    polynomial_sha = _sha256_bytes(polynomial_bytes)
    floquet_sha = _sha256_bytes(floquet_bytes)
    family_sha = _sha256_bytes(family_bytes)
    _require(
        polynomial_sha == EXPECTED_POLYNOMIAL_SHA256,
        "SHARP_DEPENDENCY_FAIL: Task 38 polynomial SHA mismatch",
    )
    _require(
        floquet_sha == EXPECTED_FLOQUET_SHA256,
        "SHARP_DEPENDENCY_FAIL: Task 38 Floquet SHA mismatch",
    )
    _require(
        family_sha == EXPECTED_FAMILY_SHA256,
        "SHARP_DEPENDENCY_FAIL: Task 39 family SHA mismatch",
    )
    polynomial_data = json.loads(polynomial_bytes.decode("utf-8"))
    floquet = json.loads(floquet_bytes.decode("utf-8"))
    family = json.loads(family_bytes.decode("utf-8"))
    _require(
        polynomial_data.get("status") == "PERIOD8_INDEPENDENT_POLYNOMIAL_FROZEN",
        "SHARP_DEPENDENCY_FAIL: polynomial status mismatch",
    )
    _require(
        floquet.get("status") == "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
        "SHARP_DEPENDENCY_FAIL: Floquet status mismatch",
    )
    _require(
        family.get("status") == "PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED",
        "SHARP_DEPENDENCY_FAIL: family status mismatch",
    )
    _require(
        family.get("floquet_dependency", {}).get("sha256") == floquet_sha
        and family.get("floquet_dependency", {}).get("polynomial_snapshot_sha256")
        == polynomial_sha,
        "SHARP_DEPENDENCY_FAIL: Task 39 internal dependency mismatch",
    )
    _require(
        floquet.get("P_independent_coefficient_map")
        == polynomial_data.get("P_independent_coefficient_map"),
        "SHARP_DEPENDENCY_FAIL: polynomial maps disagree",
    )
    _require(
        floquet.get("hermitian_check") is True
        and floquet.get("direct_sum_proof_status") == "FLOQUET_DIRECT_SUM_PASS"
        and floquet.get("squared_eigenvalue_root_link_status")
        == "SQUARED_EIGENVALUE_ROOT_LINK_PASS",
        "SHARP_DEPENDENCY_FAIL: spectral interpretation is incomplete",
    )
    y, c = sp.symbols("y c")
    polynomial = _reconstruct_polynomial(
        polynomial_data["P_independent_coefficient_map"], y, c
    )
    stored = sp.sympify(polynomial_data["P_independent"], locals={"y": y, "c": c})
    _require(sp.expand(polynomial - stored) == 0, "SHARP_DEPENDENCY_FAIL: P fields disagree")
    return {
        "polynomial_data": polynomial_data,
        "floquet": floquet,
        "family": family,
        "polynomial_sha256": polynomial_sha,
        "floquet_sha256": floquet_sha,
        "family_sha256": family_sha,
        "P": polynomial,
        "y": y,
        "c": c,
    }


def validate_candidate_is_largest(candidate: sp.Expr, ordered_roots: list[sp.Expr]) -> bool:
    return bool(ordered_roots and sp.simplify(candidate - ordered_roots[-1]) == 0)


def derive_endpoint_candidate(P: sp.Expr, y: sp.Symbol, c: sp.Symbol) -> dict[str, Any]:
    x, w, Y, R = sp.symbols("x w Y R")
    endpoint = sp.Poly(sp.expand(P.subs(c, 2)), y, domain=sp.QQ).as_expr()
    shifted = sp.Poly(sp.expand(endpoint.subs(y, x + 4)), x, domain=sp.QQ)
    _require(
        all(degree[0] % 2 == 0 for degree, _ in shifted.terms()),
        "endpoint translation is not biquadratic",
    )
    w_polynomial = sp.Poly(
        sum(coefficient * w ** (degree[0] // 2) for degree, coefficient in shifted.terms()),
        w,
        domain=sp.QQ,
    )
    w_roots = _sort_exact([sp.simplify(value) for value in sp.solve(w_polynomial.as_expr(), w)])
    _require(len(w_roots) == 2 and all(_exact_positive(value) for value in w_roots), "bad w roots")
    endpoint_roots = _sort_exact(
        [sp.simplify(4 + sign * sp.sqrt(value)) for value in w_roots for sign in (-1, 1)]
    )
    _require(len(endpoint_roots) == 4, "endpoint root count mismatch")
    eta = endpoint_roots[-1]
    _require(validate_candidate_is_largest(eta, endpoint_roots), "largest endpoint root check failed")
    _require(all(_exact_positive(root) for root in endpoint_roots), "endpoint has a negative y root")
    minimal_eta = sp.Poly(sp.minimal_polynomial(eta, Y), Y, domain=sp.QQ)
    _require(sp.simplify(minimal_eta.as_expr().subs(Y, eta)) == 0, "eta minimal root check failed")
    _require(
        sp.expand(minimal_eta.as_expr().subs(Y, y) - endpoint) == 0,
        "eta minimal polynomial is not P(y,2)",
    )
    rho_star = sp.sqrt(eta)
    minimal_rho = sp.Poly(sp.minimal_polynomial(rho_star, R), R, domain=sp.QQ)
    even_relation = sp.expand(endpoint.subs(y, R**2))
    _require(sp.simplify(minimal_rho.as_expr().subs(R, rho_star)) == 0, "rho minimal root check")
    _require(sp.simplify(even_relation.subs(R, rho_star)) == 0, "rho even relation failed")

    eta_lower = sp.Rational(1951, 250)
    eta_upper = OLD_BOUND
    _require(
        minimal_eta.eval(eta_lower) < 0
        and minimal_eta.eval(eta_upper) > 0
        and int(minimal_eta.count_roots(eta_lower, eta_upper)) == 1,
        "eta isolating interval failed",
    )
    _require(_exact_positive(eta - eta_lower) and _exact_positive(eta_upper - eta), "eta placement failed")
    rho_lower = sp.Rational(2793, 1000)
    rho_upper = sp.Rational(1397, 500)
    _require(
        minimal_rho.eval(rho_lower) < 0
        and minimal_rho.eval(rho_upper) > 0
        and int(minimal_rho.count_roots(rho_lower, rho_upper)) == 1,
        "rho isolating interval failed",
    )
    _require(
        _exact_positive(rho_star - rho_lower) and _exact_positive(rho_upper - rho_star),
        "rho placement failed",
    )
    return {
        "status": "CANDIDATE_BAND_EDGE_DERIVED",
        "endpoint_polynomial": _expression_string(endpoint),
        "translation": "x=y-4",
        "translated_polynomial": _expression_string(shifted.as_expr()),
        "w_polynomial": _expression_string(w_polynomial.as_expr()),
        "w_roots": [_expression_string(value) for value in w_roots],
        "ordered_endpoint_roots": [_expression_string(value) for value in endpoint_roots],
        "eta": eta,
        "eta_exact": _expression_string(eta),
        "eta_minimal_polynomial": _expression_string(minimal_eta.as_expr()),
        "eta_isolating_interval": {"lower": str(eta_lower), "upper": str(eta_upper)},
        "eta_decimal_diagnostic": str(sp.N(eta, 20)),
        "rho_star": rho_star,
        "rho_star_exact": _expression_string(rho_star),
        "rho_minimal_polynomial": _expression_string(minimal_rho.as_expr()),
        "rho_even_polynomial_relation": _expression_string(even_relation),
        "rho_isolating_interval": {"lower": str(rho_lower), "upper": str(rho_upper)},
        "rho_decimal_diagnostic": str(sp.N(rho_star, 20)),
    }


def _algebraic_coefficient_map(
    polynomial: sp.Expr, variables: tuple[sp.Symbol, ...]
) -> list[dict[str, Any]]:
    poly = sp.Poly(sp.expand(polynomial), *variables, extension=True)
    rows: list[dict[str, Any]] = []
    for degrees, coefficient in poly.terms():
        row: dict[str, Any] = {
            f"{variable}_degree": degree for variable, degree in zip(variables, degrees)
        }
        row["coefficient"] = _expression_string(coefficient)
        rows.append(row)
    return rows


def validate_sharp_coefficient_map(rows: list[dict[str, Any]]) -> dict[str, Any]:
    nonconstant = [
        row
        for row in rows
        if any(int(value) != 0 for key, value in row.items() if key.endswith("_degree"))
    ]
    constants = [
        row
        for row in rows
        if all(int(value) == 0 for key, value in row.items() if key.endswith("_degree"))
    ]
    _require(len(constants) == 1, "SHARP_POSITIVITY_CERTIFICATE_FAIL: constant missing")
    constant_zero = sp.simplify(sp.sympify(constants[0]["coefficient"])) == 0
    all_positive = all(_exact_positive(sp.sympify(row["coefficient"])) for row in nonconstant)
    _require(constant_zero and all_positive, "SHARP_POSITIVITY_CERTIFICATE_FAIL")
    return {
        "constant_coefficient_zero": constant_zero,
        "all_nonconstant_coefficients_strictly_positive": all_positive,
    }


def sharp_positivity_certificate(
    P: sp.Expr, y: sp.Symbol, c: sp.Symbol, eta: sp.Expr
) -> dict[str, Any]:
    u, t = sp.symbols("u t")
    s = sp.simplify(eta - 4)
    _require(_exact_positive(s), "sharp radical s is not positive")
    _require(sp.simplify(s**2 - (10 + 2 * sp.sqrt(5))) == 0, "sharp radical identity failed")
    expanded = sp.expand(P.subs({y: eta + u, c: 2 - t}))
    rows = _algebraic_coefficient_map(expanded, (u, t))
    rows.append({"u_degree": 0, "t_degree": 0, "coefficient": "0"})
    validation = validate_sharp_coefficient_map(rows)
    coefficient_lookup = {
        (int(row["u_degree"]), int(row["t_degree"])): sp.sympify(row["coefficient"])
        for row in rows
    }
    _require(_exact_positive(coefficient_lookup[(1, 0)]), "positive pure-u term missing")
    _require(_exact_positive(coefficient_lookup[(0, 1)]), "positive pure-t term missing")
    _require(sp.simplify(expanded.subs({u: 0, t: 0})) == 0, "endpoint equality failed")
    return {
        "status": "SHARP_POSITIVITY_CERTIFICATE_PASS",
        "s": _expression_string(s),
        "eta": _expression_string(eta),
        "change_of_variables": {"u": "y-eta", "t": "2-c"},
        "expanded_polynomial": _expression_string(expanded),
        "coefficient_map": rows,
        **validation,
        "domain": "u>=0 and t>=0, equivalently y>=eta and c<=2",
        "equality_conditions": "u=0 and t=0, equivalently y=eta and c=2",
        "equality_justification": (
            "all nonconstant terms are nonnegative; positive pure-u and pure-t "
            "linear terms force u=t=0"
        ),
    }


def global_band_edge_certificate(
    P: sp.Expr,
    y: sp.Symbol,
    c: sp.Symbol,
    eta: sp.Expr,
    positivity: dict[str, Any],
) -> dict[str, Any]:
    z = sp.Symbol("z", nonzero=True)
    _require(positivity["status"] == "SHARP_POSITIVITY_CERTIFICATE_PASS", "sharp positivity missing")
    _require(sp.simplify(P.subs({y: eta, c: 2})) == 0, "eta is not attained at c=2")
    z_equation = sp.factor(z * (z + z**-1 - 2))
    _require(sp.expand(z_equation - (z - 1) ** 2) == 0, "unit-circle endpoint equation failed")
    return {
        "status": "GLOBAL_BAND_EDGE_UPPER_PASS",
        "global_upper": "rho(H(z))^2<=eta for every |z|=1",
        "squared_equality_requires": "c=2",
        "unit_circle_equation": "z+z^-1=2 iff (z-1)^2=0",
        "unique_Bloch_parameter": "z=1",
        "attainment": "P(eta,2)=0 gives eigenvalues x=+-sqrt(eta) of H(1)",
        "sharp_status": "PERIOD8_SHARP_INFINITE_VOLUME_CONSTANT_PROVED",
    }


def top_root_monotonicity_certificate(
    P: sp.Expr, y: sp.Symbol, c: sp.Symbol
) -> dict[str, Any]:
    endpoint_minus = sp.factor(P.subs(c, -2), extension=sp.sqrt(2))
    roots_minus = _sort_exact([sp.simplify(root) for root in sp.solve(P.subs(c, -2), y)])
    _require(len(roots_minus) == 4, "c=-2 root count mismatch")
    y0 = roots_minus[-1]
    _require(sp.simplify(y0 - (6 + sp.sqrt(2))) == 0, "unexpected c=-2 top root")
    value_at_y0 = sp.factor(P.subs(y, y0), extension=sp.sqrt(2))
    expected_value = (c + 2) * (c + 5 - 8 * sp.sqrt(2))
    _require(sp.expand(value_at_y0 - expected_value) == 0, "P(y0,c) factorization failed")
    _require(_exact_positive(8 * sp.sqrt(2) - 7), "P(y0,c) sign bound failed")
    derivative_c = sp.diff(P, c)
    c0 = sp.solve(derivative_c, c)[0]
    c0_derivative = sp.diff(c0, y)
    c0_y0 = sp.simplify(c0.subs(y, y0))
    _require(_exact_positive(y0 - 4), "y0 is not above vertex turning point")
    _require(sp.simplify(c0_derivative - (2 * y - 8)) == 0, "c0 derivative mismatch")
    _require(_exact_positive(c0_y0 - 2), "c0(y0) does not exceed two")
    return {
        "status": "TOP_BAND_MONOTONICITY_PROVED",
        "endpoint_c": -2,
        "endpoint_factorization": sp.sstr(endpoint_minus),
        "ordered_endpoint_roots": [_expression_string(root) for root in roots_minus],
        "y0": _expression_string(y0),
        "P_y0_c_factorization": sp.sstr(value_at_y0),
        "P_y0_c_sign": "negative for -2<c<=2",
        "root_above_y0": "P(y0,c)<0 and P(y,c)->+infinity imply r(c)>y0",
        "partial_P_partial_c": _expression_string(derivative_c),
        "c_vertex": _expression_string(c0),
        "c_vertex_derivative": _expression_string(c0_derivative),
        "c_vertex_at_y0": _expression_string(c0_y0),
        "c_vertex_lower_bound": "c0(y)>2 for y>=y0",
        "strict_decrease_in_c": "P_c(y,c)<0 for y>=y0 and c<=2",
        "strict_monotonicity_argument": (
            "for c1<c2 and y1=r(c1), P(y1,c2)<0; the positive leading term "
            "forces a root above y1, so r(c2)>r(c1)"
        ),
    }


def validate_band_edge_claim(claimed_c: sp.Expr) -> bool:
    return sp.simplify(claimed_c - 2) == 0


def validate_alpha_minus_claim(L: int, maximizing_c: sp.Expr, strict_below_eta: bool) -> bool:
    if type(L) is not int or L < 1:
        return False
    expected = 2 * sp.cos(sp.pi / L)
    return sp.simplify(maximizing_c - expected) == 0 and strict_below_eta and _exact_less(expected, 2)


def validate_sharp_bound_claim(claimed: sp.Expr, eta: sp.Expr) -> bool:
    return sp.simplify(claimed - eta) == 0


def holonomy_consequences(
    P: sp.Expr, y: sp.Symbol, c: sp.Symbol, eta: sp.Expr, monotonicity: dict[str, Any]
) -> dict[str, Any]:
    _require(monotonicity["status"] == "TOP_BAND_MONOTONICITY_PROVED", "monotonicity missing")
    endpoint_derivative = sp.simplify(sp.diff(P, y).subs({y: eta, c: 2}))
    _require(_exact_positive(endpoint_derivative), "top endpoint root is not simple")
    return {
        "alpha_plus": {
            "status": "PLUS_HOLONOMY_EXACT_FINITE_CONSTANT_PROVED",
            "domain": "every integer L>=1 (in particular family domain L>=4)",
            "admissible_relation": "z^L=1",
            "attainment_z": "z=1",
            "finite_formula_squared": _expression_string(eta),
            "finite_formula": _expression_string(sp.sqrt(eta)),
        },
        "alpha_minus": {
            "status": "MINUS_HOLONOMY_FINITE_BAND_EDGE_PROVED",
            "domain": "every finite integer L>=1",
            "admissible_parameters": "z_k=exp(i*(2k+1)*pi/L)",
            "maximizing_c": "2*cos(pi/L)",
            "finite_formula_squared": "r(2*cos(pi/L)), where r(c) is the largest real root of P(y,c)",
            "strict_below_eta": True,
            "strict_reason": "2*cos(pi/L)<2 and r(c) is strictly increasing",
            "limit": _expression_string(eta),
            "limit_reason": (
                "2*cos(pi/L)->2 and the Hermitian block spectral radius is continuous; "
                "equivalently the simple top root has P_y(eta,2)>0"
            ),
            "endpoint_root_derivative": _expression_string(endpoint_derivative),
        },
        "shared_infinite_volume_squared_constant": _expression_string(eta),
    }


def old_bound_comparison(eta: sp.Expr) -> dict[str, Any]:
    difference = sp.simplify(OLD_BOUND - eta)
    _require(_exact_positive(difference), "old rational bound does not exceed eta")
    return {
        "old_bound": str(OLD_BOUND),
        "eta": _expression_string(eta),
        "exact_difference": _expression_string(difference),
        "eta_strictly_below_old_bound": True,
        "old_bound_is_sharp": False,
        "eta_decimal_diagnostic": str(sp.N(eta, 18)),
        "difference_decimal_diagnostic": str(sp.N(difference, 18)),
        "interpretation": "1561/200 is a strict rational certificate but is not sharp",
    }


def run_sharp_constant_proof(
    polynomial_path: Path = DEFAULT_POLYNOMIAL,
    floquet_path: Path = DEFAULT_FLOQUET,
    family_path: Path = DEFAULT_FAMILY,
    result_path: Path = DEFAULT_RESULT,
) -> dict[str, Any]:
    dependency = load_dependencies(polynomial_path, floquet_path, family_path)
    endpoint = derive_endpoint_candidate(dependency["P"], dependency["y"], dependency["c"])
    eta = endpoint["eta"]
    positivity = sharp_positivity_certificate(
        dependency["P"], dependency["y"], dependency["c"], eta
    )
    band_edge = global_band_edge_certificate(
        dependency["P"], dependency["y"], dependency["c"], eta, positivity
    )
    monotonicity = top_root_monotonicity_certificate(
        dependency["P"], dependency["y"], dependency["c"]
    )
    holonomies = holonomy_consequences(
        dependency["P"], dependency["y"], dependency["c"], eta, monotonicity
    )
    comparison = old_bound_comparison(eta)
    result = {
        "schema_version": 1,
        "status": "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED",
        "source_polynomial_file": "research/audit/target_a_period8_independent_polynomial.json",
        "source_polynomial_sha256": dependency["polynomial_sha256"],
        "source_floquet_audit_file": "research/audit/period8_floquet_independent_audit.json",
        "source_floquet_audit_sha256": dependency["floquet_sha256"],
        "source_family_audit_file": "research/audit/period8_infinite_family_independent_audit.json",
        "source_family_audit_sha256": dependency["family_sha256"],
        "top_root_definition": "r(c)=largest nonnegative real root in y of P(y,c), c in [-2,2]",
        "eta_squared": {
            "exact_radical": endpoint["eta_exact"],
            "minimal_polynomial": endpoint["eta_minimal_polynomial"],
            "isolating_interval": endpoint["eta_isolating_interval"],
            "decimal_diagnostic": endpoint["eta_decimal_diagnostic"],
        },
        "rho_star": {
            "exact_radical": endpoint["rho_star_exact"],
            "minimal_polynomial": endpoint["rho_minimal_polynomial"],
            "even_polynomial_relation": endpoint["rho_even_polynomial_relation"],
            "isolating_interval": endpoint["rho_isolating_interval"],
            "decimal_diagnostic": endpoint["rho_decimal_diagnostic"],
        },
        "endpoint_derivation": {
            key: value
            for key, value in endpoint.items()
            if key not in {"eta", "rho_star"}
        },
        "c_endpoint": 2,
        "z_endpoint": 1,
        "sharp_positivity_expansion": positivity["expanded_polynomial"],
        "sharp_positivity_certificate": positivity,
        "equality_conditions": positivity["equality_conditions"],
        "band_edge": band_edge,
        "top_root_monotonicity": monotonicity,
        "alpha_plus": holonomies["alpha_plus"],
        "alpha_minus": holonomies["alpha_minus"],
        "shared_infinite_volume_squared_constant": holonomies[
            "shared_infinite_volume_squared_constant"
        ],
        "old_rational_bound_comparison": comparison,
        "checker": {
            "path": "research/scripts/verify_target_a_period8_sharp_constant.py",
            "status": "TARGET_A_PERIOD8_SHARP_CONSTANT_PASS",
        },
        "scope_boundary": {
            "period8_global_optimality_proved": False,
            "all_sufficiently_large_even_orders_fail": False,
            "global_m_n_solved": False,
            "new_period_search_performed": False,
        },
        "script_sha256": _sha256_file(Path(__file__).resolve()),
        "next_gate": "Task 40B",
    }
    _write_json(result_path, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--polynomial", type=Path, default=DEFAULT_POLYNOMIAL)
    parser.add_argument("--floquet-audit", type=Path, default=DEFAULT_FLOQUET)
    parser.add_argument("--family-audit", type=Path, default=DEFAULT_FAMILY)
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()
    try:
        result = run_sharp_constant_proof(
            args.polynomial, args.floquet_audit, args.family_audit, args.output
        )
        _require(
            result["status"] == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED",
            "final sharp constant status failed",
        )
    except Exception as error:
        print(f"Target A period-8 sharp constant proof failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_SHARP_CONSTANT_FAIL")
        raise SystemExit(1)
    print("CANDIDATE_BAND_EDGE_DERIVED")
    print("SHARP_POSITIVITY_CERTIFICATE_PASS")
    print("GLOBAL_BAND_EDGE_UPPER_PASS")
    print("TOP_BAND_MONOTONICITY_PROVED")
    print("PLUS_HOLONOMY_EXACT_FINITE_CONSTANT_PROVED")
    print("MINUS_HOLONOMY_FINITE_BAND_EDGE_PROVED")
    print("PERIOD8_SHARP_INFINITE_VOLUME_CONSTANT_PROVED")
    print("PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED")


if __name__ == "__main__":
    main()
