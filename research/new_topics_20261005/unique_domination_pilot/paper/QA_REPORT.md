# Manuscript quality assurance

Completed 5 October 2026.

## Build

- Compiled manuscript.tex with pdfLaTeX using build.sh
- Two final compilation passes completed successfully
- Final PDF: 7 pages
- Final build contains no LaTeX warnings, undefined citations/references, overfull boxes or underfull boxes
- A workspace-local TeX format and font map were used because the installed file database was incomplete; no system configuration was changed

## Visual inspection

All seven pages of the final PDF were rendered to PNG at a 1550-pixel long edge and individually inspected. Text, mathematical symbols, displayed equations, page numbers and both tables are legible. No clipping, overlap, missing glyphs or stranded reference-only final page remains. The main theorem stays together on page 2. The final page contains the supplemental table, verification description and complete bibliography.

## Mathematical alignment

- Theorem 1.1 matches the independently audited sharp value gamma(gamma+7)/2 for every gamma>=2
- The equality statement remains restricted to gamma>=4
- Connected examples establish that the connected restriction has the same maximum
- The text distinguishes unique minimum cardinality from inclusion-minimality
- The p=0 edge case is retained in both upper-bound cases
- The six-/seven-vertex local replacement proofs are fully present
- The source's six-vertex argument is explicitly credited
- The thirteen-vertex example is not claimed to be the smallest counterexample over all n,gamma
- Supplementary pattern counts and the domination-count vector match the saved exact certificates
- No Lean certification, journal review, external submission or publication priority is claimed

## Source and metadata

The source comparison is pinned to arXiv:2511.01719v1, Conjecture 1, PDF page 2. The arXiv record was rechecked on 5 October 2026 and still listed v1 only. The bounded erratum search and its limitations are recorded in SOURCE_STATUS.md. Author and affiliation fields are intentionally blank pending confirmation; the PDF contains no invented author metadata.

The earlier proof package and independent audit are preserved outside paper/. The manuscript is a prose presentation of those audited claims, not a replacement for the exact certificates.

## Attribution revision, 08:46 UTC

The abstract now calls the 13-vertex counterexample previously reported. The introduction and bibliography credit John Erlbacher’s pinned public package and acknowledge Koch–Narayan’s n=10 equality discussion. Chinese handoff and source notes were updated consistently. No theorem, proof, checker or finite certificate changed. The former manuscript snapshot is preserved in frozen_pre_attribution_0835/.

Two further pdfLaTeX passes succeeded without warnings or box errors; the paper remains seven pages. All seven revised pages were rendered and visually inspected. The attribution on page 1 and pinned reference on page 7 are legible, and the theorem remains together on page 2.
