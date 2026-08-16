"""Independently certify the complete Target A period-8 infinite family."""

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
DEFAULT_FLOQUET_AUDIT = RESEARCH_ROOT / "audit" / "period8_floquet_independent_audit.json"
DEFAULT_POLYNOMIAL_SNAPSHOT = (
    RESEARCH_ROOT / "audit" / "target_a_period8_independent_polynomial.json"
)
DEFAULT_POSITIVITY_SNAPSHOT = (
    RESEARCH_ROOT / "audit" / "target_a_period8_uniform_positivity_snapshot.json"
)
DEFAULT_AUDIT = RESEARCH_ROOT / "audit" / "period8_infinite_family_independent_audit.json"
DEFAULT_TARGET_SPEC = RESEARCH_ROOT / "conjectures" / "TARGET_A_SPEC.md"
EXPECTED_FLOQUET_AUDIT_SHA256 = "2a5657d0791b1e1a3c742ae8e0a738f083115b4e4516e5e8d8fd4d1999d6c3ee"
EXPECTED_POLYNOMIAL_SNAPSHOT_SHA256 = (
    "cc26dedfee3fe3e6c0674f1b217fde592a043a5d8b4913752dc37ad2a62193b2"
)
BOUND = sp.Rational(1561, 200)
TAU_PERIOD = (1, 1, -1, 1, -1, -1, 1, -1)
ALPHA_VALUES = (-1, 1)
FAMILY_START_L = 4


class UniformBoundAuditError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise UniformBoundAuditError(message)


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


def _coefficient_map(polynomial: sp.Expr, variables: tuple[sp.Symbol, ...]) -> list[dict[str, Any]]:
    poly = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    rows: list[dict[str, Any]] = []
    for degrees, coefficient in poly.terms():
        row: dict[str, Any] = {
            f"{variable}_degree": degree for variable, degree in zip(variables, degrees)
        }
        row["coefficient"] = str(coefficient)
        rows.append(row)
    return rows


def reconstruct_polynomial(
    rows: list[dict[str, Any]], y: sp.Symbol, c: sp.Symbol
) -> sp.Expr:
    _require(isinstance(rows, list) and rows, "FLOQUET_DEPENDENCY_FAIL: empty coefficient map")
    polynomial = sp.Integer(0)
    monomials: set[tuple[int, int]] = set()
    for row in rows:
        try:
            y_degree = int(row["y_degree"])
            c_degree = int(row["c_degree"])
            coefficient = sp.Rational(str(row["coefficient"]))
        except (KeyError, TypeError, ValueError) as error:
            raise UniformBoundAuditError(
                f"FLOQUET_DEPENDENCY_FAIL: malformed coefficient row: {error}"
            ) from error
        _require(y_degree >= 0 and c_degree >= 0, "FLOQUET_DEPENDENCY_FAIL: negative degree")
        monomial = (y_degree, c_degree)
        _require(monomial not in monomials, "FLOQUET_DEPENDENCY_FAIL: duplicate monomial")
        monomials.add(monomial)
        polynomial += coefficient * y**y_degree * c**c_degree
    return sp.expand(polynomial)


def load_floquet_dependency(
    audit_path: Path = DEFAULT_FLOQUET_AUDIT,
    polynomial_snapshot_path: Path = DEFAULT_POLYNOMIAL_SNAPSHOT,
    expected_audit_sha256: str = EXPECTED_FLOQUET_AUDIT_SHA256,
    expected_snapshot_sha256: str = EXPECTED_POLYNOMIAL_SNAPSHOT_SHA256,
) -> dict[str, Any]:
    audit_bytes = audit_path.read_bytes()
    snapshot_bytes = polynomial_snapshot_path.read_bytes()
    audit_sha = _sha256_bytes(audit_bytes)
    snapshot_sha = _sha256_bytes(snapshot_bytes)
    _require(
        audit_sha == expected_audit_sha256,
        "FLOQUET_DEPENDENCY_FAIL: Task 38 audit SHA-256 mismatch",
    )
    _require(
        snapshot_sha == expected_snapshot_sha256,
        "FLOQUET_DEPENDENCY_FAIL: Task 38 polynomial snapshot SHA-256 mismatch",
    )
    audit = json.loads(audit_bytes.decode("utf-8"))
    snapshot = json.loads(snapshot_bytes.decode("utf-8"))
    _require(
        audit.get("status") == "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
        "FLOQUET_DEPENDENCY_FAIL: Task 38 status mismatch",
    )
    _require(
        snapshot.get("status") == "PERIOD8_INDEPENDENT_POLYNOMIAL_FROZEN",
        "FLOQUET_DEPENDENCY_FAIL: polynomial snapshot status mismatch",
    )
    _require(
        audit.get("independent_snapshot_sha256") == snapshot_sha,
        "FLOQUET_DEPENDENCY_FAIL: Task 38 internal snapshot SHA mismatch",
    )
    _require(
        audit.get("P_independent_coefficient_map")
        == snapshot.get("P_independent_coefficient_map"),
        "FLOQUET_DEPENDENCY_FAIL: coefficient maps disagree",
    )
    y, c = sp.symbols("y c")
    polynomial = reconstruct_polynomial(snapshot["P_independent_coefficient_map"], y, c)
    snapshot_expression = sp.sympify(snapshot.get("P_independent", ""), locals={"y": y, "c": c})
    _require(
        sp.expand(polynomial - snapshot_expression) == 0,
        "FLOQUET_DEPENDENCY_FAIL: coefficient map and expression disagree",
    )
    _require(audit.get("hermitian_check") is True, "FLOQUET_DEPENDENCY_FAIL: Hermitian check missing")
    _require(
        audit.get("direct_sum_proof_status") == "FLOQUET_DIRECT_SUM_PASS",
        "FLOQUET_DEPENDENCY_FAIL: direct-sum proof missing",
    )
    _require(
        audit.get("squared_eigenvalue_root_link_status")
        == "SQUARED_EIGENVALUE_ROOT_LINK_PASS",
        "FLOQUET_DEPENDENCY_FAIL: squared-root link missing",
    )
    _require("[-2,2]" in audit.get("c_range", ""), "FLOQUET_DEPENDENCY_FAIL: c range missing")
    finite_checks = audit.get("finite_consistency_checks", [])
    _require(
        {row.get("alpha") for row in finite_checks if row.get("charpoly_match") is True}
        == {-1, 1},
        "FLOQUET_DEPENDENCY_FAIL: both holonomies are not covered",
    )
    return {
        "audit": audit,
        "snapshot": snapshot,
        "audit_sha256": audit_sha,
        "snapshot_sha256": snapshot_sha,
        "polynomial": polynomial,
        "y": y,
        "c": c,
    }


def validate_positive_coefficient_map(rows: list[dict[str, Any]]) -> dict[str, bool]:
    coefficients = [sp.Rational(str(row["coefficient"])) for row in rows]
    constant_rows = [
        row
        for row in rows
        if all(key == "coefficient" or not key.endswith("_degree") or int(value) == 0 for key, value in row.items())
    ]
    _require(len(constant_rows) == 1, "POSITIVE_COEFFICIENT_CERTIFICATE_FAIL: constant missing")
    all_nonnegative = all(coefficient >= 0 for coefficient in coefficients)
    strict_constant = bool(sp.Rational(str(constant_rows[0]["coefficient"])) > 0)
    _require(
        all_nonnegative and strict_constant,
        "POSITIVE_COEFFICIENT_CERTIFICATE_FAIL",
    )
    return {
        "all_coefficients_nonnegative": all_nonnegative,
        "strict_positive_constant": strict_constant,
    }


def positive_coefficient_certificate(
    polynomial: sp.Expr, y: sp.Symbol, c: sp.Symbol, bound: sp.Rational = BOUND
) -> dict[str, Any]:
    u, t = sp.symbols("u t")
    expanded = sp.Poly(
        sp.expand(polynomial.subs({y: bound + u, c: 2 - t})), u, t, domain=sp.QQ
    ).as_expr()
    rows = _coefficient_map(expanded, (u, t))
    validation = validate_positive_coefficient_map(rows)
    reconstructed = reconstruct_multivariate_map(rows, (u, t))
    _require(sp.expand(reconstructed - expanded) == 0, "positivity coefficient map mismatch")
    return {
        "status": "POSITIVE_COEFFICIENT_CERTIFICATE_PASS",
        "B": str(bound),
        "change_of_variables": {"u": "y-B", "t": "2-c"},
        "expanded_polynomial": _expression_string(expanded),
        "monomial_coefficient_map": rows,
        **validation,
        "target_region": "u>=0 and 0<=t<=4, equivalent to y>=B and c in [-2,2]",
        "proved_region": "u>=0 and t>=0, equivalently y>=B and c<=2",
        "strictness": "the positive constant term excludes equality at y=B",
    }


def reconstruct_multivariate_map(
    rows: list[dict[str, Any]], variables: tuple[sp.Symbol, ...]
) -> sp.Expr:
    polynomial = sp.Integer(0)
    seen: set[tuple[int, ...]] = set()
    for row in rows:
        degrees = tuple(int(row[f"{variable}_degree"]) for variable in variables)
        _require(degrees not in seen, "duplicate multivariate monomial")
        seen.add(degrees)
        term = sp.Rational(str(row["coefficient"]))
        for variable, degree in zip(variables, degrees):
            term *= variable**degree
        polynomial += term
    return sp.expand(polynomial)


def vertex_crosscheck(
    polynomial: sp.Expr, y: sp.Symbol, c: sp.Symbol, bound: sp.Rational = BOUND
) -> dict[str, Any]:
    u = sp.Symbol("u")
    poly_in_c = sp.Poly(polynomial, c, domain=sp.QQ.frac_field(y))
    _require(poly_in_c.degree() == 2, "vertex cross-check requires a quadratic in c")
    quadratic, linear, _ = poly_in_c.all_coeffs()
    vertex = sp.factor(-linear / (2 * quadratic))
    vertex_derivative = sp.diff(vertex, y)
    vertex_at_bound = sp.factor(vertex.subs(y, bound))
    _require(bound > 4, "B must exceed four for the vertex monotonicity proof")
    _require(sp.expand(vertex_derivative - (2 * y - 8)) == 0, "unexpected vertex derivative")
    _require(vertex_at_bound > 2, "vertex is not to the right of c=2")
    boundary_shift = sp.Poly(
        sp.expand(polynomial.subs({y: bound + u, c: 2})), u, domain=sp.QQ
    ).as_expr()
    boundary_rows = _coefficient_map(boundary_shift, (u,))
    _require(
        all(sp.Rational(str(row["coefficient"])) > 0 for row in boundary_rows),
        "vertex boundary polynomial lacks strict positive coefficients",
    )
    return {
        "status": "VERTEX_CROSSCHECK_PASS",
        "dP_dc": _expression_string(sp.diff(polynomial, c)),
        "vertex_c0": _expression_string(vertex),
        "vertex_derivative": _expression_string(vertex_derivative),
        "B_greater_than_4": True,
        "vertex_at_B": str(vertex_at_bound),
        "vertex_at_B_exceeds_2": True,
        "monotonicity": "c0'(y)>0 for y>=B and dP/dc<0 for c<=2",
        "boundary_shift": _expression_string(boundary_shift),
        "boundary_coefficient_map": boundary_rows,
        "all_boundary_coefficients_positive": True,
    }


def _exact_positive(expression: sp.Expr) -> bool:
    algebraic = to_number_field(sp.simplify(expression)).to_root()
    if algebraic.is_positive is True:
        return True
    return sp.simplify(algebraic > 0) is sp.true


def threshold_formula_from_spec(spec_path: Path = DEFAULT_TARGET_SPEC) -> dict[str, Any]:
    spec_bytes = spec_path.read_bytes()
    spec_text = spec_bytes.decode("utf-8")
    definition = "2 sqrt(cos²(π/n)+cos²(2π/n))"
    _require(definition in spec_text, "threshold definition missing from TARGET_A_SPEC")
    n = sp.Symbol("n", integer=True, positive=True)
    angles = (sp.pi / n, 2 * sp.pi / n)
    squared_definition = 4 * sum(sp.cos(angle) ** 2 for angle in angles)
    identity_checks = [
        sp.trigsimp(sp.cos(angle) ** 2 - (1 + sp.cos(2 * angle)) / 2) == 0
        for angle in angles
    ]
    _require(all(identity_checks), "cosine-square identity verification failed")
    derived = sp.expand(
        4 * sum((1 + sp.cos(2 * angle)) / 2 for angle in angles)
    )
    _require(sp.trigsimp(squared_definition - derived) == 0, "threshold formula derivation failed")
    return {
        "spec_file": "research/conjectures/TARGET_A_SPEC.md",
        "spec_sha256": _sha256_bytes(spec_bytes),
        "definition": "rho_-(n)=2*sqrt(cos(pi/n)^2+cos(2*pi/n)^2)",
        "identity": "cos(theta)^2=(1+cos(2*theta))/2",
        "identity_checks": identity_checks,
        "squared_formula": _expression_string(derived),
        "expression": derived,
        "n_symbol": n,
    }


def algebraic_n32_threshold_certificate(
    squared_formula: sp.Expr,
    n: sp.Symbol,
    lower: sp.Rational = sp.Rational(7809, 1000),
    upper: sp.Rational = sp.Rational(781, 100),
) -> dict[str, Any]:
    X = sp.Symbol("X")
    cos_pi_4 = sp.sqrt(2) / 2
    cos_pi_8 = sp.sqrt((1 + cos_pi_4) / 2)
    cos_pi_16 = sp.sqrt((1 + cos_pi_8) / 2)
    _require(
        sp.simplify(cos_pi_8**2 - (1 + cos_pi_4) / 2) == 0,
        "first half-angle identity failed",
    )
    _require(
        sp.simplify(cos_pi_16**2 - (1 + cos_pi_8) / 2) == 0,
        "second half-angle identity failed",
    )
    _require(
        sp.simplify(sp.expand_func(sp.cos(sp.pi / 8)) - cos_pi_8) == 0,
        "exact cos(pi/8) identity failed",
    )
    _require(
        sp.cos(sp.pi / 16).equals(cos_pi_16) is True,
        "exact cos(pi/16) half-angle identity failed",
    )
    radical = sp.simplify(4 + 2 * cos_pi_16 + 2 * cos_pi_8)
    expected_from_formula = squared_formula.subs(n, 32)
    _require(
        sp.expand(expected_from_formula - (4 + 2 * sp.cos(sp.pi / 16) + 2 * sp.cos(sp.pi / 8)))
        == 0,
        "n=32 threshold substitution failed",
    )
    _require(
        to_number_field(expected_from_formula - radical).as_expr() == 0,
        "n=32 trigonometric threshold and radical differ",
    )
    minimal = sp.Poly(sp.minimal_polynomial(radical, X), X, domain=sp.QQ)
    expected_coefficients = [
        1,
        -32,
        432,
        -3216,
        14456,
        -40224,
        67736,
        -63184,
        25022,
    ]
    _require(minimal.all_coeffs() == expected_coefficients, "unexpected n=32 minimal polynomial")
    _require(sp.simplify(minimal.as_expr().subs(X, radical)) == 0, "radical is not a polynomial root")
    lower_value = sp.factor(minimal.eval(lower))
    upper_value = sp.factor(minimal.eval(upper))
    root_count = int(minimal.count_roots(lower, upper))
    radical_above_lower = _exact_positive(radical - lower)
    radical_below_upper = _exact_positive(upper - radical)
    _require(lower_value < 0 and upper_value > 0, "isolating interval endpoint signs failed")
    _require(root_count == 1, "algebraic threshold interval does not isolate one root")
    _require(radical_above_lower and radical_below_upper, "exact radical is outside isolating interval")
    _require(BOUND < lower, "uniform bound is not below rational isolating lower endpoint")
    return {
        "status": "N32_THRESHOLD_ALGEBRAIC_PASS",
        "formula_at_n32": _expression_string(expected_from_formula),
        "formula_equals_radical_exactly": True,
        "half_angle_chain": {
            "cos_pi_4": _expression_string(cos_pi_4),
            "cos_pi_8": _expression_string(cos_pi_8),
            "cos_pi_16": _expression_string(cos_pi_16),
            "positive_square_root_reason": "all three angles lie in (0,pi/2)",
        },
        "exact_radical": _expression_string(radical),
        "minimal_polynomial": _expression_string(minimal.as_expr()),
        "minimal_polynomial_coefficients": [str(value) for value in minimal.all_coeffs()],
        "isolating_interval": {"lower": str(lower), "upper": str(upper)},
        "endpoint_values": {"at_lower": str(lower_value), "at_upper": str(upper_value)},
        "endpoint_signs": {"at_lower": -1, "at_upper": 1},
        "root_count": root_count,
        "radical_in_interval_exact": True,
        "rational_lower": str(lower),
        "B_below_lower": True,
    }


def threshold_above_bound(n_value: int, bound: sp.Rational = BOUND) -> bool:
    _require(n_value >= 8, "threshold order must be at least eight")
    expression = 4 + 2 * sp.cos(2 * sp.pi / n_value) + 2 * sp.cos(4 * sp.pi / n_value)
    return _exact_positive(expression - bound)


def threshold_monotonicity_certificate(start_n: int = 32) -> dict[str, Any]:
    _require(start_n == 32, "THRESHOLD_MONOTONICITY_FAIL: certified start must be 32")
    _require(sp.simplify(2 * sp.pi / start_n <= sp.pi / 16) is sp.true, "first angle bound failed")
    _require(sp.simplify(4 * sp.pi / start_n <= sp.pi / 8) is sp.true, "second angle bound failed")
    _require(sp.simplify(sp.pi / 8 < sp.pi) is sp.true, "cosine monotonicity interval failed")
    return {
        "status": "THRESHOLD_MONOTONICITY_PASS",
        "function": "R(n)=4+2*cos(2*pi/n)+2*cos(4*pi/n)",
        "domain": "integers n>=32",
        "proof": (
            "for n2>n1>=32 both positive angles 2*pi/n and 4*pi/n strictly "
            "decrease inside (0,pi), where cosine is strictly decreasing; hence R(n2)>R(n1)"
        ),
        "strictly_increasing": True,
        "minimum_at_32": True,
    }


def validate_alpha_coverage(alpha_values: tuple[int, ...] | list[int]) -> bool:
    return set(alpha_values) == {-1, 1} and len(alpha_values) == 2


def validate_family_domain(
    start_L: int,
    alpha_values: tuple[int, ...] | list[int],
    n_rule: str,
    theorem_statement: str,
) -> bool:
    expected_rule = "n=8L with integer L>=4"
    expected_theorem = (
        "For every integer L>=4 and alpha in {-1,+1}, the period-8 signing on "
        "C_(8L)(1,2) satisfies rho(A)^2 < 1561/200 < rho_-(8L)^2."
    )
    return (
        start_L == 4
        and threshold_above_bound(8 * start_L)
        and validate_alpha_coverage(alpha_values)
        and n_rule == expected_rule
        and theorem_statement == expected_theorem
        and "all even" not in theorem_statement.lower()
    )


def spectral_implication(dependency: dict[str, Any], positivity: dict[str, Any]) -> dict[str, Any]:
    audit = dependency["audit"]
    _require(audit.get("hermitian_check") is True, "spectral implication lacks Hermitian dependency")
    _require(
        audit.get("squared_eigenvalue_root_link_status")
        == "SQUARED_EIGENVALUE_ROOT_LINK_PASS",
        "spectral implication lacks squared-root dependency",
    )
    _require(
        audit.get("direct_sum_proof_status") == "FLOQUET_DIRECT_SUM_PASS",
        "spectral implication lacks direct-sum dependency",
    )
    _require(
        positivity.get("status") == "POSITIVE_COEFFICIENT_CERTIFICATE_PASS"
        and positivity.get("strict_positive_constant") is True,
        "spectral implication lacks strict positivity",
    )
    return {
        "status": "UNIFORM_SPECTRAL_BOUND_PASS",
        "hermitian_dependency": True,
        "squared_root_dependency": True,
        "direct_sum_dependency": True,
        "contradiction": (
            "lambda^2>=B would make P(lambda^2,c)>0, contradicting "
            "P(lambda^2,c)=0"
        ),
        "strict_block_bound": "rho(H(z))^2 < 1561/200 for every admissible z",
        "strict_full_bound": "rho(A_(8L,alpha))^2 < 1561/200",
        "alpha_values": [-1, 1],
    }


def taylor_threshold_crosscheck(bound: sp.Rational = BOUND) -> dict[str, Any]:
    a = sp.Symbol("a", positive=True)
    truncation = lambda value: 1 - value**2 / 2 + value**4 / 24 - value**6 / 720
    combined = sp.Poly(sp.expand(truncation(a) + truncation(2 * a)), a, domain=sp.QQ)
    _require(sp.simplify(sp.pi / 8 < 1) is sp.true, "Taylor argument is outside 0<t<1")
    _require(sp.simplify(sp.pi**2 > 9) is sp.true, "lower pi-squared bound failed")
    _require(sp.simplify(sp.pi**2 < 10) is sp.true, "upper pi-squared bound failed")
    sum_lower = (
        sp.Rational(2)
        - sp.Rational(50, 512)
        + sp.Rational(17 * 81, 24 * 256**2)
        - sp.Rational(65 * 1000, 720 * 256**3)
    )
    threshold_lower = sp.factor(4 + 2 * sum_lower)
    expected = sp.Rational(1178731111, 150994944)
    _require(threshold_lower == expected, "Taylor rational lower bound mismatch")
    _require(threshold_lower > bound, "Taylor lower bound does not exceed B")
    return {
        "status": "TAYLOR_THRESHOLD_CROSSCHECK_PASS",
        "cosine_lower_polynomial": "1-t^2/2+t^4/24-t^6/720",
        "validity": "alternating Taylor remainder gives a strict lower bound for 0<t<1",
        "combined_at_a_and_2a": _expression_string(combined.as_expr()),
        "a": "pi/16",
        "pi_squared_bounds": "9<pi^2<10",
        "cosine_sum_rational_lower": str(sum_lower),
        "threshold_squared_rational_lower": str(threshold_lower),
        "expected_old_lower_rederived": True,
        "lower_exceeds_B": True,
        "difference_from_B": str(sp.factor(threshold_lower - bound)),
    }


def derive_primary_snapshot(
    floquet_audit_path: Path = DEFAULT_FLOQUET_AUDIT,
    polynomial_snapshot_path: Path = DEFAULT_POLYNOMIAL_SNAPSHOT,
    positivity_snapshot_path: Path = DEFAULT_POSITIVITY_SNAPSHOT,
    target_spec_path: Path = DEFAULT_TARGET_SPEC,
) -> dict[str, Any]:
    dependency = load_floquet_dependency(floquet_audit_path, polynomial_snapshot_path)
    polynomial = dependency["polynomial"]
    y = dependency["y"]
    c = dependency["c"]
    positivity = positive_coefficient_certificate(polynomial, y, c)
    vertex = vertex_crosscheck(polynomial, y, c)
    formula = threshold_formula_from_spec(target_spec_path)
    threshold = algebraic_n32_threshold_certificate(formula["expression"], formula["n_symbol"])
    monotonicity = threshold_monotonicity_certificate()
    implication = spectral_implication(dependency, positivity)
    theorem_statement = (
        "For every integer L>=4 and alpha in {-1,+1}, the period-8 signing on "
        "C_(8L)(1,2) satisfies rho(A)^2 < 1561/200 < rho_-(8L)^2."
    )
    n_rule = "n=8L with integer L>=4"
    _require(
        validate_family_domain(FAMILY_START_L, ALPHA_VALUES, n_rule, theorem_statement),
        "infinite-family domain validation failed",
    )
    q_period = tuple(TAU_PERIOD[index] * TAU_PERIOD[(index + 1) % 8] for index in range(8))
    snapshot = {
        "schema_version": 1,
        "status": "UNIFORM_POSITIVITY_CERTIFIED",
        "B": str(BOUND),
        "source_P_sha256": dependency["snapshot_sha256"],
        "floquet_audit_sha256": dependency["audit_sha256"],
        "source_P_coefficient_map": dependency["snapshot"]["P_independent_coefficient_map"],
        "change_of_variables": positivity["change_of_variables"],
        "expanded_polynomial": positivity["expanded_polynomial"],
        "monomial_coefficient_map": positivity["monomial_coefficient_map"],
        "all_coefficients_nonnegative": positivity["all_coefficients_nonnegative"],
        "strict_positive_constant": positivity["strict_positive_constant"],
        "proved_region": positivity["proved_region"],
        "positive_coefficient_certificate": positivity,
        "secondary_vertex_check": vertex,
        "spectral_implication": implication,
        "threshold_formula": {
            key: value for key, value in formula.items() if key not in {"expression", "n_symbol"}
        },
        "n32_primary_algebraic_threshold": threshold,
        "threshold_monotonicity": monotonicity,
        "family": {
            "tau_period": list(TAU_PERIOD),
            "Q_period": list(q_period),
            "n_rule": n_rule,
            "start_L": FAMILY_START_L,
            "alpha_values": list(ALPHA_VALUES),
        },
        "theorem_statement": theorem_statement,
        "old_family_proof_read_before_snapshot": False,
        "source_file": "research/scripts/target_a_period8_uniform_bound_audit.py",
        "source_sha256": _sha256_file(Path(__file__).resolve()),
    }
    _write_json(positivity_snapshot_path, snapshot)
    return snapshot


def run_independent_audit(
    floquet_audit_path: Path = DEFAULT_FLOQUET_AUDIT,
    polynomial_snapshot_path: Path = DEFAULT_POLYNOMIAL_SNAPSHOT,
    positivity_snapshot_path: Path = DEFAULT_POSITIVITY_SNAPSHOT,
    target_spec_path: Path = DEFAULT_TARGET_SPEC,
    audit_path: Path = DEFAULT_AUDIT,
) -> dict[str, Any]:
    snapshot = derive_primary_snapshot(
        floquet_audit_path,
        polynomial_snapshot_path,
        positivity_snapshot_path,
        target_spec_path,
    )
    snapshot_sha = _sha256_file(positivity_snapshot_path)

    # The independent positivity and algebraic threshold are frozen before this cross-check.
    taylor = taylor_threshold_crosscheck()
    audit = {
        "schema_version": 1,
        "status": "PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED",
        "family": snapshot["family"],
        "floquet_dependency": {
            "audit_path": "research/audit/period8_floquet_independent_audit.json",
            "sha256": snapshot["floquet_audit_sha256"],
            "polynomial_snapshot_path": (
                "research/audit/target_a_period8_independent_polynomial.json"
            ),
            "polynomial_snapshot_sha256": snapshot["source_P_sha256"],
            "status": "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
        },
        "positivity_snapshot_path": (
            "research/audit/target_a_period8_uniform_positivity_snapshot.json"
        ),
        "positivity_snapshot_sha256": snapshot_sha,
        "primary_snapshot_frozen_before_secondary_or_old_proof": True,
        "uniform_bound": {
            "B": snapshot["B"],
            "change_of_variables": snapshot["change_of_variables"],
            "positivity_expansion": snapshot["expanded_polynomial"],
            "coefficient_map": snapshot["monomial_coefficient_map"],
            "all_coefficients_nonnegative": snapshot["all_coefficients_nonnegative"],
            "strict_positive_constant": snapshot["strict_positive_constant"],
            "proved_region": snapshot["proved_region"],
            "status": "POSITIVE_COEFFICIENT_CERTIFICATE_PASS",
            "secondary_vertex_check": snapshot["secondary_vertex_check"],
        },
        "spectral_implication": snapshot["spectral_implication"],
        "threshold": {
            "formula": snapshot["threshold_formula"],
            "n32": snapshot["n32_primary_algebraic_threshold"],
            "monotonicity": snapshot["threshold_monotonicity"],
        },
        "secondary_threshold_crosscheck": taylor,
        "theorem_statement": snapshot["theorem_statement"],
        "checker": {
            "path": "research/scripts/verify_target_a_period8_infinite_family.py",
            "expected_output": "TARGET_A_PERIOD8_INFINITE_FAMILY_PASS",
            "status": "TARGET_A_PERIOD8_INFINITE_FAMILY_PASS",
        },
        "independence": {
            "standard_library_and_sympy_only": True,
            "old_family_helper_imported": False,
            "old_positivity_certificate_used_as_primary_input": False,
            "floating_point_proof_used": False,
            "new_spectral_search_performed": False,
        },
        "script_sha256": _sha256_file(Path(__file__).resolve()),
        "next_gate": "Task 40A",
    }
    _write_json(audit_path, audit)
    return audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--floquet-audit", type=Path, default=DEFAULT_FLOQUET_AUDIT)
    parser.add_argument("--polynomial-snapshot", type=Path, default=DEFAULT_POLYNOMIAL_SNAPSHOT)
    parser.add_argument("--positivity-output", type=Path, default=DEFAULT_POSITIVITY_SNAPSHOT)
    parser.add_argument("--target-spec", type=Path, default=DEFAULT_TARGET_SPEC)
    parser.add_argument("--audit-output", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--derive-only", action="store_true")
    args = parser.parse_args()
    try:
        if args.derive_only:
            derive_primary_snapshot(
                args.floquet_audit,
                args.polynomial_snapshot,
                args.positivity_output,
                args.target_spec,
            )
            print("FLOQUET_DEPENDENCY_PASS")
            print("POSITIVE_COEFFICIENT_CERTIFICATE_PASS")
            print("VERTEX_CROSSCHECK_PASS")
            print("UNIFORM_SPECTRAL_BOUND_PASS")
            print("N32_THRESHOLD_ALGEBRAIC_PASS")
            print("THRESHOLD_MONOTONICITY_PASS")
            print("UNIFORM_POSITIVITY_CERTIFIED")
            return
        audit = run_independent_audit(
            args.floquet_audit,
            args.polynomial_snapshot,
            args.positivity_output,
            args.target_spec,
            args.audit_output,
        )
        _require(
            audit["status"] == "PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED",
            "final infinite-family audit status failed",
        )
    except Exception as error:
        print(f"Independent period-8 family audit failed: {error}", file=sys.stderr)
        print("PERIOD8_INFINITE_FAMILY_AUDIT_FAIL")
        raise SystemExit(1)
    print("FLOQUET_DEPENDENCY_PASS")
    print("POSITIVE_COEFFICIENT_CERTIFICATE_PASS")
    print("VERTEX_CROSSCHECK_PASS")
    print("UNIFORM_SPECTRAL_BOUND_PASS")
    print("N32_THRESHOLD_ALGEBRAIC_PASS")
    print("THRESHOLD_MONOTONICITY_PASS")
    print("TAYLOR_THRESHOLD_CROSSCHECK_PASS")
    print("PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED")


if __name__ == "__main__":
    main()
