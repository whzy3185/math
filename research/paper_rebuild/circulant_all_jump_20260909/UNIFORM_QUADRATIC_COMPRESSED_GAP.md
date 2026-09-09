# Uniform quadratic gap bounds for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

For even `L>=4` and `q>=0`, let

\[
\Gamma_{L,q}=8-R_{L,q}
\]

be the global continuous squared Bloch gap of the period-`2L` compressed two-defect phase with jump `s=L(2q+1)`.

Put

\[
x_0=\arccos(1/3).
\]

The general compression theorem proves `Gamma_(L,q)>0` for every parameter, while the global sharp-gap theorem proves uniformly in the odd multiplier

\[
L^2\Gamma_{L,q}\longrightarrow4x_0^2.
\]

The present note packages these facts into a nonasymptotic quadratic-scale theorem and replaces the old exponentially small existence bound as the correct qualitative finite-scale estimate.

## Theorem A — global two-sided quadratic scale

There exists an absolute constant

\[
\boxed{c_*>0}
\]

such that for every even `L>=4` and every `q>=0`,

\[
\boxed{
\frac{c_*}{L^2}
\le \Gamma_{L,q}
<\frac{\pi^2}{L^2}.
}
\tag{1}
\]

Thus the compressed two-defect family has a genuinely polynomial, rather than exponentially small, spectral gap uniformly over the whole odd-multiplier parameter.

The lower constant `c_*` is asserted existentially here; the sharp asymptotic theorem identifies the optimal large-`L` constant.

### Proof of the upper bound

Let

\[
e_L=8-\rho(H_{L,q}(1))^2
\]

be the endpoint gap. Since the global Bloch edge is the maximum over all phases,

\[
\Gamma_{L,q}\le e_L.
\]

Write `L=2r`. The endpoint Robin theorem gives

\[
e_L=2-2\cos(x_r/r),
\qquad 0<x_r<\pi/2.
\]

Using `2-2 cos u<u^2` for `u>0`,

\[
e_L
<\frac{x_r^2}{r^2}
<\frac{\pi^2}{4r^2}
=\frac{\pi^2}{L^2}.
\]

This proves the right side of (1).

### Proof of the lower bound

The global sharp-gap theorem is uniform in the sequential sense with respect to `q`: for every sequence of even `L->infinity` and arbitrary integers `q=q(L)>=0`,

\[
L^2\Gamma_{L,q}\to4x_0^2>0.
\]

Equivalently, uniform convergence holds over the odd multiplier. Hence there exists an even `L_1` such that

\[
L^2\Gamma_{L,q}\ge2x_0^2
\tag{2}
\]

for every even `L>=L_1` and every `q>=0`.

For the finitely many even `L` with `4<=L<L_1`, the general compression theorem gives the explicit positive estimate

\[
\Gamma_{L,q}\ge\frac{16}{8^{L-1}}
\]

uniformly in `q`. Therefore

\[
c_*:=\min\left\{
2x_0^2,
\min_{\substack{4\le L<L_1\\L\text{ even}}}
\frac{16L^2}{8^{L-1}}
\right\}>0
\]

is independent of both `L` and `q` and proves the left side of (1).

## Theorem B — asymptotically arbitrary sharp lower constant

For every real number

\[
0<c<4x_0^2,
\]

there exists an even `L_c` such that for every even `L>=L_c` and every `q>=0`,

\[
\boxed{
\Gamma_{L,q}\ge\frac{c}{L^2}.
}
\tag{3}
\]

Likewise, for every `C>4x_0^2`, after enlarging `L_c` if necessary,

\[
\boxed{
\Gamma_{L,q}\le\frac{C}{L^2}
}
\tag{4}
\]

uniformly in `q`.

This is simply the epsilon form of the uniform sharp limit, but it is useful in the manuscript because it states directly that the determinant estimate `16/8^(L-1)` is only a coarse certificate of positivity, not the actual spectral scale.

## Corollary C — period form

Writing the primitive period as

\[
p=2L,
\]

there is an absolute `c_*>0` such that

\[
\boxed{
\frac{4c_*}{p^2}
\le 8-R_{L,q}
<\frac{4\pi^2}{p^2}.
}
\]

Moreover the sharp period-normalized constant is

\[
\boxed{
p^2\Gamma_{L,q}\to16\arccos(1/3)^2}
\]

uniformly over arbitrary odd multipliers.

## Editorial consequence

The old bound

\[
\Gamma_{L,q}\ge16/8^{L-1}
\]

should remain only as an elementary finite positivity certificate. The theorem-level quantitative statement for the compressed family is now the quadratic law (1), with the sharp constant supplied by the global asymptotic theorem.