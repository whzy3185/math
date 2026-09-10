# Even defect gaps 16 through 30 are locally forbidden

This note continues the exact all-signing width-five analysis of the horizontal resonance `N=5s`.  Transition masks are as in the preceding local rules: `31` denotes a complement transition and every mask `0,...,30` is a defect.

## Theorem 1

Let `M` be an open width-five strip with

\[
\rho(M)^2<8.
\]

Suppose two specified defect transitions are separated by exactly `g` complement transitions, where

\[
\boxed{g\in\{16,18,20,22,24,26,28,30\}.}
\]

Then they cannot occur with one arbitrary transition on each side.  Equivalently no sub-threshold strip contains

\[
\boxed{(*,d,31^g,e,*),\qquad d,e\ne31.}
\tag{1}
\]

for any of these eight gaps.

### Proof

Normalize the initial pentagon state and quotient transition words by the simultaneous dihedral action `D_5`.  For every fixed `g`, the `31^2=961` labelled central pairs `(d,e)` give exactly 121 dihedral orbits.

A candidate is rejected only when an integer vector `w` satisfies

\[
w^T(M^2-8I)w\ge0,
\qquad w\ne0.
\tag{2}
\]

Thus every rejection is an exact certificate that the open strip cannot lie strictly below the threshold.

For each of the eight values of `g`, the exact survivor chain is identical:

\[
\boxed{
121\to12,
\qquad
336\to6,
\qquad
168\to0.
}
\tag{3}

The first arrow is the central pair, the second follows after adding one arbitrary transition on the left, and the third after adding one arbitrary transition on the right.  All 32 masks are permitted at both context extensions.

Moreover the six one-sided survivors stabilize, up to the `D_5` action, to

\[
(31,15,31^g,e),
\qquad
 e\in\{11,15,21,22,23,27\}.
\tag{4}

Every one of their 32 possible right extensions has an exact witness (2).  Hence the final survivor set is empty and (1) follows. `square`

The complete finite certificate is reproduced by `verify_n5s_width5_even_gap_16_30.py`.  Floating eigenvectors are used only to propose integer witnesses; (2) is evaluated with exact integer arithmetic before a branch is discarded.

## Structural significance

The identical state counts in (3) and the stable boundary family (4) are the first direct transfer evidence in the width-five problem.  The theorem itself is finite--it makes no claim for even gaps above 30--but it isolates the correct six boundary states that a uniform complement-pair transfer theorem must control.