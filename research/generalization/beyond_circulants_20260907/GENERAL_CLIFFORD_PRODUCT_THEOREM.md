# Clifford Cartesian-product signing theorem

Date: 2026-09-07.
Branch: `research/quadratic-gap-upgrade`.

This note extends the project beyond cyclic circulants to Cartesian products
of arbitrary bipartite graphs.  The construction is explicit and purely
algebraic.

## 1. Setup

For `j=1,...,d`, let `G_j` be a finite bipartite graph, let `A_j` be the
adjacency matrix of an arbitrary signing of `G_j`, and let `D_j` be the
diagonal bipartition involution (`+1` on one side, `-1` on the other).
Then

\[
D_j^2=I,\qquad D_jA_j=-A_jD_j.
\tag{1}
\]

On the Cartesian product

\[
G=G_1\square\cdots\square G_d
\]

define the `j`-th signed directional adjacency operator

\[
\Gamma_j=D_1\otimes\cdots\otimes D_{j-1}\otimes A_j\otimes I\otimes\cdots\otimes I.
\tag{2}
\]

Each `Gamma_j` is supported exactly on the edges in the `j`-th Cartesian
direction, with entries in `{+1,-1}`.  Hence

\[
A:=\Gamma_1+\cdots+\Gamma_d
\]

is the signed adjacency matrix of a signing of `G`.

## 2. Main theorem

**Theorem CP.** The directional operators anticommute pairwise:

\[
\Gamma_i\Gamma_j=-\Gamma_j\Gamma_i\qquad(i\ne j).
\tag{3}
\]

Consequently

\[
\boxed{
A^2=\sum_{j=1}^d
 I\otimes\cdots\otimes A_j^2\otimes\cdots\otimes I.}
\tag{4}
\]

All summands on the right commute.  Therefore

\[
\boxed{
\operatorname{Spec}(A^2)=
\left\{\lambda_1^2+\cdots+\lambda_d^2:
\lambda_j\in\operatorname{Spec}(A_j)\right\}}
\tag{5}
\]

with multiplicities, and in particular

\[
\boxed{\rho(A)^2=\rho(A_1)^2+\cdots+\rho(A_d)^2.}
\tag{6}
\]

### Proof

For `i<j`, all tensor factors commute except in coordinate `i`, where the
first product contains `A_iD_i` and the reversed product contains `D_iA_i`.
Equation (1) contributes exactly one minus sign, proving (3).  Squaring the
sum therefore cancels all mixed anticommutators and gives (4).  Since the
terms in (4) act on separate tensor coordinates, a tensor product of
`A_j^2`-eigenvectors is an eigenvector with eigenvalue the sum of the
coordinate eigenvalues, proving (5)--(6).

## 3. Minimum-radius consequence

Write `m(G)` for the minimum signed adjacency spectral radius over all
signings of a fixed graph `G`.  Choosing independently radius-minimizing
signings of the factors gives

\[
\boxed{
m(G_1\square\cdots\square G_d)^2
\le\sum_{j=1}^d m(G_j)^2.}
\tag{7}
\]

This is a constructive upper bound, not a general equality claim.

## 4. Flat-signing closure theorem

Suppose in addition that every `G_j` is `k_j`-regular and admits a flat
signing

\[
A_j^2=k_jI.
\tag{8}
\]

Then (4) gives

\[
A^2=(k_1+\cdots+k_d)I.
\]

The Cartesian product is `K=sum k_j` regular.  For every signing `B` of a
`K`-regular graph,

\[
\operatorname{tr}(B^2)=K|V|,
\]

so `rho(B)^2>=K`.  Hence the Clifford signing is globally optimal:

\[
\boxed{
m(G_1\square\cdots\square G_d)=\sqrt{k_1+\cdots+k_d}.}
\tag{9}
\]

Thus the class of bipartite regular graphs with a two-eigenvalue flat signing
is closed under Cartesian product at the level of exact minimum signed
spectral radius.

## 5. Scope and literature boundary

The tensor/anticommutation mechanism is closely related to signed Cartesian
products, Huang-type hypercube signings, Clifford constructions, and the
literature on signed graphs with two symmetric eigenvalues.  It should be
presented as a unifying theorem/application framework, not as a claim that
Cartesian products or two-eigenvalue signings are themselves new.
