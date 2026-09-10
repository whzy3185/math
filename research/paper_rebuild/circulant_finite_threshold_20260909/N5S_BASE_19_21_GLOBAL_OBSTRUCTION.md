# Global width-five obstruction at `s=19,21`

This note extends the all-signing width-five obstruction beyond the previously closed cases `s=15,17`.  It uses the same intrinsic pentagon-column flux encoding and the already proved local complement/even-gap rules, but the residual cyclic populations are audited independently here.

## Theorem 1

For the finite signed circulants

\[
C_{95}(1,19),\qquad C_{105}(1,21),
\]

one has

\[
\boxed{m(95,19)\ge \sqrt8,\qquad m(105,21)\ge \sqrt8.}
\tag{1}
\]

The quantifier is over **all** edge signings.

---

## 1. Width-five transition encoding

For odd `s`, reorder `C_(5s)(1,s)` into the `s` chord-pentagon columns

\[
V_j=\{j,j+s,j+2s,j+3s,j+4s\},\qquad j\in\mathbb Z_s.
\]

The five elementary square fluxes across the boundary between `V_j` and `V_(j+1)` form a switching-invariant five-bit transition mask `delta_j`.  A boundary is **complement** when `delta_j=31`; otherwise it is a **defect**.

Let the cyclic defect transitions be separated by complement gaps

\[
g_1,\ldots,g_r\ge0,
\]

so

\[
s=r+\sum_i g_i.
\tag{2}
\]

The all-complement case is impossible for odd `s`: if `p_j` is the signed flux of the chord pentagon in column `j`, the product of the five square fluxes across a complement boundary is `-1`, hence

\[
p_{j+1}=-p_j,
\]

which cannot close after an odd number of columns.

A unique defect is excluded by the already proved fourteen-column single-defect certificate.  For `r>=2`, the thirteen-column complement rule excludes adjacent defects whenever the relevant interval is proper, so `g_i>=1`.  Since `s` is odd, (2) implies that at least one `g_i` is even.

The exact embedded even-gap rules exclude `g=2,4` and `g=6,8,10,12,14` whenever the required context lies in a proper open interval.

---

## 2. The case `s=19`

For a cyclic word of length 19, every even gap at most 12 is excluded by a proper open interval.  Combining positivity of all gaps, the parity condition, and the sum relation (2), the only residual gap patterns, up to cyclic rotation and reversal, are

\[
\boxed{(16,1),\qquad(14,3),\qquad(14,1,1).}
\tag{3}
\]

The first two have two defects.  Cut at a complement boundary in the long gap and switch all remaining inter-column matchings to `+1`.  The helical seam is retained as a signed 5-cycle permutation.  After common row switching its sign word is

\[
q=(1,1,1,1,\alpha),\qquad \alpha\in\{\pm1\}.
\]

For each of the patterns `(16,1)` and `(14,3)`, enumerate both `alpha`, all 32 initial pentagon states, and all `31^2` choices of the two defect masks, retaining only the exact seam-complement solutions.  In each case exactly

\[
\boxed{1920}
\tag{4}
\]

full cyclic candidates remain.  Every one admits an integer vector `w` with

\[
w^T(A^2-8I)w\ge0.
\tag{5}
\]

Hence neither two-defect residual can be strictly sub-`sqrt(8)`.

For `(14,1,1)`, use `D_5` to normalize the first defect to one of the seven representatives

\[
0,1,3,5,7,11,15.
\]

There are therefore

\[
7\cdot31^2=6727
\]

canonical defect triples before spectral pruning.  For every one of these triples, the first proper 18-column principal open strip already has an exact integer Rayleigh witness for squared radius at least eight.  Thus the survivor count is

\[
\boxed{6727\longrightarrow0.}
\tag{6}
\]

No cyclic seam audit is required for this third pattern.  Equations (3)--(6) prove

\[
m(95,19)\ge\sqrt8.
\]

---

## 3. The case `s=21`

Now the even-gap rule through `g=14` is available on proper open intervals.  The same gap arithmetic leaves precisely

\[
\boxed{(18,1),\qquad(16,3),\qquad(16,1,1)}
\tag{7}
\]

up to cyclic rotation and reversal.

For each two-defect pattern `(18,1)` and `(16,3)`, the full helical-seam enumeration described above again leaves exactly

\[
\boxed{1920}
\tag{8}
\]

seam-compatible candidates, and every candidate has an exact integer witness (5).

For `(16,1,1)`, the same seven-representative normalization produces 6727 canonical defect triples, and every one is already rejected by the first proper 20-column principal strip:

\[
\boxed{6727\longrightarrow0.}
\tag{9}
\]

Therefore

\[
m(105,21)\ge\sqrt8.
\]

This completes the proof of (1). `square`

---

## 4. Reproducibility and trust boundary

The companion script `verify_n5s_19_21_global_obstruction.py` reconstructs the strip and cyclic matrices from the transition masks.  A floating eigensolver is used only to propose integer directions.  A branch or cyclic candidate is rejected only after the exact integer inequality

\[
w^T(M^2-8I)w\ge0
\]

(or its full cyclic analogue) is verified.  Thus floating error may retain an unnecessary candidate but cannot create a false obstruction.

The two-defect candidate count `1920` is stable across all four residual families in this note and also across the corresponding `s=15,17` families.  This stability is evidence for a transfer description of the long complement chain, but no uniform-in-`s` theorem is claimed here.

## Corollary 1.1

On the horizontal resonance `N=5s`, the currently proved odd obstruction points include

\[
\boxed{s\in\{15,17,19,21\}\Longrightarrow m(5s,s)\ge\sqrt8.}
\tag{10}
\]

The positive odd points `s=3,5,7,9,11,13` were proved earlier.  Thus the finite-global data now exhibit a contiguous proved change of behavior between `s=13` and `s=15` through step 21.