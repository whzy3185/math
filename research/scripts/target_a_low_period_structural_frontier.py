"""Compress the exact low-period frontier into moments and five residuals."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

from target_a_general_period_moments import closed_walk_moments


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FRONTIER = RESEARCH_ROOT / "proofs" / "target_a_low_period_spectral_frontier.json"
DEFAULT_RESULT = RESEARCH_ROOT / "proofs" / "target_a_low_period_structural_frontier.json"
TASK42A_SOURCE = RESEARCH_ROOT / "scripts" / "target_a_general_period_moments.py"
EXPECTED_FRONTIER_SHA256 = "82e69ab7df7d81d6c2c46364a6e07aba7578fbc3ad21a69dcc17ffd08333928d"
EXPECTED_TASK42A_SOURCE_SHA256 = "04579c1d67c6af2da2a2629ba97352294864c19ae3a9b0ccc832111587731c6d"
PRIMARY_MAX_F = 24
RESIDUAL_MAX_F = 64
EXPECTED_TARGET_IDS = ["P08-0006", "P16-0512"]
EXPECTED_BASELINE_IDS = [
    "P02-0001",
    "P04-0001",
    "P06-0001",
    "P08-0001",
    "P10-0001",
    "P12-0001",
    "P14-0001",
    "P16-0001",
]
EXPECTED_EXCEPTION_IDS = [
    "P10-0006",
    "P12-0006",
    "P14-0006",
    "P14-0154",
    "P16-0006",
]


class LowPeriodStructuralError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise LowPeriodStructuralError(message)


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def adaptive_first_positive(q: tuple[int, ...]) -> tuple[int, int] | None:
    moments = closed_walk_moments(q, PRIMARY_MAX_F + 1)
    for index in range(1, PRIMARY_MAX_F + 1):
        excess = moments[index] - 8 * moments[index - 1]
        if excess > 0:
            return index, excess
    moments = closed_walk_moments(q, RESIDUAL_MAX_F + 1)
    for index in range(PRIMARY_MAX_F + 1, RESIDUAL_MAX_F + 1):
        excess = moments[index] - 8 * moments[index - 1]
        if excess > 0:
            return index, excess
    return None


def load_frontier(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    _require(_sha256_bytes(raw) == EXPECTED_FRONTIER_SHA256, "TASK42B_FRONTIER_SHA_MISMATCH")
    payload = json.loads(raw)
    _require(payload.get("status") == "PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED", "TASK42B_FRONTIER_STATUS_MISMATCH")
    _require(_sha256_file(TASK42A_SOURCE) == EXPECTED_TASK42A_SOURCE_SHA256, "TASK42A_SOURCE_SHA_MISMATCH")
    return payload


def run_structural_frontier(
    frontier_path: Path = DEFAULT_FRONTIER, result_path: Path = DEFAULT_RESULT
) -> dict[str, Any]:
    frontier = load_frontier(frontier_path)
    detected = []
    residual = []
    distribution: dict[str, int] = {}
    for row in frontier["orbits"]:
        q = tuple(row["canonical_q_signs"])
        first = adaptive_first_positive(q)
        if first is None:
            residual.append(row)
            continue
        index, value = first
        distribution[str(index)] = distribution.get(str(index), 0) + 1
        detected.append(
            {
                "orbit_id": row["orbit_id"],
                "p": row["p"],
                "canonical_q_bits": row["canonical_q_bits"],
                "first_positive_F_index": index,
                "first_positive_F_value": value,
                "conclusion": "R(Q)>8>eta",
            }
        )

    _require(len(detected) == 2611 and len(residual) == 15, "STRUCTURAL_RESIDUAL_COUNT_MISMATCH")
    target = sorted(row["orbit_id"] for row in residual if row["target_infinite_phase"])
    baseline = sorted(
        row["orbit_id"]
        for row in residual
        if all(value == -1 for value in row["canonical_q_signs"])
    )
    exceptions = sorted(
        row["orbit_id"]
        for row in residual
        if row["orbit_id"] not in set(target).union(baseline)
    )
    _require(target == EXPECTED_TARGET_IDS, "STRUCTURAL_TARGET_RESIDUAL_MISMATCH")
    _require(baseline == EXPECTED_BASELINE_IDS, "STRUCTURAL_BASELINE_RESIDUAL_MISMATCH")
    _require(exceptions == EXPECTED_EXCEPTION_IDS, "STRUCTURAL_EXCEPTION_RESIDUAL_MISMATCH")

    exception_rows = []
    for row in residual:
        if row["orbit_id"] not in exceptions:
            continue
        certificate = row["exact_certificate"]
        _require(certificate["type"] == "EXACT_ENDPOINT_INTEGER_RAYLEIGH", "STRUCTURAL_EXCEPTION_CERTIFICATE_TYPE_MISMATCH")
        exception_rows.append(
            {
                "orbit_id": row["orbit_id"],
                "p": row["p"],
                "canonical_q_bits": row["canonical_q_bits"],
                "defect_statistics": row["defect_statistics"],
                "primitive_tau_period": row["primitive_tau_period"],
                "numeric_R_squared_preview": row["numeric_preview"]["R_squared_preview"],
                "exact_certificate": certificate,
                "conclusion": "R(Q)>eta",
            }
        )
    exception_rows.sort(key=lambda row: row["orbit_id"])

    result = {
        "schema_version": 1,
        "status": "LOW_PERIOD_STRUCTURAL_FRONTIER_PROVED",
        "theorem": (
            "For the complete p<=16 legal-Q orbit space, a uniform closed-walk hierarchy "
            "through F_64 proves R>8 for 2611 classes. The 15 residual representations are "
            "eight copies of the all-negative cancellation phase, two copies of the Target A "
            "phase, and five explicitly certified competitors."
        ),
        "dependencies": {
            "Task42B_frontier": {"path": "research/proofs/target_a_low_period_spectral_frontier.json", "sha256": EXPECTED_FRONTIER_SHA256},
            "Task42A_moments": {"path": "research/scripts/target_a_general_period_moments.py", "sha256": EXPECTED_TASK42A_SOURCE_SHA256},
        },
        "moment_hierarchy": {
            "definition": "F_k(Q)=M_(k+1)(Q)-8*M_k(Q)",
            "valid_logic": "F_k>0 implies R(Q)>8",
            "negative_excess_used_as_upper_bound": False,
            "primary_range": [1, PRIMARY_MAX_F],
            "adaptive_residual_range": [PRIMARY_MAX_F + 1, RESIDUAL_MAX_F],
            "detected_orbits": len(detected),
            "first_positive_index_distribution": distribution,
            "rows": detected,
        },
        "residual_partition": {
            "count": len(residual),
            "all_negative_representations": {
                "orbit_ids": baseline,
                "representation_count": len(baseline),
                "infinite_phase_count": 1,
                "primitive_tau_period": 2,
                "exact_identity": "A^2=4I+S^2+S^-2+S^4+S^-4",
                "exact_R_squared": "8",
                "comparison": "8>eta",
            },
            "target_representations": {
                "orbit_ids": target,
                "representation_count": len(target),
                "infinite_phase_count": 1,
                "primitive_tau_period": 8,
                "exact_R_squared": frontier["eta"],
                "comparison": "R=eta",
            },
            "exceptional_competitors": exception_rows,
            "exceptional_competitor_count": len(exception_rows),
        },
        "compression_summary": {
            "total_orbits": 2626,
            "target_representations": 2,
            "competitor_representations": 2624,
            "competitors_proved_above_8_by_one_moment_lemma": 2611,
            "all_negative_representations_proved_equal_8_by_one_baseline_lemma": 8,
            "residual_endpoint_certificates": 5,
            "uncertified": 0,
            "Task42B_endpoint_certificates_replaced_by_moment_hierarchy": 832,
        },
        "scope": {
            "structural_compression_of_period_le_16_frontier": "PROVED",
            "negative_moment_excess_proves_upper_bound": False,
            "exact_upper_bound_for_four_separation4_exceptions": "NOT_CLAIMED",
            "exact_R_equals_8_for_p14_exception": "NOT_CLAIMED",
            "period_17_or_larger": "NOT_CLAIMED",
            "all_period_global_optimality": "NOT_CLAIMED",
            "paper_manuscript_started": False,
        },
        "checker": {
            "path": "research/scripts/verify_target_a_low_period_structural_frontier.py",
            "expected_status": "TARGET_A_LOW_PERIOD_STRUCTURAL_FRONTIER_PASS",
        },
        "script_sha256": _sha256_file(Path(__file__).resolve()),
        "next_gate": "synchronize Task 41 novelty audit with N10 and N11",
    }
    _write_json(result_path, result)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frontier", type=Path, default=DEFAULT_FRONTIER)
    parser.add_argument("--output", type=Path, default=DEFAULT_RESULT)
    args = parser.parse_args()
    try:
        result = run_structural_frontier(args.frontier, args.output)
    except Exception as error:
        print(f"Target A low-period structural frontier failed: {error}", file=sys.stderr)
        print("TARGET_A_LOW_PERIOD_STRUCTURAL_FRONTIER_FAIL")
        raise SystemExit(1)
    print(result["status"])


if __name__ == "__main__":
    main()
