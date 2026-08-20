# Target A Journal Variant Notes

Checked: 20 August 2026

The publication tree keeps one shared mathematical body.  The `main_jgt.tex`
and `main_sidma.tex` files are lightweight pre-adaptation builds, not claims
that a final journal has been selected.

## Journal of Graph Theory

The current Journal of Graph Theory author instructions recommend Wiley's New
Journal Design LaTeX authoring template.  They also request a compiled PDF with
the LaTeX main document and all supporting source files.  The current generic
front matter already reserves author affiliations, acknowledgments, and four
to seven keywords.  Migration to the Wiley NJD class should occur only after
JGT is selected, because the final template package and submission metadata
must then be supplied together.

Official guidance:
<https://onlinelibrary.wiley.com/page/journal/10970118/homepage/forauthors.html>

## SIAM Journal on Discrete Mathematics

The current SIDMA instructions strongly encourage SIAM's standard macros and
require keywords and MSC codes.  SIAM's journal-author page currently lists
`siamart251216.cls`, `siamplain.bst`, article/supplement examples, and shared
article/supplement source.  The SIDMA pre-adaptation uses a fleqn-style generic
build and the same shared body.  A final SIDMA package should migrate the
wrapper to `siamart251216.cls`, use `siamplain.bst`, and map the existing
supplement placeholders into SIAM's shared article/supplement structure.

Official guidance:
<https://epubs.siam.org/journal/sidma/instructions-for-authors>
and <https://epubs.siam.org/journal-authors>.
