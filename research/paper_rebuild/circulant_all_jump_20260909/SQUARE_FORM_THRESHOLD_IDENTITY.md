# Single-square form of the general separation threshold determinant

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

The compact four-term threshold formula admits a substantially simpler representation. This is useful for the remaining exact finite phase-diagram problem.

## Setup

Write

\[
L=2(N+m),\qquad h=2m,
\]

and at the squared threshold `8` define

\[
x=\frac{4-d}{2},\qquad y=\frac{4+d}{2},\qquad x+y=4.
\]

Put

\[
u=U_{N-1}(x),\qquad p=U_{m-1}(y),
\]

\[
X=T_N(x),\qquad Y=T_m(y).
\]

The general threshold formula is

\[
P_{N,m,z}(8)=\mathcal F_{N,m}(d)-e
\]

with

\[
\begin{aligned}
\mathcal F_{N,m}(d)-2
={}&\frac{(4-d^2)(20-d^2)}2p^2u^2\\
&+2(4-d^2)XYpu\\
&+(d^2+12d+4)p^2\\
&+(d^2-8d+12)u^2.
\end{aligned}
\tag{1}
\]

## Theorem — exact square collapse

Define

\[
\boxed{
Z_{N,m}(d):=XY+(x-1)(y-1)pu.
}
\tag{2}
\]

Then

\[
\boxed{
\mathcal F_{N,m}(d)-2
=4Z_{N,m}(d)^2-8(x-1)p^2-4.
}
\tag{3}
\]

Equivalently,

\[
\boxed{
\mathcal F_{N,m}(d)
=4Z_{N,m}(d)^2-8(x-1)p^2-2.
}
\tag{4}
\]

Hence a sufficient and, for the relaxed value `e=2`, exact threshold condition is

\[
\boxed{
Z_{N,m}(d)^2>1+2(x-1)p^2.
}
\tag{5}
\]

## Proof

The Chebyshev identities give

\[
X^2-1=(x^2-1)u^2,
\qquad
Y^2-1=(y^2-1)p^2.
\tag{6}
\]

Since `x+y=4`,

\[
(x-1)(y-1)=xy-3=\frac{4-d^2}{4}.
\tag{7}
\]

Expanding the square in (3),

\[
\begin{aligned}
4Z^2={}&4X^2Y^2
+8(x-1)(y-1)XYpu\\
&+4(x-1)^2(y-1)^2p^2u^2.
\end{aligned}
\]

Use (6) to expand `4X^2Y^2`. Its `p^2u^2` coefficient is

\[
4(x^2-1)(y^2-1)
+4(x-1)^2(y-1)^2.
\]

Factoring `(x-1)(y-1)` and using `x+y=4` gives

\[
\begin{aligned}
&4(x-1)(y-1)\bigl((x+1)(y+1)+(x-1)(y-1)\bigr)\\
&\qquad=8(x-1)(y-1)(xy+1)\\
&\qquad=\frac{(4-d^2)(20-d^2)}2.
\end{aligned}
\]

The mixed coefficient becomes

\[
8(x-1)(y-1)=2(4-d^2).
\]

The pure `u^2` coefficient is

\[
4(x^2-1)=d^2-8d+12.
\]

For the pure `p^2` term, after subtracting `8(x-1)p^2`,

\[
4(y^2-1)-8(x-1)
=d^2+12d+4.
\]

Finally the constant `4` from `4X^2Y^2` is cancelled by the terminal `-4` in (3). Thus the right side of (3) is exactly (1).

## Endpoint checks

At `d=-2`, one has `x=3`, `y=1`, `Y=1`, `p=m`, and `(x-1)(y-1)=0`. Therefore

\[
Z_{N,m}(-2)=T_N(3)
\]

and

\[
\mathcal F_{N,m}(-2)-2
=4\bigl(T_N(3)^2-4m^2-1\bigr),
\]

recovering the antiperiodic margin.

At `d=2`, one has `x=1`, `y=3`, so

\[
Z_{N,m}(2)=T_m(3)
\]

and

\[
\mathcal F_{N,m}(2)-2=4\bigl(T_m(3)^2-1\bigr)>0.
\]

## Significance

The general exact-classification problem is now reduced to controlling one quantity,

\[
Z_{N,m}(d),
\]

against the explicit comparison scale

\[
\sqrt{1+2(x-1)U_{m-1}(y)^2}.
\]

In particular the conjectural exact criterion

\[
2m<T_N(3)
\]

is equivalent to showing that positivity at the antiperiodic endpoint cannot be lost inside the phase interval.