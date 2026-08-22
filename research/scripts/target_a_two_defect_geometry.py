"""Task 47 Experiment A: general-period two-defect geometry."""

from __future__ import annotations

import argparse
import csv
import json
import math
import platform
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

from target_a_task47_common import (
    ETA,
    TARGET_Q,
    adaptive_radius_squared,
    canonical_q,
    defect_gaps,
    exact_endpoint_rayleigh,
    exact_moment_profile,
    primitive_period,
    q_bits,
    repository_head,
    sha256,
    tau_lift,
    write_json,
)


RESEARCH = Path(__file__).resolve().parents[1]
REPO = RESEARCH.parent
DEFAULT_OUTPUT = RESEARCH / "experiments" / "two_defect_geometry"


def two_defect_word(period: int, separation: int) -> tuple[int, ...]:
    if period < 2 or period % 2:
        raise ValueError("the two-positive-defect family is legal only at even period")
    if not 1 <= separation <= period // 2:
        raise ValueError("separation is outside the canonical reflection range")
    q = tuple(1 if index in (0, separation) else -1 for index in range(period))
    if math.prod(q) != 1:
        raise AssertionError("constructed Q word is illegal")
    return q


def analyze_case(period: int, separation: int, coarse_grid: int, moments: int) -> dict[str, Any]:
    q = two_defect_word(period, separation)
    tau = tau_lift(q)
    estimate = adaptive_radius_squared(q, coarse_grid)
    profile = exact_moment_profile(q, moments)
    repeated_target = (
        period == 8
        and primitive_period(tau) == 8
        and canonical_q(q) == canonical_q(TARGET_Q)
    )
    certificate: dict[str, Any] | None
    if repeated_target:
        certificate = {
            "status": "CERTIFIED_R_EQ_ETA",
            "method": "existing exact period-8 theorem plus zone folding",
            "R_squared": "4+sqrt(10+2*sqrt(5))",
        }
    else:
        certificate = exact_endpoint_rayleigh(q)
    return {
        "period": period,
        "separation": separation,
        "normalized_separation": separation / period,
        "q_bits": q_bits(q),
        "canonical_q_bits": q_bits(canonical_q(q)),
        "primitive_q_period": primitive_period(q),
        "primitive_tau_period": primitive_period(tau),
        "defect_gaps": defect_gaps(q),
        "repeated_target": repeated_target,
        "moments_M1_through_Mk_plus_1": profile["moments"],
        "excesses_F1_through_Fk": profile["excesses"],
        "first_positive_moment": profile["first_positive_k"],
        "spectral_estimate": estimate,
        "gap_from_eta_numerical": estimate["value"] - ETA,
        "gap_from_8_numerical": estimate["value"] - 8,
        "rigorous_certificate": certificate,
    }


def _monotonicity(rows: list[dict[str, Any]]) -> dict[str, Any]:
    ordered = sorted(rows, key=lambda row: row["separation"])
    violations = []
    for left, right in zip(ordered, ordered[1:]):
        if right["spectral_estimate"]["value"] > left["spectral_estimate"]["value"] + 1e-9:
            violations.append([left["separation"], right["separation"]])
    minimum = min(ordered, key=lambda row: row["spectral_estimate"]["value"])
    return {
        "minimum_separation": minimum["separation"],
        "maximal_separation": ordered[-1]["separation"],
        "maximal_separation_is_minimum": minimum["separation"] == ordered[-1]["separation"],
        "nonincreasing_with_separation": not violations,
        "adjacent_monotonicity_violations": violations,
    }


def run(min_period: int, max_period: int, coarse_grid: int, moments: int, output: Path) -> dict[str, Any]:
    periods = [period for period in range(min_period, max_period + 1) if period % 2 == 0]
    records = [
        analyze_case(period, separation, coarse_grid, moments)
        for period in periods
        for separation in range(1, period // 2 + 1)
    ]
    by_period = []
    for period in periods:
        rows = [row for row in records if row["period"] == period]
        by_period.append({"period": period, **_monotonicity(rows)})
    numerical_below_eta = [row for row in records if row["spectral_estimate"]["value"] < ETA - 1e-8]
    non8_below8 = [
        row for row in records
        if row["period"] != 8 and row["spectral_estimate"]["value"] < 8 - 1e-8
    ]
    certified_below_eta = [
        row for row in records
        if row["rigorous_certificate"]
        and row["rigorous_certificate"]["status"] == "CERTIFIED_R_LT_ETA"
    ]
    best = min(records, key=lambda row: row["spectral_estimate"]["value"])
    payload = {
        "schema_version": 1,
        "status": "TARGET_A_TWO_DEFECT_GEOMETRY_COMPLETE",
        "evidence_scope": "EXPERIMENTAL_NON_THEOREM",
        "period_range": [min(periods), max(periods)],
        "legal_periods": periods,
        "case_count": len(records),
        "eta": "4+sqrt(10+2*sqrt(5))",
        "eta_decimal": ETA,
        "method": {
            "family": "two Q_i=+1 defects at positions 0 and s; all remaining Q_i=-1",
            "canonical_separation": "1<=s<=floor(p/2), with s identified with p-s",
            "screening": "adaptive numerical Bloch maximization from a deterministic coarse grid",
            "rigorous_followup": "existing exact target theorem or exact endpoint integer-Rayleigh lower bound",
            "warning": "an adaptive floating maximum is not a certified continuous-fiber bound",
            "coarse_grid": coarse_grid,
            "exact_moment_depth": moments,
        },
        "software": {"python": platform.python_version(), "numpy": np.__version__, "sympy": sp.__version__},
        "repository_head": repository_head(REPO),
        "script_sha256": sha256(Path(__file__)),
        "records": records,
        "best_by_period": [
            min((row for row in records if row["period"] == period), key=lambda row: row["spectral_estimate"]["value"])
            for period in periods
        ],
        "period_monotonicity": by_period,
        "summary": {
            "numerical_candidates_below_eta": len(numerical_below_eta),
            "certified_candidates_below_eta": len(certified_below_eta),
            "period_not_equal_8_numerical_candidates_below_8": len(non8_below8),
            "periods_supporting_maximal_separation": sum(row["maximal_separation_is_minimum"] for row in by_period),
            "periods_with_full_monotonicity": sum(row["nonincreasing_with_separation"] for row in by_period),
            "global_numerical_minimum": {key: best[key] for key in ("period", "separation", "q_bits", "primitive_q_period", "primitive_tau_period", "repeated_target", "gap_from_eta_numerical")},
        },
    }
    output.mkdir(parents=True, exist_ok=True)
    write_json(output / "summary.json", payload)
    fields = ["period", "separation", "normalized_separation", "q_bits", "primitive_q_period", "primitive_tau_period", "repeated_target", "R_squared_estimate", "gap_from_eta", "gap_from_8", "certificate_status", "first_positive_moment"]
    with (output / "all_records.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in records:
            writer.writerow({
                "period": row["period"], "separation": row["separation"],
                "normalized_separation": row["normalized_separation"], "q_bits": row["q_bits"],
                "primitive_q_period": row["primitive_q_period"], "primitive_tau_period": row["primitive_tau_period"],
                "repeated_target": row["repeated_target"], "R_squared_estimate": row["spectral_estimate"]["value"],
                "gap_from_eta": row["gap_from_eta_numerical"], "gap_from_8": row["gap_from_8_numerical"],
                "certificate_status": row["rigorous_certificate"]["status"] if row["rigorous_certificate"] else "NUMERICAL_ONLY",
                "first_positive_moment": row["first_positive_moment"],
            })
    with (output / "best_by_period.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in payload["best_by_period"]:
            writer.writerow({
                "period": row["period"], "separation": row["separation"], "normalized_separation": row["normalized_separation"],
                "q_bits": row["q_bits"], "primitive_q_period": row["primitive_q_period"], "primitive_tau_period": row["primitive_tau_period"],
                "repeated_target": row["repeated_target"], "R_squared_estimate": row["spectral_estimate"]["value"],
                "gap_from_eta": row["gap_from_eta_numerical"], "gap_from_8": row["gap_from_8_numerical"],
                "certificate_status": row["rigorous_certificate"]["status"] if row["rigorous_certificate"] else "NUMERICAL_ONLY",
                "first_positive_moment": row["first_positive_moment"],
            })
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-period", type=int, default=8)
    parser.add_argument("--max-period", type=int, default=64)
    parser.add_argument("--coarse-grid", type=int, default=128)
    parser.add_argument("--moments", type=int, default=8)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = run(args.min_period, args.max_period, args.coarse_grid, args.moments, args.output)
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
