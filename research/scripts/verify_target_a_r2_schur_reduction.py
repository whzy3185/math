"""Exact fixed-width Schur reduction for the residue-two one-G6 family."""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from target_a_flux_search import signing_from_q
from target_a_reproduce import numpy_matrix
from target_a_task48a_common import canonical_code, q_from_gaps
from target_a_task54_threshold import gap_word


CAP_NUMERATOR = 198
CAP_DENOMINATOR = 25


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def _matrix(n: int) -> list[list[Fraction]]:
    family, gaps = gap_word(n)
    _require(family == "ONE_G6" and n % 8 == 2, "wrong residue-two family")
    q = q_from_gaps(n, gaps)
    adjacency = numpy_matrix(
        signing_from_q(canonical_code(q), n, 1)
    ).astype(np.int64)
    square = adjacency @ adjacency
    return [
        [Fraction(CAP_NUMERATOR if i == j else 0) - CAP_DENOMINATOR * int(square[i, j]) for j in range(n)]
        for i in range(n)
    ]


def _submatrix(matrix: list[list[Fraction]], indices: list[int]) -> list[list[Fraction]]:
    return [[matrix[i][j] for j in indices] for i in indices]


def _eliminate_first(matrix: list[list[Fraction]], pivot_index: int = 0) -> tuple[Fraction, list[list[Fraction]]]:
    pivot = matrix[pivot_index][pivot_index]
    rest = [index for index in range(len(matrix)) if index != pivot_index]
    reduced = [
        [
            matrix[i][j] - matrix[i][pivot_index] * matrix[pivot_index][j] / pivot
            for j in rest
        ]
        for i in rest
    ]
    return pivot, reduced


def _positive_ldl(matrix: list[list[Fraction]]) -> bool:
    active = matrix
    while active:
        pivot, active = _eliminate_first(active)
        if pivot <= 0:
            return False
    return True


def _bulk_step(
    state: list[list[Fraction]], matrix: list[list[Fraction]], front: int
) -> tuple[Fraction, list[list[Fraction]]]:
    """Eliminate `front` while retaining four left and eight forward sites."""
    pivot = state[4][4]
    rest = list(range(4)) + list(range(5, 12))
    reduced = [
        [state[i][j] - state[i][4] * state[4][j] / pivot for j in rest]
        for i in rest
    ]
    new_site = front + 8
    retained_sites = list(range(4)) + list(range(front + 1, front + 8))
    next_state = [[Fraction(0) for _ in range(12)] for _ in range(12)]
    for i in range(11):
        for j in range(11):
            next_state[i][j] = reduced[i][j]
    for i, site in enumerate(retained_sites):
        next_state[i][11] = next_state[11][i] = matrix[site][new_site]
    next_state[11][11] = matrix[new_site][new_site]
    return pivot, next_state


def _full_ldl_positive(matrix: list[list[Fraction]], n: int) -> bool:
    boundary = 4
    order = list(range(boundary, n - boundary)) + list(range(boundary)) + list(range(n - boundary, n))
    return _positive_ldl(_submatrix(matrix, order))


def reduce(n: int) -> dict[str, object]:
    _require(n >= 50 and n % 8 == 2, "n must be a residue-two order at least 50")
    matrix = _matrix(n)
    initial_indices = list(range(4)) + list(range(4, 12))
    state = _submatrix(matrix, initial_indices)
    front = 4
    bulk_pivots = []
    while front < n - 8:
        pivot, state = _bulk_step(state, matrix, front)
        bulk_pivots.append(pivot)
        front += 1

    tail_pivots = []
    for _ in range(4):
        pivot, state = _eliminate_first(state, 4)
        tail_pivots.append(pivot)

    recurrence_positive = all(pivot > 0 for pivot in bulk_pivots + tail_pivots) and _positive_ldl(state)
    full_positive = _full_ldl_positive(matrix, n)
    _require(recurrence_positive == full_positive, f"Schur equivalence failed at n={n}")
    return {
        "n": n,
        "bulk_step_count": len(bulk_pivots),
        "state_dimensions": {"bulk": 12, "final_boundary": 8},
        "all_bulk_pivots_positive": all(pivot > 0 for pivot in bulk_pivots),
        "all_tail_pivots_positive": all(pivot > 0 for pivot in tail_pivots),
        "final_boundary_positive": _positive_ldl(state),
        "full_matrix_positive": full_positive,
    }


def verify() -> dict[str, object]:
    rows = [reduce(n) for n in (50, 58, 66, 74, 82, 90)]
    _require(all(row["full_matrix_positive"] for row in rows), "known residue-two cap failed")
    _require([row["bulk_step_count"] for row in rows] == [38, 46, 54, 62, 70, 78], "bulk length is not affine")
    return {
        "status": "R2_FIXED_WIDTH_SCHUR_REDUCTION_PASS",
        "rows": rows,
        "bulk_period_increment": 8,
        "remaining_theorem": "construct a rational invariant domain for the repeated bulk update",
    }


if __name__ == "__main__":
    print(verify())
