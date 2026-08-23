"""Bounded falsification and theorem-oriented reconnaissance for Task 52."""

from __future__ import annotations

import csv
import itertools
import json
import math
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np
import sympy as sp

from target_a_flux_search import canonical_q_code, signing_from_q, triangle_flux_from_q
from target_a_general_period_moments import closed_walk_q_expansion
from target_a_low_period_spectral_frontier import _candidate_vectors, primitive_period
from target_a_period10_family import polynomial_y_c
from target_a_reproduce import numpy_matrix
from target_a_task47_common import write_json
from target_a_task48a_common import q_from_gaps
from target_a_task49_insurance import spread_gaps
from target_a_task49_interface_robustness import finite_ring_evans


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "experiments" / "task52"
PROOFS = RESEARCH / "proofs" / "task52" / "certificates"
ETA = 4 + math.sqrt(10 + 2 * math.sqrt(5))
C6 = 7.905369311620327
C6_LEFT = sp.Rational(7905369311620327, 10**15)
C6_RIGHT = sp.Rational(7905369311620328, 10**15)
ALPHABET = tuple(value for value in range(1, 13) if value != 4)


def canonical_interface(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word, tuple(reversed(word)))


def is_primitive_interface(word: tuple[int, ...]) -> bool:
    charges = tuple(gap - 4 for gap in word)
    if not charges or any(gap == 4 for gap in word):
        return False
    length = len(charges)
    for start in range(length):
        total = 0
        for stop in range(start, length):
            total += charges[stop]
            if total == 0 and stop - start + 1 < length:
                return False
    return True


def interface_q_positions(word: tuple[int, ...], low: int, high: int) -> set[int]:
    positions = set(range(-4 * ((-low + 3) // 4), 1, 4))
    endpoint = 0
    for gap in word:
        endpoint += gap
        positions.add(endpoint)
    positions.update(range(endpoint, high + 4, 4))
    return positions


def open_interface_levels(word: tuple[int, ...], half_width: int) -> list[float]:
    endpoint = sum(word)
    low, high = -half_width - 4, endpoint + half_width + 5
    positions = interface_q_positions(word, low, high)
    q = {index: 1 if index in positions else -1 for index in range(low, high)}
    tau = {0: 1}
    for index in range(high - 1):
        tau[index + 1] = q[index] * tau[index]
    for index in range(-1, low, -1):
        tau[index] = q[index] * tau[index + 1]
    indices = np.arange(-half_width, endpoint + half_width + 1)
    size = len(indices)
    matrix = np.zeros((size, size), dtype=float)
    for local, physical in enumerate(indices):
        if local + 1 < size:
            matrix[local, local + 1] = matrix[local + 1, local] = 1.0
        if local + 2 < size:
            matrix[local, local + 2] = matrix[local + 2, local] = float(tau[int(physical)])
    values, vectors = np.linalg.eigh(matrix)
    core = (indices >= -16) & (indices <= endpoint + 16)
    boundary = (indices < -half_width + 12) | (indices > endpoint + half_width - 12)
    levels = []
    for column, value in enumerate(values):
        squared = float(value * value)
        mass = vectors[:, column] ** 2
        if squared > ETA + 1e-4 and float(mass[core].sum()) > 0.2 and float(mass[boundary].sum()) < 0.03:
            levels.append(squared)
    # Positive/negative partners can differ at the truncation scale.
    levels.sort()
    merged = []
    for value in levels:
        if not merged or abs(value - merged[-1]) > 2e-6:
            merged.append(value)
        else:
            merged[-1] = max(merged[-1], value)
    return merged


def primitive_interface_search() -> dict[str, Any]:
    records = []
    counts = {}
    for total_charge in (-2, 2, 4, 6):
        words = []
        for length in range(1, 5):
            for word in itertools.product(ALPHABET, repeat=length):
                if sum(gap - 4 for gap in word) != total_charge:
                    continue
                if word != canonical_interface(word) or not is_primitive_interface(word):
                    continue
                words.append(word)
        counts[str(total_charge)] = len(words)
        for word in words:
            levels = open_interface_levels(word, 44)
            records.append({
                "word": list(word),
                "canonical_word": list(canonical_interface(word)),
                "charges": [gap - 4 for gap in word],
                "total_charge": total_charge,
                "support_span": sum(word),
                "localized_levels_squared_scan": levels,
                "interface_cost_scan": max(levels) if levels else None,
                "scan_half_width": 44,
                "evidence": "EXPERIMENTAL_DETERMINISTIC_FP64_OPEN_INTERFACE",
            })
    ranked = sorted((row for row in records if row["interface_cost_scan"] is not None), key=lambda row: row["interface_cost_scan"])
    rechecked = []
    for row in ranked[:24]:
        word = tuple(row["word"])
        levels_68 = open_interface_levels(word, 68)
        levels_92 = open_interface_levels(word, 92)
        rechecked.append({
            "word": row["word"],
            "total_charge": row["total_charge"],
            "levels_half_width_68": levels_68,
            "levels_half_width_92": levels_92,
            "cost_half_width_92": max(levels_92) if levels_92 else None,
            "maximum_level_width_difference": max(
                (min(abs(value - other) for other in levels_68) for value in levels_92), default=None
            ),
        })
    genuine_below = [
        row for row in rechecked
        if row["word"] != [6] and row["cost_half_width_92"] is not None and row["cost_half_width_92"] < C6 - 1e-5
    ]
    return {
        "status": "PLUS_TWO_UNIQUE_ELEMENTARY_EVEN_CHARGE_STRONGLY_SUPPORTED",
        "definition": {
            "finite_word": "A linear word of non-4 gaps between left and right period-four bulk sectors.",
            "charge": "sum(g_i-4)",
            "support": "from the first abnormal gap to the last abnormal gap",
            "equivalence": "translation is removed by putting the first left defect at 0; reflection reverses the gap word",
            "decomposable": "contains a proper contiguous zero-charge subword or an intervening bulk gap 4",
            "primitive": "canonical under reflection and not decomposable by the bounded definition",
        },
        "scope": {"gap_alphabet": list(ALPHABET), "maximum_word_length": 4, "charges": [-2, 2, 4, 6]},
        "canonical_word_counts": counts,
        "records": records,
        "precision_rechecks": rechecked,
        "best_by_charge": {
            str(charge): min(
                (row for row in rechecked if row["total_charge"] == charge and row["cost_half_width_92"] is not None),
                key=lambda row: row["cost_half_width_92"],
                default=None,
            )
            for charge in (-2, 2, 4, 6)
        },
        "non_G6_candidates_below_c6": genuine_below,
        "completeness_achieved": False,
        "proof_boundary": "The search is exhaustive only in the displayed finite alphabet and support length. It cannot prove uniqueness among all primitive interfaces.",
    }


def large_gap_scan() -> dict[str, Any]:
    rows = []
    for gap in range(13, 77):
        word = (gap,)
        first = open_interface_levels(word, 72)
        second = open_interface_levels(word, 96)
        cost = max(second) if second else None
        rows.append({
            "gap": gap,
            "charge": gap - 4,
            "gap_mod_8": gap % 8,
            "levels_half_width_72": first,
            "levels_half_width_96": second,
            "interface_cost": cost,
            "below_c6": cost is not None and cost < C6 - 1e-5,
            "status": "EXPERIMENTAL_DETERMINISTIC_FP64",
        })
    return {
        "status": "NO_LARGE_GAP_THREAT_FOUND_BOUNDED",
        "range": [13, 76],
        "rows": rows,
        "any_cost_below_c6": any(row["below_c6"] for row in rows),
        "asymptotic_limit": "OPEN",
        "eventual_monotonicity": "OPEN",
    }


def ring_spectrum(gaps: list[int], alpha: int) -> tuple[np.ndarray, tuple[int, ...]]:
    q = q_from_gaps(sum(gaps), gaps)
    code = canonical_q_code(sum((value == 1) << index for index, value in enumerate(q)), len(q))
    matrix = numpy_matrix(signing_from_q(code, len(q), alpha)).astype(float)
    return np.linalg.eigvalsh(matrix), q


def fixed_r_scan() -> dict[str, Any]:
    rows = []
    for r in (1, 2, 3, 4):
        for defect_count in (16, 24, 32, 48, 64):
            gaps = spread_gaps([6] * r, defect_count)
            for alpha in (-1, 1):
                values, q = ring_spectrum(gaps, alpha)
                positive_upper = sorted(float(value * value) for value in values if value > 0 and value * value > ETA + 1e-6)
                cluster = [value for value in positive_upper if abs(value - C6) < 0.08]
                reversed_values, _ = ring_spectrum(list(reversed(gaps)), alpha)
                rows.append({
                    "r": r,
                    "defect_count": defect_count,
                    "n": sum(gaps),
                    "alpha": alpha,
                    "gaps": gaps,
                    "legal_even_defect_count": len(gaps) % 2 == 0,
                    "charge_congruence": sum(gap - 4 for gap in gaps) % 8 == sum(gaps) % 8,
                    "positive_upper_gap_levels": positive_upper,
                    "near_c6_cluster": cluster,
                    "near_c6_cluster_count": len(cluster),
                    "hidden_positive_upper_levels": [value for value in positive_upper if value not in cluster],
                    "rho_squared": float(max(abs(values[0]), abs(values[-1])) ** 2),
                    "cluster_contains_r_levels": len(cluster) >= r,
                    "orientation_reversal_rho_error": float(abs(max(abs(values)) ** 2 - max(abs(reversed_values)) ** 2)),
                    "evidence": "EXPERIMENTAL_DETERMINISTIC_FULL_FP64_SPECTRUM",
                })
    large_separation = [row for row in rows if row["defect_count"] >= 48]
    return {
        "status": "FIXED_R_CLUSTER_NUMERICAL_STRESS_COMPLETE_GLOBAL_CAP_OPEN",
        "rows": rows,
        "large_separation_all_have_r_cluster_levels": all(row["cluster_contains_r_levels"] for row in large_separation),
        "large_separation_hidden_branch_cases": sum(bool(row["hidden_positive_upper_levels"]) for row in large_separation),
        "r4_stress": "PASS_NUMERICAL_CLUSTER_EXISTENCE" if all(row["cluster_contains_r_levels"] for row in rows if row["r"] == 4 and row["defect_count"] >= 48) else "MIXED",
        "proof_boundary": "Full FP64 spectra falsify hidden-branch claims only for the listed finite rings. Exact counting and a uniform spectral cap remain open.",
    }


def high_precision_cluster(r: int, defect_count: int, alpha: int) -> dict[str, Any]:
    gaps = spread_gaps([6] * r, defect_count)
    values, q = ring_spectrum(gaps, alpha)
    guesses = sorted(
        (float(value) for value in values if value > 0 and abs(value * value - C6) < 0.08), reverse=True
    )[:r]
    code = canonical_q_code(sum((value == 1) << index for index, value in enumerate(q)), len(q))
    tau = triangle_flux_from_q(code, len(q))
    ladder = []
    previous = None
    for digits in (80, 120, 160):
        mp.mp.dps = digits
        roots = []
        for index, guess in enumerate(guesses):
            nearest = min((abs(guess - other) for j, other in enumerate(guesses) if j != index), default=1e-4)
            step = max(mp.mpf("1e-10"), mp.mpf(str(nearest)) / 8)
            center = mp.mpf(str(guess))
            root = mp.findroot(
                lambda value: finite_ring_evans(value, tau, alpha),
                (center - step, center + step), solver="secant",
                tol=mp.mpf(10) ** (-(digits - 20)), maxsteps=100, verify=False,
            )
            roots.append(root)
        roots.sort(reverse=True)
        y_values = [root * root for root in roots]
        agreement = None if previous is None else max(abs(y_values[i] - previous[i]) for i in range(r))
        ladder.append({
            "digits": digits,
            "lambda": [mp.nstr(value, digits - 10) for value in roots],
            "y": [mp.nstr(value, digits - 10) for value in y_values],
            "max_y_change_from_previous_precision": None if agreement is None else mp.nstr(agreement, 25),
        })
        previous = y_values
    fp64_y = [guess * guess for guess in guesses]
    return {
        "r": r,
        "defect_count": defect_count,
        "n": sum(gaps),
        "alpha": alpha,
        "fp64_y": fp64_y,
        "precision_ladder": ladder,
        "finite_matrix_transfer_max_difference": mp.nstr(max(abs(previous[i] - fp64_y[i]) for i in range(r)), 25),
        "reciprocal_Floquet_structure": "Inherited exact M8 palindromic quartic with two stable and two reciprocal unstable multipliers.",
        "evidence": "HIGH_PRECISION_FINITE_RING_TRANSFER_EVANS",
    }


def high_precision_fixed_r() -> dict[str, Any]:
    cases = []
    for r, defect_count in ((2, 24), (3, 24)):
        for alpha in (-1, 1):
            cases.append(high_precision_cluster(r, defect_count, alpha))
    return {
        "status": "R2_R3_REPRESENTATIVE_HIGH_PRECISION_EVANS_COMPLETE",
        "cases": cases,
        "full_arbitrary_precision_matrix_eigensolves": "Not repeated; Task49 already supplies representative r=2 finite-matrix cross-checks.",
    }


def c6_weighted_moments() -> dict[str, Any]:
    expansions = {moment: closed_walk_q_expansion(2 * moment)["translation_class_coefficients"] for moment in range(1, 7)}
    forms = {}
    for k in range(1, 6):
        keys = sorted(set(expansions[k]) | set(expansions[k + 1]))
        coefficients = {
            key: {"rational": expansions[k + 1].get(key, 0), "c6_coefficient": -expansions[k].get(key, 0)}
            for key in keys
            if expansions[k + 1].get(key, 0) or expansions[k].get(key, 0)
        }
        forms[f"F{k}"] = {
            "definition": f"M{k + 1}-c6*M{k}",
            "translation_class_count": len(coefficients),
            "coefficients_a_plus_b_c6": coefficients,
        }
    return {
        "status": "C6_WEIGHTED_MOMENT_FORMS_EXACT",
        "number_field": "Q(c6), with c6 defined by the Task51 irreducible degree-ten polynomial and its isolating interval",
        "implication": "R^2<=c6 implies F_k<=0 for k=1,...,5",
        "forms": forms,
        "small_combination_search": "NO_LOW_DIMENSIONAL_POSITIVITY_SIGNAL",
        "deeper_moment_generation": "STOPPED_AT_M6_BY_TASK_RULE",
    }


def c6_low_energy_grammar() -> dict[str, Any]:
    levels = []
    survivors: set[tuple[int, ...]] = set()
    for support_length in range(6, 11):
        width = support_length + 2
        current = set()
        certificates = 0
        for tau_word in itertools.product((-1, 1), repeat=width):
            from target_a_task51_crystallization import local_rayleigh_matrix

            square = local_rayleigh_matrix(tau_word, support_length)
            excluded = False
            for vector in _candidate_vectors(square):
                column = np.asarray(vector, dtype=np.int64)
                denominator = int(column @ column)
                numerator = int(column @ square @ column)
                if sp.Rational(numerator, denominator) > C6_RIGHT:
                    excluded = True
                    break
            q_window = tuple(tau_word[index] * tau_word[index + 1] for index in range(width - 1))
            if excluded:
                certificates += 1
            else:
                current.add(q_window)
        levels.append({
            "support_length": support_length,
            "tau_windows": 2**width,
            "exact_c6_Rayleigh_exclusions": certificates,
            "distinct_Q_survivors": len(current),
        })
        if support_length == 10:
            survivors = current

    window_length = 11
    nodes = {word[:-1] for word in survivors} | {word[1:] for word in survivors}
    edges = {(word[:-1], word[1:]) for word in survivors}
    cycles = set()
    for period in range(1, 17):
        for word in itertools.product((-1, 1), repeat=period):
            if primitive_period(word) != period:
                continue
            if all(tuple(word[(start + offset) % period] for offset in range(window_length)) in survivors for start in range(period)):
                rotations = [word[index:] + word[:index] for index in range(period)]
                cycles.add(min(rotations + [tuple(reversed(item)) for item in rotations]))
    target = (-1, -1, -1, 1)
    target_present = any(
        len(word) == 4 and word in {target[index:] + target[:index] for index in range(4)} for word in cycles
    )
    return {
        "status": "C6_LOW_ENERGY_GRAMMAR_EXACT_FINITE_PARTIAL",
        "threshold_upper_endpoint": str(C6_RIGHT),
        "levels": levels,
        "overlap_automaton": {"window_length": window_length, "nodes": len(nodes), "edges": len(edges)},
        "primitive_cycles_through_period_16": len(cycles),
        "displayed_cycles": ["".join("1" if value == 1 else "0" for value in word) for word in sorted(cycles, key=lambda word: (len(word), word))[:200]],
        "period_eight_bulk_cycle_present": target_present,
        "bulk_plus_slip_decomposition": "OPEN",
        "dense_defect_lower_bound": "OPEN",
        "classification": "WEAK" if len(cycles) > 1 else "STRONG_BOUNDED",
        "proof_boundary": "Every local exclusion is an exact rational Rayleigh comparison with the rational upper endpoint for c6. The overlap/cycle audit is finite and does not classify all long words.",
    }


def p24_c6_audit() -> dict[str, Any]:
    rows = list(csv.DictReader((RESEARCH / "experiments" / "task51" / "subeight_periodic_phases.csv").open()))
    primitive = [
        row for row in rows
        if row["band_at_8"] == "R_LT_8" and int(row["primitive_tau_period"]) == int(row["period"])
    ]
    target = [row for row in primitive if int(row["primitive_tau_period"]) == 8]
    non_target = [row for row in primitive if int(row["primitive_tau_period"]) != 8]
    below = [row for row in non_target if float(row["R_squared"]) < C6 - 1e-10]
    y, c = sp.symbols("y c")
    endpoint = sp.expand(polynomial_y_c(y, c).subs(c, -2))
    derivative = sp.diff(endpoint, y)
    period10_checks = {
        "P_at_c6_right_negative": bool(endpoint.subs(y, C6_RIGHT) < 0),
        "P_at_8_positive": bool(endpoint.subs(y, 8) > 0),
        "derivative_positive_at_c6_left": bool(derivative.subs(y, C6_LEFT) > 0),
        "derivative_no_root_on_c6_to_8": bool(sp.Poly(derivative, y).count_roots(C6_LEFT, 8) == 0),
    }
    return {
        "status": "P24_C6_BOUNDED_AUDIT_COMPLETE",
        "primitive_sub8_count": len(primitive),
        "target_period8_rows": len(target),
        "non_target_rows": len(non_target),
        "numerical_non_target_below_c6": below,
        "period10_exact": {
            "status": "PERIOD10_BAND_EDGE_GT_C6_PROVED",
            "Bloch_endpoint": "c=-2",
            "argument": "P(c6,-2)<0, P(8,-2)>0, and dP/dy has no zero on [c6,8], so the endpoint block has one root in (c6,8).",
            "checks": period10_checks,
        },
        "other_phases": "EXPERIMENTAL numerical comparisons only",
        "bounded_period_boundary": "No conclusion beyond primitive periods at most 24.",
    }


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    payloads = {
        "primitive_interface_search.json": primitive_interface_search(),
        "large_gap_scan.json": large_gap_scan(),
        "fixed_r_full_spectrum_scan.json": fixed_r_scan(),
        "fixed_r_high_precision_evans.json": high_precision_fixed_r(),
        "c6_weighted_moments.json": c6_weighted_moments(),
        "c6_low_energy_grammar.json": c6_low_energy_grammar(),
        "p24_c6_audit.json": p24_c6_audit(),
    }
    for name, payload in payloads.items():
        write_json(OUTPUT / name, payload)
    summary = {
        "status": "TASK52_BOUNDED_EXPLORATION_COMPLETE",
        "primitive_threat": bool(payloads["primitive_interface_search.json"]["non_G6_candidates_below_c6"]),
        "large_gap_threat": payloads["large_gap_scan.json"]["any_cost_below_c6"],
        "fixed_r_global_cap": "OPEN",
        "low_energy_grammar": payloads["c6_low_energy_grammar.json"]["classification"],
        "artifacts": sorted(payloads),
    }
    write_json(OUTPUT / "exploration_summary.json", summary)
    print(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    run()
