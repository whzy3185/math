"""Task 47 Experiment D: exact checks for dangerous high-period candidates."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

import numpy as np

from target_a_high_period_exploration import q_word
from target_a_task47_common import (
    ETA,
    TARGET_Q,
    canonical_q,
    exact_endpoint_rayleigh,
    grid_radius_squared,
    q_bits,
    repository_head,
    sha256,
    write_json,
)


RESEARCH = Path(__file__).resolve().parents[1]
REPO = RESEARCH.parent
DEFAULT_MOMENTS = RESEARCH / "experiments" / "high_period_moments" / "summary.json"
DEFAULT_OUTPUT = RESEARCH / "experiments" / "high_period_certified"


def classify_candidate(row: dict[str, Any], numerical_grid: int) -> dict[str, Any]:
    p = row["period"]
    q = q_word(row["canonical_q_code"], p)
    numerical = grid_radius_squared(q, numerical_grid)
    target = p % 8 == 0 and canonical_q(q) == canonical_q(TARGET_Q * (p // 8))
    if target:
        certificate = {
            "status": "CERTIFIED_R_EQ_ETA",
            "method": "existing period-8 exact theorem and zone folding",
            "R_squared": "4+sqrt(10+2*sqrt(5))",
        }
    else:
        certificate = exact_endpoint_rayleigh(q)
        if certificate is None:
            certificate = {
                "status": "UNRESOLVED",
                "method": "endpoint exact Rayleigh attempt did not cross 1561/200",
                "warning": "the numerical grid is not a continuous-fiber certificate",
            }
    return {
        **row,
        "q_bits": q_bits(q),
        "numerical_screen": numerical,
        "numerical_gap_from_eta": numerical["value"] - ETA,
        "classification": certificate["status"],
        "certificate": certificate,
    }


def run(moment_path: Path, output: Path, per_period: int, selection_grid: int, certification_grid: int) -> dict[str, Any]:
    moments = json.loads(moment_path.read_text(encoding="utf-8"))
    selected = []
    selection_records = []
    for period_result in moments["results"]:
        ranked = []
        for row in period_result["residual_structures"]:
            q = q_word(row["canonical_q_code"], row["period"])
            preview = grid_radius_squared(q, selection_grid)
            rank = (
                preview["value"],
                row["defect_density"],
                -(row["maximum_defect_separation"] or 0),
                -row["primitive_tau_period"],
                row["canonical_q_code"],
            )
            ranked.append((rank, row, preview))
        ranked.sort(key=lambda item: item[0])
        chosen = ranked[:per_period]
        selection_records.append(
            {
                "period": period_result["period"],
                "residual_pool": len(ranked),
                "selected": len(chosen),
                "rule": "lowest grid R, then low defect density, largest separation, largest primitive tau period, canonical code",
            }
        )
        for _rank, row, preview in chosen:
            selected.append({**row, "selection_grid_screen": preview})

    certified = [classify_candidate(row, certification_grid) for row in selected]
    output.mkdir(parents=True, exist_ok=True)
    certificate_dir = output / "certificates"
    certificate_dir.mkdir(parents=True, exist_ok=True)
    for row in certified:
        path = certificate_dir / f"p{row['period']}_q{row['canonical_q_code']}.json"
        write_json(path, row)
        row["certificate_file"] = str(path.relative_to(REPO))
        row["certificate_file_sha256"] = sha256(path)
    counts = {status: sum(row["classification"] == status for row in certified) for status in ("CERTIFIED_R_GT_ETA", "CERTIFIED_R_EQ_ETA", "CERTIFIED_R_LT_ETA", "UNRESOLVED", "NUMERICAL_ONLY")}
    payload = {
        "schema_version": 1,
        "status": "TARGET_A_HIGH_PERIOD_CANDIDATE_CHECKS_COMPLETE",
        "scope": "RIGOROUS_LOWER_COMPARISON_WHERE_CERTIFIED; NO_GLOBAL_CLASSIFICATION",
        "source_moment_file": str(moment_path.relative_to(REPO)),
        "source_moment_sha256": sha256(moment_path),
        "selection_rule": "complete F1..F16 survivor pool; rank by stated deterministic tuple; at most 20 per period",
        "selection_grid": selection_grid,
        "certification_diagnostic_grid": certification_grid,
        "selection_records": selection_records,
        "classification_counts": counts,
        "candidates": certified,
        "software": {"python": platform.python_version(), "numpy": np.__version__},
        "repository_head": repository_head(REPO),
        "script_sha256": sha256(Path(__file__)),
        "logical_boundary": "CERTIFIED_R_GT_ETA is a rigorous lower comparison; numerical grids never certify the continuous supremum",
    }
    write_json(output / "candidates.json", payload)
    unresolved = [row for row in certified if row["classification"] in ("UNRESOLVED", "NUMERICAL_ONLY")]
    write_json(output / "unresolved.json", unresolved)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--moments", type=Path, default=DEFAULT_MOMENTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--per-period", type=int, default=20)
    parser.add_argument("--selection-grid", type=int, default=128)
    parser.add_argument("--certification-grid", type=int, default=2048)
    args = parser.parse_args()
    payload = run(args.moments, args.output, args.per_period, args.selection_grid, args.certification_grid)
    print(json.dumps(payload["classification_counts"], indent=2))


if __name__ == "__main__":
    main()
