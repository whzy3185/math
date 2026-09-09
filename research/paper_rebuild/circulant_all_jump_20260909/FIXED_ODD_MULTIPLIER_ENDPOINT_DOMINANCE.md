# Eventual endpoint dominance for a fixed odd multiplier

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It strengthens the uniform global asymptotic theorem when the odd multiplier of the jump is fixed.

## 1. Statement

Fix an odd integer

\[
n=2q+1\ge1.
\]

For every even `L>=4`, consider the period-`2L` compressed two-defect phase with jump

\[
s=Ln.
\]

Let

\[
R_{L,q}=\max_{|z|=1}\rho(H_{L,q}(z))^2
\]

and let

\[
e_L=8-\rho(H_{L,q}(1))^2
\]

be the endpoint gap.

### Theorem A — eventual exact endpoint dominance

For every fixed odd multiplier `n`, there exists an even threshold `L_0(n)` such that for every even

\[
L\ge L_0(n),
\]

the global Bloch edge is attained uniquely at the periodic phase `z=1`:

\[
\boxed{
R_{L,q}=\rho(H_{L,q}(1))^2.}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
8-R_{L,q}=e_L.}
\tag{1.2}
\]

Consequently the full endpoint expansion becomes the global expansion:

\[
\boxed{
\begin{aligned}
8-R_{L,q}={}&\frac{4x_0^2}{L^2}
+\frac{16x_0^2}{3L^3}\\
&+\frac{4x_0^2}{9L^4}
\bigl(-3x_0^2+\sqrt2\,x_0+12\bigr)
+O(L^{-5}),
\end{aligned}}
\tag{1.3}
\]

where

\[
x_0=\arccos(1/3).
\]

The threshold `L_0(n)` is not optimized here.

---

## 2. Global phase localization

Let a maximizing phase be written

\[
z=e^{i\phi},
\qquad -\pi\le\phi\le\pi.
\]

The uniform global sharp-gap theorem proves, for arbitrary varying odd multipliers,

\[
z+z^{-1}\to2
\]

and

\[
L^2\left(2-z^n-z^{-n}\right)\to0.
\tag{2.1}
\]

For fixed `n`, the first statement gives

\[
\phi\to0.
\]

Moreover

\[
2-z^n-z^{-n}
=2-2\cos(n\phi)
=n^2\phi^2+O(\phi^4).
\]

Hence (2.1) yields

\[
\boxed{L\phi\to0.}
\tag{2.2}
\]

Thus every global maximizing phase eventually lies in an arbitrarily small `O(1/L)` neighborhood of the endpoint.

---

## 3. Rescaled local spectral problem

Put

\[
r=L/2,
\qquad
\phi=\frac\psi r.
\]

Fix a compact interval `|psi|<=Psi`. Then, uniformly on that interval,

\[
\mu:=2-z^n-z^{-n}
=\frac{n^2\psi^2}{r^2}+O(r^{-4}),
\tag{3.1}
\]

and

\[
e:=z+z^{-1}
=2-\frac{\psi^2}{r^2}+O(r^{-4}).
\tag{3.2}
\]

Write the top squared branch as

\[
y=8-\frac{G_r(\psi)}{r^2}.
\tag{3.3}
\]

Near the endpoint the exact two-phase characteristic equation lies in the elliptic regime. Put

\[
h=g-\mu,
\qquad
h=2-2\cos\theta,
\qquad
x=r\theta.
\]

The Chebyshev factors are

\[
u=\frac{\sin((r-1)\theta)}{\sin\theta},
\qquad
w=\frac{\sin((r-2)\theta)}{\sin\theta}.
\]

Uniformly for `x` and `psi` in fixed compact sets,

\[
\frac ur=\frac{\sin x}{x}+O(r^{-1}),
\qquad
\frac wr=\frac{\sin x}{x}+O(r^{-1}),
\tag{3.4}
\]

with the expansions valid after two derivatives in the rescaled variables as well.

Substituting (3.1)--(3.4) into the exact characteristic equation gives

\[
P=34-2-36\sin^2x+O(r^{-1})
=32-36\sin^2x+O(r^{-1}),
\tag{3.5}
\]

locally uniformly in `C^2`.

The limiting root is therefore

\[
x=x_0=\arccos(1/3),
\]

and the relation

\[
g=\mu+2-2\cos\theta
\]

gives the rescaled local gap law

\[
\boxed{
G_r(\psi)
=x_0^2+n^2\psi^2+O(r^{-1})}
\tag{3.6}
\]

locally uniformly in `C^2` on every fixed compact `psi` interval.

The `C^2` form follows directly by differentiating the exact two-phase equation: at the limiting root,

\[
\frac{d}{dx}(32-36\sin^2x)
=-72\sin x_0\cos x_0\ne0,
\]

so the implicit root remains simple and all differentiated Chebyshev expansions are uniform.

---

## 4. Strict local convexity

Differentiating (3.6) twice gives

\[
\boxed{
G_r''(\psi)=2n^2+O(r^{-1})}
\tag{4.1}
\]

uniformly for `|psi|<=Psi`.

Thus, for all sufficiently large `r`,

\[
G_r''(\psi)>n^2>0
\]

on a fixed neighborhood of the origin.

The Bloch spectrum is invariant under `phi -> -phi` by complex conjugation, so the top branch and its gap are even in `psi`. Therefore

\[
G_r'(0)=0.
\]

Strict convexity implies that

\[
\boxed{\psi=0}
\]

is the unique local minimizer of the gap in that neighborhood, equivalently `z=1` is the unique local maximizer of the squared spectral edge.

---

## 5. Local plus global gives exact dominance

By the global phase localization (2.2), every global maximizing phase has

\[
\psi=r\phi\to0.
\]

Hence, for all sufficiently large `L`, every global maximizer lies inside the fixed strictly convex neighborhood from Section 4. The only minimizer there is `psi=0`.

Therefore

\[
z=1
\]

is the unique global maximizing Bloch phase for all sufficiently large even `L`, proving (1.1)--(1.2).

Finally, substituting the endpoint expansion from `COMPRESSED_ENDPOINT_SHARP_GAP.md` proves (1.3).

---

## 6. Interpretation

There is a sharp contrast with the older even-jump period-`4s` family, whose maximizing phase develops a genuine `Theta(s^-2)` phase slip. For the compressed two-defect family, a fixed odd multiplier has the opposite behavior: the endpoint is eventually exactly stable.

Thus the arithmetic compression does more than shorten the period. It changes the boundary-layer mechanism itself:

\[
\boxed{
\text{compressed family: eventual endpoint locking},
\qquad
\text{old }4s\text{ family: phase slip}.}
\]

The remaining finite problem is to decide whether the numerically observed stronger statement

\[
L\ge6\Longrightarrow z=1\text{ globally maximizing for every odd multiplier}
\]

holds without the qualifier `L` sufficiently large and uniformly in `q`.
