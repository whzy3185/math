#!/usr/bin/env python3
"""Deterministic integrity checks for the period-eight reference library."""

from collections import Counter
import csv
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
INDEX = HERE / "MASTER_REFERENCE_INDEX.csv"
CANONICAL_BIB = HERE / "bibliography" / "manuscript_core.bib"
MANUSCRIPT = HERE.parent / "manuscript_period8_jgt"
MANUSCRIPT_BIB = MANUSCRIPT / "references.bib"
CLAIM_MAP = HERE / "CLAIM_REFERENCE_MAP.md"


def require_unique(rows, field):
    values = [row[field].strip().lower() for row in rows if row[field].strip()]
    duplicates = [value for value, count in Counter(values).items() if count > 1]
    assert not duplicates, f"duplicate {field}: {duplicates}"


def bib_keys(text):
    return set(re.findall(r"^@\w+\{([^,]+),", text, re.M))


with INDEX.open(newline="", encoding="utf-8") as stream:
    rows = list(csv.DictReader(stream))

expected_fields = {
    "id", "cite_key", "collection", "topic", "status", "year", "authors",
    "title", "venue", "volume", "issue", "pages_or_article", "doi", "arxiv",
    "local_fulltext", "manuscript_role", "decision",
}
assert set(rows[0]) == expected_fields
assert len(rows) == 30

require_unique(rows, "id")
require_unique(rows, "cite_key")
require_unique(rows, "doi")
require_unique(rows, "arxiv")

allowed_collections = {
    "manuscript_core", "specific_recent_context", "jgt_structure_corpus", "reserve"
}
assert {row["collection"] for row in rows} <= allowed_collections
assert all(row["authors"] and row["title"] and row["venue"] and row["year"] for row in rows)

citation_rows = [
    row for row in rows
    if row["collection"] in {"manuscript_core", "specific_recent_context"}
]
assert len(citation_rows) == 15
assert sum(row["collection"] == "jgt_structure_corpus" for row in rows) == 10
assert sum(row["collection"] == "reserve" for row in rows) == 5
assert all(row["cite_key"] for row in citation_rows)
assert all(not row["cite_key"] for row in rows if row not in citation_rows)

preprints = [row for row in citation_rows if row["status"] == "preprint"]
assert [row["cite_key"] for row in preprints] == ["Suvagiya2026"]
assert all(row["doi"] or row["arxiv"] or row["status"] == "book" for row in citation_rows)

for row in rows:
    local_path = row["local_fulltext"].strip()
    if local_path:
        assert (REPO / local_path).exists(), f"missing local source: {local_path}"

canonical_text = CANONICAL_BIB.read_text(encoding="utf-8")
manuscript_text = MANUSCRIPT_BIB.read_text(encoding="utf-8")
assert canonical_text == manuscript_text, "canonical and manuscript BibTeX differ"

index_keys = {row["cite_key"] for row in citation_rows}
assert bib_keys(canonical_text) == index_keys

claim_map = CLAIM_MAP.read_text(encoding="utf-8")
mapped_keys = set(re.findall(r"\| `([^`]+)` \|", claim_map))
assert mapped_keys == index_keys

for language in ("en", "zh"):
    source = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((MANUSCRIPT / f"sections_{language}").glob("*.tex"))
    )
    cited = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", source):
        cited.update(key.strip() for key in group.split(","))
    assert cited == index_keys, f"{language} citations do not match core"

print("PERIOD8_REFERENCE_LIBRARY_INTEGRITY_PASS")
print("rows=30 citation_core=15 jgt_corpus=10 reserve=5")
