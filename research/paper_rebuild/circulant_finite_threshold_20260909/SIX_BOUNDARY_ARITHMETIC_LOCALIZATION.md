# Arithmetic localization at the `sqrt(6)` boundary

This note belongs entirely to the finite-global signed-circulant paper.  It strengthens the root-quotient reduction by showing that a signing with squared spectral radius at most `6` can occur only on four elementary arithmetic resonance loci in the reduced parity circulant.

Throughout

\[
2\le s<N/2,\qquad A=A_\sigma,\qquad B=A^2-4I,
\]

and put

\[
d:=\gcd(N,2),\qquad q:=N/d,
\qquad t:=\min\{s,q-s\}.
\]

We exclude in the main statement the already separated degeneracies

\[
N=2s+2\qquad\text{and}\qquad N=4s.
\]

For every other pair, the parity-defect graph

\[
P:=\operatorname{supp}(B\bmod 2)
\]

has `d` connected components, each isomorphic to

\[
C_q(1,t).
\]

In particular `2<=t<q/2`.

## Theorem 1 (four-locus localization)

Assume `N!=2s+2` and `N!=4s`.  If there is a signing of `C_N(1,s)` such that

\[
\rho(A)^2\le 6,
\]

then

\[
\boxed{
 t=2,
 \qquad q=2t+1,
 \qquad q=2t+2,
 \qquad\text{or}\qquad q=3t.
}
\tag{1}
\]

Equivalently, away from these four reduced arithmetic loci every signing satisfies the **strict** inequality

\[
\boxed{\rho(A)^2>6.}
\tag{2}
\]

Consequently, after the complete strict sub-`sqrt(6)` classification is inserted, every as-yet-unclassified equality pair `m(N,s)^2=6` is confined to (1).

The new ingredient is that repeated roots at the non-strict boundary can occur only when the parity-defect graph has twins, and a connected 4-regular step circulant has twins only on its own flat line.

---

## 1. A size-two defect entry forces twins modulo two

Set

\[
K:=6I-A^2=2I-B.
\]

If `rho(A)^2<=6`, then `K` is positive semidefinite.  Hence there are Euclidean roots `r_i` with

\[
K_{ij}=\langle r_i,r_j\rangle,
\qquad \|r_i\|^2=2.
\]

Since `K` is integral, Cauchy--Schwarz gives

\[
K_{ij}\in\{-2,-1,0,1,2\}.
\]

### Lemma 2

If `|B_ij|=2` for distinct `i,j`, then `i,j` are nonadjacent twins in the parity graph `P=supp(B mod 2)`.

### Proof

The condition `|B_ij|=2` is equivalent to `|K_ij|=2`.  Equality in Cauchy--Schwarz gives

\[
r_j=\varepsilon r_i,
\qquad \varepsilon\in\{\pm1\}.
\]

Therefore for every `k`

\[
K_{jk}=\varepsilon K_{ik}.
\]

Reducing modulo two removes the sign `epsilon`.  Since off the diagonal `K=-B`, the `i`-th and `j`-th rows of `B mod 2` coincide.  Moreover `B_ij` is even, so `i` and `j` are not adjacent in `P`.  Thus they are nonadjacent twins.  `square`

---

## 2. Twins in a 4-regular step circulant

### Lemma 3 (twin classification)

Let

\[
2\le t<q/2
\]

and let

\[
G=C_q(1,t)=\operatorname{Cay}(\mathbb Z_q,\{\pm1,\pm t\}).
\]

Then `G` has two distinct vertices with the same open neighbourhood if and only if

\[
\boxed{q=2t+2.}
\tag{3}
\]

### Proof

By translation it is enough to ask when the connection set

\[
S=\{\pm1,\pm t\}
\]

has a nonzero translational period `a`, i.e.

\[
S+a=S.
\tag{4}
\]

Let `H` be the subgroup of translations stabilizing `S`.  Its action on `S` is free, so `|H|` divides `|S|=4`.  If `H` is nontrivial, `|H|` is `2` or `4`.

If `|H|=2`, then `q` is even and

\[
H=\{0,q/2\}.
\]

The four-element set `S` is therefore the union of the two `H`-orbits through `1` and `-1`:

\[
S=\{1,1+q/2,-1,-1+q/2\}.
\]

Because `2<=t<q/2`, this forces

\[
t=q/2-1,
\]

which is exactly `q=2t+2`.

If `|H|=4`, then `S` is one coset of the unique order-four translation subgroup.  Since both `1` and `-1` lie in that coset, their difference `2` lies in the order-four subgroup.  For `q>=5` this forces `q=8`; then necessarily `t=3`, again giving `q=2t+2`.

Conversely, if `q=2t+2`, translation by `q/2=t+1` sends

\[
1\leftrightarrow -t,
\qquad -1\leftrightarrow t,
\]

so `S+q/2=S`, and opposite vertices are twins.  `square`

### Corollary 3.1

If `q!=2t+2` and `rho(A)^2<=6`, then `B` has no off-diagonal entry of absolute value `2`.

Indeed every component of `P` is a copy of `C_q(1,t)`, and vertices in different components cannot be twins because their nonempty neighbourhoods lie in disjoint components.

Since the parity-support entries of `B` are odd and all other entries are even, the bound `|B_ij|<=2` now gives

\[
B_{ij}=\pm1\quad\text{on }P,
\qquad
B_{ij}=0\quad\text{off }P.
\tag{5}
\]

Thus `B` is a genuine signed adjacency matrix of `P` whenever `q!=2t+2`.

---

## 3. Triangle-free equality collapses to the flat theorem

Assume now that `q!=2t+2` and that the reduced parity component `C_q(1,t)` is triangle-free.  By (5), each connected component `C` of `B` is a signed adjacency matrix of this 4-regular graph.  Hence

\[
\operatorname{tr}C=0,
\qquad
\operatorname{tr}C^2=4q,
\qquad
\operatorname{tr}C^3=0.
\tag{6}
\]

All eigenvalues `lambda` of `C` satisfy `lambda<=2`, because

\[
\lambda_{\max}(B)=\rho(A)^2-4\le2.
\]

For every such eigenvalue,

\[
(2-\lambda)(2+\lambda)^2\ge0.
\]

Summing over the spectrum and using (6) gives

\[
\sum_\lambda(2-\lambda)(2+\lambda)^2
=8q+4\operatorname{tr}C-2\operatorname{tr}C^2-\operatorname{tr}C^3
=0.
\tag{7}
\]

Every summand in (7) is nonnegative, so every eigenvalue of `C` is `2` or `-2`.  Therefore

\[
C^2=4I.
\tag{8}
\]

But the exact flat-minimum theorem for signed step circulants says that a signing of `C_q(1,t)` can satisfy (8) only when

\[
q=2t+2.
\]

This contradicts the present assumption `q!=2t+2`.  We conclude:

> if `rho(A)^2<=6`, then either the parity component has twins (`q=2t+2`) or it contains a triangle.

Finally, the elementary three-increment classification for `C_q(1,t)` gives

\[
C_q(1,t)\text{ contains a triangle}
\iff
 t=2\text{ or }q=2t+1\text{ or }q=3t.
\tag{9}
\]

Combining (3) and (9) proves Theorem 1.  `square`

---

## 4. Translation back to the original parameters

The reduced form `(q,t)` is the cleanest statement.  Two useful consequences are immediate.

### Odd order

If `N` is odd, then `q=N` and `t=s`.  Hence any signing with `rho(A)^2<=6` must satisfy

\[
\boxed{s=2\quad\text{or}\quad N=2s+1\quad\text{or}\quad N=3s.}
\tag{10}
\]

(The twin relation `N=2s+2` is even and cannot occur.)

Thus every odd pair outside the three loci in (10) satisfies the strengthened strict bound

\[
\boxed{m(N,s)>\sqrt6.}
\tag{11}
\]

### Even order

If `N` is even, then `q=N/2` and `t=min(s,N/2-s)`.  Equality or sub-equality at six is therefore confined to

\[
t=2,
\qquad N/2=2t+1,
\qquad N/2=2t+2,
\qquad N/2=3t.
\tag{12}
\]

The twin line `N/2=2t+2` translates exactly to

\[
\boxed{N=4s+4\quad\text{or}\quad N=4s-4.}
\tag{13}
\]

This explains structurally why the known equality examples `(12,4)`, `(16,3)`, and `(16,5)` all lie on the two neighbouring resonances `N=4s+-4`, while `(20,8)` belongs to the separate triangular locus `t=2`.

---

## 5. Status

- Theorem 1 and Lemmas 2--3 are **Proved** analytically.
- No computation is used in their proofs.
- The result does **not** claim a complete `m^2=6` classification; it reduces that classification to four explicit arithmetic loci.
- Together with the strict sub-six theorem, it gives a new strict lower bound `m(N,s)>sqrt(6)` on every parameter pair outside those loci and the already separated sub-six families.
