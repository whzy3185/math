"""Task 48A Part E: a bounded exact Hankel/moment-matrix pilot."""

from __future__ import annotations

import csv
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from target_a_general_period_moments import closed_walk_moments
from target_a_high_period_exploration import q_word
from target_a_task47_common import TARGET_Q, sha256, write_json


RESEARCH = Path(__file__).resolve().parents[1]
SOURCE = RESEARCH / "experiments" / "high_period_moments" / "summary.json"
OUTPUT = RESEARCH / "experiments" / "task48a" / "moment_matrix"
ETA_UPPER = Fraction(1561, 200)


def hankel(moments: list[int], depth: int) -> tuple[list[list[int]], list[list[int]]]:
    h = [[moments[i + j] for j in range(depth + 1)] for i in range(depth + 1)]
    s = [[moments[i + j + 1] for j in range(depth + 1)] for i in range(depth + 1)]
    return h, s


def quadratic(matrix: list[list[int]], vector: list[Fraction]) -> Fraction:
    return sum(vector[i] * matrix[i][j] * vector[j] for i in range(len(vector)) for j in range(len(vector)))


def generalized_witness(moments: list[int], depth: int) -> dict[str, Any]:
    h, s = hankel(moments, depth)
    scale = np.asarray([8.0**i for i in range(depth + 1)])
    hf = np.asarray(h, dtype=float) / np.outer(scale, scale)
    sf = np.asarray(s, dtype=float) / np.outer(scale, scale)
    values, vectors = np.linalg.eig(np.linalg.solve(hf, sf))
    index = int(np.argmax(values.real))
    numerical = float(values[index].real)
    vector = vectors[:, index].real
    for integer_scale in (10**5, 10**7, 10**9, 10**11):
        integers = [int(round(value * integer_scale)) for value in vector]
        rational_vector = [Fraction(value, 8**i) for i, value in enumerate(integers)]
        denominator = quadratic(h, rational_vector)
        numerator = quadratic(s, rational_vector)
        ratio = numerator / denominator
        if ratio > ETA_UPPER:
            return {
                "excluded": True,
                "depth": depth,
                "numerical_generalized_bound": numerical,
                "integer_scaled_basis_witness": integers,
                "basis": "sum_i witness_i (x/8)^i",
                "exact_rayleigh_ratio": str(ratio),
                "comparison_rational": str(ETA_UPPER),
                "logic": "R >= moment generalized Rayleigh ratio > 1561/200 > eta",
            }
    return {
        "excluded": False,
        "depth": depth,
        "numerical_generalized_bound": numerical,
        "reason": "no tested rationalized generalized eigenvector crossed the exact eta upper comparison",
    }


def analyze(q: tuple[int, ...]) -> dict[str, Any]:
    moments = [len(q)] + closed_walk_moments(q, 20)
    first = None
    witnesses = []
    for depth in range(2, 6):
        witness = generalized_witness(moments, depth)
        witnesses.append(witness)
        if first is None and witness["excluded"]:
            first = depth
    return {"moments_M0_M20": [str(value) for value in moments], "first_exact_exclusion_depth": first, "witnesses": witnesses}


def run() -> dict[str, Any]:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    rows = []
    for period_result in source["results"]:
        for survivor in period_result["residual_structures"]:
            q = q_word(survivor["canonical_q_code"], survivor["period"])
            rows.append({
                "period": survivor["period"],
                "canonical_q_code": survivor["canonical_q_code"],
                "target_repetition": survivor["target_repetition"],
                **analyze(q),
            })
    if len(rows) != 184:
        raise AssertionError("moment pilot did not consume all 184 survivors")
    target_check = analyze(TARGET_Q)
    if target_check["first_exact_exclusion_depth"] is not None:
        raise AssertionError("Hankel support test incorrectly excludes the target")
    cumulative = {
        str(depth): sum(row["first_exact_exclusion_depth"] is not None and row["first_exact_exclusion_depth"] <= depth for row in rows)
        for depth in range(2, 6)
    }
    non_target = sum(not row["target_repetition"] for row in rows)
    exact_excluded = cumulative["5"]
    fraction = exact_excluded / non_target
    value = "HIGH" if fraction > 0.5 else "MODERATE" if fraction >= 0.1 else "LOW"
    summary = {
        "status": "TARGET_A_MOMENT_MATRIX_PILOT_COMPLETE",
        "input_F16_survivors": len(rows),
        "non_target_survivors": non_target,
        "moments": "M0 through M20, exact integers",
        "depths": [2, 3, 4, 5],
        "cumulative_exact_exclusions": cumulative,
        "exact_excluded_at_m5": exact_excluded,
        "remaining_at_m5": len(rows) - exact_excluded,
        "non_target_exclusion_fraction": fraction,
        "MOMENT_MATRIX_VALUE": value,
        "stop_rule_applied": value == "LOW",
        "target_PSD_direction_sanity": "PASS",
        "logical_direction": "If support were contained in [0,eta], eta H_m-S_m would be PSD; a rational generalized quotient above eta disproves that support bound.",
        "source_sha256": sha256(SOURCE),
        "rows": rows,
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "summary.json", summary)
    with (OUTPUT / "moment_matrix_results.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["period", "canonical_q_code", "target_repetition", "first_exact_exclusion_depth"], lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row[key] for key in writer.fieldnames})
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps({"cumulative": result["cumulative_exact_exclusions"], "value": result["MOMENT_MATRIX_VALUE"]}, indent=2))
