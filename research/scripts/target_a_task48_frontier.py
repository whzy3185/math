"""Task 48 Phase I: close the exact moment/certificate frontier through p=24."""

from __future__ import annotations

import json
import platform
from pathlib import Path
from typing import Any

from target_a_high_period_exploration import q_word
from target_a_task47_common import (
    TARGET_Q,
    canonical_q,
    exact_endpoint_rayleigh,
    q_bits,
    repository_head,
    sha256,
    write_json,
)


RESEARCH = Path(__file__).resolve().parents[1]
REPO = RESEARCH.parent
MOMENTS = RESEARCH / "experiments" / "high_period_moments" / "summary.json"
TASK47 = RESEARCH / "experiments" / "high_period_certified" / "candidates.json"
OUTPUT = RESEARCH / "experiments" / "exact_frontier"


def _target_equivalent(q: tuple[int, ...]) -> bool:
    return len(q) % 8 == 0 and canonical_q(q) == canonical_q(TARGET_Q * (len(q) // 8))


def classify(row: dict[str, Any]) -> dict[str, Any]:
    q = q_word(row["canonical_q_code"], row["period"])
    if _target_equivalent(q):
        certificate = {
            "status": "CERTIFIED_R_EQ_ETA",
            "method": "period-8 target theorem plus exact repeated-cell zone folding",
            "R_squared": "4+sqrt(10+2*sqrt(5))",
        }
    else:
        certificate = exact_endpoint_rayleigh(q)
        if certificate is None:
            certificate = {
                "status": "UNRESOLVED",
                "method": "exact endpoint integer Rayleigh quotient did not cross 1561/200",
            }
    return {
        "period": row["period"],
        "canonical_q_code": row["canonical_q_code"],
        "q_bits": q_bits(q),
        "primitive_q_period": row["primitive_q_period"],
        "primitive_tau_period": row["primitive_tau_period"],
        "target_repetition": row["target_repetition"],
        "classification": certificate["status"],
        "certificate": certificate,
    }


def run() -> dict[str, Any]:
    source = json.loads(MOMENTS.read_text(encoding="utf-8"))
    prior = json.loads(TASK47.read_text(encoding="utf-8"))
    prior_keys = {
        (row["period"], row["canonical_q_code"])
        for row in prior["candidates"]
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    certificate_dir = OUTPUT / "certificates"
    certificate_dir.mkdir(exist_ok=True)
    period_payloads = []
    all_rows = []
    for period_row in source["results"]:
        classified = [classify(row) for row in period_row["residual_structures"]]
        for row in classified:
            row["task47_selected"] = (row["period"], row["canonical_q_code"]) in prior_keys
            path = certificate_dir / f"p{row['period']}_q{row['canonical_q_code']}.json"
            write_json(path, row)
            row["certificate_file"] = str(path.relative_to(REPO))
            row["certificate_sha256"] = sha256(path)
        counts = {
            status: sum(row["classification"] == status for row in classified)
            for status in ("CERTIFIED_R_GT_ETA", "CERTIFIED_R_EQ_ETA", "CERTIFIED_R_LT_ETA", "UNRESOLVED")
        }
        payload = {
            "schema_version": 1,
            "status": "COMPLETE_EXACT_CLOSURE" if counts["UNRESOLVED"] == 0 else "INCOMPLETE",
            "period": period_row["period"],
            "legal_dihedral_orbits": period_row["dihedral_orbits"],
            "represented_q_words": period_row["represented_q_words"],
            "moment_excluded_through_F16": period_row["dihedral_orbits"] - period_row["residual_count"],
            "F16_survivors": period_row["residual_count"],
            "classification_counts": counts,
            "primitive_survivors": sum(row["primitive_q_period"] == row["period"] for row in classified),
            "target_equalities": [row["canonical_q_code"] for row in classified if row["classification"] == "CERTIFIED_R_EQ_ETA"],
            "survivors": classified,
            "coverage_logic": "Every legal orbit is either excluded by the exact F_k>0 implication or appears in this exact survivor classification.",
        }
        write_json(OUTPUT / f"p{period_row['period']}_closure.json", payload)
        period_payloads.append(payload)
        all_rows.extend(classified)

    unresolved = [row for row in all_rows if row["classification"] == "UNRESOLVED"]
    remaining_task47 = [row for row in all_rows if not row["task47_selected"]]
    remaining_counts = {
        str(p): sum(row["period"] == p for row in remaining_task47)
        for p in (22, 23, 24)
    }
    summary = {
        "schema_version": 1,
        "status": "P24_EXACT_FRONTIER_CLOSED" if not unresolved else "INCOMPLETE",
        "scope": "EXACT FRONTIER CERTIFICATION; FORMAL THEOREM NOT MODIFIED",
        "periods": list(range(17, 25)),
        "total_legal_dihedral_orbits": sum(row["legal_dihedral_orbits"] for row in period_payloads),
        "total_moment_excluded": sum(row["moment_excluded_through_F16"] for row in period_payloads),
        "total_F16_survivors": len(all_rows),
        "certificate_resolved_GT": sum(row["classification"] == "CERTIFIED_R_GT_ETA" for row in all_rows),
        "equalities": [row for row in all_rows if row["classification"] == "CERTIFIED_R_EQ_ETA"],
        "unresolved_count": len(unresolved),
        "task47_selected_survivors": sum(row["task47_selected"] for row in all_rows),
        "task48_previously_unselected_counts": remaining_counts,
        "task48_previously_unselected_resolved": sum(row["classification"] != "UNRESOLVED" for row in remaining_task47),
        "theorem_candidate": "LOW_PERIOD_OPTIMALITY_P24_CANDIDATE" if not unresolved else None,
        "source_moment_sha256": sha256(MOMENTS),
        "source_task47_certificate_sha256": sha256(TASK47),
        "repository_head": repository_head(REPO),
        "software": {"python": platform.python_version()},
        "script_sha256": sha256(Path(__file__)),
    }
    write_json(OUTPUT / "summary.json", summary)
    with (OUTPUT / "closure_waterfall.csv").open("w", encoding="utf-8", newline="") as stream:
        stream.write("period,legal_orbits,moment_excluded,F16_survivors,certified_gt,equalities,unresolved\n")
        for row in period_payloads:
            counts = row["classification_counts"]
            stream.write(f"{row['period']},{row['legal_dihedral_orbits']},{row['moment_excluded_through_F16']},{row['F16_survivors']},{counts['CERTIFIED_R_GT_ETA']},{counts['CERTIFIED_R_EQ_ETA']},{counts['UNRESOLVED']}\n")
    return summary


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
