# Complete strict sub-`sqrt(6)` classification

This note belongs entirely to the finite-global paper.  It uses no result from the periodic/Bloch project.  The only external structural input is the published classification of connected edge-signed graphs with smallest eigenvalue strictly greater than `-2` by Greaves--Koolen--Munemasa--Sano--Taniguchi, *J. Combin. Theory Ser. B* 110 (2015), 90--111.

Throughout,

\[
2\le s<N/2,\qquad G=C_N(1,s),\qquad A=A_\sigma,
\]

and

\[
B:=A^2-4I,\qquad M:=\lambda_{\max}(B).
\]

Since `A` is real symmetric,

\[
\rho(A)^2=\lambda_{\max}(A^2)=4+M. \tag{1}
\]

Let `beta` be the largest real root of

\[
x^3-7x+7=0.
\]

Thus

\[
\beta=1.692021471630095\ldots<2. \tag{2}
\]

## Theorem A: complete strict sub-six classification

For every admissible pair `(N,s)`,

\[
\boxed{m(N,s)^2<6}
\]

if and only if exactly one of the following holds.

1. `N=2s+2`; then
   \[
   m(N,s)^2=4.
   \]
2. `(N,s)=(5,2)` or `(10,3)`; then
   \[
   m(N,s)^2=5.
   \]
3. `N=4s`; then
   \[
   m(4s,s)^2=4+2\cos\frac{\pi}{2s}.
   \]
4. `N=14` and `s\in\{3,4,5\}`; then
   \[
   m(14,s)^2=4+\beta.
   \]

Consequently, every parameter pair outside these four families satisfies

\[
\boxed{m(N,s)^2\ge6.} \tag{3}
\]

The first three alternatives are established independently in the low-end and `N=4s` sections.  The proof below supplies the global exclusion and the order-14 exceptional family.

---

## 1. Strictly below six, the defect support is forced

The parity-defect identity is

\[
\operatorname{supp}(B\bmod2)=
\begin{cases}
\varnothing,&N=2s+2,\\[1mm]
\operatorname{Cay}(\mathbb Z_N,\{\pm2\}),&N=4s,\\[1mm]
\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}),&\text{otherwise}.
\end{cases} \tag{4}
\]

Indeed, over `F_2[Z_N]`,

\[
(x+x^{-1}+x^s+x^{-s})^2
=x^2+x^{-2}+x^{2s}+x^{-2s}.
\]

Assume now that `N` is neither `2s+2` nor `4s`, and suppose

\[
\rho(A)^2<6.
\]

By (1), `M<2`.  Every off-diagonal entry `b_ij` occurs in the principal block

\[
\begin{pmatrix}0&b_{ij}\\b_{ij}&0\end{pmatrix},
\]

so interlacing gives `|b_ij|\le M<2`.  Since `B` is integral,

\[
b_{ij}\in\{0,\pm1\}. \tag{5}
\]

Equation (4) and (5) therefore imply that every parity-support entry is `+-1` and every off-support entry is zero.  Hence `B` is exactly a signed adjacency matrix of

\[
P_{N,s}:=\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}). \tag{6}
\]

Put

\[
d:=\gcd(N,2),\qquad q:=N/d.
\]

The graph `P_{N,s}` has `d` connected components, each of order `q`; after choosing a generator of the parity coset, each component is a connected 4-regular circulant.  If `C` is one signed component of `B`, then

\[
\lambda_{\max}(C)<2,
\]

so the edge-signed graph with adjacency matrix `-C` has smallest eigenvalue strictly greater than `-2`.  This is exactly the range classified by Greaves et al.

---

## 2. A 4-regular consequence of the Greaves classification

### Lemma 2.1

Let `Gamma` be a connected 4-regular edge-signed graph with smallest eigenvalue greater than `-2`.  If `|V(Gamma)|\ge9`, then no such graph exists.

More precisely: among the integrally represented cases in the Greaves--Koolen--Munemasa--Sano--Taniguchi classification, the only 4-regular underlying graph is `K_5`.

### Proof

Greaves et al., Theorem 19, shows that every exceptional edge-signed graph with smallest eigenvalue greater than `-2` has order `6`, `7`, or `8`.  Thus a graph of order at least `9` is integrally represented.  Their Theorem 6 describes its representation graph `H`: `H` is a simple tree, a unicyclic graph, or a tree with one doubled edge.  The underlying graph of `Gamma` is the line graph of `H` (with the standard doubled-edge interpretation in the third case).

First suppose `H` is simple.  For every edge `uv` of `H`, 4-regularity of `L(H)` gives

\[
d_H(u)+d_H(v)-2=4,
\]

hence

\[
d_H(u)+d_H(v)=6. \tag{7}
\]

If `H` is a tree, choose a leaf.  Its neighbour has degree `5`, and (7) forces every other neighbour of that degree-5 vertex to have degree `1`.  Thus `H=K_{1,5}` and `L(H)=K_5`.

If `H` is unicyclic and has a leaf, the same argument produces an isolated `K_{1,5}` component, contradicting unicyclic connectedness.  Hence a connected unicyclic `H` has no leaf, so `H` is a cycle; its line graph is 2-regular, not 4-regular.

It remains to consider a representation graph having exactly two parallel edges between vertices `a,b`, with the simple reduction a tree.  Degrees below are multigraph degrees.  For either parallel edge, the other parallel edge is counted from both endpoints and must be counted only once in the line graph.  Therefore

\[
4=d_H(a)+d_H(b)-3,
\]

so

\[
d_H(a)+d_H(b)=7. \tag{8}
\]

For every ordinary edge `uv`, there is no such double counting and again

\[
d_H(u)+d_H(v)=6. \tag{9}
\]

The simple reduction of `H` is a finite tree, hence has a leaf `u`.  Since `a,b` each have multigraph degree at least `2`, this leaf is different from `a,b`; let `v` be its neighbour.  Equation (9) gives `d_H(v)=5`.  If `v` were different from `a,b`, then every other neighbour of `v` would have degree `1` by (9), making the entire connected graph a star and leaving no place for the doubled edge.  Hence `v` is one of `a,b`, say `v=a`.  Then (8) gives `d_H(b)=2`, so the two parallel `ab` edges exhaust the degree of `b`.  Vertex `a` has the two parallel edges plus three ordinary edges, and (9) forces the three other endpoints to be leaves.  Thus `H` consists of the doubled pair `ab` and three leaf edges at `a`.  All five edges are pairwise incident at `a`, and therefore

\[
L(H)=K_5.
\]

So the only integrally represented connected 4-regular case is `K_5`, which has order five.  Together with the exceptional-order bound, no connected 4-regular example of order at least nine can have smallest eigenvalue greater than `-2`. `square`

Applying Lemma 2.1 to `-C` gives a decisive finite reduction:

\[
q=N/\gcd(N,2)\le8 \tag{10}
\]

for every generic strict sub-six signing.

---

## 3. Exact small component analysis

Since a simple 4-regular graph has at least five vertices, (10) leaves `q=5,6,7,8`.

### 3.1 Order five

The unique 4-regular underlying graph is `K_5`.  If a signing has largest eigenvalue below `2`, every triangle must be negative: a positive signed triangle has largest eigenvalue `2` and interlaces.  If all triangles are negative, switching at a fixed vertex shows that the signing is switching-equivalent to the all-negative `K_5`, whose largest eigenvalue is `1`.

Thus the unique sub-2 switching class on `K_5` has index `1`.

### 3.2 Order six

The forced connected 4-regular circulant is `C_6(1,2)`.  A sub-2 signing again has all eight triangles negative.  Switch the path edges

`01,12,23,34,45`

to `+1`.  The eight triangle equations determine the remaining signs uniquely, and the characteristic polynomial is

\[
x^3(x-2)^2(x+4). \tag{11}
\]

Its largest eigenvalue is `2`.  Hence no signing of this component has largest eigenvalue strictly below `2`.

### 3.3 Order seven

The two connected 4-regular circulants are isomorphic:

\[
C_7(1,2)\cong C_7(1,3)\cong\overline{C_7}.
\]

A sub-2 signing has all seven triangles negative.  In the path gauge

`01,12,23,34,45,56>0`,

the triangle equations have exactly two labelled switching solutions.  Their characteristic polynomials are

\[
(x+4)(x^3-2x^2-x+1)^2 \tag{12}
\]

and

\[
x(x^3-7x+7)^2. \tag{13}
\]

The first class has largest eigenvalue `2.2469796...>2`; the second has largest eigenvalue exactly `beta`.  Therefore:

\[
\boxed{\min_{\eta}\lambda_{\max}(A_{\overline C_7,\eta})=\beta,} \tag{14}
\]

and the minimizer below `2` is one labelled switching class.

### 3.4 Order eight

There are two relevant connected 4-regular circulants.

For `C_8(1,2)`, all-negative-triangle path-gauge solutions give exactly two classes, with characteristic polynomials

\[
(x^4-8x^2+8x-2)^2 \tag{15}
\]

and

\[
x(x-2)^2(x+4)(x^2-2)^2. \tag{16}
\]

Their largest eigenvalues are respectively `2.17958...` and `2`.

For `C_8(1,3)=K_{4,4}`, every signing has block form

\[
\begin{pmatrix}0&W\\W^T&0\end{pmatrix},
\]

where `W` is a `4x4` matrix with entries `+-1`.  Since `||W||_F^2=16`, its largest singular value is at least `2`.  Thus neither order-eight component permits strict sub-2 index.

Consequently, only component orders `5` and `7` can occur in a generic strict sub-six signing.

---

## 4. Lifting the order-five component

Here `q=5`, so `N=5` or `N=10`.  The already proved first-gap classification gives exactly

\[
(N,s)=(5,2),(10,3),
\]

with

\[
m(N,s)^2=5. \tag{17}
\]

For completeness, `(10,2)` cannot lift the all-negative `K_5` defect: vanishing of the even two-walk channels forces alternating triangle flux, while a defect triangle then has positive sign, contradicting the negative-triangle condition in the `K_5` defect class.  The pair `(10,4)` is on the flat line and was separated before the generic reduction.

---

## 5. Lifting the order-seven component

### 5.1 Odd order `N=7` is impossible

The admissible steps are `s=2,3`.  In each case one of the mixed two-walk displacements `s-1,s+1` lies outside the parity support.  Under `M<2`, every off-support entry of `B` is zero.  Writing `h_i` for the signed step-one edge and `tau_i` for the signed step-`s` edge, the vanishing mixed channel has the form

\[
h_i\tau_{i+1}+\tau_i h_{i+s}=0 \tag{18}
\]

(up to the harmless index reversal for the other mixed displacement).  Multiplying (18) over all `i\in\mathbb Z_7` cancels every edge sign twice and gives

\[
1=(-1)^7,
\]

an impossibility.  Hence no `N=7` signing is strictly sub-six.

### 5.2 Order `N=14`

The generic steps are `s=2,3,4,5`; `s=6` is flat.  Normalize the step-one Hamilton path and let `T` be the signed cyclic shift with

\[
T^{14}=\alpha I,\qquad \alpha\in\{\pm1\}.
\]

Write the step-`s` signing as

\[
Q=DT^s+T^{-s}D,
\]

with `D` diagonal and `D^2=I`.  As above, a mixed channel lies outside the forced parity support.  Its vanishing is exactly

\[
DT=-TD. \tag{19}
\]

Thus

\[
D=\varepsilon\,\operatorname{diag}(1,-1,1,-1,\ldots),
\qquad \varepsilon\in\{\pm1\}. \tag{20}
\]

With `A=T+T^{-1}+Q`, (19) gives cancellation of all mixed terms and

\[
B=T^2+T^{-2}+(-1)^s(T^{2s}+T^{-2s}). \tag{21}
\]

This is a finite identity.  On an eigenvector of `T` with `T`-eigenvalue `z`, where

\[
z^{14}=\alpha,
\]

the defect eigenvalue is

\[
\mu(z)=z^2+z^{-2}+(-1)^s(z^{2s}+z^{-2s}). \tag{22}
\]

Exact characteristic-polynomial factorization gives

\[
\begin{array}{c|c|c}
s&\alpha&\chi_B(x)\\ \hline
2&-1&x^2(x^3-7x-7)^4\\
2&+1&(x-4)^2(x^3+2x^2-x-1)^4\\
3&-1&x^2(x^3-7x+7)^4\\
3&+1&x^2(x^3-7x-7)^4\\
4&-1&x^2(x^3-7x+7)^4\\
4&+1&(x-4)^2(x^3+2x^2-x-1)^4\\
5&-1&x^2(x^3-7x-7)^4\\
5&+1&x^2(x^3-7x+7)^4.
\end{array} \tag{23}
\]

The only rows in (23) with largest defect eigenvalue below `2` are

\[
(s,\alpha)=(3,-1),(4,-1),(5,+1),
\]

and in each case that eigenvalue is `beta`.  Hence

\[
\boxed{m(14,s)^2=4+\beta\quad(s=3,4,5),} \tag{24}
\]

while

\[
m(14,2)^2\ge6. \tag{25}
\]

Together with Sections 1--4, this proves Theorem A. `square`

---

## Theorem B: rigidity of the order-14 exception

For each `s\in\{3,4,5\}`, the minimizers of `C_{14}(1,s)` form exactly two labelled switching classes.  In Hamilton gauge they are the two signs `\varepsilon=\pm1` in (20), with uniquely forced holonomy

\[
\alpha=-1\quad(s=3,4),\qquad
\alpha=+1\quad(s=5). \tag{26}
\]

A one-step rotation exchanges the two labelled classes.

### Proof

Any minimizer has squared radius `4+beta<6`, so the strict-support reduction applies.  By (14), both parity components of its defect must lie in the unique sub-2 switching class of `\overline C_7`.  The off-support mixed channel then vanishes and forces (19), hence (20).  The exact finite spectrum (23) fixes `alpha` uniquely.  Thus only `epsilon=+-1` remains.  A one-step rotation changes the sign of the alternating diagonal and exchanges those two Hamilton-gauge representatives. `square`

A full enumeration of all `2^15` Hamilton-gauge representatives was also run as an independent hostile audit: it returns exactly two minimizers for each of `s=3,4,5`.  This enumeration is not used in the proof.

---

## Corollary 1: a universal odd-order floor

For every odd `N\ge7` and every admissible `s`,

\[
\boxed{m(N,s)\ge\sqrt6.} \tag{27}
\]

Indeed, every strict sub-six family in Theorem A has even order except `(5,2)`.

This is considerably stronger than a resonance-only statement: it applies to every two-step circulant of odd order.

## Corollary 2: all odd resonance ratios

If `k\ge3` and `s\ge3` are both odd, then

\[
\boxed{m(ks,s)\ge\sqrt6.} \tag{28}
\]

Thus the general resonance problem has a uniform finite-global obstruction at the `sqrt(6)` scale throughout the entire odd--odd region.  The line `k=3` is special not because it is the first place where a lower obstruction exists, but because its signed triangles amplify that universal odd-order floor past the larger threshold `sqrt(8)` for odd `s\ge7`.

---

## Reproducibility boundary

The small component statements (11)--(16) and the order-14 factorization (23) are checked by `verify_sub_sqrt6_exact.py` using exact symbolic characteristic polynomials.  Floating eigenvalues are printed only for readability and are not accepted as certificates.

The external Greaves classification is used only in Lemma 2.1 to reduce arbitrarily large 4-regular defect components to orders at most eight.  Everything after that reduction is explicit finite algebra in this paper.