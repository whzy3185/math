"""Assemble bounded residue-class and finite-size evidence for Task 51."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from target_a_task47_common import write_json
from target_a_task51_interfaces import cluster_record


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "experiments" / "task51"
C6 = 7.905369311620327
ETA_TEXT = "4+sqrt(10+2*sqrt(5))"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []

    g6 = load_csv(RESEARCH / "experiments" / "task48a" / "interface" / "g6_spectrum.csv")
    for target in (130, 258, 514, 1026):
        source = min(g6, key=lambda row: abs(int(row["n"]) - target))
        value = float(source["rho_squared"])
        rows.append({
            "residue_mod_8": 2,
            "n": int(source["n"]),
            "family": "single +2 / G6",
            "rho_squared": value,
            "difference_from_c6": value - C6,
            "status": "BELOW_DOUBLE_RESOLUTION" if abs(value - C6) < 1e-12 else "FP64_STRUCTURED_EVIDENCE",
        })

    residue4 = load_csv(RESEARCH / "experiments" / "task48a" / "residue12" / "family_comparison.csv")
    two_g6 = [row for row in residue4 if row["family"] == "R2_TWO_GAP6"]
    for target in (124, 252, 508):
        same_n = [row for row in two_g6 if int(row["n"]) == target]
        if not same_n:
            same_n = sorted(two_g6, key=lambda row: abs(int(row["n"]) - target))[:20]
        source = min(same_n, key=lambda row: float(row["rho_squared"]))
        value = float(source["rho_squared"])
        rows.append({
            "residue_mod_8": 4,
            "n": int(source["n"]),
            "family": "two separated +2 / two G6",
            "rho_squared": value,
            "difference_from_c6": value - C6,
            "status": "BELOW_DOUBLE_RESOLUTION" if abs(value - C6) < 1e-12 else "FP64_STRUCTURED_EVIDENCE",
        })

    for defect_count in (32, 64):
        source = cluster_record([6, 6, 6], defect_count)
        value = float(source["rho_squared"])
        rows.append({
            "residue_mod_8": 6,
            "n": int(source["n"]),
            "family": "three separated +2 / three G6",
            "rho_squared": value,
            "difference_from_c6": value - C6,
            "status": "BELOW_DOUBLE_RESOLUTION" if abs(value - C6) < 1e-12 else "FP64_STRUCTURED_EVIDENCE",
        })
    insurance = json.loads((RESEARCH / "experiments" / "task49" / "insurance" / "charge_landscape.json").read_text())
    source = next(row for row in insurance["cases"] if row["configuration"] == "E6_THREE_PLUS2")
    value = float(source["rho_squared"])
    rows.append({
        "residue_mod_8": 6,
        "n": int(source["n"]),
        "family": "three separated +2 / three G6",
        "rho_squared": value,
        "difference_from_c6": value - C6,
        "status": "FP64_STRUCTURED_EVIDENCE",
    })

    with (OUTPUT / "asymptotic_mn_candidates.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "status": "COMMON_NONZERO_RESIDUE_LIMIT_STRONGLY_SUPPORTED_NOT_PROVED",
        "candidate_limits": {
            "residue_0": ETA_TEXT,
            "residue_2": "c6",
            "residue_4": "c6",
            "residue_6": "c6",
        },
        "c6": C6,
        "evidence_rows": len(rows),
        "largest_late_difference_by_residue": {
            str(residue): max(abs(row["difference_from_c6"]) for row in rows if row["residue_mod_8"] == residue and row["n"] >= 250)
            for residue in (2, 4, 6)
        },
        "leading_corrections": {
            "status": "OPEN",
            "reason": "Several competitive rows are at or below double resolution; Task 51 does not extend n or infer coefficients from unresolved FP64 corrections.",
            "expected_scale": "slow G6 Floquet multiplier raised to the shortest interface separation",
            "mod16": "geometry/holonomy-dependent prefactors remain unresolved",
        },
        "lower_bound_requirements": [
            "arbitrary-period crystallization or an equivalent global compactness theorem",
            "fixed-r multi-slip lower bounds and complete upper-gap eigenvalue counting",
            "uniform control of mixed and negative charge decompositions",
        ],
        "claim_boundary": "These are explicit-family upper bounds and convergence signals, not residue-class global minimality or a theorem about m_n.",
    }
    write_json(OUTPUT / "asymptotic_mn_summary.json", summary)
    print(json.dumps({"status": summary["status"], "rows": len(rows)}, indent=2))
    return summary


if __name__ == "__main__":
    run()
