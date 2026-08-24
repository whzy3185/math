# Hostile Graph-Theory Review

## Verdict

`PASS`; the canonical proof package satisfies the presentation requirements
listed below.

The mathematical spine can be read as a signed-graph spectral problem:
switching reduces signings of `C_n(1,2)` to flux and holonomy data; positive
flux positions define cyclic gaps; gap four is the reference phase; gap six
is the elementary phase slip; separated phase slips produce explicit finite
signed graphs in every nonzero even residue class.

## Strengths

- The objects remain signed graphs, not abstract transfer matrices detached
  from the original problem.
- Gap words give a direct combinatorial description of the explicit
  counterexamples.
- The residue proof checks gap sum, flux lift, sector closure, and holonomy.
- The complete even-order result is a truth-value classification and does not
  overclaim a minimizer classification.

## Required presentation discipline

1. Define `C_n(1,2)`, switching, `Q`, and holonomy before introducing
   operators.
2. Introduce transfer/Evans and IMS methods only after the graph reduction.
3. State the bounded periodic theorem in an appendix; it is supporting
   structure, not the main classification.
4. Do not use internal task labels as theorem dependencies.
5. Keep the distinction between a gap count and spectral multiplicity visible:
   `r` G6 gaps produce `2r` squared near-edge levels.

## Resolved adverse finding

Some distributed historical G6 sources defined `c6` by referring to an
earlier polynomial record. The canonical package now displays the complete
degree-ten polynomial and isolating interval in
`05_g6_edge/THEOREM_STATEMENT.md` before any decimal approximation. The later
manuscript reframe must preserve that order; no graph-theoretic proof blocker
remains.
