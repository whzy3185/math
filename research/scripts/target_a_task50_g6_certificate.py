"""Rigorous G6 Evans zero certificate using exact rational intervals."""

from __future__ import annotations

import itertools
import json
import platform
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp

from target_a_task47_common import write_json
from target_a_task50_interval import Dual, Interval, dual_sqrt, interval_record


RESEARCH = Path(__file__).resolve().parents[1]
OUTPUT = RESEARCH / "proofs" / "task50" / "certificates"
GAP = 6
Y_LEFT = Fraction(7905369311620327, 10**15)
Y_RIGHT = Fraction(7905369311620328, 10**15)


def q_infinite(index: int, gap: int) -> int:
    left = index <= 0 and index % 4 == 0
    right = index >= gap and (index - gap) % 4 == 0
    return 1 if left or right else -1


def tau_window(gap: int, low: int = -32, high: int = 40) -> dict[int, int]:
    tau = {0: 1}
    for index in range(high):
        tau[index + 1] = q_infinite(index, gap) * tau[index]
    for index in range(-1, low - 1, -1):
        tau[index] = q_infinite(index, gap) * tau[index + 1]
    return tau


def identity(size: int) -> list[list[Dual]]:
    return [[Dual.constant(int(row == column)) for column in range(size)] for row in range(size)]


def matrix_multiply(left: list[list[Dual]], right: list[list[Dual]]) -> list[list[Dual]]:
    return [
        [sum((left[row][k] * right[k][column] for k in range(len(right))), Dual.constant(0)) for column in range(len(right[0]))]
        for row in range(len(left))
    ]


def matrix_vector(matrix: list[list[Dual]], vector: list[Dual]) -> list[Dual]:
    return [sum((entry * value for entry, value in zip(row, vector)), Dual.constant(0)) for row in matrix]


def determinant(matrix: list[list[Dual]]) -> Dual:
    size = len(matrix)
    result = Dual.constant(0)
    for permutation in itertools.permutations(range(size)):
        inversions = sum(permutation[i] > permutation[j] for i in range(size) for j in range(i + 1, size))
        term = Dual.constant(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term = term * matrix[row][column]
        result = result + term
    return result


def transfer(tau: dict[int, int], index: int, lam: Dual) -> list[list[Dual]]:
    a = tau[index]
    b = tau[index - 2]
    return [
        [-a, a * lam, -a, -a * b],
        [Dual.constant(1), Dual.constant(0), Dual.constant(0), Dual.constant(0)],
        [Dual.constant(0), Dual.constant(1), Dual.constant(0), Dual.constant(0)],
        [Dual.constant(0), Dual.constant(0), Dual.constant(1), Dual.constant(0)],
    ]


def product(tau: dict[int, int], start: int, stop: int, lam: Dual) -> list[list[Dual]]:
    result = identity(4)
    for index in range(start, stop):
        result = matrix_multiply(transfer(tau, index, lam), result)
    return result


def cofactor_eigenvector(
    matrix: list[list[Dual]], eigenvalue: Dual, rows: tuple[int, int, int] = (0, 1, 2)
) -> list[Dual]:
    shifted = [[matrix[row][column] - (eigenvalue if row == column else 0) for column in range(4)] for row in range(4)]
    vector = []
    for excluded in range(4):
        minor = [[shifted[row][column] for column in range(4) if column != excluded] for row in rows]
        vector.append(((-1) ** excluded) * determinant(minor))
    return vector


def evans(
    y_interval: Interval,
    gap: int = GAP,
    cofactor_rows: tuple[int, int, int] = (0, 1, 2),
) -> tuple[Dual, list[list[Dual]], dict[str, Any]]:
    y = Dual.variable(y_interval)
    lam = dual_sqrt(y)
    tau = tau_window(gap)
    start = -8
    stop = gap + 8
    left = product(tau, start - 8, start, lam)
    right = product(tau, stop, stop + 8, lam)
    defect = product(tau, start, stop, lam)

    h = 2 * y**2 - 16 * y + 13
    disc = -12 * y**2 + 96 * y + 17
    root_disc = dual_sqrt(disc)
    w_minus = (h - root_disc) / 2
    w_plus = (h + root_disc) / 2
    stable = [(w - dual_sqrt(w**2 - 4)) / 2 for w in (w_minus, w_plus)]
    unstable = [1 / value for value in stable]
    left_vectors = [cofactor_eigenvector(left, value, cofactor_rows) for value in unstable]
    right_vectors = [cofactor_eigenvector(right, value, cofactor_rows) for value in stable]
    propagated = [matrix_vector(defect, vector) for vector in left_vectors]
    matching = [[propagated[column][row] for column in range(2)] + [right_vectors[column][row] for column in range(2)] for row in range(4)]
    value = determinant(matching)
    pivots = []
    for label, vector in zip(("left_w_minus", "left_w_plus", "right_w_minus", "right_w_plus"), left_vectors + right_vectors):
        valid = [index for index, component in enumerate(vector) if component.value.excludes_zero()]
        pivots.append({"vector": label, "nonzero_components": valid})
    metadata = {
        "cofactor_rows": list(cofactor_rows),
        "stable_multiplier_intervals": [interval_record(value.value) for value in stable],
        "unstable_multiplier_intervals": [interval_record(value.value) for value in unstable],
        "cofactor_pivots": pivots,
    }
    return value, defect, metadata


def symbolic_defect_transfer(gap: int = GAP) -> dict[str, Any]:
    lam = sp.symbols("lambda")
    tau = tau_window(gap)
    result = sp.eye(4)
    for index in range(-8, gap + 8):
        a = tau[index]
        b = tau[index - 2]
        step = sp.Matrix([[-a, a * lam, -a, -a * b], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
        result = step * result
    result = result.applyfunc(sp.expand)
    return {
        "gap": gap,
        "cut": [-8, gap + 8],
        "orientation": "left defects at 4Z through 0; right defects at gap+4Z from gap onward",
        "tau": {str(index): tau[index] for index in range(-10, gap + 10)},
        "entries": [[str(result[row, column]) for column in range(4)] for row in range(4)],
        "determinant": str(sp.factor(result.det())),
    }


def run() -> dict[str, Any]:
    interval = Interval(Y_LEFT, Y_RIGHT)
    left_value, _left_defect, left_meta = evans(Interval.point(Y_LEFT))
    right_value, _right_defect, right_meta = evans(Interval.point(Y_RIGHT))
    enclosure, _defect, interval_meta = evans(interval)
    checks = {
        "ordered_rational_interval": Y_LEFT < Y_RIGHT,
        "inside_bulk_G6_interval": Fraction(1581, 200) < Y_LEFT < Y_RIGHT < Fraction(3953, 500),
        "left_sign_negative": left_value.value.sign() == -1,
        "right_sign_positive": right_value.value.sign() == 1,
        "derivative_positive": enclosure.derivative.lo > 0,
        "all_cofactor_vectors_nonzero": all(row["nonzero_components"] for row in interval_meta["cofactor_pivots"]),
        "upper_endpoint_below_8": Y_RIGHT < 8,
    }
    if not all(checks.values()):
        raise AssertionError(f"G6 interval Evans certificate failed: {checks}")
    symbolic = symbolic_defect_transfer()
    if symbolic["determinant"] != "1":
        raise AssertionError("G6 defect transfer is not unimodular")
    payload = {
        "status": "G6_INTERFACE_THEOREM_PROVED",
        "method": "exact rational interval Evans determinant with automatic derivative enclosure",
        "arithmetic": {
            "rational_endpoints": True,
            "sqrt_outward_decimal_digits": 120,
            "python": platform.python_version(),
            "sympy": sp.__version__,
        },
        "y_interval": [str(Y_LEFT), str(Y_RIGHT)],
        "left_evans": interval_record(left_value.value),
        "right_evans": interval_record(right_value.value),
        "derivative_on_interval": interval_record(enclosure.derivative),
        "interval_metadata": interval_meta,
        "endpoint_metadata": {"left": left_meta, "right": right_meta},
        "checks": checks,
        "localization": {
            "bulk_cell_rate": "9/25",
            "statement": "the matched state decays by at most C*(9/25)^|j| in period-eight bulk cells",
        },
        "defect_transfer": symbolic,
        "proof_boundary": "Existence and simplicity use IVT plus a strictly positive interval derivative; no floating value or empirical constant enters acceptance.",
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_json(OUTPUT / "g6_defect_transfer.json", symbolic)
    write_json(OUTPUT / "g6_interface_certificate.json", payload)
    print(json.dumps({
        "status": payload["status"],
        "interval": payload["y_interval"],
        "left_sign": left_value.value.sign(),
        "right_sign": right_value.value.sign(),
        "derivative_sign": enclosure.derivative.sign(),
    }, indent=2))
    return payload


if __name__ == "__main__":
    run()
