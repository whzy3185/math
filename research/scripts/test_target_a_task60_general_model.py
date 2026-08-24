"""Tests for the Task 60 formal model and independent verifier."""

from itertools import product

import pytest

from target_a_task60_general_model import (
    adjacency_matrix,
    canonical_generator,
    channel_collisions,
    flux_word,
    lift_flux,
    matmul,
    squared_formula_matrix,
    twisted_squared_formula_matrix,
    twisted_tau,
)
from verify_target_a_task60_general_model import (
    direct_adjacency,
    predicted_square,
    square,
    verify,
)


def test_independent_verifier() -> None:
    result = verify()
    assert result["general_checks"] == 288
    assert result["twisted_checks"] > 100
    assert result["tamper_checks"] == 1


@pytest.mark.parametrize(
    ("order", "chord"), [(5, 2), (8, 3), (10, 4), (12, 5), (14, 6)]
)
def test_exhaustive_small_words(order: int, chord: int) -> None:
    for tau in product((-1, 1), repeat=order):
        if order > 10 and tau[0:4] != (-1, -1, -1, -1):
            continue
        for alpha in (-1, 1):
            matrix = adjacency_matrix(order, chord, list(tau), alpha)
            assert matmul(matrix, matrix) == squared_formula_matrix(
                order, chord, list(tau), alpha
            )


def test_flux_lifts_are_exactly_two() -> None:
    flux = [-1, -1, 1, -1, 1, 1, -1, 1]
    positive = lift_flux(flux, 1)
    negative = lift_flux(flux, -1)
    assert flux_word(positive) == flux
    assert flux_word(negative) == flux
    assert negative == [-value for value in positive]


def test_invalid_flux_lift_is_rejected() -> None:
    with pytest.raises(ValueError):
        lift_flux([-1, 1, 1])


def test_twisted_formula_and_odd_order_obstruction() -> None:
    tau = twisted_tau(14, -1)
    direct = matmul(
        adjacency_matrix(14, 5, tau, -1),
        adjacency_matrix(14, 5, tau, -1),
    )
    assert direct == twisted_squared_formula_matrix(14, 5, -1)
    with pytest.raises(ValueError):
        twisted_tau(13)


def test_canonical_multiplier_orbit() -> None:
    assert canonical_generator(13, 2) == 2
    assert canonical_generator(13, 5) == 5
    assert canonical_generator(17, 7) == 5


def test_collision_classes_cover_generic_and_modular_exceptions() -> None:
    assert channel_collisions(11, 3) == {2: ["+2", "+(s-1)"],
                                         9: ["-2", "-(s-1)"]}
    assert any(len(names) >= 2 for names in channel_collisions(10, 4).values())


def test_tampered_coefficient_fails() -> None:
    tau = tuple(1 if i % 2 else -1 for i in range(9))
    direct = square(direct_adjacency(9, 3, tau, 1))
    assert direct != predicted_square(9, 3, tau, 1, tamper=True)
