# Exponentially accurate compressed-antiperiodic locking and high-order global gap

Date: 2026-09-14

Status: **Proved after hostile-audit correction**.

## Correction record

An earlier version of this note claimed exact physical locking at `z=-1` throughout the macroscopic `m>N` regime. That is true when the odd multiplier is one, but false for a general multiplier `n=2q+1>1`.

The correct statement is stronger in the sense relevant to the algebraic asymptotic theory and weaker only at an exponentially small scale:

- the global optimizer lies exponentially close to the **compressed antiperiodic well** `d=-2`;
- among the physical solutions of `z^n=-1`, the seam term selects the roots with largest `e=z+z^{-1}`, namely `z=exp(+- i pi/n)`;
- the actual optimizer is displaced from those roots by `O(Lambda^(-2N))` in compressed phase;
- consequently every algebraic `1/m` coefficient previously computed remains unchanged.

No theorem depending only on the displayed algebraic gap expansion is affected.

---

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and assume

\[
N,m\to\infty,
\qquad
1+\varepsilon\le\frac mN\le C
\tag{1.1}
\]

for fixed positive `epsilon,C`.

Let

\[
n=2q+1
\]

be the odd multiplier, allowed to vary arbitrarily, and define

\[
\Gamma_{N,m,q}
:=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

The two Bloch coordinates are

\[
d=z^n+z^{-n},
\qquad
e=z+z^{-1}.
\]

The macroscopic full-Bloch theorem forces every maximizing phase into the well

\[
d\to-2.
\]

Put

\[
\Lambda=3+2\sqrt2.
\]

---

## Theorem A — exponential compressed-antiperiodic localization

For every global maximizing phase `z_*`, choose a root

\[
z_0^n=-1
\]

nearest to `z_*`, and write the compressed displacement as

\[
z_*=z_0\exp(i\delta/n).
\]

Then, uniformly under (1.1) and uniformly in the odd multiplier,

\[
\boxed{
|\delta|=O(\Lambda^{-2N}).
}
\tag{1.2}

Moreover, among the exact compressed-antiperiodic roots `z_0^n=-1`, the ones with largest physical seam coordinate are

\[
\boxed{
z_0=e^{\pm i\pi/n},}
\tag{1.3}

and every global optimizer is exponentially close to one of these two conjugate roots.

For `n=1`, (1.3) reduces to the genuine physical antiperiodic point `z=-1`.

Thus the correct finite statement is **exponential locking to the compressed antiperiodic well**, not exact locking to physical `z=-1` for arbitrary odd multiplier.

---

## Theorem B — algebraic global gap expansion is unchanged

Let

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

Then

\[
\boxed{
\Gamma_{N,m,q}
=e^-_{N,m}+O(\Lambda^{-2N})
}
\tag{1.4}

uniformly under (1.1) and uniformly in the odd multiplier.

Consequently, to every algebraic order in `1/m`,

\[
\boxed{
\Gamma_{N,m,q}\sim A(m),
}
\tag{1.5}

where `A` is the universal Robin series from `ALL_ORDERS_MACROSCOPIC_ROBIN_EXPANSION.md`.

In particular,

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}
+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7})+O(\Lambda^{-2N}).
\end{aligned}}
\tag{1.6}

The polynomial coefficients remain independent of the odd multiplier.

---

## 2. Physical geometry of the compressed antiperiodic set

Write

\[
z=e^{i\phi}.
\]

The condition `d=-2` is

\[
n\phi=(2j+1)\pi
\quad(\bmod 2\pi),
\]

so the physical roots are

\[
z_j=e^{i(2j+1)\pi/n}.
\]

At fixed `d=-2`, the characteristic equation has the form

\[
P(y;-2,e)=G(y,-2)-e.
\]

Hence larger `e` favors a larger squared spectral root. Among the `n` roots of `z^n=-1`, the maximal value of

\[
e=2\cos\phi
\]

is

\[
\boxed{e_*=2\cos(\pi/n),}
\]

attained exactly at the conjugate pair (1.3).

This already explains why physical `z=-1` is not the finite optimizer when `n>1`.

---

## 3. Local expansion including the seam term

Fix the root

\[
z_0=e^{i\pi/n}
\]

and parameterize

\[
z=z_0e^{i\delta/n}.
\]

Then

\[
d=2\cos(\pi+\delta)
=-2+\delta^2+O(\delta^4),
\tag{3.1}
\]

whereas

\[
\begin{aligned}
e
&=2\cos\frac{\pi+\delta}{n}\\
&=2\cos\frac\pi n
-\frac{2}{n}\sin\frac\pi n\,\delta
-\frac{1}{n^2}\cos\frac\pi n\,\delta^2
+O(\delta^3/n^3).
\end{aligned}
\tag{3.2}

The first term in (3.2) is the seam value at the compressed endpoint; the linear term is the finite physical-seam force missed by the earlier exact-locking claim.

Now divide the exact transfer determinant by the square of the expanding generic hard-channel factor. At the first defect-soft root, the normalized root equation is simple. The hard factor has size

\[
\Theta(\Lambda^N),
\]

so differentiation of the *unnormalized* characteristic polynomial gives

\[
\boxed{
|\partial_y P|
\ge c\Lambda^{2N}
}
\tag{3.3}

for a constant `c>0` uniform on the macroscopic ratio range. Since

\[
\partial_eP=-1,
\]

the change of the squared root caused directly by the seam coordinate is therefore

\[
O(\Lambda^{-2N}|e-e_*|).
\tag{3.4}

By contrast, changing `d+2` changes the normalized soft mass at order one. Thus the local gap has the form

\[
\boxed{
 g(\delta)
=g(0)+\kappa_{N,m}\delta^2
+\Lambda^{-2N}\bigl(\beta_{n,N,m}\delta+O(\delta^2)\bigr)
+O(\delta^4),
}
\tag{3.5}

with

\[
\kappa_{N,m}=1+O(m^{-1})+O(\Lambda^{-2N})
\]

and uniformly bounded `beta_{n,N,m}`.  The bound is uniform in `n` because

\[
\frac1n\sin\frac\pi n\le1.
\]

In particular `kappa>1/2` for all sufficiently large parameters.

---

## 4. Exponentially small optimizing displacement

Differentiate (3.5):

\[
2\kappa_{N,m}\delta
+O(\delta^3)
+O(\Lambda^{-2N})=0.
\]

The unique local minimizer therefore satisfies

\[
\boxed{
\delta_*=O(\Lambda^{-2N}),
}
\]

which proves (1.2).

Substituting back into (3.5), the gain from the seam-induced displacement is actually `O(Lambda^(-4N))` relative to the best exact `d=-2` root. The difference between that root and the physical `z=-1` endpoint is `O(Lambda^(-2N))` by (3.4). Hence (1.4) follows.

---

## 5. Global localization

Because `m/N` stays uniformly above one, the periodic well has leading gap

\[
\frac{\pi^2}{4N^2},
\]

whereas the compressed-antiperiodic well has leading gap

\[
\frac{\pi^2}{4m^2}.
\]

The latter is strictly smaller by a fixed relative amount. `MACROSCOPIC_FULL_BLOCH_GAP_LAW.md` therefore localizes every global maximizing phase to the `d=-2` well.

Inside that well, (3.5) is strictly convex after the exponentially small seam perturbation. Hence its unique minimizer is the exponentially shifted point from Section 4. This proves the global localization statement.

---

## 6. Corrected asymmetric two-well picture

The macroscopic transition is still asymmetric, but the correct finite interpretation is:

- `N>m`: periodic well has an **algebraic** avoided-crossing phase slip of order `N^-2` in compressed phase;
- `N=m`: the same periodic cusp resolves the balanced degeneracy;
- `m>N`: the compressed-antiperiodic well is analytic; the physical seam induces only an **exponentially small** phase displacement of order `Lambda^(-2N)`.

Thus all algebraic orientation asymmetry stated in the high-order phase diagram remains valid. What is retracted is only the stronger finite claim of exact physical `z=-1` locking for arbitrary odd multiplier.
