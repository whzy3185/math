# Complete sub-`sqrt(6)` classification

This note is self-contained modulo one explicitly cited published classification theorem of Greaves--Koolen--Munemasa--Sano--Taniguchi (JCTB 110 (2015), 90--111). It belongs entirely to the finite-global paper and uses no continuous Bloch/Floquet result.

Throughout, `2 <= s < N/2`, `A=A_sigma` is an arbitrary signed adjacency matrix of `C_N(1,s)`, and

\[
B:=A^2-4I,\qquad M:=\lambda_{\max}(B).
\]

Since `A^2` is positive semidefinite,

\[
\rho(A)^2=4+M.
\]

Let `beta` denote the largest real root of

\[
x^3-7x+7=0.
\]

Numerically,

\[
\beta=1.692021471630095\ldots .
\]

## Main theorem

For every admissible pair `(N,s)`,

\[
\boxed{m(N,s)^2<6}
\]

if and only if one of the following mutually disjoint alternatives holds:

1. `N=2s+2`, in which case
   \[
   m(N,s)^2=4;
   \]
2. `(N,s)=(5,2)` or `(10,3)`, in which case
   \[
   m(N,s)^2=5;
   \]
3. `N=4s`, in which case
   \[
   m(4s,s)^2=4+2\cos\frac{\pi}{2s};
   \]
4. `N=14` and `s in {3,4,5}`, in which case
   \[
   m(14,s)^2=4+\beta.
   \]

Equivalently, outside these four families,

\[
\boxed{m(N,s)^2\ge 6.}
\]

The first three alternatives were already proved in the rebuild. The new content is the global exclusion below `6` and the exact `N=14` exceptional family.

---

## 1. Reduction below `6` to a signed parity-defect graph

The parity-defect trichotomy gives

\[
\operatorname{supp}(B\bmod2)=
\begin{cases}
\varnothing, & N=2s+2,\\
\operatorname{Cay}(\mathbb Z_N,\{\pm2\}), & N=4s,\\
\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}), & \text{otherwise}.
\end{cases}
\]

Assume from now on that neither `N=2s+2` nor `N=4s`, and suppose

\[
\rho(A)^2<6.
\]

Then `M<2`. For every off-diagonal entry `b_ij`, the principal `2x2` submatrix

\[
\begin{pmatrix}0&b_{ij}\\b_{ij}&0\end{pmatrix}
\]

has largest eigenvalue `|b_ij|`, so interlacing gives `|b_ij|<2`. Since `B` is integral,

\[
b_{ij}\in\{0,\pm1\}.
\]

On the parity support the entries are odd, hence `+-1`; off the parity support the entries are even, hence `0`. Therefore under the strict sub-`6` hypothesis, `B` is exactly a signed adjacency matrix of

\[
P_{N,s}:=\operatorname{Cay}(\mathbb Z_N,\{\pm2,\pm2s\}). \tag{1}
\]

Let

\[
d:=\gcd(N,2),\qquad n:=N/d.
\]

The graph `P_{N,s}` has exactly `d` connected components, each of order `n`; after dividing coordinates by `2` inside a component, each component is a connected 4-regular circulant. Thus every component `C` of `B` satisfies

\[
\lambda_{\max}(C)<2,
\]

or equivalently the signed graph `-C` has smallest eigenvalue greater than `-2`.

---

## 2. Large 4-regular components cannot occur

We use the classification of connected edge-signed graphs with smallest eigenvalue greater than `-2` due to Greaves, Koolen, Munemasa, Sano and Taniguchi, *J. Combin. Theory Ser. B* 110 (2015), 90--111. Their Theorems 6 and 19 imply:

- every exceptional such signed graph has at most eight vertices;
- every non-exceptional one is of one of three signed-line-graph types coming from a tree or a unicyclic representation graph (with one doubled-edge variant).

We need only the following elementary corollary.

### Lemma 2.1

Let `Gamma` be a connected 4-regular edge-signed graph with smallest eigenvalue greater than `-2`. If `|V(Gamma)|>=9`, then no such `Gamma` exists.

More precisely, among the integrally represented cases of the Greaves--Koolen--Munemasa--Sano--Taniguchi classification, the only connected 4-regular underlying graph that occurs is `K_5`.

### Proof

Exceptional graphs have at most eight vertices, so assume an integral representation.

For the line-graph cases, if `Gamma` has underlying graph `L(H)`, every edge `uv` of `H` must satisfy

\[
d_H(u)+d_H(v)-2=4,
\]

hence `d_H(u)+d_H(v)=6`. If `H` is a tree, choose a leaf `u`. Its neighbour has degree `5`; every other neighbour of that degree-5 vertex must then have degree `1`. Hence `H=K_{1,5}` and `L(H)=K_5`.

If `H` is unicyclic, any leaf would give the same degree-5-star argument and contradict unicyclicity. Hence `H` has no leaves, so it is a cycle, whose line graph is 2-regular, not 4-regular.

It remains to rule out the doubled-edge tree case. In the standard description, take the underlying simple tree `T` and the distinguished edge `ab` corresponding to the two orthogonal doubled-edge roots. The two corresponding vertices of the signed graph are nonadjacent twins. 4-regularity forces

\[
d_T(a)+d_T(b)=6.
\]

For an edge `av` or `bv` adjacent to the distinguished edge, the extra twin neighbour gives

\[
d_T(a)+d_T(v)=5\quad\text{or}\quad d_T(b)+d_T(v)=5,
\]

while every edge `xy` away from `a,b` must satisfy

\[
d_T(x)+d_T(y)=6.
\]

A finite tree has a leaf. If a leaf lies away from `a,b`, its neighbour has degree `5`, and all its other neighbours are forced to be leaves, disconnecting the distinguished edge. Thus every leaf is adjacent to `a` or `b`. If, say, `a` has a leaf, then `d_T(a)=4` and hence `d_T(b)=2`. The other neighbour of `b` has degree `3`; thereafter every edge away from `a,b` joins degree-3 vertices, producing further branches and eventually a leaf away from `a,b`, a contradiction. The case of a leaf at `b` is symmetric, while no leaves at either endpoint is impossible for a finite tree. Thus the doubled-edge case cannot be 4-regular.

So the only integral 4-regular case is `K_5`, of order five. In particular there is no connected 4-regular example of order at least nine. `square`

Consequently, if (1) has a component of order `n>=9`, then `M<2` is impossible. Therefore every generic sub-`6` pair must satisfy

\[
n=N/\gcd(N,2)\le8. \tag{2}
\]

---

## 3. The small 4-regular parity components

Only orders `5,6,7,8` can occur in (2). The necessary one-sided signed spectral facts can be proved by tiny switching calculations.

### Order 5: `K_5`

If a signing of `K_5` has largest eigenvalue below `2`, then every triangle must be negative: a positive signed triangle is switching-equivalent to the all-positive `K_3`, whose largest eigenvalue is `2`. Having every triangle negative forces the signing to be switching-equivalent to the all-negative `K_5`, whose largest eigenvalue is `1`.

Thus the unique sub-`2` switching class on the order-5 component has largest eigenvalue `1`.

### Order 6: `C_6(1,2)`

Again, largest eigenvalue below `2` forces every triangle to be negative. Switch the path edges

`01,12,23,34,45`

to `+1`. The eight triangle equations then determine the seven remaining edge signs uniquely. The resulting characteristic polynomial is

\[
x^3(x-2)^2(x+4).
\]

Hence its largest eigenvalue is exactly `2`, contradiction. Therefore every signing of this component has largest eigenvalue at least `2`.

### Order 7: `C_7(1,2) \cong C_7(1,3) \cong \overline{C_7}`

There are seven triangles. If the largest eigenvalue is below `2`, all seven must be negative. Switch the path edges

`01,12,23,34,45,56`

to `+1`. Solving the seven triangle equations leaves exactly two switching classes. Their characteristic polynomials are

\[
(x+4)(x^3-2x^2-x+1)^2
\]

and

\[
x(x^3-7x+7)^2.
\]

The first class has largest eigenvalue

\[
2.2469796037\ldots>2,
\]

whereas the second has largest eigenvalue exactly `beta`, the largest root of `x^3-7x+7`. Hence:

> A signing of `\overline{C_7}` has largest eigenvalue below `2` if and only if it belongs to one unique labelled switching class, and then its largest eigenvalue is `beta`.

This is the rigidity that creates the new `N=14` family.

### Order 8

For `C_8(1,2)`, the all-negative-triangle equations leave two switching classes; their characteristic polynomials are

\[
(x^4-8x^2+8x-2)^2
\]

and

\[
x(x-2)^2(x+4)(x^2-2)^2.
\]

Their largest eigenvalues are respectively `2.17958...` and `2`. Thus no signing has largest eigenvalue below `2`.

The other 4-regular circulant on eight vertices relevant here is

\[
C_8(1,3)=K_{4,4}.
\]

Any signing has block form

\[
\begin{pmatrix}0&W\\W^T&0\end{pmatrix}
\]

with `W` a `4x4` matrix of `+-1` entries. Its largest eigenvalue equals the largest singular value of `W`. Since

\[
\|W\|_F^2=16,
\]

the largest squared singular value is at least `16/4=4`; hence the largest eigenvalue is at least `2`.

Therefore orders `6` and `8` cannot support a strict sub-`2` defect component, while order `7` has exactly the single class described above.

---

## 4. Parameter reduction

The only generic component orders that can yield `M<2` are now `n=5` and `n=7`.

### `n=5`

This means `N=5` or `N=10`.

- `(5,2)` attains `m^2=5` by the conference-core signing.
- At `N=10`, the flat pair is `(10,4)`. Of the generic pairs `(10,2)` and `(10,3)`, the defect `K_5` class is liftable only for `(10,3)`, where the `K_{5,5}`-minus-matching block construction gives `m^2=5`.
- `(10,2)` is impossible at `M=1`: the alternating triangle-flux cancellation forced by the two-walk equations gives positive defect triangles, whereas an all-negative `K_5` defect has every triangle negative. This is the previously proved exact exclusion.

Thus `n=5` contributes exactly `(5,2)` and `(10,3)`.

### `n=7`: first exclude `N=7`

For `N=7`, the two admissible steps are `s=2,3`. In each case at least one mixed two-walk displacement `s+1` or `s-1` lies off the parity support. Under `M<2` that mixed channel must vanish. Writing `h_i` for the step-one edge signs and `tau_i` for the step-`s` edge signs gives a recurrence of the form

\[
h_i\tau_{i+1}+\tau_i h_{i+s}=0
\]

(or its shifted `s-1` version). Multiplying over all `i` yields

\[
1=(-1)^N,
\]

which is impossible for odd `N=7`. Hence no `N=7` pair has `m^2<6`.

### `n=7`: the order `N=14` lifts

The generic steps are `s=2,3,4,5`; `s=6` is flat. For each `s=2,3,4,5`, at least one mixed displacement is outside the parity support, so under `M<2` its vanishing forces the chord diagonal `D` to anticommute with the signed step-one shift `T`:

\[
DT=-TD,\qquad T^{14}=\alpha I,\qquad \alpha\in\{\pm1\}.
\]

Therefore every hypothetical sub-`6` lift must satisfy

\[
B=T^2+T^{-2}+(-1)^s(T^{2s}+T^{-2s}). \tag{3}
\]

This is a finite identity. Diagonalizing the finite signed shift, with `z^{14}=alpha`, gives

\[
\mu(z)=z^2+z^{-2}+(-1)^s(z^{2s}+z^{-2s}). \tag{4}
\]

A direct evaluation of the fourteen roots in (4) gives:

- `s=2`: for `alpha=-1`, `M=3.0489173395...`; for `alpha=+1`, `M=4`. Hence no sub-`6` signing.
- `s=3`: `alpha=-1` gives characteristic polynomial
  \[
  \chi_B(x)=x^2(x^3-7x+7)^4,
  \]
  hence `M=beta`; `alpha=+1` gives `M=3.0489173395...`.
- `s=4`: `alpha=-1` again gives `chi_B(x)=x^2(x^3-7x+7)^4`, hence `M=beta`; `alpha=+1` gives `M=4`.
- `s=5`: `alpha=+1` gives `chi_B(x)=x^2(x^3-7x+7)^4`, hence `M=beta`; `alpha=-1` gives `M=3.0489173395...`.

The anticommuting signings in the three good cases are genuine finite signings of `C_14(1,s)`, so the lower bound from the unique sub-`2` switching class on `\overline{C_7}` is attained. Thus

\[
\boxed{m(14,s)^2=4+\beta\qquad(s=3,4,5).}
\]

This completes the sub-`sqrt(6)` classification. `square`

---

## 5. Consequences for the paper narrative

The low-end theory is now naturally stated as a threshold hierarchy, not merely as isolated gaps:

- the exact trace floor `m=2` occurs precisely on `N=2s+2`;
- the exact first off-flat value is `sqrt(5)`, only at `(5,2)` and `(10,3)`;
- the exact `N=4s` resonance lies strictly between `sqrt(4+sqrt(2))` and `sqrt(6)`;
- the sporadic 7-vertex parity-defect root-system phenomenon gives the exact order-14 family `m^2=4+beta`;
- every remaining parameter pair lies at or above `sqrt(6)`.

The new order-14 family should be presented as a defect-component exception, not as an isolated computer discovery: it is forced by the unique sub-`2` switching class on the 4-regular graph `\overline{C_7}`.