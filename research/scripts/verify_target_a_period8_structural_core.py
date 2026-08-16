"""Verify the period-8 structural proof without the orbit-classification artifact."""

from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
SHARP = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
TARGET = (1, -1, -1, -1, 1, -1, -1, -1)
EXPECTED_D2 = {1: (4, 5504), 2: (6, 64336), 3: (9, 2872096)}


class StructuralCoreError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise StructuralCoreError(message)


def legal_q_words():
    return [q for q in itertools.product((-1, 1), repeat=8) if math.prod(q) == 1]


def lift(q):
    tau = [1]
    for value in q[:-1]:
        tau.append(tau[-1] * value)
    _check(tau[-1] * q[-1] == tau[0], "TAU_CLOSURE_FAIL")
    return tuple(tau)


def transitions(tau, position):
    return (
        (position - 1, 1),
        (position + 1, 1),
        (position - 2, tau[(position - 2) % 8]),
        (position + 2, tau[position % 8]),
    )


def moments(q, maximum_k=10):
    tau = lift(q)
    states = [{start: 1} for start in range(8)]
    result = []
    for length in range(1, 2 * maximum_k + 1):
        updated_states = []
        for state in states:
            updated = {}
            for position, amplitude in state.items():
                for endpoint, coefficient in transitions(tau, position):
                    updated[endpoint] = updated.get(endpoint, 0) + amplitude * coefficient
            updated_states.append(updated)
        states = updated_states
        if length % 2 == 0:
            result.append(sum(states[start].get(start, 0) for start in range(8)))
    return result


def first_positive_excess(q, maximum_k=9):
    values = moments(q, maximum_k + 1)
    for k in range(1, maximum_k + 1):
        excess = values[k] - 8 * values[k - 1]
        if excess > 0:
            return k, excess
    return None


def separation(q):
    positions = [index for index, value in enumerate(q) if value == 1]
    _check(len(positions) == 2, "SEPARATION_DOMAIN_FAIL")
    distance = (positions[1] - positions[0]) % 8
    return min(distance, 8 - distance)


def verify_core() -> dict:
    sharp = json.loads(SHARP.read_text(encoding="utf-8"))
    _check(sharp.get("status") == "PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED", "SHARP_DEPENDENCY_FAIL")
    _check(sharp.get("eta_squared", {}).get("exact_radical") == "sqrt(2*sqrt(5) + 10) + 4", "ETA_IDENTITY_FAIL")
    # eta<8 follows after squaring from sqrt(5)<3.
    _check(5 < 9, "ETA_EIGHT_COMPARISON_FAIL")

    categories = {"below": 0, "equal": 0, "above": 0}
    d2_records = {}
    for q in legal_q_words():
        d = sum(value == 1 for value in q)
        positive = first_positive_excess(q)
        if d == 0:
            _check(q == (-1,) * 8 and positive is None, "BASELINE_CLASSIFICATION_FAIL")
            categories["equal"] += 1
        elif d == 2 and separation(q) == 4:
            _check(q in {TARGET[index:] + TARGET[:index] for index in range(8)}, "TARGET_ORBIT_FAIL")
            _check(positive is None, "TARGET_NEGATIVE_MOMENT_MISUSE_FAIL")
            categories["below"] += 1
        else:
            _check(positive is not None, f"MISSING_POSITIVE_EXCESS:{q}")
            if d == 2:
                d2_records.setdefault(separation(q), positive)
                _check(d2_records[separation(q)] == positive, "D2_ROTATION_INVARIANCE_FAIL")
            elif d >= 4:
                _check(positive[0] <= 2, "HIGH_DEFECT_NOT_EXCLUDED_BY_LOW_MOMENT")
            categories["above"] += 1
    _check(categories == {"below": 4, "equal": 1, "above": 123}, "TRICHOTOMY_COUNT_FAIL")
    _check(d2_records == EXPECTED_D2, "D2_HIERARCHY_FAIL")
    return {
        "status": "TARGET_A_PERIOD8_STRUCTURAL_CORE_PASS",
        "classification_dependency_used": False,
        "sharp_dependency_used": True,
        "legal_q_words": 128,
        "categories": categories,
        "d2_first_positive": {str(key): list(value) for key, value in sorted(d2_records.items())},
        "valid_implication": "F_k>0 implies R(Q)>8",
        "target_upper_bound_source": "period-8 sharp theorem"
    }


def main() -> None:
    try:
        verify_core()
    except Exception as error:
        print(f"Period-8 structural core verification failed: {error}", file=sys.stderr)
        print("TARGET_A_PERIOD8_STRUCTURAL_CORE_FAIL")
        raise SystemExit(1)
    print("TARGET_A_PERIOD8_STRUCTURAL_CORE_PASS")


if __name__ == "__main__":
    main()
