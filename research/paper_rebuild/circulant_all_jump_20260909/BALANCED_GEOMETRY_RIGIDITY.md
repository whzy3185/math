# Quantitative rigidity of asymptotically optimal defect geometry

Date: 2026-09-10

Status: **Proved**. This is an immediate but useful consequence of the full-Bloch macroscopic gap law.

## 1. Setup

Let

\[
L=2(N+m),\qquad h=2m,
\]

with

\[
N,m\to\infty,
\qquad
\alpha:=\frac hL=\frac m{N+m}.
\]

For an arbitrary odd multiplier let

\[
\Gamma_{N,m,q}=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The full-Bloch macroscopic theorem gives, whenever

\[
\alpha\to\alpha_0\in(0,1),
\]

\[
\boxed{
L^2\Gamma_{N,m,q}
\longrightarrow
E(\alpha_0):=
\frac{\pi^2}{\max\{\alpha_0,1-\alpha_0\}^2}.
}
\tag{1.1}
\]

## Theorem A — unique asymptotic optimizer

For every `alpha_0 in (0,1)`,

\[
\boxed{E(\alpha_0)\le4\pi^2,}
\tag{1.2}
\]

with equality if and only if

\[
\boxed{\alpha_0=\frac12.}
\tag{1.3}
\]

Thus balanced defect geometry is the unique macroscopic optimizer of the leading full-Bloch gap constant.

## Theorem B — quantitative stability

Fix `epsilon in (0,1/2)`. If a sequence of geometries satisfies

\[
\left|\frac hL-\frac12\right|\ge\epsilon
\]

for all sufficiently large indices, then

\[
\boxed{
\limsup L^2\Gamma_{N,m,q}
\le
\frac{4\pi^2}{(1+2\epsilon)^2}
<4\pi^2.
}
\tag{1.4}
\]

Equivalently, there is a definite leading-order spectral penalty for every fixed macroscopic imbalance.

### Proof

If

\[
|\alpha-1/2|\ge\epsilon,
\]

then

\[
\max\{\alpha,1-\alpha\}
=\frac12+|\alpha-1/2|
\ge\frac12+\epsilon.
\]

Substitution into (1.1) gives

\[
E(\alpha)
\le
\frac{\pi^2}{(1/2+\epsilon)^2}
=
\frac{4\pi^2}{(1+2\epsilon)^2}.
\]

This proves (1.4).

## Corollary C — near-optimal sequences must balance

Suppose

\[
\limsup L^2\Gamma_{N,m,q}=4\pi^2.
\]

Then necessarily

\[
\boxed{
\frac hL\longrightarrow\frac12.
}
\tag{1.5}
\]

Indeed, otherwise some subsequence would stay a positive distance from `1/2`, contradicting Theorem B.

## Corollary D — first-order loss away from balance

Write

\[
\alpha=\frac12+\delta.
\]

Then the exact leading constant is

\[
E(\alpha)=\frac{4\pi^2}{(1+2|\delta|)^2}.
\]

Consequently, as `delta->0`,

\[
\boxed{
E(1/2+\delta)
=4\pi^2
-16\pi^2|\delta|
+48\pi^2\delta^2
+O(|\delta|^3).
}
\tag{1.6}
\]

The cusp at `delta=0` reflects competition between the two endpoint soft channels: the longer arc immediately controls the global edge once the geometry becomes unbalanced.

## 2. Interpretation

The balanced phase is not merely one aesthetically symmetric choice. The macroscopic spectral problem has a genuine variational rigidity:

\[
\text{near-optimal normalized gap}
\Longrightarrow
\text{near-balanced defect geometry}.
\]

Moreover the loss from imbalance is linear in `|alpha-1/2|` at first order, rather than quadratic. This non-smooth geometry dependence is another manifestation of the two-well nature of the Bloch edge.