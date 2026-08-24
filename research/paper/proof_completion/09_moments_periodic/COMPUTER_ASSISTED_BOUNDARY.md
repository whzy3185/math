# Computer-Assisted Boundary: Moments and Periodic Frontier

## General moment theorem

[APPENDIX_REQUIRED]

**NONE REQUIRED FOR THE FIRST THREE IDENTITIES OR THEIR NECESSARY
OBSTRUCTIONS.** The closed words of lengths two, four, and six can be listed
by hand, and the conversion from `tau` endpoints to `Q` intervals is an exact
identity. Programs independently re-enumerate the same walks as an audit.

## Bounded frontier theorem

[APPENDIX_REQUIRED]

Machine assistance is logically essential for the complete `p<=24` orbit
partition. Its accepting arithmetic is limited to:

- finite exhaustive enumeration and finite graph/orbit accounting;
- exact integer closed-walk moments;
- exact Gaussian-integer or integer Rayleigh quotients;
- exact rational comparison with `c6_upper`;
- exact hashes binding source closure files and certificate records.

No floating-point eigenvalue is an endpoint. Floating calculations only
suggest witness vectors.

## Finiteness

For every `p<=24`, the legal set has `2^(p-1)` words. The quotient group is
finite, and there are finitely many periods. The certificate consumes every
canonical orbit exactly once. This is why a finite computation proves the
bounded theorem and why it cannot prove an all-period theorem.

## Independence mechanism

[REPRODUCIBILITY_ONLY]

Independence is layered.

1. The primary `c6` checker rebuilds all stored Bloch matrices, integer
   quotients, source hashes, and closure equations. It shares a small set of
   canonical/Bloch helper routines with the producer, so it is not a fully
   implementation-disjoint checker.
2. A separate period-17--24 audit imports no canonical or moment helper. It
   independently regenerates necklaces/bracelets, lifts `Q`, computes moments,
   builds finite matrices, and consumes all 370,100 orbits with zero remainder.
   Its stored endpoint threshold is `1561/200`, so it independently validates
   orbit completeness but is not by itself the full `>c6` checker.
3. The exact `>c6` comparisons are integer cross-multiplications against the
   certified rational endpoint and are rebuilt record by record by the
   primary checker.

Together these layers separate exhaustive coverage from spectral arithmetic.
For a publication artifact, this division must be stated explicitly rather
than described as one wholly independent implementation.

## Excluded evidence

The exact period-25/26 read-only scans have no integrated producer/checker
pair at the same standard. They are not used. Higher-moment exploratory tables
and numerical within-period rankings are also not theorem evidence.
