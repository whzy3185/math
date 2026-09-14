# Second-order phase slip for the balanced two-defect geometry

Date: 2026-09-10; corrected 2026-09-14 after hostile audit.

Status: **Proved**.

## 1. Balanced geometry

Let

\[
N=m=r\to\infty,
\qquad L=4r,
\qquad h=2r.
\]

The primitive coefficient period is `8r`. Let

\[
s=L(2q+1)
\]

with arbitrary odd multiplier and write

\[
z=e^{i\phi},\qquad \psi=(2q+1)\phi.
\]

Let

\[
\Gamma_r:=8-\max_{|z|=1}\rho(H(z))^2,
\]

\[
e_r^+:=8-\rho(H(1))^2,
\qquad
e_r^-:=8-\rho(H(-1))^2.
\]

The two endpoint gaps agree to every algebraic order and differ only by exponentially small tunneling:

\[
e_r^+-e_r^-=O(\Lambda^{-r}),
\qquad \Lambda=3+2\sqrt2.
\tag{1.1}
\]

However, their **local phase structures are different**:

- the periodic endpoint `d=2` contains an exponentially split soft pair and develops a `|delta|` cusp;
- the antiperiodic endpoint `d=-2` has a simple analytic top soft root and is locally locked.

Thus the global algebraic improvement comes from the periodic well.

## Theorem A — balanced periodic-well phase slip

Let `delta_r` be the compressed displacement of a global maximizing phase from the periodic endpoint,

\[
\psi_r=\delta_r
\quad\text{mod }2\pi,
\qquad \delta_r\in[-\pi,\pi].
\]

Then

\[
\boxed{
r^2|\delta_r|
\longrightarrow\frac\pi{4\sqrt2}.
}
\tag{1.2}
\]

Moreover, with

\[
e_r:=\min\{e_r^+,e_r^-\},
\]

\[
\boxed{
r^4(e_r-\Gamma_r)
\longrightarrow\frac{\pi^2}{32}.
}
\tag{1.3}
\]

Since `e_r^+-e_r^-` is exponentially small, either endpoint gap may be used as the algebraic reference value in (1.3), but the **phase-slip mechanism itself is periodic-side only**.

---

## 2. Periodic boundary layer

Near `d=2`, put

\[
\mu=2-d=2-2\cos\delta\ge0.
\]

Let `g` denote the local squared gap and define the periodic soft angle by

\[
g-\mu=2-2\cos\theta,
\qquad x=r\theta.
\]

At the endpoint let `x_r^0` satisfy

\[
e_r^+=2-2\cos(x_r^0/r),
\qquad x_r^0\to\frac\pi2.
\]

Subtracting the endpoint transfer equation from the phase-shifted one gives

\[
|x-x_r^0|
\le C\bigl(\sqrt\mu+|g-e_r^+|+\mu+\Lambda^{-r}\bigr).
\tag{2.1}
\]

Using

\[
g-e_r^+
=\mu+
\left(2-2\cos\frac xr\right)
-
\left(2-2\cos\frac{x_r^0}r\right)
\tag{2.2}
\]

and `g<=e_r^++o(r^-A)` at a globally improving phase gives

\[
\boxed{
\mu=O(r^{-4}),
\qquad |x-x_r^0|=O(r^{-2}),
\qquad |g-e_r^+|=O(r^{-4}).
}
\tag{2.3}
\]

Hence `|delta|=O(r^-2)`.

---

## 3. Cusp coefficient

Take

\[
\delta=\frac\zeta{r^2}.
\]

Then

\[
r^2\sqrt\mu\to|\zeta|,
\qquad r^4\mu\to\zeta^2.
\]

After hard-channel normalization the soft-pair splitting is

\[
2\Lambda^{-1}\sqrt\mu+o(r^{-2}),
\]

while the normalized soft derivative tends to

\[
-(1-\Lambda^{-2}).
\]

Therefore the improving branch satisfies

\[
\boxed{
r^2(x-x_r^0)
\longrightarrow-rac{|\zeta|}{2\sqrt2}.
}
\tag{3.1}
\]

The algebraic identity used here is

\[
\frac{2\Lambda^{-1}}{1-\Lambda^{-2}}=\frac1{2\sqrt2}.
\]

---

## 4. Effective parabola

From (2.2), (3.1), and `x_r^0->pi/2`,

\[
\boxed{
r^4\bigl(g_r(\zeta/r^2)-e_r^+\bigr)
=\zeta^2-rac\pi{2\sqrt2}|\zeta|+o(1).
}
\tag{4.1}
\]

The limiting potential

\[
V(\zeta)=\zeta^2-\frac\pi{2\sqrt2}|\zeta|
\]

has minimizers

\[
\boxed{\zeta=\pm\frac\pi{4\sqrt2}}
\]

and minimum

\[
\boxed{-\frac{\pi^2}{32}}.
\]

This proves (1.2)--(1.3).

## 5. Antiperiodic endpoint audit

Near `d=-2`, write the compressed displacement from `pi` as `delta`. The top soft root is simple and the local characteristic function is analytic and even in `delta`. Its gap satisfies

\[
g^-(\delta)-e_r^-
=\bigl(1+O(r^{-1})\bigr)\delta^2+O(\delta^4).
\tag{5.1}
\]

There is no `|delta|` term. Hence `z=-1` is a strict local maximizer of the squared edge, but it is beaten globally by the `Theta(r^-4)` periodic-well cusp improvement.

## 6. Higher-order refinement

The corrected higher-order coefficients are proved in `HIGH_ORDER_MACROSCOPIC_PHASE_SLIP.md`:

\[
|\delta_r|
=\frac\pi{4\sqrt2 r^2}
-\frac\pi{8r^3}
+\frac{\pi(32-27\sqrt2)}{192r^4}
+O(r^{-5}),
\]

and

\[
e_r-\Gamma_r
=\frac{\pi^2}{32r^4}
-\frac{3\pi^2}{32\sqrt2 r^5}
+\frac{\pi^2(32\sqrt2-3)}{768r^6}
+O(r^{-7}).
\]

The balanced picture is therefore asymmetric beyond the endpoint gap values: periodic cusp versus antiperiodic exact locking.