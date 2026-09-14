# Universal Dirichlet upper bound for every endpoint soft channel

Date: 2026-09-14

Status: **Proved**. This note gives the finite, non-asymptotic endpoint estimate needed for the all-layer quarter-period optimization problem.

## 1. Setup

Write

\[
L=2(N+m),\qquad N,m\ge1,
\]

for an even-separation two-defect cell.  At the periodic Bloch endpoint `z=1`, the generic arc of length parameter `N` is the soft channel and the defect arc of length parameter `m` is hyperbolic.  Let

\[
e^+_{N,m}:=8-\rho(H_{N,m,q}(1))^2.
\]

At the antiperiodic endpoint `z=-1` the two roles are exchanged; write

\[
e^-_{N,m}:=8-\rho(H_{N,m,q}(-1))^2.
\]

Both endpoint spectra are independent of the odd multiplier `2q+1`.

## Theorem A — periodic endpoint Dirichlet upper bound

For every `N,m>=1`,

\[
\boxed{
0<e^+_{N,m}
<2-2\cos\frac{\pi}{2N}.
}
\tag{1.1}
\]

Equivalently the periodic endpoint has a squared eigenvalue strictly larger than

\[
6+2\cos\frac{\pi}{2N}.
\]

## Theorem B — antiperiodic endpoint Dirichlet upper bound

For every `N,m>=1` for which the antiperiodic endpoint is sub-eight,

\[
\boxed{
e^-_{N,m}
<2-2\cos\frac{\pi}{2m}.
}
\tag{1.2}
\]

(The same inequality remains a valid upper bound on the signed quantity `8-rho^2` when the endpoint is super-eight.)

Consequently, for the full Bloch gap

\[
\Gamma_{N,m,q}=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2,
\]

if

\[
M:=\max\{N,m\},
\]

then

\[
\boxed{
\Gamma_{N,m,q}
< D_M:=2-2\cos\frac{\pi}{2M}.
}
\tag{1.3}
\]

whenever the geometry is sub-eight; if it is super-eight the inequality is automatic because `Gamma<0<D_M`.

---

## 2. Exact periodic endpoint quantization

The exact periodic endpoint equation from the general even-separation transfer reduction is

\[
\begin{aligned}
&T_m(2+\cos\theta)
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}\\
&\qquad-
\bigl[U_m(2+\cos\theta)+U_{m-1}(2+\cos\theta)\bigr]
\tan(\theta/2)\sin(N\theta)
=1,
\end{aligned}
\tag{2.1}
\]

where a solution `theta in (0,pi)` gives the squared spectral value

\[
y=6+2\cos\theta.
\tag{2.2}
\]

At `theta=0` the left side of (2.1) equals

\[
T_m(3)>1.
\tag{2.3}
\]

Set

\[
\theta_D:=\frac\pi{2N},
\qquad
a_D:=2+\cos\theta_D>1.
\]

Then

\[
\frac{\cos((N-\tfrac12)\theta_D)}{\cos(\theta_D/2)}
=\tan\frac{\theta_D}{2},
\qquad
\sin(N\theta_D)=1.
\]

Hence the left side of (2.1) at `theta_D` is

\[
\tan\frac{\theta_D}{2}
\left[
T_m(a_D)-U_m(a_D)-U_{m-1}(a_D)
\right].
\tag{2.4}
\]

For every `a>1` and `m>=1`,

\[
\boxed{U_m(a)>T_m(a).}
\tag{2.5}
\]

Indeed, write `a=cosh eta`, `eta>0`.  Then

\[
U_m(a)=\frac{\sinh((m+1)\eta)}{\sinh\eta}
\]

and

\[
\sinh((m+1)\eta)
=\sinh(m\eta)\cosh\eta+\cosh(m\eta)\sinh\eta
>\cosh(m\eta)\sinh\eta.
\]

Thus (2.5) follows because `T_m(a)=cosh(m eta)`.  In particular the bracket in (2.4) is strictly negative, so the left side of (2.1) at `theta_D` is negative and hence strictly smaller than `1`.

By continuity, equation (2.1) has a root

\[
0<\theta_*<\theta_D.
\tag{2.6}
\]

The corresponding squared eigenvalue (2.2) obeys

\[
y_*>6+2\cos\theta_D.
\]

Therefore

\[
\rho(H(1))^2\ge y_*
>6+2\cos\frac\pi{2N},
\]

which is exactly (1.1).

Note that this argument does not require uniqueness of the first root: existence of one root before the Dirichlet angle already gives the desired spectral lower bound.

---

## 3. Antiperiodic endpoint

At `z=-1` the defect arc is the soft oscillatory channel and the generic arc is hyperbolic.  The block-transfer calculation is the channel-exchanged version of (2.1).  Repeating the preceding argument with

\[
N\longleftrightarrow m
\]

gives a squared eigenvalue larger than

\[
6+2\cos\frac\pi{2m},
\]

which proves (1.2).

Finally the full Bloch gap is bounded above by either special endpoint gap.  Choosing the endpoint whose soft length is `M=max{N,m}` gives (1.3).

## 4. Role in finite-period optimization

Fix total geometry

\[
N+m=2r.
\]

Every unbalanced integer geometry satisfies

\[
M=\max\{N,m\}\ge r+1.
\]

Since `D_M` is strictly decreasing in `M`, Theorem A--B give the universal competitor bound

\[
\boxed{
\Gamma_{N,m,q}
<D_{r+1}
=2-2\cos\frac\pi{2(r+1)}
\qquad((N,m)\ne(r,r)).
}
\tag{4.1}
\]

Thus the exact all-period balanced-geometry problem is reduced to proving the single lower bound

\[
\Gamma_{r,r,q}>D_{r+1}.
\]

No information about the individual unbalanced separations is needed after this reduction.
