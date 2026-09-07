# Observed large-`L` critical ratio for the canonical one-defect family

Date: 2026-09-07.

This note is **numerical exploration only**.  It uses the exact analytic
`4L` endpoint reduction from `ONE_DEFECT_ENDPOINT_REDUCTION.md`, but the
large-`L` limiting statement below is not yet a theorem.

For odd `L`, extend the continuant index

\[
 r=(s-1)/2
\]

from integers to a positive real parameter by the scalar spectral formula
for each eigenvalue `g>=2` of the layer matrix `G`:

\[
 D_n(g)=\frac{\sinh((n+1)\eta)}{\sinh\eta},
 \qquad 2\cosh\eta=g,
\]

with the soft limit `D_n(2)=n+1`.

This gives a continuous endpoint matrix

\[
 \mathcal S_{L,r}^{-1,+1}
\]

for the favorable one-defect sector.  Define `r_c(L)` by the zero of its
smallest eigenvalue and put

\[
 c_L=\frac{2r_c(L)+1}{L}.
\]

## Current numerical values

The companion explorer gives

\[
\begin{array}{c|c}
L & c_L\\ \hline
51  & 2.09641732044\\
75  & 2.09693479476\\
101 & 2.09713382272\\
151 & 2.09726882132\\
201 & 2.09731639583.
\end{array}
\]

A fit of the four largest rows to

\[
 c_L=c_\infty+\frac aL+\frac b{L^2}
\]

gives `c_infty` about `2.0973775` and a numerically tiny `a`.  A fit to the
even-power ansatz

\[
 c_L=c_\infty+\frac b{L^2}+\frac d{L^4}
\]

gives

\[
 \boxed{c_\infty\approx2.0973780}
\]

with leading finite-size correction near `-2.49/L^2`.

The apparent absence of a `1/L` correction is itself only an observation at
this stage.

## Conjectural asymptotic statement

The data motivate the working conjecture that the favorable canonical
one-defect threshold has a limit

\[
 \boxed{
 \frac{s_c(L)}L\longrightarrow c_*\approx2.097378
 }
\]

through odd `L`, with an expansion beginning at order `L^-2`.

The integer staircase then arises by rounding the continuous threshold to the
nearest admissible odd `s`.  This is consistent with the exact rows already
proved for

`L=3,5,7,9,11,13,15,17,19`.

## Analytic target

The exact endpoint matrix is a fixed-rank seam perturbation of two
matrix-valued path Dirichlet-to-Neumann maps.  The likely route to a theorem is:

1. separate the soft layer modes of `G=6I-B^2` from the exponentially stable
   hard modes;
2. take `L,r->infinity` with `r/L` fixed;
3. derive the limiting seam Green/Birman--Schwinger matrix;
4. reduce its zero-eigenvalue condition to a scalar equation for
   `t=r/L`;
5. prove uniqueness of the positive critical root and identify
   `c_*=2t_*`.

No closed form for `c_*` is currently claimed.