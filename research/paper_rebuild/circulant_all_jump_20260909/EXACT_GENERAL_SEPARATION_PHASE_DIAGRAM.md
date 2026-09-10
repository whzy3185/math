# Exact all-parameter phase diagram for the even-separation two-defect family

Date: 2026-09-10

Status: **Proved**. This is a headline theorem for Paper I.

This note closes the finite two-parameter threshold problem left open by the general separation formula and the asymptotic phase-transition theorem.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\ge1,
\]

and consider the period-`2L` two-defect flux word

\[
Q_0=Q_h=1,
\qquad Q_j=-1\quad(j\ne0,h).
\]

For any odd multiplier

\[
s=L(2q+1),\qquad q\ge0,
\]

let `H_{N,m,q}(z)` be the corresponding Bloch fiber and put

\[
R_{N,m,q}:=\max_{|z|=1}\rho(H_{N,m,q}(z))^2.
\]

Let `T_n,U_n` denote the Chebyshev polynomials of the first and second kind.

## Theorem A — exact global sub-eight classification

For every `N,m>=1` and every `q>=0`,

\[
\boxed{
R_{N,m,q}<8
\quad\Longleftrightarrow\quad
2m<T_N(3).
}
\tag{1.1}
\]

If

\[
2m>T_N(3),
\]

then the antiperiodic fiber already crosses the threshold:

\[
\boxed{
\rho(H_{N,m,q}(-1))^2>8.
}
\tag{1.2}
\]

There is no equality case, because `T_N(3)` is odd whereas `2m` is even.

Thus the entire even-separation two-defect phase diagram is governed by one exact Chebyshev inequality.

---

## 2. The obstructed side

The exact antiperiodic threshold determinant proved earlier is

\[
\boxed{
P_{N,m,-1}(8)
=4\bigl(T_N(3)^2-4m^2\bigr),
}
\tag{2.1}
\]

where `P` is the monic characteristic polynomial in the squared spectral variable.

If

\[
2m>T_N(3),
\]

then (2.1) is negative. Since the squared roots are real and nonnegative, at least one squared eigenvalue is larger than `8`. This proves (1.2) and the necessary direction of (1.1).

It remains to prove the converse.

---

## 3. Arithmetic form of the safe condition

Put

\[
U:=U_{N-1}(3),
\qquad
T:=T_N(3).
\]

The standard Chebyshev identity at `x=3` is

\[
\boxed{T^2-8U^2=1.}
\tag{3.1}
\]

The integer `T` is odd. Define

\[
M:=\frac{T-1}{2}\in\mathbb Z_{\ge1}.
\]

Equation (3.1) is equivalent to the exact Pell-type identity

\[
\boxed{M(M+1)=2U^2.}
\tag{3.2}
\]

The safe condition `2m<T` is therefore exactly

\[
1\le m\le M.
\tag{3.3}
\]

In particular

\[
\boxed{m^2<2U^2,}
\tag{3.4}
\]

and, writing

\[
c:=\frac mU,
\]

we have `c^2<2`. More quantitatively,

\[
\boxed{
2-c^2
=\frac{2U^2-m^2}{U^2}
\ge\frac{M}{U^2}.
}
\tag{3.5}
\]

The right side is the finite arithmetic margin that will dominate the boundary-layer errors.

---

## 4. Reduction to the exponentially thin antiperiodic layer

Assume from now on that `2m<T_N(3)`.

For `N=1,2`, the safe direction has already been proved exactly in `EXACT_SMALL_BULK_PHASE_DIAGRAM_N1_N2.md`. Hence it is enough to treat

\[
N\ge3.
\]

Let

\[
d=-2+4t,
\qquad 0\le t\le1.
\]

The exponential phase-localization theorem proves that every phase outside

\[
\boxed{
0\le t<\frac1{4U^2}
}
\tag{4.1}
\]

is already strictly sub-eight. Thus only (4.1) remains.

On this interval put

\[
x=3-2t,
\qquad y=1+2t,
\]

\[
u=U_{N-1}(x),
\qquad p=U_{m-1}(y).
\]

The compact threshold formula gives the lower estimate

\[
\boxed{
\frac{\mathcal F_{N,m}(d)-2}{16}
\ge
p^2\bigl(a(t)u^2-b(t)\bigr)+g(t)u^2,
}
\tag{4.2}
\]

where

\[
a(t)=8t(1-t)(1+t-t^2),
\]

\[
b(t)=1-2t-t^2,
\qquad
g(t)=(1-t)(2-t).
\tag{4.3}
\]

We prove that the right side of (4.2) is strictly positive.

---

## 5. Uniform control of the two Chebyshev factors

### Lemma B — lower control of the bulk factor

On (4.1),

\[
\boxed{
u\ge(1-Nt)U.}
\tag{5.1}
\]

### Proof

Use the positive expansion

\[
U_{N-1}(1+2s)
=\sum_{j=0}^{N-1}
\binom{N+j}{2j+1}(4s)^j.
\]

Here `s=1-t`. Since

\[
(1-t)^j\ge1-jt\ge1-Nt,
\]

termwise comparison gives (5.1).

Put

\[
\rho:=1-Nt.
\tag{5.2}
\]

Since `U>=N` and `t<1/(4U^2)`, we have `rho>0`.

### Lemma C — upper control of the defect factor

Let

\[
\xi:=tU^2,
\qquad
r:=2m\sqrt t=2c\sqrt\xi.
\tag{5.3}
\]

Then

\[
\boxed{
p\le m\,S_0(r),
\qquad
S_0(r):=\frac{\sinh r}{r},
}
\tag{5.4}
\]

with the continuous convention `S_0(0)=1`.

### Proof

Write

\[
y=1+2t=\cosh\beta.
\]

Then

\[
\beta=2\operatorname{arsinh}\sqrt t\le2\sqrt t
\]

and exactly

\[
\sinh\beta=2\sqrt{t(1+t)}\ge2\sqrt t.
\]

Therefore

\[
\begin{aligned}
p
&=\frac{\sinh(m\beta)}{\sinh\beta}\\
&\le\frac{\sinh(2m\sqrt t)}{2\sqrt t}
=m\frac{\sinh r}{r}.
\end{aligned}
\]

This proves (5.4).

Because `xi<1/4` and `c^2<2`,

\[
0\le r<\sqrt2.
\tag{5.5}
\]

The power series of `sinh r/r` gives the convenient uniform estimate

\[
\boxed{S_0(r)<\frac32\qquad(0\le r\le\sqrt2).}
\tag{5.6}
\]

Indeed

\[
S_0(r)
\le1+\sum_{k\ge1}\frac{2^k}{(2k+1)!}
<1+\frac13\sum_{j\ge0}10^{-j}
<\frac32.
\]

---

## 6. The limiting boundary-layer inequality with a finite margin

Define

\[
\boxed{
\Phi(c,\xi)
:=2+c^2S_0(r)^2(8\xi-1),
\qquad r=2c\sqrt\xi.
}
\tag{6.1}
\]

### Lemma D — universal ideal lower bound

For

\[
0\le\xi\le\frac14,
\qquad0\le c^2\le2,
\]

one has

\[
\boxed{
\Phi(c,\xi)\ge2-c^2.
}
\tag{6.2}
\]

### Proof

If `xi>=1/8`, then `8xi-1>=0`, so

\[
\Phi\ge2\ge2-c^2.
\]

Suppose `0<=xi<=1/8`. Then `r<=1`, and since

\[
8\xi c^2=2r^2,
\]

we have

\[
\Phi=2+(2r^2-c^2)S_0(r)^2.
\]

Hence

\[
\begin{aligned}
\Phi-(2-c^2)
&=2r^2S_0(r)^2-c^2(S_0(r)^2-1)\\
&\ge2\{r^2S_0(r)^2-(S_0(r)^2-1)\}\\
&=2\{1-(1-r^2)S_0(r)^2\}.
\end{aligned}
\]

For `0<=r<=1`,

\[
(1-r^2)\left(\frac{\sinh r}{r}\right)^2\le1.
\tag{6.3}
\]

To verify (6.3), set

\[
f(r)=\frac r{\sqrt{1-r^2}}-\sinh r.
\]

Then `f(0)=0` and

\[
f'(r)=(1-r^2)^{-3/2}-\cosh r\ge0,
\]

because

\[
-\log(1-r^2)\ge r^2,
\qquad
\log\cosh r\le r^2/2.
\]

Thus (6.3) holds and proves (6.2).

---

## 7. Finite-`N` error is smaller than the arithmetic margin

Let

\[
B(t):=p^2(a(t)u^2-b(t))+g(t)u^2.
\]

If

\[
a(t)u^2-b(t)\ge0,
\]

then immediately `B(t)>0`. Hence suppose

\[
a(t)u^2-b(t)<0.
\tag{7.1}
\]

Using (5.1), (5.4), and the sign in (7.1),

\[
\frac{B(t)}{U^2}
\ge
c^2S_0(r)^2\left(8\xi\rho^2A_t-1\right)
+g(t)\rho^2,
\tag{7.2}
\]

where

\[
A_t:=(1-t)(1+t-t^2)=1-2t^2+t^3.
\]

Compare (7.2) with `Phi(c,xi)`. Their difference is bounded below by `-E`, where

\[
E
=c^2S_0(r)^2\,8\xi(1-\rho^2A_t)
+\bigl(2-g(t)\rho^2\bigr).
\tag{7.3}
\]

We have

\[
1-\rho^2A_t
\le2Nt+2t^2,
\tag{7.4}
\]

and

\[
2-g(t)\rho^2
\le4Nt+3t.
\tag{7.5}
\]

Also, by (5.6) and `c^2<2`,

\[
c^2S_0(r)^2<\frac92<5,
\]

while `8xi<2`. Hence

\[
\begin{aligned}
E
&<20Nt+20t^2+4Nt+3t\\
&\le24Nt+8t\\
&=(24N+8)t\\
&<\frac{6N+2}{U^2}.
\end{aligned}
\tag{7.6}
\]

For `N>=3`, the integer

\[
M=\frac{T_N(3)-1}{2}
\]

satisfies

\[
\boxed{M>6N+2.}
\tag{7.7}
\]

Indeed `M=49` at `N=3`, while the recurrence

\[
T_{N+1}(3)=6T_N(3)-T_{N-1}(3)>5T_N(3)
\]

makes the left side grow by a factor exceeding five at each subsequent step.

Combining (3.5), (6.2), and (7.6)--(7.7),

\[
\begin{aligned}
\frac{B(t)}{U^2}
&\ge\Phi(c,\xi)-E\\
&\ge(2-c^2)-E\\
&\ge\frac{M}{U^2}-E\\
&>0.
\end{aligned}
\]

Thus `B(t)>0` throughout the entire residual boundary layer (4.1).

Equation (4.2) now gives

\[
\boxed{
\mathcal F_{N,m}(d)>2
}
\]

for every residual phase.

Together with the exponential localization theorem, this holds for every

\[
d\in[-2,2].
\]

Since the physical seam coordinate always obeys `e<=2`,

\[
P_{N,m,z}(8)=\mathcal F_{N,m}(d)-e>0
\]

for every unit Bloch phase.

The periodic endpoint `z=1` is strictly sub-eight. The Hermitian fibers vary continuously around the connected unit circle, and the strict positivity above prevents any squared eigenvalue from crossing the level `8`. Therefore

\[
\rho(H_{N,m,q}(z))^2<8
\]

for every `z`, proving the sufficient direction of Theorem A.

---

## 8. Exact phase diagram and first values

The complete criterion is therefore

\[
\boxed{
R_{N,m,q}<8
\iff2m<T_N(3).
}
\]

The first threshold values are

\[
\begin{array}{c|c|c}
N&T_N(3)&\text{largest safe }m\\ \hline
1&3&1\\
2&17&8\\
3&99&49\\
4&577&288\\
5&3363&1681\\
6&19601&9800
\end{array}
\]

Thus the safe defect length grows exponentially in the complementary bulk length.

Using

\[
T_N(3)=\frac{(3+2\sqrt2)^N+(3-2\sqrt2)^N}{2},
\]

the exact threshold is asymptotic to

\[
\boxed{
m_{\max}(N)
=\frac{T_N(3)-1}{2}
\sim\frac14(3+2\sqrt2)^N.
}
\]

This upgrades the earlier asymptotic transition theorem to an exact finite classification.