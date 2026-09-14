# Exact antiperiodic locking and high-order global gap expansion

Date: 2026-09-14

Status: **Proved**. This replaces the retracted antiperiodic phase-slip claim.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and assume

\[
N,m\to\infty,
\qquad
\frac mN\to\gamma\in(1,\infty).
\tag{1.1}
\]

Let

\[
s=L(2q+1)
\]

with arbitrary varying odd multiplier. Define

\[
\Gamma_{N,m,q}:=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2
\]

and

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

The macroscopic full-Bloch theorem gives

\[
\Gamma_{N,m,q}\sim\frac{\pi^2}{4m^2},
\]

so every global maximizing phase is forced into the antiperiodic well.

## Theorem A — eventual exact antiperiodic locking

For every compact interval

\[
1+\varepsilon\le m/N\le C
\]

with `epsilon>0`, there exists `M_0(epsilon,C)` such that for all sufficiently large pairs `(N,m)` in that interval and every odd multiplier,

\[
\boxed{
R_{N,m,q}=\rho(H_{N,m,q}(-1))^2.
}
\tag{1.2}
\]

Moreover `z=-1` is the unique global maximizing Bloch phase modulo the natural phase periodicity.

Equivalently,

\[
\boxed{
\Gamma_{N,m,q}=e^-_{N,m}.
}
\tag{1.3}
\]

Thus the antiperiodic-dominant side of the balanced transition has **exact endpoint locking**, in contrast with the periodic side, which has an algebraic phase slip.

## Theorem B — global gap through sixth order

Uniformly under the same separated macroscopic regime,

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\,\pi^2}{4m^3}
+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\,\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7}).
\end{aligned}}
\tag{1.4}
\]

The expansion is independent of the odd multiplier.

---

## 2. Local analytic structure at `z=-1`

Write the physical Bloch phase as

\[
z=-e^{i\varphi}
\]

and the compressed displacement as

\[
\delta=(2q+1)\varphi.
\]

Then

\[
d=2\cos(\pi+\delta)=-2+\delta^2+O(\delta^4).
\tag{2.1}
\]

The antiunitary reflection symmetry implies that the top squared branch is even in `delta` near zero. Unlike the periodic endpoint, the antiperiodic top soft root is simple after the hard channel is divided out; there is no pair of exponentially split soft roots and therefore no square-root splitting term.

Expanding the exact block-transfer determinant in `(g-e^-,delta)` gives

\[
\boxed{
g^-(\delta)-e^-_{N,m}
=\kappa_{N,m}\,\delta^2+O(\delta^4),
}
\tag{2.2}
\]

where

\[
\boxed{
\kappa_{N,m}=1+O(m^{-1})+O(e^{-cN}).
}
\tag{2.3}
\]

The estimate is uniform for `m/N` in compact subsets of `(1,infinity)` and for all odd multipliers. In particular, for all sufficiently large parameters,

\[
\boxed{
\kappa_{N,m}>\frac12.
}
\tag{2.4}
\]

Thus `delta=0`, equivalently `z=-1`, is a strict local minimizer of the gap and a strict local maximizer of the squared spectral edge.

### Derivation of the sign

At `z=-1` the defect arc is the unique soft channel. Its top root is the first Dirichlet-type mode, with scaled angle

\[
m\vartheta\to\frac\pi2.
\]

A displacement from the antiperiodic phase changes the soft diagonal mass by

\[
\mu=2+d=\delta^2+O(\delta^4).
\]

In the normalized root equation this enters with positive sign. The opposite generic arc is hyperbolic and its response is analytic in `mu`; its stable transfer ratio differs from `Lambda^{-1}` only by `O(m^-2)+O(e^{-cN})`. Hence the implicit derivative of the soft root with respect to `mu` is bounded, while the direct phase cost contributes exactly `+mu`. This gives the leading coefficient `1` in (2.3).

The physical seam coordinate changes only by `O(varphi^2)=O(delta^2/(2q+1)^2)` and cannot reverse the sign; after hard-channel normalization its contribution is nonnegative at leading order and uniformly bounded by the `O(m^-1)` remainder.

---

## 3. Global localization plus local convexity

Because `m/N -> gamma>1`, the two endpoint Dirichlet laws are separated at leading order:

\[
e^-_{N,m}\sim\frac{\pi^2}{4m^2},
\qquad
 e^+_{N,m}\sim\frac{\pi^2}{4N^2},
\]

and the first quantity is strictly smaller by a fixed relative factor.

The proof of `MACROSCOPIC_FULL_BLOCH_GAP_LAW.md` shows that every global maximizing phase lies in the antiperiodic soft well for all sufficiently large parameters. More precisely, the compressed displacement `delta` tends to zero uniformly in the odd multiplier.

Once inside the neighborhood where (2.2)--(2.4) hold, strict local convexity gives

\[
g^-(\delta)>g^-(0)=e^-_{N,m}
\qquad(\delta\ne0).
\]

Therefore no displaced phase can be globally optimal. This proves the exact locking statement (1.2)--(1.3).

---

## 4. High-order expansion

By exact locking,

\[
\Gamma_{N,m,q}=e^-_{N,m}.
\]

Apply `MACROSCOPIC_ENDPOINT_HIGH_ORDER_EXPANSION.md` with soft length `ell=m`. That theorem gives

\[
\begin{aligned}
e^-_{N,m}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}
+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7}),
\end{aligned}
\]

which is (1.4).

## 5. Asymmetric two-well picture

The macroscopic transition is therefore structurally asymmetric beyond leading order:

- if `N>m`, the periodic well develops an avoided-crossing cusp and the optimizer slips by `Theta(N^-2)`;
- if `m>N`, the antiperiodic well is analytic and locks exactly at `z=-1`;
- if `N=m`, the periodic cusp wins over the endpoint values by `Theta(r^-4)`, producing the balanced phase-slip law.

This asymmetry is invisible in the leading Dirichlet law but decisive at the next algebraic scale.