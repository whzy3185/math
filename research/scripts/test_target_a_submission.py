"""Focused tests for the Target A submission entry point."""

from verify_target_a_submission import verify


def test_submission_scope_and_literature() -> None:
    result = verify()
    assert result["citations"] >= 18
    assert result["labels"] > 100


def test_submission_manifest_contract() -> None:
    result = verify()
    assert result["families"] == 7
    assert result["certificates"] == 12


def test_submission_pdf_inventory() -> None:
    pages = verify()["pages"]
    assert pages["main"] >= 30
    assert pages["anonymous"] == pages["main"]
    assert pages["supplement"] >= 10
    assert pages["supplement_anonymous"] == pages["supplement"]


def test_submission_status_is_truthful() -> None:
    assert verify()["verdict"] == (
        "SUBMISSION_READY_MODULO_AUTHOR_METADATA_AND_ARCHIVE"
    )
