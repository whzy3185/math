# Proof Overview

The global-edge proof is organized as four lemmas followed by an elementary
symmetry argument.

## Lemma A: bulk hyperbolicity

For every `y>eta`, the period-eight transfer matrix has a two-dimensional
stable space and a two-dimensional unstable space. This follows by reducing
its reciprocal quartic to a quadratic in `w=z+z^(-1)` and excluding
`w in [-2,2]`.

## Lemma B: physical matching

Transport the left unstable plane through the finite G6 core. A squared
energy `y>eta` is physical precisely when the transported plane intersects
the right stable plane nontrivially. This exterior-product condition is
coordinate free. Grassmann charts are merely local formulas for it.

## Lemma C: complete candidate exclusion

Exact elimination of the matching equations produces a finite resultant
candidate set above the upper endpoint in (1). A certified atlas covers the
physical stable and unstable planes through every chart transition. Sturm
counts find the complete candidate list, and the unsquared matching
determinant is nonzero on every candidate interval. Hence no physical G6
level lies above `c6`.

## Lemma D: physical realization

On the interval (1), the genuine unsquared Evans determinant changes sign
and has derivative of fixed nonzero sign. It therefore has exactly one
simple positive root. Exact elimination identifies its square with `c6`.

## Rank two and the negative branch

The coefficient identities `Q_(6-i)=Q_i` and `tau_(7-i)=-tau_i` imply (4).
The simple positive eigenvector is sent to a simple negative eigenvector.
After squaring, the two orthogonal vectors span `ker(H_6-c6)`. The same
symmetry transfers exclusion of the positive branch to the negative branch.

## Proof architecture

```text
mathematical reduction
  -> reciprocal bulk polynomial and geometric plane matching
finite exact object
  -> chart cover, resultant factors, isolating intervals
machine verification
  -> exact Sturm counts and unsquared nonvanishing
consequence
  -> global edge c6 with squared multiplicity two.
```

## Publication placement

- `MAIN_TEXT_REQUIRED`: the theorem, bulk-hyperbolicity lemma,
  coordinate-free matching criterion, candidate-completeness statement,
  physical realization, and rank-two symmetry.
- `APPENDIX_REQUIRED`: Grassmann charts, chart transitions, resultant
  factors, isolating intervals, Sturm counts, and unsquared exclusion signs.
- `REPRODUCIBILITY_ONLY`: producer/checker schemas, raw interval records, and
  tamper-oriented implementation details.
