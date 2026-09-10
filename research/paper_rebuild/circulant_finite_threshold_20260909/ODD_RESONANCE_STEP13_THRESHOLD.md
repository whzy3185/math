# Exact vertical `sqrt(8)` threshold for step thirteen

The step-thirteen vertical family again has a single obstructed chord-cycle length: the triangle resonance `k=3`.  Every larger chord-cycle length admits a finite signing strictly below `sqrt(8)`.

## Theorem 1

For every admissible integer `k>=3`,

\[
\boxed{m(13k,13)<\sqrt8\iff k\ge4.}
\tag{1}
\]

At `k=3`, the horizontal odd-resonance theorem gives

\[
m(39,13)^2\ge8+\frac2{139}>8.
\tag{2}
\]

Every even `k` is positive by the all-even-order construction.  We treat odd `k>=5` below.

---

## 1. Alternating seam signing for odd `k>=7`

Let `N=13k` with odd `k>=7`.  In Hamilton gauge choose

\[
h_i=1\ (0\le i<N-1),\qquad h_{N-1}=-1,
\]

and

\[
c_i=(-1)^i
\]

on the step-thirteen chords.  Put `K=8I-A^2`.

By the general two-seam-defect decomposition, after multiplication-by-two reindexing,

\[
K=L_\Sigma+E_-+E_+,
\tag{3}
\]

where `L_Sigma` is a signed Laplacian on `C_N(1,13)` and

\[
(E_-)_{0,N-7}=-2,
\qquad
(E_+)_{a,a+6}=+2,
\qquad
 a=\frac{N-13}{2},
\tag{4}
\]

with symmetric transposed entries understood.

Take the base-graph radius-four induced edge sets around the two exceptional pairs.  Once the local pattern has stabilized, the negative absorber has 76 vertices and 128 base edges, and exact rational `LDL^T` factorization has only positive pivots with

\[
\boxed{
\det Q_-=24571566789956681668333404160>0.
}
\tag{5}
\]

The positive absorber has 75 vertices and 124 base edges and

\[
\boxed{
\det Q_+=727573024226645153483653120>0,
}
\tag{6}
\]

again with every exact LDL pivot positive.

For odd `k>=19`, the two radius-four vertex sets are disjoint.  Indeed, lift the negative ball to offsets

\[
\delta+u+13v,
\qquad \delta\in\{0,-7\},\quad |u|+|v|\le4,
\]

which lie in `[-59,52]`.  The positive ball is a translate by

\[
a=\frac{N-13}{2}
\]

of offsets in `[-52,58]`.  When `k>=19`,

\[
a\ge117,
\qquad N-a\ge130,
\]

so the lifted intervals are separated on both sides of the cyclic seam; hence the induced edge sets are disjoint.

Therefore the full quadratic form is the sum of the two positive-definite local forms and the remaining nonnegative signed-edge squares.  Connectivity propagates equality to the zero vector, proving

\[
8I-A^2\succ0
\qquad(k\ge19\text{ odd}).
\tag{7}
\]

---

## 2. Exact finite bases `k=7,9,11,13,15,17`

For the six smaller odd lengths the local neighborhoods overlap, but the same alternating signing is directly positive definite.  Exact rational LDL gives only positive pivots, with determinants

\[
\begin{array}{c|c}
k&\det(8I-A^2)\\ \hline
7&777822683438738293824269088964559041231880192,\\
9&40178111447360478660721529323877341901237465003508791537664,\\
11&834670184595986161898253528412539880891529504123995209158656633956804984,\\
13&14656605269736600831818047041457539635031211796660386607258337268810764502635306436552,\\
15&243585933444252138485512585640693612321567484386234437066272326258045709008024992175761023618919552,\\
17&3963174854812045796053420102968566538099459483102725723763065164924888915802214672795545687441379572817116286024.
\end{array}
\tag{8}
\]

Thus every odd `k>=7` is strictly sub-threshold.

---

## 3. The remaining odd base `k=5`

For `N=65`, the unmodified alternating chord word is not used.  Start from `c_i=(-1)^i` and reverse exactly the adjacent signs

\[
c_{54},\ c_{55}.
\tag{9}
\]

Keep the negative Hamilton seam.  For this explicit integer matrix, exact rational LDL of `8I-A^2` has 65 positive pivots and

\[
\boxed{
\det(8I-A^2)=268663021725556297527269942728>0.
}
\tag{10}
\]

Hence

\[
m(65,13)<\sqrt8.
\tag{11}
\]

All certificates in this note are reconstructed by `verify_step13_subsqrt8_local.py` without floating-point acceptance.

Combining (2), the even-order theorem, (7)--(11) proves Theorem 1. `square`

---

## Corollary 1.1

For fixed odd steps through thirteen the exact vertical threshold is now

\[
\begin{array}{c|c}
s&m(sk,s)<\sqrt8\\ \hline
3&k\ge3,\\
5&k\ge3,\\
7,9,11,13&k\ge4.
\end{array}
\tag{12}
\]

This gives four consecutive odd steps for which the only obstruction is the chord-triangle line `k=3`.