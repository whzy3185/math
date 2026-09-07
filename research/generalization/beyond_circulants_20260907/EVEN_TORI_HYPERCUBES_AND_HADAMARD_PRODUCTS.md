# Even tori, hypercubes, and Hadamard-product corollaries

Date: 2026-09-07.

This note applies `GENERAL_CLIFFORD_PRODUCT_THEOREM.md` to several concrete
families beyond `C_N(1,s)`.

## 1. Even-cycle tori

Let

\[
T(n_1,\dots,n_d)=C_{n_1}\square\cdots\square C_{n_d},
\qquad n_j\ge4\text{ even}.
\]

On each factor choose the antiperiodic signed cycle: all path edges positive
and the closing edge negative.  Its eigenvalues are

\[
2\cos\frac{(2k+1)\pi}{n_j},
\]

so its signed spectral radius is

\[
\rho_j=2\cos\frac\pi{n_j}.
\]

The Clifford product signing therefore satisfies

\[
\boxed{
\rho(T)^2=4\sum_{j=1}^d\cos^2\frac\pi{n_j}.}
\tag{T1}
\]

Equivalently, relative to the infinite `pi`-flux threshold `4d`, the squared
gap is exactly

\[
\boxed{
4d-\rho(T)^2=4\sum_{j=1}^d\sin^2\frac\pi{n_j}.}
\tag{T2}
\]

Hence if all side lengths tend to infinity,

\[
4d-\rho(T)^2
=4\pi^2\sum_j n_j^{-2}+O\!\left(\sum_j n_j^{-4}\right).
\tag{T3}
\]

For `d=2` this gives an explicit signing of every even-by-even toroidal grid
with

\[
\rho^2=4\cos^2(\pi/m)+4\cos^2(\pi/n)<8.
\]

## 2. Exact flat tori `C_4^square d`

For the antiperiodic signed `C_4`,

\[
A(C_4)^2=2I.
\]

Therefore on

\[
C_4^{\square d}
\]

the Clifford product signing satisfies

\[
A^2=2dI.
\]

The underlying graph is `2d`-regular, so the universal trace bound gives
`rho>=sqrt(2d)` for every signing.  Thus

\[
\boxed{m(C_4^{\square d})=\sqrt{2d}.}
\tag{T4}
\]

This includes the 4-regular `C_4 square C_4` toral tessellation with exact
minimum `2`.

## 3. Hypercubes

Take every factor to be `K_2`.  Its adjacency matrix squares to `I`, so the
construction gives on the `d`-cube `Q_d=K_2^{square d}`

\[
A^2=dI.
\]

Since `Q_d` is `d`-regular,

\[
\boxed{m(Q_d)=\sqrt d.}
\tag{H1}
\]

This recovers the well-known Huang/Clifford signing as a special case of the
general product theorem.

## 4. Mixed flat products

Combining `p` copies of `K_2` and `q` copies of `C_4` gives

\[
G=Q_p\square C_4^{\square q},
\]

a `(p+2q)`-regular graph with

\[
\boxed{m(G)=\sqrt{p+2q}.}
\tag{M1}
\]

This already gives infinitely many exact-minimum signed graph families with
varying degree and non-isomorphic product geometry.

## 5. Hadamard bipartite factors

If a Hadamard matrix `H` of order `q` exists, then the signing of `K_{q,q}`
with adjacency

\[
A_H=\begin{pmatrix}0&H\\H^T&0\end{pmatrix}
\]

satisfies

\[
A_H^2=qI.
\]

Hence `m(K_(q,q))=sqrt(q)`, and any Cartesian product of such Hadamard
bipartite factors, hypercubes and flat `C_4` factors has exact minimum equal
to the square root of its total degree.

For example, if Hadamard orders `q_1,...,q_t` are available, then

\[
\boxed{
m\!\left(Q_p\square C_4^{\square r}\square
\prod_{j=1}^t K_{q_j,q_j}\right)
=\sqrt{p+2r+\sum_j q_j}.}
\tag{M2}
\]

## 6. Evidence boundary

All displayed identities are direct analytic consequences of the Clifford
product theorem plus elementary factor spectra.  The Python verifier
`verify_clifford_product_families.py` independently checks representative
matrix identities.  Literature on signed toral tessellations, signed graphs
with two eigenvalues, and Huang-type product constructions overlaps strongly
with several special cases, so novelty should be claimed only for any new
synthesis or downstream application, not for the known special families.
