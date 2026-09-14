# All-orders expansion for the periodic-well phase slip

Date: 2026-09-14

Status: **Proved**. This upgrades the explicit `N^-6` phase-slip formulas to an arbitrary-order theorem.

## 1. Setup

Assume

\[
N,m\to\infty,
\qquad
0<c_0\le m/N\le1,
\]

so that the periodic well is globally dominant, including the balanced endpoint `m=N`.

Let

\[
e^+_{N,m}=8-\rho(H(1))^2
\]

and let `delta` be the compressed phase displacement from the periodic endpoint. Put

\[
h=N^{-1},
\qquad
\delta=h^2\zeta.
\]

The improving branch is taken with `zeta>=0`; the opposite sign is supplied by complex-conjugation symmetry.

## Theorem A — all-orders local effective potential

There is a real-analytic function

\[
\mathscr V(\zeta,h)
\]

in a neighborhood of

\[
\left(\frac\pi{4\sqrt2},0\right)
\]

such that, for every fixed `K`, uniformly for `zeta` in a fixed compact neighborhood of the limiting minimizer,

\[
\boxed{
N^4\bigl(g(h^2\zeta)-e^+_{N,m}\bigr)
=\mathscr V(\zeta,h)
+O_{K}(h^{K+1})
+O(\Lambda^{-2m}),
}
\tag{1.1}
\]

and

\[
\boxed{
\mathscr V(\zeta,0)
=\zeta^2-\frac\pi{2\sqrt2}\zeta.
}
\tag{1.2}
\]

Consequently

\[
\mathscr V(\zeta,h)
=
\sum_{j\ge0}V_j(\zeta)h^j
\]

with analytic coefficient functions `V_j`.

## Theorem B — all-orders optimizing phase

There is a unique analytic minimizer

\[
\boxed{
\zeta_*(h)=b_0+b_1h+b_2h^2+\cdots
}
\tag{1.3}
\]

near the positive limiting minimizer, with

\[
\boxed{
b_0=\frac\pi{4\sqrt2}.}
\]

For every fixed `K`, the global maximizing compressed phase in the periodic well satisfies

\[
\boxed{
|\delta_N|
=
\sum_{j=0}^{K}b_jN^{-j-2}
+O_K(N^{-K-3})
+O(\Lambda^{-2m}N^{-2}).
}
\tag{1.4}

The first three coefficients are

\[
\boxed{
 b_0=\frac\pi{4\sqrt2},
 \qquad
 b_1=-\frac\pi8,
 \qquad
 b_2=\frac{\pi(32-27\sqrt2)}{192}.
}
\tag{1.5}

## Theorem C — all-orders phase-slip gain

There is a universal coefficient sequence `c_0,c_1,c_2,...` such that

\[
\boxed{
 e^+_{N,m}-\Gamma_{N,m,q}
 =
 \sum_{j=0}^{K}c_jN^{-j-4}
 +O_K(N^{-K-5})
 +O(\Lambda^{-2m}N^{-4})
}
\tag{1.6}

for every fixed `K`, throughout the periodic-dominant region and at balance.

The first coefficients are

\[
\boxed{
 c_0=\frac{\pi^2}{32},
 \qquad
 c_1=-\frac{3\pi^2}{32\sqrt2},
 \qquad
 c_2=\frac{\pi^2(32\sqrt2-3)}{768}.
}
\tag{1.7}

---

## 2. Analytic branch after resolving the cusp

Let

\[
\mu=2-2\cos\delta.
\]

For `delta=h^2 zeta` and `zeta>=0`,

\[
\sqrt\mu
=h^2\zeta\,S(h^2\zeta),
\]

where `S` is analytic near zero and `S(0)=1`.

Thus the apparent absolute-value nonanalyticity disappears once the improving sign is fixed. The exact hard-divided `4 x 4` transfer determinant becomes a real-analytic equation

\[
\mathscr G(x,\zeta,h)=0
\tag{2.1}
\]

near

\[
(x,\zeta,h)
=
\left(\frac\pi2,\frac\pi{4\sqrt2},0\right).
\]

At `h=0`, the normalized equation has soft derivative

\[
\partial_x\mathscr G
=-(1-\Lambda^{-2})\ne0.
\tag{2.2}
\]

Therefore the analytic implicit-function theorem gives a unique analytic soft coordinate

\[
\boxed{
x=x(\zeta,h).}
\tag{2.3}
\]

The finite hard arc changes this branch only by `O(Lambda^-2m)` with all fixed derivatives.

---

## 3. Analytic effective potential

The exact gap identity is

\[
g-e^+
=
\mu+
2-2\cos(hx(\zeta,h))
-
\bigl(2-2\cos(hx_0(h))\bigr),
\tag{3.1}
\]

where `x_0(h)` is the analytic endpoint Robin root from the all-orders endpoint theorem.

Since both `x(\zeta,h)` and `x_0(h)` are analytic, and

\[
\mu=h^4\zeta^2+O(h^8),
\]

the quotient

\[
\boxed{
\mathscr V(\zeta,h)
:=h^{-4}(g-e^+)
}
\tag{3.2}
\]

extends analytically to `h=0`.

The leading endpoint-subtracted transfer equation gives

\[
x(\zeta,0)-x_0(0)
=-\frac{\zeta}{2\sqrt2},
\]

so (3.1)--(3.2) yield

\[
\mathscr V(\zeta,0)
=
\zeta^2-
\frac\pi{2\sqrt2}\zeta,
\]

proving (1.2).

---

## 4. Analytic minimizer

At `h=0`,

\[
\partial_\zeta\mathscr V
=2\zeta-\frac\pi{2\sqrt2},
\]

so the unique positive critical point is

\[
\zeta_0=\frac\pi{4\sqrt2}.
\]

Moreover

\[
\partial_\zeta^2\mathscr V(\zeta_0,0)=2>0.
\tag{4.1}
\]

Applying the analytic implicit-function theorem to

\[
\partial_\zeta\mathscr V(\zeta,h)=0
\]

gives the analytic minimizer `zeta_*(h)` in (1.3). Taylor expansion proves (1.4).

Substitution of `zeta_*(h)` into `-mathscr V` gives an analytic gain series

\[
-\mathscr V(\zeta_*(h),h)
=c_0+c_1h+c_2h^2+\cdots,
\]

which proves (1.6).

---

## 5. Recovery of the known coefficients

Carrying the recursive expansion of the exact transfer equation through order `h^2` gives

\[
\zeta_*(h)
=
\frac\pi{4\sqrt2}
-
\frac\pi8h
+
\frac{\pi(32-27\sqrt2)}{192}h^2
+O(h^3),
\]

and

\[
-\mathscr V(\zeta_*(h),h)
=
\frac{\pi^2}{32}
-
\frac{3\pi^2}{32\sqrt2}h
+
\frac{\pi^2(32\sqrt2-3)}{768}h^2
+O(h^3),
\]

recovering the previously audited formulas.

---

## 6. Balanced and unbalanced consequences

- If `m<N`, the periodic well is globally dominant and (1.4)--(1.6) are the global Bloch expansions.
- If `m=N`, the endpoint gaps agree beyond every algebraic order, but the periodic cusp produces the algebraic gain (1.6), so the same expansions remain global.
- If `m>N`, this theorem describes only a losing local periodic well; the true global edge is exactly antiperiodic and is governed by the all-orders Robin series with soft length `m`.

Thus the full higher-order phase diagram consists of one all-orders cusp series on the periodic side and one all-orders analytic Robin series on the antiperiodic side.