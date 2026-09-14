# Uniform balanced full-Bloch comparison with the next Dirichlet level

Date: 2026-09-14

Status: **Proved**.

This is the analytic tail for fixed-period balanced geometry. The original proof started at `r>=16`; sharpening one elementary lower bound moves the exact threshold to

\[
\boxed{r\ge9.}
\]

## 1. Statement

Let

\[
N=m=r,
\qquad r\ge9,
\]

and let

\[
\Gamma_{r,r,q}
=8-\max_{|z|=1}\rho(H_{r,r,q}(z))^2.
\]

Define

\[
D_{r+1}=2-2\cos\frac\pi{2(r+1)}.
\]

### Theorem A — uniform all-phase lower gap

For every integer `q>=0` and every integer `r>=9`,

\[
\boxed{
\Gamma_{r,r,q}>D_{r+1}.
}
\tag{1.1}

Consequently, among all integer geometries

\[
N+m=2r,
\]

the balanced geometry `(r,r)` has strictly larger full Bloch gap than every unbalanced geometry.

---

## 2. Reduction to a scalar inequality

Put

\[
\tau=\frac\pi{2(r+1)},
\qquad c=\cos\tau,
\]

and use the comparison energy

\[
y_*=8-D_{r+1}=6+2c.
\]

For the balanced geometry, the all-energy single-square identity gives, after writing

\[
d=4s-2,
\qquad0\le s\le1,
\]

\[
\frac14P(y_*;d,2)
=Z(s)^2-1-4(1-s)p(s)^2,
\tag{2.1}
\]

where

\[
a=c+2s,
\qquad x=c+2(1-s),
\]

\[
p=U_{r-1}(a),
\qquad u=U_{r-1}(x),
\]

and

\[
Z=T_r(x)T_r(a)+(ax-3)up.
\tag{2.2}
\]

For a physical Bloch phase, `e<=2`, so positivity of (2.1) implies positivity of the actual determinant at `y_*`.

We prove

\[
\boxed{
Z(s)^2>1+4(1-s)p(s)^2
\qquad(0\le s\le1).
}
\tag{2.3}

---

## 3. A log-concave Chebyshev ratio

Define

\[
R_r(z):=\frac{T_r(z)}{U_{r-1}(z)}.
\]

Let the zeros of `T_r` be

\[
t_j=\cos\frac{(2j-1)\pi}{2r},
\qquad1\le j\le r,
\]

and those of `U_{r-1}` be

\[
u_j=\cos\frac{j\pi}{r},
\qquad1\le j\le r-1.
\]

They interlace as

\[
t_j>u_j>t_{j+1}.
\]

Since

\[
c=\cos\frac\pi{2(r+1)}>t_1,
\]

both Chebyshev polynomials are positive on `[c,\infty)`. Moreover

\[
(\log R_r)'(z)
=\sum_{j=1}^r\frac1{z-t_j}
-\sum_{j=1}^{r-1}\frac1{z-u_j}.
\]

Differentiating,

\[
(\log R_r)''(z)
=-\sum_{j=1}^r\frac1{(z-t_j)^2}
+\sum_{j=1}^{r-1}\frac1{(z-u_j)^2}<0,
\tag{3.1}
\]

because each `t_j>u_j` makes the paired negative term strictly larger in magnitude, and one extra negative term remains. Thus

\[
\boxed{\log R_r\text{ is strictly concave on }[c,\infty).}
\tag{3.2}

Let

\[
S=2+2c
\]

and, for `b\in[c,S/2]`, define

\[
F(b)=R_r(b)R_r(S-b)+b(S-b)-3.
\tag{3.3}
\]

Then

\[
\begin{aligned}
F'(b)
={}&R_r(b)R_r(S-b)
\bigl[(\log R_r)'(b)-(\log R_r)'(S-b)\bigr]\\
&+(S-2b)\ge0
\end{aligned}
\]

by (3.2). Therefore

\[
\boxed{F(b)\ge F(c)=:F_0.}
\tag{3.4}

Since `Z=upF(min{a,x})`, this gives the common lower scattering factor used on both halves of the phase interval.

---

## 4. Explicit lower bound on the endpoint scattering factor

At `b=c`, put `H=2+c`. The soft values are

\[
U_{r-1}(c)=\cot\tau,
\qquad T_r(c)=\sin\tau.
\]

For the hard ratio,

\[
R_r(H)>\sqrt{H^2-1}=\sqrt{(1+c)(3+c)}.
\]

Multiplying `F_0` by `\cot\tau` gives

\[
\cot\tau\,F_0
>
\sqrt{(1+c)(3+c)}\sin\tau
-(1-c)(3+c)c\,\csc\tau.
\]

The right side simplifies exactly to

\[
\tan\frac\tau2
\frac{1+3c}
{\sqrt{(1+c)^3/(3+c)}+c}.
\tag{4.1}
\]

For `0<c\le1`,

\[
\frac{1+3c}
{\sqrt{(1+c)^3/(3+c)}+c}
>\frac{33}{20}.
\tag{4.2}

Indeed, after moving the `c` term and squaring positive quantities, (4.2) is equivalent to

\[
(20+27c)^2(c+3)>33^2(1+c)^3,
\]

and the difference is

\[
-(3c+1)(120c^2-40c-111)>0
\]

on `[0,1]`. Hence

\[
\boxed{
F_0>
\frac{33}{20}\tan\frac\tau2\tan\tau.
}
\tag{4.3}

---

## 5. The half interval `0<=s<=1/2`

Here `a<=x`, so

\[
x\ge1+c.
\]

Because `U_{r-1}` is increasing to the right of all its zeros,

\[
u\ge U_{r-1}(1+c).
\]

Also `p>=U_{r-1}(c)=\cot\tau>1`. By (3.4),

\[
\frac Zp=uF(a)
\ge U_{r-1}(1+c)F_0.
\tag{5.1}
\]

For `r>=4`, `\tau<=\pi/10` and

\[
c>1-\frac{\pi^2}{200}>\frac{19}{20},
\]

using `\pi^2<10`. Thus

\[
U_{r-1}(1+c)>U_{r-1}(39/20).
\]

From (4.3), `\tan x>x`, and `\pi^2>9`,

\[
U_{r-1}(1+c)F_0
>
\frac{33\pi^2}{160(r+1)^2}U_{r-1}(39/20).
\tag{5.2}
\]

At `r=4`,

\[
U_3(39/20)=\frac{51519}{1000},
\]

so the right side of (5.2) is larger than

\[
\frac{15301143}{4000000}>\frac94>\sqrt5.
\]

Moreover

\[
\frac{U_{r-1}(39/20)}{(r+1)^2}
\]

is strictly increasing for `r>=4`: the Chebyshev recurrence gives

\[
U_r(39/20)>\frac{29}{10}U_{r-1}(39/20),
\]

while

\[
\frac{29}{10}\frac{(r+1)^2}{(r+2)^2}>1.
\]

Thus (5.1) is larger than `\sqrt5` for every `r>=4`. Consequently

\[
\begin{aligned}
\frac1{p^2}\bigl[Z^2-1-4(1-s)p^2\bigr]
&=\left(\frac Zp\right)^2-4(1-s)-\frac1{p^2}\\
&>5-4-1=0.
\end{aligned}
\]

This proves (2.3) on the first half interval.

---

## 6. The half interval `1/2<=s<=1`: sharpened tail estimate

Put

\[
v=1-s\in[0,1/2].
\]

Then the smaller argument is

\[
b=x=c+2v,
\]

while

\[
a=2+c-2v\ge1+c.
\]

By (3.4), `F(b)>=F_0`. The polynomial `U_{r-1}` is convex on `[c,\infty)`, so

\[
u=U_{r-1}(c+2v)
\ge U_0+2vU_1,
\tag{6.1}
\]

where

\[
U_0=U_{r-1}(c)=\cot\tau
\]

and

\[
U_1=U_{r-1}'(c)
=\frac{c^2-r\sin^2\tau}{\sin^3\tau}.
\tag{6.2}
\]

Also

\[
p\ge P_0:=U_{r-1}(1+c).
\]

Use

\[
f_0:=\frac{33}{20}\tan\frac\tau2\tan\tau<F_0
\]

and define

\[
A=f_0U_0,
\qquad B=2f_0U_1.
\]

Then

\[
\frac1{p^2}\bigl[Z^2-1-4vp^2\bigr]
\ge(A+Bv)^2-4v-P_0^{-2}.
\tag{6.3}
\]

A direct simplification gives

\[
AB
=\frac{1089}{200}
\frac{c^2-r\sin^2\tau}{c(1+c)^2}.
\tag{6.4}
\]

Now

\[
c^2-r\sin^2\tau
=1-(r+1)\sin^2\tau.
\]

Since `\sin\tau<\tau` and `\pi^2<10`, for every `r>=9`,

\[
1-(r+1)\sin^2\tau
>
1-\frac{\pi^2}{4(r+1)}
\ge1-\frac{10}{40}
=\frac34.
\tag{6.5}
\]

Also

\[
c(1+c)^2<4.
\]

Therefore

\[
\boxed{
AB>
\frac{1089}{200}\frac{3/4}{4}
=\frac{3267}{3200}
=1+\frac{67}{3200}.
}
\tag{6.6}
\]

As before, `c>1/2`, `1+c>3/2`, and `\sin\tau>1/(r+1)` give

\[
B<\frac{22}{5}(r+1).
\tag{6.7}
\]

The quadratic on the right of (6.3), minimized over the whole real line, has minimum

\[
\frac{4(AB-1)}{B^2}-P_0^{-2}.
\]

Equations (6.6)--(6.7) imply

\[
\frac{4(AB-1)}{B^2}
>
\boxed{
\frac{67}{15488(r+1)^2}.
}
\tag{6.8}
\]

Finally

\[
P_0>U_{r-1}(3/2)>2^{r-1},
\]

so

\[
P_0^{-2}<4^{-(r-1)}.
\tag{6.9}
\]

At `r=9`,

\[
4^{-8}=\frac1{65536}
<\frac{67}{15488\cdot100}.
\tag{6.10}
\]

For each subsequent increment of `r`, the left side falls by a factor four, whereas the rational lower bound on the right is multiplied by

\[
\left(\frac{r+1}{r+2}\right)^2>\frac14.
\]

Hence (6.10) remains true for every `r>=9`. Combining (6.8)--(6.9) proves that the right side of (6.3) is strictly positive.

This completes (2.3) on the second half interval for every `r>=9`.

---

## 7. Return to the Bloch spectrum

We have proved

\[
P(y_*;d,2)>0
\qquad(-2\le d\le2)
\]

for every `r>=9`. For a physical phase,

\[
P(y_*;d,e)=P(y_*;d,2)+(2-e)>0.
\]

At the reference phase `z=1`, `BALANCED_ENDPOINT_BEATS_NEXT_DIRICHLET_LEVEL.md` gives

\[
e_r^+>D_{r+1},
\]

so the endpoint fiber has no squared eigenvalue at or above `y_*`. Since the determinant never vanishes at `y_*`, inertia is constant around the Bloch circle. Therefore every fiber lies strictly below `y_*`, proving

\[
\Gamma_{r,r,q}>D_{r+1}.
\]

For any unbalanced geometry with `N+m=2r`, `UNIVERSAL_ENDPOINT_DIRICHLET_UPPER_BOUND.md` gives

\[
\Gamma_{N,m,q}<D_{r+1}.
\]

Thus the balanced geometry is the unique full-gap maximizer for every integer `r>=9`, uniformly in the odd multiplier.
