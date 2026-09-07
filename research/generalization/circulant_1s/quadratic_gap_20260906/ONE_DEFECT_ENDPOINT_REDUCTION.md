# Exact endpoint reduction for the canonical one-defect resonance family

Date: 2026-09-07.

This note gives an exact dimension reduction for the canonical one-defect
signing on

\[
 C_{Ls}(1,s),
\]

with `L` and `s` odd.  It explains why the `L=3,5,7,9` threshold computations
can be reduced from matrices of order `Ls` to matrices of order only `4L`.
It is intended as the analytic entry point for the general odd-`L`
aspect-ratio conjecture.

Throughout write

\[
 s=2r+1,
 \qquad r\ge2,
\]

and use the Hamilton-gauge word

\[
 \tau_i=\varepsilon(-1)^i,
 \qquad \varepsilon\in\{\pm1\},
\]

with Hamilton holonomy `alpha=+/-1`.

## 1. Width-`L` column coordinates

Write each vertex uniquely as

\[
 i=j+a s,
 \qquad 0\le j<s,\quad 0\le a<L.
\]

Order vertices first by the column `j`, then by the layer `a`.
Let `B` be the signed adjacency matrix of the chord `L`-cycle in column
`j=0`.  Since `s` is odd, the chord block in column `j` is

\[
 B_j=(-1)^j B.
\tag{1}
\]

Changing `epsilon` globally negates `B`, so `B^2` is independent of
`epsilon`.

Let

\[
 S_\alpha=
 \begin{pmatrix}
 0&1&&&\\
 &0&1&&\\
 &&\ddots&\ddots&\\
 &&&0&1\\
 \alpha&&&&0
 \end{pmatrix}
\tag{2}
\]

be the signed cyclic shift in the layer coordinate and put

\[
 P=-S_\alpha^T.
\tag{3}
\]

Finally define the rank-two mixed seam block

\[
 M=-2\varepsilon
 \bigl(E_{00}+\alpha E_{1,L-1}\bigr).
\tag{4}
\]

## 2. Exact block form of the threshold matrix

Let

\[
 C=8I-A^2.
\]

The general squared-operator formula and the one-defect cancellation give the
following exact block description.

Every diagonal column block is

\[
 \boxed{G=6I_L-B^2.}
\tag{5}
\]

For ordinary columns, the only nonzero off-diagonal blocks are the
second-neighbor couplings

\[
 C_{j,j+2}=C_{j+2,j}=-I_L.
\tag{6}
\]

All ordinary adjacent-column mixed blocks vanish.  The only additional
seam blocks are

\[
\boxed{
 C_{0,s-2}=P,
 \qquad
 C_{1,s-1}=P,
 \qquad
 C_{0,s-1}=M,
}
\tag{7}
\]

with reverse blocks given by transposition.

Thus the bulk separates by column parity.

### Even-column chain

The even columns

\[
 0,2,4,\ldots,2r=s-1
\]

form a block path of length `r+1`, with diagonal block `G` and off-diagonal
block `-I_L`.

### Odd-column chain

The odd columns

\[
 1,3,5,\ldots,2r-1=s-2
\]

form the same block path of length `r`.

The seam blocks (7) couple only the four path endpoints.

## 3. Matrix continuants

Define matrix polynomials

\[
 D_{-1}(G)=0,
 \qquad
 D_0(G)=I,
 \qquad
 D_n(G)=G D_{n-1}(G)-D_{n-2}(G).
\tag{8}
\]

Because all `D_n(G)` are polynomials in the same real symmetric matrix `G`,
they commute.

A block path with `m>=2` vertices, diagonal `G` and off-diagonal `-I`, has,
after eliminating its `m-2` interior blocks, the endpoint Schur complement

\[
 \boxed{
 \begin{pmatrix}
 H_m&-J_m\\
 -J_m&H_m
 \end{pmatrix},
 }
\tag{9}
\]

where

\[
 H_m=D_{m-1}(G)D_{m-2}(G)^{-1},
 \qquad
 J_m=D_{m-2}(G)^{-1}.
\tag{10}
\]

This is the matrix-valued continuant analogue of the usual scalar path
identity.

For the two parity chains put

\[
 H_e=D_rD_{r-1}^{-1},
 \qquad
 J_e=D_{r-1}^{-1},
\tag{11}
\]

and

\[
 H_o=D_{r-1}D_{r-2}^{-1},
 \qquad
 J_o=D_{r-2}^{-1}.
\tag{12}
\]

## 4. The `4L` endpoint matrix

Order the four endpoint blocks as

\[
 E_0=0,
 \qquad
 E_r=s-1,
 \qquad
 O_0=1,
 \qquad
 O_{r-1}=s-2.
\]

Eliminating every interior column gives the exact endpoint Schur complement

\[
\boxed{
\mathcal S_{L,r}^{\varepsilon,\alpha}
=
\begin{pmatrix}
 H_e&-J_e+M&0&P\\
 -J_e+M^T&H_e&P^T&0\\
 0&P&H_o&-J_o\\
 P^T&0&-J_o&H_o
\end{pmatrix}.
}
\tag{13}
\]

Its dimension is `4L`, independent of `s` except through the continuant index
`r=(s-1)/2`.

This is the promised exact reduction from `Ls` dimensions to `4L`.

## 5. Inertia equivalence

The reduction is especially useful because no sign information is lost.

The signed cycle block `B` satisfies

\[
 \|B\|\le2,
\]

hence

\[
 G=6I-B^2\ge2I.
\tag{14}
\]

After diagonalizing `G`, every interior parity-path block becomes a direct
sum of scalar path matrices with diagonal `g>=2` and off-diagonal `-1`.
Every such finite path matrix is positive definite, since

\[
 g-2\cos\frac{\pi}{m+1}>0.
\]

Therefore the principal block eliminated in forming (13) is positive
definite.  Sylvester inertia additivity for Schur complements gives

\[
 \boxed{
 n_-(C)=n_-(\mathcal S_{L,r}^{\varepsilon,\alpha}),
 }
\tag{15}
\]

and in particular

\[
 \boxed{
 8I-A^2>0
 \iff
 \mathcal S_{L,r}^{\varepsilon,\alpha}>0.
 }
\tag{16}
\]

The determinant has the same sign as well, because the eliminated interior
determinant is positive.

Thus the question whether the one-defect signing lies below `sqrt(8)` is
**exactly** a `4L`-dimensional endpoint positivity problem.

## 6. Soft and hard layer channels

The row matrix `G` has a distinguished soft mode.  After a switching and a
permutation by the step-two order on the odd cycle, `G` is equivalent to

\[
 4I-A(C_L),
\tag{17}
\]

in the appropriate chord-flux sector.  Its smallest eigenvalue is `2`.
On that scalar channel the matrix continuant becomes

\[
 D_n(2)=n+1.
\tag{18}
\]

Hence the soft-channel endpoint impedances are rational functions whose
leading scale is linear in the parity-path lengths `r+1` and `r`.
All remaining row modes have `G`-eigenvalue strictly larger than `2` and
therefore have exponentially stabilizing continuants.

This separates the prospective general proof into:

1. one soft layer channel carrying the aspect-ratio dependence;
2. finitely many hard layer channels that can be Schur-complemented into a
   seam scattering correction.

The empirical critical law `s=2L`, proved separately for `L=3,5,7,9`, should
therefore be sought as an endpoint/Robin condition in (13), rather than as a
large `Ls` determinant identity.

## 7. Verified regression

The companion script `verify_one_defect_endpoint_reduction.py` constructs both
`C` and (13) and checks representative cases on both sides of the observed
threshold:

\[
 (L,s)=(5,9),(5,11),(7,13),(7,15),(9,17),(9,19).
\]

In every case the negative inertia of the full threshold matrix agrees with
the endpoint matrix: zero negatives on the sub-eight side and one negative on
the super-eight side.  The determinant signs also agree.

These numerical checks are only an indexing regression; equations (5)--(16)
are the analytic proof of the reduction.

## 8. Consequences and next target

The reduction changes the general odd-`L` conjecture from an expanding graph
problem into a fixed-width matrix-function problem:

\[
 \mathcal S_{L,r}^{\varepsilon,\alpha}>0\ ?
\]

The next analytic target is to eliminate the hard layer modes of (13) and
obtain a scalar or low-rank soft-channel determinant.  A successful formula
should explain the observed one-defect phase transition

\[
 s<2L\quad\text{versus}\quad s>2L
\]

uniformly for all odd `L`.

The theorem concerns only the canonical one-defect family.  It does not
classify all signings for `L>=5`.
