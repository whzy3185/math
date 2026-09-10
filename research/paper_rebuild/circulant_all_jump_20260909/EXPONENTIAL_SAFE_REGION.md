# An exponential-size global sub-eight safe region

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

The earlier theorem `HALF_PERIOD_DEFECT_SAFE_REGION.md` proved global sub-eight whenever `m<=N`. The exact threshold formula allows a much larger safe region, on the correct exponential scale of the antiperiodic obstruction curve.

## 1. Statement

Write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\ge1.
\]

Let

\[
U_N^*:=U_{N-1}(3).
\]

### Theorem A — exponential safe region

If `N>=2` and

\[
\boxed{
m\le\frac23 U_{N-1}(3),}
\tag{1.1}
\]

then, for every odd multiplier `2q+1`, the arbitrary-even-separation two-defect phase satisfies

\[
\boxed{
\max_{|z|=1}\rho(H_{L,q,h}(z))^2<8.}
\tag{1.2}
\]

The remaining small safe pair `(N,m)=(1,1)` is covered by the original compressed theorem.

Since

\[
U_{N-1}(3)
=\frac{(3+2\sqrt2)^N-(3-2\sqrt2)^N}{4\sqrt2},
\]

(1.1) is an exponential-size safe region in the defect half-length `m`.

---

## 2. Rescaled dangerous-phase formula

The compact threshold formula shows that only

\[
d<-6+4\sqrt2
\]

can be dangerous. Put

\[
d=-2+4t,
\qquad 0\le t<\sqrt2-1.
\tag{2.1}
\]

Then

\[
x=3-2t,
\qquad y=1+2t,
\]

and set

\[
u=U_{N-1}(x),
\qquad p=U_{m-1}(y),
\]

\[
X=T_N(x),
\qquad Y=T_m(y).
\]

Dividing `mathcal F(d)-2` by `16` gives

\[
\begin{aligned}
Q(t):=\frac{\mathcal F(d)-2}{16}
={}&8t(1-t)(1+t-t^2)p^2u^2\\
&+2t(1-t)XYpu\\
&+(t^2+2t-1)p^2\\
&+(1-t)(2-t)u^2.
\end{aligned}
\tag{2.2}
\]

The second term is nonnegative. Write

\[
a(t)=8t(1-t)(1+t-t^2),
\]

\[
b(t)=1-2t-t^2>0,
\qquad
g(t)=(1-t)(2-t)>0.
\]

Then

\[
Q(t)\ge p^2(a(t)u^2-b(t))+g(t)u^2.
\tag{2.3}
\]

Also, on the dangerous interval,

\[
\boxed{g(t)-2b(t)=t+3t^2\ge0.}
\tag{2.4}
\]

---

## 3. The region away from the antiperiodic endpoint

Put

\[
u_0:=U_{N-1}(3).
\]

Since `t<sqrt(2)-1`,

\[
1-t\ge2-\sqrt2,
\qquad
1+t-t^2\ge1,
\]

so

\[
\boxed{a(t)\ge8(2-\sqrt2)t.}
\tag{3.1}
\]

We claim that

\[
\boxed{
t\ge\frac1{4u_0^2}
\quad\Longrightarrow\quad
a(t)u^2\ge1.}
\tag{3.2}
\]

For `0<=t<=1/(2N)`, use the positive expansion of

\[
U_{N-1}(3-2t)=U_{N-1}(1+2(1-t))
\]

in powers of `1-t`. It gives

\[
u\ge(1-Nt)u_0.
\tag{3.3}
\]

On the interval

\[
\frac1{4u_0^2}\le t\le\frac1{2N},
\]

the function `t(1-Nt)^2` has no interior minimum: its only interior critical point is a maximum at `t=1/(3N)`. Hence it suffices to check the endpoints.

For `N>=2`, the elementary recurrence for `U_j(3)` gives

\[
u_0\ge3N.
\tag{3.4}
\]

At the left endpoint,

\[
Nt\le\frac{N}{4u_0^2}\le\frac1{72},
\]

so (3.1)--(3.3) yield

\[
a(t)u^2
\ge2(2-\sqrt2)\left(\frac{71}{72}\right)^2>1.
\tag{3.5}
\]

At the right endpoint,

\[
a(t)u^2
\ge8(2-\sqrt2)\frac1{2N}\frac{u_0^2}{4}
\ge9(2-\sqrt2)N>1.
\tag{3.6}
\]

If instead `t>=1/(2N)`, then `x>=1` gives

\[
u=U_{N-1}(x)\ge U_{N-1}(1)=N,
\]

and therefore

\[
a(t)u^2
\ge8(2-\sqrt2)\frac1{2N}N^2
=4(2-\sqrt2)N>1.
\tag{3.7}
\]

This proves (3.2).

Since `b(t)<=1`, (3.2) gives

\[
a(t)u^2-b(t)\ge0.
\]

Equation (2.3) then implies

\[
Q(t)>0
\]

throughout this region.

---

## 4. The very-near-antiperiodic region

It remains to consider

\[
0\le t<\frac1{4u_0^2}.
\tag{4.1}
\]

From the same positive `1-t` expansion and (3.4),

\[
u\ge(1-Nt)u_0
\ge\frac{71}{72}u_0.
\tag{4.2}
\]

Write

\[
y=1+2t=\cosh\beta.
\]

Since

\[
\cosh(2\sqrt t)\ge1+2t,
\]

we have

\[
0\le\beta\le2\sqrt t.
\tag{4.3}
\]

The hyperbolic representation gives

\[
p=U_{m-1}(\cosh\beta)
=\frac{\sinh(m\beta)}{\sinh\beta}
\le m e^{m\beta}
\le m e^{2m\sqrt t}.
\tag{4.4}
\]

Under (1.1) and (4.1),

\[
2m\sqrt t
\le\frac23.
\]

Hence

\[
p\le\frac23 e^{2/3}u_0.
\tag{4.5}
\]

The elementary inequality

\[
e^{2/3}<2
\]

follows, for example, from

\[
\log2=2\left(\frac13+\frac1{3^3\cdot3}+\frac1{3^5\cdot5}+\cdots\right)>\frac23.
\]

Therefore

\[
\frac pu
<\frac{(4/3)u_0}{(71/72)u_0}
=\frac{96}{71}<\sqrt2.
\tag{4.6}
\]

Using (2.4),

\[
\begin{aligned}
g(t)u^2-b(t)p^2
&\ge b(t)(2u^2-p^2)\\
&>0.
\end{aligned}
\tag{4.7}
\]

The remaining terms in (2.2) are nonnegative, so again

\[
Q(t)>0.
\]

Thus

\[
\mathcal F_{N,m}(d)>2
\]

throughout the entire dangerous interval.

---

## 5. Completion of the spectral argument

Outside the dangerous interval, the general threshold formula already gives `mathcal F(d)>2`. Hence for every unit Bloch phase,

\[
P_{N,m,z}(8)=\mathcal F(d)-e>0
\]

because `e<=2`.

At `z=1`, the endpoint theorem gives

\[
8I-H(1)^2>0.
\]

By continuity of the Hermitian fibers and the absence of a threshold crossing, the inertia remains positive around the whole connected Bloch circle. Therefore

\[
8I-H(z)^2>0
\]

for every unit `z`, proving (1.2).

---

## 6. Comparison with the exact obstruction scale

The antiperiodic obstruction occurs when

\[
2m>T_N(3).
\]

Using

\[
T_N(3)^2-8U_{N-1}(3)^2=1,
\]

the obstruction threshold satisfies

\[
\frac{T_N(3)}2
\sim\sqrt2\,U_{N-1}(3).
\]

Thus both the proved safe region and the proved obstructed region have the same exponential scale

\[
(3+2\sqrt2)^N.
\]

The remaining multiplicative gap is only an absolute constant factor. This is substantially sharper than the earlier linear safe condition `m<=N`.