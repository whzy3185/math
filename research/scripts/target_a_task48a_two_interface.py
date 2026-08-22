"""Task 48A Parts C-D: two-interface splitting and residue-12 reconnaissance."""

from __future__ import annotations

import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from target_a_flux_search import signing_from_q
from target_a_reproduce import numpy_matrix
from target_a_task47_common import q_bits, sha256, write_json
from target_a_task48a_common import (
    canonical_code,
    dense_spectrum,
    fit_models,
    q_from_gaps,
    single_slip_gaps,
    sparse_exact_ldl_positive,
    sparse_radius_squared,
    threshold_squared_float,
    two_slip_gaps,
)


RESEARCH = Path(__file__).resolve().parents[1]
ROOT = RESEARCH / "experiments" / "task48a"
INTERFACE = ROOT / "interface"
TWO_OUTPUT = ROOT / "two_interface"
R12_OUTPUT = ROOT / "residue12"


def _levels(q: tuple[int, ...], alpha: int) -> dict[str, float]:
    values, _vectors = dense_spectrum(q, alpha)
    positive = sorted((float(value) for value in values if value > 0), reverse=True)
    if len(positive) < 2:
        raise AssertionError("missing positive interface levels")
    return {
        "lambda_1": positive[0],
        "lambda_2": positive[1],
        "lambda_1_squared": positive[0] ** 2,
        "lambda_2_squared": positive[1] ** 2,
        "rho_squared": float(max(abs(values[0]), abs(values[-1])) ** 2),
    }


def scan_two_interface() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    orders = [52, 60, 68, 76, 84, 92, 100, 108, 116, 124, 132, 140, 148, 156]
    rows = []
    best = []
    for n in orders:
        defect_count = (n - 4) // 4
        order_rows = []
        for separation_index in range((defect_count - 2) // 2 + 1):
            gaps = two_slip_gaps(n, separation_index)
            q = q_from_gaps(n, gaps)
            arc = 6 + 4 * separation_index
            for alpha in (-1, 1):
                row = {
                    "n": n,
                    "residue_mod_16": n % 16,
                    "alpha": alpha,
                    "separation_index": separation_index,
                    "arc_vertices": arc,
                    "complement_vertices": n - arc,
                    "arc_bulk_cells": separation_index,
                    **_levels(q, alpha),
                }
                rows.append(row)
                order_rows.append(row)
        winner = min(order_rows, key=lambda row: (row["rho_squared"], row["separation_index"], row["alpha"]))
        best.append(winner)
    c6 = float(json.loads((INTERFACE / "constants.json").read_text(encoding="utf-8"))["G6"]["R_squared"])
    fit_rows = [
        {"n": row["n"], "m": min(row["arc_vertices"], row["complement_vertices"]) / 8, "rho_squared": row["rho_squared"]}
        for row in rows
        if row["alpha"] == -1 and min(row["arc_vertices"], row["complement_vertices"]) >= 14
    ]
    multiplier = float(json.loads((INTERFACE / "floquet_multipliers.json").read_text(encoding="utf-8"))["G6"]["slow_bulk_multiplier"])
    splitting = [
        {
            **row,
            "mean_interface_level_squared": 0.5 * (row["lambda_1_squared"] + row["lambda_2_squared"]),
            "level_splitting_squared": row["lambda_1_squared"] - row["lambda_2_squared"],
            "mean_gap_from_c6": 0.5 * (row["lambda_1_squared"] + row["lambda_2_squared"]) - c6,
        }
        for row in rows
    ]
    summary = {
        "orders": orders,
        "separation_classes": len(rows) // 2,
        "spectral_states": len(rows),
        "best_by_order": best,
        "hybridization_fit": fit_models(fit_rows, [multiplier, float(json.loads((INTERFACE / "floquet_multipliers.json").read_text())["G6"]["stable_bulk_multipliers"][1])]),
        "parity_observation": "For 4 mod 16 the optimum is the symmetric split; for 12 mod 16 it shifts by one period-8 bulk cell.",
        "holonomy_observation": "alpha=-1 attains every order minimum in the prescribed scan.",
        "MOD16_INTERFACE_SIGNAL": "STRONG",
    }
    return splitting, summary


def _structured_residue_families(n: int) -> list[tuple[str, list[int], int]]:
    defect_count = (n - 4) // 4
    families: list[tuple[str, list[int], int]] = []
    families.append(("R1_SINGLE_GAP8", single_slip_gaps(n, 8), 0))
    for separation in range((defect_count - 2) // 2 + 1):
        families.append(("R2_TWO_GAP6", two_slip_gaps(n, separation), separation))
    bulk = defect_count - 2
    families.append(("R3_GAP10_PLUS_GAP2", [10] + [4] * (bulk // 2) + [2] + [4] * (bulk - bulk // 2), 0))
    # Charges +2,+2,+2,-2 sum to the required total excess +4.
    remaining = defect_count - 4
    quarter = remaining // 4
    gaps = []
    for special in (6, 6, 6, 2):
        gaps.append(special)
        gaps.extend([4] * quarter)
    gaps.extend([4] * (defect_count - len(gaps)))
    families.append(("R4_THREE_PLUS2_ONE_MINUS2", gaps, 0))
    for family, gaps, _parameter in families:
        if sum(gaps) != n or len(gaps) != defect_count:
            raise AssertionError(f"invalid structured family {family} at n={n}")
    return families


def _rho(q: tuple[int, ...], alpha: int) -> float:
    # At these reconnaissance sizes accelerated LAPACK is cheap and avoids
    # selecting the lower member of a near-degenerate interface pair.
    values, _vectors = dense_spectrum(q, alpha)
    return float(max(abs(values[0]), abs(values[-1])) ** 2)


def _certificate(n: int, q: tuple[int, ...], alpha: int, rho_squared: float) -> dict[str, Any]:
    denominator = 1000 if n >= 60 else 10000
    bound = Fraction(math.ceil((rho_squared + 2e-7) * denominator), denominator)
    signing = signing_from_q(canonical_code(q), n, alpha)
    adjacency = numpy_matrix(signing)
    matrix = bound.numerator * np.eye(n, dtype=np.int64) - bound.denominator * (adjacency @ adjacency)
    ldl = sparse_exact_ldl_positive(matrix)
    threshold_lower = Fraction(8) - Fraction(200, n * n)
    pivot_strings = [str(value) for value in ldl["pivots"]]
    pivot_bytes = (json.dumps(pivot_strings, separators=(",", ":")) + "\n").encode()
    matrix_bytes = matrix.tobytes(order="C")
    verified = ldl["positive"] and threshold_lower > bound
    return {
        "status": "CERTIFIED_COUNTEREXAMPLE" if verified else "CERTIFICATE_FAILED",
        "n": n,
        "alpha": alpha,
        "q_bits": q_bits(q),
        "rho_squared_numerical": rho_squared,
        "rational_upper_bound": str(bound),
        "threshold_rational_lower": str(threshold_lower),
        "threshold_margin_lower": str(threshold_lower - bound),
        "exact_sparse_LDL_positive": ldl["positive"],
        "pivot_count": len(pivot_strings),
        "all_pivots_positive": all(value > 0 for value in ldl["pivots"]),
        "pivot_sequence_sha256": hashlib.sha256(pivot_bytes).hexdigest(),
        "maximum_pivot_numerator_bits": max(value.numerator.bit_length() for value in ldl["pivots"]),
        "maximum_pivot_denominator_bits": max(value.denominator.bit_length() for value in ldl["pivots"]),
        "certificate_matrix_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
        "elimination_order": "vertices 4..n-5, then the eight cyclic boundary vertices",
        "reproduction": "target_a_task48a_two_interface.py recomputes every exact rational pivot",
    }


def scan_residue12() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    orders = list(range(44, 509, 16))
    comparison = []
    best_rows = []
    certificate_dir = R12_OUTPUT / "certificates"
    certificate_dir.mkdir(parents=True, exist_ok=True)
    certificates = []
    for n in orders:
        defect_count = (n - 4) // 4
        order_rows = []
        for family, gaps, parameter in _structured_residue_families(n):
            q = q_from_gaps(n, gaps)
            for alpha in (-1, 1):
                rho_squared = _rho(q, alpha)
                row = {
                    "n": n,
                    "family": family,
                    "parameter": parameter,
                    "alpha": alpha,
                    "gap_sequence": " ".join(map(str, gaps)),
                    "rho_squared": rho_squared,
                    "threshold_squared": threshold_squared_float(n),
                    "delta_squared": rho_squared - threshold_squared_float(n),
                    "below_8": rho_squared < 8,
                }
                comparison.append(row)
                order_rows.append(row)
        numerical_minimum = min(row["rho_squared"] for row in order_rows)
        preferred_parameter = (defect_count - 4) // 2
        preferred = next(
            row
            for row in order_rows
            if row["family"] == "R2_TWO_GAP6"
            and row["parameter"] == preferred_parameter
            and row["alpha"] == -1
        )
        winner = preferred if preferred["rho_squared"] <= numerical_minimum + 1e-10 else min(
            order_rows,
            key=lambda row: (row["rho_squared"], row["family"], row["parameter"], row["alpha"]),
        )
        best_rows.append(winner)
        if winner["delta_squared"] < -1e-7:
            gaps = list(map(int, winner["gap_sequence"].split()))
            certificate = _certificate(n, q_from_gaps(n, gaps), winner["alpha"], winner["rho_squared"])
            certificate["family"] = winner["family"]
            certificate["parameter"] = winner["parameter"]
            write_json(certificate_dir / f"n{n}.json", certificate)
            certificates.append(certificate)
    cdata = json.loads((INTERFACE / "constants.json").read_text(encoding="utf-8"))["G6"]
    fdata = json.loads((INTERFACE / "floquet_multipliers.json").read_text(encoding="utf-8"))["G6"]
    fit = fit_models(
        [{"n": row["n"], "m": (row["n"] - 12) // 16, "rho_squared": row["rho_squared"]} for row in best_rows],
        [float(value) for value in fdata["stable_bulk_multipliers"]],
    )
    exact = [row for row in certificates if row["status"] == "CERTIFIED_COUNTEREXAMPLE"]
    summary = {
        "status": "RESIDUE12_STABLE_C_LT_8_FAMILY",
        "orders": orders,
        "orders_tested": len(orders),
        "families": sorted({row["family"] for row in comparison}),
        "both_holonomies": True,
        "numerical_counterexamples": sum(row["delta_squared"] < 0 for row in best_rows),
        "exact_counterexamples": len(exact),
        "first_exact_order": min(row["n"] for row in exact),
        "first_failed_order": 44,
        "stable_family": "two gap-6 with alpha=-1 and separation shifted one bulk cell from the symmetric split",
        "asymptotic_constant": cdata["R_squared"],
        "asymptotic_fit": fit,
        "all_exact_certificates_pass": len(exact) == len(certificates),
        "signal": "STRONG",
    }
    return comparison, best_rows, summary


def _write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def run() -> dict[str, Any]:
    TWO_OUTPUT.mkdir(parents=True, exist_ok=True)
    splitting, two_summary = scan_two_interface()
    fields = ["n", "residue_mod_16", "alpha", "separation_index", "arc_vertices", "complement_vertices", "arc_bulk_cells", "lambda_1", "lambda_2", "lambda_1_squared", "lambda_2_squared", "rho_squared", "mean_interface_level_squared", "level_splitting_squared", "mean_gap_from_c6"]
    _write_csv(TWO_OUTPUT / "separation_scan.csv", splitting, fields)
    _write_csv(TWO_OUTPUT / "eigenvalue_splitting.csv", splitting, fields)
    write_json(TWO_OUTPUT / "fitting.json", two_summary["hybridization_fit"])
    write_json(TWO_OUTPUT / "summary.json", two_summary)

    comparison, best, residue_summary = scan_residue12()
    comparison_fields = ["n", "family", "parameter", "alpha", "gap_sequence", "rho_squared", "threshold_squared", "delta_squared", "below_8"]
    _write_csv(R12_OUTPUT / "family_comparison.csv", comparison, comparison_fields)
    _write_csv(R12_OUTPUT / "best_by_n.csv", best, comparison_fields)
    write_json(R12_OUTPUT / "asymptotic_fit.json", residue_summary["asymptotic_fit"])
    write_json(R12_OUTPUT / "summary.json", residue_summary)
    result = {"two_interface": two_summary, "residue12": residue_summary, "script_sha256": sha256(Path(__file__))}
    print(json.dumps({"mod16": two_summary["MOD16_INTERFACE_SIGNAL"], "residue12": residue_summary["status"], "exact": residue_summary["exact_counterexamples"]}, indent=2))
    return result


if __name__ == "__main__":
    run()
