# Universal all-orders Robin expansion for the macroscopic endpoint gaps

Date: 2026-09-14

Status: **Proved**. This upgrades the finite coefficient calculations to an arbitrary-order theorem.

## 1. Setup

Write

\[
L=2(N+m),\qquad N,m\to\infty,
\]

and assume the two soft lengths remain macroscopically comparable:

\[
0<c_0\le \frac mN\le c_1<\infty.
\tag{1.1}
\]

Let

\[
e^+_{N,m}=8-\rho(H(1))^2,
\qquad
e^-_{N,m}=8-\rho(H(-1))^2.
\]

Put

\[
\Lambda=3+2\sqrt2.
\]

## Theorem A — all-orders periodic endpoint expansion

There is a universal sequence of real coefficients

\[
a_2,a_3,a_4,\ldots
\]

such that for every fixed integer `K>=2`, uniformly under (1.1),

\[
\boxed{
 e^+_{N,m}
 =\sum_{j=2}^{K}a_jN^{-j}
 +O_{K,c_0,c_1}(N^{-K-1})
 +O(\Lambda^{-2m}).
}
\tag{1.2}
\]

The coefficients do not depend on the ratio `m/N`.

## Theorem B — all-orders antiperiodic endpoint expansion

The *same* coefficients satisfy, for every fixed `K>=2`,

\[
\boxed{
 e^-_{N,m}
 =\sum_{j=2}^{K}a_jm^{-j}
 +O_{K,c_0,c_1}(m^{-K-1})
 +O(\Lambda^{-2N}).
}
\tag{1.3}
\]

Thus the two endpoint theories are algebraically identical after exchanging the soft length; their difference is only the exponentially small tunneling through the opposite hard arc.

The first coefficients, already computed explicitly, are

\[
\boxed{
 a_2=\frac{\pi^2}{4},
 \qquad
 a_3=-\frac{\sqrt2\pi^2}{4},
}
\]

\[
\boxed{
 a_4=\frac{\pi^2(72-\pi^2)}{192},
 \qquad
 a_5=\frac{\sqrt2\pi^2(-64+3\pi^2)}{256},
}
\]

and

\[
\boxed{
 a_6=
 \frac{\pi^2(\pi^4-750\pi^2+7200)}{23040}.
}
\tag{1.4}
\]

---

## 2. Limiting hard-wall ratio

For the periodic endpoint, the exact scalar quantization equation can be written

\[
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}
-
R_m(2+\cos\theta)
\tan(\theta/2)\sin(N\theta)
=
\frac1{T_m(2+\cos\theta)},
\tag{2.1}
\]

where

\[
R_m(a)=\frac{U_m(a)+U_{m-1}(a)}{T_m(a)}.
\]

For `a` in a fixed neighborhood of `3`, the hyperbolic representation gives

\[
R_m(a)=R_\infty(a)+O(\Lambda^{-2m}),
\tag{2.2}
\]

uniformly with any fixed number of derivatives, where

\[
R_\infty(a)
=
\frac{e^{\eta(a)}+1}{\sinh\eta(a)},
\qquad
\cosh\eta(a)=a.
\tag{2.3}
\]

The right side of (2.1) is also `O(Lambda^-m)` and hence beyond every algebraic order in `1/N` under (1.1).

---

## 3. Analytic implicit equation

Set

\[
h=N^{-1},
\qquad
x=N\theta.
\]

After replacing the finite hard ratio by its limiting value, equation (2.1) becomes

\[
\mathscr F(x,h)=0,
\tag{3.1}
\]

where

\[
\boxed{
\mathscr F(x,h)
=
\frac{\cos(x-xh/2)}{\cos(xh/2)}
-
R_\infty(2+\cos(xh))
\tan(xh/2)\sin x.
}
\tag{3.2}
\]

The function `mathscr F` is real analytic near

\[
(x,h)=\left(\frac\pi2,0\right).
\]

At `h=0`,

\[
\mathscr F(x,0)=\cos x,
\]

so

\[
\mathscr F(\pi/2,0)=0,
\qquad
\partial_x\mathscr F(\pi/2,0)=-1\ne0.
\tag{3.3}
\]

The analytic implicit-function theorem therefore gives a unique analytic root

\[
\boxed{
 x(h)=\frac\pi2+b_1h+b_2h^2+b_3h^3+\cdots
}
\tag{3.4}
\]

for `|h|` sufficiently small.

The actual finite-`m` root differs from `x(h)` by `O(Lambda^-m)` after any fixed number of differentiations, by (2.2) and the uniform inverse bound from (3.3).

---

## 4. Recovering the universal gap series

The endpoint gap is

\[
e^+_{N,m}=2-2\cos(hx(h))+O(\Lambda^{-2m}).
\tag{4.1}
\]

Since the right side is analytic in `h` and begins at order `h^2`, it has a unique convergent local expansion

\[
2-2\cos(hx(h))
=\sum_{j\ge2}a_jh^j.
\tag{4.2}
\]

Taylor's theorem gives (1.2) to arbitrary fixed order. Recursive coefficient comparison in (3.2) produces all `b_j`, hence all `a_j`, algorithmically.

The values in (1.4) are obtained by carrying this recursion through `h^6` and agree with the independently derived finite-order formulas.

---

## 5. Antiperiodic endpoint by channel exchange

At `z=-1`, the defect arc is the soft oscillatory channel and the complementary generic arc is hyperbolic. After exchanging

\[
N\longleftrightarrow m,
\]

the hard stable root is again `Lambda`, the same analytic function `R_infty` appears, and the normalized first-soft-root equation is exactly (3.2) with

\[
h=m^{-1}.
\]

The finite generic hard arc contributes `O(Lambda^-2N)`. Thus the same analytic root `x(h)` and the same coefficients `a_j` give (1.3).

---

## 6. Consequences

1. The equal endpoint coefficients observed through sixth order are not accidental: they agree to **every algebraic order**.
2. At balanced geometry `N=m=r`,
   \[
   e^+_{r,r}-e^-_{r,r}=O(\Lambda^{-2r}),
   \]
   so the endpoint splitting is beyond all powers of `1/r`.
3. Every algebraic orientation asymmetry in the full Bloch gap must therefore come from the local Bloch-phase structure, not from the endpoint Robin series.
4. The coefficient sequence is recursively computable to arbitrary order from one fixed analytic equation.