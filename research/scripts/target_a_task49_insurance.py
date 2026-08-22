"""Bounded Task 49 insurance experiments for likely reviewer questions."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

import numpy as np

from target_a_general_period_moments import closed_walk_moments
from target_a_task47_common import write_json
from target_a_task48a_common import dense_spectrum, q_from_gaps, single_slip_gaps, two_slip_gaps
from target_a_task49_hankel_independent import first_negative_principal_minor


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "experiments" / "task49" / "insurance"


def spread_gaps(special: list[int], defect_count: int) -> list[int]:
    remaining = defect_count - len(special)
    buckets = [remaining // len(special)] * len(special)
    for index in range(remaining % len(special)):
        buckets[index] += 1
    gaps = []
    for value, count in zip(special, buckets):
        gaps.append(value)
        gaps.extend([4] * count)
    return gaps


def min_rho(gaps: list[int]) -> dict[str, Any]:
    q = q_from_gaps(sum(gaps), gaps)
    rows = []
    for alpha in (-1, 1):
        values, _vectors = dense_spectrum(q, alpha)
        rows.append({"alpha": alpha, "rho_squared": float(max(abs(values[0]), abs(values[-1])) ** 2)})
    return min(rows, key=lambda row: row["rho_squared"])


def charge_landscape() -> dict[str, Any]:
    cases = []
    specifications = [
        ("E2_SINGLE_PLUS2", 506, [6]),
        ("E4_SINGLE_PLUS4", 508, [8]),
        ("E4_TWO_PLUS2", 508, [6, 6]),
        ("E4_PLUS6_MINUS2", 508, [10, 2]),
        ("E4_PLUS3_PLUS1", 508, [7, 5]),
        ("E6_SINGLE_PLUS6", 510, [10]),
        ("E6_PLUS4_PLUS2", 510, [8, 6]),
        ("E6_THREE_PLUS2", 510, [6, 6, 6]),
    ]
    for name, n, special in specifications:
        defect_count = (n - sum(value - 4 for value in special)) // 4
        gaps = spread_gaps(special, defect_count)
        result = min_rho(gaps)
        cases.append({"configuration": name, "n": n, "charges": [value - 4 for value in special], "special_gaps": special, "gap_count": len(gaps), **result, "status": "NUMERICAL_LARGE_SEPARATION_EVIDENCE"})
    by_excess = {}
    for total in (2, 4, 6):
        rows = [row for row in cases if sum(row["charges"]) == total]
        by_excess[str(total)] = min(rows, key=lambda row: row["rho_squared"])["configuration"]
    return {"status": "USEFUL", "best_by_total_excess": by_excess, "cases": cases, "no_selection_theorem_claimed": True}


def four_step_stability() -> dict[str, Any]:
    n = 128
    base = [4] * 32
    patterns = {
        "BULK_4_4": base,
        "3_5": [3, 5] + base[2:],
        "2_6": [2, 6] + base[2:],
        "3_4_5": [3, 4, 5] + base[3:],
        "2_5_5": [2, 5, 5] + base[3:],
    }
    rows = []
    for name, gaps in patterns.items():
        rows.append({"pattern": name, **min_rho(gaps), "gap_sequence": gaps, "status": "NUMERICAL_LOCAL_PERTURBATION_EVIDENCE"})
    bulk = next(row for row in rows if row["pattern"] == "BULK_4_4")["rho_squared"]
    for row in rows:
        row["penalty_from_bulk"] = row["rho_squared"] - bulk
    stable = all(row["penalty_from_bulk"] > 0 for row in rows if row["pattern"] != "BULK_4_4")
    return {"classification": "LOCALLY_STABLE_SIGNAL" if stable else "MIXED", "rows": rows}


def legalize(bits: list[int]) -> tuple[int, ...]:
    n = len(bits)
    if sum(bits) % 2 != n % 2:
        bits[-1] ^= 1
    return tuple(bits)


def stress_candidates(period: int) -> list[tuple[str, tuple[int, ...]]]:
    target = [1, 0, 0, 0, 1, 0, 0, 0]
    rng = random.Random(49000 + period)
    candidates = [
        ("TARGET_TRUNCATION", legalize([target[i % 8] for i in range(period)])),
        ("LOW_DEFECT", legalize([1 if i in (0, period // 2) else 0 for i in range(period)])),
        ("GAP4_LIKE", legalize([1 if i % 4 == 0 else 0 for i in range(period)])),
        ("LONG_PRIMITIVE", legalize([1 if i in (0, 4, 9, 15, period - 3) else 0 for i in range(period)])),
        ("SEEDED_CONTROL", legalize([rng.randrange(2) for _ in range(period)])),
    ]
    return candidates


def hankel_stress() -> dict[str, Any]:
    rows = []
    for period in range(25, 41):
        for family, bits in stress_candidates(period):
            q = tuple(1 if bit else -1 for bit in bits)
            moments = [period] + closed_walk_moments(q, 11)
            first = None
            for depth in range(2, 6):
                if first_negative_principal_minor(moments, depth) is not None:
                    first = depth
                    break
            rows.append({"period": period, "family": family, "first_Hankel_exclusion_depth": first, "survives_m5": first is None, "primitive_control_intent": family in ("LONG_PRIMITIVE", "SEEDED_CONTROL")})
    survivors = sum(row["survives_m5"] for row in rows)
    return {
        "status": "SUPPORTING_EVIDENCE_ONLY",
        "classification": "STRONG" if survivors <= 8 else "MIXED" if survivors <= 24 else "WEAK",
        "periods": [25, 40],
        "states": len(rows),
        "m5_survivors": survivors,
        "not_a_classification": True,
        "not_a_theorem": True,
        "rows": rows,
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    charge = charge_landscape()
    stability = four_step_stability()
    stress = hankel_stress()
    portability = {
        "status": "NO_PORTABILITY_CLAIM",
        "reason": "The JCTB proof-readiness gates already produced decisive information; a nearby-model experiment would start a separate project and was stopped by the resource rule.",
    }
    write_json(OUTPUT / "charge_landscape.json", charge)
    write_json(OUTPUT / "four_step_stability.json", stability)
    write_json(OUTPUT / "hankel_beyond_p24_stress.json", stress)
    write_json(OUTPUT / "interface_portability.json", portability)
    result = {"charge": charge["status"], "four_step": stability["classification"], "hankel_stress": stress["classification"], "portability": portability["status"]}
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    run()
