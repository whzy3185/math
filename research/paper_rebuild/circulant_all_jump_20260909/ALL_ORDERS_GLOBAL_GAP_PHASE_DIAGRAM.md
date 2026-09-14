# All-orders global gap phase diagram across the balanced transition

Date: 2026-09-14

Status: **Proved after hostile-audit correction**.

The algebraic phase diagram is unchanged.  The corrected finite statement is that the `m>N` optimizer is exponentially close to the compressed-antiperiodic set `d=-2`; it is not generally the literal physical phase `z=-1` when the odd multiplier exceeds one.

## 1. Setup

Write

\[
L=2(N+m),
\qquad
N,m\to\infty,
\qquad
0<c_0\le m/N\le c_1<\infty.
\]

Let

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

There are two universal coefficient sequences:

1. endpoint Robin coefficients `a_2,a_3,...`;
2. periodic phase-slip gain coefficients `c_0,c_1,...`.

Define

\[
 g_j=a_j\quad(j=2,3),
\qquad
 g_j=a_j-c_{j-4}\quad(j\ge4).
\tag{1.1}
\]

## Theorem A — all-orders periodic/balanced branch

If

\[
\boxed{m\le N,}
\]

then for every fixed `K>=2`, uniformly in the odd multiplier,

\[
\boxed{
\Gamma_{N,m,q}
=
\sum_{j=2}^{K}g_jN^{-j}
+O_K(N^{-K-1})
+O(\Lambda^{-2m}).
}
\tag{1.2}

This includes balance: the endpoint gaps agree beyond every algebraic order, but the periodic cusp supplies the global algebraic improvement.

## Theorem B — all-orders compressed-antiperiodic branch

If

\[
\boxed{m>N,}
\]

then every global maximizing phase lies exponentially close to the compressed well

\[
\boxed{d=z^{2q+1}+z^{-(2q+1)}=-2.}
\]

For every fixed `K>=2`,

\[
\boxed{
\Gamma_{N,m,q}
=
\sum_{j=2}^{K}a_jm^{-j}
+O_K(m^{-K-1})
+O(\Lambda^{-2N}).
}
\tag{1.3}

Thus there is no algebraic phase-slip series on this side.  The physical seam induces only an exponentially small shift of the maximizing phase.

If `n=2q+1` and `z_0=e^{\pm i\pi/n}`, then a global maximizer can be written

\[
z_*=z_0e^{i\delta/n},
\qquad
|\delta|=O(\Lambda^{-2N}).
\tag{1.4}

For `n=1`, this reduces to physical `z=-1` up to the exact symmetry of that case.

---

## 2. First displayed coefficients

The endpoint series is

\[
\boxed{
\begin{aligned}
A(\ell)={}&\frac{\pi^2}{4\ell^2}
-\frac{\sqrt2\pi^2}{4\ell^3}
+\frac{\pi^2(72-\pi^2)}{192\ell^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256\ell^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040\ell^6}
+\cdots.
\end{aligned}}
\tag{2.1}
\]

The periodic gain series is

\[
\boxed{
C(N)=\frac{\pi^2}{32N^4}
-\frac{3\pi^2}{32\sqrt2N^5}
+\frac{\pi^2(32\sqrt2-3)}{768N^6}
+\cdots.
}
\tag{2.2}

Hence

\[
\boxed{G_+(N)=A(N)-C(N)}
\tag{2.3}
\]

on the periodic/balanced side and

\[
\boxed{G_-(m)=A(m)}
\tag{2.4}
\]

as the complete algebraic series on the compressed-antiperiodic side.

Through sixth order,

\[
\boxed{
\begin{aligned}
G_+(N)={}&\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}
+\frac{\pi^2(66-\pi^2)}{192N^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256N^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2-960\sqrt2+7290)}{23040N^6}
+\cdots.
\end{aligned}}
\tag{2.5}
\]

---

## 3. Algebraic switch at balance

At a common soft length `ell`,

\[
G_+(\ell)-G_-(\ell)
=-\frac{\pi^2}{32\ell^4}+O(\ell^{-5}).
\tag{3.1}
\]

The integer geometry selects

\[
\boxed{
\begin{cases}
G_+(N),&m\le N,\\
G_-(m),&m>N,
\end{cases}}
\tag{3.2}
\]

to every algebraic order.

The physical phase on the second branch differs from the exact `d=-2` set only beyond every algebraic order, so it does not alter (3.2).

Because `m-N` is integral, the algebraic switch occurs between

\[
m=N
\quad\text{and}\quad
m=N+1.
\]

---

## 4. Optimizer data

On the periodic/balanced side,

\[
|\delta_N|
=N^{-2}
\left(
 b_0+b_1N^{-1}+b_2N^{-2}+\cdots
\right),
\]

with

\[
b_0=\frac\pi{4\sqrt2},
\qquad
b_1=-\frac\pi8,
\qquad
b_2=\frac{\pi(32-27\sqrt2)}{192}.
\]

On the compressed-antiperiodic side there is **no algebraic displacement series**.  Instead the physical optimizer satisfies the exponential localization (1.4).

This is the precise asymmetry between the two wells.

## 5. Consequences

1. The algebraic macroscopic theory is governed by only two universal formal series, `A` and `C`.
2. Endpoint coefficients are orientation-independent; algebraic orientation enters only through the periodic cusp.
3. The `m>N` physical seam affects the optimizer only beyond every algebraic order.
4. Balance is the unique integer layer where an endpoint degeneracy is resolved by an algebraic cusp correction.
5. All algebraic coefficients remain recursively computable from the fixed Robin and cusp implicit equations.