# Residue-Two Fixed-Width Schur Reduction

Fix the standard one-G6 signing at `n=8k+2` and put

```text
M_n = 198 I - 25 A_n^2.
```

Positive definiteness of `M_n` is exactly the desired bound
`rho(A_n)^2<198/25`.

Order the vertices as

```text
4,5,...,n-5, 0,1,2,3,n-4,n-3,n-2,n-1.
```

Because `A_n^2` has range four, retain the four left boundary vertices and
the eight forward vertices while eliminating one interior vertex. This is an
exact Schur-complement update on a `12 x 12` symmetric rational state. After
the repeated bulk steps, eliminate four forward sites without adding new
sites; the remaining `8 x 8` matrix is the final boundary Schur complement.

Thus for every `n=8k+2`, positivity is equivalent to:

```text
all repeated bulk pivots are positive
and the fixed 8 x 8 final boundary Schur complement is positive.
```

The update in a complete period-eight bulk cell is independent of `n`. The
checker reconstructs this reduction using only exact `Fraction` arithmetic
and verifies exact equality with a full interior-first LDL computation at
`n=50,58,66,74,82,90`.

This is a genuine dimension reduction from an unbounded matrix problem to a
fixed-width rational recurrence. It is not yet the all-length theorem: the
remaining step is a rational invariant domain for the eight-step bulk map and
a uniform positive boundary Schur estimate.
