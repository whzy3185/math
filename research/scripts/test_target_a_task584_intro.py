"""Focused tests for the Task 58.4 abstract and Introduction."""

from verify_target_a_task584_intro import verify


def test_abstract_contract() -> None:
    result = verify()
    assert 150 <= result["abstract_words"] <= 190
    assert result["abstract_sentences"] == 6


def test_introduction_contract() -> None:
    result = verify()
    assert result["introduction_paragraphs"] == 11
    assert result["introduction_theorems"] == 2


def test_page_and_stub_budgets() -> None:
    result = verify()
    assert result["section_two_page"] <= 5
    assert result["baseline_draft_stubs"] == 32
    assert 0 <= result["draft_stubs"] <= result["baseline_draft_stubs"]


def test_manuscript_freezes() -> None:
    assert verify()["historical_trees_frozen"]
