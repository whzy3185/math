# Target A Technical Interface Audit

Date: 2026-08-21

Status: **PASS, SUBJECT TO FINAL REGRESSION**

## Zone Folding and Primitive Cells

- The operator-level identity is stated as
  `H_(mq)(z) ~= direct_sum_(w^m=z) H_q(w)`, including multiplicities.
- The independent transition checker covers repeated cells and records that
  finite sectors additionally impose `z^L=alpha`.
- The displayed `p=16` target row is explicitly identified as a repeated-cell
  representation of the primitive period-eight phase.
- The controlled `p=24` experiment recognizes the target row as primitive
  `tau` period 8 and assigns its exact value only through the proved zone-folding
  lemma.

Evidence: `verify_target_a_periodic_operator_equivalences.py`,
`target_a_periodic_operator_equivalences.json`, the low-period section, and the
high-period experiment JSON.

## Finite and Infinite Floquet Domains

- Finite order `n=pL` uses only the discrete grid `z^L=alpha`.
- Infinite periodic radius uses the continuous unit circle `|z|=1`.
- The finite counterexample family first proves a uniform unit-circle bound and
  then restricts it to the finite grid; it does not replace the finite spectrum
  by the infinite supremum.
- The exact band edge and bounded periodic classification are explicitly
  labeled infinite-volume statements.

## Moment Logic

- The only exclusion implication used is `F_k>0 => R(Q)>8`.
- The preliminaries, general-period section, low-period section, discussion,
  and experiment all state that nonpositive excesses do not give an upper
  bound.
- The defect-density and clustering inequalities remain necessary conditions
  only.

## Period-Eight Trichotomy

- Legal `Q` words have even defect count.
- The proof separates `d=0`, the two-defect distances `1,2,3,4`, and `d>=4`.
- Distance 4 is one dihedral orbit and is identified with the target phase;
  the other cases receive exact moment or endpoint certificates.

## Short-Cell Collisions

- The Laurent construction adds coincident offsets rather than overwriting
  them.
- The general-period moment proof and independent checker include `p=1,2,3,4`.
- The manuscript states explicitly that the cyclic formulas retain
  multiplicity in these periods.

## Expressions and Cross-References

- ASCII `+-` expressions were replaced by `\pm` in the band-edge and squared
  operator sections.
- The manually written `Lemmas 2.1-2.2` and a hard-coded section endpoint were
  replaced by labels.
- Final gates must still require zero manual equation tags, undefined labels,
  undefined citations, ASCII pseudo-math, absolute local paths, and Task IDs in
  the manuscript body.

## Scope

No theorem scope changed. In particular, the high-period experiment is not a
`p<=24` classification, and no all-period, all-signing, or all-even-order claim
has been added.
