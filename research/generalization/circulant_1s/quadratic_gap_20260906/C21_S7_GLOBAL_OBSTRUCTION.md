# A global finite-order obstruction at `C_21(1,7)`

Date: 2026-09-06.

This note strengthens `ODD_ORDER_ONE_DEFECT_OBSTRUCTION.md`.  The earlier
result only excluded the naive one-defect near-alternating Ansatz.  The new
result is exhaustive over **all edge signings** up to switching and graph
translation.

## Theorem F21

Let `A_sigma` be the signed adjacency matrix of an arbitrary edge signing of

\[
 C_{21}(1,7).
\]

Then

\[
 \boxed{
 \rho(A_\sigma)^2\ge \frac{1066}{131}>8.}
 \tag{1}
\]

In particular,

\[
 \boxed{
 \rho(A_\sigma)>\sqrt8
 \quad\text{for every signing }\sigma.}
 \tag{2}
\]

Thus `C_21(1,7)` is a genuine finite-order obstruction: no choice of edge
signs reaches the sub-`sqrt(8)` regime available in the continuous odd-jump
Bloch model and in many other finite orders.

This theorem is a finite exhaustive computer-assisted result with an exact
integer certificate for every enumerated representative.  It is not inferred
from floating eigenvalues.

## 1. Exhaustive Hamilton-gauge parametrization

Switching preserves the spectrum.  Fix the step-one Hamilton cycle and switch
along a spanning path so that its first `20` edges have sign `+1`.  The last
cycle edge has Hamilton holonomy

\[
 \alpha\in\{+1,-1\}.
\]

Let

\[
 \tau_i\in\{+1,-1\}
\]

be the chord coordinate for the edge from `i` to `i+7` on the quasiperiodic
cover.  Every switching class has such a representative.

Define

\[
 Q_i=\tau_i\tau_{i+1}.
\]

Because the product telescopes around the finite word,

\[
 \prod_{i=0}^{20}Q_i=1.
\tag{3}
\]

Conversely, a cyclic `Q` word satisfying (3), together with one anchor
`tau_0=+/-1`, uniquely reconstructs `tau`.  Therefore all Hamilton-gauge
signings are parametrized by

\[
 (Q,\tau_0,\alpha),
 \qquad
 \prod Q_i=1.
\tag{4}
\]

## 2. Rotation reduction

Translation of the underlying circulant is a graph automorphism and preserves
the signed spectrum.  After restoring Hamilton gauge, translation rotates the
cyclic `Q` word; the anchor may change, while the Hamilton holonomy remains in
the scanned set `+/-1`.

Hence it is enough to take one binary necklace representative for every
cyclic rotation class of admissible `Q` words, and then scan both anchors and
both holonomies.

For length `21` with product constraint (3), there are exactly

\[
 49,940
\]

such binary necklaces.  The exhaustive population is therefore

\[
 49,940\times2\times2=199,760
\tag{5}
\]

Hamilton-gauge representatives.

The generator in `verify_c21_s7_all_signings.py` constructs this population
directly; the displayed counts are asserted by the script.

## 3. Seam-safe finite adjacency

The finite matrix is built from the quasiperiodic shift rather than by
silently wrapping chord entries without holonomy.  If a displacement crosses
the Hamilton seam, its matrix coefficient is multiplied by `alpha`.

Equivalently, with `T^21=alpha I` and `M_tau=diag(tau)`,

\[
 A=T+T^{-1}+M_\tau T^7+T^{-7}M_\tau.
\tag{6}
\]

This seam convention is essential.  It is the same finite model used in the
pre-existing exact one-defect certificate.

## 4. Exact Rayleigh certificate for each representative

For each representative define the integer symmetric matrix

\[
 C=8I-A^2.
\tag{7}
\]

To prove `rho(A)^2>8`, it is enough to find a nonzero integer vector `w` with

\[
 w^T Cw<0.
\tag{8}
\]

Indeed (8) is equivalent to

\[
 \frac{w^TA^2w}{w^Tw}>8,
\]

so the top eigenvalue of `A^2` exceeds `8`.

The verifier uses a floating eigensolver only as a **witness proposer**: it
computes an approximate least eigenvector of `C`, multiplies it by `16`, and
rounds to an integer vector.  The floating eigenvalue is then discarded.  The
script checks (8) using integer matrix multiplication.

On the full population (5), the scale `16` witness succeeds in every single
case.

Therefore a successful verifier run is exact at the certification stage:
roundoff can at worst fail to propose a witness, but it cannot make the exact
integer assertion (8) true when it is false.

## 5. Uniform rational margin

The generated witnesses satisfy the stronger exact inequality

\[
 \frac{-w^TCw}{w^Tw}\ge\frac{18}{131}
\tag{9}
\]

for every one of the `199,760` representatives.  This comparison is checked
cross-multiplied over the integers:

\[
 131(-w^TCw)\ge18(w^Tw).
\]

Hence

\[
 \frac{w^TA^2w}{w^Tw}
 =8+\frac{-w^TCw}{w^Tw}
 \ge8+\frac{18}{131}
 =\frac{1066}{131}.
\]

This proves (1).

The weakest generated witness occurs in the one-defect rotation class and has

\[
 -w^TCw=36,
 \qquad
 w^Tw=262,
\]

so its exact Rayleigh excess is `18/131`.  The actual spectral excess is a bit
larger; no exact formula for the global minimum over signings is claimed here.

## 6. Significance for finite-order compatibility

The continuous odd-jump alternating-flux model has a strict gap below `8`
for every odd jump.  Finite even orders inherit that model directly.  Odd
orders cannot be handled by a blanket statement of the form "repair the
alternating word by a few local defects": `C_21(1,7)` proves that, at least at
this order, **no repair exists at all**.

Thus the project now has a sharp distinction:

- **jump-parameter theorem:** every integer jump `s>=2` admits an explicit
  periodic Bloch family with edge below `sqrt(8)` and sharp `pi^2/s^2` gap;
- **finite-order theorem:** not every admissible pair `(N,s)` admits any
  signing below `sqrt(8)`.

The finite-order classification problem is therefore genuinely arithmetic and
cannot be reduced to period compatibility alone.

## 7. Next questions

The natural next finite problems are:

1. determine whether `C_(3s)(1,s)` is a systematic obstruction family for
   sufficiently large odd `s`;
2. find the exact minimum `m(21,7)` rather than only the lower bound (1);
3. classify the odd orders for which one-defect or multi-defect words do
   achieve `rho^2<8`;
4. replace exhaustive enumeration by a structural analytic obstruction, for
   example via the width-three triangular-strip representation when `N=3s`;
5. formalize the finite exhaustive certificate in Lean or another proof
   assistant if the result becomes part of the final manuscript.

The verifier for Theorem F21 is `verify_c21_s7_all_signings.py`.
