# General two-generator circulants as square-lattice quotients

Date: 2026-09-07.

This note removes the assumption that one generator is a unit.  It is a
structural reduction preparing the next finite-arithmetic classification.

Let

\[
G_N(a,b)=\operatorname{Cay}(\mathbb Z_N,\{\pm a,\pm b\})
\]

be connected and simple four-regular, so in particular

\[
\gcd(N,a,b)=1.
\]

## Theorem LQ

Define

\[
\Phi:\mathbb Z^2\to\mathbb Z_N,
\qquad
\Phi(x,y)=ax+by\pmod N.
\]

Connectivity makes `Phi` surjective.  Its kernel

\[
L=\{(x,y)\in\mathbb Z^2:ax+by\equiv0\pmod N\}
\]

is a rank-two sublattice of index `N`.  The induced map gives an abelian-group
isomorphism

\[
\mathbb Z^2/L\cong\mathbb Z_N
\]

under which the coordinate steps `±e_1,±e_2` map to `±a,±b`.  Hence

\[
\boxed{
G_N(a,b)\cong
\operatorname{Cay}(\mathbb Z^2/L,\{\pm e_1,\pm e_2\}).}
\tag{LQ1}
\]

So every connected four-regular two-generator circulant is a finite
square-lattice torus with a possibly skew/helical fundamental lattice.

## Bipartiteness criterion

The graph is bipartite exactly when there exists a homomorphism
`chi:Z_N -> Z_2` taking both `a` and `b` to `1`.  Since the only nontrivial
homomorphism exists when `N` is even and is reduction mod `2`,

\[
\boxed{
G_N(a,b)\text{ is bipartite}
\iff N\text{ is even and }a,b\text{ are odd}.}
\tag{LQ2}
\]

This identifies precisely when a global parity involution is available.

## Generator-cycle arithmetic

The `a`-edges alone form `gcd(N,a)` disjoint cycles of length

\[
L_a=N/\gcd(N,a),
\]

and similarly the `b`-edges form `gcd(N,b)` cycles of length

\[
L_b=N/\gcd(N,b).
\]

Thus the previously discovered `N=3s` obstruction for `C_N(1,s)` is the
special case in which the second generator has cycle length `3`.  For general
`G_N(a,b)`, the natural resonance parameters are the pair `(L_a,L_b)` plus
the skew class of the lattice `L`.

## Next theorem targets

1. classify the threshold `m(G)<sqrt(8)` by short generator-cycle lengths
   `L_a,L_b`, starting with `3,5,7`;
2. derive width-`L_a` or width-`L_b` signed block-Jacobi representations;
3. generalize the nine-column forbidden-state argument from signed triangles
   (`L=3`) to signed pentagons and heptagons;
4. identify when a `pi`-flux/Clifford signing descends through a skew lattice
   without defects.

This quotient model is exact and applies also when neither generator is a
unit, e.g. cases not isomorphic to any `C_N(1,s)` by a cyclic automorphism.
