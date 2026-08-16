"""Classify the Target A periodic Hamilton-gauge frontier through period 16."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import sympy as sp


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SHARP = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_low_period_spectral_frontier.json"
EXPECTED_SHARP_SHA256 = "f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63"
MAX_PERIOD = 16
COARSE_SAMPLES = 256
REFINED_SAMPLES = 4096
REFINED_PER_PERIOD = 5
STURM_CROSSCHECK_COUNT = 24
TARGET_PRIMITIVE_Q = (-1, -1, -1, 1)
EXPECTED_ORBIT_COUNTS = (1, 2, 2, 4, 4, 8, 9, 18, 23, 44, 63, 122, 190, 362, 612, 1162)


class LowPeriodFrontierError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise LowPeriodFrontierError(message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def sign_bits(signs: Iterable[int]) -> str:
    return "".join("1" if value == 1 else "0" for value in signs)


def rotate(signs: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= len(signs)
    return signs[amount:] + signs[:amount]


def dihedral_images(signs: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {
        rotate(base, amount)
        for base in (signs, tuple(reversed(signs)))
        for amount in range(len(signs))
    }


def canonical_q(signs: tuple[int, ...]) -> tuple[int, ...]:
    return min(dihedral_images(signs), key=sign_bits)


def legal_q_vectors(p: int) -> Iterable[tuple[int, ...]]:
    for prefix in itertools.product((-1, 1), repeat=p - 1):
        yield prefix + (math.prod(prefix),)


def route_a_orbits(p: int) -> list[dict[str, Any]]:
    legal = set(legal_q_vectors(p))
    representatives = sorted({canonical_q(q) for q in legal}, key=sign_bits)
    covered: set[tuple[int, ...]] = set()
    result = []
    for representative in representatives:
        members = dihedral_images(representative)
        _require(not covered.intersection(members), "LOW_PERIOD_ROUTE_A_ORBIT_OVERLAP")
        covered.update(members)
        result.append({"representative": representative, "orbit_size": len(members)})
    _require(covered == legal, "LOW_PERIOD_ROUTE_A_COVERAGE_MISMATCH")
    return result


def _permutation_cycles(p: int, kind: str, parameter: int) -> list[list[int]]:
    if kind == "rotation":
        image = lambda index: (index + parameter) % p
    else:
        _require(kind == "reflection", "unknown dihedral element")
        image = lambda index: (parameter - index) % p
    unseen = set(range(p))
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        index = start
        while index in unseen:
            unseen.remove(index)
            cycle.append(index)
            index = image(index)
        cycles.append(cycle)
    return cycles


def route_b_burnside(p: int) -> dict[str, Any]:
    rows = []
    for kind in ("rotation", "reflection"):
        for parameter in range(p):
            cycle_lengths = [len(cycle) for cycle in _permutation_cycles(p, kind, parameter)]
            cycle_count = len(cycle_lengths)
            fixed_legal = 2 ** (cycle_count - 1) if any(length % 2 for length in cycle_lengths) else 2**cycle_count
            rows.append(
                {
                    "kind": kind,
                    "parameter": parameter,
                    "cycle_lengths": cycle_lengths,
                    "fixed_legal_q_count": fixed_legal,
                }
            )
    fixed_sum = sum(row["fixed_legal_q_count"] for row in rows)
    _require(fixed_sum % (2 * p) == 0, "LOW_PERIOD_BURNSIDE_NONINTEGRAL")
    return {
        "method": "cycle decomposition; parity-product count without enumerating sign words",
        "group_order": 2 * p,
        "fixed_point_sum": fixed_sum,
        "orbit_count": fixed_sum // (2 * p),
        "group_elements": rows,
    }


def primitive_period(signs: tuple[int, ...]) -> int:
    p = len(signs)
    for period in range(1, p + 1):
        if p % period == 0 and all(signs[index] == signs[index % period] for index in range(p)):
            return period
    raise LowPeriodFrontierError("primitive period not found")


def tau_lift(q: tuple[int, ...]) -> tuple[int, ...]:
    _require(q and math.prod(q) == 1, "illegal Q lift")
    tau = [1]
    for value in q[:-1]:
        tau.append(value * tau[-1])
    _require(tau[-1] * q[-1] == 1, "tau lift failed to close")
    return tuple(tau)


def reconstruct_q(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[index] * tau[(index + 1) % len(tau)] for index in range(len(tau)))


def verify_geometric_equivalences(q: tuple[int, ...], tau: tuple[int, ...]) -> None:
    p = len(q)
    tau_images = set()
    for amount in range(p):
        translated = tuple(tau[(index + amount) % p] for index in range(p))
        reflected = tuple(tau[(-index + amount) % p] for index in range(p))
        for image in (translated, reflected):
            tau_images.add(image)
            tau_images.add(tuple(-value for value in image))
    _require(
        {reconstruct_q(image) for image in tau_images} == dihedral_images(q),
        "GENERAL_GEOMETRIC_EQUIVALENCE_MISMATCH",
    )


def defect_statistics(q: tuple[int, ...]) -> tuple[int, int, int]:
    p = len(q)
    return (
        sum(value == 1 for value in q),
        sum(q[index] == q[(index + 1) % p] == 1 for index in range(p)),
        sum(q[index] == q[(index + 2) % p] == 1 for index in range(p)),
    )


def bloch_laurent_matrix(tau: tuple[int, ...]) -> list[list[dict[int, int]]]:
    p = len(tau)
    matrix = [[{} for _ in range(p)] for _ in range(p)]
    for output in range(p):
        transitions = (
            (-1, 1),
            (1, 1),
            (-2, tau[(output - 2) % p]),
            (2, tau[output]),
        )
        for displacement, coefficient in transitions:
            source = output + displacement
            cell, residue = divmod(source, p)
            matrix[output][residue][cell] = matrix[output][residue].get(cell, 0) + coefficient
    return matrix


def verify_bloch_identities(tau: tuple[int, ...]) -> None:
    p = len(tau)
    matrix = bloch_laurent_matrix(tau)
    for row in range(p):
        for column in range(p):
            adjoint = {-power: coefficient for power, coefficient in matrix[column][row].items()}
            _require(matrix[row][column] == adjoint, "GENERAL_BLOCH_TRANSPOSE_IDENTITY_FAIL")

    negative = bloch_laurent_matrix(tuple(-value for value in tau))
    phase_sign = -1 if p % 2 else 1
    diagonal = [(-1) ** index for index in range(p)]
    for row in range(p):
        for column in range(p):
            transformed = {
                power: -diagonal[row] * diagonal[column] * phase_sign**power * coefficient
                for power, coefficient in matrix[row][column].items()
            }
            _require(negative[row][column] == transformed, "GENERAL_TAU_NEGATION_IDENTITY_FAIL")


def evaluate_bloch(
    matrix: list[list[dict[int, int]]], z: complex
) -> np.ndarray:
    p = len(matrix)
    result = np.zeros((p, p), dtype=np.complex128)
    for row in range(p):
        for column in range(p):
            result[row, column] = sum(coefficient * z**power for power, coefficient in matrix[row][column].items())
    return result


def endpoint_matrix(tau: tuple[int, ...], z_value: int) -> np.ndarray:
    matrix = bloch_laurent_matrix(tau)
    return np.array(
        [
            [
                sum(
                    coefficient * (1 if z_value == 1 or power % 2 == 0 else -1)
                    for power, coefficient in entry.items()
                )
                for entry in row
            ]
            for row in matrix
        ],
        dtype=np.int64,
    )


def numeric_preview(tau: tuple[int, ...], sample_count: int) -> dict[str, Any]:
    matrix = bloch_laurent_matrix(tau)
    best = -1.0
    best_index = 0
    for index in range(sample_count):
        theta = 2.0 * math.pi * index / sample_count
        fiber = evaluate_bloch(matrix, complex(math.cos(theta), math.sin(theta)))
        _require(np.allclose(fiber, fiber.conj().T, atol=1e-11), "NUMERIC_BLOCH_HERMITIAN_FAIL")
        eigenvalues = np.linalg.eigvalsh(fiber)
        squared_radius = float(np.max(np.abs(eigenvalues)) ** 2)
        if squared_radius > best:
            best = squared_radius
            best_index = index
    return {
        "evidence": "OBSERVED_DENSE_BLOCH_GRID",
        "sample_count": sample_count,
        "R_squared_preview": best,
        "argmax_theta_over_pi_preview": 2.0 * best_index / sample_count,
    }


def rational_gt_eta(numerator: int, denominator: int) -> tuple[bool, dict[str, int]]:
    value = Fraction(numerator, denominator)
    if value <= 4:
        return False, {}
    u = ((value - 4) ** 2 - 10) / 2
    difference = u * u - 5
    valid = u > 0 and difference > 0
    return valid, {
        "u_numerator": u.numerator,
        "u_denominator": u.denominator,
        "u_squared_minus_5_numerator": difference.numerator,
        "u_squared_minus_5_denominator": difference.denominator,
    }


def _candidate_vectors(matrix: np.ndarray) -> list[tuple[int, ...]]:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix.astype(float))
    vectors: set[tuple[int, ...]] = set()
    order = np.argsort(np.abs(eigenvalues))[::-1]
    for column in order:
        vector = eigenvectors[:, column]
        for threshold in sorted(set(abs(vector)), reverse=True):
            candidate = tuple(
                int(1 if value >= 0 else -1) if abs(value) + 1e-14 >= threshold else 0
                for value in vector
            )
            if any(candidate):
                vectors.add(candidate)
        for scale in (2, 3, 4, 5, 6, 8, 10, 12):
            candidate_values = [int(round(scale * value)) for value in vector]
            divisor = math.gcd(*map(abs, candidate_values))
            if divisor:
                candidate_values = [value // divisor for value in candidate_values]
            candidate = tuple(candidate_values)
            if any(candidate):
                vectors.add(candidate)
    return sorted(vectors, key=lambda vector: (max(map(abs, vector)), sum(value * value for value in vector), vector))


def find_rayleigh_certificate(tau: tuple[int, ...]) -> dict[str, Any]:
    ternary_best: tuple[Fraction, int, tuple[int, ...], int, int] | None = None
    integer_best: tuple[Fraction, int, tuple[int, ...], int, int] | None = None
    for z_value in (1, -1):
        matrix = endpoint_matrix(tau, z_value)
        square = matrix @ matrix
        for vector in _candidate_vectors(matrix):
            column = np.array(vector, dtype=np.int64)
            denominator = int(column @ column)
            numerator = int(column @ square @ column)
            valid, comparison = rational_gt_eta(numerator, denominator)
            if not valid:
                continue
            record = (Fraction(numerator, denominator), z_value, vector, numerator, denominator)
            if max(map(abs, vector)) <= 1:
                if ternary_best is None or record[0] > ternary_best[0]:
                    ternary_best = record
            elif integer_best is None or record[0] > integer_best[0]:
                integer_best = record
    best = ternary_best if ternary_best is not None else integer_best
    _require(best is not None, "LOW_PERIOD_EXACT_CERTIFICATE_NOT_FOUND")
    quotient, z_value, vector, numerator, denominator = best
    valid, comparison = rational_gt_eta(numerator, denominator)
    _require(valid, "LOW_PERIOD_RAYLEIGH_COMPARISON_FAIL")
    return {
        "type": "EXACT_ENDPOINT_INTEGER_RAYLEIGH",
        "z": z_value,
        "vector": list(vector),
        "vector_alphabet": "TERNARY" if max(map(abs, vector)) <= 1 else "SMALL_INTEGER",
        "numerator": numerator,
        "denominator": denominator,
        "quotient": f"{quotient.numerator}/{quotient.denominator}",
        "eta_comparison": comparison,
        "conclusion": "R(Q)>eta",
    }


def moment_certificate(q: tuple[int, ...]) -> dict[str, Any] | None:
    p = len(q)
    d, a, b = defect_statistics(q)
    f1 = 16 * d - 12 * p
    f2 = -42 * p + 40 * d + 96 * a + 48 * b
    if f1 > 0:
        return {
            "type": "TASK42A_MOMENT_EXCESS",
            "excess": "F1",
            "value": f1,
            "logic": "F1>0 implies R(Q)>8>eta",
            "conclusion": "R(Q)>eta",
        }
    if f2 > 0:
        return {
            "type": "TASK42A_MOMENT_EXCESS",
            "excess": "F2",
            "value": f2,
            "logic": "F2>0 implies R(Q)>8>eta",
            "conclusion": "R(Q)>eta",
        }
    return None


def is_target_phase(q: tuple[int, ...], tau: tuple[int, ...]) -> bool:
    q_period = primitive_period(q)
    primitive_q = canonical_q(q[:q_period])
    return primitive_q == TARGET_PRIMITIVE_Q and primitive_period(tau) == 8


def sturm_crosscheck(row: dict[str, Any]) -> dict[str, Any]:
    tau = tuple(row["tau_lift"])
    z_value = row["exact_certificate"]["z"]
    matrix = sp.Matrix(endpoint_matrix(tau, z_value).tolist())
    variable = sp.Symbol("y")
    polynomial = (matrix * matrix).charpoly(variable).as_poly()
    intervals = polynomial.intervals(eps=sp.Rational(1, 10**10))
    _require(intervals, "STURM_ROOT_ISOLATION_EMPTY")
    interval, multiplicity = intervals[-1]
    lower, upper = interval
    valid, comparison = rational_gt_eta(int(lower.p), int(lower.q))
    _require(valid, "STURM_LOWER_ENDPOINT_NOT_ABOVE_ETA")
    return {
        "status": "EXACT_STURM_CROSSCHECK_PASS",
        "orbit_id": row["orbit_id"],
        "z": z_value,
        "squared_charpoly_coefficients": [int(value) for value in polynomial.all_coeffs()],
        "largest_root_isolating_interval": [f"{lower.p}/{lower.q}", f"{upper.p}/{upper.q}"],
        "largest_root_multiplicity": multiplicity,
        "lower_endpoint_eta_comparison": comparison,
        "conclusion": "largest endpoint squared eigenvalue > eta",
    }


def load_sharp(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    _require(_sha256_bytes(raw) == EXPECTED_SHARP_SHA256, "TASK40A_SHARP_SHA_MISMATCH")
    payload = json.loads(raw)
    _require(payload.get("status") == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED", "TASK40A_SHARP_STATUS_MISMATCH")
    return {"payload": payload, "sha256": _sha256_bytes(raw)}


def run_frontier(
    sharp_path: Path = DEFAULT_SHARP, result_path: Path = DEFAULT_RESULT
) -> dict[str, Any]:
    sharp = load_sharp(sharp_path)
    eta_numeric = float(4 + sp.sqrt(10 + 2 * sp.sqrt(5)))
    periods = []
    all_rows = []
    route_a_counts = []
    route_b_counts = []
    constructor_checks = 0

    for p in range(1, MAX_PERIOD + 1):
        route_a = route_a_orbits(p)
        route_b = route_b_burnside(p)
        _require(len(route_a) == route_b["orbit_count"], "LOW_PERIOD_ORBIT_COUNT_MISMATCH")
        _require(len(route_a) == EXPECTED_ORBIT_COUNTS[p - 1], "LOW_PERIOD_EXPECTED_ORBIT_COUNT_MISMATCH")
        route_a_counts.append(len(route_a))
        route_b_counts.append(route_b)
        period_rows = []
        for index, orbit in enumerate(route_a, start=1):
            q = orbit["representative"]
            tau = tau_lift(q)
            verify_bloch_identities(tau)
            verify_geometric_equivalences(q, tau)
            constructor_checks += 1
            q_period = primitive_period(q)
            tau_period = primitive_period(tau)
            primitive_q = canonical_q(q[:q_period])
            target = is_target_phase(q, tau)
            preview = numeric_preview(tau, COARSE_SAMPLES)
            certificate = None if target else moment_certificate(q)
            if certificate is None and not target:
                certificate = find_rayleigh_certificate(tau)
            row = {
                "orbit_id": f"P{p:02d}-{index:04d}",
                "p": p,
                "canonical_q_bits": sign_bits(q),
                "canonical_q_signs": list(q),
                "dihedral_orbit_size": orbit["orbit_size"],
                "tau_lift": list(tau),
                "primitive_q_period": q_period,
                "primitive_tau_period": tau_period,
                "primitive_q_canonical_bits": sign_bits(primitive_q),
                "infinite_phase_key": f"tau{tau_period}:Q{sign_bits(primitive_q)}",
                "cell_repetition": tau_period < p,
                "target_infinite_phase": target,
                "defect_statistics": dict(zip(("d", "a", "b"), defect_statistics(q))),
                "numeric_preview": preview,
                "numeric_gap_from_eta": preview["R_squared_preview"] - eta_numeric,
                "exact_certificate": (
                    {
                        "type": "TASK40A_TARGET_EXACT_SHARP_CONSTANT",
                        "dependency_sha256": sharp["sha256"],
                        "R_squared": sharp["payload"]["eta_squared"]["exact_radical"],
                        "conclusion": "R(Q)=eta",
                    }
                    if target
                    else certificate
                ),
            }
            period_rows.append(row)
            all_rows.append(row)

        for row in sorted(period_rows, key=lambda item: item["numeric_preview"]["R_squared_preview"])[:REFINED_PER_PERIOD]:
            refined = numeric_preview(tuple(row["tau_lift"]), REFINED_SAMPLES)
            row["numeric_preview"] = refined
            row["numeric_gap_from_eta"] = refined["R_squared_preview"] - eta_numeric

        minimum = min(period_rows, key=lambda item: item["numeric_preview"]["R_squared_preview"])
        target_rows = [row for row in period_rows if row["target_infinite_phase"]]
        periods.append(
            {
                "p": p,
                "legal_q_count": 2 ** (p - 1),
                "dihedral_orbit_count": len(route_a),
                "primitive_tau_period_p_orbits": sum(row["primitive_tau_period"] == p for row in period_rows),
                "numeric_minimum_R_squared": minimum["numeric_preview"]["R_squared_preview"],
                "numeric_minimizing_orbit": minimum["orbit_id"],
                "numeric_minimizing_q_bits": minimum["canonical_q_bits"],
                "numeric_gap_from_eta": minimum["numeric_gap_from_eta"],
                "minimum_value_status": "EXACT_ETA" if target_rows else "OBSERVED_NUMERIC_MINIMUM",
                "frontier_relation_to_eta": "PROVED_EQUAL_TARGET_REPETITION" if target_rows else "PROVED_STRICTLY_ABOVE_FOR_EVERY_ORBIT",
                "target_representations": [row["orbit_id"] for row in target_rows],
            }
        )

    _require(route_a_counts == list(EXPECTED_ORBIT_COUNTS), "LOW_PERIOD_ROUTE_A_DIAGNOSTIC_MISMATCH")
    _require(sum(route_a_counts) == 2626, "LOW_PERIOD_TOTAL_ORBIT_COUNT_MISMATCH")
    target_rows = [row for row in all_rows if row["target_infinite_phase"]]
    _require([(row["p"], row["primitive_tau_period"]) for row in target_rows] == [(8, 8), (16, 8)], "TARGET_REPETITION_CLASSIFICATION_FAIL")
    competitors = [row for row in all_rows if not row["target_infinite_phase"]]
    _require(all(row["exact_certificate"]["conclusion"] == "R(Q)>eta" for row in competitors), "LOW_PERIOD_UNCERTIFIED_COMPETITOR")

    rayleigh_rows = [row for row in competitors if row["exact_certificate"]["type"] == "EXACT_ENDPOINT_INTEGER_RAYLEIGH"]
    dangerous = sorted(rayleigh_rows, key=lambda row: row["numeric_gap_from_eta"])[:STURM_CROSSCHECK_COUNT]
    sturm = [sturm_crosscheck(row) for row in dangerous]
    moment_count = sum(row["exact_certificate"]["type"] == "TASK42A_MOMENT_EXCESS" for row in competitors)
    ternary_count = sum(row["exact_certificate"].get("vector_alphabet") == "TERNARY" for row in competitors)
    integer_count = sum(row["exact_certificate"].get("vector_alphabet") == "SMALL_INTEGER" for row in competitors)
    near_threshold = [
        {
            "orbit_id": row["orbit_id"],
            "p": row["p"],
            "canonical_q_bits": row["canonical_q_bits"],
            "numeric_gap_from_eta": row["numeric_gap_from_eta"],
            "certificate_type": row["exact_certificate"]["type"],
            "sturm_crosschecked": any(item["orbit_id"] == row["orbit_id"] for item in sturm),
        }
        for row in sorted(competitors, key=lambda item: item["numeric_gap_from_eta"])
        if row["numeric_gap_from_eta"] < 0.25
    ]
    _require(not [row for row in competitors if row["numeric_preview"]["R_squared_preview"] < eta_numeric - 1e-7], "LOW_PERIOD_BETTER_PHASE_FOUND")

    result = {
        "schema_version": 1,
        "status": "PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED",
        "component_statuses": [
            "LOW_PERIOD_PHASE_SPACE_COMPLETE",
            "LOW_PERIOD_SPECTRAL_FRONTIER_TABLE_PROVED",
            "PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED",
        ],
        "theorem": (
            "Among periodic Hamilton-gauge signings with primitive tau period at most 16, "
            "the Target A period-8 phase is the unique minimizer up to translation, reflection, "
            "global tau negation, and unit-cell repetition."
        ),
        "eta": sharp["payload"]["eta_squared"]["exact_radical"],
        "dependencies": {"Task40A_sharp": {"sha256": sharp["sha256"], "status": sharp["payload"]["status"]}},
        "phase_space": {
            "period_range": [1, MAX_PERIOD],
            "legal_condition": "product Q_i=1",
            "route_a_method": "explicit legal-Q enumeration and dihedral orbit partition",
            "route_a_orbit_counts": route_a_counts,
            "route_b_method": "independent Burnside cycle decomposition and parity-product count",
            "route_b": route_b_counts,
            "expected_diagnostics": list(EXPECTED_ORBIT_COUNTS),
            "total_orbit_count": len(all_rows),
            "route_mismatch_count": 0,
        },
        "bloch_construction": {
            "method": "general-p infinite-lattice transitions with exact cell-crossing Laurent exponents",
            "checked_orbits": constructor_checks,
            "transpose_identity": "H_tau(z)^T=H_tau(z^-1)",
            "hermitian_on_unit_circle": True,
            "tau_negation_identity": "H_(-tau)(z)=-D*H_tau((-1)^p*z)*D",
            "odd_period_phase_shift_recorded": True,
            "translation_reflection_tau_lift_images_verified_for_all_orbits": True,
            "primitive_reduction_recorded_for_every_orbit": True,
        },
        "certificate_summary": {
            "competitor_orbits": len(competitors),
            "Task42A_moment_excess": moment_count,
            "endpoint_ternary_rayleigh": ternary_count,
            "endpoint_small_integer_rayleigh": integer_count,
            "target_representations": len(target_rows),
            "uncertified": 0,
            "sturm_crosschecks": len(sturm),
        },
        "target_repetition": {
            "infinite_phase_key": target_rows[0]["infinite_phase_key"],
            "representations": [row["orbit_id"] for row in target_rows],
            "periods": [row["p"] for row in target_rows],
            "primitive_tau_period": 8,
            "counted_as_distinct_minimizers": False,
        },
        "near_threshold_classes": near_threshold,
        "sturm_crosschecks": sturm,
        "frontier_table": periods,
        "orbits": all_rows,
        "scope": {
            "primitive_tau_period_at_most_16": "PROVED_UNIQUE_TARGET_OPTIMUM",
            "period_17_or_larger": "NOT_CLAIMED",
            "all_period_global_optimality": "NOT_CLAIMED",
            "finite_size_global_optimality": "NOT_CLAIMED",
            "all_signings_global_optimality": "NOT_CLAIMED",
            "numeric_previews_used_as_proof": False,
            "paper_manuscript_started": False,
        },
        "checker": {
            "path": "research/scripts/verify_target_a_low_period_spectral_frontier.py",
            "expected_status": "TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER_PASS",
        },
        "script_sha256": _sha256_file(Path(__file__).resolve()),
        "next_gate": "Task 42C low-period structural compression",
    }
    _write_json(result_path, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sharp", type=Path, default=DEFAULT_SHARP)
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()
    try:
        result = run_frontier(args.sharp, args.output)
    except Exception as error:
        print(f"Target A low-period frontier failed: {error}", file=sys.stderr)
        print("TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER_FAIL")
        raise SystemExit(1)
    for status in result["component_statuses"]:
        print(status)
    print(result["status"])


if __name__ == "__main__":
    main()
