"""Focused tests for Task 58.10 Section 7."""

from verify_target_a_task5810_section7 import verify


def test_section_shape() -> None:
    result = verify()
    assert result["subsections"] == 5
    assert result["section_eight_page"] - result["section_seven_page"] <= 6


def test_finite_counts() -> None:
    result = verify()
    assert result["terminal_records"] == 64
    assert result["bridge_orders"] == 96


def test_progressive_stub_budget() -> None:
    result = verify()
    assert result["baseline_draft_stubs"] == 4
    assert 0 <= result["draft_stubs"] <= result["baseline_draft_stubs"]


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
