"""Focused tests for Task 58.5 Section 2."""

from verify_target_a_task585_section2 import verify


def test_section_shape() -> None:
    result = verify()
    assert result["subsections"] == 4
    assert result["section_three_page"] - result["section_two_page"] <= 4


def test_figure_shape() -> None:
    assert verify()["figure_panels"] == 2


def test_progressive_stub_budget() -> None:
    result = verify()
    assert result["baseline_draft_stubs"] == 27
    assert 0 <= result["draft_stubs"] <= result["baseline_draft_stubs"]


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
