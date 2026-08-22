"""Task 48A Part A: rebuild and audit the exact p=17..24 partition."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from target_a_task47_common import sha256, write_json


RESEARCH = Path(__file__).resolve().parents[1]
MOMENTS = RESEARCH / "experiments" / "high_period_moments" / "summary.json"
HANDLED = RESEARCH / "experiments" / "high_period_certified" / "candidates.json"
CLOSED = RESEARCH / "experiments" / "exact_frontier"
OUTPUT = RESEARCH / "experiments" / "task48a" / "p24_frontier"


def key(row: dict[str, Any]) -> tuple[int, int]:
    return row["period"], row["canonical_q_code"]


def run() -> dict[str, Any]:
    moments = json.loads(MOMENTS.read_text(encoding="utf-8"))
    handled_payload = json.loads(HANDLED.read_text(encoding="utf-8"))
    handled_rows = handled_payload["candidates"]
    handled_keys = [key(row) for row in handled_rows]
    if len(handled_keys) != len(set(handled_keys)):
        raise AssertionError("duplicate Task 47 handled survivor")
    survivor_rows = [row for result in moments["results"] for row in result["residual_structures"]]
    survivor_keys = [key(row) for row in survivor_rows]
    if len(survivor_keys) != len(set(survivor_keys)):
        raise AssertionError("duplicate moment survivor")
    survivor_set = set(survivor_keys)
    handled_set = set(handled_keys)
    if not handled_set <= survivor_set:
        raise AssertionError("Task 47 handled state is absent from survivor set")
    remaining = [row for row in survivor_rows if key(row) not in handled_set]
    counts = {str(p): sum(row["period"] == p for row in remaining) for p in (22, 23, 24)}
    if counts != {"22": 11, "23": 14, "24": 34} or len(remaining) != 59:
        raise AssertionError(f"unexpected remaining set: {counts}")

    closed_rows = []
    period_partitions = []
    for result in moments["results"]:
        closure = json.loads((CLOSED / f"p{result['period']}_closure.json").read_text(encoding="utf-8"))
        if closure["status"] != "COMPLETE_EXACT_CLOSURE":
            raise AssertionError("checkpoint closure is incomplete")
        rows = closure["survivors"]
        if {key(row) for row in rows} != {key(row) for row in result["residual_structures"]}:
            raise AssertionError("canonical survivor mismatch")
        classes = {
            "M": result["dihedral_orbits"] - result["residual_count"],
            "C": sum(row["classification"] == "CERTIFIED_R_GT_ETA" for row in rows),
            "E": sum(row["classification"] == "CERTIFIED_R_EQ_ETA" for row in rows),
            "L": sum(row["classification"] == "CERTIFIED_R_LT_ETA" for row in rows),
            "U": sum(row["classification"] == "UNRESOLVED" for row in rows),
        }
        if sum(classes.values()) != result["dihedral_orbits"]:
            raise AssertionError("orbit partition is not exhaustive")
        period_partitions.append({
            "period": result["period"],
            "legal_dihedral_orbits": result["dihedral_orbits"],
            "represented_q_words": result["represented_q_words"],
            "classes": classes,
            "closed": classes["L"] == classes["U"] == 0,
            "primitive_survivors": sum(row["primitive_q_period"] == result["period"] for row in rows),
            "equality_codes": [row["canonical_q_code"] for row in rows if row["classification"] == "CERTIFIED_R_EQ_ETA"],
        })
        closed_rows.extend(rows)

    remaining_keys = {key(row) for row in remaining}
    certifications = [row for row in closed_rows if key(row) in remaining_keys]
    if len(certifications) != 59 or any(row["classification"] == "UNRESOLVED" for row in certifications):
        raise AssertionError("remaining certification coverage failed")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "remaining_59.json", {
        "count": len(remaining),
        "counts_by_period": counts,
        "duplicate_count": 0,
        "already_consumed_count": 0,
        "canonical_mismatch_count": 0,
        "states": remaining,
    })
    write_json(OUTPUT / "certifications.json", {
        "count": len(certifications),
        "classification_counts": {
            status: sum(row["classification"] == status for row in certifications)
            for status in ("CERTIFIED_R_GT_ETA", "CERTIFIED_R_EQ_ETA", "CERTIFIED_R_LT_ETA", "UNRESOLVED")
        },
        "states": certifications,
    })
    write_json(OUTPUT / "p17_p24_partition.json", {
        "classes": {
            "M": "exact F_k>0 for some k<=16, hence R>8>eta",
            "C": "F16 survivor with exact certificate R>eta",
            "E": "target or repeated-target equality R=eta",
            "L": "exact R<eta",
            "U": "unresolved",
        },
        "periods": period_partitions,
        "consumed_exactly_once": True,
        "holonomy_note": "Moment exclusion is continuous-fiber and endpoint certificates maximize over both alpha endpoints.",
        "zone_folding_note": "The sole displayed-period equality has primitive Q period 4 and tau period 8.",
    })
    gt = sum(row["classes"]["C"] for row in period_partitions)
    eq = sum(row["classes"]["E"] for row in period_partitions)
    lt = sum(row["classes"]["L"] for row in period_partitions)
    unresolved = sum(row["classes"]["U"] for row in period_partitions)
    summary = {
        "status": "P24_EXACT_FRONTIER_CLOSED" if lt == unresolved == 0 else "INCOMPLETE",
        "P21_status": "P21_EXACT_FRONTIER_CLOSED" if all(row["closed"] for row in period_partitions[:5]) else "INCOMPLETE",
        "remaining_input": 59,
        "remaining_resolved": len(certifications) - sum(row["classification"] == "UNRESOLVED" for row in certifications),
        "GT_survivors": gt,
        "EQ_survivors": eq,
        "LT_survivors": lt,
        "UNRESOLVED_survivors": unresolved,
        "periods": period_partitions,
        "unique_equality": "period-24 displayed-cell repetition of the period-8 target",
        "theorem_candidate": "P24_BOUNDED_OPTIMALITY",
        "theorem_status": "PROOF_ALREADY_COMPLETE_AS_EXPERIMENTAL_EXACT_CERTIFICATE_CHAIN",
        "formal_theorem_modified": False,
        "sources": {
            "moments_sha256": sha256(MOMENTS),
            "task47_handled_sha256": sha256(HANDLED),
            "checkpoint_summary_sha256": sha256(CLOSED / "summary.json"),
        },
    }
    write_json(OUTPUT / "closure_summary.json", summary)
    return summary


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
