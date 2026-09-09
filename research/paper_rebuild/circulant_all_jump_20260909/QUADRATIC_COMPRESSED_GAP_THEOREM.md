# Quadratic gap for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note strengthens `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md` from an elementary exponential determinant bound to the correct polynomial scale.

Throughout `L>=6` is even, `q>=0`, and `H_{L,q}(z)` is the period-`2L` two-defect Bloch fiber from the general compression theorem. Put

\[
g_{L,q}:=8-\max_{|z|=1}\rho(H_{L,q}(z))^2.
\]

---

## Theorem A — uniform quadratic lower gap

For every even `L>=6` and every `q>=0`,

\[
\boxed{
g_{L,q}\ge\frac{1}{10L^2}.}
\tag{A1}
\]

The constant is intentionally simple rather than optimized.

At the periodic phase `z=1`, write

\[
e_L:=8-\rho(H_{L,q}(1))^2.
\]

This quantity is independent of `q`. If

\[
a:=\arccos\frac13,
\]

then

\[
\boxed{L^2e_L\longrightarrow4a^2
=4\arccos^2\frac13.}
\tag{A2}
\]

Consequently, uniformly in the odd multiplier,

\[
\boxed{
\frac{1}{10L^2}
\le g_{L,q}
\le e_L
=\frac{4\arccos^2(1/3)+o(1)}{L^2}.}
\tag{A3}
\]

Thus the compressed family has the genuine scale

\[
\boxed{g_{L,q}=\Theta(L^{-2})}
\]

with constants independent of `q`.

For `L=4`, the separate exact period-eight theorem is much stronger than (A1), so the quadratic conclusion can be extended to all even `L>=4` after treating that single base case separately.

---

## 1. Full characteristic formula near the threshold

Use the notation from the general compression theorem:

\[
d=\omega^2+\omega^{-2},\qquad e=z+z^{-1},
\]

and

\[
m=\frac{L-4}{2}.
\]

For a squared spectral parameter `y`, define

\[
t_y=\frac{y-d-4}{2},
\qquad
u=U_m(t_y),
\qquad
w=U_{m-1}(t_y).
\tag{1.1}
\]

The same `4 x 4` transfer calculation used at `y=8` gives the complete squared characteristic polynomial

\[
\det(\lambda I-H_{L,q}(z))=P(y,d,e),
\qquad y=\lambda^2,
\]

with

\[
\boxed{
P(y,d,e)=u^2\mathcal A(y,d)+uw\mathcal B(y,d)+\mathcal C(y,d,e),
}
\tag{1.2}
\]

where

\[
\begin{aligned}
\mathcal A(y,d)={}&d^4-2d^2y^2+16d^2y-21d^2-2dy+8d\\
&+y^4-16y^3+83y^2-152y+84,
\end{aligned}
\tag{1.3}
\]

\[
\begin{aligned}
\mathcal B(y,d)={}&d^3+d^2y-4d^2-dy^2+8dy-4d\\
&-y^3+12y^2-36y+16,
\end{aligned}
\tag{1.4}
\]

and

\[
\mathcal C(y,d,e)=d^2+2dy-4d-e+y^2-8y+6.
\tag{1.5}
\]

This formula follows from the monodromy determinant after using

\[
u^2+w^2-(y-d-4)uw=1.
\]

At `y=8`, it reduces to the threshold identity

\[
P(8,d,e)=F_L(d)+d-e\ge16.
\tag{1.6}
\]

---

## 2. Threshold derivative

At `y=8`, abbreviate

\[
A(d)=d^4-21d^2-8d+84,
\]

\[
B(d)=d^3+4d^2-4d-16,
\]

and

\[
C(d,e)=d^2+12d+6-e.
\]

Then

\[
P(8,d,e)=u^2A+uwB+C,
\tag{2.1}
\]

where now

\[
u=U_m((4-d)/2),\qquad w=U_{m-1}((4-d)/2).
\]

Let `u_y,w_y` denote derivatives with respect to `y` through the argument `(y-d-4)/2`. Differentiating (1.2) gives

\[
\begin{aligned}
P_y(8,d,e)={}&2uu_yA+(u_yw+uw_y)B\\
&+u^2A_1+uwB_1+C_1,
\end{aligned}
\tag{2.2}
\]

where

\[
A_1=152-16d^2-2d,
\]

\[
B_1=d^2-8d-36,
\]

\[
C_1=2(d+4).
\tag{2.3}
\]

On `[-2,2]`,

\[
A\ge0,\qquad B\le0,\qquad B_1<0,\qquad A_1\le153,\qquad C_1\le12.
\tag{2.4}
\]

---

## 3. Two elementary lower bounds for the threshold determinant

Put

\[
S(d):=A(d)+B(d).
\]

The factorization

\[
S(d)=(2-d)K(d),
\qquad
K(d)=-d^3-3d^2+11d+34
\tag{3.1}
\]

and

\[
K(d)-8=-(d+2)(d^2+d-13)\ge0
\]

show that

\[
\boxed{S(d)\ge8(2-d).}
\tag{3.2}
\]

Also

\[
5S(d)-3A(d)
=(d-2)^2(2d^2+13d+22)\ge0,
\]

so

\[
\boxed{A(d)\le\frac53S(d).}
\tag{3.3}
\]

Because `(4-d)/2>=1`,

\[
0\le w\le u.
\tag{3.4}
\]

Since `B<=0`, (2.1) gives

\[
P(8,d,e)\ge u^2S(d)+d^2+12d+4,
\tag{3.5}
\]

where we used `e<=2`.

If `d>=0`, the scalar term in (3.5) is at least `4`. If `d<=0`, then `S(d)>=16`, `u>=m+1>=2`, and the scalar term is at least `-16`. Hence in both cases

\[
\boxed{
P(8,d,e)\ge\frac12u^2S(d)+4.
}
\tag{3.6}
\]

We also retain the stronger absolute bound from the compression theorem,

\[
\boxed{P(8,d,e)\ge16.}
\tag{3.7}
\]

---

## 4. Chebyshev logarithmic derivative

All zeros of `U_m` lie in `(-1,1)`. Therefore, for `t>=1`,

\[
\frac{U_m'(t)}{U_m(t)}
=\sum_{j=1}^m\frac{1}{t-\cos(j\pi/(m+1))}
\]

is decreasing in `t`. At `t=1`,

\[
U_m(1)=m+1,
\qquad
U_m'(1)=\frac{m(m+1)(m+2)}3.
\]

Since the argument `t_y` changes with `y` at rate `1/2`,

\[
\boxed{
0\le\frac{u_y}{u}
\le\frac{m(m+2)}6.
}
\tag{4.1}
\]

The same positivity gives `w_y>=0`.

Using (2.2), (2.4), and the negative signs of the two `B` terms,

\[
P_y(8,d,e)
\le \frac{m(m+2)}3u^2A+153u^2+12.
\tag{4.2}
\]

By (3.3) and (3.6), the first term satisfies

\[
\frac{m(m+2)}3u^2A
\le\frac{10}{9}m(m+2)P(8,d,e).
\tag{4.3}
\]

---

## 5. Controlling `u^2/P`

Let

\[
\delta=2-d.
\]

We claim

\[
\boxed{
\frac{u^2}{P(8,d,e)}
\le\frac{(m+1)^2}{4}.
}
\tag{5.1}
\]

If

\[
\delta\ge\frac1{(m+1)^2},
\]

then (3.2) and (3.6) give

\[
P(8,d,e)
\ge4\delta u^2
\ge\frac{4u^2}{(m+1)^2}.
\]

Now suppose

\[
\delta<\frac1{(m+1)^2}.
\]

Write

\[
1+\delta/2=\cosh\theta.
\]

Since `cosh(theta)>=1+theta^2/2`,

\[
0\le\theta<\frac1{m+1}.
\]

The hyperbolic representation gives

\[
u=\frac{\sinh((m+1)\theta)}{\sinh\theta}.
\]

Using `sinh(theta)>=theta`, `sinh x<=x cosh x`, and `(m+1)theta<1`,

\[
u<2(m+1).
\]

Together with (3.7), this again gives (5.1).

---

## 6. Trace-resolvent bound and the quadratic gap

Combining (4.2)--(4.3) with (5.1) and `P>=16`, and using `m>=1`,

\[
\begin{aligned}
\frac{P_y(8,d,e)}{P(8,d,e)}
&\le\frac{10}{9}m(m+2)
+\frac{153}{4}(m+1)^2+\frac34\\
&<40(m+1)^2.
\end{aligned}
\tag{6.1}
\]

By the general compression theorem all squared roots satisfy

\[
0\le y_j<8.
\]

Hence

\[
\frac{P_y(8)}{P(8)}
=\sum_{j=1}^{L}\frac1{8-y_j}
\ge\frac1{8-\max_jy_j}.
\]

Therefore every Bloch phase satisfies

\[
8-\rho(H_{L,q}(z))^2
\ge\frac1{40(m+1)^2}
=\frac1{10(L-2)^2}
>\frac1{10L^2}.
\tag{6.2}
\]

Taking the worst phase proves (A1).

---

## 7. Exact periodic-phase quantization

At `z=1`, the fiber is independent of `q`. Put

\[
r=L/2.
\]

The factorization from the general compression proof is

\[
\det(\lambda I-H_{L,q}(1))
=p_r(y)(p_r(y)+4),
\qquad y=\lambda^2,
\tag{7.1}
\]

where

\[
\begin{aligned}
p_r(y)={}&
U_{r-2}\!\left(\frac{y-6}{2}\right)(y^2-8y+6)\\
&-U_{r-3}\!\left(\frac{y-6}{2}\right)(y-2)-2.
\end{aligned}
\tag{7.2}
\]

Write the top root as

\[
y=6+2\cos\theta,
\qquad 0<\theta<\frac{\pi}{2r}.
\]

Using

\[
U_j(\cos\theta)=\frac{\sin((j+1)\theta)}{\sin\theta},
\]

the equation `p_r(y)=0` reduces first to

\[
(2+\cos\theta)\sin(r\theta)
-3\sin((r-1)\theta)-\sin\theta=0,
\]

and then to the compact Robin-type quantization law

\[
\boxed{
3\cos(r\theta)
+2\tan(\theta/2)\sin(r\theta)=1.
}
\tag{7.3}
\]

The left side is strictly decreasing on `(0,pi/(2r))`. Indeed, after differentiation and division by `sin(r theta)>0`, use

\[
2r\tan(\theta/2)\cot(r\theta)
\le \frac{2\tan(\theta/2)}{\tan\theta}
\le1
\]

and `sec^2(theta/2)<=2` to obtain a strictly negative derivative for `r>=2`.

At `theta=0` the limiting left side is `3`, while at `theta=pi/(2r)` it equals `2tan(pi/(4r))<1`. Hence (7.3) has a unique solution `theta_r` in that interval, and it gives the top squared eigenvalue.

---

## 8. Endpoint asymptotic constant

Put

\[
a_r=r\theta_r.
\]

Equation (7.3) becomes

\[
3\cos a_r
+2\tan\left(\frac{a_r}{2r}\right)\sin a_r=1.
\tag{8.1}
\]

Since `0<a_r<pi/2`, compactness and (8.1) imply that every limit point `a_*` satisfies

\[
3\cos a_*=1.
\]

Thus

\[
\boxed{
a_r\longrightarrow a:=\arccos(1/3).}
\tag{8.2}
\]

The periodic-phase squared gap is

\[
e_L=8-(6+2\cos\theta_r)
=4\sin^2(\theta_r/2).
\]

Since `L=2r`,

\[
L^2e_L
=16r^2\sin^2\left(\frac{a_r}{2r}\right)
\longrightarrow4a^2.
\]

This proves (A2). A first correction follows directly from (8.1):

\[
a_r=a+\frac{a}{3r}+O(r^{-2}),
\tag{8.3}
\]

although this refinement is not needed for the quadratic-scale theorem.

---

## 9. Arithmetic form

If `v_2(s)=k>=2`, choose

\[
L=2^k.
\]

Then the compressed two-defect phase has period `2^{k+1}` and

\[
\boxed{
8-R_s^{\mathrm{comp}}
\ge\frac{1}{10\,4^k}.
}
\tag{9.1}
\]

At its periodic Bloch phase the natural comparison scale is

\[
\frac{4\arccos^2(1/3)}{4^k}.
\]

Thus the short-period theorem is now quantitatively arithmetic: the gap is controlled by the `2`-adic scale `2^k`, while the odd part of the jump does not enter the bounds.