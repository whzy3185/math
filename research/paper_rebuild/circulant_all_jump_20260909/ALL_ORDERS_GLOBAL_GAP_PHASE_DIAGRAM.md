# All-orders global gap phase diagram across the balanced transition

Date: 2026-09-14

Status: **Proved** by combining the all-orders Robin theorem, the all-orders periodic cusp theorem, and the uniform integer orientation-selection theorem.

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

1. the endpoint Robin coefficients
   \[
   a_2,a_3,a_4,\ldots;
   \]
2. the periodic phase-slip gain coefficients
   \[
   c_0,c_1,c_2,\ldots.
   \]

Define the periodic-global coefficients `g_j` by

\[
\boxed{
 g_j=a_j\quad(j=2,3),
 \qquad
 g_j=a_j-c_{j-4}\quad(j\ge4).
}
\tag{1.1}
\]

## Theorem A — all-orders periodic/balanced branch

If

\[
\boxed{m\le N,}
\]

then for every fixed `K>=2`, uniformly in the compatible odd multiplier,

\[
\boxed{
\Gamma_{N,m,q}
=
\sum_{j=2}^{K}g_jN^{-j}
+O_K(N^{-K-1})
+O(\Lambda^{-2m}).
}
\tag{1.2}
\]

This includes the balanced point `m=N`: the two endpoint gaps agree beyond every algebraic order, but the periodic cusp lowers the global gap by the gain series.

## Theorem B — all-orders antiperiodic branch

If

\[
\boxed{m>N,}
\]

then the global maximizing phase is exactly `z=-1` for all sufficiently large parameters and

\[
\boxed{
\Gamma_{N,m,q}
=
\sum_{j=2}^{K}a_jm^{-j}
+O_K(m^{-K-1})
+O(\Lambda^{-2N}).
}
\tag{1.3}

Thus the antiperiodic side contains no algebraic phase-slip series.

---

## 2. First displayed coefficients

The endpoint series begins

\[
\boxed{
\begin{aligned}
A(\ell):={}&\sum_{j\ge2}a_j\ell^{-j}\\
={}&\frac{\pi^2}{4\ell^2}
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
\begin{aligned}
C(N):={}&\sum_{j\ge0}c_jN^{-j-4}\\
={}&\frac{\pi^2}{32N^4}
-\frac{3\pi^2}{32\sqrt2N^5}
+\frac{\pi^2(32\sqrt2-3)}{768N^6}
+\cdots.
\end{aligned}}
\tag{2.2}
\]

Hence the periodic/balanced branch is

\[
\boxed{G_+(N)=A(N)-C(N),}
\tag{2.3}
\]

whereas the antiperiodic branch is simply

\[
\boxed{G_-(m)=A(m).}
\tag{2.4}
\]

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

## 3. Algebraic Stokes-type switch at balance

The two universal formal series agree through cubic order after identifying the soft length, but differ beginning at fourth order:

\[
\boxed{
G_+(\ell)-G_-(\ell)
=-\frac{\pi^2}{32\ell^4}+O(\ell^{-5}).
}
\tag{3.1}
\]

The physical integer geometry selects

\[
\boxed{
\begin{cases}
G_+(N),&m\le N,\\
G_-(m),&m>N.
\end{cases}}
\tag{3.2}
\]

Thus the balanced hyperplane is a genuine higher-order switching surface: the endpoint Robin series is the same on both sides, but one side acquires a cusp transseries correction and the other does not.

Because `m-N` is integral, the switch occurs between the two neighboring physical layers

\[
m=N
\quad\text{and}\quad
m=N+1.
\]

---

## 4. Full all-orders optimizer data

On the periodic/balanced side, the maximizing compressed phase has an all-orders series

\[
\boxed{
|\delta_N|
=N^{-2}
\left(
 b_0+b_1N^{-1}+b_2N^{-2}+\cdots
\right),
}
\tag{4.1}
\]

where

\[
b_0=\frac\pi{4\sqrt2},
\qquad
b_1=-\frac\pi8,
\qquad
b_2=\frac{\pi(32-27\sqrt2)}{192}.
\]

On the antiperiodic side,

\[
\boxed{z=-1}
\]

exactly for all sufficiently large parameters; there is no algebraic displacement series.

---

## 5. Consequences

1. The macroscopic two-defect theory is governed by only two universal formal series, `A` and `C`.
2. Every endpoint coefficient `a_j` is orientation-independent; orientation enters only through the cusp gain coefficients `c_j`.
3. Balance is not merely where the leading Dirichlet lengths agree. It is the unique integer layer on which an exponentially small endpoint degeneracy is resolved by an algebraic cusp correction.
4. All higher coefficients are recursively computable from fixed analytic implicit equations, so no new growing-matrix calculation is required at higher order.