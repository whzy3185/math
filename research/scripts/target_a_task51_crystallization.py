"""Bounded periodic atlas and local-certificate crystallization reconnaissance."""

from __future__ import annotations

import csv
import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from target_a_general_period_moments import (
    closed_walk_moments,
    closed_walk_q_expansion,
    tau_lift,
)
from target_a_low_period_spectral_frontier import (
    _candidate_vectors,
    numeric_preview,
    primitive_period,
    rational_gt_eta,
)
from target_a_task47_common import write_json
from target_a_task49_insurance import spread_gaps
from target_a_task51_interfaces import ETA, minimum_radius


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "experiments" / "task51"


def q_from_bits(bits: str) -> tuple[int, ...]:
    return tuple(1 if bit == "1" else -1 for bit in bits)


def gap_word(q: tuple[int, ...]) -> list[int]:
    positions = [index for index, value in enumerate(q) if value == 1]
    if not positions:
        return []
    return [
        (positions[(index + 1) % len(positions)] - positions[index]) % len(q) or len(q)
        for index in range(len(positions))
    ]


def atlas_row(period: int, q: tuple[int, ...], source: str, samples: int = 1024) -> dict[str, Any]:
    tau = tau_lift(q)
    preview = numeric_preview(tau, samples)
    gaps = gap_word(q)
    value = preview["R_squared_preview"]
    if value < 8 - 1e-8:
        band = "R_LT_8"
    elif value <= 8 + 1e-8:
        band = "R_EQ_8_NUMERIC"
    else:
        band = "R_GT_8"
    return {
        "period": period,
        "Q_bits": "".join("1" if value == 1 else "0" for value in q),
        "primitive_Q_period": primitive_period(q),
        "primitive_tau_period": primitive_period(tau),
        "gap_word": " ".join(map(str, gaps)),
        "charge_word": " ".join(str(gap - 4) for gap in gaps),
        "defect_density": len(gaps) / period,
        "charge_density": (sum(gaps) - 4 * len(gaps)) / period if gaps else 0.0,
        "R_squared": value,
        "band_at_8": band,
        "source": source,
        "status": "NUMERICAL_BLOCH_ATLAS" if value not in (8.0,) else "EXACT_BASELINE",
    }


def periodic_atlas() -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
    frontier = json.loads((RESEARCH / "proofs" / "target_a_low_period_spectral_frontier.json").read_text())
    candidates: dict[tuple[int, str], tuple[int, ...]] = {}
    for row in frontier["orbits"]:
        if row["numeric_preview"]["R_squared_preview"] <= 8.05:
            q = tuple(row["canonical_q_signs"])
            candidates[(row["p"], row["canonical_q_bits"])] = q
    for period in range(17, 25):
        closure = json.loads((RESEARCH / "experiments" / "exact_frontier" / f"p{period}_closure.json").read_text())
        for row in closure["survivors"]:
            q = q_from_bits(row["q_bits"])
            candidates[(period, row["q_bits"])] = q
    rows = [atlas_row(period, q, "reused exact p<=24 frontier") for (period, _bits), q in sorted(candidates.items())]
    primitive_sub8 = [row for row in rows if row["band_at_8"] == "R_LT_8" and row["primitive_tau_period"] == row["period"]]

    motifs = ([4], [4, 6], [4, 8], [4, 10], [4, 6, 4, 6], [4, 4, 6], [4, 6, 6])
    motif_rows = []
    for motif in motifs:
        gaps = list(motif)
        while len(gaps) % 2 or (sum(gaps) - len(gaps)) % 2:
            gaps += list(motif)
        q = tuple(1 if index in set(np.cumsum([0] + gaps[:-1]).tolist()) else -1 for index in range(sum(gaps)))
        row = atlas_row(len(q), q, "explicit motif family", 2048)
        row["displayed_motif"] = " ".join(map(str, motif))
        motif_rows.append(row)
    summary = {
        "status": "SUBEIGHT_PERIODIC_ATLAS_COMPLETE_P24_NUMERICAL_BAND_REFINEMENT",
        "reused_frontier_candidates": len(rows),
        "primitive_R_lt_8_count": len(primitive_sub8),
        "primitive_periods": sorted({row["period"] for row in primitive_sub8}),
        "minimum_non_target": min((row for row in primitive_sub8 if row["primitive_tau_period"] != 8), key=lambda row: row["R_squared"], default=None),
        "exact_boundary": "The eta comparison through p=24 remains exact. New R<8 labels use a deterministic 1024-point Bloch grid except for already proved period-eight/ten identities.",
    }
    return summary, rows, motif_rows


def evaluate_expansion(q: tuple[int, ...], expansion: dict[str, Any]) -> int:
    total = 0
    p = len(q)
    for key, coefficient in expansion["translation_class_coefficients"].items():
        if key == "const":
            total += coefficient * p
            continue
        support = tuple(map(int, key.split(",")))
        total += coefficient * sum(math.prod(q[(origin + offset) % p] for offset in support) for origin in range(p))
    return total


def higher_moments() -> dict[str, Any]:
    expansions = {length: closed_walk_q_expansion(length) for length in (8, 10, 12)}
    checks = 0
    for p in (13, 17, 23):
        for seed in range(12):
            prefix = tuple(1 if ((seed * 37 + index * 13 + index * index) % 7) < 3 else -1 for index in range(p - 1))
            q = prefix + (math.prod(prefix),)
            moments = closed_walk_moments(q, 6)
            for length in (8, 10, 12):
                if evaluate_expansion(q, expansions[length]) != moments[length // 2 - 1]:
                    raise AssertionError(f"M{length // 2} expansion mismatch")
                checks += 1
    m4 = expansions[8]["translation_class_coefficients"]
    return {
        "status": "M4_M5_M6_EXACT_LOCAL_MOTIF_EXPANSIONS_PROVED",
        "M4_identity": "M4=" + "+".join(f"{coefficient}*S[{key}]" for key, coefficient in m4.items()),
        "spacing_four_explicit": "0,2,4" in m4,
        "expansions": {
            f"M{length // 2}": {
                "closed_step_words": value["closed_step_words"],
                "translation_class_count": len(value["translation_class_coefficients"]),
                "translation_class_coefficients": value["translation_class_coefficients"],
            }
            for length, value in expansions.items()
        },
        "independent_exact_checks": checks,
        "interpretation": "M4 has only ten translation classes and explicitly sees the spacing-four monomial Q_i Q_(i+2) Q_(i+4), justifying bounded M5/M6 generation. Class counts 27 and higher show rapid growth, so no deeper moments are generated in Task 51.",
    }


def local_rayleigh_matrix(tau_word: tuple[int, ...], support_length: int) -> np.ndarray:
    # tau_word stores tau_-2,...,tau_(L-1).
    tau = {index - 2: value for index, value in enumerate(tau_word)}
    outputs = list(range(-2, support_length + 2))
    matrix = np.zeros((len(outputs), support_length), dtype=np.int64)
    for column in range(support_length):
        for row, output in enumerate(outputs):
            if abs(output - column) == 1:
                matrix[row, column] = 1
            elif output == column + 2:
                matrix[row, column] = tau[column]
            elif output == column - 2:
                matrix[row, column] = tau[column - 2]
    return matrix.T @ matrix


def local_rayleigh() -> dict[str, Any]:
    levels = []
    final_survivors: set[tuple[int, ...]] = set()
    for support_length in range(6, 11):
        width = support_length + 2
        certificates = 0
        survivors = set()
        maximum_margin = 0.0
        for tau_word in itertools.product((-1, 1), repeat=width):
            square = local_rayleigh_matrix(tau_word, support_length)
            certificate = None
            for vector in _candidate_vectors(square):
                column = np.asarray(vector, dtype=np.int64)
                denominator = int(column @ column)
                numerator = int(column @ square @ column)
                valid, _comparison = rational_gt_eta(numerator, denominator)
                if valid:
                    certificate = (numerator, denominator, vector)
                    maximum_margin = max(maximum_margin, numerator / denominator - ETA)
                    break
            q_window = tuple(tau_word[index] * tau_word[index + 1] for index in range(width - 1))
            if certificate is None:
                survivors.add(q_window)
            else:
                certificates += 1
        levels.append({
            "support_length": support_length,
            "tau_windows": 2**width,
            "exact_Rayleigh_certificates": certificates,
            "distinct_Q_survivors": len(survivors),
            "maximum_certified_margin": maximum_margin,
        })
        if support_length == 10:
            final_survivors = survivors

    # Bounded de Bruijn audit: every primitive binary Q word through period 16
    # whose cyclic windows all survive the strongest local test is retained.
    window_length = 11
    cycles = set()
    for period in range(1, 17):
        for word in itertools.product((-1, 1), repeat=period):
            if primitive_period(word) != period:
                continue
            if all(tuple(word[(start + offset) % period] for offset in range(window_length)) in final_survivors for start in range(period)):
                rotations = [word[k:] + word[:k] for k in range(period)]
                canonical = min(rotations + [tuple(reversed(item)) for item in rotations])
                cycles.add(canonical)
    target = (-1, -1, -1, 1)
    target_present = any(len(word) == 4 and word in {target[k:] + target[:k] for k in range(4)} for word in cycles)
    return {
        "status": "LOCAL_RAYLEIGH_LEVEL2_COMPLETE",
        "levels": levels,
        "strongest_Q_survivors": len(final_survivors),
        "de_bruijn_bounded_cycle_count_period_le_16": len(cycles),
        "bounded_cycles": ["".join("1" if value == 1 else "0" for value in word) for word in sorted(cycles, key=lambda word: (len(word), word))[:200]],
        "target_cycle_present": target_present,
        "classification": "STRONG" if len(cycles) == 1 and target_present else "WEAK",
        "proof_boundary": "Each exclusion is an exact integer Rayleigh quotient. The cycle audit is complete only through primitive period 16, so it is not an arbitrary-period theorem.",
    }


def peierls_search() -> dict[str, Any]:
    motifs = set()
    for length in range(2, 5):
        for charges in itertools.product((-2, -1, 1, 2), repeat=length):
            if sum(charges) != 0:
                continue
            rotations = [charges[k:] + charges[:k] for k in range(length)]
            motifs.add(min(rotations + [tuple(reversed(item)) for item in rotations]))
    rows = []
    for charges in sorted(motifs, key=lambda value: (len(value), value)):
        special = [4 + value for value in charges]
        ladders = []
        for defect_count in (32, 64):
            gaps = special + [4] * (defect_count - len(special))
            best = minimum_radius(gaps)
            ladders.append({"n": sum(gaps), **best, "Delta": best["rho_squared"] - ETA})
        rows.append({"charges": list(charges), "gaps": special, "precision_ladder": ladders})
    best = min((step | {"charges": row["charges"], "gaps": row["gaps"]} for row in rows for step in row["precision_ladder"]), key=lambda row: row["Delta"])
    if best["Delta"] < -1e-8:
        scenario = "D_DEFECT_BELOW_BULK"
    elif best["Delta"] <= 1e-8:
        scenario = "B_OR_C_TRANSPARENT_SIGNAL"
    else:
        scenario = "A_BOUNDED_SUPPORT_POSITIVE_SIGNAL"
    return {
        "status": "FINITE_DEFECT_PEIERLS_BOUNDED_SEARCH_COMPLETE",
        "motif_count": len(rows),
        "support_charge_alphabet": [-2, -1, 1, 2],
        "support_lengths": [2, 4],
        "rows": rows,
        "minimum": best,
        "scenario": scenario,
        "transparent_defect_found": best["Delta"] <= 1e-8,
        "proof_boundary": "This is a deterministic exhaustive search in the stated charge alphabet and support bound, not a uniform Peierls theorem over arbitrary finite defects.",
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    atlas, atlas_rows, motifs = periodic_atlas()
    moments = higher_moments()
    rayleigh = local_rayleigh()
    peierls = peierls_search()
    write_json(OUTPUT / "subeight_periodic_summary.json", atlas)
    write_csv(OUTPUT / "subeight_periodic_phases.csv", atlas_rows)
    write_json(OUTPUT / "defect_crystal_families.json", {"families": motifs})
    write_json(OUTPUT / "higher_moment_motifs.json", moments)
    write_json(OUTPUT / "local_rayleigh_debruijn.json", rayleigh)
    write_json(OUTPUT / "transparent_defect_search.json", peierls)
    result = {
        "atlas": atlas["status"],
        "primitive_sub8": atlas["primitive_R_lt_8_count"],
        "moments": moments["status"],
        "rayleigh": rayleigh["classification"],
        "peierls": peierls["scenario"],
    }
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    run()
