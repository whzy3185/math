# Every step-three resonance lies below `sqrt(8)`

This note gives a new positive theorem on the odd-resonance side of the second threshold.  It is finite and global over all edge signings: one explicit signing is constructed and proved strictly sub-threshold by an elementary signed-Laplacian decomposition.

## Theorem 1

For every integer `k>=3`,

\[
\boxed{m(3k,3)<\sqrt8.}
\tag{1}
\]

For even `k`, this is already a consequence of the all-even-order theorem because `N=3k` is even.  The new content is therefore

\[
\boxed{k\ge3\text{ odd}\Longrightarrow m(3k,3)<\sqrt8.}
\tag{2}
\]

### Construction for odd `k`

Put

\[
N=3k,
\qquad k\ge3\text{ odd}.
\]

Thus `N` is odd.  In Hamilton gauge let the step-one signs be

\[
h_i=1\quad(0\le i\le N-2),
\qquad
h_{N-1}=-1,
\tag{3}
\]

and let the step-three signs be

\[
c_i=(-1)^i,
\qquad 0\le i<N.
\tag{4}
\]

Let `A` be the resulting signed adjacency matrix.  We prove

\[
8I-A^2\succ0.
\tag{5}
\]

This implies `rho(A)<sqrt(8)` and hence (2).

---

## 1. Exact two-walk calculation

Put

\[
B=A^2-4I,
\qquad
K=8I-A^2=4I-B.
\tag{6}
\]

Apart from the diagonal, a two-step walk can have displacement only

\[
\pm2,\quad\pm4,\quad\pm6.
\]

With all indices interpreted modulo `N`, direct enumeration of the intermediate vertices gives

\[
B_{x,x+2}
=h_xh_{x+1}+h_{x-1}c_{x-1}+c_xh_{x+2},
\tag{7}
\]

\[
B_{x,x+4}
=h_xc_{x+1}+c_xh_{x+3},
\tag{8}
\]

and

\[
B_{x,x+6}=c_xc_{x+3}.
\tag{9}
\]

Substituting (3)--(4), using that `N` is odd, yields the exact table

\[
B_{x,x+2}=
\begin{cases}
+1,&0\le x\le N-4,\\
-1,&x=N-3,N-2,N-1,
\end{cases}
\tag{10}
\]

\[
B_{x,x+4}=
\begin{cases}
2,&x=N-4,\\
0,&\text{otherwise},
\end{cases}
\tag{11}
\]

and

\[
B_{x,x+6}=
\begin{cases}
-1,&0\le x\le N-4,\\
+1,&x=N-3,N-2,N-1.
\end{cases}
\tag{12}
\]

No floating-point spectral calculation is involved in these identities.

---

## 2. Reindexing exposes one exceptional edge

Because `N` is odd, multiplication by `2` is a permutation of `Z_N`.  Reindex the vertices by

\[
\pi(j)=2j\pmod N.
\tag{13}
\]

Under this permutation, the displacement-two and displacement-six entries in (10),(12) become respectively step-one and step-three edges.  Every such off-diagonal entry of `K` is `+-1`.

The unique entry (11) becomes

\[
K_{0,N-2}=K_{N-2,0}=-2.
\tag{14}
\]

Hence

\[
\boxed{K=L_\Sigma+E,}
\tag{15}
\]

where:

- `Sigma` is an edge-signed copy of the 4-regular graph `C_N(1,3)`;
- `L_Sigma` is its signed Laplacian, so
  \[
  (L_\Sigma)_{ii}=4,
  \qquad
  (L_\Sigma)_{ij}=-\sigma_{ij}
  \]
  on its signed edges;
- `E` has only the two symmetric entries
  \[
  E_{0,N-2}=E_{N-2,0}=-2
  \tag{16}
  \]
  and zero diagonal.

Thus, for every real vector `x`,

\[
x^TL_\Sigma x
=\sum_{\{i,j\}\in E(C_N(1,3))}
(x_i-\sigma_{ij}x_j)^2\ge0,
\tag{17}
\]

while

\[
x^TEx=-4x_0x_{N-2}.
\tag{18}
\]

The whole issue is to absorb this single indefinite term.

---

## 3. Three negative two-edge paths absorb the exceptional edge

Set

\[
u=0,
\qquad
v=N-2.
\]

In the signed graph `Sigma`, the vertices `u,v` are joined by the three edge-disjoint length-two paths

\[
0-1-(N-2),
\tag{19}
\]

\[
0-(N-3)-(N-2),
\tag{20}
\]

and

\[
0-(N-1)-(N-2).
\tag{21}
\]

Their six `K`-entries are, directly from (10),(12) after the reindexing,

\[
K_{0,1}=-1,
\qquad
K_{1,N-2}=+1,
\tag{22}
\]

\[
K_{0,N-3}=+1,
\qquad
K_{N-3,N-2}=-1,
\tag{23}
\]

and

\[
K_{0,N-1}=+1,
\qquad
K_{N-1,N-2}=-1.
\tag{24}
\]

Since `sigma_ij=-K_ij` on the signed-Laplacian edges, the product of the two edge signs on each path is `-1`.

Consider any one such path `u-w-v`, with

\[
\sigma_{uw}\sigma_{wv}=-1.
\]

Writing `a=x_u`, `b=x_v`, and `y=sigma_uw x_w`, its two edge energies are

\[
(a-y)^2+(y+b)^2
\ge\frac12(a+b)^2.
\tag{25}
\]

The three paths are edge-disjoint, so their six edge energies are distinct terms of (17).  Summing (25) over them gives

\[
\text{path energy}\ge\frac32(x_u+x_v)^2.
\tag{26}
\]

Combining (18) and (26),

\[
\frac32(x_u+x_v)^2-4x_ux_v
=(x_u-x_v)^2+rac12(x_u+x_v)^2.
\tag{27}
\]

The right-hand side is positive definite in `(x_u,x_v)`.  All remaining signed-Laplacian edge energies are nonnegative.  Consequently

\[
x^TKx\ge0.
\tag{28}
\]

In fact equality is impossible for nonzero `x`.  If `x^TKx=0`, (27) first forces

\[
x_u=x_v=0.
\]

Then equality in the three path-energy terms forces the three intermediate coordinates also to vanish.  Equality in every remaining square in (17) forces every coordinate to propagate from zero along the connected step-one Hamilton cycle.  Hence `x=0`.

Therefore

\[
\boxed{K=8I-A^2\succ0.}
\tag{29}
\]

This proves (2), and the even-`k` theorem completes (1). `square`

---

## Corollary 1.1

The odd-resonance `sqrt(8)` frontier cannot be governed by chord-cycle parity alone.  Even when the chord-cycle length `k` is arbitrarily large and odd, the entire vertical family

\[
C_{3k}(1,3)
\]

stays strictly below `sqrt(8)`.

This should be contrasted with the previously proved horizontal triangle-resonance family

\[
C_{3s}(1,s),
\]

where odd `s>=7` satisfies

\[
m(3s,s)^2\ge8+\frac2{139}.
\]

Thus the obstruction at `sqrt(8)` depends on the geometry of the step relative to the order, not merely on an odd cycle length.
