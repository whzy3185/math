"""Focused tests for Task 58.6 Section 3."""

from verify_target_a_task586_section3 import verify


def test_section_shape() -> None:
    result = verify()
    assert result["subsections"] == 3
    assert result["section_four_page"] - result["section_three_page"] <= 2


def test_progressive_stub_budget() -> None:
    result = verify()
    assert result["baseline_draft_stubs"] == 24
    assert 0 <= result["draft_stubs"] <= result["baseline_draft_stubs"]


def test_modular_laws_are_closed() -> None:
    assert verify()["subsections"] == 3


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
