# Bilingual conclusion correction

Frozen source: `6766ecbc20b084c648b29b0bf3813b8c1ecf86cb`.
Correction branch: `paper/period8-conclusion-correction`.
The tag `freeze/period8-jgt-2026-09-05` and the original paper branch remain
unchanged. No general-jump result has been imported into this branch.

The previous conclusion asked whether the global minimum equals
`sqrt(eta)` for infinitely many finite `L`. Section 4 already proves that
the legal negative-holonomy signing has smaller radius for every finite
`L>=1`. Since the global minimum ranges over both holonomies, that proposed
open question had an already negative answer.

Both conclusions now state the available bound

`m(C_(8L)(1,2)) <= rho(A*_(8L,-)) < sqrt(eta)`.

They retain the open problem of determining the global minimum and the
minimizing switching classes, without speculating about equality with the
positive-holonomy value. The correction changes no theorem or proof in
Sections 1–5 and adds no mathematical result.

The old integrity reports record historical checks; their unrestricted
wording about final readiness is not a certificate of mathematical
correctness. This correction closes this particular conclusion defect only.

## Verification performed

- Both Tectonic builds passed: English 16 pages, Chinese 15 pages.
- Bilingual label/section/citation verifier passed.
- Reference-library verifier passed (30 records, 14 manuscript citations).
- No unresolved citation/reference or overfull/underfull box was reported.
- Rendered English pages 15–16 and Chinese pages 14–15 were inspected after
  the correction; the corrected inequality, conclusion and bibliography fit.
- The tracked changes are limited to both conclusion sources, both PDFs and
  this correction record. Sections 1–5, figures, bibliography and Lean are
  unchanged. Full mathematical regressions were not rerun for this prose-only
  correction; the inequality used is already proved in Section 4.

The Chinese build uses the existing macOS font set and emits its customary
platform-font reproducibility warning. No font or layout configuration was
changed by this correction.
