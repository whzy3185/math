# Target A Exact Interface Theorem

## Statement

For each `g in {6,10}`, let `A_g` be the infinite signed
`C_infinity(1,2)` recurrence whose quadrilateral defects have spacing four on
both sides and a single phase slip of gap `g`, with the conventions in
`G6_DEFECT_TRANSFER.md` and `G10_DEFECT_TRANSFER.md`.

There is a unique simple squared level `c_g` in the following rational
interval:

\[
\frac{7905369311620327}{10^{15}}
<c_6<
\frac{7905369311620328}{10^{15}}<8,
\]

\[
\frac{7977104370400546}{10^{15}}
<c_{10}<
\frac{7977104370400547}{10^{15}}<8.
\]

At `lambda=sqrt(c_g)`, the recurrence has a nonzero state exponentially
localized at the phase slip.  In period-eight cells its tails satisfy

\[
\|X_j\|\le C_6(9/25)^{|j|}
\quad\text{for G6},
\qquad
\|X_j\|\le C_{10}(4/15)^{|j|}
\quad\text{for G10}.
\]

The relevant stable and unstable multipliers are positive real reciprocal
pairs.

## Evans Definition

Let `u_1,u_2` be cofactor eigenvectors of the left monodromy for its two
unstable multipliers, and let `s_1,s_2` be cofactor eigenvectors of the right
monodromy for its stable multipliers.  Put

\[
D_g(y)=\det(P_g(\sqrt y)u_1,P_g(\sqrt y)u_2,s_1,s_2).
\]

The multiplier formulas are the exact nested-radical expressions derived from
the palindromic quartic.  The cofactor vectors use the first three rows of
`M-zI`.  The certificates prove that every vector has a nonzero component on
the whole root interval, so this is a valid coordinate chart.  Here
`sqrt(y)>0` is part of the definition: the certified Evans function proves the
positive interface eigenvalue `lambda=sqrt(c_g)`.  No symmetry assertion for
the negative-lambda Evans chart is needed or claimed.

## Proof

Bulk hyperbolicity and the positive reciprocal root structure follow from
`TARGET_A_BULK_HYPERBOLICITY_PROOF.md`.  Exact multiplication gives the two
unimodular defect transfers.  The interval evaluator performs every field
operation over `Fraction` endpoints.  Each square root is enclosed outward by
integer square-root bounds at 120 decimal places.  Automatic differentiation
propagates an enclosure of `D_g'(y)` through the same exact expression graph.

For G6 the certified left and right Evans intervals have signs `-1` and `+1`,
and the derivative enclosure is strictly positive throughout the rational
root interval.  The intermediate-value theorem gives a zero and the derivative
test gives uniqueness and simplicity.  The G10 certificate has the same three
properties.  No high-precision approximation is used in these acceptance
checks.

The localized-state conclusion and the stated decay bounds now follow from
the Localized Finite-Defect Matching Lemma and the rational multiplier bounds
`9/25` and `4/15`.

## Computer-Assisted Components

- exact multiplication of the 4-by-4 transfer matrices;
- outward rational evaluation of nested square roots;
- exact-rational interval evaluation of the Evans determinant and derivative;
- nonvanishing checks for the four cofactor eigenvectors.

The producer certificates are `g6_interface_certificate.json` and
`g10_interface_certificate.json`.  An independent coordinate checker uses
cofactors from the last three monodromy rows and reproduces the sign,
simple-zero, and nondegeneracy conclusions in
`research/reproducibility/task50/interface_checker_output.json`.

## Evidence Status

`G6_INTERFACE_THEOREM_PROVED`

`G10_INTERFACE_THEOREM_PROVED`

The result is a computer-assisted proof with exact rational acceptance.  It
does not yet prove a uniform upper bound for the spectral radius of every
finite ring.
