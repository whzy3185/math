# First correction and phase rigidity for the compressed two-defect gap

Date: 2026-09-09

Status: **Proved**. This note refines `SHARP_COMPRESSED_GAP_ASYMPTOTIC.md`. It does not assume that the periodic Bloch phase is the exact finite-`L` maximizer.

Let `L>=6` be even, `q>=0`, and

\[
g_{L,q}=8-\max_{|z|=1}\rho(H_{L,q}(z))^2.
\]

Put

\[
a=\arccos(1/3),
\qquad
\Gamma_0=4a^2,
\qquad
\Gamma_1=\frac{16a^2}{3}.
\]

---

## Theorem A — first global correction

Uniformly in the odd multiplier `2q+1`,

\[
\boxed{
L^2g_{L,q}
=\Gamma_0+rac{\Gamma_1}{L}+o(L^{-1}).
}
\tag{A1}
\]

Equivalently,

\[
\boxed{
g_{L,q}
=\frac{4a^2}{L^2}
+\frac{16a^2}{3L^3}
+o(L^{-3}).}
\tag{A2}
\]

Thus the first correction to the sharp compressed constant is also attained asymptotically by the periodic Bloch phase.

---

## Theorem B — stronger maximizing-phase rigidity

Let `z_L=e^{it_L}` be any Bloch phase attaining the global edge and define

\[
d_L=2\cos((2q+1)t_L),
\qquad
e_L=2\cos t_L.
\]

Then, uniformly in `q`,

\[
\boxed{
L^3(2-d_L)\longrightarrow0,
\qquad
L(2-e_L)\longrightarrow0.
}
\tag{B1}
\]

In angular form,

\[
\operatorname{dist}((2q+1)t_L,2\pi\mathbb Z)
=o(L^{-3/2}),
\]

and

\[
\operatorname{dist}(t_L,2\pi\mathbb Z)
=o(L^{-1/2}).
\]

The first statement is the stronger arithmetic localization: the folded long-jump phase is forced to the periodic point at a scale much smaller than the spectral scale.

---

## 1. Endpoint expansion

At `z=1`, write `r=L/2` and let

\[
a_r=r\theta_r
\]

be the unique solution of

\[
3\cos a_r
+2\tan\left(\frac{a_r}{2r}\right)\sin a_r=1.
\tag{1.1}
\]

The implicit-function expansion gives

\[
\boxed{
a_r=a+\frac{a}{3r}+O(r^{-2}).}
\tag{1.2}
\]

Since the endpoint gap is

\[
e_L^{\rm end}=4\sin^2\left(\frac{a_r}{2r}\right),
\]

and `L=2r`,

\[
\boxed{
L^2e_L^{\rm end}
=4a^2+\frac{16a^2}{3L}+O(L^{-2}).}
\tag{1.3}
\]

Because the global gap is no larger than the endpoint gap,

\[
L^2g_{L,q}
\le\Gamma_0+\frac{\Gamma_1}{L}+O(L^{-2}).
\tag{1.4}
\]

---

## 2. Local normalized characteristic function

For a global maximizing phase define

\[
\gamma=L^2g_{L,q},
\qquad
D=L^2(2-d),
\qquad
E=2-e.
\tag{2.1}
\]

The sharp leading theorem already proves, uniformly in `q`,

\[
\gamma\to\Gamma_0,
\qquad
D\to0,
\qquad
E\to0.
\tag{2.2}
\]

Let

\[
h=L^{-1},
\qquad
\xi=\gamma-D,
\qquad
x=\frac{\sqrt\xi}{2}.
\]

Use the exact characteristic formula

\[
P(y,d,e)=u^2\mathcal A(y,d)+uw\mathcal B(y,d)+\mathcal C(y,d,e),
\]

with

\[
y=8-\gamma h^2,
\qquad
d=2-Dh^2,
\qquad
e=2-E.
\]

For `xi` in a fixed neighborhood of `Gamma_0`, the Chebyshev factors have the uniform expansions

\[
\boxed{
hu
=\frac{\sin x}{\sqrt\xi}-h\cos x+O(h^2+D h),}
\tag{2.3}
\]

\[
\boxed{
hw
=\frac{\sin x}{\sqrt\xi}-2h\cos x+O(h^2+D h).}
\tag{2.4}
\]

These follow from

\[
U_m(\cos\theta)=\frac{\sin((m+1)\theta)}{\sin\theta},
\qquad
m=\frac L2-2,
\]

and the local relation

\[
\theta=h\sqrt\xi+O(h^3+h^3D).
\]

The coefficient polynomials satisfy

\[
\frac{\mathcal A}{h^2}
=-84\gamma+60D+O(h^2),
\tag{2.5}
\]

\[
\frac{\mathcal B}{h^2}
=48\gamma-24D+O(h^2),
\tag{2.6}
\]

and

\[
\mathcal C=32+E+O(h^2).
\tag{2.7}
\]

Substitution gives the local normalized root equation

\[
\boxed{
0=
32+E
-36\sin^2\left(\frac{\sqrt{\gamma-D}}2\right)
+hG_0
+O\bigl(h^2+h(D+E)+D^2+E^2\bigr),}
\tag{2.8}
\]

where the first finite-size coefficient at the base point is

\[
\boxed{
G_0=\frac{32\sqrt2\,a}{3}.}
\tag{2.9}
\]

Indeed the `h`-term contributed by (2.3)--(2.6) at `D=0`, `gamma=Gamma_0` is

\[
24\sqrt{\Gamma_0}\sin a\cos a
=\frac{32\sqrt2\,a}{3}.
\]

All remainders are uniform in `q` because `q` enters the exact determinant only through the phase variables `d,e`.

---

## 3. A quantitative local implicit law

Define

\[
f(\xi)=32-36\sin^2(\sqrt\xi/2).
\]

At

\[
\xi=\Gamma_0=4a^2,
\]

we have `f(Gamma_0)=0` and

\[
\boxed{
f'(\Gamma_0)=-\frac{2\sqrt2}{a}<0.}
\tag{3.1}
\]

Therefore the implicit-function theorem applied to (2.8) gives, throughout a fixed neighborhood of the base point,

\[
\boxed{
\gamma
=\Gamma_0+D
+\frac{a}{2\sqrt2}E
+\frac{\Gamma_1}{L}
+O\left(L^{-2}+D^2+E^2+\frac{D+E}{L}\right).}
\tag{3.2}
\]

The value of the `1/L` coefficient follows from

\[
-\frac{G_0}{f'(\Gamma_0)}
=\frac{16a^2}{3}
=\Gamma_1.
\tag{3.3}
\]

This formula is the decisive refinement: both phase variables have nonnegative first-order cost.

---

## 4. Bootstrap of the phase variables

From the endpoint comparison (1.4) and the local law (3.2),

\[
D+\frac{a}{2\sqrt2}E
\le O(L^{-1})
+O(D^2+E^2).
\]

Since `D,E->0`, the quadratic terms can be absorbed for all sufficiently large `L`. Hence

\[
\boxed{D=O(L^{-1}),\qquad E=O(L^{-1}).}
\tag{4.1}
\]

Now take any subsequence such that

\[
L D\to\delta\ge0,
\qquad
L E\to\varepsilon\ge0,
\]

and

\[
L(\gamma-\Gamma_0)\to\kappa
\]

(after a further subsequence if necessary). Multiplying (3.2) by `L` gives

\[
\boxed{
\kappa
=\Gamma_1+\delta+rac{a}{2\sqrt2}\varepsilon.}
\tag{4.2}
\]

But the endpoint upper bound (1.4) gives

\[
\kappa\le\Gamma_1.
\]

Since `delta,epsilon>=0`, necessarily

\[
\boxed{
\delta=0,
\qquad
\varepsilon=0,
\qquad
\kappa=\Gamma_1.}
\tag{4.3}
\]

Every subsequence has the same limits. Therefore

\[
L D\to0,
\qquad
L E\to0,
\]

which is exactly (B1), and

\[
L(\gamma-\Gamma_0)\to\Gamma_1,
\]

which proves (A1)--(A2).

---

## 5. Interpretation

The leading scaled variational problem already penalizes the folded phase displacement by the additive cost `D`. The first finite-size correction preserves this boundary minimum: there is no phase-slip analogue at order `L^{-3}` for the compressed family.

This sharply contrasts with the older even period-`4s` family, where a nonzero Bloch phase produces a genuine correction at the next nontrivial scale. The two periodic mechanisms therefore differ not only in their leading constants but also in their phase-selection behavior.