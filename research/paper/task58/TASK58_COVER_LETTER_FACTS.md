# Task 58 Cover-Letter Facts

This file records facts only. It is not promotional copy.

## Mathematical problem

For even `n>=8`, the paper minimizes the adjacency spectral radius over all
`{+1,-1}` edge signings of the fixed cycle square
`C_n^2=C_n(1,2)`. Switching-equivalent signings have the same spectrum.

## Direct prior art

Suvagiya's 2026 preprint studies the same fixed graph family, objective, and
distinguished twisted candidate. It proves the candidate formula, verifies
optimality through order 18, and states all-even-order optimality as
Conjecture 3. The present paper resolves and disproves that conjecture.

## Complete classification

The distinguished candidate attains `rho_-(n)` at every even order, but is
globally minimizing exactly at

```text
8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46.
```

Strict failure occurs exactly at `32`, `40`, and every even `n>=48`. The
small-order pattern is nonmonotone: failure first occurs at 32, equality
returns, failure recurs at 40, equality returns again, and continuous failure
begins at 48.

## Structural contribution

The paper separates the attaining candidate from a period-eight reference
bulk. The reference squared edge is
`eta=4+sqrt(10+2sqrt(5))`. Its elementary gap-six phase slip has an exact
algebraic squared edge `c_6`, a rank-two squared eigenspace, and simple
unsquared partners. Among abnormal positive single gaps, G6 is the unique
minimum and every other gap is separated by more than `1/250`.

Charge-compatible one-, two-, and three-slip finite rings cover the nonzero
even residues. Patch identification and a discrete IMS estimate prove strict
failure for every even `n>=240`. Exact finite verification on the disjoint
interval `48<=n<240` establishes the sharp continuous onset 48.

## Computer-assisted disclosure

The computer-assisted portions follow the same four-stage pattern:

```text
mathematical reduction
-> finite exact object
-> exact verification
-> mathematical consequence.
```

The finite objects include exact switching-class decisions, parity-lifted
finite-state closures, rational positive-definiteness certificates, G6
matching/atlas data, and exact separated-interface constants. No theorem is
decided by a floating-point eigenvalue comparison. The paper includes the
human completeness and consequence arguments; the supplement provides full
exact-`2r` and integer-witness detail plus the reproducibility manifest.

## Submission package

```text
Main identified-source PDF: 38 pages, author metadata pending
Anonymous review PDF: 38 pages, identity-safe
Appendices: 14 pages within the main PDF
Supplement: 13 pages
Main-text figures: 3 monochrome figures
Development repository: https://github.com/whzy3185/math
Immutable archive: pending; no DOI assigned
```

The direct-prior-art and novelty audits were last run on 2026-08-24.

