"""Exact two-cycle Loewner invariant box for the residue-two bulk Riccati map."""

from __future__ import annotations

from fractions import Fraction


D = [[
    Fraction(98, 25) if i == j else Fraction(-1)
    if {i, j} in ({0, 2}, {1, 3}) else Fraction(0)
    for j in range(4)
] for i in range(4)]
E_PLUS = [[Fraction(x) for x in row] for row in (
    (-1, 0, 0, 0),
    (0, 1, 0, 0),
    (-1, 2, 1, 0),
    (2, -1, 0, -1),
)]
E_MINUS = [[Fraction(x) for x in row] for row in (
    (-1, 0, 0, 0),
    (0, 1, 0, 0),
    (-1, -2, 1, 0),
    (-2, -1, 0, -1),
)]

# Centers rounded to denominator 500, with a 3/100 Loewner radius.
L0 = [[Fraction(x) for x in row] for row in (
    (Fraction(1014, 500), Fraction(-551, 500), Fraction(-159, 250), Fraction(-149, 250)),
    (Fraction(-551, 500), Fraction(1126, 500), Fraction(11, 20), Fraction(-539, 500)),
    (Fraction(-159, 250), Fraction(11, 20), Fraction(1798, 500), Fraction(-1, 500)),
    (Fraction(-149, 250), Fraction(-539, 500), Fraction(-1, 500), Fraction(1709, 500)),
)]
L1 = [[Fraction(x) for x in row] for row in (
    (Fraction(1014, 500), Fraction(551, 500), Fraction(-159, 250), Fraction(149, 250)),
    (Fraction(551, 500), Fraction(1126, 500), Fraction(-11, 20), Fraction(-539, 500)),
    (Fraction(-159, 250), Fraction(-11, 20), Fraction(1798, 500), Fraction(1, 500)),
    (Fraction(149, 250), Fraction(-539, 500), Fraction(1, 500), Fraction(1709, 500)),
)]
U0 = [[entry + (Fraction(3, 50) if i == j else 0) for j, entry in enumerate(row)] for i, row in enumerate(L0)]
U1 = [[entry + (Fraction(3, 50) if i == j else 0) for j, entry in enumerate(row)] for i, row in enumerate(L1)]


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def multiply(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(left[i][k] * right[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def subtract(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[left[i][j] - right[i][j] for j in range(4)] for i in range(4)]


def inverse(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    active = [row[:] + [Fraction(i == j) for j in range(4)] for i, row in enumerate(matrix)]
    for pivot_index in range(4):
        pivot = active[pivot_index][pivot_index]
        if pivot == 0:
            raise AssertionError("singular Riccati state")
        for column in range(8):
            active[pivot_index][column] /= pivot
        for row in range(4):
            if row == pivot_index:
                continue
            coefficient = active[row][pivot_index]
            for column in range(8):
                active[row][column] -= coefficient * active[pivot_index][column]
    return [row[4:] for row in active]


def riccati(state: list[list[Fraction]], coupling: list[list[Fraction]]) -> list[list[Fraction]]:
    return subtract(D, multiply(transpose(coupling), multiply(inverse(state), coupling)))


def positive_definite(matrix: list[list[Fraction]]) -> bool:
    active = [row[:] for row in matrix]
    for pivot_index in range(4):
        pivot = active[pivot_index][pivot_index]
        if pivot <= 0:
            return False
        for row in range(pivot_index + 1, 4):
            for column in range(row, 4):
                active[row][column] = active[column][row] = (
                    active[row][column]
                    - active[row][pivot_index] * active[pivot_index][column] / pivot
                )
    return True


def between(state: list[list[Fraction]], lower: list[list[Fraction]], upper: list[list[Fraction]]) -> bool:
    return positive_definite(subtract(state, lower)) and positive_definite(subtract(upper, state))


def verify() -> dict[str, object]:
    checks = {
        "box_lower_positive": positive_definite(L0) and positive_definite(L1),
        "plus_lower": positive_definite(subtract(riccati(L0, E_PLUS), L1)),
        "plus_upper": positive_definite(subtract(U1, riccati(U0, E_PLUS))),
        "minus_lower": positive_definite(subtract(riccati(L1, E_MINUS), L0)),
        "minus_upper": positive_definite(subtract(U0, riccati(U1, E_MINUS))),
    }
    state = D
    entrance = []
    for step in range(6):
        entrance.append(between(state, L0 if step % 2 == 0 else L1, U0 if step % 2 == 0 else U1))
        state = riccati(state, E_PLUS if step % 2 == 0 else E_MINUS)
    checks["entry_after_four_steps"] = entrance == [False, False, False, False, True, True]
    if not all(checks.values()):
        raise AssertionError(checks)
    return {
        "status": "R2_BULK_INVARIANT_BOX_PASS",
        "radius": "3/100",
        "entry_steps": 4,
        "checks": checks,
        "consequence": "every subsequent alternating bulk Schur pivot is positive",
        "remaining_obligation": "uniform fixed boundary-core closure",
    }


if __name__ == "__main__":
    print(verify())
