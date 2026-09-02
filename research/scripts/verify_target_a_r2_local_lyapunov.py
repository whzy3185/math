"""Exact local data checks for the residue-two Riccati contraction lemma.

This verifier checks only rational matrix statements at the selected centre.
The neighbourhood derivative estimate is a separate hand proof recorded in
``analytic_inventory/r2_local_contraction.md``.
"""

from __future__ import annotations

from fractions import Fraction

from verify_target_a_r2_bulk_invariant_box import D, E_MINUS, E_PLUS, inverse, riccati


RADIUS = Fraction(1, 10**10)
W0 = (
    (10125, 118, 156, -171, 30, 73, -78, 64, -140, 77),
    (118, 10141, 107, -96, 39, 79, -79, 24, -32, 6),
    (156, 107, 10436, -492, 24, 151, -163, 228, -527, 307),
    (-171, -96, -492, 10588, -18, -152, 177, -266, 639, -386),
    (30, 39, 24, -18, 10014, 12, -6, 13, -27, 16),
    (73, 79, 151, -152, 12, 10132, -150, -3, 49, -54),
    (-78, -79, -163, 177, -6, -150, 10184, 12, -78, 79),
    (64, 24, 228, -266, 13, -3, 12, 10268, -641, 387),
    (-140, -32, -527, 639, -27, 49, -78, -641, 11592, -992),
    (77, 6, 307, -386, 16, -54, 79, 387, -992, 10638),
)
P0 = (
    (10766, 87, 19, 974),
    (87, 12664, 148, -2418),
    (19, 148, 10093, -25),
    (974, -2418, -25, 14009),
)
Q0 = (
    (11503, 614, 990, -1101),
    (614, 10470, 15, 113),
    (990, 15, 12299, -2632),
    (-1101, 113, -2632, 13260),
)


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def subtract(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left))] for i in range(len(left))]


def scale(value, matrix):
    return [[value * entry for entry in row] for row in matrix]


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


def phi(state):
    return riccati(riccati(state, E_PLUS), E_MINUS)


def derivative_f(state, coupling, direction):
    state_inverse = inverse(state)
    return multiply(
        transpose(coupling),
        multiply(state_inverse, multiply(direction, multiply(state_inverse, coupling))),
    )


def coordinate_matrix(matrix):
    return [matrix[i][j] for i in range(4) for j in range(i, 4)]


def jacobian(center):
    middle = riccati(center, E_PLUS)
    basis = []
    for i in range(4):
        for j in range(i, 4):
            direction = [[Fraction(0) for _ in range(4)] for _ in range(4)]
            direction[i][j] = direction[j][i] = Fraction(1)
            basis.append(direction)
    columns = [
        coordinate_matrix(
            derivative_f(middle, E_MINUS, derivative_f(center, E_PLUS, direction))
        )
        for direction in basis
    ]
    return transpose(columns)


def verify():
    center = [row[:] for row in D]
    for _ in range(12):
        center = phi(center)
    middle = riccati(center, E_PLUS)
    image = phi(center)
    residual = subtract(image, center)
    residual_squared = sum(entry * entry for row in residual for entry in row)
    identity4 = [[Fraction(i == j) for j in range(4)] for i in range(4)]
    identity10 = [[Fraction(i == j) for j in range(10)] for i in range(10)]
    weight = [[Fraction(entry, 10**4) for entry in row] for row in W0]
    response_weight = [[Fraction(entry, 10**4) for entry in row] for row in P0]
    response_dual_weight = [[Fraction(entry, 10**4) for entry in row] for row in Q0]
    derivative = jacobian(center)
    response_transfer = multiply(
        multiply(inverse(center), E_PLUS), multiply(inverse(middle), E_MINUS)
    )
    checks = {
        "center_ge_half_identity": positive_definite(subtract(center, scale(Fraction(1, 2), identity4))),
        "middle_ge_half_identity": positive_definite(subtract(middle, scale(Fraction(1, 2), identity4))),
        "weight_ge_nine_tenths_identity": positive_definite(subtract(weight, scale(Fraction(9, 10), identity10))),
        "weight_le_two_identity": positive_definite(subtract(scale(Fraction(2), identity10), weight)),
        "local_lyapunov_six_over_25": positive_definite(
            subtract(scale(Fraction(6, 25), weight), multiply(transpose(derivative), multiply(weight, derivative)))
        ),
        "residual_lt_radius_over_40": residual_squared < (RADIUS / 40) ** 2,
        "response_weight_ge_nine_tenths_identity": positive_definite(
            subtract(response_weight, scale(Fraction(9, 10), identity4))
        ),
        "response_weight_le_two_identity": positive_definite(
            subtract(scale(Fraction(2), identity4), response_weight)
        ),
        "response_transfer_two_fifths": positive_definite(
            subtract(
                scale(Fraction(2, 5), response_weight),
                multiply(transpose(response_transfer), multiply(response_weight, response_transfer)),
            )
        ),
        "response_dual_weight_ge_nine_tenths_identity": positive_definite(
            subtract(response_dual_weight, scale(Fraction(9, 10), identity4))
        ),
        "response_dual_weight_le_two_identity": positive_definite(
            subtract(scale(Fraction(2), identity4), response_dual_weight)
        ),
        "response_dual_transfer_two_fifths": positive_definite(
            subtract(
                scale(Fraction(2, 5), response_dual_weight),
                multiply(response_transfer, multiply(response_dual_weight, transpose(response_transfer))),
            )
        ),
    }
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R2_LOCAL_LYAPUNOV_DATA_PASS",
        "iterate": 12,
        "radius": str(RADIUS),
        "checks": checks,
    }


if __name__ == "__main__":
    print(verify())
