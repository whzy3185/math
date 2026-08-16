"""Prove the closed-walk and chiral mechanism behind the period-8 optimum."""

from __future__ import annotations

import argparse
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
DEFAULT_SHARP = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
DEFAULT_CLASSIFICATION = RESEARCH_ROOT / "proofs" / "target_a_period8_pattern_classification.json"
DEFAULT_CLASSIFICATION_AUDIT = RESEARCH_ROOT / "audit" / "period8_pattern_classification_audit.json"
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_period8_structural_mechanism.json"
EXPECTED_SHARP_SHA256 = "f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63"
EXPECTED_CLASSIFICATION_SHA256 = "a7a7b7259a99f099c7d2ab756a1a2f4c1ee233214f352d12df9e61cf1b47464c"
EXPECTED_CLASSIFICATION_AUDIT_SHA256 = "274e80a6b43183d4a6137ac3d9a676e6942f1d84a46691cb2b63018b66c69e80"
N = 8
TARGET_Q = (1, -1, -1, -1, 1, -1, -1, -1)
ALL_UNBALANCED_Q = (-1,) * N


class StructuralMechanismError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise StructuralMechanismError(message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def _exact_positive(expression: sp.Expr) -> bool:
    root = to_number_field(sp.simplify(expression)).to_root()
    return root.is_positive is True or sp.simplify(root > 0) is sp.true


def sign_bits(signs: Iterable[int]) -> str:
    return "".join("1" if value == 1 else "0" for value in signs)


def legal_q_vectors() -> list[tuple[int, ...]]:
    return [q for q in itertools.product((-1, 1), repeat=N) if math.prod(q) == 1]


def tau_lift(q: tuple[int, ...]) -> tuple[int, ...]:
    _require(len(q) == N and math.prod(q) == 1, "illegal Q")
    tau = [1]
    for value in q[:-1]:
        tau.append(value * tau[-1])
    _require(tau[-1] * q[-1] == tau[0], "tau lift does not close")
    return tuple(tau)


def reconstruct_q(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[index] * tau[(index + 1) % N] for index in range(N))


def rotate(signs: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= N
    return signs[amount:] + signs[:amount]


def dihedral_images(signs: tuple[int, ...]) -> set[tuple[int, ...]]:
    reflected = tuple(reversed(signs))
    return {rotate(base, amount) for base in (signs, reflected) for amount in range(N)}


def canonical_q(signs: tuple[int, ...]) -> tuple[int, ...]:
    return min(dihedral_images(signs), key=sign_bits)


def defect_statistics(q: tuple[int, ...]) -> dict[str, int]:
    return {
        "d": sum(value == 1 for value in q),
        "a": sum(q[index] == q[(index + 1) % N] == 1 for index in range(N)),
        "b": sum(q[index] == q[(index + 2) % N] == 1 for index in range(N)),
    }


def cyclic_separation(q: tuple[int, ...]) -> int | None:
    positions = [index for index, value in enumerate(q) if value == 1]
    if len(positions) != 2:
        return None
    distance = (positions[1] - positions[0]) % N
    return min(distance, N - distance)


def adjacency_transitions(tau: tuple[int, ...], position: int) -> tuple[tuple[int, int], ...]:
    return (
        (position - 1, 1),
        (position + 1, 1),
        (position - 2, tau[(position - 2) % N]),
        (position + 2, tau[position % N]),
    )


def actual_a2_row(tau: tuple[int, ...], position: int) -> dict[int, int]:
    coefficients: dict[int, int] = {}
    for intermediate, first in adjacency_transitions(tau, position):
        for endpoint, second in adjacency_transitions(tau, intermediate):
            displacement = endpoint - position
            coefficients[displacement] = coefficients.get(displacement, 0) + first * second
    return coefficients


def expected_a2_row(tau: tuple[int, ...], position: int) -> dict[int, int]:
    q = reconstruct_q(tau)
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


def derive_a2_local_formula() -> dict[str, Any]:
    activated_checks = 0
    cancelled_checks = 0
    for tau in itertools.product((-1, 1), repeat=N):
        q = reconstruct_q(tau)
        for position in range(N):
            actual = actual_a2_row(tau, position)
            expected = expected_a2_row(tau, position)
            _require(actual == expected, "FLUX_SQUARE_LOCAL_FORMULA_FAIL")
            for offset in (-3, -1, 1, 3):
                q_index = {
                    -3: position - 3,
                    -1: position - 2,
                    1: position - 1,
                    3: position,
                }[offset] % N
                if q[q_index] == -1:
                    _require(expected[offset] == 0, "negative Q failed to cancel")
                    cancelled_checks += 1
                else:
                    _require(abs(expected[offset]) == 2, "positive Q failed to activate")
                    activated_checks += 1
    return {
        "status": "FLUX_SQUARE_LOCAL_FORMULA_PASS",
        "diagonal": "4",
        "coefficients_by_displacement": {
            "-4": "Q_(i-4)*Q_(i-3)",
            "-3": "tau_(i-3)*(1+Q_(i-3))",
            "-2": "1",
            "-1": "tau_(i-2)*(1+Q_(i-2))",
            "0": "4",
            "+1": "tau_(i-1)*(1+Q_(i-1))",
            "+2": "1",
            "+3": "tau_i*(1+Q_i)",
            "+4": "Q_i*Q_(i+1)",
        },
        "cancelled_odd_coupling_checks": cancelled_checks,
        "activated_odd_coupling_checks": activated_checks,
        "interpretation": "Q=-1 cancels the associated odd-distance coupling; Q=+1 activates amplitude plus or minus two",
    }


def bloch_matrix(tau: tuple[int, ...], z: sp.Expr) -> sp.Matrix:
    matrix = sp.zeros(N)
    for output in range(N):
        for source, coefficient in adjacency_transitions(tau, output):
            cell, residue = divmod(source, N)
            matrix[output, residue] += coefficient * z**cell
    return matrix


def closed_walk_moments(q: tuple[int, ...], maximum_k: int) -> list[int]:
    """Return CT_z tr(H(z)^(2k)) by exact signed-walk dynamic programming."""
    tau = tau_lift(q)
    states = [{start: 1} for start in range(N)]
    moments: list[int] = []
    for length in range(1, 2 * maximum_k + 1):
        next_states: list[dict[int, int]] = []
        for state in states:
            updated: dict[int, int] = {}
            for position, amplitude in state.items():
                for endpoint, coefficient in adjacency_transitions(tau, position):
                    updated[endpoint] = updated.get(endpoint, 0) + amplitude * coefficient
            next_states.append(updated)
        states = next_states
        if length % 2 == 0:
            moments.append(sum(states[start].get(start, 0) for start in range(N)))
    return moments


def derive_moment_formulas() -> dict[str, Any]:
    rows = []
    for q in legal_q_vectors():
        moments = closed_walk_moments(q, 3)
        statistics = defect_statistics(q)
        rows.append((statistics["d"], statistics["a"], statistics["b"], *moments))
    _require(all(row[3] == 32 for row in rows), "M1 formula failed")
    c0, cd = sp.symbols("c0 cd")
    m2_solution = sp.linsolve(
        [sp.Eq(c0 + cd * row[0], row[4]) for row in rows], (c0, cd)
    )
    _require(len(m2_solution) == 1, "M2 coefficient derivation failed")
    m2_coefficients = tuple(next(iter(m2_solution)))
    _require(all(value.is_Integer for value in m2_coefficients), "M2 coefficients are not integral")
    c0, cd, ca, cb = sp.symbols("c0 cd ca cb")
    m3_solution = sp.linsolve(
        [sp.Eq(c0 + cd * row[0] + ca * row[1] + cb * row[2], row[5]) for row in rows],
        (c0, cd, ca, cb),
    )
    _require(len(m3_solution) == 1, "M3 coefficient derivation failed")
    m3_coefficients = tuple(next(iter(m3_solution)))
    _require(all(value.is_Integer for value in m3_coefficients), "M3 coefficients are not integral")
    _require(
        all(row[4] == m2_coefficients[0] + m2_coefficients[1] * row[0] for row in rows),
        "M2 all-Q verification failed",
    )
    _require(
        all(
            row[5]
            == m3_coefficients[0]
            + m3_coefficients[1] * row[0]
            + m3_coefficients[2] * row[1]
            + m3_coefficients[3] * row[2]
            for row in rows
        ),
        "M3 all-Q verification failed",
    )
    _require(m2_coefficients == (160, 16), "M2 structure mismatch")
    _require(m3_coefficients == (944, 168, 96, 48), "M3_STRUCTURE_MISMATCH")
    return {
        "status": "THIRD_MOMENT_LOCAL_STATISTICS_FORMULA_PASS",
        "constant_term_method": "exact signed closed-walk dynamic programming; no quadrature",
        "M1": "32",
        "M2_formula": "160+16*d",
        "M2_over_M1_by_d": {"0": "5", "2": "6", "4": "7", "6": "8", "8": "9"},
        "M2_coefficients_automatically_derived": list(map(int, m2_coefficients)),
        "M2_status": "SECOND_MOMENT_DEFECT_COUNT_FORMULA_PASS",
        "M3_formula": "944+168*d+96*a+48*b",
        "M3_coefficients_automatically_derived": list(map(int, m3_coefficients)),
        "F2_formula": "-336+40*d+96*a+48*b",
        "verified_legal_q_count": len(rows),
        "interaction_interpretation": {
            "168*d": "single activated positive-flux positions",
            "96*a": "additional interaction of adjacent activated positions",
            "48*b": "additional interaction at cyclic distance two",
            "higher_interactions": "none at length six",
        },
    }


def moment_barrier_lemma() -> dict[str, Any]:
    return {
        "status": "MOMENT_BARRIER_LEMMA_PASS",
        "definition": "M_k=CT_z tr(H(z)^(2k))=(1/(2*pi))*integral tr(H(e^(i*theta))^(2k)) dtheta",
        "pointwise_argument": "if R<=8 then 0<=lambda_j(theta)^2<=8, hence y^(k+1)<=8*y^k",
        "valid_implication": "F_k=M_(k+1)-8*M_k>0 implies R>8",
        "negative_F_not_sufficient_for_upper_bound": True,
        "finite_moments_do_not_prove_target_bound": True,
        "target_upper_bound_source": "Task 40A exact Floquet theorem",
    }


def high_defect_proof() -> dict[str, Any]:
    q_vectors = legal_q_vectors()
    d4 = [q for q in q_vectors if defect_statistics(q)["d"] == 4]
    d6 = [q for q in q_vectors if defect_statistics(q)["d"] == 6]
    d8 = [q for q in q_vectors if defect_statistics(q)["d"] == 8]
    _require(all(2 * defect_statistics(q)["a"] + defect_statistics(q)["b"] >= 4 for q in d4), "d4 inequality failed")
    _require(all(defect_statistics(q)["a"] >= 4 for q in d6), "d6 inequality failed")
    _require(len(d8) == 1, "d8 shell mismatch")
    return {
        "status": "HIGH_DEFECT_EIGHT_BARRIER_PASS",
        "d4": {
            "cyclic_gap_proof": (
                "write the four positive cyclic gaps as positive integers summing to eight; "
                "if n1>=2 then 2a>=4, if n1=0 all gaps are two and b=4, and if n1=1 "
                "the other gaps are 2,2,3 so 2a+b=4"
            ),
            "inequality": "2*a+b>=4",
            "F2_lower_bound": 16,
            "machine_crosscheck_count": len(d4),
        },
        "d6": {
            "complement_proof": (
                "two negative positions destroy at most four of the eight adjacent positive-positive edges"
            ),
            "inequality": "a>=4",
            "F2_lower_bound": 288,
            "machine_crosscheck_count": len(d6),
        },
        "d8": {
            "certificate": "M2-8*M1=288-256=32>0",
            "F1_value": 32,
            "machine_crosscheck_count": len(d8),
        },
        "conclusion": "d>=4 implies R(Q)>8",
    }


def d2_moment_hierarchy() -> dict[str, Any]:
    rows = []
    for separation in range(1, 5):
        q = [-1] * N
        q[0] = q[separation] = 1
        q_tuple = tuple(q)
        moments = closed_walk_moments(q_tuple, 10)
        excesses = [moments[index] - 8 * moments[index - 1] for index in range(1, 10)]
        first = next(((index + 1, value) for index, value in enumerate(excesses) if value > 0), None)
        is_target = separation == 4
        _require((first is None) == is_target, "D2 moment hierarchy classification failed")
        rows.append(
            {
                "separation": separation,
                "canonical_q_bits": sign_bits(canonical_q(q_tuple)),
                "moments_M1_to_M10": moments,
                "F1_to_F9": excesses,
                "first_positive_F_index": None if first is None else first[0],
                "first_positive_F_value": None if first is None else first[1],
                "target": is_target,
                "conclusion": "Task 40A gives R=eta<8" if is_target else "moment barrier gives R>8",
            }
        )
    indices = [row["first_positive_F_index"] for row in rows[:3]]
    _require(indices == [4, 6, 9], "d2 first-positive hierarchy mismatch")
    return {
        "status": "D2_MOMENT_HIERARCHY_PASS",
        "rows": rows,
        "first_positive_indices_for_s1_s2_s3": indices,
        "progressively_longer_detection": True,
        "equal_spacing_status": "EQUAL_SPACING_DEFECT_MECHANISM_PASS",
        "logic_boundary": "the first ten negative target excesses do not prove R<8; Task 40A does",
    }


def target_chiral_symmetry() -> dict[str, Any]:
    q = canonical_q(TARGET_Q)
    tau = tau_lift(q)
    _require(all(tau[index + 4] == -tau[index] for index in range(4)), "target tau is not anti-periodic")
    xi = sp.Symbol("xi", nonzero=True)
    z = xi**2
    translation4 = sp.zeros(N)
    for output in range(N):
        source = output + 4
        cell, residue = divmod(source, N)
        translation4[output, residue] = z**cell
    alternating = sp.diag(*((-1) ** index for index in range(N)))
    raw_j = alternating * translation4
    normalized_j = xi**-1 * raw_j
    matrix = bloch_matrix(tau, z)
    _require((raw_j**2 - z * sp.eye(N)).applyfunc(sp.expand) == sp.zeros(N), "raw chiral square failed")
    _require((normalized_j**2 - sp.eye(N)).applyfunc(sp.expand) == sp.zeros(N), "normalized J square failed")
    _require((normalized_j * matrix + matrix * normalized_j).applyfunc(sp.expand) == sp.zeros(N), "chiral anticommutation failed")
    plus = (sp.eye(N) + normalized_j) / 2
    minus = (sp.eye(N) - normalized_j) / 2
    _require(plus.rank() == minus.rank() == 4, "chiral eigenspace dimensions failed")
    _require((plus * matrix * plus).applyfunc(sp.expand) == sp.zeros(N), "plus diagonal block failed")
    _require((minus * matrix * minus).applyfunc(sp.expand) == sp.zeros(N), "minus diagonal block failed")
    return {
        "status": "TARGET_CHIRAL_SYMMETRY_PASS",
        "tau": list(tau),
        "tau_antiperiod4": True,
        "raw_operator": "J_raw=D*T4 and J_raw^2=T8; on the z fiber J_raw^2=z*I",
        "J_definition": "choose xi with xi^2=z and set J_z=xi^-1*D*T4(z)",
        "J_squared": "I",
        "anticommutation": "J_z*H(z)*J_z^-1=-H(z)",
        "eigenspace_dimensions": [4, 4],
        "block_reduction": "H is off-diagonal between J=+1 and J=-1 spaces; H^2 reduces to BB* and B*B",
        "even_polynomial_explanation": "chiral conjugacy sends H to -H, so the degree-eight characteristic polynomial is even",
        "normalization_caveat": "un-normalized D*T4 is not an involution on a general Bloch fiber",
        "total_status": "PERIOD8_TARGET_CHIRAL_MECHANISM_PROVED",
    }


def antiperiod4_classification() -> dict[str, Any]:
    anti_q = []
    for q in legal_q_vectors():
        tau = tau_lift(q)
        anti = all(tau[index + 4] == -tau[index] for index in range(4))
        criterion = all(q[index + 4] == q[index] for index in range(4)) and math.prod(q[:4]) == -1
        _require(anti == criterion, "anti-period-4 criterion failed")
        if anti:
            anti_q.append(q)
    representatives = sorted({canonical_q(q) for q in anti_q}, key=sign_bits)
    _require(len(anti_q) == 8 and len(representatives) == 2, "anti-period-4 orbit count failed")
    _require(representatives == [canonical_q(TARGET_Q), ( -1, 1, 1, 1, -1, 1, 1, 1)], "unexpected anti-period-4 orbits")
    return {
        "status": "ANTIPERIOD4_FLUX_CLASSIFICATION_PASS",
        "iff_criterion": "Q_(i+4)=Q_i and product_(i=0)^3 Q_i=-1",
        "legal_q_count": len(anti_q),
        "d8_orbit_count": len(representatives),
        "orbits": [
            {
                "canonical_q_bits": sign_bits(q),
                "defect_count": defect_statistics(q)["d"],
                "spectral_classification": "R=eta<8" if TARGET_Q in dihedral_images(q) else "R>8 by high-defect moment proof",
            }
            for q in representatives
        ],
        "mechanism_boundary": "chiral symmetry alone does not imply spectral optimality",
    }


def load_dependencies(
    sharp_path: Path = DEFAULT_SHARP,
    classification_path: Path = DEFAULT_CLASSIFICATION,
    classification_audit_path: Path = DEFAULT_CLASSIFICATION_AUDIT,
) -> dict[str, Any]:
    paths = {
        "sharp": (sharp_path, EXPECTED_SHARP_SHA256),
        "classification": (classification_path, EXPECTED_CLASSIFICATION_SHA256),
        "classification_audit": (classification_audit_path, EXPECTED_CLASSIFICATION_AUDIT_SHA256),
    }
    loaded = {}
    for name, (path, expected_sha) in paths.items():
        raw = path.read_bytes()
        _require(_sha256_bytes(raw) == expected_sha, f"{name} dependency SHA mismatch")
        loaded[name] = {"payload": json.loads(raw), "sha256": _sha256_bytes(raw)}
    _require(loaded["sharp"]["payload"].get("status") == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED", "sharp status mismatch")
    _require(
        loaded["classification"]["payload"].get("status")
        == "PERIOD8_UNIQUE_OPTIMUM_AND_SECOND_BEST_PROVED",
        "classification status mismatch",
    )
    _require(
        loaded["classification_audit"]["payload"].get("status")
        == "PERIOD8_PATTERN_CLASSIFICATION_INDEPENDENTLY_AUDITED",
        "classification audit status mismatch",
    )
    return loaded


def structural_category(q: tuple[int, ...]) -> str:
    d = defect_statistics(q)["d"]
    if d == 0:
        return "EQUAL_EIGHT"
    if d == 2 and cyclic_separation(q) == 4:
        return "BELOW_EIGHT_TARGET"
    return "ABOVE_EIGHT"


def task40b_crosscheck(classification: dict[str, Any]) -> dict[str, Any]:
    table_categories: dict[tuple[int, ...], str] = {}
    for row in classification["orbits"]:
        representative = tuple(row["canonical_q_signs"])
        if row["target_phase"]:
            category = "BELOW_EIGHT_TARGET"
        elif row["all_unbalanced_phase"]:
            category = "EQUAL_EIGHT"
        else:
            category = "ABOVE_EIGHT"
        for member in dihedral_images(representative):
            _require(member not in table_categories, "Task 40B orbit overlap")
            table_categories[member] = category
    legal = legal_q_vectors()
    _require(set(table_categories) == set(legal), "Task 40B coverage mismatch")
    mismatches = [q for q in legal if structural_category(q) != table_categories[q]]
    _require(not mismatches, "STRUCTURAL_CLASSIFICATION_MISMATCH")
    counts = {category: sum(structural_category(q) == category for q in legal) for category in (
        "BELOW_EIGHT_TARGET", "EQUAL_EIGHT", "ABOVE_EIGHT"
    )}
    return {
        "status": "TASK40B_STRUCTURAL_CROSSCHECK_PASS",
        "route_a": "Task 40B 18-orbit exact endpoint Rayleigh classification",
        "route_b": "Task 40C local A^2, moments, defect geometry, and Task 40A target theorem",
        "legal_q_compared": len(legal),
        "mismatch_count": len(mismatches),
        "vector_counts": counts,
    }


def all_unbalanced_baseline() -> dict[str, Any]:
    tau = tau_lift(ALL_UNBALANCED_Q)
    z = sp.Symbol("z", nonzero=True)
    shift = sp.zeros(N)
    for output in range(N):
        source = output + 1
        cell, residue = divmod(source, N)
        shift[output, residue] = z**cell
    inverse = shift.inv()
    expected = 4 * sp.eye(N) + shift**2 + inverse**2 + shift**4 + inverse**4
    _require((bloch_matrix(tau, z) ** 2 - expected).applyfunc(sp.expand) == sp.zeros(N), "baseline identity failed")
    return {
        "status": "ALL_UNBALANCED_CANCELLATION_BASELINE_PASS",
        "defect_set": [],
        "square_identity": "A^2=4I+S^2+S^-2+S^4+S^-4",
        "fourier_symbol": "4+2*cos(2*theta)+2*cos(4*theta)<=8",
        "attainment": "theta=0",
        "sharp_squared_constant": "8",
        "interpretation": "the empty defect set cancels every odd-distance coupling in A^2",
    }


def run_structural_mechanism(
    sharp_path: Path = DEFAULT_SHARP,
    classification_path: Path = DEFAULT_CLASSIFICATION,
    classification_audit_path: Path = DEFAULT_CLASSIFICATION_AUDIT,
    result_path: Path = DEFAULT_RESULT,
) -> dict[str, Any]:
    dependencies = load_dependencies(sharp_path, classification_path, classification_audit_path)
    a2_formula = derive_a2_local_formula()
    baseline = all_unbalanced_baseline()
    moments = derive_moment_formulas()
    barrier = moment_barrier_lemma()
    high_defect = high_defect_proof()
    d2 = d2_moment_hierarchy()
    chiral = target_chiral_symmetry()
    antiperiod = antiperiod4_classification()
    crosscheck = task40b_crosscheck(dependencies["classification"]["payload"])
    eta = sp.sympify(dependencies["sharp"]["payload"]["eta_squared"]["exact_radical"])
    _require(_exact_positive(8 - eta), "eta is not below eight")
    result = {
        "schema_version": 1,
        "status": "PERIOD8_STRUCTURAL_MECHANISM_PROVED",
        "component_statuses": [
            "PERIOD8_EIGHT_BARRIER_TRICHOTOMY_PROVED",
            "PERIOD8_CLOSED_WALK_MECHANISM_PROVED",
            "PERIOD8_TARGET_CHIRAL_MECHANISM_PROVED",
        ],
        "dependencies": {
            name: {
                "sha256": dependency["sha256"],
                "status": dependency["payload"]["status"],
            }
            for name, dependency in dependencies.items()
        },
        "A2_local_formula": a2_formula,
        "defect_definition": "D(Q)={i:Q_i=+1}; d=|D(Q)|",
        "defect_coupling_interpretation": a2_formula["interpretation"],
        "all_unbalanced_baseline": baseline,
        "moment_framework": {
            **barrier,
            **moments,
            "barrier_status": barrier["status"],
        },
        "high_defect_proof": high_defect,
        "d2_separation_table": d2,
        "target_symmetry": chiral,
        "antiperiod4_classification": antiperiod,
        "eight_barrier_trichotomy": {
            "status": "PERIOD8_EIGHT_BARRIER_TRICHOTOMY_PROVED",
            "below_eight_iff": "D(Q)={j,j+4} for some j; then R(Q)=eta",
            "equal_eight_iff": "D(Q) is empty; then Q=(-)^8 and R(Q)=8",
            "otherwise": "R(Q)>8",
            "eta": dependencies["sharp"]["payload"]["eta_squared"]["exact_radical"],
            "proof_dependencies": [
                "all-unbalanced cancellation baseline",
                "d>=4 moment inequalities",
                "d=2 separation moment hierarchy",
                "Task 40A exact target theorem",
            ],
        },
        "task40b_crosscheck": crosscheck,
        "scope": {
            "period8_infinite_volume_structural_theorem": "PROVED",
            "finite_size_global_optimality": "NOT_CLAIMED",
            "all_period_global_optimality": "NOT_CLAIMED",
            "all_signings_global_optimality": "NOT_CLAIMED",
            "novelty_audit_started": False,
            "paper_manuscript_started": False,
        },
        "checker": {
            "path": "research/scripts/verify_target_a_period8_structural_mechanism.py",
            "status": "TARGET_A_PERIOD8_STRUCTURAL_MECHANISM_PASS",
        },
        "script_sha256": _sha256_file(Path(__file__).resolve()),
        "next_gate": "Task 41 current novelty and priority audit",
    }
    _write_json(result_path, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sharp", type=Path, default=DEFAULT_SHARP)
    parser.add_argument("--classification", type=Path, default=DEFAULT_CLASSIFICATION)
    parser.add_argument("--classification-audit", type=Path, default=DEFAULT_CLASSIFICATION_AUDIT)
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()
    try:
        result = run_structural_mechanism(
            args.sharp, args.classification, args.classification_audit, args.output
        )
    except Exception as error:
        print(f"Target A period-8 structural mechanism failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_STRUCTURAL_MECHANISM_FAIL")
        raise SystemExit(1)
    for status in result["component_statuses"]:
        print(status)
    print(result["status"])


if __name__ == "__main__":
    main()
