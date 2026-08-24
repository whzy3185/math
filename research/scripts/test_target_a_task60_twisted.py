"""Tests for Task 60.1 twisted-candidate formulas."""

import math

import pytest

from target_a_task60_twisted import (
    angle_numerator_grid,
    even_chord_asymptotic_coefficients,
    optimized_squared_radius,
    s3_continuous_maximum,
    sector_squared_radius,
)
from verify_target_a_task60_twisted import (
    adjacency,
    identity,
    multiply,
    predicted,
    verify,
)
from verify_target_a_task60_twisted_symbolic import verify as verify_symbolic


def test_independent_exact_verifier() -> None:
    result = verify()
    assert result["exact_checks"] > 100
    assert result["lift_checks"] == 2 * result["exact_checks"]
    assert result["flat_checks"] == 9
    assert result["tamper_checks"] == 1


def test_symbolic_verifier_and_tamper() -> None:
    result = verify_symbolic()
    assert result == {
        "polynomial_checks": 9,
        "s3_checks": 2,
        "asymptotic_checks": 1,
    }
    with pytest.raises(AssertionError):
        verify_symbolic(tamper=True)


def test_allowed_fourier_grids() -> None:
    assert angle_numerator_grid(12, 1) == [0, 2, 4, 6, 8, 10]
    assert angle_numerator_grid(12, -1) == [1, 3, 5, 7, 9, 11]


def test_s2_regression_formula() -> None:
    for order in range(8, 32, 2):
        expected = (
            4
            + 2 * math.cos(2 * math.pi / order)
            + 2 * math.cos(4 * math.pi / order)
        )
        assert sector_squared_radius(order, 2, -1) == pytest.approx(expected)


def test_even_s_periodic_and_antiperiodic_dichotomy() -> None:
    assert sector_squared_radius(20, 4, 1) == pytest.approx(8.0)
    assert sector_squared_radius(20, 4, -1) < 8.0
    assert optimized_squared_radius(20, 4)[0] == -1


def test_odd_s_has_no_uniform_best_holonomy() -> None:
    assert sector_squared_radius(8, 3, 1) == pytest.approx(4.0)
    assert sector_squared_radius(8, 3, -1) > 4.0
    assert sector_squared_radius(12, 3, -1) < sector_squared_radius(12, 3, 1)
    assert sector_squared_radius(18, 3, 1) < sector_squared_radius(18, 3, -1)


def test_special_flat_collision() -> None:
    for chord in range(2, 9):
        order = 2 * chord + 2
        alpha = -((-1) ** chord)
        assert predicted(order, chord, alpha) == identity(order, 4)


def test_two_alternating_lifts_have_same_square() -> None:
    for anchor in (-1, 1):
        matrix = adjacency(16, 5, anchor, -1)
        assert multiply(matrix, matrix) == predicted(16, 5, -1)


def test_s3_continuous_maximum() -> None:
    expected = 4 + 16 * math.sqrt(3) / 9
    assert s3_continuous_maximum() == pytest.approx(expected)


def test_even_asymptotic_coefficients() -> None:
    second, fourth = even_chord_asymptotic_coefficients(4)
    assert second == pytest.approx(-68 * math.pi**2)
    assert fourth == pytest.approx((4 / 3) * 257 * math.pi**4)
    with pytest.raises(ValueError):
        even_chord_asymptotic_coefficients(3)


def test_wrong_parity_sign_is_detected() -> None:
    matrix = adjacency(14, 5, 1, -1)
    assert multiply(matrix, matrix) != predicted(
        14, 5, -1, wrong_parity_sign=True
    )
