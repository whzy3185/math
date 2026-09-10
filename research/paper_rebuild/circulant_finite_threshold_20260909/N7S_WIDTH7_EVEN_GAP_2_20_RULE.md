# First width-seven even-gap obstruction on `N=7s`

This note begins the all-signing analysis of the next horizontal resonance `N=7s`.  It is the width-seven analogue of the pentagon transition-mask method, but no conclusion from the `N=5s` theorem is used as a black box.

## 1. Open heptagon strips

For a seven-bit edge mask `eta`, let `C(eta)` be the signed adjacency matrix of the heptagon `C_7`.  For an open word of column states

\[
\eta_0,\ldots,\eta_{L-1},
\]
let `M` be the block tridiagonal matrix with diagonal blocks `C(eta_j)` and identity matchings between consecutive columns.  This is the induced signed adjacency matrix on an open interval of chord-heptagon columns of `C_(7s)(1,s)` after switching the inter-column matching edges to `+1`.

Write the transition mask as

\[
\delta_j=\eta_j\oplus\eta_{j+1}\in\{0,\ldots,127\}.
\]

A transition is **complement** when

\[
\delta_j=127,
\]

so that `eta_(j+1)=-eta_j`; every other mask is a defect.

## Theorem 1 (finite even-gap rule through twenty)

Let `M` be a width-seven open strip with

\[
\rho(M)^2<8.
\]

Suppose two defect transitions `d,e` are separated by `g` complement transitions and have three complement transitions available on both exterior sides.  Then this is impossible for

\[
\boxed{g\in\{2,4,6,8,10,12,14,16,18,20\}.}
\tag{1}
\]

Equivalently, no sub-threshold width-seven strip contains

\[
\boxed{127^3,d,127^g,e,127^3,\qquad d,e\ne127}
\tag{2}
\]

for any even `g` in (1).

### Proof

Normalize the first column state to the all-positive heptagon.  A simultaneous dihedral automorphism of the seven row labels acts on every transition mask and preserves the spectrum.  The group is `D_7` of order fourteen.

For each fixed `g`, the

\[
127^2=16129
\]

labelled defect pairs reduce to exactly

\[
\boxed{1265}
\tag{3}
\]

`D_7` orbits.  For every orbit representative, an integer vector `w` is found satisfying

\[
w^T(M^2-8I)w\ge0,
\qquad w\ne0.
\tag{4}
\]

The test (4) is evaluated in exact integer arithmetic.  Consequently every representative has squared spectral radius at least eight, and by symmetry so does every labelled pair.  The exact survivor count is therefore

\[
\boxed{1265\longrightarrow0}
\tag{5}
\]

for each of the ten values of `g` in (1).  This proves the theorem. `square`

The complete reconstruction is `verify_n7s_width7_even_gap_2_20.py`.  As in the other finite-state certificates, floating eigenvectors are used only to propose integer directions; a candidate is rejected only after (4) is checked exactly.

---

## 2. Interpretation

Theorem 1 is deliberately local.  It does **not** yet claim a complete threshold theorem on `N=7s`.

Its importance is structural: the all-signing width-seven problem already exhibits an even-gap exclusion analogous to the width-five parity mechanism.  Thus the natural next tasks are:

1. prove a uniform transfer theorem for all sufficiently long even gaps;
2. classify the short odd-gap defect clusters that survive;
3. impose the helical seam on the resulting finite residual families.

The positive side can be treated independently by the finite seam-response construction; the present theorem concerns all signings and supplies the first negative-side rigidity for the `N=7s` line.