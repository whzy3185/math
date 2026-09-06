# Sharp `pi^2` asymptotic at the phase-zero endpoint

Date: 2026-09-06.

This note proves the sharp leading constant at the endpoint `h=2`.  It does
**not** yet prove the same limit for the global Bloch gap, because
`PHASE_SLIP_COUNTEREXAMPLE.md` shows that the optimizing phase is not always
exactly zero.

For `s=2r`, define the endpoint squared gap

\[
 e_r:=8-\rho(H_s(1))^2.
\]

## Theorem EP

As `r -> infinity`,

\[
 \boxed{4r^2e_r\to\pi^2.}
 \tag{EP1}
\]

Equivalently, through even jumps,

\[
 \boxed{s^2\bigl(8-\rho(H_s(1))^2\bigr)\to\pi^2.}
 \tag{EP2}
\]

Since the global Bloch gap `g_s=8-R_s` satisfies `g_s<=e_{s/2}`, this already
improves the global asymptotic upper bound to

\[
 \limsup_{s\to\infty,\ s\text{ even}} s^2g_s\le\pi^2.
 \tag{EP3}
\]

Together with `QUADRATIC_GAP_THEOREM.md`,

\[
 \frac16\le\liminf s^2g_s\le\limsup s^2g_s\le\pi^2.
\]

## 1. Soft and hard channels at `h=2`

Write

\[
 e_r=2-2\cos\theta_r=4\sin^2(\theta_r/2),
 \qquad 0<\theta_r<\pi.
 \tag{1}
\]

At the endpoint `h=2`, the two continuant arguments at
`y=8-e_r` are

\[
 d_-=2-e_r=2\cos\theta_r,
 \qquad
 d_+=6-e_r=4+2\cos\theta_r.
\]

Introduce `eta_r>0` by

\[
 2\cosh\eta_r=6-e_r.
\]

Then

\[
 A_j:=D_j(d_-)=\frac{\sin((j+1)\theta_r)}{\sin\theta_r},
 \qquad
 B_j:=D_j(d_+)=\frac{\sinh((j+1)\eta_r)}{\sinh\eta_r}.
 \tag{2}
\]

Let

\[
 \lambda=3+2\sqrt2=e^{\eta_0},
 \qquad 2\cosh\eta_0=6.
\]

The compact determinant identity at `h=2` is

\[
 q_r(y,2)=S_r(y,2)^2-16D_{r-1}(y-6)^2-4.
 \tag{3}
\]

At the endpoint top root `y=8-e_r`, equation (3) gives

\[
 \left|S_r(8-e_r,2)\right|=\sqrt{16A_{r-1}^2+4}.
 \tag{4}
\]

Using

\[
 S_r=A_rB_r-6A_{r-1}B_{r-1}+A_{r-2}B_{r-2},
\]

divide (4) by `B_r` and set

\[
 \beta_r=\frac{B_{r-1}}{B_r},
 \qquad
 \gamma_r=\frac{B_{r-2}}{B_r},
 \qquad
 \delta_r=\frac{\sqrt{16A_{r-1}^2+4}}{B_r}.
\]

Then

\[
 A_r-6\beta_rA_{r-1}+\gamma_rA_{r-2}=\pm\delta_r.
 \tag{5}
\]

Multiplication by `sin(theta_r)` yields

\[
 \sin((r+1)\theta_r)
 -6\beta_r\sin(r\theta_r)
 +\gamma_r\sin((r-1)\theta_r)
 =\pm\delta_r\sin\theta_r.
 \tag{6}
\]

## 2. The endpoint angle is of order `1/r`

The uniform quadratic lower gap from `QUADRATIC_GAP_THEOREM.md` gives

\[
 e_r\ge\frac1{24r(r+1)}.
 \tag{7}
\]

Since `e_r=4 sin^2(theta_r/2)<=theta_r^2`,

\[
 r\theta_r\ge c>0
\]

for all sufficiently large `r`.

On the other hand, the old endpoint Rayleigh bound gives

\[
 e_r\le4\sin^2\frac\pi{2r+2}.
\]

Because `0<theta_r<pi` and `sin` is increasing on the relevant small
interval,

\[
 \theta_r\le\frac\pi{r+1}.
 \tag{8}
\]

Hence `x_r:=r theta_r` stays in a compact subinterval of `(0,pi]`.
Every subsequence therefore has a further subsequence with

\[
 x_r\to x,\qquad 0<x\le\pi.
 \tag{9}
\]

Also `theta_r->0` and `e_r=O(r^-2)`.

## 3. Hard-channel ratios

Because `e_r->0`,

\[
 \eta_r\to\eta_0.
\]

From the hyperbolic representation in (2),

\[
 \beta_r
 =\frac{\sinh(r\eta_r)}{\sinh((r+1)\eta_r)}
 =e^{-\eta_r}+O(e^{-2r\eta_r}),
\]

and similarly

\[
 \gamma_r=e^{-2\eta_r}+O(e^{-2r\eta_r}).
\]

Since `eta` is a smooth function of `e` near zero,

\[
 \eta_r-\eta_0=O(e_r)=O(\theta_r^2).
\]

Therefore

\[
 \boxed{
 \beta_r=\lambda^{-1}+O(\theta_r^2)+O(e^{-cr}),
 \qquad
 \gamma_r=\lambda^{-2}+O(\theta_r^2)+O(e^{-cr}).
 }
 \tag{10}
\]

for some absolute `c>0`.

The right side of (6) is negligible.  Indeed, (7) implies
`sin(theta_r)^{-1}=O(r)`, so `|A_{r-1}|=O(r)`, while `B_r` grows
exponentially because `eta_r` stays bounded away from zero.  Thus

\[
 \delta_r\to0.
 \tag{11}
\]

## 4. Limiting Robin equation

Use

\[
 6\lambda^{-1}=1+\lambda^{-2}.
 \tag{12}
\]

Replace `beta_r,gamma_r` in (6) by their limits from (10), move the error to
the right, and divide by `theta_r`.  The coefficient errors contribute
`O(theta_r)` after division, hence vanish.  By (11), so does the normalized
right side.

The leading expression is

\[
 \frac{\sin((r+1)\theta_r)-\sin(r\theta_r)}{\theta_r}
 -\lambda^{-2}
 \frac{\sin(r\theta_r)-\sin((r-1)\theta_r)}{\theta_r}.
 \tag{13}
\]

Using the sine-difference identity,

\[
 (13)=
 \frac{2\sin(\theta_r/2)}{\theta_r}
 \left[
 \cos\frac{(2r+1)\theta_r}{2}
 -\lambda^{-2}\cos\frac{(2r-1)\theta_r}{2}
 \right].
\]

Along the subsequence (9), this tends to

\[
 (1-\lambda^{-2})\cos x.
\]

Equation (6) therefore forces

\[
 \cos x=0.
\]

Because `0<x<=pi`,

\[
 x=\frac\pi2.
\]

Every convergent subsequence of `x_r` has the same limit, so

\[
 \boxed{r\theta_r\to\frac\pi2.}
 \tag{14}
\]

This is the limiting Dirichlet--Robin (asymptotically Neumann) condition in
the soft channel.

## 5. Recovering the gap constant

Finally,

\[
 4r^2e_r
 =16r^2\sin^2(\theta_r/2)
 =4(r\theta_r)^2
   \left(\frac{\sin(\theta_r/2)}{\theta_r/2}\right)^2.
\]

Using (14) and `theta_r->0` gives

\[
 4r^2e_r\to4\left(\frac\pi2\right)^2=\pi^2.
\]

This proves Theorem EP.

## 6. What remains for the global sharp limit

The exact phase-slip certificate shows that `e_r` is not always equal to the
global gap `g_{2r}`.  To upgrade (EP3) to

\[
 4r^2g_{2r}\to\pi^2,
\]

it is enough to prove that any phase improvement is `o(r^-2)`.  Numerical
experiments suggest a much stronger statement: the optimizing square-root
phase is `Theta(r^-2)`, so `t=4-h^2=Theta(r^-4)`, and the endpoint/global gap
difference is of order `r^-4` or smaller.  That boundary-layer estimate is
the next analytic target.
