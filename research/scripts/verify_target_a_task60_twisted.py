"""Independent exact-matrix verifier for the generalized twisted candidate."""

from __future__ import annotations


def boundary(index: int, order: int, alpha: int) -> tuple[int, int]:
    quotient, residue = divmod(index, order)
    return residue, (1 if alpha == 1 or quotient % 2 == 0 else -1)


def add(
    matrix: list[list[int]],
    row: int,
    displacement: int,
    value: int,
    alpha: int,
) -> None:
    target, sign = boundary(row + displacement, len(matrix), alpha)
    matrix[row][target] += sign * value


def adjacency(order: int, chord: int, anchor: int, alpha: int) -> list[list[int]]:
    tau = [anchor * (-1) ** i for i in range(order)]
    matrix = [[0] * order for _ in range(order)]
    for i in range(order):
        add(matrix, i, 1, 1, alpha)
        add(matrix, i, -1, 1, alpha)
        add(matrix, i, chord, tau[i], alpha)
        add(matrix, i, -chord, tau[(i - chord) % order], alpha)
    return matrix


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    order = len(left)
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(order))
            for j in range(order)
        ]
        for i in range(order)
    ]


def predicted(
    order: int,
    chord: int,
    alpha: int,
    *,
    wrong_parity_sign: bool = False,
) -> list[list[int]]:
    epsilon = (-1) ** chord
    if wrong_parity_sign:
        epsilon = -epsilon
    matrix = [[0] * order for _ in range(order)]
    for i in range(order):
        for displacement, value in (
            (0, 4),
            (2, 1),
            (-2, 1),
            (2 * chord, epsilon),
            (-2 * chord, epsilon),
        ):
            add(matrix, i, displacement, value, alpha)
    return matrix


def identity(order: int, scale: int = 1) -> list[list[int]]:
    return [
        [scale if i == j else 0 for j in range(order)]
        for i in range(order)
    ]


def verify() -> dict[str, int]:
    exact_checks = 0
    lift_checks = 0
    for chord in range(2, 11):
        first_order = 2 * chord + 2
        for order in range(first_order, 4 * chord + 10, 2):
            for alpha in (-1, 1):
                target = predicted(order, chord, alpha)
                for anchor in (-1, 1):
                    matrix = adjacency(order, chord, anchor, alpha)
                    if multiply(matrix, matrix) != target:
                        raise AssertionError(
                            f"twisted identity failed at N={order}, s={chord}"
                        )
                    lift_checks += 1
                exact_checks += 1

    flat_checks = 0
    for chord in range(2, 11):
        order = 2 * chord + 2
        alpha = -((-1) ** chord)
        if predicted(order, chord, alpha) != identity(order, 4):
            raise AssertionError(f"flat collision failed at s={chord}")
        flat_checks += 1

    sample = multiply(adjacency(14, 5, 1, -1), adjacency(14, 5, 1, -1))
    if sample == predicted(14, 5, -1, wrong_parity_sign=True):
        raise AssertionError("parity-sign tamper was not detected")

    return {
        "exact_checks": exact_checks,
        "lift_checks": lift_checks,
        "flat_checks": flat_checks,
        "tamper_checks": 1,
    }


if __name__ == "__main__":
    result = verify()
    print(
        "TARGET_A_TASK60_TWISTED_PASS "
        f"exact={result['exact_checks']} lifts={result['lift_checks']} "
        f"flat={result['flat_checks']} tamper={result['tamper_checks']}"
    )
