# Compressed-antiperiodic localization and high-order global gap

Date: 2026-09-14

Status: **Proved after hostile-audit correction**.

This note records the corrected `m>N` picture.  The authoritative beyond-all-orders calculation is `ANTIPERIODIC_SEAM_TUNNELING_ASYMPTOTIC.md`.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and assume

\[
N,m\to\infty,
\qquad
1+\varepsilon\le m/N\le C.
\]

Let

\[
n=2q+1
\]

be the compatible odd multiplier and

\[
\Gamma_{N,m,q}=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

Put

\[
U_N:=U_{N-1}(3),
\qquad
\Lambda=3+2\sqrt2.
\]

Then

\[
U_N=\Theta(\Lambda^N).
\]

The globally selected well is the compressed-antiperiodic one

\[
d=z^n+z^{-n}\approx-2.
\]

---

## Theorem A — correct physical phase localization

The exact compressed-antiperiodic set is

\[
z^n=-1.
\]

Among those roots, the physical seam coordinate

\[
e=z+z^{-1}
\]

is maximal at

\[
\boxed{z_0=e^{\pm i\pi/n}.}
\]

Write a nearby phase as

\[
z=z_0e^{i\delta/n}.
\]

Then every global maximizing phase satisfies

\[
\boxed{
\delta_*
=-
\frac{\pi^2\sin(\pi/n)}
{64\sqrt2\,n\,U_Nm^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\tag{1.1}

In particular

\[
\boxed{
|\delta_*|=O(U_N^{-1}m^{-3})
=O(\Lambda^{-N}m^{-3}).
}
\tag{1.2}

For `n=1`, the coefficient in (1.1) vanishes and the selected physical phase is exactly `z=-1` by symmetry.

Thus the correct statement is **compressed-antiperiodic locking with an exponentially small physical-seam displacement**, not exact physical `z=-1` locking for arbitrary odd multiplier.

---

## Theorem B — first beyond-all-orders gap correction

Let

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

Then

\[
\boxed{
 e^-_{N,m}-\Gamma_{N,m,q}
=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_Nm^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\tag{2.1}

Equivalently,

\[
 e^-_{N,m}-\Gamma_{N,m,q}
=
\frac{4\cos^2(\pi/(2n))\pi^2}
{64\sqrt2\,U_Nm^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
\tag{2.2}

This is the first place where the odd multiplier enters the spectral gap.

The extra gain caused by shifting away from the best exact `d=-2` root is only

\[
O(U_N^{-2}m^{-6}).
\]

---

## Theorem C — algebraic global expansion

Because the correction (2.1) is smaller than every power of `1/m`, the full algebraic expansion is still the universal endpoint Robin series:

\[
\boxed{
\Gamma_{N,m,q}\sim A(m).
}
\tag{3.1}

In particular,

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}
+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7})\\
&-
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_Nm^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
\end{aligned}}
\tag{3.2}

The first line is independent of `n`; the final exponentially small term carries the physical-seam dependence.

---

## 2. Why the scale is `U_N^{-1}m^{-3}`

At `d=-2`, the all-energy single-square identity is

\[
P(y;-2,e)=4(Z^2-1-4p^2)+(2-e).
\]

At the convenient `z=-1` endpoint the top root satisfies

\[
Z=2p.
\]

Writing the soft root as

\[
y=6+2\cos\theta,
\qquad m\theta\to\frac\pi2,
\]

the hard transfer contributes

\[
u=U_{N-1}(2+\cos\theta)
=U_N(1+O(m^{-1})).
\]

The derivative of the reduced root equation obeys

\[
\boxed{
\frac d{dy}(Z^2-4p^2)
=
\frac{16\sqrt2}{\pi^2}U_Nm^3
\left(1+O(m^{-1})\right).
}
\]

Since changing the seam coordinate changes the characteristic equation by exactly `-e`, the root response is therefore of order

\[
U_N^{-1}m^{-3},
\]

which proves the scale in Theorem B.

The detailed coefficient computation and the minimization in compressed phase are carried out in `ANTIPERIODIC_SEAM_TUNNELING_ASYMPTOTIC.md`.

---

## 3. Correct asymmetric two-well picture

The macroscopic orientation transition is:

- `N>m`: periodic well, with an algebraic avoided-crossing phase slip of order `N^-2` in compressed phase;
- `N=m`: the same periodic cusp resolves the balanced endpoint degeneracy;
- `m>N`: compressed-antiperiodic analytic well, with physical-seam displacement only of order `U_N^-1 m^-3`.

Thus the algebraic orientation asymmetry is exactly as in the previously proved phase diagram.  The finite odd-multiplier dependence lives one transseries level lower, at the hard-channel tunneling scale.