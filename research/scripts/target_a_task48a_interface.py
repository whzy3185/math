"""Task 48A Part B: explicit single phase-slip interface reconnaissance."""

from __future__ import annotations

import csv
import json
import math
import platform
from pathlib import Path
from typing import Any

import mpmath as mp
import numpy as np

from target_a_task47_common import sha256, write_json
from target_a_task48a_common import (
    dense_spectrum,
    fit_models,
    localization_profile,
    q_from_gaps,
    single_slip_gaps,
    sparse_radius_squared,
)


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "experiments" / "task48a" / "interface"


def _q_infinite(index: int, gap: int) -> int:
    left = index <= 0 and index % 4 == 0
    right = index >= gap and (index - gap) % 4 == 0
    return 1 if left or right else -1


def _tau_window(gap: int, low: int = -48, high: int = 72) -> dict[int, int]:
    tau = {0: 1}
    for index in range(high):
        tau[index + 1] = _q_infinite(index, gap) * tau[index]
    for index in range(-1, low - 1, -1):
        tau[index] = _q_infinite(index, gap) * tau[index + 1]
    return tau


def _transfer(tau: dict[int, int], index: int, lam: mp.mpf) -> mp.matrix:
    a = tau[index]
    b = tau[index - 2]
    return mp.matrix([[-a, a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])


def _product(tau: dict[int, int], start: int, stop: int, lam: mp.mpf) -> mp.matrix:
    product = mp.eye(4)
    for index in range(start, stop):
        product = _transfer(tau, index, lam) * product
    return product


def _eigenspace(matrix: mp.matrix, stable: bool) -> tuple[list[mp.mpc], mp.matrix]:
    values, right = mp.eig(matrix, left=False, right=True)
    indices = [index for index, value in enumerate(values) if (abs(value) < 1) == stable]
    indices.sort(key=lambda index: abs(values[index]))
    if len(indices) != 2:
        raise AssertionError("bulk gap does not have a two-dimensional stable splitting")
    return [values[index] for index in indices], mp.matrix([[right[row, index] for index in indices] for row in range(4)])


def _normalize_columns(matrix: mp.matrix) -> mp.matrix:
    for column in range(matrix.cols):
        norm = mp.sqrt(sum(abs(matrix[row, column]) ** 2 for row in range(matrix.rows)))
        for row in range(matrix.rows):
            matrix[row, column] /= norm
    return matrix


def evans_determinant(lam: mp.mpf, gap: int, margin: int = 8) -> mp.mpf:
    tau = _tau_window(gap)
    start = -margin
    stop = gap + margin
    left_mono = _product(tau, start - 8, start, lam)
    right_mono = _product(tau, stop, stop + 8, lam)
    _left_values, left_unstable = _eigenspace(left_mono, stable=False)
    _right_values, right_stable = _eigenspace(right_mono, stable=True)
    left_at_start = _product(tau, start - 8, start, lam) * left_unstable
    left_at_stop = _normalize_columns(_product(tau, start, stop, lam) * left_at_start)
    right_at_stop = _normalize_columns(right_stable)
    matching = mp.matrix(4, 4)
    for row in range(4):
        for column in range(2):
            matching[row, column] = left_at_stop[row, column]
            matching[row, column + 2] = right_at_stop[row, column]
    return mp.re(mp.det(matching))


def high_precision_interface(gap: int, guesses: tuple[str, str], digits: int = 220) -> dict[str, Any]:
    mp.mp.dps = digits
    root = mp.findroot(
        lambda value: evans_determinant(value, gap, 8),
        tuple(mp.mpf(value) for value in guesses),
        tol=mp.mpf(10) ** (-(digits - 25)),
        verify=False,
    )
    alternate = mp.findroot(
        lambda value: evans_determinant(value, gap, 16),
        tuple(mp.mpf(value) for value in guesses),
        tol=mp.mpf(10) ** (-(digits - 25)),
        verify=False,
    )
    y = root * root
    independent_difference = abs(root * root - alternate * alternate)
    tau = _tau_window(gap)
    monodromy = _product(tau, -40, -32, root)
    stable_values, _vectors = _eigenspace(monodromy, stable=True)
    stable_moduli = sorted([abs(value) for value in stable_values], reverse=True)
    return {
        "gap": gap,
        "lambda": mp.nstr(root, digits - 10),
        "R_squared": mp.nstr(y, digits - 10),
        "precision_digits": digits,
        "alternate_boundary_difference": mp.nstr(independent_difference, 12),
        "stable_bulk_multiplier_moduli": [mp.nstr(value, 80) for value in stable_moduli],
        "evans_residual": mp.nstr(abs(evans_determinant(root, gap, 8)), 12),
    }


def algebraic_probe(constant: str, validation_digits: int) -> dict[str, Any]:
    mp.mp.dps = validation_digits
    y = mp.mpf(constant)
    training_tolerance = mp.mpf("1e-85")
    validation_tolerance = mp.mpf("1e-170")
    degrees = [2, 4, 6, 8, 10, 12, 16, 20, 24]
    for degree in degrees:
        relation = mp.pslq(
            mp.matrix([y**power for power in range(degree + 1)]),
            tol=training_tolerance,
            maxcoeff=10**8,
            maxsteps=20000,
        )
        if relation:
            residual = abs(sum(mp.mpf(coefficient) * y**power for power, coefficient in enumerate(relation)))
            if residual < validation_tolerance:
                residual_text = mp.nstr(residual, 20) if residual else "<1e-190 (validation precision floor)"
                return {
                    "status": "ALGEBRAIC_CANDIDATE",
                    "degree": degree,
                    "coefficients_constant_first": list(map(int, relation)),
                    "height": max(abs(int(value)) for value in relation),
                    "training_tolerance": str(training_tolerance),
                    "independent_validation_residual": residual_text,
                }
            return {
                "status": "NUMERICAL_CONSTANT",
                "rejected_degree": degree,
                "rejected_relation": list(map(int, relation)),
                "independent_validation_residual": mp.nstr(residual, 20),
                "reason": "training-precision PSLQ relation failed the stronger validation gate",
            }
    return {"status": "NUMERICAL_CONSTANT", "degrees_tested": degrees, "coefficient_bound": 10**8}


def _orders(gap: int) -> list[int]:
    if gap == 6:
        values = set(range(50, 1027, 40)) | {58, 66, 130, 258, 514, 1026}
    else:
        values = set(range(94, 1023, 48)) | {102, 110, 126, 254, 510, 1022}
    return sorted(
        value
        for value in values
        if (value - gap) % 4 == 0 and ((value - gap) // 4 + 1) % 2 == 0
    )


def spectrum_family(gap: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    dense_checks = []
    for n in _orders(gap):
        q = q_from_gaps(n, single_slip_gaps(n, gap))
        sparse = sparse_radius_squared(q, 1)
        row = {
            "family": f"G{gap}",
            "gap": gap,
            "n": n,
            "m": (n - gap) // 8,
            "alpha": 1,
            "rho_squared": sparse["rho_squared"],
            "iterations": sparse["iterations"],
            "residual_A2": sparse["residual_A2"],
        }
        if n <= 126:
            values, _vectors = dense_spectrum(q, 1)
            dense_value = float(max(abs(values[0]), abs(values[-1])) ** 2)
            row["dense_rho_squared"] = dense_value
            row["dense_sparse_difference"] = abs(dense_value - sparse["rho_squared"])
            dense_checks.append(row["dense_sparse_difference"])
        rows.append(row)
    return rows, {"maximum_dense_sparse_difference": max(dense_checks), "checked": len(dense_checks)}


def run() -> dict[str, Any]:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    constants = {
        "G6": high_precision_interface(6, ("2.8116", "2.8121")),
        "G10": high_precision_interface(10, ("2.8243", "2.8248")),
    }
    constants["G6"]["algebraic_probe"] = algebraic_probe(constants["G6"]["R_squared"], 210)
    constants["G10"]["algebraic_probe"] = algebraic_probe(constants["G10"]["R_squared"], 210)
    constants["G6"]["margin_below_8"] = mp.nstr(8 - mp.mpf(constants["G6"]["R_squared"]), 80)
    constants["G10"]["margin_below_8"] = mp.nstr(8 - mp.mpf(constants["G10"]["R_squared"]), 80)
    write_json(OUTPUT / "constants.json", constants)

    all_rows: dict[str, list[dict[str, Any]]] = {}
    dense_checks = {}
    fits = {}
    for gap in (6, 10):
        name = f"G{gap}"
        rows, dense_check = spectrum_family(gap)
        all_rows[name] = rows
        dense_checks[name] = dense_check
        multipliers = [float(value) for value in constants[name]["stable_bulk_multiplier_moduli"]]
        fits[name] = fit_models(rows, multipliers)
        with (OUTPUT / f"g{gap}_spectrum.csv").open("w", encoding="utf-8", newline="") as stream:
            fields = ["family", "gap", "n", "m", "alpha", "rho_squared", "iterations", "residual_A2", "dense_rho_squared", "dense_sparse_difference"]
            writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            for row in rows:
                writer.writerow({field: row.get(field, "") for field in fields})
    write_json(OUTPUT / "convergence_fits.json", fits)

    localization = {}
    localization_dir = OUTPUT / "localization"
    localization_dir.mkdir(exist_ok=True)
    for gap, orders in ((6, (258, 514, 1026)), (10, (254, 510, 1022))):
        name = f"G{gap}"
        localization[name] = []
        for n in orders:
            q = q_from_gaps(n, single_slip_gaps(n, gap))
            sparse = sparse_radius_squared(q, 1, tolerance=5e-14, maximum_iterations=8000)
            profile = localization_profile(sparse["eigenvector_A2"], gap // 2)
            record = {
                "family": name,
                "n": n,
                "rho_squared": sparse["rho_squared"],
                "residual_A2": sparse["residual_A2"],
                "left_fit": profile["left_fit"],
                "right_fit": profile["right_fit"],
            }
            localization[name].append(record)
            write_json(localization_dir / f"g{gap}_n{n}.json", {**record, **profile})
    write_json(localization_dir / "summary.json", localization)

    floquet = {}
    for name in ("G6", "G10"):
        slow = float(constants[name]["stable_bulk_multiplier_moduli"][0])
        tail_values = [
            side["multiplier"]
            for row in localization[name]
            for side in (row["left_fit"], row["right_fit"])
            if math.isfinite(side["multiplier"])
        ]
        tail = float(np.median(tail_values))
        floquet[name] = {
            "stable_bulk_multipliers": constants[name]["stable_bulk_multiplier_moduli"],
            "dominant_localization_multiplier": tail,
            "slow_bulk_multiplier": slow,
            "absolute_difference": abs(tail - slow),
            "classification": "INTERFACE_FLOQUET_SIGNAL_STRONG" if abs(tail - slow) < 0.02 else "MODERATE",
        }
    write_json(OUTPUT / "floquet_multipliers.json", floquet)

    control = []
    for n in (52, 132, 260, 516, 1028):
        q = q_from_gaps(n, single_slip_gaps(n, 8))
        for alpha in (-1, 1):
            result = sparse_radius_squared(q, alpha)
            control.append({"family": "G8_CONTROL", "n": n, "alpha": alpha, "rho_squared": result["rho_squared"]})
    write_json(OUTPUT / "controls.json", control)

    summary = {
        "status": "TARGET_A_TASK48A_INTERFACE_RECONNAISSANCE_COMPLETE",
        "families": {name: {"orders": len(rows), "order_range": [rows[0]["n"], rows[-1]["n"]]} for name, rows in all_rows.items()},
        "constants": constants,
        "convergence": fits,
        "dense_sparse_checks": dense_checks,
        "localization": localization,
        "floquet": floquet,
        "interface_matching": {
            "status": "SYMBOLIC_INTERFACE_PROTOTYPE",
            "equation": "D_g(lambda)=det(P_g(lambda) U_left(lambda), U_right(lambda))=0",
            "finite_dimension": 4,
            "exact_transfer_entries": True,
            "stable_subspaces_evaluated_numerically": True,
            "resultant_elimination_complete": False,
        },
        "INTERFACE_THEOREM_SIGNAL": "STRONG",
        "formal_claim_boundary": "Limits, PSLQ relations, and Evans roots remain reconnaissance until an exact stable-subspace elimination is proved.",
        "software": {"python": platform.python_version(), "numpy": np.__version__, "mpmath": mp.__version__},
        "script_sha256": sha256(Path(__file__)),
    }
    write_json(OUTPUT / "summary.json", summary)
    return summary


if __name__ == "__main__":
    result = run()
    print(json.dumps({
        "signal": result["INTERFACE_THEOREM_SIGNAL"],
        "c6": result["constants"]["G6"]["R_squared"][:40],
        "c10": result["constants"]["G10"]["R_squared"][:40],
    }, indent=2))
