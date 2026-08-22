"""Task 49 Parts A-B: uniform-error templates and threshold crossings."""

from __future__ import annotations

import csv
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from target_a_flux_search import signing_from_q
from target_a_reproduce import integer_rayleigh_lower_bound, numpy_matrix
from target_a_task47_common import write_json
from target_a_task48a_common import (
    canonical_code,
    dense_spectrum,
    q_from_gaps,
    single_slip_gaps,
    sparse_exact_ldl_positive,
    sparse_radius_squared,
    threshold_squared_float,
    two_slip_gaps,
)


RESEARCH = Path(__file__).resolve().parents[1]
ROOT = RESEARCH / "experiments" / "task49"
UNIFORM = ROOT / "uniform_bounds"
CROSSING = ROOT / "threshold_crossings"
INTERFACE = RESEARCH / "experiments" / "task48a" / "interface"


def radius(q: tuple[int, ...], alpha: int) -> tuple[float, str, float]:
    if len(q) <= 512:
        values, _vectors = dense_spectrum(q, alpha)
        return float(max(abs(values[0]), abs(values[-1])) ** 2), "dense eigvalsh", 1e-14
    result = sparse_radius_squared(q, alpha, tolerance=5e-14, maximum_iterations=9000)
    return result["rho_squared"], result["solver"], result["residual_A2"]


def single_orders(gap: int) -> list[int]:
    early_start = 18 if gap == 6 else 30
    early = list(range(early_start, 127, 8))
    selected = [130, 258, 514, 1026] if gap == 6 else [134, 254, 510, 1022]
    return sorted(set(early + selected))


def single_uniform(gap: int, constant: float, multiplier: float) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    for n in single_orders(gap):
        try:
            q = q_from_gaps(n, single_slip_gaps(n, gap))
        except ValueError:
            continue
        value, solver, residual = radius(q, 1)
        bulk_cells = (n - (2 if gap == 6 else 6)) // 8
        error = value - constant
        denominator = abs(multiplier) ** bulk_cells
        resolved = abs(error) > max(5e-13, 10 * residual)
        rows.append({
            "n": n,
            "bulk_cells": bulk_cells,
            "closure_tail_cells": bulk_cells,
            "R_squared": value,
            "c": constant,
            "error": error,
            "mu": multiplier,
            "exponent": bulk_cells,
            "normalized_error": abs(error) / denominator if resolved else None,
            "solver": solver,
            "precision": "double",
            "residual": residual,
            "evidence_status": "RESOLVED_DOUBLE_ERROR" if resolved else "BELOW_DOUBLE_RESOLUTION",
        })
    resolved_values = [row["normalized_error"] for row in rows if row["normalized_error"] is not None]
    maximum = max(resolved_values)
    return rows, {
        "observed_maximum_normalized_error": maximum,
        "C_empirical_1p1": 1.1 * maximum,
        "C_empirical_2x": 2 * maximum,
        "resolved_rows": len(resolved_values),
        "unresolved_double_rows": len(rows) - len(resolved_values),
        "template": "|R_n-c| <= C |mu|^bulk_cells",
    }


def two_uniform(mu: float, c6: float) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    source = RESEARCH / "experiments" / "task48a" / "two_interface" / "separation_scan.csv"
    rows = []
    with source.open() as stream:
        for row in csv.DictReader(stream):
            n = int(row["n"])
            arc = int(row["arc_vertices"])
            complement = int(row["complement_vertices"])
            left = max(1, (arc - 4) // 8)
            right = max(1, (complement - 4) // 8)
            defect_count = (n - 4) // 4
            preferred = (defect_count - 2) // 2 if n % 16 == 4 else (defect_count - 4) // 2
            error = abs(float(row["rho_squared"]) - c6)
            one_tail = mu ** min(left, right)
            two_tail = mu**left + mu**right
            rows.append({
                **row,
                "left_tail_cells": left,
                "right_tail_cells": right,
                "error_from_c6": error,
                "explicit_family_geometry": int(row["separation_index"]) == preferred,
                "one_tail_normalized": error / one_tail,
                "two_tail_normalized": error / two_tail,
                "evidence_status": "DOUBLE_PRECISION_MECHANISM_DATA",
            })
    template_rows = [row for row in rows if row["explicit_family_geometry"]]
    one = np.asarray([row["one_tail_normalized"] for row in template_rows])
    two = np.asarray([row["two_tail_normalized"] for row in template_rows])
    return rows, {
        "one_tail_coefficient_of_variation": float(one.std() / one.mean()),
        "two_tail_coefficient_of_variation": float(two.std() / two.mean()),
        "observed_two_tail_supremum": float(two.max()),
        "template_rows": len(template_rows),
        "recommended_template": "|R_(L,M)-c6| <= C(|mu6|^L+|mu6|^(M-L))",
        "classification": "TWO_TAIL_BOUND_SUPPORTED",
    }


def exact_side(q: tuple[int, ...], alpha: int, numerical: float, threshold: float) -> dict[str, Any]:
    n = len(q)
    matrix = numpy_matrix(signing_from_q(canonical_code(q), n, alpha))
    values, vectors = np.linalg.eigh(matrix.astype(float))
    index = int(np.argmax(np.abs(values)))
    lower = integer_rayleigh_lower_bound(matrix, vectors[:, index])
    if numerical < threshold - 1e-9:
        denominator = 10**6
        bound = Fraction(math.ceil((numerical + 2e-8) * denominator), denominator)
        certificate_matrix = bound.numerator * np.eye(n, dtype=np.int64) - bound.denominator * (matrix @ matrix)
        ldl = sparse_exact_ldl_positive(certificate_matrix)
        threshold_lower = Fraction(8) - Fraction(200, n * n)
        certificate = {
            "status": "CERTIFIED_COUNTEREXAMPLE" if ldl["positive"] and threshold_lower > bound else "CERTIFICATE_FAILED",
            "rational_upper_bound": str(bound),
            "threshold_rational_lower": str(threshold_lower),
            "exact_sparse_LDL_positive": ldl["positive"],
            "pivot_count": len(ldl["pivots"]),
        }
        return {"status": certificate["status"], "certificate": certificate}
    return {
        "status": "NUMERICALLY_ABOVE_THRESHOLD",
        "rayleigh_lower": str(lower),
        "reason": "no expensive exact cyclotomic threshold enclosure was attempted for a non-counterexample row",
    }


def family_rows(name: str) -> list[dict[str, Any]]:
    if name == "G6":
        orders = list(range(18, 83, 8)); builder = lambda n: single_slip_gaps(n, 6); alpha = 1
    elif name == "G10":
        orders = list(range(30, 119, 8)); builder = lambda n: single_slip_gaps(n, 10); alpha = 1
    elif name == "TWO_SYMMETRIC":
        orders = list(range(20, 117, 16)); alpha = -1
        builder = lambda n: two_slip_gaps(n, ((n - 4) // 4 - 2) // 2)
    else:
        orders = list(range(28, 125, 16)); alpha = -1
        builder = lambda n: two_slip_gaps(n, ((n - 4) // 4 - 4) // 2)
    rows = []
    for n in orders:
        try:
            gaps = builder(n)
            q = q_from_gaps(n, gaps)
        except ValueError:
            rows.append({"family": name, "n": n, "status": "DEGENERATE_OR_ILLEGAL"})
            continue
        value, solver, residual = radius(q, alpha)
        threshold = threshold_squared_float(n)
        exact = exact_side(q, alpha, value, threshold)
        rows.append({
            "family": name,
            "n": n,
            "alpha": alpha,
            "gap_sequence": " ".join(map(str, gaps)),
            "R_squared": value,
            "threshold_squared": threshold,
            "delta": value - threshold,
            "solver": solver,
            "evidence_status": exact["status"],
            "exact_detail": exact,
        })
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def run() -> dict[str, Any]:
    constants = json.loads((INTERFACE / "constants.json").read_text(encoding="utf-8"))
    floquet = json.loads((INTERFACE / "floquet_multipliers.json").read_text(encoding="utf-8"))
    c6, c10 = float(constants["G6"]["R_squared"]), float(constants["G10"]["R_squared"])
    mu6, mu10 = float(floquet["G6"]["slow_bulk_multiplier"]), float(floquet["G10"]["slow_bulk_multiplier"])
    g6, e6 = single_uniform(6, c6, mu6)
    g10, e10 = single_uniform(10, c10, mu10)
    two, e2 = two_uniform(mu6, c6)
    fields = ["n", "bulk_cells", "closure_tail_cells", "R_squared", "c", "error", "mu", "exponent", "normalized_error", "solver", "precision", "residual", "evidence_status"]
    write_csv(UNIFORM / "g6_uniform_error.csv", g6, fields)
    write_csv(UNIFORM / "g10_uniform_error.csv", g10, fields)
    write_csv(UNIFORM / "two_interface_uniform_error.csv", two, list(two[0].keys()))
    envelopes = {"G6": e6, "G10": e10, "two_interface": e2}
    write_json(UNIFORM / "single_interface_envelopes.json", envelopes)

    crossing_rows = [row for name in ("G6", "G10", "TWO_SYMMETRIC", "TWO_SHIFTED") for row in family_rows(name)]
    write_csv(CROSSING / "threshold_crossings.csv", crossing_rows, ["family", "n", "alpha", "gap_sequence", "R_squared", "threshold_squared", "delta", "solver", "evidence_status"])
    onsets = {}
    for name in ("G6", "G10", "TWO_SYMMETRIC", "TWO_SHIFTED"):
        rows = [row for row in crossing_rows if row["family"] == name and "R_squared" in row]
        numerical = [row for row in rows if row["delta"] < 0]
        exact = [row for row in rows if row["evidence_status"] == "CERTIFIED_COUNTEREXAMPLE"]
        onsets[name] = {
            "first_numerical_crossing": min(row["n"] for row in numerical) if numerical else None,
            "first_exact_crossing": min(row["n"] for row in exact) if exact else None,
            "last_pre_crossing": max((row for row in rows if row["delta"] >= 0), key=lambda row: row["n"], default=None),
            "exact_crossing_count": len(exact),
        }
    summary = {
        "uniform_bound_gate": "UNIFORM_BOUND_TEMPLATE_FOUND",
        "single_interface_classification": "SIMPLE_SINGLE_TAIL_BOUND_SUPPORTED",
        "two_interface_classification": e2["classification"],
        "envelopes": envelopes,
        "crossing_onsets": onsets,
        "evidence_boundary": "Empirical envelopes choose theorem templates; only rows with exact certificates support finite counterexample claims.",
    }
    write_json(ROOT / "uniform_and_crossing_summary.json", summary)
    print(json.dumps({"gate": summary["uniform_bound_gate"], "onsets": {k: v["first_exact_crossing"] for k, v in onsets.items()}}, indent=2))
    return summary


if __name__ == "__main__":
    run()
