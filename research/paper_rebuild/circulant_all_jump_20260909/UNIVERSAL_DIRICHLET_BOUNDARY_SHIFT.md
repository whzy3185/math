# Universal first boundary correction in the macroscopic Dirichlet regime

Date: 2026-09-10

Status: **Proved**. This refines both the periodic and antiperiodic Dirichlet laws by one order.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and assume

\[
N,m\to\infty,
\qquad
\frac mN\to\gamma\in(0,\infty).
\]

Let

\[
e^+_{N,m}=8-\rho(H(1))^2,
\qquad
e^-_{N,m}=8-\rho(H(-1))^2.
\]

Define soft angles by

\[
e^+_{N,m}=2-2\cos\theta_+,
\]

\[
e^-_{N,m}=2-2\cos\theta_-.
\]

The leading Dirichlet laws already give

\[
N\theta_+\to\frac\pi2,
\qquad
m\theta_-\to\frac\pi2.
\]

## Theorem A — common `1/sqrt(2)` effective-length shift

One has

\[
\boxed{
N\left(\frac\pi2-N\theta_+\right)
\longrightarrow\frac\pi{2\sqrt2},
}
\tag{1.1}
\]

and

\[
\boxed{
m\left(\frac\pi2-m\theta_-\right)
\longrightarrow\frac\pi{2\sqrt2}.
}
\tag{1.2}
\]

Consequently

\[
\boxed{
e^+_{N,m}
=\frac{\pi^2}{4N^2}
-\frac{\pi^2}{2\sqrt2\,N^3}
+o(N^{-3}),}
\tag{1.3}
\]

and

\[
\boxed{
e^-_{N,m}
=\frac{\pi^2}{4m^2}
-\frac{\pi^2}{2\sqrt2\,m^3}
+o(m^{-3}).}
\tag{1.4}
\]

Thus both endpoint obstructions have the same first effective boundary shift

\[
\boxed{a_*=1/\sqrt2.}
\]

Formally,

\[
e^+_{N,m}
=\frac{\pi^2}{4(N+a_*)^2}+O(N^{-4})
\]

and similarly with `N` replaced by `m`, up to the order proved above.

---

## 2. Periodic endpoint

The exact endpoint quantization equation for general even separation is

\[
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}
-R_m(a)\tan(\theta/2)\sin(N\theta)
=\frac1{T_m(a)},
\tag{2.1}
\]

where

\[
a=2+\cos\theta
\]

and

\[
R_m(a)=\frac{U_m(a)+U_{m-1}(a)}{T_m(a)}.
\]

Since `m` is proportional to `N` and `a->3`, hyperbolic Chebyshev formulas give exponentially fast limits

\[
\frac1{T_m(a)}=o(N^{-K})
\]

for every fixed `K`, and

\[
R_m(a)=R_\infty(3)+O(N^{-2})+o(N^{-K}),
\]

where

\[
R_\infty(3)
=\frac{(3+2\sqrt2)+1}{2\sqrt2}
=1+\sqrt2.
\tag{2.2}
\]

Put

\[
x=N\theta.
\]

Using

\[
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}
=\cos x+\tan(\theta/2)\sin x,
\]

(2.1) becomes

\[
\cos x
-\sqrt2\tan(\theta/2)\sin x
=o(N^{-1}).
\tag{2.3}
\]

Write

\[
\varepsilon_N=\frac\pi2-x.
\]

Since `x->pi/2`,

\[
\cos x=\varepsilon_N+o(\varepsilon_N),
\qquad
\sin x=1+o(1),
\]

and

\[
N\tan(\theta/2)
=N\tan\frac{x}{2N}
\longrightarrow\frac\pi4.
\]

Equation (2.3) first gives `epsilon_N=O(N^-1)`, and then multiplication by `N` yields

\[
N\varepsilon_N
\longrightarrow
\sqrt2\frac\pi4
=\frac\pi{2\sqrt2}.
\]

This proves (1.1).

Now

\[
\theta_+
=\frac{x}{N}
=\frac\pi{2N}
-\frac\pi{2\sqrt2\,N^2}
+o(N^{-2}).
\]

Since

\[
2-2\cos\theta
=\theta^2+O(\theta^4),
\]

squaring gives (1.3).

---

## 3. Antiperiodic endpoint

Use the exact antiperiodic characteristic formula from `ANTIPERIODIC_DIRICHLET_GAP_LAW.md` and divide it by the square of the exponentially growing hard-channel Chebyshev factor.

Let

\[
x=m\theta_-.
\]

The hard-channel ratio converges exponentially to

\[
q_0=3-2\sqrt2.
\]

After substituting

\[
y=6+2\cos\theta_-
\]

and the soft identities

\[
p=\frac{\sin x}{\sin\theta_-},
\qquad
v=\frac{\sin(x-\theta_-)}{\sin\theta_-},
\]

the normalized determinant has the uniform second-order expansion

\[
\begin{aligned}
0={}&32\cos^2x
-16\sqrt2\,\theta_-\sin(2x)\\
&+28\theta_-^2\sin^2x
-12\theta_-^2
+o(\theta_-^2+\cos^2x).
\end{aligned}
\tag{3.1}
\]

The exponentially small hard-channel and seam corrections are absorbed into the remainder.

Write

\[
\varepsilon_m=\frac\pi2-x.
\]

The leading Dirichlet law gives `epsilon_m->0`. Expanding (3.1) around `x=pi/2`,

\[
0
=16\left(
2\varepsilon_m^2
-2\sqrt2\,\theta_-\varepsilon_m
+\theta_-^2
\right)
+o(\theta_-^2+\varepsilon_m^2).
\]

The quadratic is a perfect square:

\[
2\varepsilon_m^2
-2\sqrt2\theta_-\varepsilon_m
+\theta_-^2
=2\left(\varepsilon_m-\frac{\theta_-}{\sqrt2}\right)^2.
\]

Hence

\[
\varepsilon_m
=\frac{\theta_-}{\sqrt2}+o(\theta_-).
\]

Since

\[
m\theta_-\to\frac\pi2,
\]

we obtain

\[
m\varepsilon_m
\to\frac\pi{2\sqrt2},
\]

which is (1.2). The expansion (1.4) follows exactly as in the periodic case.

---

## 4. Interpretation

The constant `1/sqrt(2)` is the common penetration depth of the soft mode into the complementary hard alternating medium. It is independent of which arc is soft:

- at `z=1`, the `N`-arc is soft;
- at `z=-1`, the `m`-arc is soft.

This common boundary shift explains the near-symmetry of the two special-fiber gaps in balanced finite geometries and is the natural starting point for a fourth-order balanced-geometry analysis.