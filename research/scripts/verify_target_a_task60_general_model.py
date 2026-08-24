"""Independent small-matrix verifier for the Task 60 general model."""

from __future__ import annotations

import random


def wrap(index: int, order: int, alpha: int) -> tuple[int, int]:
    quotient, residue = divmod(index, order)
    sign = 1 if alpha == 1 or quotient % 2 == 0 else -1
    return residue, sign


def direct_adjacency(
    order: int, chord: int, tau: tuple[int, ...], alpha: int
) -> list[list[int]]:
    matrix = [[0] * order for _ in range(order)]
    for i in range(order):
        for displacement, coefficient in (
            (1, 1),
            (-1, 1),
            (chord, tau[i]),
            (-chord, tau[(i - chord) % order]),
        ):
            j, boundary = wrap(i + displacement, order, alpha)
            matrix[i][j] += coefficient * boundary
    return matrix


def square(matrix: list[list[int]]) -> list[list[int]]:
    order = len(matrix)
    return [
        [
            sum(matrix[i][k] * matrix[k][j] for k in range(order))
            for j in range(order)
        ]
        for i in range(order)
    ]


def predicted_square(
    order: int,
    chord: int,
    tau: tuple[int, ...],
    alpha: int,
    *,
    tamper: bool = False,
) -> list[list[int]]:
    matrix = [[0] * order for _ in range(order)]
    for i in range(order):
        contributions = (
            (0, 4),
            (2, 1),
            (-2, 1),
            (2 * chord, tau[i] * tau[(i + chord) % order]),
            (
                -2 * chord,
                tau[(i - chord) % order] * tau[(i - 2 * chord) % order],
            ),
            (chord + 1, tau[i] + tau[(i + 1) % order]),
            (chord - 1, tau[(i - 1) % order] + tau[i]),
            (
                -(chord - 1),
                tau[(i - chord) % order] + tau[(i - chord + 1) % order],
            ),
            (
                -(chord + 1),
                tau[(i - chord - 1) % order] + tau[(i - chord) % order],
            ),
        )
        for displacement, coefficient in contributions:
            j, boundary = wrap(i + displacement, order, alpha)
            matrix[i][j] += coefficient * boundary
    if tamper:
        matrix[0][0] += 1
    return matrix


def predicted_twisted_square(
    order: int, chord: int, alpha: int
) -> list[list[int]]:
    matrix = [[0] * order for _ in range(order)]
    epsilon = -1 if chord % 2 else 1
    for i in range(order):
        for displacement, coefficient in (
            (0, 4),
            (2, 1),
            (-2, 1),
            (2 * chord, epsilon),
            (-2 * chord, epsilon),
        ):
            j, boundary = wrap(i + displacement, order, alpha)
            matrix[i][j] += coefficient * boundary
    return matrix


def verify() -> dict[str, int]:
    rng = random.Random(6001)
    cases = [
        (5, 2), (6, 2), (7, 2), (8, 3), (9, 3), (10, 4),
        (11, 3), (12, 5), (13, 4), (14, 6), (15, 5), (17, 6),
    ]
    checks = 0
    for order, chord in cases:
        for alpha in (-1, 1):
            for _ in range(12):
                tau = tuple(rng.choice((-1, 1)) for _ in range(order))
                direct = square(direct_adjacency(order, chord, tau, alpha))
                predicted = predicted_square(order, chord, tau, alpha)
                if direct != predicted:
                    raise AssertionError(
                        f"H2 mismatch for N={order}, s={chord}, alpha={alpha}"
                    )
                checks += 1

    twisted_checks = 0
    for chord in range(2, 7):
        for order in range(2 * chord + 2, 30, 2):
            for alpha in (-1, 1):
                for anchor in (-1, 1):
                    tau = tuple(anchor * (-1) ** i for i in range(order))
                    direct = square(
                        direct_adjacency(order, chord, tau, alpha)
                    )
                    predicted = predicted_twisted_square(
                        order, chord, alpha
                    )
                    if direct != predicted:
                        raise AssertionError(
                            "twisted formula mismatch for "
                            f"N={order}, s={chord}, alpha={alpha}"
                        )
                    twisted_checks += 1

    sample = tuple(1 if i % 3 else -1 for i in range(11))
    direct = square(direct_adjacency(11, 3, sample, -1))
    if direct == predicted_square(11, 3, sample, -1, tamper=True):
        raise AssertionError("tamper was not detected")

    return {
        "general_checks": checks,
        "twisted_checks": twisted_checks,
        "tamper_checks": 1,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK60_GENERAL_MODEL_PASS "
        f"general={result['general_checks']} "
        f"twisted={result['twisted_checks']} "
        f"tamper={result['tamper_checks']}"
    )
