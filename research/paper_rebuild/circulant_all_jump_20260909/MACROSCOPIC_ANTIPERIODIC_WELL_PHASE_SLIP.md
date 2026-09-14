# Universal phase slip in the macroscopic antiperiodic-well regime

Date: 2026-09-14

Status: **Proved**. This is the dual counterpart of `MACROSCOPIC_PERIODIC_WELL_PHASE_SLIP.md`.

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

with arbitrary varying odd multiplier. Write

\[
z=e^{i\phi},\qquad \psi=(2q+1)\phi.
\]

Near the antiperiodic compressed endpoint write

\[
\psi=\pi+\delta,
\qquad
\mu:=2+2\cos\psi=2-2\cos\delta.
\tag{1.2}
\]

Let

\[
\Gamma_{N,m,q}:=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2
\]

and

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

Because `m/N -> gamma>1`, the exact macroscopic full-Bloch theorem gives

\[
\Gamma_{N,m,q}\sim\frac{\pi^2}{4m^2},
\qquad
 e^-_{N,m}\sim\frac{\pi^2}{4m^2},
\]

while the periodic well is separated at leading order by the shorter soft length `N`.

## Theorem A — local antiperiodic effective law

Let

\[
\delta=\frac\zeta{m^2},\qquad \zeta=O(1),
\]

and let `g^-_{N,m}(delta)` denote the lower top soft branch near the antiperiodic endpoint. Then locally uniformly for bounded `zeta`,

\[
\boxed{
m^4\bigl(g^-_{N,m}(\zeta/m^2)-e^-_{N,m}\bigr)
=\zeta^2-\frac\pi{2\sqrt2}|\zeta|+o(1).
}
\tag{1.3}
\]

The limiting law is independent of `gamma` and of the odd multiplier.

## Theorem B — global antiperiodic phase slip

Choose a global maximizing Bloch phase and choose its compressed representative nearest `pi`. Then

\[
\boxed{
m^2|\delta_{N,m,q}|
\longrightarrow\frac\pi{4\sqrt2}.
}
\tag{1.4}
\]

Moreover

\[
\boxed{
m^4\bigl(e^-_{N,m}-\Gamma_{N,m,q}\bigr)
\longrightarrow\frac{\pi^2}{32}.
}
\tag{1.5}
\]

Thus in the whole macroscopic regime `m>N`, the global edge is asymptotically locked to the antiperiodic well, but the true maximizing phase is shifted from the endpoint by a universal algebraic phase slip of order `m^-2`.

---

## 2. Antiperiodic soft coordinate

Put

\[
g-\mu=2-2\cos\vartheta,
\qquad
y=m\vartheta,
\]

where the soft channel is now the defect arc. At `delta=0`, let `y^0_{N,m}` be the endpoint soft coordinate. The antiperiodic Dirichlet theorem and the universal cubic correction give

\[
y^0_{N,m}\to\frac\pi2.
\tag{2.1}
\]

The opposite generic arc is hyperbolic. Since `N->infinity`, its stable transfer ratio tends to

\[
\Lambda^{-1}=3-2\sqrt2,
\qquad \Lambda=3+2\sqrt2.
\tag{2.2}
\]

This is exactly the same hard-channel ratio appearing in the periodic-well analysis.

---

## 3. Boundary-layer bootstrap

Subtract the exact antiperiodic hard-divided transfer equation at `(g,mu,y)` from the endpoint equation at `(e^-,0,y^0)`.

The derivative with respect to the soft coordinate stays uniformly nonzero and tends to

\[
-(1-\Lambda^{-2}).
\]

The hard-ratio perturbation is

\[
O(|g-e^-|+\mu),
\]

while the phase-induced soft-pair splitting is

\[
O(\sqrt\mu).
\]

Hence

\[
|y-y^0|
\le C\bigl(\sqrt\mu+|g-e^-|+\mu+e^{-cN}\bigr).
\tag{3.1}
\]

At a globally improving phase, `g<=e^-`. Using

\[
g-e^-=
\mu+
\left(2-2\cos\frac ym\right)
-
\left(2-2\cos\frac{y^0}m\right),
\tag{3.2}
\]

we obtain exactly as in the periodic well

\[
\boxed{
\mu=O(m^{-4}),
\quad |y-y^0|=O(m^{-2}),
\quad |g-e^-|=O(m^{-4}).
}
\tag{3.3}
\]

Therefore

\[
\boxed{|\delta|=O(m^{-2}).}
\tag{3.4}
\]

---

## 4. Universal cusp displacement

Take

\[
\delta=\frac\zeta{m^2}.
\]

Then

\[
m^2\sqrt\mu\to|\zeta|,
\qquad m^4\mu\to\zeta^2.
\tag{4.1}
\]

After normalization by the dominant generic hard transfer factor, the soft-pair splitting is

\[
2\Lambda^{-1}\sqrt\mu+o(m^{-2}).
\]

Hence the improving branch satisfies

\[
-(1-\Lambda^{-2})(y-y^0)
=2\Lambda^{-1}\sqrt\mu+o(m^{-2}).
\]

Since

\[
\frac{2\Lambda^{-1}}{1-\Lambda^{-2}}=\frac1{2\sqrt2},
\]

we get

\[
\boxed{
m^2(y-y^0)
\longrightarrow-rac{|\zeta|}{2\sqrt2}.
}
\tag{4.2}
\]

---

## 5. Effective parabola and global identification

From (3.2), (4.1), (4.2), and `y^0->pi/2`,

\[
\begin{aligned}
m^4\left[
2-2\cos\frac ym-
\left(2-2\cos\frac{y^0}m\right)
\right]
&\longrightarrow
2\left(\frac\pi2\right)
\left(-\frac{|\zeta|}{2\sqrt2}\right)\\
&=-\frac\pi{2\sqrt2}|\zeta|.
\end{aligned}
\]

Together with the phase cost `m^4 mu -> zeta^2`, this proves (1.3).

The limiting potential

\[
V(\zeta)=\zeta^2-\frac\pi{2\sqrt2}|\zeta|
\]

has minimizers

\[
\zeta=\pm\frac\pi{4\sqrt2}
\]

and minimum `-pi^2/32`.

Since `gamma>1`, the macroscopic two-well law separates the antiperiodic well from the periodic well at order `m^-2`; therefore every global maximizer lies in the antiperiodic boundary layer for all sufficiently large parameters. The same subsequence/minimizer argument used in the periodic-well theorem yields (1.4)--(1.5).

## 6. Consequence

Combining the periodic and antiperiodic phase-slip theorems gives a completely symmetric macroscopic statement. If

\[
\ell:=\max\{N,m\},
\]

and the two arc lengths are asymptotically unequal, then the global maximizing phase lies near the Bloch endpoint associated with the longer soft arc and

\[
\boxed{
\ell^2|\delta|\to\frac\pi{4\sqrt2},
\qquad
\ell^4(e_{\rm dom}-\Gamma)\to\frac{\pi^2}{32}.
}
\]

The constants are the same on both sides of the balanced transition.