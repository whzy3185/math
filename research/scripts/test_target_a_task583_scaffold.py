"""Focused tests for the Task 58.3 scaffold audit."""

from verify_target_a_task583_scaffold import verify


def test_scaffold_shape() -> None:
    result = verify()
    assert result["numbered_sections"] == 8
    assert result["appendices"] == 2


def test_visual_budget() -> None:
    assert verify()["figure_sources"] == 3


def test_stub_baseline() -> None:
    result = verify()
    assert result["baseline_draft_stubs"] == 34
    assert 0 <= result["draft_stubs"] <= result["baseline_draft_stubs"]


def test_freezes_and_build() -> None:
    result = verify()
    assert result["compiled_pdf"]
    assert result["historical_trees_frozen"]
