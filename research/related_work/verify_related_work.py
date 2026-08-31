"""Fail-closed integrity checks for the selected related-work library."""

from __future__ import annotations

import json
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
LIBRARY = ROOT / "bibliography/core_library.json"
NOTES = ROOT / "notes"
REPORTS = ROOT / "reports"
PAPERS = ROOT / "papers"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify() -> dict[str, int]:
    rows = json.loads(LIBRARY.read_text(encoding="utf-8"))
    require(len(rows) == 13, "core library must contain exactly 13 records")
    tiers = {}
    for row in rows:
        tiers[row["tier"]] = tiers.get(row["tier"], 0) + 1
    require(tiers == {"S": 3, "S-PREPRINT": 1, "A": 7, "HISTORICAL": 2},
            f"unexpected tier counts: {tiers}")

    sa_ids = {row["id"] for row in rows if row["tier"] in {"S", "S-PREPRINT", "A"}}
    note_ids = {
        path.name.split("_", 1)[0]
        for path in NOTES.glob("*.md")
        if path.name.split("_", 1)[0] in sa_ids
    }
    require(note_ids == sa_ids, "every S/A entry must have an architecture note")

    pdfs = list(PAPERS.rglob("*.pdf"))
    require(len(pdfs) == 10, f"expected 10 lawful local PDFs, found {len(pdfs)}")
    for path in pdfs:
        require(path.read_bytes()[:5] == b"%PDF-", f"not a PDF: {path.name}")
        require(len(PdfReader(path).pages) > 0, f"empty PDF: {path.name}")
        require(path.with_suffix(".md").is_file(),
                f"missing adjacent note: {path.name}")

    for path in (
        ROOT / "README.md",
        ROOT / "bibliography/access_status.md",
        ROOT / "bibliography/sources.md",
        ROOT / "citation_graph/candidate_chain.md",
        ROOT / "citation_graph/relationship_data.json",
        REPORTS / "seed_audit.md",
        REPORTS / "venue_architecture.md",
        REPORTS / "current_reference_audit.md",
        REPORTS / "new_related_work_structure.md",
        REPORTS / "final_literature_report.md",
        REPORTS / "literature_review.md",
    ):
        require(path.is_file() and path.stat().st_size > 300,
                f"missing or stubbed artifact: {path.relative_to(ROOT)}")

    final = (REPORTS / "final_literature_report.md").read_text(encoding="utf-8")
    require("No NOVELTY_ALERT is warranted." in final,
            "novelty verdict is missing or changed")
    require("Suvagiya" in final and "preprint" in final,
            "direct preprint status must remain visible")
    return {"records": len(rows), "notes": len(note_ids), "pdfs": len(pdfs)}


if __name__ == "__main__":
    result = verify()
    print(
        "RELATED_WORK_LIBRARY_PASS "
        f"records={result['records']} notes={result['notes']} pdfs={result['pdfs']}"
    )
