"""Independently verify the compressed low-period structural frontier."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_low_period_structural_frontier.json"
DEFAULT_FRONTIER = RESEARCH_ROOT / "proofs" / "target_a_low_period_spectral_frontier.json"
DEFAULT_SOURCE = RESEARCH_ROOT / "scripts" / "target_a_low_period_structural_frontier.py"
TASK42A_SOURCE = RESEARCH_ROOT / "scripts" / "target_a_general_period_moments.py"
EXPECTED_FRONTIER_SHA256 = "82e69ab7df7d81d6c2c46364a6e07aba7578fbc3ad21a69dcc17ffd08333928d"
EXPECTED_TASK42A_SHA256 = "04579c1d67c6af2da2a2629ba97352294864c19ae3a9b0ccc832111587731c6d"
EXPECTED_TARGET = ["P08-0006", "P16-0512"]
EXPECTED_BASELINE = ["P02-0001", "P04-0001", "P06-0001", "P08-0001", "P10-0001", "P12-0001", "P14-0001", "P16-0001"]
EXPECTED_EXCEPTIONS = ["P10-0006", "P12-0006", "P14-0006", "P14-0154", "P16-0006"]


class StructuralFrontierVerificationError(RuntimeError):
    pass


def _check(condition: bool, message: str) -> None:
    if not condition:
        raise StructuralFrontierVerificationError(message)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _tau(q: tuple[int, ...]) -> tuple[int, ...]:
    _check(math.prod(q) == 1, "VERIFY_ILLEGAL_Q")
    values = [1]
    for sign in q[:-1]:
        values.append(values[-1] * sign)
    return tuple(values)


def _transitions(tau: tuple[int, ...], position: int) -> tuple[tuple[int, int], ...]:
    p = len(tau)
    return (
        (position - 1, 1),
        (position + 1, 1),
        (position - 2, tau[(position - 2) % p]),
        (position + 2, tau[position % p]),
    )


def _moments(q: tuple[int, ...], maximum_k: int) -> list[int]:
    tau = _tau(q)
    states = [{start: 1} for start in range(len(q))]
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
            result.append(sum(states[start].get(start, 0) for start in range(len(q))))
    return result


def _adaptive_first(q: tuple[int, ...]) -> tuple[int, int] | None:
    moments = _moments(q, 25)
    for index in range(1, 25):
        value = moments[index] - 8 * moments[index - 1]
        if value > 0:
            return index, value
    moments = _moments(q, 65)
    for index in range(25, 65):
        value = moments[index] - 8 * moments[index - 1]
        if value > 0:
            return index, value
    return None


def _endpoint_matrix(tau: tuple[int, ...], z_value: int) -> list[list[int]]:
    p = len(tau)
    matrix = [[0 for _ in range(p)] for _ in range(p)]
    for output in range(p):
        for displacement, coefficient in (
            (-1, 1),
            (1, 1),
            (-2, tau[(output - 2) % p]),
            (2, tau[output]),
        ):
            source = output + displacement
            cell, residue = divmod(source, p)
            phase = 1 if z_value == 1 or cell % 2 == 0 else -1
            matrix[output][residue] += coefficient * phase
    return matrix


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


def _verify_rayleigh(q: tuple[int, ...], certificate: dict[str, Any]) -> None:
    matrix = _endpoint_matrix(_tau(q), certificate["z"])
    vector = certificate["vector"]
    image = [sum(value * vector[column] for column, value in enumerate(row)) for row in matrix]
    numerator = sum(value * value for value in image)
    denominator = sum(value * value for value in vector)
    _check((numerator, denominator) == (certificate["numerator"], certificate["denominator"]), "VERIFY_EXCEPTION_RAYLEIGH_FAIL")
    valid, comparison = _rational_gt_eta(numerator, denominator)
    _check(valid and comparison == certificate["eta_comparison"], "VERIFY_EXCEPTION_ETA_FAIL")


def verify_structural_frontier_data(
    result: dict[str, Any], frontier: dict[str, Any], source_sha256: str
) -> None:
    _check(result.get("schema_version") == 1, "VERIFY_SCHEMA_FAIL")
    _check(result.get("status") == "LOW_PERIOD_STRUCTURAL_FRONTIER_PROVED", "VERIFY_STATUS_FAIL")
    _check(result.get("script_sha256") == source_sha256, "VERIFY_SOURCE_SHA_FAIL")
    dependencies = result.get("dependencies", {})
    _check(dependencies.get("Task42B_frontier", {}).get("sha256") == EXPECTED_FRONTIER_SHA256, "VERIFY_FRONTIER_DEPENDENCY_FAIL")
    _check(dependencies.get("Task42A_moments", {}).get("sha256") == EXPECTED_TASK42A_SHA256, "VERIFY_MOMENT_DEPENDENCY_FAIL")
    hierarchy = result.get("moment_hierarchy", {})
    _check(hierarchy.get("valid_logic") == "F_k>0 implies R(Q)>8", "VERIFY_MOMENT_LOGIC_FAIL")
    _check(hierarchy.get("negative_excess_used_as_upper_bound") is False, "VERIFY_NEGATIVE_EXCESS_OVERCLAIM_FAIL")
    _check(hierarchy.get("primary_range") == [1, 24], "VERIFY_PRIMARY_RANGE_FAIL")
    _check(hierarchy.get("adaptive_residual_range") == [25, 64], "VERIFY_ADAPTIVE_RANGE_FAIL")
    expected_scope = {
        "structural_compression_of_period_le_16_frontier": "PROVED",
        "negative_moment_excess_proves_upper_bound": False,
        "exact_upper_bound_for_four_separation4_exceptions": "NOT_CLAIMED",
        "exact_R_equals_8_for_p14_exception": "NOT_CLAIMED",
        "period_17_or_larger": "NOT_CLAIMED",
        "all_period_global_optimality": "NOT_CLAIMED",
        "paper_manuscript_started": False,
    }
    _check(result.get("scope") == expected_scope, "VERIFY_SCOPE_FAIL")

    stored_rows = {row["orbit_id"]: row for row in hierarchy.get("rows", [])}
    _check(len(stored_rows) == hierarchy.get("detected_orbits") == 2611, "VERIFY_DETECTED_COUNT_FAIL")
    distribution: dict[str, int] = {}
    residual = []
    frontier_by_id = {}
    for row in frontier.get("orbits", []):
        frontier_by_id[row["orbit_id"]] = row
        q = tuple(row["canonical_q_signs"])
        first = _adaptive_first(q)
        if first is None:
            residual.append(row)
            _check(row["orbit_id"] not in stored_rows, "VERIFY_RESIDUAL_STORED_AS_DETECTED")
            continue
        index, value = first
        distribution[str(index)] = distribution.get(str(index), 0) + 1
        stored = stored_rows.get(row["orbit_id"])
        _check(stored is not None, "VERIFY_DETECTED_ROW_MISSING")
        _check(stored["first_positive_F_index"] == index, "VERIFY_FIRST_INDEX_FAIL")
        _check(stored["first_positive_F_value"] == value and value > 0, "VERIFY_FIRST_VALUE_FAIL")
        _check(stored["conclusion"] == "R(Q)>8>eta", "VERIFY_DETECTED_CONCLUSION_FAIL")
    _check(distribution == hierarchy.get("first_positive_index_distribution"), "VERIFY_DISTRIBUTION_FAIL")
    _check(len(residual) == 15, "VERIFY_RESIDUAL_COUNT_FAIL")

    target = sorted(row["orbit_id"] for row in residual if row["target_infinite_phase"])
    baseline = sorted(row["orbit_id"] for row in residual if all(value == -1 for value in row["canonical_q_signs"]))
    exceptions = sorted(row["orbit_id"] for row in residual if row["orbit_id"] not in set(target).union(baseline))
    _check(target == EXPECTED_TARGET, "VERIFY_TARGET_RESIDUAL_FAIL")
    _check(baseline == EXPECTED_BASELINE, "VERIFY_BASELINE_RESIDUAL_FAIL")
    _check(exceptions == EXPECTED_EXCEPTIONS, "VERIFY_EXCEPTION_RESIDUAL_FAIL")

    partition = result.get("residual_partition", {})
    _check(partition.get("count") == 15, "VERIFY_PARTITION_COUNT_FAIL")
    base_data = partition.get("all_negative_representations", {})
    _check(base_data.get("orbit_ids") == EXPECTED_BASELINE, "VERIFY_BASELINE_IDS_FAIL")
    _check(base_data.get("infinite_phase_count") == 1 and base_data.get("primitive_tau_period") == 2, "VERIFY_BASELINE_PRIMITIVE_FAIL")
    _check(base_data.get("exact_R_squared") == "8" and base_data.get("comparison") == "8>eta", "VERIFY_BASELINE_SPECTRAL_FAIL")
    target_data = partition.get("target_representations", {})
    _check(target_data.get("orbit_ids") == EXPECTED_TARGET and target_data.get("exact_R_squared") == frontier["eta"], "VERIFY_TARGET_PARTITION_FAIL")
    exception_data = partition.get("exceptional_competitors", [])
    _check([row["orbit_id"] for row in exception_data] == EXPECTED_EXCEPTIONS, "VERIFY_EXCEPTION_IDS_FAIL")
    for item in exception_data:
        frontier_row = frontier_by_id[item["orbit_id"]]
        _check(item["canonical_q_bits"] == frontier_row["canonical_q_bits"], "VERIFY_EXCEPTION_Q_FAIL")
        _check(item["exact_certificate"] == frontier_row["exact_certificate"], "VERIFY_EXCEPTION_CERTIFICATE_LINK_FAIL")
        _verify_rayleigh(tuple(frontier_row["canonical_q_signs"]), item["exact_certificate"])

    compression = result.get("compression_summary", {})
    expected_compression = {
        "total_orbits": 2626,
        "target_representations": 2,
        "competitor_representations": 2624,
        "competitors_proved_above_8_by_one_moment_lemma": 2611,
        "all_negative_representations_proved_equal_8_by_one_baseline_lemma": 8,
        "residual_endpoint_certificates": 5,
        "uncertified": 0,
        "Task42B_endpoint_certificates_replaced_by_moment_hierarchy": 832,
    }
    _check(compression == expected_compression, "VERIFY_COMPRESSION_SUMMARY_FAIL")


def verify_files(
    result_path: Path = DEFAULT_RESULT,
    frontier_path: Path = DEFAULT_FRONTIER,
    source_path: Path = DEFAULT_SOURCE,
) -> None:
    frontier_raw = frontier_path.read_bytes()
    _check(_sha256(frontier_raw) == EXPECTED_FRONTIER_SHA256, "VERIFY_FRONTIER_FILE_SHA_FAIL")
    _check(_sha256(TASK42A_SOURCE.read_bytes()) == EXPECTED_TASK42A_SHA256, "VERIFY_TASK42A_FILE_SHA_FAIL")
    verify_structural_frontier_data(
        json.loads(result_path.read_text(encoding="utf-8")),
        json.loads(frontier_raw),
        _sha256(source_path.read_bytes()),
    )


def main() -> None:
    try:
        verify_files()
    except Exception as error:
        print(f"Target A low-period structural verification failed: {error}", file=sys.stderr)
        print("TARGET_A_LOW_PERIOD_STRUCTURAL_FRONTIER_FAIL")
        raise SystemExit(1)
    print("TARGET_A_LOW_PERIOD_STRUCTURAL_FRONTIER_PASS")


if __name__ == "__main__":
    main()
