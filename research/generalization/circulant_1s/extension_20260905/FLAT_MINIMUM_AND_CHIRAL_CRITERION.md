# Exact flat minima and the parity-correct chiral criterion

These analytic results resolve C1, C2 and C4 from the preregistered local
conjecture note. They are separate from the frozen paper. Here
`2<=s<N/2`, and `m(N,s)` minimizes the signed adjacency spectral radius
over all edge signings of the simple four-regular graph `C_N(1,s)`.

## 1. Exact absolute minimum

**Theorem.**

\[
 m(N,s)=2\quad\Longleftrightarrow\quad N=2s+2.
\]

If `N!=2s+2`, every signing satisfies `rho(A)>=sqrt(5)`.

**Proof.** Since `tr(A^2)=4N`, `rho(A)>=2`, with equality if and only
if `A^2=4I`. Count the common neighbors of vertices `0` and `2` in the
underlying graph. The two-step displacement `+2` always has its pure
`+1,+1` path. Under `2<=s<N/2`, the only further channels that can end at
residue `2` are:

| condition | additional length-two paths |
|---|---|
| `s=3` | the two mixed paths of displacement `s-1` |
| `(N,s)=(5,2)` | the two mixed paths of displacement `-(s+1)` |
| `N=2s+2` | the pure displacement `-2s` path |

These conditions are exhaustive: check the list of displacements
`+/-2,+/-2s,+/-(s-1),+/-(s+1)` under the displayed range of `s`.
Outside `N=2s+2`, the common-neighbor count is therefore `1` or `3`.
For every signing, `(A^2)_(0,2)` is an odd nonzero integer. The
corresponding two-by-two principal submatrix of `A^2` is

\[
 \begin{pmatrix}4&b\\b&4\end{pmatrix},\qquad |b|\ge1.
\]

Its largest eigenvalue is at least `5`. By the Rayleigh principle,
`rho(A)^2>=5`, proving necessity and the quantitative gap.

For sufficiency use the Hamilton-gauge word `tau_i=(-1)^i` and the
holonomy `alpha=(-1)^(s+1)`. If `T` is the one-step quasiperiodic shift,
the mixed terms cancel and

\[
 A^2=4I+T^2+T^{-2}+(-1)^s(T^{2s}+T^{-2s}),\qquad T^N=\alpha I.
\]

When `N=2s+2`, `T^(2s)=alpha T^(-2)`. Thus

\[
 A^2=4I+\big(1+(-1)^s\alpha\big)(T^2+T^{-2})=4I.
\]

This construction was already present in local Task 60; the new argument
completes its necessity for this fixed-underlying-graph family.

## 2. All equality signings

**Proposition.** Suppose `N=2s+2` and `s!=3`. All equality signings have
Hamilton coordinates

\[
 \tau_i=\epsilon(-1)^i,\qquad\alpha=(-1)^{s+1},\qquad\epsilon\in\{\pm1\}.
\]

They form two switching classes on the labelled graph, identified by
translation when graph automorphisms are allowed.

**Proof.** In the squared-operator formula, the channel of displacement
`s-1` has coefficient `tau_(i-1)+tau_i`. At `N=2s+2` it has no collisions
with the other channels unless `s=3`. Hence `A^2=4I` forces this coefficient
to vanish for every `i`. It follows that `tau` alternates. The preceding
square formula then forces `alpha=(-1)^(s+1)`, since `T^2+T^(-2)` is not
the zero matrix for `N>=6`.

The Hamilton-cycle sign and the sign of each chord together with the
Hamilton path joining its endpoints are switching invariants. After fixing
the Hamilton gauge they give `(tau,alpha)` uniquely; the two lifts are
therefore two distinct switching classes. Translation by one vertex
interchanges the two alternating words and preserves the Hamilton holonomy.

For the exceptional pair `(N,s)=(8,3)`, the underlying graph is `K_(4,4)`.
Its signed adjacency matrix, ordered by the bipartition, has the form

\[
 A=\begin{pmatrix}0&B\\B^T&0\end{pmatrix},\qquad B\in\{\pm1\}^{4\times4}.
\]

Equality holds exactly when `BB^T=4I`, i.e. when `B` is an order-four
Hadamard matrix. Switching at the vertices acts by row and column signs;
bipartition-preserving automorphisms act by row and column permutations.

For completeness the equivalence here needs no general Hadamard
classification. Normalize the first row and column to be positive. Each
remaining row has exactly two negative entries among its last three
positions, and their respective positive positions must be distinct by
orthogonality. Row and column permutations therefore give the unique
normalized pattern. This proves uniqueness under switching and graph
isomorphism, but does not claim uniqueness under the smaller dihedral group.

## 3. General half-cell chirality

Let `tau` have period `p=2m` in the step-`(1,s)` operator, and let
`D x_i=(-1)^i x_i`, `T_m x_i=x_(i+m)`. Within the specified monomial
class `D T_m`, the following are equivalent:

1. the anticommutation identity holds on every Bloch fiber;
2. `tau_(i+m)=(-1)^(s+1) tau_i` for every integer `i`;
3. `Q_i=tau_i tau_(i+1)` is `m`-periodic and
   `product_(j=0)^(m-1)Q_j=(-1)^(s+1)`.

Whenever they hold, on the `z`-fiber choose a unit scalar with

\[
 \gamma(z)^2=(-1)^m z^{-1},\qquad J_z=\gamma(z)DT_m.
\]

Then `J_z` is a self-adjoint unitary involution anticommuting with the
Hermitian fiber. Its two eigenspaces have equal dimension `m`, and the
squared spectral problem reduces from `2m` to `m` dimensions.

**Proof.** Conjugation by `D` multiplies displacement-one coefficients by
`-1` and displacement-`s` coefficients by `(-1)^s`. Translation replaces
each chord coefficient by `tau_(i+m)`. Comparing the distinct integer
displacements on the infinite cover gives the equivalence of 1 and 2.
The all-phase identity is equivalent to this Laurent-operator identity;
an accidental identity at one short fiber would not establish necessity.

If 2 holds, multiplication and telescoping give 3. Conversely, the ratios
`tau_(i+m)/tau_i` are constant by half-periodicity of `Q`, and their value
is the indicated half-cell product. This proves 2.

Finally `(DT_m)^2=(-1)^m zI`, which proves the normalization. A unitary
involution is self-adjoint. Half-cell translation has no fixed coordinate,
so the monomial matrix `J_z` has trace zero, giving equal eigenspace
dimensions and the usual off-diagonal block decomposition.

For even `s`, the half-cell flux is negative, recovering the period-eight
mechanism. For odd `s`, it is positive. Moreover, at odd `s` the even-period
fiber is already bipartite and anticommutes with `D` alone for every `tau`.
This last statement does not enlarge the specified `DT_m` iff criterion.

## 4. Literature boundary

McKee and Smyth's *Integer symmetric matrices having all their eigenvalues
in the interval [-2,2]* already gives a general classification covering
signed graphs at spectral radius at most two:
[author-posted primary source](https://arxiv.org/abs/0705.3599).

Accordingly the flat theorem above is a direct classification inside the
specific circulant family, not a claim to originate the general spectral
radius-two theory. Its exact relation to the toral tessellation family and
existing weighing-matrix literature remains a priority audit item. The
all-even sub-eight theorem in the companion note is a different result.
