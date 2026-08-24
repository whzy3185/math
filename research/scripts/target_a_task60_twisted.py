"""Exact formulas and bounded numerical evaluation for Task 60.1."""

from __future__ import annotations

import math


def validate_twisted_parameters(order: int, chord: int) -> None:
    if order % 2:
        raise ValueError("Q=-1 requires even order")
    if not 2 <= chord < order / 2:
        raise ValueError("require 2 <= s < N/2")


def angle_numerator_grid(order: int, holonomy: int) -> list[int]:
    """Represent theta=(numerator*pi)/N on one period of the dispersion."""
    if holonomy not in (-1, 1):
        raise ValueError("holonomy must be +/-1")
    offset = 0 if holonomy == 1 else 1
    return [2 * k + offset for k in range(order // 2)]


def dispersion(theta: float, chord: int) -> float:
    return (
        4.0
        + 2.0 * math.cos(2.0 * theta)
        + 2.0 * ((-1) ** chord) * math.cos(2.0 * chord * theta)
    )


def sector_squared_radius(order: int, chord: int, holonomy: int) -> float:
    validate_twisted_parameters(order, chord)
    return max(
        dispersion(numerator * math.pi / order, chord)
        for numerator in angle_numerator_grid(order, holonomy)
    )


def optimized_squared_radius(order: int, chord: int) -> tuple[int, float]:
    values = {
        alpha: sector_squared_radius(order, chord, alpha)
        for alpha in (-1, 1)
    }
    alpha = min(values, key=lambda value: (values[value], value))
    return alpha, values[alpha]


def even_chord_asymptotic_coefficients(chord: int) -> tuple[float, float]:
    if chord % 2:
        raise ValueError("even-chord expansion requested for odd s")
    second = -4.0 * math.pi**2 * (1 + chord**2)
    fourth = (4.0 / 3.0) * math.pi**4 * (1 + chord**4)
    return second, fourth


def s3_continuous_maximum() -> float:
    return 4.0 + 16.0 / (3.0 * math.sqrt(3.0))
