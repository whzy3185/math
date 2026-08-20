# Target A Publication PDF Visual Audit

Status: `PASS`

Audited build: `manuscript_tex_pub/main.pdf`

Pages: 32

Audit date: 20 August 2026

## Method

All 32 pages of the generic PDF were rendered to PNG at 120 dpi and reviewed
in four eight-page contact sheets.  The first page, theorem sequence, Floquet
matrix, long polynomial displays, closed-walk recurrence, residual certificate
tables, computational listings, resource table, and bibliography were then
inspected at 140 dpi.  The first pages of the anonymous, JGT pre-adaptation,
and SIDMA pre-adaptation builds were also rendered and checked.

## Results

- First-page title, author placeholders, affiliation placeholders, abstract,
  keywords, MSC placeholder, and opening section are aligned and legible.
- Theorem 1.1--1.6 hierarchy is consistent; statement bodies, displays, and
  following prose do not collide or create orphaned headings.
- Equation numbers are automatic and unique.  Matrices, cases, radicals,
  aligned polynomials, products, sums, and Rayleigh quotients are not clipped.
- All twelve table captions are visible.  Tables remain inside the text block;
  the Appendix B certificate tables occur in logical order 8--11.
- The period-eight matrix, long exact certificate rows, and terminal checkpoint
  hashes remain readable at normal PDF zoom.
- Lists in the computer-assisted proof boundary have complete items and
  consistent indentation.
- Shell listings are confined to the computational appendix, use one typeface,
  and break within the available width.
- Data/code availability, funding, acknowledgment, supplement, archive DOI,
  and author metadata placeholders are visible and unambiguous.
- References contain no clipped lines or unresolved citation markers.
- No formula clipping, text overlap, broken bullet, missing caption, duplicate
  number, blank content page, font mismatch, or excessive isolated whitespace
  was observed.

The machine build audit independently records zero overfull boxes, undefined
references, undefined citations, and fatal LaTeX errors for all four builds.

Conclusion: `TARGET_A_PUBLICATION_VISUAL_AUDIT_PASS`.
