"""Focused tests for the Task 58.13 final audit."""

from verify_target_a_task5813_final_audit import verify


def test_final_page_inventory() -> None:
    result = verify()
    assert (result["main_pages"], result["anonymous_pages"],
            result["supplement_pages"]) == (38, 38, 13)


def test_final_hard_gates() -> None:
    result = verify()
    assert result["figures"] == 3
    assert result["stubs"] == 0
    assert result["footnotes"] == 0


def test_truthful_external_status() -> None:
    result = verify()
    assert result["archive_status"] == "IMMUTABLE_ARCHIVE_PENDING"
    assert result["author_metadata"] == "PENDING_USER_METADATA"
    assert result["verdict"] == "ANONYMOUS_REVIEW_PACKAGE_READY"


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
