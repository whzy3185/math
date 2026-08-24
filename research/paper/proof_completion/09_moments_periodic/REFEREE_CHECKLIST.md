# Referee Checklist: Moments and Periodic Frontier

## Definitions

- [x] `p` is a periodic cell length and primitive `tau` period is recomputed.
- [x] The lift condition is exactly `product Q=1`.
- [x] `R(Q)` is a supremum over the whole Bloch circle.
- [x] `M_k` is a constant-term/averaged even moment of the adjacency fiber.

## Human proof

- [x] Closed-walk weights are converted to `Q` monomials before imposing a
  period.
- [x] The formulas for `M_1,M_2,M_3` account for short-period collisions.
- [x] The implication from `R(Q)<=8` to moment inequalities has the correct
  direction.
- [x] No nonpositive moment excess is treated as an upper bound.

## Finite completeness

- [x] The legal finite domain is defined before enumeration.
- [x] Dihedral equivalence, global negation, repetition, and zone folding are
  stated.
- [x] Primitive periods are reconstructed rather than inferred from cell
  length.
- [x] Every orbit is consumed exactly once and no terminal is unresolved.
- [x] Endpoint acceptance is exact rational arithmetic.

## Scope and editorial role

- [x] The theorem is explicitly bounded by `p<=24`.
- [x] Periods 25 and 26 are excluded despite read-only exact evidence.
- [x] No aperiodic or arbitrary-interface conclusion is drawn.
- [x] `M_4,M_5,M_6` expansions are omitted from the main theorem.
- [x] The periodic frontier is assigned to an appendix, not the central
  phase-slip narrative.

## Independence disclosure

- [x] Shared helper code in the primary checker is disclosed.
- [x] The implementation-disjoint orbit audit and its weaker endpoint
  threshold are both disclosed.
- [x] The combination of coverage and exact `c6` checks is explained without
  overclaiming a single fully independent pipeline.
