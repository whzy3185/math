# Exact vertical `sqrt(8)` threshold for step seven

The next vertical resonance already displays a genuine threshold.  The horizontal odd-triangle obstruction gives a negative base point at chord-cycle length three, while the signed-Laplacian construction becomes positive for every larger chord-cycle length.

## Theorem 1

For every admissible integer `k>=3`,

\[
\boxed{
 m(7k,7)<\sqrt8
 \iff
 k\ge4.
}
\tag{1}
\]

Equivalently, the unique non-sub-threshold member of the vertical family `C_(7k)(1,7)` is

\[
(N,s)=(21,7).
\]

Indeed the previously proved exhaustive certificate gives

\[
m(21,7)^2\ge8+\frac{18}{131}>8.
\tag{2}
\]

If `k` is even, `N=7k` is even and the all-even-order theorem gives `m(7k,7)<sqrt(8)`.  It remains to prove the result for odd `k>=5`.

---

## 1. The explicit odd-order signing

Let

\[
N=7k,
\qquad k\ge5\text{ odd}.
\]

In Hamilton gauge take

\[
h_i=1\quad(0\le i<N-1),
\qquad h_{N-1}=-1,
\tag{3}
\]

and step-seven chord signs

\[
c_i=(-1)^i.
\tag{4}
\]

Let `A` be the signed adjacency matrix and put

\[
K=8I-A^2.
\tag{5}
\]

Reindex by multiplication by `2` on `Z_N`.  A direct two-walk expansion gives

\[
\boxed{K=L_\Sigma+E_-+E_+,}
\tag{6}
\]

where `L_Sigma` is a signed Laplacian on an edge-signed copy of `C_N(1,7)`, and the only two non-Laplacian off-diagonal entries are

\[
(E_-)_{0,N-4}=(E_-)_{N-4,0}=-2
\tag{7}
\]

and

\[
(E_+)_{a,a+3}=(E_+)_{a+3,a}=+2,
\qquad
 a=\frac{N-7}{2}.
\tag{8}
\]

All other nonzero off-diagonal entries of `K` are `+-1` on the step-one or step-seven base edges.  This exact decomposition is independently checked in `verify_step7_subsqrt8_local.py`.

---

## 2. Fixed local absorbers for every odd `k>=9`

Use the base-graph ball notation from the step-five theorem.  Around the negative exceptional pair take all base edges induced by radius two,

\[
F_-=F_2(\{0,N-4\}),
\]

and define the corresponding local quadratic form including the `-2` exceptional edge.  Its support has 23 vertices.  In increasing-label order its exact leading principal minors are

\[
\boxed{
\begin{aligned}
&4,15,41,149,257,514,1661,2238,1522,926,926,926,1852,\\
&4630,7408,14816,32064,64320,143896,143420,234860,326300,334960.
\end{aligned}}
\tag{9}
\]

All are positive, so this local matrix is positive definite.

Around the positive exceptional pair use

\[
F_+=F_2(\{a,a+3\}).
\]

Its support has 24 vertices, and its exact leading principal minors are

\[
\boxed{
\begin{aligned}
&1,1,2,5,13,34,89,233,610,1832,5536,16936,52130,95889,\\
&308833,671461,1296585,3966311,8547891,17810059,\\
&49673831,56657395,32920956,16015428.
\end{aligned}}
\tag{10}
\]

Again all are positive.

For every odd `k>=9`, the allocated edge sets `F_-` and `F_+` are disjoint.  Hence the full form `x^TKx` is the sum of these two positive-definite local forms and the nonnegative signed-edge squares from every unallocated base edge.  Equality would force the local coordinates to zero and then propagate zero through the connected base graph.  Thus

\[
8I-A^2\succ0
\qquad(k\ge9\text{ odd}).
\tag{11}
\]

---

## 3. Exact finite bases `k=5,7`

For `k=5` (`N=35`) and `k=7` (`N=49`) the two radius-two absorber edge sets overlap, so the disjoint local decomposition above is not used.  Instead the same explicit signing (3)--(4) is certified directly by exact Sylvester tests.

For `N=35`, every one of the 35 leading principal minors of `8I-A^2` is a positive integer; the final determinant is

\[
210822313025982584>0.
\tag{12}
\]

For `N=49`, all 49 leading principal minors are positive; the final determinant is

\[
4439255509339435940222344>0.
\tag{13}
\]

The complete exact minor lists are recomputed by `verify_step7_subsqrt8_local.py`; no floating-point comparison is used for acceptance.

Therefore the explicit signing is strictly sub-`sqrt(8)` for every odd `k>=5`.  Combining this with the even-order theorem and the negative base case (2) proves (1). `square`

---

## Corollary 1.1

The first three vertical resonances are now known exactly at the `sqrt(8)` threshold:

\[
\begin{array}{c|c}
\text{fixed step}&\text{sub-}\sqrt8\text{ chord-cycle lengths}\\ \hline
3&k\ge3,\\
5&k\ge3,\\
7&k\ge4.
\end{array}
\tag{14}
\]

In particular the point `(21,7)` is not representative of the whole step-seven family: the obstruction disappears as soon as the chord-cycle length increases beyond three.
