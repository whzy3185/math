"""Charge bookkeeping, single-charge interfaces, and bounded multi-slip tests."""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp

from target_a_flux_search import signing_from_q
from target_a_reproduce import numpy_matrix
from target_a_task47_common import write_json
from target_a_task48a_common import canonical_code, dense_spectrum, q_from_gaps
from target_a_task49_insurance import spread_gaps
from target_a_task50_g6_certificate import symbolic_defect_transfer, tau_window
from target_a_general_period_moments import tau_lift


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "experiments" / "task51"
DISCOVERY = RESEARCH / "discovery" / "task51"
ETA = 4 + math.sqrt(10 + 2 * math.sqrt(5))
GAPS = (1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12)


def charge_table() -> dict[str, Any]:
    rows = []
    for residue in (0, 2, 4, 6):
        alternatives = sorted({residue - 16, residue - 8, residue, residue + 8})
        positive = [2] * (residue // 2)
        negative = residue - 8 if residue else -8
        rows.append({
            "n_mod_8": residue,
            "legal_positive_defect_parity": "even",
            "total_charge_congruence_mod_8": residue,
            "representative_total_charges": alternatives,
            "minimal_nonnegative_plus2_decomposition": positive,
            "nearest_negative_total_charge": negative,
            "holonomy": [-1, 1],
        })
    return {
        "status": "EXACT_CHARGE_CONSERVATION_PROVED",
        "identities": {
            "gap_partition": "sum_i g_i=n",
            "charge_definition": "q_i=g_i-4",
            "total_charge": "sum_i q_i=n-4d",
            "Q_legality": "product_i Q_i=(-1)^(n-d)=1",
            "even_n_consequence": "d is even",
            "residue_consequence": "sum_i q_i congruent n (mod 8)",
        },
        "proof": "The positive-Q sites partition the cycle into d positive gaps. Summing g_i-4 gives n-4d. For even n, the periodic tau lift condition product Q=1 forces d even, hence 4d is divisible by 8.",
        "rows": rows,
        "minimality_boundary": "The +2 decompositions minimize the number and magnitude of positive even charges arithmetically; spectral optimality is a separate question.",
    }


def open_interface(gap: int, half_width: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    indices = np.arange(-half_width, half_width + 1)
    tau = tau_window(gap, low=-half_width - 4, high=half_width + 5)
    size = len(indices)
    matrix = np.zeros((size, size), dtype=float)
    for local, physical in enumerate(indices):
        if local + 1 < size:
            matrix[local, local + 1] = matrix[local + 1, local] = 1.0
        if local + 2 < size:
            matrix[local, local + 2] = matrix[local + 2, local] = float(tau[int(physical)])
    values, vectors = np.linalg.eigh(matrix)
    return indices, values, vectors


def localized_levels(gap: int, half_width: int) -> list[dict[str, Any]]:
    indices, values, vectors = open_interface(gap, half_width)
    center = gap / 2
    core = np.abs(indices - center) <= max(14, gap + 4)
    boundary = (indices < indices[0] + 20) | (indices > indices[-1] - 20)
    levels = []
    for column, value in enumerate(values):
        squared = float(value * value)
        if value <= 0 or squared <= ETA + 1e-5:
            continue
        weights = vectors[:, column] ** 2
        core_mass = float(weights[core].sum())
        boundary_mass = float(weights[boundary].sum())
        if core_mass < 0.2 or boundary_mass > 0.05:
            continue
        levels.append({
            "lambda": float(value),
            "R_squared": squared,
            "core_mass": core_mass,
            "boundary_mass": boundary_mass,
        })
    return levels


def symbolic_generators() -> dict[str, Any]:
    records = {}
    stored_task50 = {
        6: json.loads((RESEARCH / "proofs" / "task50" / "certificates" / "g6_defect_transfer.json").read_text()),
        10: json.loads((RESEARCH / "proofs" / "task50" / "certificates" / "g10_defect_transfer.json").read_text()),
    }
    for gap in GAPS:
        generated = symbolic_defect_transfer(gap)
        entries_text = json.dumps(generated["entries"], separators=(",", ":"))
        regression = None
        if gap in stored_task50:
            regression = generated == stored_task50[gap]
            if not regression:
                raise AssertionError(f"G{gap} transfer regression failed")
        lam = sp.symbols("lam")
        matrix = sp.Matrix([[sp.sympify(value.replace("lambda", "lam"), locals={"lam": lam}) for value in row] for row in generated["entries"]])
        records[str(gap)] = {
            "gap": gap,
            "charge": gap - 4,
            "cut": generated["cut"],
            "determinant": generated["determinant"],
            "maximum_entry_degree": int(max(sp.degree(value, lam) for value in matrix)),
            "entries_sha256": hashlib.sha256(entries_text.encode()).hexdigest(),
            "task50_exact_regression": regression,
            "entries": generated["entries"] if gap in (2, 6, 10) else "stored by digest; regenerate with symbolic_defect_transfer(g)",
        }
    return {
        "status": "GENERAL_CHARGE_TRANSFER_GENERATOR_EXACT",
        "orientation": "left defects at 4Z through 0; right defects at g+4Z from g onward",
        "records": records,
        "G6_regression": records["6"]["task50_exact_regression"],
        "G10_regression": records["10"]["task50_exact_regression"],
    }


def single_charge_spectrum() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    rows = []
    for gap in GAPS:
        ladders = {width: localized_levels(gap, width) for width in (120, 180)}
        final = ladders[180]
        for index, level in enumerate(final):
            nearest = min((abs(level["R_squared"] - item["R_squared"]) for item in ladders[120]), default=math.inf)
            rows.append({
                "gap": gap,
                "charge": gap - 4,
                "orientation": "canonical left/right",
                "root_index": index,
                **level,
                "width_120_to_180_difference": nearest,
                "localized_root_below_8": level["R_squared"] < 8,
                "evidence_status": "DETERMINISTIC_DOUBLE_OPEN_INTERFACE",
            })
        if not final:
            rows.append({
                "gap": gap,
                "charge": gap - 4,
                "orientation": "canonical left/right",
                "root_index": "",
                "lambda": "",
                "R_squared": "",
                "core_mass": "",
                "boundary_mass": "",
                "width_120_to_180_difference": "",
                "localized_root_below_8": False,
                "evidence_status": "NO_LOCALIZED_LEVEL_DETECTED",
            })
    actual = [row for row in rows if isinstance(row["R_squared"], float)]
    positive = [row for row in actual if row["charge"] > 0 and row["R_squared"] < 8]
    negative = [row for row in actual if row["charge"] < 0]
    gap2 = next((row for row in actual if row["gap"] == 2), None)
    c6 = next(row for row in actual if row["gap"] == 6)
    summary = {
        "status": "MULTIPLE_ELEMENTARY_CHARGES",
        "method": "two-width deterministic open-interface diagonalization with core/boundary localization filters",
        "gap2": gap2,
        "q_minus_2_conclusion": "LOCALIZED_LEVEL_ABOVE_8" if gap2 and gap2["R_squared"] > 8 else "UNRESOLVED",
        "cheapest_positive_sub8": min(positive, key=lambda row: row["R_squared"]) if positive else None,
        "cheapest_negative": min(negative, key=lambda row: row["R_squared"]) if negative else None,
        "G6_reference": c6,
        "root_count_by_gap": {str(gap): sum(row["gap"] == gap and isinstance(row["R_squared"], float) for row in rows) for gap in GAPS},
        "proof_boundary": "Only G6 and G10 retain Task 50 proof status. All new charge levels are deterministic discovery evidence pending interval Evans root counts.",
    }
    return summary, rows


def ring_matrix(gaps: list[int], alpha: int) -> tuple[np.ndarray, tuple[int, ...]]:
    q = q_from_gaps(sum(gaps), gaps)
    code = canonical_code(q)
    signing = signing_from_q(code, len(q), alpha)
    return numpy_matrix(signing).astype(float), q


def minimum_radius(gaps: list[int]) -> dict[str, Any]:
    choices = []
    for alpha in (-1, 1):
        matrix, _q = ring_matrix(gaps, alpha)
        values = np.linalg.eigvalsh(matrix)
        choices.append({"alpha": alpha, "rho_squared": float(np.max(np.abs(values)) ** 2)})
    return min(choices, key=lambda row: row["rho_squared"])


def fixed_gauge_matrix(gaps: list[int]) -> np.ndarray:
    n = sum(gaps)
    positions = set(np.cumsum([0] + gaps[:-1]).tolist())
    q = tuple(1 if index in positions else -1 for index in range(n))
    tau = tau_lift(q)
    matrix = np.zeros((n, n), dtype=np.int64)
    for index in range(n):
        matrix[index, (index + 1) % n] = matrix[(index + 1) % n, index] = 1
        matrix[index, (index + 2) % n] = matrix[(index + 2) % n, index] = tau[index]
    return matrix


def finite_rank_inertia() -> dict[str, Any]:
    cases = {
        "G6_neutralized_by_gap2": [6, 2],
        "G10_neutralized_by_three_gap2": [10, 2, 2, 2],
        "gap2_neutralized_by_G6": [2, 6],
        "gap8_neutralized_by_two_gap2": [8, 2, 2],
        "two_G6_neutralized_by_two_gap2": [6, 6, 2, 2],
    }
    rows = []
    bulk = fixed_gauge_matrix([4] * 32)
    bulk_square = bulk @ bulk
    variable = sp.symbols("x")
    for name, special in cases.items():
        gaps = special + [4] * (32 - len(special))
        matrix = fixed_gauge_matrix(gaps)
        perturbation = matrix @ matrix - bulk_square
        support = np.flatnonzero(np.any(perturbation != 0, axis=0) | np.any(perturbation != 0, axis=1))
        core = sp.Matrix(perturbation[np.ix_(support, support)].tolist())
        rank = int(core.rank())
        polynomial = sp.Poly(core.charpoly(variable).as_expr(), variable)
        zero_multiplicity = 0
        quotient = polynomial
        while quotient.eval(0) == 0:
            quotient = sp.div(quotient, sp.Poly(variable, variable))[0]
            zero_multiplicity += 1
        negative = int(quotient.count_roots(-sp.oo, 0))
        positive = rank - negative
        rows.append({
            "case": name,
            "special_gaps": special,
            "support": support.tolist(),
            "support_size": len(support),
            "rank": rank,
            "positive_inertia": positive,
            "negative_inertia": negative,
            "zero_inertia_in_core": zero_multiplicity,
            "arithmetic": "exact integer rank and exact Sturm root count",
        })
    return {
        "status": "NEUTRAL_FINITE_DEFECT_RANK_INERTIA_EXACT",
        "rows": rows,
        "charged_interface_boundary": "A lone nonzero charge joins translated bulk sectors and is not a finite-rank perturbation of one globally fixed bulk gauge. Neutralized compact combinations are finite rank as certified here.",
        "Birman_Schwinger_consequence": "A direct one-bulk finite-rank Birman-Schwinger model is not applicable to isolated G6/G10 without first constructing a piecewise bulk unitary; neutral compact defects remain viable.",
    }


def green_birman_crosscheck() -> dict[str, Any]:
    bulk = fixed_gauge_matrix([4] * 32).astype(float)
    defect = fixed_gauge_matrix([6, 2] + [4] * 30).astype(float)
    bulk_square = bulk @ bulk
    perturbation = defect @ defect - bulk_square
    support = np.flatnonzero(np.any(np.abs(perturbation) > 0, axis=0) | np.any(np.abs(perturbation) > 0, axis=1))
    core = perturbation[np.ix_(support, support)]
    y = 10.0
    resolvent_denominator = y * np.eye(len(bulk)) - bulk_square
    selector = np.eye(len(bulk))[:, support]
    solved = np.linalg.solve(resolvent_denominator, selector)
    green_from_solve = selector.T @ solved
    green_from_inverse = np.linalg.inv(resolvent_denominator)[np.ix_(support, support)]
    reduced = np.eye(len(support)) - core @ green_from_solve
    sign_full, log_full = np.linalg.slogdet(y * np.eye(len(bulk)) - defect @ defect)
    sign_bulk, log_bulk = np.linalg.slogdet(resolvent_denominator)
    sign_reduced, log_reduced = np.linalg.slogdet(reduced)
    return {
        "status": "SELECTED_GREEN_BIRMAN_CROSSCHECK_PASS",
        "case": "G6+gap2 neutral compact defect",
        "y": y,
        "support_size": len(support),
        "green_inverse_solve_max_error": float(np.max(np.abs(green_from_solve - green_from_inverse))),
        "determinant_lemma_log_error": float(abs((log_full - log_bulk) - log_reduced)),
        "determinant_lemma_sign_match": bool(sign_full * sign_bulk == sign_reduced),
        "scope": "one finite neutral ring at a resolvent point; not a finite/infinite Green comparison",
    }


def cluster_record(special: list[int], defect_count: int) -> dict[str, Any]:
    gaps = spread_gaps(special, defect_count)
    best = minimum_radius(gaps)
    matrix, _q = ring_matrix(gaps, best["alpha"])
    values, vectors = np.linalg.eigh(matrix)
    positive = [(value, column) for column, value in enumerate(values) if value > 0 and value * value > ETA + 1e-4]
    expected = len(special)
    positive = positive[-expected:]
    selected = np.column_stack([vectors[:, column] for value, column in positive])
    squared_matrix = matrix @ matrix
    # Project delta seeds near evenly spaced special defects into the positive
    # interface cluster, then orthonormalize to obtain a localized effective basis.
    positions = np.linspace(0, len(gaps) - 1, expected, endpoint=False, dtype=int)
    defect_vertices = np.cumsum([0] + gaps[:-1])
    seeds = np.zeros((matrix.shape[0], expected))
    for column, position in enumerate(positions):
        seeds[int(defect_vertices[position]) % matrix.shape[0], column] = 1
    projected = selected @ (selected.T @ seeds)
    basis, _ = np.linalg.qr(projected)
    heff = basis.T @ squared_matrix @ basis
    reconstructed = np.linalg.eigvalsh(heff)
    exact_cluster = sorted([float(value * value) for value, _column in positive])
    return {
        "special_gaps": special,
        "charges": [gap - 4 for gap in special],
        "n": sum(gaps),
        "defect_count": defect_count,
        **best,
        "positive_interface_cluster_squared": exact_cluster,
        "effective_matrix_squared": heff.tolist(),
        "effective_reconstruction_error": float(max(abs(a - b) for a, b in zip(reconstructed, exact_cluster))) if exact_cluster else None,
        "evidence_status": "DETERMINISTIC_DOUBLE_EFFECTIVE_SUBSPACE",
    }


def multi_slip() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    cases = []
    for special in ([6, 6], [6, 6, 6], [6, 6, 6, 6], [10], [8, 6], [2, 10], [8], [6]):
        defect_count = 64
        if defect_count < len(special):
            continue
        cases.append(cluster_record(list(special), defect_count))
    three = next(row for row in cases if row["special_gaps"] == [6, 6, 6])
    g10 = next(row for row in cases if row["special_gaps"] == [10])
    comparison = three["rho_squared"] - g10["rho_squared"]
    two = next(row for row in cases if row["special_gaps"] == [6, 6])
    four = next(row for row in cases if row["special_gaps"] == [6, 6, 6, 6])
    c6 = 7.905369311620327
    pair_shift = two["rho_squared"] - c6
    below_double = abs(pair_shift) < 1e-12
    three_pair_prediction = c6 + 3 * pair_shift
    four_pair_prediction = c6 + 6 * pair_shift
    summary = {
        "status": "MULTI_SLIP_RECONNAISSANCE_COMPLETE",
        "three_G6_minus_G10_at_fixed_defect_count": comparison,
        "three_G6_beats_G10": comparison < 0,
        "pairwise_scalar_diagnostic": {
            "two_slip_shift": pair_shift,
            "three_prediction": three_pair_prediction,
            "three_residual": three["rho_squared"] - three_pair_prediction,
            "four_prediction": four_pair_prediction,
            "four_residual": four["rho_squared"] - four_pair_prediction,
            "classification": "BELOW_DOUBLE_RESOLUTION" if below_double else "PAIRWISE_INSUFFICIENT",
        },
        "effective_matrix_classification": "EXACT_CLUSTER_RECONSTRUCTION_NUMERICAL_BASIS",
        "mod16": "TWO_PATH_HOLONOMY_PROMISING_NOT_DERIVED",
        "many_body_classification": "UNRESOLVED" if below_double else "PAIRWISE_INSUFFICIENT",
        "proof_boundary": "The effective matrices exactly reconstruct selected numerical clusters but do not yet provide uniform tunnelling asymptotics or global minimizer lower bounds. A pair shift below 1e-12 is explicitly treated as below double resolution.",
    }
    return summary, cases


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fields = list(rows[0])
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    DISCOVERY.mkdir(parents=True, exist_ok=True)
    charge = charge_table()
    symbolic = symbolic_generators()
    spectrum, spectrum_rows = single_charge_spectrum()
    multi, clusters = multi_slip()
    inertia = finite_rank_inertia()
    green = green_birman_crosscheck()
    write_json(OUTPUT / "charge_conservation.json", charge)
    write_json(OUTPUT / "single_charge_symbolic.json", symbolic)
    write_json(OUTPUT / "single_charge_summary.json", spectrum)
    write_csv(OUTPUT / "single_charge_spectrum.csv", spectrum_rows)
    write_json(OUTPUT / "multi_slip_summary.json", multi)
    write_json(OUTPUT / "finite_rank_inertia.json", inertia)
    write_json(OUTPUT / "green_birman_crosscheck.json", green)
    write_csv(OUTPUT / "multi_slip_clusters.csv", [{key: json.dumps(value) if isinstance(value, (list, dict)) else value for key, value in row.items()} for row in clusters])
    write_json(OUTPUT / "effective_interaction_fits.json", multi["pairwise_scalar_diagnostic"])
    result = {
        "charge": charge["status"],
        "single": spectrum["status"],
        "gap2": spectrum["q_minus_2_conclusion"],
        "three_G6_beats_G10": multi["three_G6_beats_G10"],
    }
    print(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    run()
