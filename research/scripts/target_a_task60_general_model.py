"""Formal finite-ring model for signed two-generator circulants C_N(1,s)."""

from __future__ import annotations

from math import gcd


def validate_parameters(order: int, chord: int) -> None:
    if order < 5:
        raise ValueError("order must be at least 5")
    if not 2 <= chord < order / 2:
        raise ValueError("require 2 <= s < N/2")


def boundary_factor(index: int, order: int, holonomy: int) -> int:
    """Return alpha^q when index=qN+r with 0<=r<N."""
    if holonomy not in (-1, 1):
        raise ValueError("holonomy must be +/-1")
    quotient, _ = divmod(index, order)
    return 1 if holonomy == 1 or quotient % 2 == 0 else -1


def add_displacement(
    matrix: list[list[int]],
    row: int,
    displacement: int,
    coefficient: int,
    holonomy: int,
) -> None:
    order = len(matrix)
    target = row + displacement
    matrix[row][target % order] += (
        coefficient * boundary_factor(target, order, holonomy)
    )


def zero_matrix(order: int) -> list[list[int]]:
    return [[0 for _ in range(order)] for _ in range(order)]


def matmul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    order = len(left)
    product = zero_matrix(order)
    for i in range(order):
        for k, value in enumerate(left[i]):
            if value:
                for j, other in enumerate(right[k]):
                    product[i][j] += value * other
    return product


def adjacency_matrix(
    order: int, chord: int, tau: list[int], holonomy: int
) -> list[list[int]]:
    """Build A on alpha-quasiperiodic coordinates with periodic tau."""
    validate_parameters(order, chord)
    if len(tau) != order or any(value not in (-1, 1) for value in tau):
        raise ValueError("tau must be a +/-1 word of length N")
    matrix = zero_matrix(order)
    for i in range(order):
        add_displacement(matrix, i, 1, 1, holonomy)
        add_displacement(matrix, i, -1, 1, holonomy)
        add_displacement(matrix, i, chord, tau[i], holonomy)
        add_displacement(
            matrix, i, -chord, tau[(i - chord) % order], holonomy
        )
    return matrix


def squared_formula_matrix(
    order: int, chord: int, tau: list[int], holonomy: int
) -> list[list[int]]:
    """Build the path-by-path H=A^2 formula, adding collided channels."""
    validate_parameters(order, chord)
    if len(tau) != order or any(value not in (-1, 1) for value in tau):
        raise ValueError("tau must be a +/-1 word of length N")
    matrix = zero_matrix(order)
    for i in range(order):
        add_displacement(matrix, i, 0, 4, holonomy)
        add_displacement(matrix, i, 2, 1, holonomy)
        add_displacement(matrix, i, -2, 1, holonomy)
        add_displacement(
            matrix, i, 2 * chord, tau[i] * tau[(i + chord) % order],
            holonomy,
        )
        add_displacement(
            matrix, i, -2 * chord,
            tau[(i - chord) % order] * tau[(i - 2 * chord) % order],
            holonomy,
        )
        add_displacement(
            matrix, i, chord + 1, tau[i] + tau[(i + 1) % order],
            holonomy,
        )
        add_displacement(
            matrix, i, chord - 1, tau[(i - 1) % order] + tau[i],
            holonomy,
        )
        add_displacement(
            matrix, i, -(chord - 1),
            tau[(i - chord) % order] + tau[(i - chord + 1) % order],
            holonomy,
        )
        add_displacement(
            matrix, i, -(chord + 1),
            tau[(i - chord - 1) % order] + tau[(i - chord) % order],
            holonomy,
        )
    return matrix


def flux_word(tau: list[int]) -> list[int]:
    return [tau[i] * tau[(i + 1) % len(tau)] for i in range(len(tau))]


def lift_flux(flux: list[int], anchor: int = 1) -> list[int]:
    if not flux or any(value not in (-1, 1) for value in flux):
        raise ValueError("flux must be a nonempty +/-1 word")
    if anchor not in (-1, 1):
        raise ValueError("anchor must be +/-1")
    if product(flux) != 1:
        raise ValueError("cyclic flux words must have product +1")
    tau = [anchor]
    for value in flux[:-1]:
        tau.append(value * tau[-1])
    if tau[-1] * tau[0] != flux[-1]:
        raise AssertionError("cyclic lift failed")
    return tau


def product(values: list[int]) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def twisted_tau(order: int, anchor: int = 1) -> list[int]:
    if order % 2:
        raise ValueError("Q=-1 has a cyclic tau lift only for even N")
    return [anchor * (-1) ** i for i in range(order)]


def twisted_squared_formula_matrix(
    order: int, chord: int, holonomy: int
) -> list[list[int]]:
    validate_parameters(order, chord)
    if order % 2:
        raise ValueError("twisted candidate requires even N")
    epsilon = (-1) ** chord
    matrix = zero_matrix(order)
    for i in range(order):
        add_displacement(matrix, i, 0, 4, holonomy)
        add_displacement(matrix, i, 2, 1, holonomy)
        add_displacement(matrix, i, -2, 1, holonomy)
        add_displacement(matrix, i, 2 * chord, epsilon, holonomy)
        add_displacement(matrix, i, -2 * chord, epsilon, holonomy)
    return matrix


def undirected_step(step: int, order: int) -> int:
    residue = step % order
    return min(residue, (-residue) % order)


def canonical_generator(order: int, chord: int) -> int:
    """Canonical representative under explicit cyclic-group multipliers."""
    validate_parameters(order, chord)
    candidates = {undirected_step(chord, order)}
    if gcd(chord, order) == 1:
        inverse = pow(chord, -1, order)
        candidates.add(undirected_step(inverse, order))
    candidates = {value for value in candidates if 2 <= value < order / 2}
    if not candidates:
        raise AssertionError("normalized multiplier orbit left the main regime")
    return min(candidates)


def channel_collisions(order: int, chord: int) -> dict[int, list[str]]:
    validate_parameters(order, chord)
    channels = [
        (2, "+2"),
        (-2, "-2"),
        (2 * chord, "+2s"),
        (-2 * chord, "-2s"),
        (chord - 1, "+(s-1)"),
        (-(chord - 1), "-(s-1)"),
        (chord + 1, "+(s+1)"),
        (-(chord + 1), "-(s+1)"),
    ]
    classes: dict[int, list[str]] = {}
    for displacement, name in channels:
        classes.setdefault(displacement % order, []).append(name)
    return {
        residue: names for residue, names in classes.items() if len(names) > 1
    }
