"""Independently verify the Target A period-8 structural mechanism."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable

import sympy as sp
from sympy.polys.numberfields import to_number_field


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_period8_structural_mechanism.json"
DEFAULT_SHARP = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
DEFAULT_CLASSIFICATION = RESEARCH_ROOT / "proofs" / "target_a_period8_pattern_classification.json"
DEFAULT_CLASSIFICATION_AUDIT = RESEARCH_ROOT / "audit" / "period8_pattern_classification_audit.json"
DEFAULT_SOURCE = RESEARCH_ROOT / "scripts" / "target_a_period8_structural_mechanism.py"
EXPECTED_SHARP_SHA256 = "f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63"
EXPECTED_CLASSIFICATION_SHA256 = "a7a7b7259a99f099c7d2ab756a1a2f4c1ee233214f352d12df9e61cf1b47464c"
EXPECTED_CLASSIFICATION_AUDIT_SHA256 = "274e80a6b43183d4a6137ac3d9a676e6942f1d84a46691cb2b63018b66c69e80"
N = 8
TARGET_Q = (1, -1, -1, -1, 1, -1, -1, -1)
ALL_NEGATIVE_Q = (-1,) * N


class StructuralVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise StructuralVerificationError(message)


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _positive(expression: sp.Expr) -> bool:
    root = to_number_field(sp.simplify(expression)).to_root()
    return root.is_positive is True or sp.simplify(root > 0) is sp.true


def _bits(signs: Iterable[int]) -> str:
    return "".join("1" if value == 1 else "0" for value in signs)


def _legal_q() -> list[tuple[int, ...]]:
    return [q for q in itertools.product((-1, 1), repeat=N) if math.prod(q) == 1]


def _tau(q: tuple[int, ...]) -> tuple[int, ...]:
    _check(len(q) == N and math.prod(q) == 1, "VERIFY_Q_LEGALITY_FAIL")
    values = [1]
    for sign in q[:-1]:
        values.append(sign * values[-1])
    _check(values[-1] * q[-1] == values[0], "VERIFY_TAU_CLOSURE_FAIL")
    return tuple(values)


def _q_from_tau(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[index] * tau[(index + 1) % N] for index in range(N))


def _rotate(signs: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= N
    return signs[amount:] + signs[:amount]


def _images(signs: tuple[int, ...]) -> set[tuple[int, ...]]:
    reflected = tuple(reversed(signs))
    return {_rotate(base, amount) for base in (signs, reflected) for amount in range(N)}


def _canonical(signs: tuple[int, ...]) -> tuple[int, ...]:
    return min(_images(signs), key=_bits)


def _statistics(q: tuple[int, ...]) -> tuple[int, int, int]:
    return (
        sum(value == 1 for value in q),
        sum(q[index] == q[(index + 1) % N] == 1 for index in range(N)),
        sum(q[index] == q[(index + 2) % N] == 1 for index in range(N)),
    )


def _separation(q: tuple[int, ...]) -> int | None:
    positions = [index for index, value in enumerate(q) if value == 1]
    if len(positions) != 2:
        return None
    distance = (positions[1] - positions[0]) % N
    return min(distance, N - distance)


def _transitions(tau: tuple[int, ...], position: int) -> tuple[tuple[int, int], ...]:
    return (
        (position - 1, 1),
        (position + 1, 1),
        (position - 2, tau[(position - 2) % N]),
        (position + 2, tau[position % N]),
    )


def _a2_actual(tau: tuple[int, ...], position: int) -> dict[int, int]:
    result: dict[int, int] = {}
    for middle, first in _transitions(tau, position):
        for endpoint, second in _transitions(tau, middle):
            displacement = endpoint - position
            result[displacement] = result.get(displacement, 0) + first * second
    return result


def _a2_expected(tau: tuple[int, ...], position: int) -> dict[int, int]:
    q = _q_from_tau(tau)
    return {
        -4: q[(position - 4) % N] * q[(position - 3) % N],
        -3: tau[(position - 3) % N] * (1 + q[(position - 3) % N]),
        -2: 1,
        -1: tau[(position - 2) % N] * (1 + q[(position - 2) % N]),
        0: 4,
        1: tau[(position - 1) % N] * (1 + q[(position - 1) % N]),
        2: 1,
        3: tau[position % N] * (1 + q[position % N]),
        4: q[position % N] * q[(position + 1) % N],
    }


def _bloch(tau: tuple[int, ...], z: sp.Expr) -> sp.Matrix:
    matrix = sp.zeros(N)
    for output in range(N):
        for source, coefficient in _transitions(tau, output):
            cell, residue = divmod(source, N)
            matrix[output, residue] += coefficient * z**cell
    return matrix


def _moments(q: tuple[int, ...], maximum_k: int) -> list[int]:
    tau = _tau(q)
    states = [{start: 1} for start in range(N)]
    result = []
    for length in range(1, 2 * maximum_k + 1):
        next_states = []
        for state in states:
            updated: dict[int, int] = {}
            for position, amplitude in state.items():
                for endpoint, coefficient in _transitions(tau, position):
                    updated[endpoint] = updated.get(endpoint, 0) + amplitude * coefficient
            next_states.append(updated)
        states = next_states
        if length % 2 == 0:
            result.append(sum(states[start].get(start, 0) for start in range(N)))
    return result


def _structural_category(q: tuple[int, ...]) -> str:
    d, _, _ = _statistics(q)
    if d == 0:
        return "EQUAL_EIGHT"
    if d == 2 and _separation(q) == 4:
        return "BELOW_EIGHT_TARGET"
    return "ABOVE_EIGHT"


def verify_structural_data(
    result: dict[str, Any],
    sharp: dict[str, Any],
    classification: dict[str, Any],
    classification_audit: dict[str, Any],
    dependency_hashes: dict[str, str],
    source_sha256: str,
) -> None:
    expected_hashes = {
        "sharp": EXPECTED_SHARP_SHA256,
        "classification": EXPECTED_CLASSIFICATION_SHA256,
        "classification_audit": EXPECTED_CLASSIFICATION_AUDIT_SHA256,
    }
    _check(dependency_hashes == expected_hashes, "VERIFY_DEPENDENCY_FILE_SHA_FAIL")
    _check(sharp.get("status") == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED", "VERIFY_SHARP_STATUS_FAIL")
    _check(classification.get("status") == "PERIOD8_UNIQUE_OPTIMUM_AND_SECOND_BEST_PROVED", "VERIFY_CLASSIFICATION_STATUS_FAIL")
    _check(
        classification_audit.get("status") == "PERIOD8_PATTERN_CLASSIFICATION_INDEPENDENTLY_AUDITED",
        "VERIFY_CLASSIFICATION_AUDIT_STATUS_FAIL",
    )
    for name, expected_hash in expected_hashes.items():
        _check(result.get("dependencies", {}).get(name, {}).get("sha256") == expected_hash, "VERIFY_RECORDED_DEPENDENCY_FAIL")
    _check(result.get("script_sha256") == source_sha256, "VERIFY_SOURCE_SHA_FAIL")
    eta = sp.sympify(sharp["eta_squared"]["exact_radical"])
    _check(_positive(8 - eta), "VERIFY_ETA_BOUND_FAIL")

    formula = result.get("A2_local_formula", {})
    expected_formula = {
        "-4": "Q_(i-4)*Q_(i-3)",
        "-3": "tau_(i-3)*(1+Q_(i-3))",
        "-2": "1",
        "-1": "tau_(i-2)*(1+Q_(i-2))",
        "0": "4",
        "+1": "tau_(i-1)*(1+Q_(i-1))",
        "+2": "1",
        "+3": "tau_i*(1+Q_i)",
        "+4": "Q_i*Q_(i+1)",
    }
    _check(formula.get("status") == "FLUX_SQUARE_LOCAL_FORMULA_PASS", "VERIFY_A2_STATUS_FAIL")
    _check(formula.get("coefficients_by_displacement") == expected_formula, "VERIFY_A2_RECORDED_FORMULA_FAIL")
    cancelled = activated = 0
    for tau in itertools.product((-1, 1), repeat=N):
        q = _q_from_tau(tau)
        for position in range(N):
            _check(_a2_actual(tau, position) == _a2_expected(tau, position), "VERIFY_A2_INDEX_FAIL")
            for offset, q_index in ((-3, position - 3), (-1, position - 2), (1, position - 1), (3, position)):
                coefficient = _a2_expected(tau, position)[offset]
                if q[q_index % N] == -1:
                    _check(coefficient == 0, "VERIFY_NEGATIVE_Q_CANCELLATION_FAIL")
                    cancelled += 1
                else:
                    _check(abs(coefficient) == 2, "VERIFY_POSITIVE_Q_ACTIVATION_FAIL")
                    activated += 1
    _check(formula.get("cancelled_odd_coupling_checks") == cancelled == 4096, "VERIFY_CANCELLATION_COUNT_FAIL")
    _check(formula.get("activated_odd_coupling_checks") == activated == 4096, "VERIFY_ACTIVATION_COUNT_FAIL")
    _check(formula.get("interpretation", "").startswith("Q=-1 cancels"), "VERIFY_COUPLING_INTERPRETATION_FAIL")

    legal = _legal_q()
    moment_rows = []
    for q in legal:
        d, a, b = _statistics(q)
        m1, m2, m3 = _moments(q, 3)
        moment_rows.append((d, a, b, m1, m2, m3))
    _check(all(row[3] == 32 for row in moment_rows), "VERIFY_M1_FAIL")
    c0, cd = sp.symbols("c0 cd")
    m2_solution = tuple(next(iter(sp.linsolve(
        [sp.Eq(c0 + cd * row[0], row[4]) for row in moment_rows], (c0, cd)
    ))))
    c0, cd, ca, cb = sp.symbols("c0 cd ca cb")
    m3_solution = tuple(next(iter(sp.linsolve(
        [sp.Eq(c0 + cd * row[0] + ca * row[1] + cb * row[2], row[5]) for row in moment_rows],
        (c0, cd, ca, cb),
    ))))
    _check(m2_solution == (160, 16), "VERIFY_M2_DERIVATION_FAIL")
    _check(m3_solution == (944, 168, 96, 48), "VERIFY_M3_DERIVATION_FAIL")
    framework = result.get("moment_framework", {})
    _check(framework.get("constant_term_method", "").startswith("exact signed closed-walk"), "VERIFY_EXACT_CT_FAIL")
    _check("quadrature" in framework.get("constant_term_method", ""), "VERIFY_CT_METHOD_DISCLOSURE_FAIL")
    _check(framework.get("M1") == "32", "VERIFY_RECORDED_M1_FAIL")
    _check(
        framework.get("M2_over_M1_by_d")
        == {"0": "5", "2": "6", "4": "7", "6": "8", "8": "9"},
        "VERIFY_M2_RATIO_TABLE_FAIL",
    )
    _check(framework.get("M2_coefficients_automatically_derived") == list(m2_solution), "VERIFY_RECORDED_M2_FAIL")
    _check(framework.get("M3_coefficients_automatically_derived") == list(m3_solution), "VERIFY_RECORDED_M3_FAIL")
    _check(framework.get("valid_implication") == "F_k=M_(k+1)-8*M_k>0 implies R>8", "VERIFY_BARRIER_DIRECTION_FAIL")
    _check(framework.get("barrier_status") == "MOMENT_BARRIER_LEMMA_PASS", "VERIFY_BARRIER_STATUS_FAIL")
    _check(framework.get("negative_F_not_sufficient_for_upper_bound") is True, "VERIFY_NEGATIVE_F_LOGIC_FAIL")
    _check(framework.get("finite_moments_do_not_prove_target_bound") is True, "VERIFY_FINITE_MOMENT_LOGIC_FAIL")
    _check(framework.get("target_upper_bound_source") == "Task 40A exact Floquet theorem", "VERIFY_TARGET_SOURCE_FAIL")

    high = result.get("high_defect_proof", {})
    d4 = [q for q in legal if _statistics(q)[0] == 4]
    d6 = [q for q in legal if _statistics(q)[0] == 6]
    d8 = [q for q in legal if _statistics(q)[0] == 8]
    _check(all(2 * _statistics(q)[1] + _statistics(q)[2] >= 4 for q in d4), "VERIFY_D4_COMBINATORICS_FAIL")
    _check(all(_statistics(q)[1] >= 4 for q in d6), "VERIFY_D6_COMBINATORICS_FAIL")
    _check(high.get("d4", {}).get("F2_lower_bound") == 16, "VERIFY_D4_LOWER_FAIL")
    _check(high.get("d6", {}).get("F2_lower_bound") == 288, "VERIFY_D6_LOWER_FAIL")
    _check(high.get("d8", {}).get("F1_value") == 32 and len(d8) == 1, "VERIFY_D8_LOWER_FAIL")
    _check(high.get("conclusion") == "d>=4 implies R(Q)>8", "VERIFY_HIGH_DEFECT_CONCLUSION_FAIL")

    hierarchy = result.get("d2_separation_table", {})
    recorded_rows = hierarchy.get("rows")
    _check(isinstance(recorded_rows, list) and len(recorded_rows) == 4, "VERIFY_D2_TABLE_FAIL")
    first_indices = []
    for separation, row in enumerate(recorded_rows, start=1):
        q = [-1] * N
        q[0] = q[separation] = 1
        q_tuple = tuple(q)
        moments = _moments(q_tuple, 10)
        excesses = [moments[index] - 8 * moments[index - 1] for index in range(1, 10)]
        first = next(((index + 1, value) for index, value in enumerate(excesses) if value > 0), None)
        _check(row.get("separation") == separation, "VERIFY_D2_SEPARATION_FAIL")
        _check(row.get("canonical_q_bits") == _bits(_canonical(q_tuple)), "VERIFY_D2_Q_FAIL")
        _check(row.get("moments_M1_to_M10") == moments, "VERIFY_D2_MOMENTS_FAIL")
        _check(row.get("F1_to_F9") == excesses, "VERIFY_D2_EXCESSES_FAIL")
        _check(row.get("first_positive_F_index") == (None if first is None else first[0]), "VERIFY_D2_FIRST_INDEX_FAIL")
        _check(row.get("first_positive_F_value") == (None if first is None else first[1]), "VERIFY_D2_FIRST_VALUE_FAIL")
        _check(row.get("target") is (separation == 4), "VERIFY_D2_TARGET_FAIL")
        if separation < 4:
            first_indices.append(first[0])
            _check(row.get("conclusion") == "moment barrier gives R>8", "VERIFY_D2_NON_TARGET_CONCLUSION_FAIL")
        else:
            _check(first is None, "VERIFY_TARGET_FALSE_EXCESS_FAIL")
            _check(row.get("conclusion") == "Task 40A gives R=eta<8", "VERIFY_D2_TARGET_CONCLUSION_FAIL")
    _check(first_indices == [4, 6, 9], "VERIFY_D2_HIERARCHY_FAIL")
    _check(hierarchy.get("progressively_longer_detection") is True, "VERIFY_D2_MECHANISM_FAIL")
    _check("do not prove" in hierarchy.get("logic_boundary", ""), "VERIFY_D2_LOGIC_BOUNDARY_FAIL")

    target_q = _canonical(TARGET_Q)
    target_tau = _tau(target_q)
    _check(target_tau == (1, -1, 1, -1, -1, 1, -1, 1), "VERIFY_TARGET_TAU_FAIL")
    _check(all(target_tau[index + 4] == -target_tau[index] for index in range(4)), "VERIFY_TARGET_ANTIPERIOD_FAIL")
    xi = sp.Symbol("xi", nonzero=True)
    z = xi**2
    translation = sp.zeros(N)
    for output in range(N):
        source = output + 4
        cell, residue = divmod(source, N)
        translation[output, residue] = z**cell
    alternating = sp.diag(*((-1) ** index for index in range(N)))
    raw_j = alternating * translation
    j_matrix = xi**-1 * raw_j
    h_matrix = _bloch(target_tau, z)
    _check((raw_j**2 - z * sp.eye(N)).applyfunc(sp.expand) == sp.zeros(N), "VERIFY_RAW_J_SQUARE_FAIL")
    _check((j_matrix**2 - sp.eye(N)).applyfunc(sp.expand) == sp.zeros(N), "VERIFY_J_SQUARE_FAIL")
    _check((j_matrix * h_matrix + h_matrix * j_matrix).applyfunc(sp.expand) == sp.zeros(N), "VERIFY_CHIRAL_ANTICOMMUTATION_FAIL")
    plus = (sp.eye(N) + j_matrix) / 2
    minus = (sp.eye(N) - j_matrix) / 2
    _check(plus.rank() == minus.rank() == 4, "VERIFY_CHIRAL_RANK_FAIL")
    _check((plus * h_matrix * plus).applyfunc(sp.expand) == sp.zeros(N), "VERIFY_CHIRAL_PLUS_BLOCK_FAIL")
    _check((minus * h_matrix * minus).applyfunc(sp.expand) == sp.zeros(N), "VERIFY_CHIRAL_MINUS_BLOCK_FAIL")
    symmetry = result.get("target_symmetry", {})
    _check(symmetry.get("tau") == list(target_tau), "VERIFY_RECORDED_TARGET_TAU_FAIL")
    _check(symmetry.get("tau_antiperiod4") is True, "VERIFY_RECORDED_ANTIPERIOD_FAIL")
    _check(symmetry.get("J_squared") == "I", "VERIFY_RECORDED_J_SQUARE_FAIL")
    _check(symmetry.get("anticommutation") == "J_z*H(z)*J_z^-1=-H(z)", "VERIFY_RECORDED_CHIRAL_FAIL")
    _check(symmetry.get("eigenspace_dimensions") == [4, 4], "VERIFY_RECORDED_BLOCK_DIMENSIONS_FAIL")
    _check("not an involution" in symmetry.get("normalization_caveat", ""), "VERIFY_CHIRAL_NORMALIZATION_FAIL")

    anti_q = []
    for q in legal:
        tau = _tau(q)
        anti = all(tau[index + 4] == -tau[index] for index in range(4))
        criterion = all(q[index + 4] == q[index] for index in range(4)) and math.prod(q[:4]) == -1
        _check(anti == criterion, "VERIFY_ANTIPERIOD_CRITERION_FAIL")
        if anti:
            anti_q.append(q)
    representatives = sorted({_canonical(q) for q in anti_q}, key=_bits)
    _check(len(anti_q) == 8 and [_bits(q) for q in representatives] == ["00010001", "01110111"], "VERIFY_ANTIPERIOD_CLASSES_FAIL")
    anti_record = result.get("antiperiod4_classification", {})
    _check(anti_record.get("legal_q_count") == 8 and anti_record.get("d8_orbit_count") == 2, "VERIFY_RECORDED_ANTIPERIOD_COUNT_FAIL")
    _check(
        [row.get("canonical_q_bits") for row in anti_record.get("orbits", [])]
        == ["00010001", "01110111"],
        "VERIFY_RECORDED_ANTIPERIOD_ORBITS_FAIL",
    )
    _check(anti_record.get("mechanism_boundary") == "chiral symmetry alone does not imply spectral optimality", "VERIFY_CHIRAL_OVERCLAIM_FAIL")

    z = sp.Symbol("z", nonzero=True)
    shift = sp.zeros(N)
    for output in range(N):
        source = output + 1
        cell, residue = divmod(source, N)
        shift[output, residue] = z**cell
    inverse = shift.inv()
    expected_square = 4 * sp.eye(N) + shift**2 + inverse**2 + shift**4 + inverse**4
    _check((_bloch(_tau(ALL_NEGATIVE_Q), z) ** 2 - expected_square).applyfunc(sp.expand) == sp.zeros(N), "VERIFY_BASELINE_IDENTITY_FAIL")
    baseline = result.get("all_unbalanced_baseline", {})
    _check(baseline.get("sharp_squared_constant") == "8", "VERIFY_BASELINE_CONSTANT_FAIL")
    _check(baseline.get("defect_set") == [], "VERIFY_BASELINE_DEFECT_FAIL")

    table_categories: dict[tuple[int, ...], str] = {}
    for row in classification.get("orbits", []):
        representative = tuple(row["canonical_q_signs"])
        category = (
            "BELOW_EIGHT_TARGET"
            if row["target_phase"]
            else ("EQUAL_EIGHT" if row["all_unbalanced_phase"] else "ABOVE_EIGHT")
        )
        for member in _images(representative):
            _check(member not in table_categories, "VERIFY_TASK40B_OVERLAP_FAIL")
            table_categories[member] = category
    _check(set(table_categories) == set(legal), "VERIFY_TASK40B_COVERAGE_FAIL")
    mismatches = [q for q in legal if _structural_category(q) != table_categories[q]]
    _check(not mismatches, "VERIFY_STRUCTURAL_CLASSIFICATION_MISMATCH")
    crosscheck = result.get("task40b_crosscheck", {})
    _check(crosscheck.get("legal_q_compared") == 128, "VERIFY_CROSSCHECK_COUNT_FAIL")
    _check(crosscheck.get("mismatch_count") == 0, "VERIFY_CROSSCHECK_MISMATCH_FAIL")
    _check(
        crosscheck.get("vector_counts")
        == {"BELOW_EIGHT_TARGET": 4, "EQUAL_EIGHT": 1, "ABOVE_EIGHT": 123},
        "VERIFY_TRICHOTOMY_COUNTS_FAIL",
    )
    trichotomy = result.get("eight_barrier_trichotomy", {})
    _check(trichotomy.get("status") == "PERIOD8_EIGHT_BARRIER_TRICHOTOMY_PROVED", "VERIFY_TRICHOTOMY_STATUS_FAIL")
    _check(trichotomy.get("below_eight_iff") == "D(Q)={j,j+4} for some j; then R(Q)=eta", "VERIFY_BELOW_CASE_FAIL")
    _check(trichotomy.get("equal_eight_iff") == "D(Q) is empty; then Q=(-)^8 and R(Q)=8", "VERIFY_EQUAL_CASE_FAIL")
    _check(trichotomy.get("otherwise") == "R(Q)>8", "VERIFY_ABOVE_CASE_FAIL")

    _check(result.get("status") == "PERIOD8_STRUCTURAL_MECHANISM_PROVED", "VERIFY_FINAL_STATUS_FAIL")
    _check(
        result.get("component_statuses")
        == [
            "PERIOD8_EIGHT_BARRIER_TRICHOTOMY_PROVED",
            "PERIOD8_CLOSED_WALK_MECHANISM_PROVED",
            "PERIOD8_TARGET_CHIRAL_MECHANISM_PROVED",
        ],
        "VERIFY_COMPONENT_STATUSES_FAIL",
    )
    expected_scope = {
        "period8_infinite_volume_structural_theorem": "PROVED",
        "finite_size_global_optimality": "NOT_CLAIMED",
        "all_period_global_optimality": "NOT_CLAIMED",
        "all_signings_global_optimality": "NOT_CLAIMED",
        "novelty_audit_started": False,
        "paper_manuscript_started": False,
    }
    _check(result.get("scope") == expected_scope, "VERIFY_SCOPE_OVERCLAIM_FAIL")


def verify_files(
    result_path: Path = DEFAULT_RESULT,
    sharp_path: Path = DEFAULT_SHARP,
    classification_path: Path = DEFAULT_CLASSIFICATION,
    classification_audit_path: Path = DEFAULT_CLASSIFICATION_AUDIT,
    source_path: Path = DEFAULT_SOURCE,
) -> None:
    files = {
        "sharp": sharp_path.read_bytes(),
        "classification": classification_path.read_bytes(),
        "classification_audit": classification_audit_path.read_bytes(),
    }
    verify_structural_data(
        json.loads(result_path.read_text(encoding="utf-8")),
        json.loads(files["sharp"]),
        json.loads(files["classification"]),
        json.loads(files["classification_audit"]),
        {name: _sha(raw) for name, raw in files.items()},
        _sha(source_path.read_bytes()),
    )


def main() -> None:
    try:
        verify_files()
    except Exception as error:
        print(f"Target A period-8 structural verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_STRUCTURAL_MECHANISM_FAIL")
        raise SystemExit(1)
    print("TARGET_A_PERIOD8_STRUCTURAL_MECHANISM_PASS")


if __name__ == "__main__":
    main()
