"""Task 47 Experiment C: adaptive exact high-period moment hierarchy."""

from __future__ import annotations

import argparse
import csv
import json
import math
import multiprocessing as mp
import platform
from collections import Counter
from pathlib import Path
from typing import Any

from target_a_general_period_moments import adjacency_transitions, tau_lift
from target_a_high_period_exploration import orbit_representatives, primitive_period, q_word, statistics
from target_a_task47_common import TARGET_Q, canonical_q, defect_gaps, q_bits, repository_head, sha256, write_json


RESEARCH = Path(__file__).resolve().parents[1]
REPO = RESEARCH.parent
DEFAULT_OUTPUT = RESEARCH / "experiments" / "high_period_moments"


def adaptive_first_positive(q: tuple[int, ...], maximum_k: int) -> dict[str, Any]:
    """Compute exact moments until the first positive F_k or the requested cap."""
    tau = tau_lift(q)
    p = len(q)
    states = [{start: 1} for start in range(p)]
    moments: list[int] = []
    excesses: list[int] = []
    first_positive = None
    for length in range(1, 2 * (maximum_k + 1) + 1):
        next_states: list[dict[int, int]] = []
        for state in states:
            updated: dict[int, int] = {}
            for position, amplitude in state.items():
                for endpoint, coefficient in adjacency_transitions(tau, position):
                    updated[endpoint] = updated.get(endpoint, 0) + amplitude * coefficient
            next_states.append(updated)
        states = next_states
        if length % 2:
            continue
        moment = sum(states[start].get(start, 0) for start in range(p))
        moments.append(moment)
        if len(moments) >= 2:
            k = len(moments) - 1
            excess = moments[-1] - 8 * moments[-2]
            excesses.append(excess)
            if excess > 0:
                first_positive = k
                break
    return {"moments": moments, "excesses": excesses, "first_positive_k": first_positive}


def _structural_row(code: int, q: tuple[int, ...], stats: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    gaps = defect_gaps(q)
    p = len(q)
    target_repetition = p % 8 == 0 and canonical_q(q) == canonical_q(TARGET_Q * (p // 8))
    return {
        "period": p,
        "canonical_q_code": code,
        "q_bits": q_bits(q),
        "d": stats["d"],
        "a": stats["a"],
        "b": stats["b"],
        "defect_gap_sequence": gaps,
        "minimum_defect_separation": min(gaps) if gaps else None,
        "maximum_defect_separation": max(gaps) if gaps else None,
        "defect_density": stats["d"] / p,
        "primitive_q_period": primitive_period(q),
        "primitive_tau_period": primitive_period(tau_lift(q)),
        "target_repetition": target_repetition,
        "two_defect": stats["d"] == 2,
        "near_antipodal": stats["d"] == 2 and abs(max(gaps) - p / 2) <= 1,
        "survived_through_k": len(profile["excesses"]),
        "moments": [str(value) for value in profile["moments"]],
        "excesses": [str(value) for value in profile["excesses"]],
    }


def analyze_period(arguments: tuple[int, int]) -> dict[str, Any]:
    p, maximum_k = arguments
    orbit_count = 0
    represented_words = 0
    first_positive: Counter[int] = Counter()
    survivors = []
    for code, orbit_size in orbit_representatives(p):
        orbit_count += 1
        represented_words += orbit_size
        q = q_word(code, p)
        stats = statistics(q)
        if stats["F1"] > 0:
            first_positive[1] += 1
            continue
        if stats["F2"] > 0:
            first_positive[2] += 1
            continue
        profile = adaptive_first_positive(q, maximum_k)
        if profile["first_positive_k"] is None:
            survivors.append(_structural_row(code, q, stats, profile))
        else:
            first_positive[profile["first_positive_k"]] += 1
    survival = {}
    excluded = 0
    for k in range(1, maximum_k + 1):
        excluded += first_positive[k]
        survival[k] = orbit_count - excluded
    return {
        "period": p,
        "dihedral_orbits": orbit_count,
        "represented_q_words": represented_words,
        "expected_q_words": 1 << (p - 1),
        "maximum_k": maximum_k,
        "first_positive_histogram": {str(k): first_positive[k] for k in range(1, maximum_k + 1)},
        "survival_curve": {str(k): survival[k] for k in range(1, maximum_k + 1)},
        "residual_count": len(survivors),
        "residual_structures": survivors,
        "checks": {
            "orbit_multiplicity_complete": represented_words == 1 << (p - 1),
            "partition_complete": sum(first_positive.values()) + len(survivors) == orbit_count,
            "survival_is_nonincreasing": all(survival[k] >= survival[k + 1] for k in range(1, maximum_k)),
        },
    }


def run(periods: list[int], maximum_k: int, jobs: int, output: Path) -> dict[str, Any]:
    arguments = [(period, maximum_k) for period in periods]
    if jobs == 1:
        results = [analyze_period(argument) for argument in arguments]
    else:
        with mp.get_context("spawn").Pool(min(jobs, len(arguments))) as pool:
            results = pool.map(analyze_period, arguments)
    results.sort(key=lambda row: row["period"])
    payload = {
        "schema_version": 1,
        "status": "TARGET_A_HIGH_PERIOD_MOMENT_HIERARCHY_COMPLETE",
        "scope": "EXACT_EXPERIMENTAL_NON_THEOREM",
        "periods": periods,
        "maximum_k": maximum_k,
        "method": "complete dihedral orbit stream plus adaptive exact integer closed-walk moments; stop at first F_k>0",
        "logical_boundary": "F_k>0 proves R(Q)>8; survival through k does not prove R(Q)<=8",
        "deterministic_ordering": "period, canonical Q integer",
        "random_seed": None,
        "software": {"python": platform.python_version()},
        "repository_head": repository_head(REPO),
        "script_sha256": sha256(Path(__file__)),
        "results": results,
        "checks": {"all_period_checks_pass": all(all(row["checks"].values()) for row in results)},
    }
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "summary.json", payload)
    with (output / "survival_curves.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["period", "k", "survivors"])
        for row in results:
            for k, count in row["survival_curve"].items():
                writer.writerow([row["period"], k, count])
    with (output / "first_positive_histogram.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["period", "k_first", "count"])
        for row in results:
            for k, count in row["first_positive_histogram"].items():
                writer.writerow([row["period"], k, count])
    fields = ["period", "canonical_q_code", "q_bits", "d", "a", "b", "defect_gap_sequence", "minimum_defect_separation", "maximum_defect_separation", "defect_density", "primitive_q_period", "primitive_tau_period", "target_repetition", "two_defect", "near_antipodal", "survived_through_k"]
    with (output / "residual_structures.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for result in results:
            for row in result["residual_structures"]:
                writer.writerow({key: row[key] for key in fields})
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--periods", type=int, nargs="+", default=list(range(17, 25)))
    parser.add_argument("--maximum-k", type=int, default=16)
    parser.add_argument("--jobs", type=int, default=8)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.periods, args.maximum_k, args.jobs, args.output)
    print(json.dumps({row["period"]: row["residual_count"] for row in result["results"]}, indent=2))


if __name__ == "__main__":
    main()
