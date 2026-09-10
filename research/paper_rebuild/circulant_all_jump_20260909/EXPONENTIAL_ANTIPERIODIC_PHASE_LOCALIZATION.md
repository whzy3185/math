# Exponential localization of every possible threshold failure

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

This theorem is uniform in the defect length and the odd jump multiplier.

## 1. Statement

Write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\ge1,
\]

and put

\[
u_N:=U_{N-1}(3).
\]

Let

\[
d=z^{2q+1}+z^{-(2q+1)}\in[-2,2]
\]

be the compressed long-jump Bloch coordinate.

### Theorem A — exponential antiperiodic localization

For `N>=2`, every phase satisfying

\[
\boxed{d+2\ge u_N^{-2}}
\tag{1.1}
\]

is automatically strictly below the squared threshold `8`.

Equivalently, if a Bloch phase can possibly have a squared eigenvalue at or above `8`, then necessarily

\[
\boxed{
0\le d+2<u_N^{-2}.}
\tag{1.2}
\]

Since

\[
u_N
=\frac{(3+2\sqrt2)^N-(3-2\sqrt2)^N}{4\sqrt2},
\]

the width of the only dangerous long-phase window is

\[
O\bigl((3+2\sqrt2)^{-2N}\bigr).
\]

---

## 2. Proof

Outside the universal dangerous interval

\[
d<-6+4\sqrt2,
\]

the compact threshold formula is already strictly positive. Hence suppose

\[
d=-2+4t,
\qquad
0\le t<\sqrt2-1.
\]

As in `EXPONENTIAL_SAFE_REGION.md`, put

\[
x=3-2t,
\qquad y=1+2t,
\]

\[
u=U_{N-1}(x),
\qquad p=U_{m-1}(y).
\]

The compact threshold formula implies

\[
\frac{\mathcal F(d)-2}{16}
\ge p^2\bigl(a(t)u^2-b(t)\bigr)+g(t)u^2,
\tag{2.1}
\]

where

\[
a(t)=8t(1-t)(1+t-t^2),
\]

\[
b(t)=1-2t-t^2\le1,
\qquad
g(t)=(1-t)(2-t)>0.
\]

On this interval,

\[
a(t)\ge8(2-\sqrt2)t.
\tag{2.2}
\]

We show that

\[
t\ge\frac1{4u_N^2}
\quad\Longrightarrow\quad
a(t)u^2>1.
\tag{2.3}
\]

For `t<=1/(2N)`, the positive expansion of `U_{N-1}(3-2t)` in powers of `1-t` gives

\[
u\ge(1-Nt)u_N.
\]

The function `t(1-Nt)^2` has no interior minimum on

\[
[1/(4u_N^2),1/(2N)],
\]

and `u_N>=3N` for `N>=2`. Checking the two endpoints yields

\[
8(2-\sqrt2)t u^2>1.
\]

For `t>=1/(2N)`, simply use

\[
u\ge U_{N-1}(1)=N
\]

to obtain

\[
8(2-\sqrt2)t u^2
\ge4(2-\sqrt2)N>1.
\]

Thus (2.3) holds. Since `b(t)<=1`, equation (2.1) then gives

\[
\mathcal F(d)-2>0.
\]

For a physical Bloch phase,

\[
P(8,z)=\mathcal F(d)-e,
\qquad e=z+z^{-1}\le2,
\]

so `P(8,z)>0`. Starting from the sub-eight periodic endpoint and using inertia continuity shows that the fiber cannot have a squared eigenvalue at or above `8`.

Finally

\[
d+2=4t,
\]

so `t>=1/(4u_N^2)` is exactly (1.1). This proves the theorem.

## 3. Significance

The antiperiodic obstruction theorem is not merely one convenient test phase. In the large-bulk regime, every possible failure of global sub-eight behavior is forced into an exponentially shrinking neighborhood of that phase in the compressed coordinate.

This is the key reason the exact antiperiodic curve controls the asymptotic two-parameter phase diagram.