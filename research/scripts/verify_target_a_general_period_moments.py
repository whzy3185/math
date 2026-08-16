"""Independently verify the general-period Target A moment theorem package."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_general_period_moment_obstructions.json"
DEFAULT_SOURCE = RESEARCH_ROOT / "scripts" / "target_a_general_period_moments.py"
STEPS = (-2, -1, 1, 2)


class GeneralPeriodVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise GeneralPeriodVerificationError(message)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _tau(q: tuple[int, ...]) -> tuple[int, ...]:
    _check(q and set(q) <= {-1, 1} and math.prod(q) == 1, "VERIFY_ILLEGAL_Q")
    values = [1]
    for sign in q[:-1]:
        values.append(sign * values[-1])
    _check(values[-1] * q[-1] == values[0], "VERIFY_TAU_CLOSURE_FAIL")
    return tuple(values)


def _transitions(tau: tuple[int, ...], position: int) -> tuple[tuple[int, int], ...]:
    p = len(tau)
    return (
        (position - 1, 1),
        (position + 1, 1),
        (position - 2, tau[(position - 2) % p]),
        (position + 2, tau[position % p]),
    )


def _moments(q: tuple[int, ...]) -> list[int]:
    tau = _tau(q)
    p = len(q)
    states = [{start: 1} for start in range(p)]
    result = []
    for length in range(1, 7):
        updated_states = []
        for state in states:
            updated: dict[int, int] = {}
            for position, amplitude in state.items():
                for endpoint, sign in _transitions(tau, position):
                    updated[endpoint] = updated.get(endpoint, 0) + amplitude * sign
            updated_states.append(updated)
        states = updated_states
        if length % 2 == 0:
            result.append(sum(states[start].get(start, 0) for start in range(p)))
    return result


def _statistics(q: tuple[int, ...]) -> tuple[int, int, int]:
    p = len(q)
    return (
        sum(value == 1 for value in q),
        sum(q[index] == q[(index + 1) % p] == 1 for index in range(p)),
        sum(q[index] == q[(index + 2) % p] == 1 for index in range(p)),
    )


def _formula(q: tuple[int, ...]) -> list[int]:
    p = len(q)
    d, a, b = _statistics(q)
    return [4 * p, 20 * p + 16 * d, 118 * p + 168 * d + 96 * a + 48 * b]


def _q_support(tau_support: set[int]) -> tuple[int, ...]:
    endpoints = sorted(tau_support)
    _check(len(endpoints) % 2 == 0, "VERIFY_ODD_TAU_MONOMIAL")
    support: set[int] = set()
    for left, right in zip(endpoints[::2], endpoints[1::2]):
        support.symmetric_difference_update(range(left, right))
    return tuple(sorted(support))


def _key(support: tuple[int, ...]) -> str:
    return "const" if not support else ",".join(map(str, support))


def _independent_walk_expansion(length: int) -> dict[str, Any]:
    raw: Counter[tuple[int, ...]] = Counter()

    def visit(depth: int, position: int, tau_support: set[int]) -> None:
        if depth == length:
            if position == 0:
                raw[_q_support(tau_support)] += 1
            return
        for step in STEPS:
            changed = position if step == 2 else position - 2 if step == -2 else None
            next_support = set(tau_support)
            if changed is not None:
                if changed in next_support:
                    next_support.remove(changed)
                else:
                    next_support.add(changed)
            visit(depth + 1, position + step, next_support)

    visit(0, 0, set())
    translated: Counter[tuple[int, ...]] = Counter()
    for support, coefficient in raw.items():
        if support:
            origin = min(support)
            support = tuple(index - origin for index in support)
        translated[support] += coefficient
    return {
        "closed_step_words": sum(raw.values()),
        "raw_monomial_count": len(raw),
        "translation_class_coefficients": {
            _key(support): coefficient for support, coefficient in sorted(translated.items())
        },
        "raw_coefficients": {
            _key(support): coefficient for support, coefficient in sorted(raw.items())
        },
    }


def _independent_checks() -> None:
    for p in range(1, 11):
        for prefix in itertools.product((-1, 1), repeat=p - 1):
            q = prefix + (math.prod(prefix),)
            _check(_moments(q) == _formula(q), "VERIFY_EXHAUSTIVE_FORMULA_FAIL")
    generator = random.Random(42143)
    for p in (13, 19, 33):
        for _ in range(40):
            prefix = tuple(generator.choice((-1, 1)) for _ in range(p - 1))
            q = prefix + (math.prod(prefix),)
            _check(_moments(q) == _formula(q), "VERIFY_RANDOM_FORMULA_FAIL")


def verify_general_period_data(result: dict[str, Any], source_sha256: str) -> None:
    _check(result.get("schema_version") == 1, "VERIFY_SCHEMA_FAIL")
    _check(
        result.get("status") == "GENERAL_PERIOD_CLOSED_WALK_OBSTRUCTIONS_PROVED",
        "VERIFY_STATUS_FAIL",
    )
    _check(
        result.get("component_statuses")
        == [
            "GENERAL_PERIOD_CLOSED_WALK_IDENTITIES_PROVED",
            "GENERAL_PERIOD_DEFECT_DENSITY_OBSTRUCTION_PROVED",
            "GENERAL_PERIOD_LOCAL_CLUSTER_OBSTRUCTION_PROVED",
        ],
        "VERIFY_COMPONENT_STATUS_FAIL",
    )
    _check(result.get("script_sha256") == source_sha256, "VERIFY_SOURCE_SHA_FAIL")

    setup = result.get("setup", {})
    _check(setup.get("period") == "arbitrary integer p>=1", "VERIFY_PERIOD_SCOPE_FAIL")
    _check(
        setup.get("legal_condition") == "product_(i=0)^(p-1) Q_i=1",
        "VERIFY_LEGAL_CONDITION_FAIL",
    )

    local = result.get("A2_local_formula", {})
    _check(local.get("status") == "GENERAL_FLUX_SQUARE_LOCAL_FORMULA_PROVED", "VERIFY_A2_STATUS_FAIL")
    _check(local.get("period_independent") is True, "VERIFY_A2_PERIOD_FAIL")
    _check(local.get("checked_tau_words") == 510, "VERIFY_A2_WORD_COUNT_FAIL")
    _check(local.get("checked_rows") == 3586, "VERIFY_A2_ROW_COUNT_FAIL")
    expected_coefficients = {
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
    _check(local.get("coefficients_by_displacement") == expected_coefficients, "VERIFY_A2_FORMULA_FAIL")

    identities = result.get("moment_identities", {})
    _check(
        identities.get("status") == "GENERAL_PERIOD_CLOSED_WALK_IDENTITIES_PROVED",
        "VERIFY_IDENTITY_STATUS_FAIL",
    )
    expansions = identities.get("expansions", [])
    _check([row.get("length") for row in expansions] == [2, 4, 6], "VERIFY_EXPANSION_LENGTHS_FAIL")
    for row in expansions:
        independent = _independent_walk_expansion(row["length"])
        for key, expected in independent.items():
            _check(row.get(key) == expected, f"VERIFY_EXPANSION_{key.upper()}_FAIL")
    _check(
        identities.get("defect_basis_identities")
        == {
            "M1": "4*p",
            "M2": "20*p+16*d",
            "M3": "118*p+168*d+96*a+48*b",
        },
        "VERIFY_DEFECT_FORMULAS_FAIL",
    )

    checks = result.get("machine_checks", {})
    _check(checks.get("exhaustive_period_range") == [1, 12], "VERIFY_SMALL_RANGE_FAIL")
    _check(checks.get("exhaustive_legal_q_count") == 4095, "VERIFY_SMALL_COUNT_FAIL")
    _check(checks.get("independent_laurent_ct_count") == 63, "VERIFY_LAURENT_COUNT_FAIL")
    _check(checks.get("random_check_count") == 320, "VERIFY_RANDOM_COUNT_FAIL")
    _check("no quadrature" in checks.get("arithmetic", ""), "VERIFY_EXACT_CT_FAIL")

    obstruction = result.get("obstructions", {})
    _check(obstruction.get("F1") == "16*d-12*p", "VERIFY_F1_FAIL")
    _check(obstruction.get("F2") == "-42*p+40*d+96*a+48*b", "VERIFY_F2_FAIL")
    _check(
        obstruction.get("density_necessary_condition") == "R(Q)<=8 implies d<=3*p/4",
        "VERIFY_DENSITY_DIRECTION_FAIL",
    )
    _check(
        obstruction.get("cluster_necessary_condition")
        == "R(Q)<=8 implies 40*d+96*a+48*b<=42*p",
        "VERIFY_CLUSTER_DIRECTION_FAIL",
    )
    limits = obstruction.get("logical_limits", {})
    _check(limits.get("conditions_are_sufficient_for_R_le_8") is False, "VERIFY_SUFFICIENCY_OVERCLAIM_FAIL")
    _check(limits.get("nonpositive_excess_proves_R_le_8") is False, "VERIFY_EXCESS_DIRECTION_FAIL")
    _check(limits.get("target_globally_optimal_among_all_periods") is False, "VERIFY_GLOBAL_OVERCLAIM_FAIL")

    scope = result.get("scope", {})
    expected_scope = {
        "arbitrary_period_necessary_conditions": "PROVED",
        "conditions_sufficient_for_sub_eight": "NOT_CLAIMED",
        "all_period_global_optimality": "NOT_CLAIMED",
        "finite_size_global_optimality": "NOT_CLAIMED",
        "all_signings_global_optimality": "NOT_CLAIMED",
        "M4_formula": "NOT_EXPLORED_IN_THEOREM_PACKAGE",
        "paper_manuscript_started": False,
    }
    _check(scope == expected_scope, "VERIFY_SCOPE_FAIL")
    _independent_checks()


def verify_files(
    result_path: Path = DEFAULT_RESULT, source_path: Path = DEFAULT_SOURCE
) -> None:
    verify_general_period_data(
        json.loads(result_path.read_text(encoding="utf-8")),
        _sha256(source_path.read_bytes()),
    )


def main() -> None:
    try:
        verify_files()
    except Exception as error:
        print(f"Target A general-period moment verification failed: {error}", file=sys.stderr)
        print("TARGET_A_GENERAL_PERIOD_MOMENTS_FAIL")
        raise SystemExit(1)
    print("TARGET_A_GENERAL_PERIOD_MOMENTS_PASS")


if __name__ == "__main__":
    main()
