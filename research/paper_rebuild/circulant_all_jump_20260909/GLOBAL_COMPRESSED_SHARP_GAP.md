# Uniform global sharp gap for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It upgrades the endpoint result to the full continuous Bloch edge and is uniform in the odd multiplier of the jump.

## 1. Statement

Let `L>=4` be even and let the period-`2L` two-defect word be

\[
Q_0=Q_2=1,\qquad Q_j=-1\quad(j\ne0,2),
\]

with Hamilton-gauge lift

\[
\tau_0=\tau_1=1,
\qquad
\tau_2=\tau_3=-1,
\qquad
\tau_j=(-1)^j\quad(4\le j<2L).
\]

For

\[
s=L(2q+1),\qquad q\ge0,
\]

let

\[
R_{L,q}=\max_{|z|=1}\rho(H_{L,q}(z))^2
\]

be the continuous squared Bloch edge, and define the global gap

\[
\Gamma_{L,q}:=8-R_{L,q}.
\]

Put

\[
x_0:=\arccos\frac13.
\]

### Theorem A — global sharp compressed gap

For every sequence of even integers `L->infinity` and every sequence of integers `q=q(L)>=0`,

\[
\boxed{
L^2\Gamma_{L,q}
\longrightarrow
4x_0^2
=4\arccos(1/3)^2.}
\tag{1.1}
\]

Thus the convergence is uniform with respect to the odd multiplier in the sequential sense: the odd part of the jump may vary arbitrarily with `L`.

Equivalently,

\[
\boxed{
\Gamma_{L,q}
=\frac{4\arccos(1/3)^2}{L^2}+o(L^{-2})}
\tag{1.2}
\]

uniformly over all odd multipliers.

Numerically,

\[
4\arccos(1/3)^2\approx6.06104434856.
\]

No numerical input is used in the proof.

### Theorem B — asymptotic phase rigidity

Let `z_{L,q}` be any Bloch phase attaining `R_{L,q}`. Define

\[
d_{L,q}=z_{L,q}^{2q+1}+z_{L,q}^{-(2q+1)},
\qquad
e_{L,q}=z_{L,q}+z_{L,q}^{-1}.
\]

Then

\[
\boxed{e_{L,q}\longrightarrow2,}
\tag{1.3}
\]

and, more strongly,

\[
\boxed{
L^2(2-d_{L,q})\longrightarrow0.}
\tag{1.4}
\]

Thus every global maximizing phase becomes periodic in the basic Bloch coordinate and is even more tightly locked in the compressed long-jump coordinate.

---

## 2. Endpoint upper bound

Let

\[
e_L:=8-\rho(H_{L,q}(1))^2.
\]

The endpoint theorem proves that `e_L` is independent of `q` and

\[
L^2e_L\longrightarrow4x_0^2.
\tag{2.1}
\]

Since the global Bloch edge is at least the value of the `z=1` fiber,

\[
0<\Gamma_{L,q}\le e_L.
\tag{2.2}
\]

Hence, with

\[
r=L/2,
\]

we have uniformly in `q`

\[
\Gamma_{L,q}=O(r^{-2}).
\tag{2.3}
\]

Choose a maximizing Bloch phase and abbreviate

\[
g:=\Gamma_{L,q},
\qquad
d=2-\mu,
\qquad 0\le\mu\le4,
\qquad e=z+z^{-1}\in[-2,2].
\tag{2.4}
\]

At the top root

\[
y=8-g.
\]

The exact two-phase characteristic equation is

\[
P(y)=u^2A(y,d)+uwB(y,d)+C(y,d)-e=0,
\tag{2.5}
\]

where

\[
t=\frac{y-d-4}{2}=1+\frac{\mu-g}{2},
\qquad
u=U_{r-2}(t),
\qquad
w=U_{r-3}(t).
\tag{2.6}
\]

---

## 3. Hyperbolic near-edge roots are impossible

Put

\[
\delta:=\mu-g.
\tag{3.1}
\]

We first prove that, along any sequence `L->infinity`, a maximizing root cannot have `delta>=0` infinitely often.

In the variables `(g,delta)`, the coefficients in (2.5) are

\[
A=
(\delta^2+2\delta g-5\delta+2g)
(\delta^2+2\delta g-3\delta+6g-12),
\tag{3.2}
\]

\[
B=-(\delta+2g-6)
(\delta^2+2\delta g-4\delta+4g),
\tag{3.3}
\]

and

\[
C=\delta^2+4\delta g-16\delta+4g^2-28g+34.
\tag{3.4}
\]

Suppose first that

\[
r^2\delta\longrightarrow D<\infty
\]

along a subsequence. Since `g=O(r^-2)`, write also, after refinement,

\[
r^2g\longrightarrow G.
\]

Let

\[
\kappa=\sqrt D.
\]

Because

\[
t=1+\frac{\delta}{2},
\]

the standard hyperbolic Chebyshev representation gives

\[
\frac ur,\frac wr
\longrightarrow
S(\kappa):=
\begin{cases}
\dfrac{\sinh\kappa}{\kappa},&\kappa>0,\\
1,&\kappa=0.
\end{cases}
\tag{3.5}
\]

From (3.2)--(3.4),

\[
r^2A\longrightarrow60D-24G,
\qquad
r^2B\longrightarrow24(G-D),
\qquad
C\longrightarrow34.
\tag{3.6}
\]

Therefore the root equation (2.5) converges to

\[
0
=36D\,S(\kappa)^2+34-e_*,
\tag{3.7}
\]

where `e_* in [-2,2]` is a subsequential limit of `e`. But

\[
36D S(\kappa)^2=36\sinh^2\kappa\ge0,
\]

so the right side of (3.7) is at least `32`, a contradiction.

It remains to exclude

\[
r^2\delta\longrightarrow\infty.
\tag{3.8}
\]

Since `delta>=0`, `t>=1`, hence

\[
u\ge w\ge0,
\qquad
u\ge r-1.
\tag{3.9}
\]

At `g=0`, the two relevant coefficient combinations are

\[
A_0(\delta)
=\delta(\delta-5)(\delta^2-3\delta-12)>0
\quad(0<\delta\le4),
\tag{3.10}
\]

and

\[
A_0(\delta)+B_0(\delta)
=\delta(\delta^3-9\delta^2+13\delta+36)>0.
\tag{3.11}
\]

For completeness, the cubic in (3.11) is at least `8` on `[0,4]`: its derivative has only one critical point in `[0,4]`, which is a local maximum, so its minimum is attained at an endpoint, where the values are `36` and `8`.

The quotients of (3.10)--(3.11) by `delta` extend continuously and positively to `delta=0`. Therefore there exists an absolute `c>0` such that, for `0<delta<=4`,

\[
\min(A_0,A_0+B_0)\ge c\delta.
\tag{3.12}
\]

Since `g=O(r^-2)` and (3.8) implies `delta/g->infinity`, uniform continuity of the polynomial coefficients gives, for all sufficiently large indices,

\[
\min(A,A+B)\ge\frac c2\delta.
\tag{3.13}
\]

Writing `a=w/u in [0,1]`,

\[
A+aB\ge\min(A,A+B)\ge\frac c2\delta.
\]

Hence

\[
u^2A+uwB
=u^2(A+aB)
\ge\frac c2(r-1)^2\delta\longrightarrow\infty,
\]

while `C-e` stays bounded. This contradicts (2.5).

Thus every maximizing near-edge root satisfies, eventually,

\[
\boxed{\delta<0.}
\tag{3.14}
\]

---

## 4. Elliptic scaling and the limiting Robin law

By (3.14),

\[
0\le\mu<g.
\tag{4.1}
\]

Put

\[
h:=g-\mu>0.
\]

Define `theta in (0,pi)` by

\[
h=2-2\cos\theta.
\tag{4.2}
\]

Then

\[
t=1-\frac h2=\cos\theta,
\]

and therefore

\[
u=rac{\sin((r-1)\theta)}{\sin\theta},
\qquad
w=rac{\sin((r-2)\theta)}{\sin\theta}.
\tag{4.3}
\]

Set

\[
x=r\theta.
\]

Because `h<=g<=e_L`, the exact endpoint representation

\[
e_L=2-2\cos(x_r/r),
\qquad x_r<\pi/2,
\]

implies

\[
0<x\le x_r.
\tag{4.4}
\]

In particular `x` is uniformly bounded and every subsequence has a convergent refinement. Let

\[
x\to x_*,
\qquad
r^2\mu\to M,
\qquad
e\to e_*.
\tag{4.5}
\]

Since `mu<=g=O(r^-2)`, the middle limit is finite. Equation (4.2) gives

\[
r^2h\longrightarrow x_*^2.
\tag{4.6}
\]

The elliptic Chebyshev representation yields

\[
\frac ur,\frac wr
\longrightarrow
\begin{cases}
\dfrac{\sin x_*}{x_*},&x_*>0,\\
1,&x_*=0.
\end{cases}
\tag{4.7}
\]

In the variables `(h,mu)`, the coefficient formulas are

\[
A=(h^2+2h\mu-7h-2\mu)
(h^2+2h\mu-9h-6\mu+12),
\tag{4.8}
\]

\[
B=(h+2\mu-6)
(h^2+2h\mu-8h-4\mu),
\tag{4.9}
\]

\[
C=h^2+4h\mu-12h+4\mu^2-28\mu+34.
\tag{4.10}
\]

Hence

\[
r^2A\longrightarrow-84x_*^2-24M,
\]

\[
r^2B\longrightarrow48x_*^2+24M,
\]

and

\[
C\longrightarrow34.
\]

The `M` terms cancel between the two Chebyshev contributions. Passing to the limit in (2.5) gives the universal Robin law

\[
\boxed{
36\sin^2x_*=34-e_*.}
\tag{4.11}
\]

---

## 5. Rigidity of the limiting root

Because `e_*<=2`, (4.11) implies

\[
\sin^2x_*\ge\frac89.
\tag{5.1}
\]

On the other hand, (4.4) and the endpoint theorem give

\[
x_*\le x_0=\arccos(1/3)<\pi/2.
\]

Since `sin` is strictly increasing on this interval,

\[
\sin^2x_*\le\sin^2x_0=\frac89.
\tag{5.2}
\]

Thus equality holds throughout:

\[
\boxed{x_*=x_0,\qquad e_*=2.}
\tag{5.3}
\]

Finally,

\[
r^2g=r^2\mu+r^2h
\longrightarrow M+x_0^2.
\tag{5.4}
\]

But the endpoint upper bound (2.2) and the endpoint theorem imply

\[
\limsup r^2g\le x_0^2.
\]

Therefore

\[
\boxed{M=0}
\]

and

\[
\boxed{r^2g\longrightarrow x_0^2.}
\tag{5.5}
\]

Since `L=2r`, (5.5) is exactly (1.1). It also gives

\[
r^2\mu\to0,
\]

which is equivalent to (1.4), while (5.3) proves (1.3).

Because every subsequence admits only this limiting behavior, the convergence holds for the full sequence and for arbitrary varying odd multipliers.

---

## 6. Consequences

The compressed two-defect family now has a sharp polynomial global gap:

\[
\boxed{
8-R_{L,q}
\sim
\frac{4\arccos(1/3)^2}{L^2}.}
\]

This replaces the earlier elementary exponential lower estimate

\[
16/8^{L-1}
\]

by the correct leading scale and exact constant.

For `v_2(s)=k>=2`, choosing

\[
L=2^k
\]

gives period

\[
2^{k+1}
\]

and, as the `2`-adic scale grows,

\[
8-R_s
\sim
\frac{4\arccos(1/3)^2}{4^k},
\]

uniformly in the odd part of `s`.

This is a genuinely arithmetic spectral-compression law: the period and the sharp gap scale depend on the `2`-adic part of the jump, while the odd part disappears from the leading asymptotics.
