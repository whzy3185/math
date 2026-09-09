# Every step-five resonance lies below `sqrt(8)`

The signed-Laplacian mechanism from the step-three theorem extends one level further.  The finite defect now contains two exceptional entries, but for all sufficiently large odd chord-cycle lengths they are absorbed by two fixed local positive-definite blocks.

## Theorem 1

For every integer `k>=3`,

\[
\boxed{m(5k,5)<\sqrt8.}
\tag{1}
\]

For even `k`, the order `N=5k` is even, so the all-even-order theorem already gives (1).  We therefore assume below that `k` is odd.

The case `k=3` is the already proved exact certificate

\[
m(15,5)<\sqrt8.
\tag{2}
\]

It remains to handle odd `k>=5`.

---

## 1. The explicit signing and its two exceptional entries

Put

\[
N=5k.
\]

In Hamilton gauge choose

\[
h_i=1\quad(0\le i\le N-2),
\qquad
h_{N-1}=-1,
\tag{3}
\]

for the step-one edges and

\[
c_i=(-1)^i
\tag{4}
\]

for the step-five edges.  Let `A` be the resulting signed adjacency matrix and put

\[
K=8I-A^2.
\tag{5}
\]

Because `N` is odd, multiplication by `2` permutes `Z_N`.  Reindex by

\[
\pi(j)=2j\pmod N.
\tag{6}
\]

A direct two-walk calculation gives the following exact structure.

### Lemma 1.1

After the reindexing (6), every nonzero off-diagonal entry of `K` is a `+-1` entry on an edge of `C_N(1,5)`, except for exactly two entries:

\[
K_{0,N-3}=-2
\tag{7}
\]

and

\[
K_{a,a+2}=+2,
\qquad
 a=\frac{N-5}{2}.
\tag{8}
\]

Consequently

\[
\boxed{K=L_\Sigma+E_-+E_+,}
\tag{9}
\]

where `L_Sigma` is the signed Laplacian of an edge-signed copy of `C_N(1,5)`, while `E_-` and `E_+` contain only the symmetric off-diagonal pairs in (7),(8), respectively.

The proof is the same finite channel expansion as in the step-three note: the step-one and pure step-five two-walk channels become the `+-1` base edges, while the seam leaves exactly one residual mixed term in each of the two mixed displacements.  The exact identities are checked independently in `verify_step5_subsqrt8_local.py`.

For every real vector `x`,

\[
x^TL_\Sigma x
=\sum_{\{i,j\}}(x_i-\sigma_{ij}x_j)^2.
\tag{10}
\]

Thus only the two exceptional bilinear terms need control.

---

## 2. Two fixed local absorbers for every odd `k>=7`

Work in the underlying base graph `C_N(1,5)` from (9), carrying the exact signs inherited from `K`.

For an exceptional pair `e={u,v}`, let `B_r(e)` denote the vertices at base-graph distance at most `r` from `u` or `v`, and let `F_r(e)` be the set of base edges whose two endpoints both lie in `B_r(e)`.

Define

\[
Q_-:=\sum_{ij\in F_1(\{0,N-3\})}
(x_i-\sigma_{ij}x_j)^2-4x_0x_{N-3},
\tag{11}
\]

and

\[
Q_+:=\sum_{ij\in F_2(\{a,a+2\})}
(x_i-\sigma_{ij}x_j)^2+4x_ax_{a+2}.
\tag{12}
\]

For every odd `k>=7`, these two local signed patterns are independent of `k` up to relabelling.  The first has 10 vertices.  In increasing-label order, the leading principal minors of its exact integer matrix are

\[
\boxed{
4,11,18,13,13,21,36,27,18,12.
}
\tag{13}
\]

The second has 19 vertices, with leading principal minors

\[
\boxed{
\begin{aligned}
&1,1,2,5,13,34,89,269,818,2521,5601,18533,\\
&41560,130852,301184,929024,1162752,732444,420480.
\end{aligned}}
\tag{14}
\]

Every number in (13)--(14) is positive.  Sylvester's criterion therefore gives

\[
Q_->0,
\qquad
Q_+>0
\tag{15}
\]

on their respective coordinate spaces.

For odd `k>=7`, the two local edge sets

\[
F_1(\{0,N-3\}),
\qquad
F_2(\{a,a+2\})
\]

are disjoint.  Hence the full quadratic form decomposes exactly as

\[
x^TKx
=Q_-+Q_+
+\sum_{ij\in E(C_N(1,5))\setminus(F_1\cup F_2)}
(x_i-\sigma_{ij}x_j)^2.
\tag{16}
\]

Every term on the right is nonnegative.  If equality held, the positive definiteness in (15) would force all coordinates in the two local supports to vanish.  The remaining edge-square equations then propagate zero through the connected base graph (all edges crossing the local balls belong to the remaining sum).  Thus `x=0`.

Therefore

\[
\boxed{8I-A^2\succ0}
\tag{17}
\]

for every odd `k>=7`.

---

## 3. The remaining odd case `k=5`

Here `N=25`; the two local edge sets used above overlap, so we do not claim the decomposition (16).  Instead we certify the same explicit signing directly.

For its exact integer matrix `K=8I-A^2`, the 25 leading principal minors are

\[
\begin{aligned}
&4,16,60,225,840,3136,11704,43681,163020,608400,\\
&2109120,7311616,24747008,83759104,282174464,866853120,\\
&2660537664,7809976464,22923102260,45930833425,\\
&137043447130,386860210844,1086784172626,2676007398625,\\
&4179320749384.
\end{aligned}
\tag{18}
\]

All are positive, so Sylvester's criterion gives

\[
8I-A^2\succ0.
\tag{19}
\]

Together with (2), (17), and the all-even-order theorem, this proves (1). `square`

---

## Corollary 1.1

The positive side of the odd-resonance `sqrt(8)` problem now contains two complete vertical families:

\[
\boxed{
 m(3k,3)<\sqrt8,
 \qquad
 m(5k,5)<\sqrt8
 \quad(k\ge3).
}
\tag{20}
\]

This reinforces the conclusion that the negative theorem on the horizontal line `N=3s`, odd `s>=7`, is a genuinely geometric resonance phenomenon rather than a consequence of odd order or odd chord-cycle length alone.
