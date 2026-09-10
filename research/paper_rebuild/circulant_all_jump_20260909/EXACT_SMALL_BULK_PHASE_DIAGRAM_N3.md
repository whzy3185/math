# Exact finite phase diagram for complementary bulk length `N=3`

Date: 2026-09-10

Status: **Proved by analytic reduction plus exact rational Bernstein certificates**. This note belongs only to Paper I.

We continue the finite classification for

\[
L=2(N+m),\qquad h=2m,
\]

using the exact threshold equation

\[
P_{N,m,z}(8)=\mathcal F_{N,m}(d)-e,
\qquad d,e\in[-2,2].
\]

## Theorem — exact `N=3` phase diagram

For complementary bulk length

\[
N=3,
\]

the entire Bloch spectrum is strictly below the squared threshold `8` if and only if

\[
\boxed{1\le m\le49.}
\]

Equivalently,

\[
\boxed{
\text{global sub-eight}
\iff
2m<T_3(3)=99.
}
\]

The first super-eight case is `m=50`.

## 1. Obstructed side

The exact antiperiodic determinant is

\[
P_{3,m,-1}(8)
=4\bigl(T_3(3)^2-4m^2\bigr).
\]

Since

\[
T_3(3)=99,
\]

we have

\[
P_{3,m,-1}(8)<0
\qquad(m\ge50).
\]

Therefore the `z=-1` fiber has a squared eigenvalue above `8` for every `m\ge50`.

## 2. Analytic safe range

The exponential safe-region theorem states that

\[
m\le\frac23U_{N-1}(3)
\]

is sufficient for global sub-eight behavior. For `N=3`,

\[
U_2(3)=35,
\]

so every

\[
1\le m\le23
\]

is already covered analytically.

It remains to certify

\[
24\le m\le49.
\]

## 3. Exact Bernstein reduction

Put

\[
t=\frac{d+2}{4}\in[0,1],
\]

and define

\[
f_m(t):=\mathcal F_{3,m}(-2+4t)-2.
\]

Using the single-square threshold identity,

\[
f_m(t)=4\left[Z_{3,m}(t)^2-4(1-t)U_{m-1}(1+2t)^2-1\right],
\]

where

\[
\begin{aligned}
Z_{3,m}(t)={}&T_3(3-2t)T_m(1+2t)\\
&+4t(1-t)U_2(3-2t)U_{m-1}(1+2t).
\end{aligned}
\]

Thus `f_m` is a polynomial with integer coefficients and degree `2m+6`.

Expand it in the Bernstein basis of its exact degree:

\[
f_m(t)=\sum_{k=0}^{2m+6}b_{m,k}\binom{2m+6}{k}t^k(1-t)^{2m+6-k}.
\]

For every integer

\[
24\le m\le49,
\]

exact rational arithmetic gives

\[
\boxed{
b_{m,k}\ge b_{m,0}=39200-16m^2>0
\qquad(0\le k\le2m+6).}
\]

The endpoint value follows directly from

\[
\begin{aligned}
f_m(0)
&=4\bigl(T_3(3)^2-4m^2-1\bigr)\\
&=4(99^2-4m^2-1)\\
&=39200-16m^2.
\end{aligned}
\]

Because Bernstein basis functions are nonnegative and sum to one on `[0,1]`,

\[
f_m(t)\ge39200-16m^2>0
\]

for every `t\in[0,1]` and every `24\le m\le49`.

Consequently

\[
\mathcal F_{3,m}(d)>2
\]

throughout `[-2,2]`. Since the physical seam coordinate satisfies `e\le2`,

\[
P_{3,m,z}(8)>0
\]

for every Bloch phase. The periodic endpoint is strictly sub-eight, and connected Hermitian inertia propagation therefore gives

\[
\rho(H_{3,m,q}(z))^2<8
\]

for every unit `z` and every odd multiplier.

This completes the proof.

## 4. Exact-certificate status

The accompanying verifier `verify_exact_N3_bernstein.py` uses only integer/rational polynomial recurrences. It does not sample phases and does not use floating-point eigenvalues. Its role is to make the finite Bernstein coefficient check reproducible.

The mathematical reduction to finitely many rational coefficient inequalities is analytic; the remaining inequalities are exact symbolic certificates.

## 5. Consequence

Together with the previously proved `N=1,2` phase diagrams, the conjectural antiperiodic criterion

\[
2m<T_N(3)
\]

is now exact for

\[
\boxed{N=1,2,3.}
\]

The next finite layer is `N=4`, where

\[
T_4(3)=577
\]

and the conjectural safe range is `m\le288`.