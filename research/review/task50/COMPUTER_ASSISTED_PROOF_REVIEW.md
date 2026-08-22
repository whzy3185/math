# Task 50 Computer-Assisted-Proof Review

## Findings

### MODERATE 1: the independent checker shares the interval kernel

The checker changes the eigenvector coordinate chart from first-three-row to
last-three-row cofactors and independently reruns every determinant.  It still
shares the `Fraction` interval and integer-square-root kernel with the
producer.  This is adequate for the repository gate because the kernel is
small and directly tested, but a journal artifact would benefit from a second
implementation in Arb or another directed-rounding library.

### MINOR 1: retain the outward-enclosure format explanation

Internal fractions can have thousands of digits.  Stored determinant bounds
are compressed to 30-decimal outward rational intervals.  The manifest and
paper supplement must say that this is outward compression of exact internal
fractions, not a conversion to ordinary decimal floating point.

## Accepted Components

All transfer entries are exact integer polynomials.  Input root intervals are
rational.  Square roots use integer `isqrt` bounds at 120 decimal places.
Automatic derivatives are propagated with exact rational endpoints.  Root
existence, uniqueness, nondegenerate cofactor charts, and `b_g<8` are all
fail-closed checks.  No empirical Task 49 constant is imported.

## Verdict

- BLOCKER: 0
- MAJOR: 0
- MODERATE: 1
- MINOR: 1
