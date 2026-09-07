# Rank-four defect and exact 2-by-2 Green criterion for the canonical one-defect family

Date: 2026-09-07.

This note strengthens `ONE_DEFECT_ENDPOINT_REDUCTION.md`.  For the favorable
canonical one-defect sector it reduces the threshold question from `Ls`
dimensions, first to `4L`, and then conceptually to a **2-by-2 Green matrix**.

A subtlety is important: the positive reference operator below is not an
ordinary scalar circulant on an odd-by-odd finite quotient.  It retains the
helical `Z_2` seam.  The rank-four perturbation and the 2-by-2 criterion are
nevertheless exact.

Throughout let `L,s` be odd, `N=Ls`, and use

\[
 \tau_i=-(-1)^i
\]

with positive Hamilton holonomy `alpha=+1`.  This is the favorable
unbalanced chord-cycle one-defect sector studied in the preceding threshold
notes.

## 1. Split the signed adjacency into two directions

Write

\[
 A=X+Y,
\]

where `X` contains the step-one edges and `Y` contains the step-`s` chord
edges.  Both `X` and `Y` are real symmetric degree-two signed adjacencies.

Define the positive reference threshold

\[
 C_0=(4I-X^2)+(4I-Y^2).
\tag{1}
\]

Then

\[
 C:=8I-A^2
 =C_0-(XY+YX).
\tag{2}
\]

For any signed graph of maximum degree two, the adjacency norm is at most
`2`; hence

\[
 4I-X^2\ge0,
 \qquad
 4I-Y^2\ge0.
\]

In the canonical odd one-defect configuration their kernels do not intersect:
a common `|lambda|=2` vector would impose a globally compatible alternating
mixed flux, impossible on the odd cyclic Hamilton word.  Therefore

\[
 \boxed{C_0>0.}
\tag{3}
\]

Equivalently, this positivity can be read directly from the block-path
representation in `ONE_DEFECT_ENDPOINT_REDUCTION.md` after deleting the mixed
seam block `M`.

## 2. The anticommutator is supported on only two edges

The mixed path coefficients cancel everywhere except at the cyclic parity
defect.  A direct use of the universal squared-operator formula gives

\[
 K:=XY+YX
 =-2(E_{0,s-1}+E_{s-1,0})
   -2(E_{s,N-1}+E_{N-1,s}).
\tag{4}
\]

Thus

\[
 \boxed{\operatorname{rank}K\le4.}
\tag{5}
\]

Put

\[
 p=0,
 \quad q=s-1,
 \quad r=s,
 \quad t=N-1.
\]

The entire difference between the true threshold `C` and the positive
reference `C_0` is supported on these four vertices.

## 3. Reflection decomposition

The involution

\[
 \mathcal R(i)=s-1-i\pmod N
\tag{6}
\]

preserves `C_0`.  On the four defect vertices it swaps

\[
 p\leftrightarrow q,
 \qquad
 r\leftrightarrow t.
\]

Introduce the normalized even and odd defect vectors

\[
 u_1^+=\frac{e_p+e_q}{\sqrt2},
 \quad
 u_2^+=\frac{e_r+e_t}{\sqrt2},
\]

\[
 u_1^-=\frac{e_p-e_q}{\sqrt2},
 \quad
 u_2^-=\frac{e_r-e_t}{\sqrt2}.
\tag{7}
\]

On the reflection-even defect subspace,

\[
 K=-2I_2,
\]

so passing from `C_0` to `C=C_0-K` adds a positive rank-two perturbation.
This sector can never create a negative threshold eigenvalue.

On the reflection-odd defect subspace,

\[
 K=+2I_2,
\]

so the true threshold subtracts a rank-two positive perturbation.  All
possible loss of positivity therefore occurs in this two-dimensional channel.

## 4. The exact Green matrix

Let

\[
 G_0=C_0^{-1}.
\]

Define the `2 x 2` reflection-odd Green matrix

\[
\boxed{
 \mathcal G_-=
 \begin{pmatrix}
 \langle u_1^-,G_0u_1^-\rangle&
 \langle u_1^-,G_0u_2^-\rangle\\
 \langle u_2^-,G_0u_1^-\rangle&
 \langle u_2^-,G_0u_2^-\rangle
 \end{pmatrix}.
}
\tag{8}
\]

Since `C_0>0`, the matrix `mathcal G_-` is positive definite.

A rank-two Schur-complement / matrix-determinant-lemma argument gives the
central criterion.

**Theorem G2 (exact Green criterion).**

\[
\boxed{
 8I-A^2>0
 \iff
 I_2-2\mathcal G_->0
 \iff
 \lambda_{\max}(\mathcal G_-)<\frac12.
}
\tag{9}
\]

Similarly,

\[
 \lambda_{\max}(\mathcal G_-)>\frac12
\]

implies that `8I-A^2` has a negative eigenvalue and hence

\[
 \rho(A)^2>8.
\]

At equality, the signed spectral radius touches `sqrt(8)`.

Thus the canonical one-defect threshold is governed exactly by one scalar
crossing of a 2-by-2 positive matrix.

## 5. Entrywise form

Let

\[
 R_{ab}=e_a^T C_0^{-1}e_b.
\]

Reflection symmetry gives

\[
\mathcal G_-=
\begin{pmatrix}
 R_{pp}-R_{pq} &
 \frac12(R_{pr}-R_{pt}-R_{qr}+R_{qt})\\
 \frac12(R_{pr}-R_{pt}-R_{qr}+R_{qt}) &
 R_{rr}-R_{rt}
\end{pmatrix}.
\tag{10}
\]

This formula is exact and does not assume ordinary translation invariance.
On the odd finite quotient, `C_0` still carries the helical seam, so the
entries in (10) should be computed by the width-`L` block/continuant model,
not by an unjustified scalar circulant Fourier formula.

## 6. Relation to the `4L` endpoint matrix

In the endpoint reduction, the mixed seam block `M` is precisely the
rank-four perturbation encoded by `K`.  Setting `M=0` produces the endpoint
Schur complement of `C_0`; restoring `M` performs the rank-four update.

Consequently `mathcal G_-` can be computed without inverting an `Ls x Ls`
matrix: invert only the `4L x 4L` endpoint matrix with `M=0`, or eliminate its
reflection-even channel first.  This gives an efficient exact route for large
`L`.

## 7. Regression values

The companion script `verify_one_defect_green_criterion.py` compares the
2-by-2 criterion with the full threshold matrix in representative cases.
For example, the largest eigenvalue of `mathcal G_-` is

- below `1/2` for `(L,s)=(5,9)` and `(13,27)`;
- above `1/2` for `(L,s)=(5,11)` and `(13,29)`.

The sign agrees with the exact threshold classification in every tested case.

These floating values are regression only.  The equivalence (9) is an exact
rank-two perturbation theorem.

## 8. New asymptotic target

The observed critical staircase is now reduced to the study of

\[
 \lambda_{\max}(\mathcal G_-(L,s))=\frac12.
\tag{11}
\]

The large-`L` problem is to take `L,s->infinity` with `s/L->c`, derive the
continuum Dirichlet-to-Neumann limit of the positive reference operator
`C_0`, and obtain a limiting `2 x 2` Green matrix

\[
 \mathcal G_-^{\infty}(c).
\]

The numerical critical ratio near `2.0974` should then be characterized by

\[
 \lambda_{\max}(\mathcal G_-^{\infty}(c_*))=\frac12.
\tag{12}
\]

No value of `c_*` is claimed analytically yet.
