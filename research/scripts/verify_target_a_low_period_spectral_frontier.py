"""Independently verify the Target A low-period spectral frontier."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

import sympy as sp


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_low_period_spectral_frontier.json"
DEFAULT_SOURCE = RESEARCH_ROOT / "scripts" / "target_a_low_period_spectral_frontier.py"
DEFAULT_SHARP = RESEARCH_ROOT / "proofs" / "target_a_period8_sharp_constant.json"
EXPECTED_SHARP_SHA256 = "f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63"
EXPECTED_COUNTS = [1, 2, 2, 4, 4, 8, 9, 18, 23, 44, 63, 122, 190, 362, 612, 1162]


class LowPeriodVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise LowPeriodVerificationError(message)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _bits(signs: Iterable[int]) -> str:
    return "".join("1" if value == 1 else "0" for value in signs)


def _rotate(signs: tuple[int, ...], amount: int) -> tuple[int, ...]:
    amount %= len(signs)
    return signs[amount:] + signs[:amount]


def _images(signs: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {
        _rotate(base, amount)
        for base in (signs, tuple(reversed(signs)))
        for amount in range(len(signs))
    }


def _canonical(signs: tuple[int, ...]) -> tuple[int, ...]:
    return min(_images(signs), key=_bits)


def _tau(q: tuple[int, ...]) -> tuple[int, ...]:
    _check(q and math.prod(q) == 1, "VERIFY_ILLEGAL_Q")
    values = [1]
    for sign in q[:-1]:
        values.append(values[-1] * sign)
    _check(values[-1] * q[-1] == 1, "VERIFY_TAU_CLOSURE_FAIL")
    return tuple(values)


def _q_from_tau(tau: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(tau[index] * tau[(index + 1) % len(tau)] for index in range(len(tau)))


def _primitive(signs: tuple[int, ...]) -> int:
    return next(
        period
        for period in range(1, len(signs) + 1)
        if len(signs) % period == 0
        and all(signs[index] == signs[index % period] for index in range(len(signs)))
    )


def _independent_orbit_count(p: int) -> int:
    representatives = set()
    for prefix in itertools.product((-1, 1), repeat=p - 1):
        q = prefix + (math.prod(prefix),)
        representatives.add(_canonical(q))
    return len(representatives)


def _cycles(p: int, reflection: bool, parameter: int) -> list[int]:
    image = (
        (lambda index: (parameter - index) % p)
        if reflection
        else (lambda index: (index + parameter) % p)
    )
    unseen = set(range(p))
    lengths = []
    while unseen:
        index = min(unseen)
        length = 0
        while index in unseen:
            unseen.remove(index)
            length += 1
            index = image(index)
        lengths.append(length)
    return lengths


def _independent_burnside_count(p: int) -> int:
    total = 0
    for reflection in (False, True):
        for parameter in range(p):
            lengths = _cycles(p, reflection, parameter)
            total += 2 ** (len(lengths) - 1) if any(length % 2 for length in lengths) else 2 ** len(lengths)
    _check(total % (2 * p) == 0, "VERIFY_BURNSIDE_NONINTEGRAL")
    return total // (2 * p)


def _laurent(tau: tuple[int, ...]) -> list[list[dict[int, int]]]:
    p = len(tau)
    result = [[{} for _ in range(p)] for _ in range(p)]
    for output in range(p):
        for displacement, coefficient in (
            (-1, 1),
            (1, 1),
            (-2, tau[(output - 2) % p]),
            (2, tau[output]),
        ):
            source = output + displacement
            cell, residue = divmod(source, p)
            result[output][residue][cell] = result[output][residue].get(cell, 0) + coefficient
    return result


def _verify_bloch(tau: tuple[int, ...]) -> None:
    p = len(tau)
    matrix = _laurent(tau)
    negative = _laurent(tuple(-value for value in tau))
    diagonal = [(-1) ** index for index in range(p)]
    phase_sign = -1 if p % 2 else 1
    for row in range(p):
        for column in range(p):
            _check(
                matrix[row][column]
                == {-power: coefficient for power, coefficient in matrix[column][row].items()},
                "VERIFY_BLOCH_TRANSPOSE_FAIL",
            )
            expected_negative = {
                power: -diagonal[row] * diagonal[column] * phase_sign**power * coefficient
                for power, coefficient in matrix[row][column].items()
            }
            _check(negative[row][column] == expected_negative, "VERIFY_TAU_NEGATION_FAIL")


def _endpoint_matrix(tau: tuple[int, ...], z_value: int) -> list[list[int]]:
    return [
        [
            sum(
                coefficient * (1 if z_value == 1 or power % 2 == 0 else -1)
                for power, coefficient in entry.items()
            )
            for entry in row
        ]
        for row in _laurent(tau)
    ]


def _matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(value * vector[column] for column, value in enumerate(row)) for row in matrix]


def _rational_gt_eta(numerator: int, denominator: int) -> tuple[bool, dict[str, int]]:
    value = Fraction(numerator, denominator)
    if value <= 4:
        return False, {}
    u = ((value - 4) ** 2 - 10) / 2
    difference = u * u - 5
    return u > 0 and difference > 0, {
        "u_numerator": u.numerator,
        "u_denominator": u.denominator,
        "u_squared_minus_5_numerator": difference.numerator,
        "u_squared_minus_5_denominator": difference.denominator,
    }


def _verify_geometric_images(q: tuple[int, ...], tau: tuple[int, ...]) -> None:
    p = len(q)
    tau_images = set()
    for amount in range(p):
        for image in (
            tuple(tau[(index + amount) % p] for index in range(p)),
            tuple(tau[(-index + amount) % p] for index in range(p)),
        ):
            tau_images.add(image)
            tau_images.add(tuple(-value for value in image))
    _check({_q_from_tau(image) for image in tau_images} == _images(q), "VERIFY_GEOMETRIC_IMAGES_FAIL")


def _verify_sturm(item: dict[str, Any], row: dict[str, Any]) -> None:
    tau = tuple(row["tau_lift"])
    matrix = sp.Matrix(_endpoint_matrix(tau, item["z"]))
    variable = sp.Symbol("y")
    polynomial = (matrix * matrix).charpoly(variable).as_poly()
    _check([int(value) for value in polynomial.all_coeffs()] == item["squared_charpoly_coefficients"], "VERIFY_STURM_POLY_FAIL")
    lower_text, upper_text = item["largest_root_isolating_interval"]
    lower = sp.Rational(lower_text)
    upper = sp.Rational(upper_text)
    intervals = polynomial.intervals(eps=sp.Rational(1, 10**10))
    _check(intervals[-1][0] == (lower, upper), "VERIFY_STURM_INTERVAL_FAIL")
    _check(intervals[-1][1] == item["largest_root_multiplicity"], "VERIFY_STURM_MULTIPLICITY_FAIL")
    valid, comparison = _rational_gt_eta(int(lower.p), int(lower.q))
    _check(valid and comparison == item["lower_endpoint_eta_comparison"], "VERIFY_STURM_ETA_FAIL")


def verify_low_period_data(
    result: dict[str, Any], sharp_sha256: str, source_sha256: str
) -> None:
    _check(result.get("schema_version") == 1, "VERIFY_SCHEMA_FAIL")
    _check(result.get("status") == "PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED", "VERIFY_STATUS_FAIL")
    _check(
        result.get("component_statuses")
        == [
            "LOW_PERIOD_PHASE_SPACE_COMPLETE",
            "LOW_PERIOD_SPECTRAL_FRONTIER_TABLE_PROVED",
            "PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED",
        ],
        "VERIFY_COMPONENT_STATUS_FAIL",
    )
    _check(sharp_sha256 == EXPECTED_SHARP_SHA256, "VERIFY_SHARP_FILE_SHA_FAIL")
    _check(result.get("dependencies", {}).get("Task40A_sharp", {}).get("sha256") == sharp_sha256, "VERIFY_SHARP_DEPENDENCY_FAIL")
    _check(result.get("script_sha256") == source_sha256, "VERIFY_SOURCE_SHA_FAIL")

    phase = result.get("phase_space", {})
    _check(phase.get("period_range") == [1, 16], "VERIFY_PERIOD_RANGE_FAIL")
    _check(phase.get("route_a_orbit_counts") == EXPECTED_COUNTS, "VERIFY_ROUTE_A_COUNTS_FAIL")
    _check(phase.get("expected_diagnostics") == EXPECTED_COUNTS, "VERIFY_DIAGNOSTICS_FAIL")
    _check(phase.get("total_orbit_count") == 2626, "VERIFY_TOTAL_COUNT_FAIL")
    _check(phase.get("route_mismatch_count") == 0, "VERIFY_ROUTE_MISMATCH_FAIL")
    independent_a = [_independent_orbit_count(p) for p in range(1, 17)]
    independent_b = [_independent_burnside_count(p) for p in range(1, 17)]
    _check(independent_a == independent_b == EXPECTED_COUNTS, "VERIFY_INDEPENDENT_ORBIT_COUNTS_FAIL")
    for p, burnside in enumerate(phase.get("route_b", []), start=1):
        _check(burnside.get("orbit_count") == EXPECTED_COUNTS[p - 1], "VERIFY_STORED_BURNSIDE_FAIL")

    rows = result.get("orbits", [])
    _check(len(rows) == 2626, "VERIFY_ORBIT_TABLE_LENGTH_FAIL")
    _check(len({row.get("orbit_id") for row in rows}) == 2626, "VERIFY_DUPLICATE_ORBIT_ID_FAIL")
    expected_representatives = {
        p: sorted(
            {
                _canonical(prefix + (math.prod(prefix),))
                for prefix in itertools.product((-1, 1), repeat=p - 1)
            },
            key=_bits,
        )
        for p in range(1, 17)
    }
    actual_representatives = {p: [] for p in range(1, 17)}
    for row in rows:
        actual_representatives[row["p"]].append(tuple(row["canonical_q_signs"]))
    for p in range(1, 17):
        actual_representatives[p].sort(key=_bits)
        _check(actual_representatives[p] == expected_representatives[p], f"VERIFY_CANONICAL_ORBIT_SET_FAIL:{p}")
        expected_ids = [f"P{p:02d}-{index:04d}" for index in range(1, len(expected_representatives[p]) + 1)]
        actual_ids = [row["orbit_id"] for row in rows if row["p"] == p]
        _check(actual_ids == expected_ids, f"VERIFY_DETERMINISTIC_ORBIT_IDS_FAIL:{p}")
    distribution = {"moment": 0, "ternary": 0, "integer": 0, "target": 0}
    by_period = {p: [] for p in range(1, 17)}
    rows_by_id = {}
    for row in rows:
        p = row["p"]
        q = tuple(row["canonical_q_signs"])
        tau = tuple(row["tau_lift"])
        _check(len(q) == p and math.prod(q) == 1, "VERIFY_ROW_Q_FAIL")
        _check(_canonical(q) == q and _bits(q) == row["canonical_q_bits"], "VERIFY_ROW_CANONICAL_FAIL")
        _check(len(_images(q)) == row["dihedral_orbit_size"], "VERIFY_ROW_ORBIT_SIZE_FAIL")
        _check(_tau(q) == tau, "VERIFY_ROW_TAU_FAIL")
        _check(_primitive(q) == row["primitive_q_period"], "VERIFY_PRIMITIVE_Q_FAIL")
        _check(_primitive(tau) == row["primitive_tau_period"], "VERIFY_PRIMITIVE_TAU_FAIL")
        primitive_q = _canonical(q[: row["primitive_q_period"]])
        _check(_bits(primitive_q) == row["primitive_q_canonical_bits"], "VERIFY_PRIMITIVE_KEY_FAIL")
        _check(row["cell_repetition"] == (row["primitive_tau_period"] < p), "VERIFY_REPETITION_FLAG_FAIL")
        _verify_bloch(tau)
        _verify_geometric_images(q, tau)

        certificate = row["exact_certificate"]
        kind = certificate["type"]
        if row["target_infinite_phase"]:
            _check(kind == "TASK40A_TARGET_EXACT_SHARP_CONSTANT", "VERIFY_TARGET_CERTIFICATE_FAIL")
            _check(row["primitive_tau_period"] == 8 and primitive_q == (-1, -1, -1, 1), "VERIFY_TARGET_IDENTITY_FAIL")
            distribution["target"] += 1
        elif kind == "TASK42A_MOMENT_EXCESS":
            d = sum(value == 1 for value in q)
            a = sum(q[index] == q[(index + 1) % p] == 1 for index in range(p))
            b = sum(q[index] == q[(index + 2) % p] == 1 for index in range(p))
            expected = 16 * d - 12 * p if certificate["excess"] == "F1" else -42 * p + 40 * d + 96 * a + 48 * b
            _check(expected == certificate["value"] and expected > 0, "VERIFY_MOMENT_CERTIFICATE_FAIL")
            distribution["moment"] += 1
        else:
            _check(kind == "EXACT_ENDPOINT_INTEGER_RAYLEIGH", "VERIFY_CERTIFICATE_TYPE_FAIL")
            vector = certificate["vector"]
            matrix = _endpoint_matrix(tau, certificate["z"])
            image = _matrix_vector(matrix, vector)
            numerator = sum(value * value for value in image)
            denominator = sum(value * value for value in vector)
            _check((numerator, denominator) == (certificate["numerator"], certificate["denominator"]), "VERIFY_RAYLEIGH_ARITHMETIC_FAIL")
            valid, comparison = _rational_gt_eta(numerator, denominator)
            _check(valid and comparison == certificate["eta_comparison"], "VERIFY_RAYLEIGH_ETA_FAIL")
            alphabet = "TERNARY" if max(map(abs, vector)) <= 1 else "SMALL_INTEGER"
            _check(certificate["vector_alphabet"] == alphabet, "VERIFY_VECTOR_ALPHABET_FAIL")
            distribution["ternary" if alphabet == "TERNARY" else "integer"] += 1
        _check(certificate["conclusion"] in {"R(Q)>eta", "R(Q)=eta"}, "VERIFY_CONCLUSION_FAIL")
        by_period[p].append(row)
        rows_by_id[row["orbit_id"]] = row

    _check(distribution == {"moment": 1787, "ternary": 824, "integer": 13, "target": 2}, "VERIFY_CERTIFICATE_DISTRIBUTION_FAIL")
    summary = result.get("certificate_summary", {})
    _check(summary.get("competitor_orbits") == 2624 and summary.get("uncertified") == 0, "VERIFY_CERTIFICATE_SUMMARY_FAIL")
    _check(summary.get("Task42A_moment_excess") == 1787, "VERIFY_MOMENT_SUMMARY_FAIL")
    _check(summary.get("endpoint_ternary_rayleigh") == 824, "VERIFY_TERNARY_SUMMARY_FAIL")
    _check(summary.get("endpoint_small_integer_rayleigh") == 13, "VERIFY_INTEGER_SUMMARY_FAIL")

    target = result.get("target_repetition", {})
    _check(target.get("representations") == ["P08-0006", "P16-0512"], "VERIFY_TARGET_REPRESENTATIONS_FAIL")
    _check(target.get("periods") == [8, 16] and target.get("counted_as_distinct_minimizers") is False, "VERIFY_TARGET_REPETITION_FAIL")
    table = result.get("frontier_table", [])
    _check(len(table) == 16, "VERIFY_FRONTIER_TABLE_LENGTH_FAIL")
    for p, entry in enumerate(table, start=1):
        _check(entry["p"] == p and entry["legal_q_count"] == 2 ** (p - 1), "VERIFY_FRONTIER_ROW_FAIL")
        _check(entry["dihedral_orbit_count"] == len(by_period[p]) == EXPECTED_COUNTS[p - 1], "VERIFY_FRONTIER_ORBITS_FAIL")
        exact_primitive = sum(row["primitive_tau_period"] == p for row in by_period[p])
        _check(entry["primitive_tau_period_p_orbits"] == exact_primitive, "VERIFY_FRONTIER_PRIMITIVE_COUNT_FAIL")
        expected_relation = "PROVED_EQUAL_TARGET_REPETITION" if p in (8, 16) else "PROVED_STRICTLY_ABOVE_FOR_EVERY_ORBIT"
        _check(entry["frontier_relation_to_eta"] == expected_relation, "VERIFY_FRONTIER_RELATION_FAIL")

    sturm = result.get("sturm_crosschecks", [])
    _check(len(sturm) == 24, "VERIFY_STURM_COUNT_FAIL")
    for item in sturm:
        _verify_sturm(item, rows_by_id[item["orbit_id"]])
    sturm_ids = {item["orbit_id"] for item in sturm}
    for item in result.get("near_threshold_classes", []):
        _check(item["orbit_id"] in sturm_ids and item["sturm_crosschecked"] is True, "VERIFY_NEAR_THRESHOLD_CROSSCHECK_FAIL")

    bloch = result.get("bloch_construction", {})
    _check(bloch.get("checked_orbits") == 2626, "VERIFY_BLOCH_CHECK_COUNT_FAIL")
    _check(bloch.get("odd_period_phase_shift_recorded") is True, "VERIFY_ODD_PERIOD_SHIFT_FAIL")
    _check(bloch.get("translation_reflection_tau_lift_images_verified_for_all_orbits") is True, "VERIFY_GEOMETRIC_STATUS_FAIL")
    scope = result.get("scope", {})
    expected_scope = {
        "primitive_tau_period_at_most_16": "PROVED_UNIQUE_TARGET_OPTIMUM",
        "period_17_or_larger": "NOT_CLAIMED",
        "all_period_global_optimality": "NOT_CLAIMED",
        "finite_size_global_optimality": "NOT_CLAIMED",
        "all_signings_global_optimality": "NOT_CLAIMED",
        "numeric_previews_used_as_proof": False,
        "paper_manuscript_started": False,
    }
    _check(scope == expected_scope, "VERIFY_SCOPE_FAIL")


def verify_files(
    result_path: Path = DEFAULT_RESULT,
    sharp_path: Path = DEFAULT_SHARP,
    source_path: Path = DEFAULT_SOURCE,
) -> None:
    verify_low_period_data(
        json.loads(result_path.read_text(encoding="utf-8")),
        _sha256(sharp_path.read_bytes()),
        _sha256(source_path.read_bytes()),
    )


def main() -> None:
    try:
        verify_files()
    except Exception as error:
        print(f"Target A low-period frontier verification failed: {error}", file=sys.stderr)
        print("TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER_FAIL")
        raise SystemExit(1)
    print("TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER_PASS")


if __name__ == "__main__":
    main()
