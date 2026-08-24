"""Focused tests for Task 58.8 Section 5."""

from verify_target_a_task588_section5 import verify


def test_section_shape() -> None:
    result = verify()
    assert result["subsections"] == 4
    assert result["section_six_page"] - result["section_five_page"] <= 3


def test_exact_small_gap_partition() -> None:
    assert verify()["small_gap_rows"] == 6


def test_progressive_stub_budget() -> None:
    result = verify()
    assert result["baseline_draft_stubs"] == 16
    assert 0 <= result["draft_stubs"] <= result["baseline_draft_stubs"]


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
