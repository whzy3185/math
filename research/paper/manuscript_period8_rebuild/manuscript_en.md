# A period-eight analytic counterexample family for signed spectral-radius minimization

## 1. Introduction and main theorem

We study signings of the fixed graph `C_n(1,2)` and their adjacency spectral
radius.  A natural twisted candidate supplies a sharp-looking benchmark, but
it is not optimal on an infinite subsequence.  The mechanism is an explicit
period-eight Hamilton-gauge phase with a chiral Floquet fiber.

**Main Theorem.** For every `L >= 4`, the explicit alpha = +1 period-eight
signing on `C_(8L)(1,2)` has spectral radius strictly smaller than the twisted
benchmark on the same graph.

The proof factors the finite matrix into eight-site cells, reduces the fiber
through a chiral symmetry, and excludes all squared fiber eigenvalues above
`1561/200`.  The twisted benchmark is strictly larger than this rational
threshold.

## 2. Gauge coordinates and finite Bloch decomposition

Introduce switching, Hamilton gauge, the triangle word `tau`, and Hamilton
holonomy `alpha`.  For a period-`p` word on `n=pL`, write the finite problem in
cells and impose `z^L=alpha`.  State the finite direct-sum decomposition before
specializing to period eight.

## 3. The chiral period-eight fiber

Fix

`tau=(+,+,-,+,-,-,+,-)`.

Display the `8 x 8` fiber `H(z)`.  Exhibit its chiral involution and perform
the reductions `8 x 8 -> 4 x 4 -> 2 x 2`.  The resulting squared-eigenvalue
polynomial is

`P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38`,

where `c=z+z^{-1}`.  Record the exact infinite-volume edge separately from
the rational certificate used below.

## 4. Uniform polynomial certificate

Prove directly, with no numerical root search, that

`P(y,c)>0` for `y >= 1561/200` and `c <= 2`.

Deduce that every finite period-eight fiber has squared eigenvalues below
`1561/200`.  Keep this proof entirely readable as a polynomial positivity
argument.

## 5. Infinite counterexample family

Compute the twisted benchmark on the shifted grid and prove

`1561/200 < 4+2cos(pi/(4L))+2cos(pi/(2L))`

for `L >= 4`.  Combine this with Section 4 to prove the Main Theorem.

## 6. Why period eight is distinguished

Present the local square identity, the period-eight trichotomy, and the unique
sub-eight antipodal two-defect phase.  Any small closed-walk recurrence used
here must be displayed as a finite exact integer calculation, not as a broad
computer-assisted search claim.

## 7. General periodic defect obstruction

Derive the first three closed-walk moments `M1`, `M2`, and `M3`, and explain
the resulting defect-density and clustering inequalities.  This section gives
necessary structural constraints only; it does not claim a full classification.

## 8. Conclusion and scope

Summarize the period-eight counterexample family and its analytic mechanism.
State explicitly that the paper does not classify all even orders, all
minimizers, or the excluded R2/R4/R6/G6 families.

### Supplementary verification statement

The alpha = +1 finite theorem kernel underlying Sections 2--5 was
independently checked in Lean.  This statement covers the explicit witness,
not the structural extensions of Sections 6--7 or alpha = -1 packaging.
