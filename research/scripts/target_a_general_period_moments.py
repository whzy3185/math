"""Prove general-period closed-walk identities and eight-barrier obstructions."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_general_period_moment_obstructions.json"
SMALL_PERIOD_MAX = 12
LAURENT_PERIOD_MAX = 6
RANDOM_PERIODS = (13, 17, 24, 31, 48)
RANDOM_SAMPLES_PER_PERIOD = 64
RANDOM_SEED = 42042
STEPS = (-2, -1, 1, 2)


class GeneralPeriodMomentError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise GeneralPeriodMomentError(message)


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def sign_bits(signs: Iterable[int]) -> str:
    return "".join("1" if value == 1 else "0" for value in signs)


def reconstruct_q(tau: tuple[int, ...]) -> tuple[int, ...]:
    p = len(tau)
    _require(p >= 1 and set(tau) <= {-1, 1}, "invalid tau word")
    return tuple(tau[index] * tau[(index + 1) % p] for index in range(p))


def tau_lift(q: tuple[int, ...]) -> tuple[int, ...]:
    _require(len(q) >= 1 and set(q) <= {-1, 1}, "invalid Q word")
    _require(math.prod(q) == 1, "Q does not admit a periodic tau lift")
    tau = [1]
    for value in q[:-1]:
        tau.append(value * tau[-1])
    _require(tau[-1] * q[-1] == tau[0], "tau lift failed to close")
    return tuple(tau)


def legal_q_vectors(p: int) -> Iterable[tuple[int, ...]]:
    _require(p >= 1, "period must be positive")
    for prefix in itertools.product((-1, 1), repeat=p - 1):
        yield prefix + (math.prod(prefix),)


def defect_statistics(q: tuple[int, ...]) -> dict[str, int]:
    p = len(q)
    return {
        "d": sum(value == 1 for value in q),
        "a": sum(q[index] == q[(index + 1) % p] == 1 for index in range(p)),
        "b": sum(q[index] == q[(index + 2) % p] == 1 for index in range(p)),
    }


def adjacency_transitions(
    tau: tuple[int, ...], position: int
) -> tuple[tuple[int, int], ...]:
    p = len(tau)
    return (
        (position - 1, 1),
        (position + 1, 1),
        (position - 2, tau[(position - 2) % p]),
        (position + 2, tau[position % p]),
    )


def actual_a2_row(tau: tuple[int, ...], position: int) -> dict[int, int]:
    coefficients: dict[int, int] = {}
    for intermediate, first in adjacency_transitions(tau, position):
        for endpoint, second in adjacency_transitions(tau, intermediate):
            displacement = endpoint - position
            coefficients[displacement] = coefficients.get(displacement, 0) + first * second
    return coefficients


def expected_a2_row(tau: tuple[int, ...], position: int) -> dict[int, int]:
    p = len(tau)
    q = reconstruct_q(tau)
    return {
        -4: q[(position - 4) % p] * q[(position - 3) % p],
        -3: tau[(position - 3) % p] * (1 + q[(position - 3) % p]),
        -2: 1,
        -1: tau[(position - 2) % p] * (1 + q[(position - 2) % p]),
        0: 4,
        1: tau[(position - 1) % p] * (1 + q[(position - 1) % p]),
        2: 1,
        3: tau[position % p] * (1 + q[position % p]),
        4: q[position % p] * q[(position + 1) % p],
    }


def derive_general_a2_formula() -> dict[str, Any]:
    checked_words = 0
    checked_rows = 0
    for p in range(1, 9):
        for tau in itertools.product((-1, 1), repeat=p):
            checked_words += 1
            for position in range(p):
                _require(
                    actual_a2_row(tau, position) == expected_a2_row(tau, position),
                    "GENERAL_A2_LOCAL_FORMULA_MISMATCH",
                )
                checked_rows += 1
    return {
        "status": "GENERAL_FLUX_SQUARE_LOCAL_FORMULA_PROVED",
        "derivation": "direct multiplication of the four infinite-lattice transitions",
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
        "period_independent": True,
        "exhaustive_tau_periods": [1, 8],
        "checked_tau_words": checked_words,
        "checked_rows": checked_rows,
    }


def _tau_index_for_step(position: int, step: int) -> int | None:
    if step == 2:
        return position
    if step == -2:
        return position - 2
    return None


def _q_support_from_tau_support(tau_support: set[int]) -> tuple[int, ...]:
    """Rewrite an even tau monomial as Q intervals, reducing exponents mod two."""
    endpoints = sorted(tau_support)
    _require(len(endpoints) % 2 == 0, "closed walk produced an odd tau monomial")
    q_support: set[int] = set()
    for left, right in zip(endpoints[::2], endpoints[1::2]):
        for index in range(left, right):
            if index in q_support:
                q_support.remove(index)
            else:
                q_support.add(index)
    return tuple(sorted(q_support))


def _normalized_support(support: tuple[int, ...]) -> tuple[int, ...]:
    if not support:
        return ()
    origin = min(support)
    return tuple(index - origin for index in support)


def _support_key(support: tuple[int, ...]) -> str:
    return "const" if not support else ",".join(map(str, support))


def closed_walk_q_expansion(length: int) -> dict[str, Any]:
    """Enumerate closed step words and collect their exact Q monomials."""
    raw: Counter[tuple[int, ...]] = Counter()
    closed_words = 0
    for word in itertools.product(STEPS, repeat=length):
        if sum(word) != 0:
            continue
        closed_words += 1
        position = 0
        tau_support: set[int] = set()
        for step in word:
            tau_index = _tau_index_for_step(position, step)
            if tau_index is not None:
                if tau_index in tau_support:
                    tau_support.remove(tau_index)
                else:
                    tau_support.add(tau_index)
            position += step
        raw[_q_support_from_tau_support(tau_support)] += 1
    translated: Counter[tuple[int, ...]] = Counter()
    for support, coefficient in raw.items():
        translated[_normalized_support(support)] += coefficient
    return {
        "length": length,
        "closed_step_words": closed_words,
        "raw_monomial_count": len(raw),
        "translation_class_coefficients": {
            _support_key(support): coefficient
            for support, coefficient in sorted(translated.items())
        },
        "raw_coefficients": {
            _support_key(support): coefficient
            for support, coefficient in sorted(raw.items())
        },
    }


def closed_walk_moments_from_tau(tau: tuple[int, ...], maximum_k: int) -> list[int]:
    p = len(tau)
    states = [{start: 1} for start in range(p)]
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
            moments.append(sum(states[start].get(start, 0) for start in range(p)))
    return moments


def closed_walk_moments(q: tuple[int, ...], maximum_k: int = 3) -> list[int]:
    return closed_walk_moments_from_tau(tau_lift(q), maximum_k)


def formula_moments(q: tuple[int, ...]) -> list[int]:
    p = len(q)
    statistics = defect_statistics(q)
    d, a, b = statistics["d"], statistics["a"], statistics["b"]
    return [4 * p, 20 * p + 16 * d, 118 * p + 168 * d + 96 * a + 48 * b]


def _poly_add(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
        if result[exponent] == 0:
            del result[exponent]
    return result


def _poly_multiply(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for first_power, first_coefficient in left.items():
        for second_power, second_coefficient in right.items():
            power = first_power + second_power
            result[power] = result.get(power, 0) + first_coefficient * second_coefficient
    return {power: coefficient for power, coefficient in result.items() if coefficient}


def _bloch_laurent_matrix(tau: tuple[int, ...]) -> list[list[dict[int, int]]]:
    p = len(tau)
    matrix = [[{} for _ in range(p)] for _ in range(p)]
    for output in range(p):
        for source, coefficient in adjacency_transitions(tau, output):
            cell, residue = divmod(source, p)
            matrix[output][residue] = _poly_add(matrix[output][residue], {cell: coefficient})
    return matrix


def _matrix_multiply(
    left: list[list[dict[int, int]]], right: list[list[dict[int, int]]]
) -> list[list[dict[int, int]]]:
    p = len(left)
    result = [[{} for _ in range(p)] for _ in range(p)]
    for row in range(p):
        for middle in range(p):
            if not left[row][middle]:
                continue
            for column in range(p):
                if right[middle][column]:
                    product = _poly_multiply(left[row][middle], right[middle][column])
                    result[row][column] = _poly_add(result[row][column], product)
    return result


def laurent_constant_term_moments(q: tuple[int, ...], maximum_k: int = 3) -> list[int]:
    matrix = _bloch_laurent_matrix(tau_lift(q))
    power = [[{0: int(row == column)} for column in range(len(q))] for row in range(len(q))]
    moments = []
    for exponent in range(1, 2 * maximum_k + 1):
        power = _matrix_multiply(power, matrix)
        if exponent % 2 == 0:
            moments.append(sum(power[index][index].get(0, 0) for index in range(len(q))))
    return moments


def _rotate(word: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= len(word)
    return word[amount:] + word[:amount]


def verify_moment_identities() -> dict[str, Any]:
    exhaustive_count = 0
    laurent_count = 0
    invariance_count = 0
    by_period: dict[str, int] = {}
    for p in range(1, SMALL_PERIOD_MAX + 1):
        period_count = 0
        for q in legal_q_vectors(p):
            exact = closed_walk_moments(q)
            _require(exact == formula_moments(q), "GENERAL_MOMENT_FORMULA_MISMATCH")
            tau = tau_lift(q)
            _require(
                closed_walk_moments_from_tau(tuple(-value for value in tau), 3) == exact,
                "TAU_FLIP_MOMENT_MISMATCH",
            )
            _require(closed_walk_moments(_rotate(q, 1)) == exact, "TRANSLATION_MOMENT_MISMATCH")
            _require(closed_walk_moments(tuple(reversed(q))) == exact, "REFLECTION_MOMENT_MISMATCH")
            invariance_count += 3
            if p <= LAURENT_PERIOD_MAX:
                _require(
                    laurent_constant_term_moments(q) == exact,
                    "LAURENT_CONSTANT_TERM_MISMATCH",
                )
                laurent_count += 1
            exhaustive_count += 1
            period_count += 1
        by_period[str(p)] = period_count

    generator = random.Random(RANDOM_SEED)
    random_count = 0
    for p in RANDOM_PERIODS:
        for _ in range(RANDOM_SAMPLES_PER_PERIOD):
            prefix = tuple(generator.choice((-1, 1)) for _ in range(p - 1))
            q = prefix + (math.prod(prefix),)
            exact = closed_walk_moments(q)
            _require(exact == formula_moments(q), "RANDOM_GENERAL_MOMENT_FORMULA_MISMATCH")
            _require(closed_walk_moments(_rotate(q, generator.randrange(p))) == exact, "RANDOM_TRANSLATION_MISMATCH")
            _require(closed_walk_moments(tuple(reversed(q))) == exact, "RANDOM_REFLECTION_MISMATCH")
            random_count += 1
            invariance_count += 2
    return {
        "status": "GENERAL_PERIOD_MOMENT_MACHINE_CHECKS_PASS",
        "exhaustive_period_range": [1, SMALL_PERIOD_MAX],
        "legal_q_by_period": by_period,
        "exhaustive_legal_q_count": exhaustive_count,
        "independent_laurent_ct_period_range": [1, LAURENT_PERIOD_MAX],
        "independent_laurent_ct_count": laurent_count,
        "random_seed": RANDOM_SEED,
        "random_periods": list(RANDOM_PERIODS),
        "random_samples_per_period": RANDOM_SAMPLES_PER_PERIOD,
        "random_check_count": random_count,
        "invariance_check_count": invariance_count,
        "arithmetic": "exact integers and Laurent-polynomial constant terms; no quadrature",
    }


def derive_moment_identities() -> dict[str, Any]:
    expansions = {length: closed_walk_q_expansion(length) for length in (2, 4, 6)}
    expected = {
        2: {"const": 4},
        4: {"const": 28, "0": 8},
        6: {"const": 238, "0": 156, "0,1": 24, "0,2": 12},
    }
    for length, coefficients in expected.items():
        _require(
            expansions[length]["translation_class_coefficients"] == coefficients,
            "CLOSED_WALK_SYMBOLIC_EXPANSION_MISMATCH",
        )
    return {
        "status": "GENERAL_PERIOD_CLOSED_WALK_IDENTITIES_PROVED",
        "derivation_method": (
            "enumerate all closed step words over {-2,-1,1,2}; reduce tau exponents "
            "modulo two; rewrite paired tau endpoints as Q intervals; collect translation classes"
        ),
        "expansions": [expansions[length] for length in (2, 4, 6)],
        "Q_basis_identities": {
            "M1": "4*p",
            "M2": "28*p+8*sum_i Q_i",
            "M3": "238*p+156*sum_i Q_i+24*sum_i Q_i*Q_(i+1)+12*sum_i Q_i*Q_(i+2)",
        },
        "defect_basis_change": "I_i=(1+Q_i)/2; d=sum I_i; a=sum I_i*I_(i+1); b=sum I_i*I_(i+2)",
        "defect_basis_identities": {
            "M1": "4*p",
            "M2": "20*p+16*d",
            "M3": "118*p+168*d+96*a+48*b",
        },
        "locality_statement": "through length six, only single defects and pairs at cyclic offsets one and two occur",
    }


def barrier_obstructions() -> dict[str, Any]:
    return {
        "status": "GENERAL_PERIOD_CLOSED_WALK_OBSTRUCTIONS_PROVED",
        "spectral_definition": "R(Q)=sup_(|z|=1) rho(H_(p,Q)(z))^2",
        "moment_inequality": "R(Q)<=8 implies M_(k+1)<=8*M_k for every k>=1",
        "proof": "for y=lambda^2 in [0,8], y^(k+1)<=8*y^k; sum over bands and average over the Bloch phase",
        "valid_contrapositive": "F_k=M_(k+1)-8*M_k>0 implies R(Q)>8",
        "F1": "16*d-12*p",
        "density_necessary_condition": "R(Q)<=8 implies d<=3*p/4",
        "density_status": "GENERAL_PERIOD_DEFECT_DENSITY_OBSTRUCTION_PROVED",
        "F2": "-42*p+40*d+96*a+48*b",
        "cluster_necessary_condition": "R(Q)<=8 implies 40*d+96*a+48*b<=42*p",
        "cluster_status": "GENERAL_PERIOD_LOCAL_CLUSTER_OBSTRUCTION_PROVED",
        "strict_conclusions": {
            "density": "16*d-12*p>0 implies R(Q)>8",
            "cluster": "40*d+96*a+48*b-42*p>0 implies R(Q)>8",
        },
        "logical_limits": {
            "conditions_are_sufficient_for_R_le_8": False,
            "nonpositive_excess_proves_R_le_8": False,
            "target_globally_optimal_among_all_periods": False,
        },
    }


def run_general_period_proof(result_path: Path = DEFAULT_RESULT) -> dict[str, Any]:
    result = {
        "schema_version": 1,
        "status": "GENERAL_PERIOD_CLOSED_WALK_OBSTRUCTIONS_PROVED",
        "component_statuses": [
            "GENERAL_PERIOD_CLOSED_WALK_IDENTITIES_PROVED",
            "GENERAL_PERIOD_DEFECT_DENSITY_OBSTRUCTION_PROVED",
            "GENERAL_PERIOD_LOCAL_CLUSTER_OBSTRUCTION_PROVED",
        ],
        "setup": {
            "period": "arbitrary integer p>=1",
            "tau_periodicity": "tau_(i+p)=tau_i",
            "flux": "Q_i=tau_i*tau_(i+1)",
            "legal_condition": "product_(i=0)^(p-1) Q_i=1",
            "moments": "M_k(Q)=CT_z tr(H_(p,Q)(z)^(2k))",
        },
        "A2_local_formula": derive_general_a2_formula(),
        "moment_identities": derive_moment_identities(),
        "machine_checks": verify_moment_identities(),
        "obstructions": barrier_obstructions(),
        "scope": {
            "arbitrary_period_necessary_conditions": "PROVED",
            "conditions_sufficient_for_sub_eight": "NOT_CLAIMED",
            "all_period_global_optimality": "NOT_CLAIMED",
            "finite_size_global_optimality": "NOT_CLAIMED",
            "all_signings_global_optimality": "NOT_CLAIMED",
            "M4_formula": "NOT_EXPLORED_IN_THEOREM_PACKAGE",
            "paper_manuscript_started": False,
        },
        "checker": {
            "path": "research/scripts/verify_target_a_general_period_moments.py",
            "expected_status": "TARGET_A_GENERAL_PERIOD_MOMENTS_PASS",
        },
        "script_sha256": _sha256_file(Path(__file__).resolve()),
        "next_gate": "Task 42B complete low-period frontier p<=16",
    }
    _write_json(result_path, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()
    try:
        result = run_general_period_proof(args.output)
    except Exception as error:
        print(f"Target A general-period moments failed: {error}", file=sys.stderr)
        print("TARGET_A_GENERAL_PERIOD_MOMENTS_FAIL")
        raise SystemExit(1)
    for status in result["component_statuses"]:
        print(status)
    print(result["status"])


if __name__ == "__main__":
    main()
