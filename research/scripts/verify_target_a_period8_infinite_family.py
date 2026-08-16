"""Verify the frozen Task 38 and Task 39 infinite-family evidence chain."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.polys.numberfields import to_number_field


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUDIT = RESEARCH_ROOT / "audit" / "period8_infinite_family_independent_audit.json"
DEFAULT_POSITIVITY = (
    RESEARCH_ROOT / "audit" / "target_a_period8_uniform_positivity_snapshot.json"
)
DEFAULT_FLOQUET = RESEARCH_ROOT / "audit" / "period8_floquet_independent_audit.json"
DEFAULT_POLYNOMIAL = RESEARCH_ROOT / "audit" / "target_a_period8_independent_polynomial.json"
BOUND = sp.Rational(1561, 200)
EXPECTED_THEOREM = (
    "For every integer L>=4 and alpha in {-1,+1}, the period-8 signing on "
    "C_(8L)(1,2) satisfies rho(A)^2 < 1561/200 < rho_-(8L)^2."
)


class InfiniteFamilyVerificationError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise InfiniteFamilyVerificationError(message)


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


def _map_expression(rows: list[dict[str, Any]], variables: tuple[sp.Symbol, ...]) -> sp.Expr:
    result = sp.Integer(0)
    monomials: set[tuple[int, ...]] = set()
    for row in rows:
        degrees = tuple(int(row[f"{variable}_degree"]) for variable in variables)
        _require(degrees not in monomials, "duplicate positivity monomial")
        monomials.add(degrees)
        term = sp.Rational(str(row["coefficient"]))
        for variable, degree in zip(variables, degrees):
            term *= variable**degree
        result += term
    return sp.expand(result)


def verify_infinite_family(
    audit_path: Path = DEFAULT_AUDIT,
    positivity_path: Path = DEFAULT_POSITIVITY,
    floquet_path: Path = DEFAULT_FLOQUET,
    polynomial_path: Path = DEFAULT_POLYNOMIAL,
) -> dict[str, Any]:
    audit_raw, audit = _read_json(audit_path)
    positivity_raw, positivity = _read_json(positivity_path)
    floquet_raw, floquet = _read_json(floquet_path)
    polynomial_raw, polynomial = _read_json(polynomial_path)

    _require(
        audit.get("status") == "PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED",
        "Task 39 audit status mismatch",
    )
    dependency = audit.get("floquet_dependency", {})
    _require(_sha256(floquet_raw) == dependency.get("sha256"), "Task 38 audit SHA mismatch")
    _require(
        _sha256(polynomial_raw) == dependency.get("polynomial_snapshot_sha256"),
        "Task 38 polynomial SHA mismatch",
    )
    _require(
        _sha256(positivity_raw) == audit.get("positivity_snapshot_sha256"),
        "Task 39 positivity snapshot SHA mismatch",
    )
    _require(
        floquet.get("status") == "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
        "Floquet status mismatch",
    )
    _require(
        polynomial.get("status") == "PERIOD8_INDEPENDENT_POLYNOMIAL_FROZEN",
        "polynomial snapshot status mismatch",
    )
    _require(
        positivity.get("status") == "UNIFORM_POSITIVITY_CERTIFIED",
        "positivity snapshot status mismatch",
    )
    _require(
        positivity.get("floquet_audit_sha256") == _sha256(floquet_raw)
        and positivity.get("source_P_sha256") == _sha256(polynomial_raw),
        "positivity dependency hashes mismatch",
    )
    _require(
        positivity.get("source_P_coefficient_map")
        == polynomial.get("P_independent_coefficient_map")
        == floquet.get("P_independent_coefficient_map"),
        "audited polynomial maps disagree",
    )
    _require(
        floquet.get("hermitian_check") is True
        and floquet.get("direct_sum_proof_status") == "FLOQUET_DIRECT_SUM_PASS"
        and floquet.get("squared_eigenvalue_root_link_status")
        == "SQUARED_EIGENVALUE_ROOT_LINK_PASS",
        "Floquet logical dependencies are incomplete",
    )

    uniform = audit.get("uniform_bound", {})
    rows = uniform.get("coefficient_map", [])
    u, t = sp.symbols("u t")
    expansion = _map_expression(rows, (u, t))
    _require(
        sp.expand(
            expansion
            - sp.sympify(uniform.get("positivity_expansion", ""), locals={"u": u, "t": t})
        )
        == 0,
        "positivity expansion and map disagree",
    )
    coefficients = [sp.Rational(str(row["coefficient"])) for row in rows]
    constants = [
        sp.Rational(str(row["coefficient"]))
        for row in rows
        if int(row["u_degree"]) == 0 and int(row["t_degree"]) == 0
    ]
    _require(len(constants) == 1, "positivity constant missing")
    _require(all(value >= 0 for value in coefficients), "negative positivity coefficient")
    _require(constants[0] > 0, "positivity constant is not strict")
    _require(
        uniform.get("status") == "POSITIVE_COEFFICIENT_CERTIFICATE_PASS"
        and uniform.get("secondary_vertex_check", {}).get("status") == "VERTEX_CROSSCHECK_PASS",
        "uniform positivity statuses are incomplete",
    )

    implication = audit.get("spectral_implication", {})
    _require(
        implication.get("status") == "UNIFORM_SPECTRAL_BOUND_PASS"
        and implication.get("hermitian_dependency") is True
        and implication.get("squared_root_dependency") is True
        and implication.get("direct_sum_dependency") is True,
        "spectral implication is incomplete",
    )

    threshold = audit.get("threshold", {})
    n32 = threshold.get("n32", {})
    X = sp.Symbol("X")
    minimal = sp.Poly(
        sum(
            sp.Rational(coefficient) * X ** (len(n32["minimal_polynomial_coefficients"]) - index - 1)
            for index, coefficient in enumerate(n32["minimal_polynomial_coefficients"])
        ),
        X,
        domain=sp.QQ,
    )
    parsed_minimal = sp.Poly(sp.sympify(n32["minimal_polynomial"], locals={"X": X}), X)
    _require(
        sp.expand(minimal.as_expr() - parsed_minimal.as_expr()) == 0,
        "minimal polynomial fields disagree",
    )
    lower = sp.Rational(n32["isolating_interval"]["lower"])
    upper = sp.Rational(n32["isolating_interval"]["upper"])
    _require(lower < upper and BOUND < lower, "invalid threshold rational ordering")
    _require(minimal.eval(lower) < 0 and minimal.eval(upper) > 0, "threshold endpoint signs fail")
    _require(int(minimal.count_roots(lower, upper)) == 1, "threshold interval does not isolate one root")
    radical = sp.sympify(n32["exact_radical"])
    _require(sp.simplify(minimal.as_expr().subs(X, radical)) == 0, "radical is not a minimal root")
    _require(
        _exact_positive(radical - lower) and _exact_positive(upper - radical),
        "radical is outside the exact isolating interval",
    )
    _require(
        n32.get("status") == "N32_THRESHOLD_ALGEBRAIC_PASS"
        and n32.get("formula_equals_radical_exactly") is True,
        "primary n=32 threshold status fails",
    )
    monotonicity = threshold.get("monotonicity", {})
    _require(
        monotonicity.get("status") == "THRESHOLD_MONOTONICITY_PASS"
        and monotonicity.get("strictly_increasing") is True
        and monotonicity.get("minimum_at_32") is True,
        "threshold monotonicity status fails",
    )
    secondary = audit.get("secondary_threshold_crosscheck", {})
    _require(
        secondary.get("status") == "TAYLOR_THRESHOLD_CROSSCHECK_PASS"
        and sp.Rational(secondary["threshold_squared_rational_lower"]) > BOUND,
        "secondary threshold cross-check fails",
    )

    family = audit.get("family", {})
    tau = tuple(family.get("tau_period", []))
    expected_q = tuple(tau[index] * tau[(index + 1) % 8] for index in range(8))
    _require(len(tau) == 8 and all(value in (-1, 1) for value in tau), "invalid tau family")
    _require(tuple(family.get("Q_period", [])) == expected_q, "Q period mismatch")
    _require(
        family.get("start_L") == 4
        and family.get("n_rule") == "n=8L with integer L>=4",
        "family start or n rule mismatch",
    )
    _require(set(family.get("alpha_values", [])) == {-1, 1}, "both holonomies are not covered")
    _require(audit.get("theorem_statement") == EXPECTED_THEOREM, "theorem domain mismatch")
    _require("all even" not in audit["theorem_statement"].lower(), "overbroad theorem domain")
    _require(
        audit.get("checker", {}).get("status") == "TARGET_A_PERIOD8_INFINITE_FAMILY_PASS",
        "checker status field mismatch",
    )
    return {
        "status": "TARGET_A_PERIOD8_INFINITE_FAMILY_PASS",
        "audit_sha256": _sha256(audit_raw),
        "floquet_dependency_verified": True,
        "positivity_dependency_verified": True,
        "algebraic_threshold_verified": True,
        "family_domain_verified": True,
        "alpha_values_verified": [-1, 1],
    }


def main() -> None:
    try:
        report = verify_infinite_family()
        _require(
            report["status"] == "TARGET_A_PERIOD8_INFINITE_FAMILY_PASS",
            "final checker status failed",
        )
    except Exception as error:
        print(f"Target A period-8 infinite-family verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_INFINITE_FAMILY_FAIL")
        raise SystemExit(1)
    print("TARGET_A_PERIOD8_INFINITE_FAMILY_PASS")


if __name__ == "__main__":
    main()
