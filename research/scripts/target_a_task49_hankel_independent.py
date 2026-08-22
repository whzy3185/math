"""Independent exact principal-minor audit of the Task 48A Hankel pilot."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

from target_a_task47_common import write_json


RESEARCH = Path(__file__).resolve().parents[1]
SOURCE = RESEARCH / "experiments" / "task48a" / "moment_matrix" / "summary.json"
OUTPUT = RESEARCH / "reproducibility" / "task49" / "hankel_independent"


def first_negative_principal_minor(moments: list[int], depth: int) -> dict | None:
    matrix = sp.Matrix([
        [1561 * moments[i + j] - 200 * moments[i + j + 1] for j in range(depth + 1)]
        for i in range(depth + 1)
    ])
    for size in range(1, depth + 2):
        for indices in itertools.combinations(range(depth + 1), size):
            determinant = int(matrix.extract(indices, indices).det())
            if determinant < 0:
                return {"indices": list(indices), "determinant": str(determinant)}
    return None


def run() -> dict:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    rows = []
    for row in source["rows"]:
        moments = list(map(int, row["moments_M0_M20"]))
        first = None
        witness = None
        for depth in range(2, 6):
            witness = first_negative_principal_minor(moments, depth)
            if witness is not None:
                first = depth
                break
        rows.append({
            "period": row["period"],
            "canonical_q_code": row["canonical_q_code"],
            "target_repetition": row["target_repetition"],
            "first_exclusion_depth": first,
            "negative_principal_minor": witness,
        })
    cumulative = {str(depth): sum(row["first_exclusion_depth"] is not None and row["first_exclusion_depth"] <= depth for row in rows) for depth in range(2, 6)}
    survivors = [row for row in rows if row["first_exclusion_depth"] is None]
    representatives = []
    for period in range(17, 25):
        period_rows = [row for row in rows if row["period"] == period]
        representatives.extend(period_rows[:2])
    representatives.extend(sorted(rows, key=lambda row: row["first_exclusion_depth"] or 99, reverse=True)[:4])
    status = "HANKEL_AUDIT_PASS" if cumulative == {"2": 1, "3": 145, "4": 180, "5": 183} and len(survivors) == 1 and survivors[0]["target_repetition"] else "HANKEL_AUDIT_FAIL"
    payload = {
        "status": status,
        "method": "exact principal-minor search on 1561 H_m - 200 S_m; no floating generalized eigenvector or Task 48A witness reused",
        "inputs": len(rows),
        "independently_checked": len(rows),
        "cumulative_exact_exclusions": cumulative,
        "survivors": survivors,
        "target_survives": len(survivors) == 1 and survivors[0]["target_repetition"],
        "representative_second_checks": representatives,
        "rows": rows,
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "summary.json", payload)
    print(json.dumps({"status": status, "cumulative": cumulative, "target_survives": payload["target_survives"]}, indent=2))
    return payload


if __name__ == "__main__":
    run()
