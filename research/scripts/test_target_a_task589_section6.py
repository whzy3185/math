"""Focused tests for Task 58.9 Section 6."""

from verify_target_a_task589_section6 import verify


def test_section_shape() -> None:
    result = verify()
    assert result["subsections"] == 5
    assert result["section_seven_page"] - result["section_six_page"] <= 5


def test_two_core_figures() -> None:
    assert verify()["figures"] == 2


def test_progressive_stub_budget() -> None:
    result = verify()
    assert result["baseline_draft_stubs"] == 9
    assert 0 <= result["draft_stubs"] <= result["baseline_draft_stubs"]


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
