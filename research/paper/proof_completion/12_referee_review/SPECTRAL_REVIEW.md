# Hostile Spectral-Theory Review

## Verdict

`PASS`; the canonical G6 presentation fix identified during review is
resolved in `05_g6_edge/THEOREM_STATEMENT.md`.

## G6 global edge

The global-edge argument does more than find roots of a resultant. It has the
required chain:

```text
bulk hyperbolicity
  -> stable/unstable matching condition
  -> global Grassmann chart cover
  -> finite resultant candidate list
  -> unsquared physical acceptance/exclusion
  -> spectral top c6.
```

The two higher resultant candidates are excluded by nonzero unsquared G6
matching determinants. A confluent repeated-multiplier case is handled
separately. The norm bound closes the remaining spectral range. Thus the proof
does not confuse algebraic candidates with physical spectrum.

## Rank and multiplicity

The symmetry `K^2=-I`, `KA=-AK`, `KH=HK` sends the simple positive adjacency
root to a simple negative root. Both square to `c6`, so the squared eigenspace
has dimension two. The separated-ring theorem correctly counts `2r` levels
with multiplicity and does not assert individual simplicity.

## Single gaps

The hierarchy covers all positive `g`: gap four is reference bulk, gap six is
the unique equality interface, six remaining small gaps have exact witnesses,
and one finite-support vector covers every `g>=9` by locality. The uniform
`1/250` separation is a strict exact corollary.

## Resolved presentation check

The canonical theorem now defines `c6` directly as the unique root in the
certified interval of

```text
16y^10-520y^9+6913y^8-48448y^7+191768y^6
-423904y^5+484528y^4-270464y^3+137856y^2-19968y+256.
```

Only after this definition may the manuscript give
`c6 approximately 7.905369311620327`. The proof package follows this order,
so no spectral presentation blocker remains.
