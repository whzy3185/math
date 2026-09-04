# Period-eight JGT-first manuscript

- `main_en.tex`: authoritative English manuscript.
- `main_zh.tex`: synchronized Simplified Chinese companion.
- `references.bib`: strictly verified working bibliography.
- `figures/`, `figures_zh/`: source-native TikZ figures.
- `AUTHOR_AND_SUBMISSION_QUESTIONS.md`: unresolved submission metadata only.
- `STRUCTURE_RATIONALE.md`: one-page architecture explanation.
- `BIBLIOGRAPHY_VERIFICATION.md`: metadata verification ledger.

The organized canonical reference index is `../reference_library/`.  The
local `references.bib` is intentionally retained as an identical mirror so the
manuscript source remains self-contained; `verify_reference_library.py`
enforces byte-for-byte synchronization.

The mathematical authority is `../final_theorem_package.md`.  The manuscript
does not import prose from the superseded paper trees.
