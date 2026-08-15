"""Reconstruct the Target A n=32 witness from flux definitions in a new gauge."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.polys.numberfields import to_number_field


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FROZEN_WITNESS = (
    RESEARCH_ROOT / "counterexamples" / "target_a_n32_period8.json"
)
DEFAULT_CONSTRUCTION = (
    RESEARCH_ROOT / "audit" / "target_a_n32_independent_reconstruction.json"
)
DEFAULT_AUDIT = RESEARCH_ROOT / "audit" / "n32_witness_reconstruction_audit.json"
N = 32
ALPHA = 1
TAU_PERIOD = (1, 1, -1, 1, -1, -1, 1, -1)
Q_PERIOD = (1, -1, -1, -1)
# Four negative signs per period give a deterministic, nontrivial alpha=+1 gauge.
STEP1_PERIOD = (1, -1, 1, -1, -1, 1, -1, 1)
BOUND = Fraction(1561, 200)


class ReconstructionError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ReconstructionError(message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def _product(signs: tuple[int, ...]) -> int:
    value = 1
    for sign in signs:
        value *= sign
    return value


def build_adjacency(
    n: int, step1: tuple[int, ...], step2: tuple[int, ...]
) -> list[list[int]]:
    _require(n == N, "adjacency order must be 32")
    _require(len(step1) == n and len(step2) == n, "edge-sign vector length mismatch")
    _require(all(sign in (-1, 1) for sign in step1 + step2), "non-sign edge value")
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i, sign in enumerate(step1):
        j = (i + 1) % n
        _require(matrix[i][j] == 0, "duplicate step-1 edge")
        matrix[i][j] = matrix[j][i] = sign
    for i, sign in enumerate(step2):
        j = (i + 2) % n
        _require(matrix[i][j] == 0, "step edge families overlap")
        matrix[i][j] = matrix[j][i] = sign

    _require(len(matrix) == n and all(len(row) == n for row in matrix), "matrix shape mismatch")
    for i in range(n):
        _require(matrix[i][i] == 0, "matrix diagonal is nonzero")
        _require(sum(value != 0 for value in matrix[i]) == 4, "row degree is not four")
        for j in range(n):
            distance = min((i - j) % n, (j - i) % n)
            expected_support = distance in (1, 2)
            _require(matrix[i][j] == matrix[j][i], "matrix is not symmetric")
            _require((matrix[i][j] != 0) == expected_support, "support is not C_32(1,2)")
            if expected_support:
                _require(matrix[i][j] in (-1, 1), "nonzero matrix entry is not a sign")
    return matrix


def reconstruct_from_definitions(
    tau_period: tuple[int, ...] = TAU_PERIOD,
    step1_period: tuple[int, ...] = STEP1_PERIOD,
) -> dict[str, Any]:
    _require(tuple(tau_period) == TAU_PERIOD, "triangle flux input differs from the specification")
    _require(len(step1_period) == 8, "independent gauge period must have length eight")
    _require(all(sign in (-1, 1) for sign in step1_period), "independent gauge contains a non-sign")
    tau = tuple(tau_period[i % len(tau_period)] for i in range(N))
    step1 = tuple(step1_period[i % len(step1_period)] for i in range(N))
    _require(step1 != (1,) * N, "independent gauge is trivial")
    _require(step1.count(-1) > 1, "independent gauge has too few negative signs")
    _require(_product(step1) == ALPHA, "independent gauge holonomy mismatch")

    # This is the triangle-flux definition solved directly for the step-2 sign.
    step2 = tuple(
        tau[i] * step1[i] * step1[(i + 1) % N] for i in range(N)
    )
    reconstructed_tau = tuple(
        step1[i] * step1[(i + 1) % N] * step2[i] for i in range(N)
    )
    _require(reconstructed_tau == tau, "triangle flux reconstruction failed")
    quadrilaterals = tuple(
        reconstructed_tau[i] * reconstructed_tau[(i + 1) % N]
        for i in range(N)
    )
    expected_q = tuple(Q_PERIOD[i % len(Q_PERIOD)] for i in range(N))
    _require(quadrilaterals == expected_q, "quadrilateral flux reconstruction failed")
    _require(_product(step1) == ALPHA, "alpha reconstruction failed")

    adjacency = build_adjacency(N, step1, step2)
    return {
        "n": N,
        "tau": tau,
        "Q": quadrilaterals,
        "alpha": _product(step1),
        "step1": step1,
        "step2": step2,
        "adjacency": adjacency,
    }


def construction_snapshot(construction: dict[str, Any]) -> dict[str, Any]:
    script_path = Path(__file__).resolve()
    return {
        "schema_version": 1,
        "status": "RECONSTRUCTION_FROM_DEFINITIONS_PASS",
        "n": construction["n"],
        "tau": list(construction["tau"]),
        "Q": list(construction["Q"]),
        "alpha": construction["alpha"],
        "independent_step1": list(construction["step1"]),
        "independent_step2": list(construction["step2"]),
        "adjacency_sha256": _sha256_bytes(_json_bytes(construction["adjacency"])),
        "construction_method": (
            "fixed nontrivial step-1 gauge; b_i=tau_i*a_i*a_(i+1) from the "
            "triangle-flux definition; frozen witness not read"
        ),
        "source_file": "research/scripts/target_a_n32_independent_reconstruction.py",
        "source_sha256": _sha256_file(script_path),
    }


def _parse_signing(data: dict[str, Any]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    _require(set(data) == {"n", "step1", "step2"}, "unexpected frozen witness fields")
    _require(data.get("n") == N, "frozen witness order mismatch")
    step1 = data.get("step1")
    step2 = data.get("step2")
    _require(isinstance(step1, list) and len(step1) == N, "invalid frozen step1")
    _require(isinstance(step2, list) and len(step2) == N, "invalid frozen step2")
    _require(
        all(type(sign) is int and sign in (-1, 1) for sign in step1 + step2),
        "invalid frozen edge sign",
    )
    return tuple(step1), tuple(step2)


def switching_equivalence(
    construction: dict[str, Any], frozen_data: dict[str, Any]
) -> dict[str, Any]:
    independent_step1 = construction["step1"]
    independent_step2 = construction["step2"]
    frozen_step1, frozen_step2 = _parse_signing(frozen_data)
    _require(
        independent_step1 != frozen_step1 or independent_step2 != frozen_step2,
        "independent gauge accidentally equals the frozen gauge",
    )
    frozen_adjacency = build_adjacency(N, frozen_step1, frozen_step2)

    switching = [1]
    for i in range(N):
        next_value = independent_step1[i] * switching[i] * frozen_step1[i]
        if i + 1 < N:
            switching.append(next_value)
        else:
            _require(next_value == switching[0], "switching vector does not close")
    switching_vector = tuple(switching)
    step1_equations = tuple(
        independent_step1[i]
        == switching_vector[i]
        * frozen_step1[i]
        * switching_vector[(i + 1) % N]
        for i in range(N)
    )
    _require(all(step1_equations), "step-1 switching equation failed")
    step2_equations = tuple(
        independent_step2[i]
        == switching_vector[i]
        * frozen_step2[i]
        * switching_vector[(i + 2) % N]
        for i in range(N)
    )
    _require(all(step2_equations), "step-2 switching equation failed")

    independent_adjacency = construction["adjacency"]
    dad = [
        [
            switching_vector[i] * frozen_adjacency[i][j] * switching_vector[j]
            for j in range(N)
        ]
        for i in range(N)
    ]
    _require(independent_adjacency == dad, "full D A_frozen D identity failed")
    return {
        "switching_vector": switching_vector,
        "closes": True,
        "step1_equations": step1_equations,
        "step2_equations": step2_equations,
        "matrix_relation_exact": True,
        "frozen_step1": frozen_step1,
        "frozen_step2": frozen_step2,
        "frozen_adjacency": frozen_adjacency,
    }


def _coefficient_sha256(coefficients: list[sp.Expr]) -> str:
    return _sha256_bytes(_json_bytes([str(value) for value in coefficients]))


def exact_spectral_consistency(
    independent: list[list[int]], frozen: list[list[int]]
) -> dict[str, Any]:
    x = sp.Symbol("x")
    independent_matrix = sp.Matrix(independent)
    frozen_matrix = sp.Matrix(frozen)
    independent_charpoly = independent_matrix.charpoly(x).all_coeffs()
    frozen_charpoly = frozen_matrix.charpoly(x).all_coeffs()
    _require(independent_charpoly == frozen_charpoly, "charpoly(A) mismatch")
    independent_square_charpoly = (independent_matrix * independent_matrix).charpoly(x).all_coeffs()
    frozen_square_charpoly = (frozen_matrix * frozen_matrix).charpoly(x).all_coeffs()
    _require(independent_square_charpoly == frozen_square_charpoly, "charpoly(A^2) mismatch")
    return {
        "charpoly_equal": True,
        "charpoly_A2_equal": True,
        "charpoly_sha256": _coefficient_sha256(independent_charpoly),
        "charpoly_A2_sha256": _coefficient_sha256(independent_square_charpoly),
    }


def _certificate_matrix(adjacency: list[list[int]]) -> list[list[int]]:
    square = [
        [sum(adjacency[i][k] * adjacency[k][j] for k in range(N)) for j in range(N)]
        for i in range(N)
    ]
    return [
        [
            (BOUND.numerator if i == j else 0) - BOUND.denominator * square[i][j]
            for j in range(N)
        ]
        for i in range(N)
    ]


def _bareiss_leading_minors(matrix: list[list[int]]) -> list[int]:
    work = [row[:] for row in matrix]
    previous = 1
    pivots: list[int] = []
    for k in range(len(work) - 1):
        pivot = work[k][k]
        pivots.append(pivot)
        _require(pivot != 0, f"zero Bareiss pivot at index {k}")
        for i in range(k + 1, len(work)):
            for j in range(k + 1, len(work)):
                numerator = work[i][j] * pivot - work[i][k] * work[k][j]
                quotient, remainder = divmod(numerator, previous)
                _require(remainder == 0, f"non-exact Bareiss division at index {k}")
                work[i][j] = quotient
        previous = pivot
    pivots.append(work[-1][-1])
    return pivots


def _rational_ldl_diagonal(matrix: list[list[int]]) -> list[Fraction]:
    lower = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    diagonal: list[Fraction] = []
    for j in range(N):
        lower[j][j] = Fraction(1)
        pivot = Fraction(matrix[j][j]) - sum(
            lower[j][k] * lower[j][k] * diagonal[k] for k in range(j)
        )
        _require(pivot != 0, f"zero LDL pivot at index {j}")
        diagonal.append(pivot)
        for i in range(j + 1, N):
            numerator = Fraction(matrix[i][j]) - sum(
                lower[i][k] * lower[j][k] * diagonal[k] for k in range(j)
            )
            lower[i][j] = numerator / pivot
    return diagonal


def _exact_positive(value: sp.Expr) -> bool:
    root = to_number_field(sp.simplify(value)).to_root()
    if root.is_positive is True:
        return True
    return sp.simplify(root > 0) is sp.true


def exact_counterexample_check(adjacency: list[list[int]]) -> dict[str, Any]:
    certificate_matrix = _certificate_matrix(adjacency)
    minors = _bareiss_leading_minors(certificate_matrix)
    diagonal = _rational_ldl_diagonal(certificate_matrix)
    _require(len(minors) == N and all(value > 0 for value in minors), "Bareiss positivity failed")
    _require(len(diagonal) == N and all(value > 0 for value in diagonal), "LDL positivity failed")
    cumulative = Fraction(1)
    for index, pivot in enumerate(diagonal):
        cumulative *= pivot
        _require(
            cumulative.denominator == 1 and cumulative.numerator == minors[index],
            f"Bareiss/LDL mismatch at index {index}",
        )
    threshold_squared = 4 * (
        sp.cos(sp.pi / N) ** 2 + sp.cos(2 * sp.pi / N) ** 2
    )
    threshold_above_bound = _exact_positive(
        threshold_squared - sp.Rational(BOUND.numerator, BOUND.denominator)
    )
    _require(threshold_above_bound, "exact threshold comparison failed")
    return {
        "positive_definite_check": {
            "status": "PASS",
            "methods": ["fraction-free Bareiss", "rational LDL^T"],
            "positive_leading_principal_minors": len(minors),
            "positive_ldl_pivots": len(diagonal),
            "bareiss_ldl_match": True,
            "certificate_matrix_sha256": _sha256_bytes(_json_bytes(certificate_matrix)),
            "leading_minors_sha256": _sha256_bytes(_json_bytes(minors)),
            "ldl_diagonal_sha256": _sha256_bytes(
                _json_bytes([str(value) for value in diagonal])
            ),
        },
        "threshold_check": {
            "status": "PASS",
            "method": "exact real-algebraic sign comparison",
            "bound": "1561/200",
            "threshold_exceeds_bound": True,
        },
        "counterexample_check": True,
        "exact_inequality": "rho(A_independent)^2 < 1561/200 < rho_-(32)^2",
    }


def run_independent_audit(
    frozen_witness_path: Path = DEFAULT_FROZEN_WITNESS,
    construction_path: Path = DEFAULT_CONSTRUCTION,
    audit_path: Path = DEFAULT_AUDIT,
) -> dict[str, Any]:
    construction = reconstruct_from_definitions()
    snapshot = construction_snapshot(construction)

    # Independence boundary: freeze the construction before opening the old witness.
    _write_json(construction_path, snapshot)
    construction_sha256 = _sha256_file(construction_path)

    frozen_bytes = frozen_witness_path.read_bytes()
    frozen_data = json.loads(frozen_bytes.decode("utf-8"))
    switching = switching_equivalence(construction, frozen_data)
    spectral = exact_spectral_consistency(
        construction["adjacency"], switching["frozen_adjacency"]
    )
    counterexample = exact_counterexample_check(construction["adjacency"])
    script_path = Path(__file__).resolve()
    audit = {
        "schema_version": 1,
        "status": "N32_WITNESS_INDEPENDENTLY_RECONSTRUCTED",
        "n": N,
        "tau": list(construction["tau"]),
        "Q": list(construction["Q"]),
        "alpha": construction["alpha"],
        "independent_step1": list(construction["step1"]),
        "independent_step2": list(construction["step2"]),
        "independent_adjacency_sha256": snapshot["adjacency_sha256"],
        "construction_snapshot_file": "research/audit/target_a_n32_independent_reconstruction.json",
        "construction_snapshot_sha256": construction_sha256,
        "construction_frozen_before_witness_read": True,
        "frozen_witness_file": "research/counterexamples/target_a_n32_period8.json",
        "frozen_witness_sha256": _sha256_bytes(frozen_bytes),
        "switching_vector": list(switching["switching_vector"]),
        "switching_vector_closes": switching["closes"],
        "all_step1_switching_equations": all(switching["step1_equations"]),
        "all_step2_switching_equations": all(switching["step2_equations"]),
        "switching_relation_exact": switching["matrix_relation_exact"],
        **spectral,
        **counterexample,
        "independent_script_file": "research/scripts/target_a_n32_independent_reconstruction.py",
        "independent_script_sha256": _sha256_file(script_path),
        "independence_constraints": {
            "standard_library_and_sympy_only": True,
            "prohibited_target_a_helpers_imported": False,
            "frozen_witness_used_during_construction": False,
            "floating_eigenvalues_used": False,
        },
        "overall_status": "INDEPENDENT_N32_RECONSTRUCTION_PASS",
    }
    _write_json(audit_path, audit)
    return audit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen-witness", type=Path, default=DEFAULT_FROZEN_WITNESS)
    parser.add_argument("--construction-output", type=Path, default=DEFAULT_CONSTRUCTION)
    parser.add_argument("--audit-output", type=Path, default=DEFAULT_AUDIT)
    args = parser.parse_args()
    try:
        audit = run_independent_audit(
            args.frozen_witness, args.construction_output, args.audit_output
        )
        _require(
            audit["overall_status"] == "INDEPENDENT_N32_RECONSTRUCTION_PASS",
            "final audit status failed",
        )
    except Exception as error:
        print(f"Independent n=32 reconstruction failed: {error}", file=sys.stderr)
        print("INDEPENDENT_N32_RECONSTRUCTION_FAIL")
        raise SystemExit(1)
    print("RECONSTRUCTION_FROM_DEFINITIONS_PASS")
    print("SWITCHING_EQUIVALENCE_PASS")
    print("INDEPENDENT_COUNTEREXAMPLE_PASS")
    print("INDEPENDENT_N32_RECONSTRUCTION_PASS")


if __name__ == "__main__":
    main()
