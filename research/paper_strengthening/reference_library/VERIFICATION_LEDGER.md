# Verification ledger

## Current snapshot

| check | population | result |
|---|---:|---|
| unique master IDs | 30 | PASS |
| unique nonempty citation keys | 14 | PASS |
| unique nonempty DOIs | 28 | PASS |
| unique nonempty arXiv identifiers | checked | PASS |
| manuscript-core rows | 13 mature + 1 recent-context row | PASS |
| JGT structure corpus | 10 | PASS |
| reserve collection | 5 | PASS |
| local paths declared in manifest | all existing | PASS |
| canonical vs manuscript BibTeX keys | 14/14 | PASS |
| canonical vs manuscript BibTeX bytes | identical | PASS |
| claim-map core coverage | 14/14 | PASS |
| cited vs bibliography keys | 14/14 both languages | PASS |

## Bibliographic verification authority

The full item-by-item query and source trail for the manuscript core is in
`../manuscript_period8_jgt/INTEGRITY_REPORT_STAGE_2_5.md`.  Compact metadata
status is mirrored in
`../manuscript_period8_jgt/BIBLIOGRAPHY_VERIFICATION.md`.

## Version boundary

This library records the period-eight-only paper after mathematical closure.
Earlier `research/related_work` reports may contain correct metadata but stale
editorial roles for all-even, G6, or computation-heavy manuscripts.  On any
role conflict, this library controls the current manuscript; on any
bibliographic conflict, the authoritative external record must be checked
again rather than selecting whichever local file is newer.
