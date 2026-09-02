"""Exact block-response recurrence for the residue-two cyclic Schur core."""

from __future__ import annotations

from fractions import Fraction

import verify_target_a_r2_schur_reduction as reduction


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def add(left, right):
    return [[left[i][j] + right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def subtract(left, right):
    return [[left[i][j] - right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def inverse(matrix):
    size = len(matrix)
    active = [row[:] + [Fraction(i == j) for j in range(size)] for i, row in enumerate(matrix)]
    for pivot_index in range(size):
        pivot = active[pivot_index][pivot_index]
        if pivot == 0:
            raise AssertionError("singular response pivot")
        for column in range(2 * size):
            active[pivot_index][column] /= pivot
        for row in range(size):
            if row != pivot_index:
                factor = active[row][pivot_index]
                for column in range(2 * size):
                    active[row][column] -= factor * active[pivot_index][column]
    return [row[size:] for row in active]


def block_response_core(n):
    matrix = reduction._matrix(n)
    block_count = (n - 2) // 4
    blocks = [[0, 1]] + [list(range(2 + 4 * j, 6 + 4 * j)) for j in range(block_count)]

    def block(i, j):
        return [[matrix[row][column] / 25 for column in blocks[j]] for row in blocks[i]]

    g = block(0, 0)
    h = block(block_count, block_count)
    c = block(0, block_count)
    response_left = block(0, 1)
    response_right = block(1, block_count)
    pivot = block(1, 1)

    for index in range(1, block_count):
        coupling = block(index, index + 1)
        # The physical last edge is not part of the propagated response.
        if index == block_count - 1:
            response_right = add(response_right, coupling)
        pivot_inverse = inverse(pivot)
        g = subtract(g, multiply(response_left, multiply(pivot_inverse, transpose(response_left))))
        h = subtract(h, multiply(transpose(response_right), multiply(pivot_inverse, response_right)))
        c = subtract(c, multiply(response_left, multiply(pivot_inverse, response_right)))
        if index < block_count - 1:
            response_left = [[-entry for entry in row] for row in multiply(response_left, multiply(pivot_inverse, coupling))]
            response_right = [[-entry for entry in row] for row in multiply(transpose(coupling), multiply(pivot_inverse, response_right))]
            pivot = subtract(block(index + 1, index + 1), multiply(transpose(coupling), multiply(pivot_inverse, coupling)))

    return [g[i] + c[i] for i in range(2)] + [transpose(c)[i] + h[i] for i in range(4)]


def direct_core(n):
    matrix = reduction._matrix(n)
    block_count = (n - 2) // 4
    blocks = [[0, 1]] + [list(range(2 + 4 * j, 6 + 4 * j)) for j in range(block_count)]
    interior = [vertex for index in range(1, block_count) for vertex in blocks[index]]
    order = interior + blocks[0] + blocks[block_count]
    active = [[matrix[i][j] / 25 for j in order] for i in order]
    for pivot_index in range(len(interior)):
        pivot = active[pivot_index][pivot_index]
        if pivot == 0:
            raise AssertionError("singular direct pivot")
        for row in range(pivot_index + 1, len(active)):
            for column in range(row, len(active)):
                active[row][column] = active[column][row] = (
                    active[row][column]
                    - active[row][pivot_index]
                    * active[pivot_index][column]
                    / pivot
                )
    return [row[len(interior):] for row in active[len(interior):]]


def verify():
    orders = (50, 58, 66, 74, 82, 90)
    checks = {n: block_response_core(n) == direct_core(n) for n in orders}
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R2_RESPONSE_RECURRENCE_PASS",
        "orders": orders,
        "terminal_rule": "W_final = W_propagated + E_terminal",
        "checks": checks,
    }


if __name__ == "__main__":
    print(verify())
