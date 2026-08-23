"""Tests for the independent Task 56 single-gap checker."""

from __future__ import annotations

import pytest

from verify_target_a_task56_single_gap import (
    SMALL_CASES,
    TAIL_VECTOR,
    exact_image,
    verify,
    verify_case,
)


def test_checker_passes() -> None:
    assert all(verify().values())


@pytest.mark.parametrize("gap", sorted(SMALL_CASES))
def test_small_case_vector_tamper_fails(gap: int) -> None:
    low, vector, denominator, numerator = SMALL_CASES[gap]
    changed = (vector[0] + 1,) + vector[1:]
    with pytest.raises(AssertionError):
        verify_case(gap, low, changed, denominator, numerator)


def test_gap_tamper_fails() -> None:
    low, vector, denominator, numerator = SMALL_CASES[3]
    with pytest.raises(AssertionError):
        verify_case(4, low, vector, denominator, numerator)


def test_numerator_tamper_fails() -> None:
    low, vector, denominator, numerator = SMALL_CASES[8]
    with pytest.raises(AssertionError):
        verify_case(8, low, vector, denominator, numerator + 1)


def test_denominator_tamper_fails() -> None:
    with pytest.raises(AssertionError):
        verify_case(11, -2, TAIL_VECTOR, 390, 3094)


def test_tail_locality_boundary() -> None:
    assert exact_image(10, -2, TAIL_VECTOR) != exact_image(11, -2, TAIL_VECTOR)
    assert exact_image(11, -2, TAIL_VECTOR) == exact_image(1000, -2, TAIL_VECTOR)
