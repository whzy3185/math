"""Exact integer checks for the finite Rayleigh table in the period-8 trichotomy."""

from __future__ import annotations


CASES = (
    (1, 1, (-1, -1, -1, -1, -1, -1, -1, -1), 72, 8),
    (2, -1, (-1, -1, -1, 0, -1, -1, -1, 1), 60, 7),
    (3, 1, (-1, -1, -1, 0, -1, -1, -1, -1), 60, 7),
)


def fiber(q, z):
    tau = [1]
    for sign in q[:-1]:
        tau.append(tau[-1] * sign)
    if tau[-1] * q[-1] != 1:
        raise AssertionError("Q word does not close")
    matrix = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for delta, coefficient in ((-2, tau[(i - 2) % 8]), (-1, 1), (1, 1), (2, tau[i])):
            target = i + delta
            residue = target % 8
            shift = (target - residue) // 8
            matrix[i][residue] += coefficient * (z ** shift)
    return matrix


def image(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(8)) for i in range(8)]


def verify():
    checks = {}
    for separation, z, vector, numerator, denominator in CASES:
        q = [-1] * 8
        q[0] = q[separation] = 1
        matrix = fiber(q, z)
        first = image(matrix, vector)
        second = image(matrix, first)
        actual_numerator = sum(vector[i] * second[i] for i in range(8))
        actual_denominator = sum(value * value for value in vector)
        checks[f"separation_{separation}"] = (
            actual_numerator == numerator
            and actual_denominator == denominator
            and actual_numerator > 8 * actual_denominator
        )
    if not all(checks.values()):
        raise AssertionError(checks)
    return {"status": "PERIOD8_TRICHOTOMY_RAYLEIGH_TABLE_PASS", "checks": checks}


if __name__ == "__main__":
    print(verify())
