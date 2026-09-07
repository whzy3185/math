# Canonical one-defect critical staircase and continuum program

Date: 2026-09-07.

This note records the corrected large-`L` program after the exact
`L=13` counterexample to the naive `s=2L` extrapolation.  It combines exact
finite-dimensional algebra with a numerical continuum candidate.  The
limiting constant in this note is **Observed**, not a theorem.

## 1. Exact starting point

For odd `L,s`, the favorable canonical one-defect signing on `C_(Ls)(1,s)`
has two exact reductions:

1. `ONE_DEFECT_ENDPOINT_REDUCTION.md`:
   \[
   Ls\times Ls\quad\longrightarrow\quad4L\times4L
   \]
   by a matrix-continuant Schur complement;
2. `ONE_DEFECT_RANK4_GREEN_CRITERION.md`:
   \[
   8I-A^2>0
   \iff
   \lambda_{\max}(\mathcal G_-(L,s))<\frac12,
   \]
   where `mathcal G_-` is a `2 x 2` reflection-odd Green matrix.

Thus the threshold is a scalar crossing in a two-dimensional
Birman--Schwinger channel.

## 2. A second exact row reduction

Let

\[
 G=6I-B^2
\]

be the `L x L` row block in the endpoint theorem and let

\[
 P=-S_\alpha^T
\]

be the seam monomial matrix, in the favorable `alpha=+1` sector.

For `L=2m+1`, reorder the row vertices by the step-two order

\[
 a=2k\pmod L
\]

and switch along the row cycle so that `G` becomes the ordinary cycle
Laplacian shift form

\[
 G'=4I-T-T^T.
\tag{1}
\]

Let `P'` be the seam matrix in the same gauge.  Then a direct sign chase gives

\[
 \boxed{(P')^L=-I}
\tag{2}
\]

and the exact rank-two relation

\[
\boxed{
 G'=4I+(P')^2+(P'^T)^2
 -2(E_{m,m+1}+E_{m+1,m}).
}
\tag{3}
\]

Hence `P'` is a negative-holonomy cyclic shift, and `G'` differs from the
matrix that is exactly Fourier-diagonal in the `P'` basis by only one row
edge flip.

Equation (3) identifies the residual obstruction as a one-edge change of row
spin structure, rather than a large uncontrolled matrix effect.

## 3. Real-length continuation of the continuants

For a scalar row eigenvalue

\[
 g=2\cosh\eta\ge2,
\]

the path continuant is

\[
 D_n(g)=\frac{\sinh((n+1)\eta)}{\sinh\eta}.
\]

This formula has a natural continuation in the path length.  For real
`m>1`, define endpoint impedance functions

\[
 h_m(g)=\frac{\sinh(m\eta)}{\sinh((m-1)\eta)},
 \qquad
 j_m(g)=\frac{\sinh\eta}{\sinh((m-1)\eta)}.
\tag{4}
\]

At the soft value `g=2`, use the continuous limits

\[
 h_m(2)=\frac m{m-1},
 \qquad
 j_m(2)=\frac1{m-1}.
\tag{5}
\]

Replacing the integer

\[
 r=\frac{s-1}{2}
\]

in the `4L` endpoint matrix by a real variable using (4)--(5) defines a
natural continuous threshold function

\[
 F_L(r)=\lambda_{\max}(\mathcal G_-(L,r))-\frac12.
\tag{6}
\]

This continuation is a computational/analytic interpolation; only integer
`r` corresponds to an actual finite graph.

## 4. Continuous critical roots

Let `r_L` denote the numerically determined root of

\[
 F_L(r_L)=0
\]

near the first one-defect threshold, and define

\[
 c_L=\frac{2r_L+1}{L}.
\tag{7}
\]

Using the exact endpoint formulas with stable hyperbolic evaluation gives:

\[
\begin{array}{c|c}
L&c_L\\ \hline
13&2.0814188208\\
21&2.0915846092\\
31&2.0947584792\\
51&2.0964173204\\
101&2.0971338227\\
201&2.0973163958\\
301&2.0973505333\\
401&2.0973625250\\
501&2.0973680862\\
701&2.0973729361.
\end{array}
\tag{8}
\]

A simple inverse-size extrapolation of these values suggests

\[
 \boxed{c_*\approx2.097378.}
\tag{9}
\]

Again, (8)--(9) are **Observed numerical asymptotics**, not proved limits.
They replace the disproved `c_*=2` guess.

## 5. Why the integer thresholds form a staircase

At the continuous crossing, the Green matrix itself approaches

\[
 \mathcal G_-\to\frac12 I_2.
\]

The sign is decided at the next scale.  At the critical aspect ratio,
numerics give

\[
 \frac12-(\mathcal G_-)_{11}=\Theta(L^{-1}),
 \qquad
 |(\mathcal G_-)_{12}|=\Theta(L^{-1}),
\]

with the two coefficients canceling in the largest eigenvalue.

Therefore moving `r` by one integer changes the threshold at precisely the
same small scale as the finite-`L` correction.  The first failing odd `s`
necessarily moves in a staircase rather than following a single formula such
as `2L+1`.

This also explains why the small cases `L=3,5,7,9,11` accidentally shared the
same integer offset.

## 6. Limiting operator target

For row Fourier wave number `k` fixed as `L->infinity`, the ordinary cycle
block has

\[
 g_k=4-2\cos\frac{2\pi k}{L}
 =2+\frac{4\pi^2k^2}{L^2}+O(L^{-4}).
\]

If

\[
 r/L\to\gamma=c/2,
\]

then the scaled endpoint impedances from (4) converge to the
Dirichlet-to-Neumann multipliers

\[
 a_\gamma(k)=2\pi|k|\coth(2\pi|k|\gamma),
\]

\[
 b_\gamma(k)=2\pi|k|\operatorname{csch}(2\pi|k|\gamma),
\tag{10}
\]

with the `k=0` values interpreted as `1/gamma`.

The remaining seam matrix is the negative-holonomy monomial `P'`, related to
the row Laplacian by the one-edge identity (3).  The next theorem target is
to prove convergence of the finite endpoint Green matrix to the
Dirichlet-to-Neumann problem obtained from (10) plus this single row
spin-structure defect.

The desired limiting theorem would produce a function

\[
 F_\infty(c)
 =\lim_{L\to\infty}
 L\left(\lambda_{\max}(\mathcal G_-(L,cL))-\frac12\right)
\tag{11}
\]

and characterize the critical constant by

\[
 \boxed{F_\infty(c_*)=0.}
\tag{12}
\]

Numerically, `F_infty(c)` changes sign once near the value (9).

## 7. Scope

The continuum program concerns only the canonical one-defect family.  Even a
complete proof of (12) would not classify `m(Ls,s)` over all signings for
`L>=5`.

The all-signing finite problem remains a separate branch: `L=3` is solved,
whereas `L=5` already has a substantially larger recurrent finite-state
space and may require a global invariant or a multi-defect counterexample.
