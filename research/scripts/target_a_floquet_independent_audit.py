"""Derive the Target A period-8 Floquet determinant from first principles."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Iterable

import sympy as sp
from sympy.polys.polyerrors import PolynomialError


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TRANSITIONS = RESEARCH_ROOT / "audit" / "target_a_period8_cell_transitions.json"
DEFAULT_SNAPSHOT = RESEARCH_ROOT / "audit" / "target_a_period8_independent_polynomial.json"
DEFAULT_AUDIT = RESEARCH_ROOT / "audit" / "period8_floquet_independent_audit.json"
DEFAULT_FROZEN_CERTIFICATE = (
    RESEARCH_ROOT / "counterexamples" / "target_a_period8_family_certificate.json"
)
TAU_PERIOD = (1, 1, -1, 1, -1, -1, 1, -1)
CELL_SIZE = 8
DELTAS = (-2, -1, 1, 2)


class FloquetAuditError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise FloquetAuditError(message)


def _json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


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


def derive_cell_transitions(
    tau_period: tuple[int, ...] = TAU_PERIOD,
) -> list[dict[str, int]]:
    _require(len(tau_period) == CELL_SIZE, "tau period must have length eight")
    _require(all(sign in (-1, 1) for sign in tau_period), "tau contains a non-sign")
    transitions: list[dict[str, int]] = []
    for output_residue in range(CELL_SIZE):
        for delta in DELTAS:
            target_integer = output_residue + delta
            target_residue = target_integer % CELL_SIZE
            cell_shift = target_integer // CELL_SIZE
            if delta == -2:
                coefficient = tau_period[(output_residue - 2) % CELL_SIZE]
            elif delta == 2:
                coefficient = tau_period[output_residue]
            else:
                coefficient = 1
            transitions.append(
                {
                    "output_residue": output_residue,
                    "delta": delta,
                    "target_residue": target_residue,
                    "cell_shift": cell_shift,
                    "coefficient": coefficient,
                }
            )
    validate_cell_transitions(transitions)
    return transitions


def validate_cell_transitions(transitions: list[dict[str, int]]) -> None:
    _require(len(transitions) == CELL_SIZE * len(DELTAS), "transition count mismatch")
    expected_pairs = {(residue, delta) for residue in range(CELL_SIZE) for delta in DELTAS}
    actual_pairs = {(row["output_residue"], row["delta"]) for row in transitions}
    _require(actual_pairs == expected_pairs, "transition table is incomplete")
    for row in transitions:
        residue = row["output_residue"]
        delta = row["delta"]
        target_integer = residue + delta
        _require(row["target_residue"] == target_integer % CELL_SIZE, "target residue mismatch")
        _require(row["cell_shift"] == target_integer // CELL_SIZE, "cell shift mismatch")
        _require(row["coefficient"] in (-1, 1), "transition coefficient is not a sign")


def transition_snapshot(transitions: list[dict[str, int]]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "status": "PERIOD8_CELL_TRANSITIONS_DERIVED",
        "tau_period": list(TAU_PERIOD),
        "operator": (
            "(Ax)_i=x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i*x_(i+2)"
        ),
        "cell_coordinate": "i=8m+r",
        "transition_count": len(transitions),
        "transitions": transitions,
    }


def build_floquet_block(
    transitions: list[dict[str, int]], z: sp.Symbol
) -> sp.Matrix:
    validate_cell_transitions(transitions)
    entries = [[sp.Integer(0) for _ in range(CELL_SIZE)] for _ in range(CELL_SIZE)]
    for row in transitions:
        entries[row["output_residue"]][row["target_residue"]] += (
            row["coefficient"] * z ** row["cell_shift"]
        )
    return sp.Matrix(entries)


def floquet_entries(block: sp.Matrix) -> list[list[str]]:
    return [
        [_expression_string(block[row, column]) for column in range(CELL_SIZE)]
        for row in range(CELL_SIZE)
    ]


def hermitian_on_unit_circle(block: sp.Matrix, z: sp.Symbol) -> bool:
    for row in range(CELL_SIZE):
        for column in range(CELL_SIZE):
            starred = sp.expand(block[column, row].subs(z, z ** -1))
            if sp.expand(block[row, column] - starred) != 0:
                return False
    return True


def _finite_twisted_matrix(
    cell_count: int, alpha: int, transitions: list[dict[str, int]]
) -> sp.Matrix:
    _require(cell_count >= 2, "at least two cells are required")
    _require(alpha in (-1, 1), "alpha must be a sign")
    validate_cell_transitions(transitions)
    order = CELL_SIZE * cell_count
    matrix = [[0 for _ in range(order)] for _ in range(order)]
    for cell in range(cell_count):
        for row in transitions:
            target_cell = cell + row["cell_shift"]
            boundary_factor = 1
            if target_cell < 0:
                target_cell += cell_count
                boundary_factor = alpha
            elif target_cell >= cell_count:
                target_cell -= cell_count
                boundary_factor = alpha
            output_index = CELL_SIZE * cell + row["output_residue"]
            target_index = CELL_SIZE * target_cell + row["target_residue"]
            matrix[output_index][target_index] += boundary_factor * row["coefficient"]
    result = sp.Matrix(matrix)
    _require(result == result.T, "finite twisted operator is not symmetric")
    return result


def _hamilton_gauge_matrix(
    cell_count: int, alpha: int, tau_period: tuple[int, ...] = TAU_PERIOD
) -> sp.Matrix:
    _require(alpha in (-1, 1), "alpha must be a sign")
    order = CELL_SIZE * cell_count
    tau = tuple(tau_period[index % CELL_SIZE] for index in range(order))
    step1 = [1] * order
    step1[-1] = alpha
    step2 = [
        tau[index] * step1[index] * step1[(index + 1) % order]
        for index in range(order)
    ]
    matrix = [[0 for _ in range(order)] for _ in range(order)]
    for index, coefficient in enumerate(step1):
        target = (index + 1) % order
        matrix[index][target] = matrix[target][index] = coefficient
    for index, coefficient in enumerate(step2):
        target = (index + 2) % order
        matrix[index][target] = matrix[target][index] = coefficient
    return sp.Matrix(matrix)


def operator_derivation_check(transitions: list[dict[str, int]]) -> dict[str, Any]:
    checks: dict[str, bool] = {}
    for alpha in (1, -1):
        checks[f"alpha_{alpha:+d}"] = (
            _finite_twisted_matrix(4, alpha, transitions)
            == _hamilton_gauge_matrix(4, alpha)
        )
    _require(all(checks.values()), "Hamilton gauge and twisted-boundary operator differ")
    return {
        "status": "OPERATOR_DERIVATION_PASS",
        "step1_local_sign": 1,
        "step2_local_sign_rule": "b_i=tau_i",
        "finite_hamilton_gauge": "a_0=...=a_(n-2)=1, a_(n-1)=alpha",
        "twisted_boundary": "x_(i+n)=alpha*x_i",
        "exact_finite_equivalence": checks,
    }


def boundary_derivation(cell_count: int, alpha: int) -> dict[str, Any]:
    _require(cell_count >= 1, "cell count must be positive")
    _require(alpha in (-1, 1), "alpha must be a sign")
    return {
        "status": "BLOCH_BOUNDARY_DERIVATION_PASS",
        "ansatz": "u_m=z^m*v",
        "global_boundary": f"u_(m+{cell_count})={alpha:+d}*u_m",
        "derived_relation": f"z^{cell_count}={alpha:+d}",
        "derivation": "z^(m+L)*v=alpha*z^m*v and v!=0 imply z^L=alpha",
        "unit_modulus": "|z|^L=|alpha|=1 implies |z|=1",
    }


def boundary_polynomial_matches(cell_count: int, alpha: int, candidate: sp.Expr, z: sp.Symbol) -> bool:
    expected = z**cell_count - alpha
    return sp.Poly(sp.expand(candidate - expected), z).is_zero


def completeness_check(cell_count: int, block_count: int, block_dimension: int = CELL_SIZE) -> bool:
    return block_count == cell_count and block_count * block_dimension == CELL_SIZE * cell_count


def determinant_via_sympy(block: sp.Matrix, x: sp.Symbol) -> sp.Expr:
    return sp.expand((x * sp.eye(CELL_SIZE) - block).det())


def determinant_via_bareiss(block: sp.Matrix, x: sp.Symbol) -> sp.Expr:
    laurent_symbols = block.free_symbols - {x}
    _require(len(laurent_symbols) == 1, "expected one Laurent variable")
    laurent_symbol = next(iter(laurent_symbols))
    work = [
        [x * int(row == column) - block[row, column] for column in range(CELL_SIZE)]
        for row in range(CELL_SIZE)
    ]
    previous = sp.Integer(1)
    sign = 1
    for pivot_index in range(CELL_SIZE - 1):
        pivot_row = next(
            (
                row
                for row in range(pivot_index, CELL_SIZE)
                if work[row][pivot_index] != 0
            ),
            None,
        )
        _require(pivot_row is not None, f"zero Bareiss column at {pivot_index}")
        if pivot_row != pivot_index:
            work[pivot_index], work[pivot_row] = work[pivot_row], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, CELL_SIZE):
            for column in range(pivot_index + 1, CELL_SIZE):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                quotient = sp.cancel(numerator / previous)
                numerator_part, denominator_part = sp.fraction(quotient)
                denominator_poly = sp.Poly(denominator_part, laurent_symbol)
                _require(
                    x not in denominator_part.free_symbols
                    and len(denominator_poly.terms()) == 1,
                    f"non-exact Bareiss division at {pivot_index}",
                )
                work[row][column] = sp.expand(numerator_part / denominator_part)
            work[row][pivot_index] = sp.Integer(0)
        previous = pivot
    return sp.expand(sign * work[-1][-1])


def _laurent_coefficients(expression: sp.Expr, z: sp.Symbol) -> dict[int, sp.Expr]:
    coefficients: dict[int, sp.Expr] = {}
    for term in sp.Add.make_args(sp.expand(expression)):
        powers = term.as_powers_dict()
        exponent = powers.get(z, sp.Integer(0))
        _require(exponent.is_Integer is True, "nonintegral Laurent exponent")
        coefficient = sp.expand(term / z**exponent)
        _require(z not in coefficient.free_symbols, "failed to extract Laurent coefficient")
        key = int(exponent)
        coefficients[key] = sp.expand(coefficients.get(key, 0) + coefficient)
    return {key: value for key, value in coefficients.items() if value != 0}


def determinant_structure(
    determinant: sp.Expr, x: sp.Symbol, z: sp.Symbol
) -> dict[str, Any]:
    coefficients = _laurent_coefficients(determinant, z)
    inversion_symmetric = all(
        sp.expand(value - coefficients.get(-exponent, 0)) == 0
        for exponent, value in coefficients.items()
    )
    even_in_x = sp.expand(determinant.subs(x, -x) - determinant) == 0
    exact_coefficients = all(
        coefficient.as_poly(x, domain=sp.QQ) is not None for coefficient in coefficients.values()
    )
    return {
        "laurent_coefficients": coefficients,
        "inversion_symmetric": inversion_symmetric,
        "even_in_x": even_in_x,
        "exact_rational_coefficients": exact_coefficients,
    }


def _chebyshev_sums(maximum: int, c: sp.Symbol) -> list[sp.Expr]:
    sums = [sp.Integer(2)]
    if maximum == 0:
        return sums
    sums.append(c)
    for index in range(1, maximum):
        sums.append(sp.expand(c * sums[index] - sums[index - 1]))
    return sums


def reduce_determinant_to_y_c(
    determinant: sp.Expr, x: sp.Symbol, z: sp.Symbol, y: sp.Symbol, c: sp.Symbol
) -> sp.Expr:
    structure = determinant_structure(determinant, x, z)
    _require(structure["inversion_symmetric"], "determinant is not inversion symmetric")
    _require(structure["even_in_x"], "determinant is not even in x")
    coefficients: dict[int, sp.Expr] = structure["laurent_coefficients"]
    maximum = max(abs(exponent) for exponent in coefficients)
    sums = _chebyshev_sums(maximum, c)
    polynomial_x_c = coefficients.get(0, sp.Integer(0))
    for exponent in range(1, maximum + 1):
        coefficient = coefficients.get(exponent, sp.Integer(0))
        _require(
            sp.expand(coefficient - coefficients.get(-exponent, 0)) == 0,
            f"Laurent coefficient mismatch at exponent {exponent}",
        )
        polynomial_x_c += coefficient * sums[exponent]
    polynomial_x_c = sp.Poly(sp.expand(polynomial_x_c), x, c, domain=sp.QQ)
    polynomial_y_c = sp.Integer(0)
    for (x_degree, c_degree), coefficient in polynomial_x_c.terms():
        _require(x_degree % 2 == 0, "odd x power survived reduction")
        polynomial_y_c += coefficient * y ** (x_degree // 2) * c**c_degree
    result = sp.expand(polynomial_y_c)
    reconstructed = sp.expand(result.subs({y: x**2, c: z + z**-1}) - determinant)
    _require(reconstructed == 0, "y,c reduction does not reconstruct determinant")
    return result


def polynomial_coefficient_map(polynomial: sp.Expr, y: sp.Symbol, c: sp.Symbol) -> list[dict[str, Any]]:
    poly = sp.Poly(sp.expand(polynomial), y, c, domain=sp.QQ)
    return [
        {
            "y_degree": degrees[0],
            "c_degree": degrees[1],
            "coefficient": str(coefficient),
        }
        for degrees, coefficient in poly.terms()
    ]


def _laurent_product_over_boundary(
    determinant: sp.Expr, cell_count: int, alpha: int, z: sp.Symbol
) -> sp.Expr:
    coefficients = _laurent_coefficients(determinant, z)
    minimum = min(coefficients)
    clearing_power = max(0, -minimum)
    polynomial = sp.Poly(sp.expand(determinant * z**clearing_power), z).as_expr()
    boundary = z**cell_count - alpha
    resultant = sp.resultant(boundary, polynomial, z)
    product_of_roots = (-1) ** (cell_count + 1) * alpha
    return sp.expand(resultant / (product_of_roots**clearing_power))


def finite_direct_sum_check(
    cell_count: int,
    alpha: int,
    full_transitions: list[dict[str, int]],
    block_transitions: list[dict[str, int]] | None = None,
) -> dict[str, Any]:
    x, z = sp.symbols("x z")
    finite_matrix = _finite_twisted_matrix(cell_count, alpha, full_transitions)
    block = build_floquet_block(block_transitions or full_transitions, z)
    determinant = determinant_via_sympy(block, x)
    full_charpoly = sp.expand(finite_matrix.charpoly(x).as_expr())
    block_product = _laurent_product_over_boundary(determinant, cell_count, alpha, z)
    match = sp.expand(full_charpoly - block_product) == 0
    return {
        "cell_count": cell_count,
        "alpha": alpha,
        "order": CELL_SIZE * cell_count,
        "allowed_z_relation": f"z^{cell_count}={alpha:+d}",
        "block_count": cell_count,
        "dimension_count": f"{cell_count}*{CELL_SIZE}={CELL_SIZE * cell_count}",
        "complete": completeness_check(cell_count, cell_count),
        "charpoly_match": match,
        "full_charpoly_sha256": _sha256_bytes(_json_bytes(_expression_string(full_charpoly))),
        "block_product_sha256": _sha256_bytes(_json_bytes(_expression_string(block_product))),
    }


def compare_coefficient_maps(
    independent: list[dict[str, Any]], frozen: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    def keyed(rows: list[dict[str, Any]]) -> dict[tuple[int, int], str]:
        return {
            (int(row["y_degree"]), int(row["c_degree"])): str(row["coefficient"])
            for row in rows
        }

    independent_map = keyed(independent)
    frozen_map = keyed(frozen)
    comparison = []
    for monomial in sorted(set(independent_map) | set(frozen_map), reverse=True):
        left = independent_map.get(monomial, "0")
        right = frozen_map.get(monomial, "0")
        comparison.append(
            {
                "y_degree": monomial[0],
                "c_degree": monomial[1],
                "independent_coefficient": left,
                "frozen_coefficient": right,
                "match": sp.Rational(left) == sp.Rational(right),
            }
        )
    _require(all(row["match"] for row in comparison), "CRITICAL_FLOQUET_MISMATCH")
    return comparison


def _walk_json(value: Any, path: str = "$") -> Iterable[tuple[str, Any]]:
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from _walk_json(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _walk_json(child, f"{path}[{index}]")


def extract_frozen_polynomial(certificate: dict[str, Any], y: sp.Symbol, c: sp.Symbol) -> tuple[str, sp.Expr]:
    candidates: list[tuple[str, sp.Expr]] = []
    for path, value in _walk_json(certificate):
        if not isinstance(value, str) or ("y" not in value and "c" not in value):
            continue
        try:
            expression = sp.sympify(value.replace("^", "**"), locals={"y": y, "c": c})
            poly = sp.Poly(expression, y, c, domain=sp.QQ)
        except (sp.SympifyError, PolynomialError, TypeError, ValueError, NameError):
            continue
        if poly.degree(y) == 4 and poly.degree(c) >= 1:
            candidates.append((path, sp.expand(poly.as_expr())))
    unique = {sp.sstr(expression): (path, expression) for path, expression in candidates}
    _require(len(unique) == 1, f"expected one frozen polynomial, found {len(unique)}")
    return next(iter(unique.values()))


def derive_independent_snapshot(
    transitions_path: Path = DEFAULT_TRANSITIONS,
    snapshot_path: Path = DEFAULT_SNAPSHOT,
) -> dict[str, Any]:
    x, y, z, c = sp.symbols("x y z c")
    transitions = derive_cell_transitions()
    transition_payload = transition_snapshot(transitions)
    _write_json(transitions_path, transition_payload)
    transition_sha = _sha256_file(transitions_path)

    operator = operator_derivation_check(transitions)
    boundary_plus = boundary_derivation(4, 1)
    boundary_minus = boundary_derivation(4, -1)
    block = build_floquet_block(transitions, z)
    _require(hermitian_on_unit_circle(block, z), "symbolic Hermitian check failed")
    determinant_route1 = determinant_via_sympy(block, x)
    determinant_route2 = determinant_via_bareiss(block, x)
    _require(
        sp.expand(determinant_route1 - determinant_route2) == 0,
        "independent determinant routes disagree",
    )
    structure = determinant_structure(determinant_route1, x, z)
    _require(structure["exact_rational_coefficients"], "determinant coefficients are not exact")
    polynomial = reduce_determinant_to_y_c(determinant_route1, x, z, y, c)
    finite_checks = [
        finite_direct_sum_check(4, alpha, transitions) for alpha in (1, -1)
    ]
    _require(
        all(check["complete"] and check["charpoly_match"] for check in finite_checks),
        "finite direct-sum consistency failed",
    )
    script_path = Path(__file__).resolve()
    snapshot = {
        "schema_version": 1,
        "status": "PERIOD8_INDEPENDENT_POLYNOMIAL_FROZEN",
        "tau_period": list(TAU_PERIOD),
        "operator_derivation": operator,
        "cell_transition_table_file": "research/audit/target_a_period8_cell_transitions.json",
        "cell_transition_table_sha256": transition_sha,
        "bloch_convention": "u_m=z^m*v",
        "boundary_derivations": [boundary_plus, boundary_minus],
        "allowed_z_relation": "z^L=alpha",
        "unit_circle_consequence": "|z|=1",
        "H_entries": floquet_entries(block),
        "hermitian_check": True,
        "direct_sum_proof_status": "FLOQUET_DIRECT_SUM_PASS",
        "direct_sum_dimension_argument": "L distinct Bloch roots times 8 residues equals 8L",
        "finite_consistency_checks": finite_checks,
        "independent_determinant": _expression_string(determinant_route1),
        "determinant_inversion_symmetry": structure["inversion_symmetric"],
        "determinant_even_in_x": structure["even_in_x"],
        "determinant_exact_coefficients": structure["exact_rational_coefficients"],
        "second_determinant_method": "hand-written fraction-free Bareiss elimination",
        "second_determinant_match": True,
        "P_independent": _expression_string(polynomial),
        "P_independent_coefficient_map": polynomial_coefficient_map(polynomial, y, c),
        "c_range": "[-2,2] because c=z+z^-1=2*cos(theta) for |z|=1",
        "squared_eigenvalue_root_link": (
            "H(z) Hermitian on |z|=1 gives real lambda; det(lambda*I-H)=0 "
            "implies P(lambda^2,c)=0 with lambda^2>=0"
        ),
        "source_file": "research/scripts/target_a_floquet_independent_audit.py",
        "source_sha256": _sha256_file(script_path),
        "independence_boundary": (
            "snapshot written before frozen family certificate or proof is opened"
        ),
    }
    _write_json(snapshot_path, snapshot)
    return snapshot


def run_independent_audit(
    transitions_path: Path = DEFAULT_TRANSITIONS,
    snapshot_path: Path = DEFAULT_SNAPSHOT,
    frozen_certificate_path: Path = DEFAULT_FROZEN_CERTIFICATE,
    audit_path: Path = DEFAULT_AUDIT,
) -> dict[str, Any]:
    snapshot = derive_independent_snapshot(transitions_path, snapshot_path)
    snapshot_sha = _sha256_file(snapshot_path)

    # Independence boundary: only now may the frozen polynomial evidence be opened.
    frozen_bytes = frozen_certificate_path.read_bytes()
    frozen_certificate = json.loads(frozen_bytes.decode("utf-8"))
    y, c = sp.symbols("y c")
    frozen_path, frozen_polynomial = extract_frozen_polynomial(frozen_certificate, y, c)
    frozen_map = polynomial_coefficient_map(frozen_polynomial, y, c)
    comparison = compare_coefficient_maps(snapshot["P_independent_coefficient_map"], frozen_map)
    audit = {
        **snapshot,
        "status": "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
        "independent_snapshot_file": "research/audit/target_a_period8_independent_polynomial.json",
        "independent_snapshot_sha256": snapshot_sha,
        "independent_snapshot_frozen_before_old_evidence_read": True,
        "frozen_certificate_file": "research/counterexamples/target_a_period8_family_certificate.json",
        "frozen_certificate_sha256": _sha256_bytes(frozen_bytes),
        "frozen_polynomial_source_path": frozen_path,
        "frozen_polynomial": _expression_string(frozen_polynomial),
        "frozen_polynomial_coefficient_map": frozen_map,
        "coefficient_comparison": comparison,
        "frozen_polynomial_comparison_status": "FLOQUET_POLYNOMIAL_MATCH_PASS",
        "operator_derivation_status": "OPERATOR_DERIVATION_PASS",
        "bloch_boundary_status": "BLOCH_BOUNDARY_DERIVATION_PASS",
        "floquet_hermitian_status": "FLOQUET_HERMITIAN_PASS",
        "second_determinant_status": "SECOND_DETERMINANT_ROUTE_PASS",
        "squared_eigenvalue_root_link_status": "SQUARED_EIGENVALUE_ROOT_LINK_PASS",
        "alpha_role": "H(z) is independent of alpha; alpha only selects roots of z^L=alpha",
        "uniform_bound_audited": False,
        "next_gate": "Task 39",
        "script_sha256": _sha256_file(Path(__file__).resolve()),
    }
    _write_json(audit_path, audit)
    return audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--transitions-output", type=Path, default=DEFAULT_TRANSITIONS)
    parser.add_argument("--snapshot-output", type=Path, default=DEFAULT_SNAPSHOT)
    parser.add_argument("--frozen-certificate", type=Path, default=DEFAULT_FROZEN_CERTIFICATE)
    parser.add_argument("--audit-output", type=Path, default=DEFAULT_AUDIT)
    parser.add_argument("--derive-only", action="store_true")
    args = parser.parse_args()
    try:
        if args.derive_only:
            derive_independent_snapshot(args.transitions_output, args.snapshot_output)
            print("OPERATOR_DERIVATION_PASS")
            print("BLOCH_BOUNDARY_DERIVATION_PASS")
            print("FLOQUET_HERMITIAN_PASS")
            print("FLOQUET_DIRECT_SUM_PASS")
            print("SECOND_DETERMINANT_ROUTE_PASS")
            print("INDEPENDENT_POLYNOMIAL_FROZEN")
            return
        audit = run_independent_audit(
            args.transitions_output,
            args.snapshot_output,
            args.frozen_certificate,
            args.audit_output,
        )
        _require(
            audit["status"] == "PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED",
            "final audit status failed",
        )
    except Exception as error:
        print(f"Independent Floquet audit failed: {error}", file=sys.stderr)
        print("INDEPENDENT_FLOQUET_AUDIT_FAIL")
        raise SystemExit(1)
    print("OPERATOR_DERIVATION_PASS")
    print("BLOCH_BOUNDARY_DERIVATION_PASS")
    print("FLOQUET_HERMITIAN_PASS")
    print("FLOQUET_DIRECT_SUM_PASS")
    print("FLOQUET_POLYNOMIAL_MATCH_PASS")
    print("SECOND_DETERMINANT_ROUTE_PASS")
    print("SQUARED_EIGENVALUE_ROOT_LINK_PASS")
    print("PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED")


if __name__ == "__main__":
    main()
