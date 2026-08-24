"""Focused tests for Task 58.11 submission artifacts."""

from verify_target_a_task5811_package import verify


def test_page_gate() -> None:
    result = verify()
    assert result["main_pages"] <= 45
    assert result["anonymous_pages"] <= 45
    assert result["supplement_pages"] > 0


def test_figure_and_draft_gate() -> None:
    result = verify()
    assert result["main_figures"] == 3
    assert result["draft_stubs"] == 0
    assert result["author_footnotes"] == 0


def test_archive_status() -> None:
    assert verify()["archive_status"] == "IMMUTABLE_ARCHIVE_PENDING"


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
