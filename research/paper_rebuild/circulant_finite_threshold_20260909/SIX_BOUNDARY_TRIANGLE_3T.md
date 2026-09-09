# The final triangle locus `q=3t` and the complete `m^2=6` theorem

This note closes the last arithmetic locus left by the non-strict six-boundary reduction.

## Theorem 1 (component obstruction on the triangle resonance)

For every integer `t>=3`, every signing `C` of

\[
X_t:=C_{3t}(1,t)
\]

satisfies

\[
\boxed{\lambda_{\max}(C)>2.}
\tag{1}
\]

Thus no reduced parity component on `q=3t`, `t>=3`, can occur in a signing of an original two-step circulant with squared spectral radius at most six.

The proof is local.

---

## 1. Every chord triangle would have to be negative

The step-`t` edges of `X_t` form `t` disjoint triangles

\[
\{a,a+t,a+2t\},
\qquad a=0,\ldots,t-1.
\]

Suppose `lambda_max(C)<=2`.  If one of these signed triangles had positive flux, switch its three vertices so that its three internal edges are positive.  The vector `(1,1,1)` on that triangle has Rayleigh quotient `2`.  Its zero extension to the whole graph would therefore attain the global largest eigenvalue and hence would be a `2`-eigenvector of `C`.

For `t>=3`, every Hamilton neighbour immediately outside the triangle is adjacent to exactly one of its three vertices.  The eigenvalue equation at such an outside vertex would then read `0=+-1`, an impossibility.

Hence every chord triangle has negative flux.

Because the chord triangles are vertex-disjoint, switch within each triangle so that all three of its chord edges have sign `-1`.  We use this gauge below.

---

## 2. The local three-column strip for `t>=4`

Write a vertex as

\[
a+rt,
\qquad
0\le a<t,
\qquad
r\in\{0,1,2\}.
\]

A fixed `a` is a chord-triangle column.  For `t>=4`, the three consecutive columns `a=0,1,2` induce exactly:

- three all-negative copies of `K_3`;
- a signed perfect matching between columns `0` and `1`;
- a signed perfect matching between columns `1` and `2`;
- no other edges.

Let

\[
a=(a_1,a_2,a_3),
\qquad
b=(b_1,b_2,b_3)
\]

be the two matching sign triples.  Switching an entire column globally negates one adjacent sign triple without changing the negative chord triangles, and simultaneous permutation of the three row labels preserves the local graph.  Under these operations the `2^6=64` sign patterns reduce to exactly five types:

\[
\begin{array}{c|c}
\text{type}&(a,b)\\ \hline
I&(---,---)\\
II&(---,--+)\\
III&(--+,---)\\
IV&(--+,--+)\\
V&(--+,-+-).
\end{array}
\tag{2}
\]

Let `L` denote the signed adjacency matrix of this 9-vertex principal subgraph.  Exact determinant expansion gives:

\[
\begin{array}{c|l}
I&(x-1)^2(x+2)(x^2-2x-1)^2(x^2+4x+2)\\[1mm]
II,III&(x-1)(x^2-2x-1)
(x^6+3x^5-7x^4-19x^3+12x^2+22x-4)\\[1mm]
IV&(x-1)^2(x+2)(x^2-2x-1)
(x^4+2x^3-7x^2-8x+14)\\[1mm]
V&(x-2)(x-1)(x^2+2x-1)
(x^5+x^4-9x^3-5x^2+18x+2).
\end{array}
\tag{3}
\]

The first four types have the eigenvalue

\[
1+\sqrt2>2.
\]

For Type V, the final quintic `p(x)` satisfies

\[
p(2)=-6,
\qquad
p(x)\to+\infty\quad(x\to+\infty),
\]

so it has a real root strictly larger than `2`.  Therefore every local type in (2) has

\[
\lambda_{\max}(L)>2.
\]

Interlacing now gives `lambda_max(C)>2`, contradicting the assumed upper bound.  This proves Theorem 1 for `t>=4`.

The five exact characteristic-polynomial identities are reproduced in `verify_3t_local_strip.py`.

---

## 3. The remaining component `C_9(1,3)`

It remains to treat `t=3`.  There are exactly three chord-triangle columns, so the third column wraps back to the first and the preceding 9-vertex strip is no longer induced.  A Gram-kernel argument avoids enumeration.

Take two adjacent columns.  After the negative-triangle gauge their six-vertex principal signed adjacency matrix has block form

\[
L_2=
\begin{pmatrix}
K&D\\
D&K
\end{pmatrix},
\qquad
K=I_3-J_3,
\]

where `D` is diagonal with entries `+-1`.  Put

\[
G_2=2I-L_2.
\]

Up to switching one whole column and simultaneously permuting the three rows, `D` has only two forms:

\[
D=-I
\qquad\text{or}\qquad
D=\operatorname{diag}(-1,-1,+1).
\tag{4}
\]

In the first case

\[
\ker G_2
=\{(x,-x):\mathbf1^Tx=0\},
\tag{5}
\]

which has dimension two.  In the second case it contains the nonzero vector

\[
((1,-1,0),(-1,1,0)).
\tag{6}
\]

Now suppose the full `9x9` Gram matrix

\[
G=2I-C
\]

were positive semidefinite.  For a positive semidefinite block matrix, every vector in the kernel of a principal diagonal block must also be annihilated by the corresponding off-diagonal block.  Thus every vector in (5), or the vector (6), must couple to zero at the third column.

The third column is joined to the second by a signed diagonal matching `D_1`, and to the first by a signed matching whose underlying permutation is a 3-cycle; write the latter as the signed monomial matrix `M`.

### Mixed matching in (4)

For the kernel vector (6), the first-column and second-column parts are `x=(1,-1,0)` and `-x`.  A diagonal signed matrix preserves the position of the unique zero of `x`, whereas a signed 3-cycle monomial matrix moves that zero to a different coordinate.  Hence

\[
Mx-D_1x\ne0,
\]

contradicting the required zero coupling.

### Constant matching in (4)

For every `x` with `1^Tx=0`, zero coupling would require

\[
Mx=D_1x.
\]

Thus the signed monomial matrix

\[
Q=D_1^{-1}M
\]

would act as the identity on the two-dimensional subspace `1^perp`.  But the underlying permutation of `Q` is a 3-cycle, so

\[
Q^3=\delta I,
\qquad \delta\in\{\pm1\},
\]

and its characteristic polynomial is `x^3-delta`.  Every eigenvalue is simple.  It cannot have a two-dimensional `1`-eigenspace.  This is again a contradiction.

Therefore `C_9(1,3)` admits no signing of index at most two, completing the proof of Theorem 1. `square`

---

# 4. Complete equality classification for the original problem

We now combine the entire six-boundary chain.

## Theorem 2 (complete `sqrt(6)` equality theorem)

For every admissible pair

\[
2\le s<N/2,
\]

one has

\[
\boxed{
 m(N,s)^2=6
 \iff
 (N,s)\in
 \{(12,4),(16,3),(16,5),(20,8)\}.
}
\tag{7}

### Proof

The complete strict sub-six theorem already classifies every pair with `m^2<6`; in particular the flat and `N=4s` families are strictly below six.

For every remaining pair, `SIX_BOUNDARY_ARITHMETIC_LOCALIZATION.md` shows that a signing with `rho(A)^2<=6` can exist only on

\[
t=2,
\qquad q=2t+1,
\qquad q=2t+2,
\qquad q=3t.
\]

The preceding boundary papers give:

1. `t=2`: equality only at `(12,4)` and `(20,8)`;
2. `q=2t+1`: no equality at all;
3. `q=2t+2`: equality only at `(12,4),(16,3),(16,5)`;
4. `q=3t`: by Theorem 1 no component can occur for `t>=3`; the remaining `t=2` case is already included in the `t=2` classification and contributes only `(12,4)`.

Thus the only possible equality pairs are the four in (7).  Exact constructions for all four were already proved in `SIX_BOUNDARY_ROOT_QUOTIENT.md`, so all four are attained. `square`

---

## Corollary 2.1 (complete trichotomy through the six threshold)

Let `beta` be the largest root of `x^3-7x+7`.  Then every admissible pair belongs to exactly one of the following three classes:

### Strictly below six

\[
\begin{array}{c|c}
N=2s+2&m^2=4,\\
(N,s)=(5,2),(10,3)&m^2=5,\\
N=4s&m^2=4+2\cos(\pi/(2s)),\\
N=14,\ s=3,4,5&m^2=4+\beta.
\end{array}
\]

### Exactly at six

\[
(N,s)=(12,4),(16,3),(16,5),(20,8).
\]

### Strictly above six

Every other admissible pair satisfies

\[
\boxed{m(N,s)>\sqrt6.}
\tag{8}
\]

This is a complete finite-global classification of the first nontrivial spectral threshold above the flat regime.
