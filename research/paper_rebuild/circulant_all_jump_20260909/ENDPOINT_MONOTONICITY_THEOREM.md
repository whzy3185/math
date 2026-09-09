# Endpoint quantization monotonicity for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I.

Let `L=2r` with `r>=2`, and let `x_r in (0,pi/2)` be the unique endpoint Robin root from `COMPRESSED_ENDPOINT_SHARP_GAP.md`:

\[
3\cos x_r+2\tan\frac{x_r}{2r}\sin x_r=1.
\tag{1}
\]

Put

\[
x_0:=\arccos(1/3),
\qquad
\theta_r:=x_r/r,
\qquad
e_{2r}:=2-2\cos\theta_r.
\]

Then `8-e_(2r)` is the top squared eigenvalue of the periodic Bloch fiber `z=1`.

## Theorem A — strict monotonicity

For every `r>=2`,

\[
\boxed{x_0<x_{r+1}<x_r<\frac\pi2.}
\tag{2}
\]

Consequently

\[
\boxed{\theta_{r+1}<\theta_r,\qquad e_{2r+2}<e_{2r}.}
\tag{3}
\]

Equivalently, the endpoint squared spectral edge is strictly increasing with the compressed half-period:

\[
\boxed{
\rho(H_{2r+2,q}(1))^2>ho(H_{2r,q}(1))^2.
}
\tag{4}
\]

The statement is independent of the odd multiplier `2q+1`, because the `z=1` fiber is.

### Proof

For real `r>=2`, define

\[
\Phi_r(x):=3\cos x+2\tan\frac{x}{2r}\sin x,
\qquad 0\le x\le\frac\pi2.
\]

The endpoint analysis already proves that `Phi_r` is strictly decreasing in `x` on this interval and that `x_r` is its unique solution of `Phi_r(x)=1`.

For fixed `x in (0,pi/2]`, the map

\[
r\longmapsto \tan\frac{x}{2r}
\]

is strictly decreasing. Hence

\[
\Phi_{r+1}(x)<\Phi_r(x).
\tag{5}
\]

At `x=x_r`, (5) gives

\[
\Phi_{r+1}(x_r)<1.
\]

Since `Phi_(r+1)` is strictly decreasing and equals `1` at `x_(r+1)`, it follows that

\[
x_{r+1}<x_r.
\]

On the other hand, (1) gives

\[
3\cos x_r
=1-2\tan\frac{x_r}{2r}\sin x_r<1,
\]

so `cos x_r<1/3`, hence

\[
x_r>x_0.
\]

This proves (2). Since both the numerator decreases and the denominator increases,

\[
\frac{x_{r+1}}{r+1}<\frac{x_r}{r},
\]

which proves the first part of (3). The function `2-2 cos theta` is strictly increasing for `theta in (0,pi)`, so the second part follows. Equation (4) is equivalent to it.

## Theorem B — explicit finite localization

For every `r>=2`,

\[
\boxed{
0<x_r-x_0
\le \frac1{\sqrt2}\tan\frac{\pi}{4r}.
}
\tag{6}
\]

In particular,

\[
x_r=x_0+O(r^{-1})
\]

with an explicit bound valid at every finite `r`.

### Proof

Subtract `3 cos x_0=1` from (1):

\[
3(\cos x_0-\cos x_r)
=2\tan\frac{x_r}{2r}\sin x_r.
\tag{7}
\]

By the mean-value theorem, for some `xi in (x_0,x_r)`,

\[
\cos x_0-\cos x_r
=\sin\xi\,(x_r-x_0)
\ge \sin x_0\,(x_r-x_0).
\]

Since

\[
\sin x_0=\frac{2\sqrt2}{3},
\]

and `x_r<pi/2`, the right side of (7) is at most

\[
2\tan\frac{\pi}{4r}.
\]

Therefore

\[
2\sqrt2\,(x_r-x_0)
\le2\tan\frac\pi{4r},
\]

which is (6).

## Corollary C — explicit finite gap enclosure

For every `r>=2`,

\[
2-2\cos\frac{x_0}{r}
<e_{2r}
\le
2-2\cos\left(
\frac{x_0}{r}+\frac{1}{\sqrt2 r}\tan\frac\pi{4r}
\right).
\tag{8}
\]

Thus the exact endpoint gap is trapped between two elementary expressions without solving any polynomial or eigenvalue problem.

## Role in the paper

This result upgrades the endpoint asymptotic analysis in two ways:

1. it gives a strict finite-parameter ordering, not merely a limit;
2. it provides explicit nonasymptotic control of the Robin root used in later Bloch-phase comparison estimates.

It does not by itself assert global endpoint dominance over all Bloch phases.