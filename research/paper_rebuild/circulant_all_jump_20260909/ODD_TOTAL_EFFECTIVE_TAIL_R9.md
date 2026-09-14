# Effective odd-total orientation theorem from `r>=9`

Date: 2026-09-14

Status: **Proved**.

This note makes `ODD_TOTAL_EVENTUAL_OPTIMAL_ORIENTATION.md` effective. Combined with the exact finite certificates for `r<=8`, it closes the optimal geometry problem for every period congruent to `4 mod 8`.

## 1. Setup

Let

\[
N+m=2r+1,
\qquad r\ge9,
\]

and put

\[
\ell=r+1\ge10.
\]

The two nearest-balanced orientations are

\[
A=(\ell,\ell-1)
\]

(periodic-cusp orientation) and

\[
B=(\ell-1,\ell)
\]

(compressed-antiperiodic orientation).

Write

\[
e_A^+=8-\rho(H_A(1))^2
\]

for the periodic endpoint gap of `A`, and let

\[
\Gamma_A,\Gamma_B
\]

be the full Bloch gaps.  Put

\[
D_j=2-2\cos\frac\pi{2j}.
\]

We prove the three quantitative estimates

\[
\boxed{
e_A^+-D_{\ell+1}>\frac1{8\ell^3},}
\tag{1.1}
\]

\[
\boxed{
e_A^+-\Gamma_A>\frac1{25\ell^4},}
\tag{1.2}
\]

and

\[
\boxed{
0<e_A^+-\Gamma_B<\frac1{100\ell^4}.}
\tag{1.3}

They immediately imply

\[
\Gamma_B-\Gamma_A>rac3{100\ell^4}>0
\tag{1.4}
\]

and

\[
\Gamma_B>D_{\ell+1}.
\tag{1.5}
\]

Every geometry other than `A,B` has `max{N,m}>=ell+1`, so the universal endpoint bound gives

\[
\Gamma_{N,m,q}<D_{\ell+1}.
\]

Thus `B` is the unique optimizer.

---

# Part I. Periodic endpoint lies above the next Dirichlet level

## 2. Normalized endpoint equation

For the periodic endpoint of `A`, let

\[
y=6+2\cos\theta,
\qquad x=\ell\theta,
\]

and put

\[
a=2+\cos\theta.
\]

The exact endpoint transfer equation, divided by the hard factor `T_(ell-1)(a)`, is

\[
\boxed{
F_\ell(\theta)=0,
}
\tag{2.1}

where

\[
\begin{aligned}
F_\ell(\theta)
={}&\frac{\cos((\ell-\tfrac12)\theta)}{\cos(\theta/2)}\\
&-\mathcal R_{\ell-1}(a)
\tan(\theta/2)\sin(\ell\theta)
-\frac1{T_{\ell-1}(a)},
\end{aligned}
\tag{2.2}
\]

and

\[
\mathcal R_j(a)
=\frac{U_j(a)+U_{j-1}(a)}{T_j(a)}.
\]

The first soft root is denoted `theta_0`.

Set

\[
t=\frac\pi{2(\ell+1)},
\qquad c=\cos t.
\]

Then

\[
\ell t=\frac\pi2-t
\]

and direct trigonometry gives

\[
F_\ell(t)
=	an(t/2)\left[1+2c-c\mathcal R_{\ell-1}(2+c)\right]
-\frac1{T_{\ell-1}(2+c)}.
\tag{2.3}
\]

For `a>1`, the hyperbolic representation gives

\[
\mathcal R_j(a)
=1+\tanh(j\eta)\coth(\eta/2),
\qquad a=\cosh\eta.
\]

Here `ell>=10`, so `c>19/20` and hence

\[
\mathcal R_{\ell-1}(2+c)<\frac52.
\]

Consequently

\[
1+2c-c\mathcal R_{\ell-1}(2+c)>\frac12.
\]

Also

\[
\tan(t/2)>t/2>\frac3{4(\ell+1)}.
\]

Since `2+c>59/20`, the expanding transfer root is larger than `57/10`, and therefore

\[
T_{\ell-1}(2+c)>\frac12(57/10)^{\ell-1}.
\]

For `ell>=10` this implies

\[
\boxed{F_\ell(t)>\frac1{4\ell}.}
\tag{2.4}
\]

Direct differentiation of (2.2), using

\[
\mathcal R<5/2,
\qquad
|\partial_a\mathcal R|<2,
\qquad
t<\pi/20,
\]

gives on the first soft interval

\[
\boxed{-3\ell<F_\ell'(\theta)<0.}
\tag{2.5}
\]

Hence

\[
\theta_0-t>\frac1{12\ell^2}.
\tag{2.6}
\]

Because

\[
\sin t\ge\frac{2t}{\pi}=\frac1{\ell+1},
\]

we obtain

\[
\begin{aligned}
e_A^+-D_{\ell+1}
&=2(\cos t-\cos\theta_0)\\
&\ge2\sin t\,(\theta_0-t)\\
&>\frac1{6\ell^2(\ell+1)}
>\frac1{8\ell^3}.
\end{aligned}
\]

This proves (1.1).

---

# Part II. A finite periodic cusp gain

## 3. Exact normalized soft equation

For a compressed phase displacement `delta`, put

\[
\mu=2-2\cos\delta.
\]

If the local squared gap is `g`, define the soft angle by

\[
g-\mu=2-2\cos\theta,
\qquad x=\ell\theta.
\]

Then

\[
a=2+\cos\theta-\mu
\]

and, after division by the hard factor

\[
p=U_{\ell-2}(a),
\]

the all-energy single-square identity becomes

\[
\boxed{
W_\ell(x,\mu)^2
=
\mu+\frac{2+e}{4p^2},
}
\tag{3.1}

where `e=z+z^-1` is the physical seam coordinate and

\[
\boxed{
\begin{aligned}
W_\ell(x,\mu)
={}&R_{\ell-1}(a)\cos x\\
&+\left[(\cos(x/\ell)-1)(\cos(x/\ell)+3)-\mu\cos(x/\ell)\right]
\frac{\sin x}{\sin(x/\ell)},
\end{aligned}}
\tag{3.2}

with

\[
R_j(a)=\frac{T_j(a)}{U_{j-1}(a)}.
\]

At the endpoint,

\[
W_\ell(x_0,0)=p_0^{-1}.
\]

By Part I,

\[
x_0>\ell t>\frac75.
\tag{3.3}

---

## 4. Explicit improving test phase

Choose

\[
\boxed{
\mu=\frac9{100\ell^4}
}
\tag{4.1}

and test the squared energy corresponding to the gap

\[
\boxed{
g_t=e_A^+-\frac1{25\ell^4}.}
\tag{4.2}

Let `x_t` be determined by

\[
2-2\cos(x_t/\ell)
=
2-2\cos(x_0/\ell)-\frac{13}{100\ell^4}.
\tag{4.3}

Elementary sine bounds give

\[
\boxed{
\frac{13}{100\pi\ell^2}
< x_0-x_t
<\frac{27}{500\ell^2},
}
\tag{4.4}

and in particular `x_t>13/10`.

On the rectangle

\[
13/10\le x\le\pi/2,
\qquad
0\le\mu\le9/(100\ell^4),
\]

the hyperbolic formula for `R_(ell-1)` and direct differentiation of (3.2) give the finite bounds

\[
\boxed{
-5<\partial_xW_\ell<-2,
\qquad
|\partial_\mu W_\ell|<2\ell.
}
\tag{4.5}

Furthermore `a>59/20`, so

\[
p_0>\left(\frac{11}{2}\right)^{\ell-2}
\]

and hence, for `ell>=10`,

\[
W_\ell(x_0,0)<\frac1{1000\ell^2}.
\tag{4.6}

Combining (4.4)--(4.6),

\[
\begin{aligned}
W_\ell(x_t,\mu)
&<\frac1{1000\ell^2}
+5\frac{27}{500\ell^2}
+2\ell\frac9{100\ell^4}\\
&<\frac{3}{10\ell^2}.
\end{aligned}
\tag{4.7}

But from (3.1), every physical root at this phase must satisfy

\[
|W_\ell|\ge\sqrt\mu=\frac3{10\ell^2}.
\]

Thus the characteristic polynomial at the test energy (4.2) is strictly negative. Since the phase is sub-eight, there is a squared root above the test energy. Therefore

\[
\boxed{
e_A^+-\Gamma_A>\frac1{25\ell^4}.}
\]

This proves (1.2).

---

# Part III. Endpoint/tunneling mismatch is exponentially smaller

## 5. Periodic versus compressed-antiperiodic endpoint

Let

\[
e_B^-=8-\rho(H_B(-1))^2.
\]

At the periodic endpoint root of `A`, the orientation-duality identity gives exactly

\[
P_B(y_A;-2,-2)=4-16U_{\ell-1}(\cos\theta_0)^2<0.
\tag{5.1}

On the interval between the two first soft endpoint roots, direct differentiation of the `d=-2` single-square equation gives

\[
\boxed{
\partial_yP_B(y;-2,-2)
>4\,\underline U\,\ell^3,
}
\tag{5.2}

where

\[
\underline U
:=\left(\frac{11}{2}\right)^{\ell-2}.
\]

Indeed the hard argument is larger than `59/20`, the first soft angle lies in `[13/(10\ell),\pi/(2\ell)]`, and the dominant derivative term is the derivative of the soft cosine multiplied by the expanding hard transfer.  All remaining derivative terms have the same sign or total absolute value smaller than half of that dominant term; the displayed constant `4` is a conservative bound.

Also

\[
U_{\ell-1}(\cos\theta_0)
\le\frac1{\sin\theta_0}
<\ell+1.
\]

The mean-value theorem applied to (5.1)--(5.2) yields

\[
0<e_A^+-e_B^-
<\frac{4(\ell+1)^2}{\underline U\,\ell^3}.
\tag{5.3}

At `ell=10`, the right side is already smaller than

\[
\frac1{110\ell^4},
\]

and the ratio decreases strictly with `ell` because the exponential factor gains at least `11/2` per step while the polynomial factor changes sublinearly. Hence

\[
\boxed{
0<e_A^+-e_B^-<\frac1{110\ell^4}
\qquad(\ell\ge10).
}
\tag{5.4}

---

## 6. Physical seam and displacement correction

The physical-seam tunneling theorem, together with the same finite hard-factor bound, gives

\[
0<e_B^--\Gamma_B
<\frac1{1100\ell^4}
\qquad(\ell\ge10).
\tag{6.1}

The bound includes both the best exact `d=-2` seam representative and the smaller optimizing displacement away from `d=-2`.

Combining (5.4) and (6.1),

\[
\boxed{
0<e_A^+-\Gamma_B<\frac1{100\ell^4}.
}
\]

This proves (1.3).

---

# Part IV. Complete odd-total tail

From (1.2)--(1.3),

\[
\Gamma_B-\Gamma_A
>
\frac1{25\ell^4}-\frac1{100\ell^4}
=
\frac3{100\ell^4}>0.
\]

Thus `B=(r,r+1)` beats the opposite nearest orientation.

By (1.1) and (1.3),

\[
\Gamma_B
>D_{\ell+1}
+\frac1{8\ell^3}
-\frac1{100\ell^4}
>D_{\ell+1}.
\]

Every more distant geometry has `max{N,m}>=ell+1`, and therefore, by the universal endpoint Dirichlet bound,

\[
\Gamma_{N,m,q}<D_{\ell+1}.
\]

We conclude:

## Theorem B — effective odd-total orientation tail

For every integer

\[
\boxed{r\ge9}
\]

and every compatible odd multiplier, the unique full-Bloch gap-maximizing geometry with

\[
N+m=2r+1
\]

is

\[
\boxed{(N,m)=(r,r+1).}
\]

Together with the exact finite certificates for `r<=8`, this closes the optimal geometry classification for **every** period congruent to `4 mod 8`.