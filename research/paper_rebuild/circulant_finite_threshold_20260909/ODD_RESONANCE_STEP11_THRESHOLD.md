# Exact vertical `sqrt(8)` threshold for step eleven

The step-eleven vertical family continues the pattern seen at steps seven and nine: the chord-cycle-length-three point is globally obstructed, but every larger chord-cycle length admits a finite sub-`sqrt(8)` signing.

## Theorem 1

For every admissible integer `k>=3`,

\[
\boxed{m(11k,11)<\sqrt8\iff k\ge4.}
\tag{1}
\]

The unique negative point is `(N,s)=(33,11)`.  The horizontal odd-resonance obstruction already gives

\[
m(33,11)^2\ge 8+\frac2{139}>8.
\tag{2}
\]

If `k` is even, then `N=11k` is even and the all-even-order theorem gives the strict upper bound.  It remains to treat odd `k>=5`.

---

## 1. The alternating seam signing for odd `k>=7`

Let

\[
N=11k,
\qquad k\ge7\text{ odd}.
\]

Use Hamilton gauge

\[
h_i=1\quad(0\le i<N-1),
\qquad h_{N-1}=-1,
\tag{3}
\]

and chord signs

\[
c_i=(-1)^i.
\tag{4}
\]

Let `A` be the signed adjacency matrix and put

\[
K=8I-A^2.
\tag{5}
\]

The general two-seam-defect theorem `ODD_RESONANCE_SEAM_DEFECT_FRAMEWORK.md` applies.  After reindexing by multiplication by two on `Z_N`,

\[
K=L_\Sigma+E_-+E_+,
\tag{6}
\]

where `L_Sigma` is the signed Laplacian of a signed copy of `C_N(1,11)` and the only non-Laplacian entries are

\[
(E_-)_{0,N-6}=(E_-)_{N-6,0}=-2
\tag{7}
\]

and

\[
(E_+)_{a,a+5}=(E_+)_{a+5,a}=+2,
\qquad a=\frac{N-11}{2}.
\tag{8}
\]

### Fixed radius-four absorbers

For either exceptional pair `e`, let `B_4(e)` be the vertices at base-graph distance at most four from the endpoints of `e`, and let `F_4(e)` be the base edges induced by this set.  Define the local form by summing the signed edge squares on `F_4(e)` and adding the corresponding exceptional bilinear term.

For the negative pair (7), the stable local support has 69 vertices and 116 base edges.  Exact rational `LDL^T` factorization has only positive pivots, with determinant

\[
\boxed{58357331759813608134646848>0.}
\tag{9}
\]

For the positive pair (8), the support has 70 vertices and 120 base edges.  Again every exact `LDL^T` pivot is positive, and

\[
\boxed{1526739500502872793417814448>0.}
\tag{10}
\]

Hence both local forms are positive definite.

For `k>=19`, these two radius-four edge sets are disjoint.  One elementary way to see this is to lift the two balls to the integers.  The negative ball is contained in translates

\[
\delta+u+11v,
\qquad \delta\in\{0,-6\},\quad |u|+|v|\le4,
\]

so its offsets from zero lie between `-50` and `44`.  The positive ball is a translate by

\[
a=\frac{N-11}{2}
\]

of offsets between `-44` and `49`.  Thus a common vertex would force either

\[
a\le 88
\quad\text{or}\quad
N-a\le99.
\]

For odd `k>=19`, however,

\[
a=\frac{11(k-1)}2\ge99,
\qquad
N-a=\frac{11(k+1)}2\ge110,
\]

and direct inspection of the endpoint values at `k=19` removes the non-strict first inequality; equivalently the exact residue sets in the verification script are disjoint.  Therefore the two induced edge sets are disjoint for all larger odd `k` as well.

Consequently the full quadratic form is the sum of the two positive-definite absorber forms and the remaining nonnegative signed-edge squares.  Equality would force all coordinates in the absorber supports to vanish and then propagate zero through the connected base graph.  Hence

\[
8I-A^2\succ0
\qquad(k\ge19\text{ odd}).
\tag{11}
\]

---

## 2. Exact finite bases `k=7,9,11,13,15,17`

For these six odd chord-cycle lengths the two radius-four neighborhoods overlap, so we certify the same alternating signing directly.  Exact rational `LDL^T` factorization of the full matrix `8I-A^2` has only positive pivots.  The exact determinants are

\[
\begin{array}{c|c}
k&\det(8I-A^2)\\ \hline
7&198542354710744646733800591160528965128,\\
9&48537546289326974482796577064517737666501709538432,\\
11&8431528717945196619704965506489933748444911718619217528033864,\\
13&1347032891519196209768694990441713139707122120299552652026241225001964664,\\
15&209465313694967800022162339333057752681888819639940779892042386917708086880013123584,\\
17&32248803804806512732626264860337508296200192468837035466855251667015901045281842241991056567032.
\end{array}
\tag{12}
\]

Thus the alternating seam signing is strictly sub-threshold for every odd `k>=7`.

---

## 3. The remaining odd base `k=5`

For `N=55` the pure alternating chord word is slightly above the threshold, so it is not used as a certificate.  Instead keep the Hamilton seam (3), start with `c_i=(-1)^i`, and reverse precisely the two adjacent chord signs

\[
c_{40},\ c_{41}.
\tag{13}
\]

For this explicit signing, exact rational `LDL^T` factorization of

\[
8I-A^2
\]

has 55 positive pivots and determinant

\[
\boxed{64811885930109544285440000>0.}
\tag{14}
\]

Therefore

\[
m(55,11)<\sqrt8.
\tag{15}
\]

The script `verify_step11_subsqrt8_local.py` reconstructs all matrices above using integer arithmetic and verifies every stated positive pivot and determinant.

Combining (2), the even-order theorem, (11)--(15) proves Theorem 1. `square`

---

## Corollary 1.1

The controlled vertical families now include

\[
\begin{array}{c|c}
\text{fixed step}&m(sk,s)<\sqrt8\\ \hline
3&k\ge3,\\
5&k\ge3,\\
7&k\ge4,\\
9&k\ge4,\\
11&k\ge4.
\end{array}
\tag{16}
\]

Thus the horizontal obstruction at chord-cycle length three persists at step eleven, but disappears already at length five.