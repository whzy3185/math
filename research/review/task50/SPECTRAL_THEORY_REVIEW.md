# Task 50 Spectral-Theory Review

## Findings

### BLOCKER 1: finite localization does not identify the finite spectral radius

The exact Evans zero proves an infinite localized eigenstate, and truncation
would produce a nearby finite eigenvalue.  Neither fact excludes another
finite-ring eigenvalue of larger modulus.  The requested estimates for `R_n`
therefore remain unproved, blocking the two-tail and all-even conclusions.

### MODERATE 1: the simple-zero intersection argument should stay explicit

The cofactor charts are nonzero and the Evans derivative excludes zero, so the
matching zero is simple.  A future paper should retain the short argument that
changes of basis multiply the determinant by a nonvanishing factor and that a
higher-dimensional persistent intersection would contradict simplicity.

## Accepted Components

The stable/unstable split is exact on rational intervals.  The Evans function
is defined from exact monodromies and nonvanishing algebraic cofactor vectors.
The sign change and uniqueness use outward rational intervals, not numerical
root agreement.  Infinite and finite operators are kept distinct.

## Verdict

- BLOCKER: 1
- MAJOR: 0
- MODERATE: 1
- MINOR: 0

The blocker applies to the finite-ring/main-theorem program.  It does not
invalidate `TARGET_A_EXACT_INTERFACE_THEOREM.md`.
