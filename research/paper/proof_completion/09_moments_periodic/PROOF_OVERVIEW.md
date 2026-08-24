# Proof Overview: Moments and Bounded Periodic Phases

## Part I: human moment reduction

[APPENDIX_REQUIRED]

A closed walk of length `2k` in the step set `{-2,-1,1,2}` contributes a
monomial in the edge signs `tau`. Every closed walk contains an even number
of surviving `tau` endpoints. Pairing those endpoints rewrites the monomial
as a product over finite `Q` intervals. For lengths two, four, and six, the
translation classes collect to the three formulas in the theorem.

If `R(Q)<=8`, every squared fiber eigenvalue lies in `[0,8]`. Hence
`y^(k+1)<=8y^k`; summation over eigenvalues and Bloch averaging gives
`M_(k+1)<=8M_k`. Substituting the exact formulas yields the two necessary
obstructions.

## Part II: finite exact frontier

[APPENDIX_REQUIRED]

The bounded theorem is organized as

```text
mathematical reduction
  -> legal Q words with product Q=1
  -> dihedral orbits and primitive-period normalization

finite exact object
  -> one record for every orbit with p<=24
  -> moment exclusion, target repetition, or integer Rayleigh witness

machine verification
  -> destructive orbit accounting
  -> exact matrix/vector reconstruction
  -> exact comparison with the rational upper endpoint for c6

mathematical consequence
  -> every non-target orbit has R(Q)>c6
  -> the target has eta<c6
  -> bounded uniqueness.
```

## Why the domain is finite

[APPENDIX_REQUIRED]

For each `p`, there are exactly `2^(p-1)` legal `Q` words. Quotienting by a
finite dihedral group leaves finitely many orbits. Repetition and primitive
normalization only identify records; they do not add cases. The union over
`1<=p<=24` is therefore finite.

The stored accounting has 2,626 orbit records for `p<=16` and 370,100 for
`17<=p<=24`. Every record is consumed exactly once.

## Paper placement

[MAIN_TEXT_REQUIRED]

The main text should use only a short sentence explaining that closed-walk
moments give local periodic obstructions. Formulas (1)-(2), the finite-state
definition, and the bounded frontier theorem belong in an appendix. Higher
moment expansion tables are reproducibility material, not part of the main
narrative.
