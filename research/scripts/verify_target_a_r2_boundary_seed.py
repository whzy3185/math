"""Exact finite seed for the residue-two boundary-core closure programme."""

from __future__ import annotations

from fractions import Fraction

import verify_target_a_r2_schur_reduction as reduction


SEED_ORDER = 410


def positive_definite(matrix):
    active = [row[:] for row in matrix]
    for pivot_index in range(len(active)):
        pivot = active[pivot_index][pivot_index]
        if pivot <= 0:
            return False
        for row in range(pivot_index + 1, len(active)):
            for column in range(row, len(active)):
                active[row][column] = active[column][row] = (
                    active[row][column]
                    - active[row][pivot_index]
                    * active[pivot_index][column]
                    / pivot
                )
    return True


def final_boundary_core(n):
    matrix = reduction._matrix(n)
    state = reduction._submatrix(matrix, list(range(12)))
    front = 4
    while front < n - 8:
        _, state = reduction._bulk_step(state, matrix, front)
        front += 1
    for _ in range(4):
        _, state = reduction._eliminate_first(state, 4)
    return state


def verify():
    core = final_boundary_core(SEED_ORDER)
    shifted = [
        [core[i][j] - (Fraction(9, 20) if i == j else 0) for j in range(8)]
        for i in range(8)
    ]
    checks = {
        "seed_has_residue_two": SEED_ORDER % 8 == 2,
        "core_dimension": len(core) == 8 and all(len(row) == 8 for row in core),
        "core_minus_nine_twentieths_identity_positive": positive_definite(shifted),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R2_BOUNDARY_SEED_PASS",
        "order": SEED_ORDER,
        "margin": "S_410 - 9/20 I is positive definite",
        "checks": checks,
    }


if __name__ == "__main__":
    print(verify())
