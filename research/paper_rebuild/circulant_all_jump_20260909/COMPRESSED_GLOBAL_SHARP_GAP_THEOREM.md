# Compressed two-defect family: exact discriminant and sharp global gap asymptotic

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It concerns the explicit compressed two-defect family and is independent of the finite-global minimization problem over all signings.

This theorem strengthens `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md` and `COMPRESSED_ENDPOINT_ROBIN_ASYMPTOTIC.md`. The former proves strict sub-eight spectrum for every even half-period `L>=4`; the latter identifies the sharp periodic-fiber endpoint constant. Here we prove that the same constant governs the **full continuous Bloch maximum**, uniformly in the odd jump multiplier.

---

## 1. Setup and statement

Let `L>=6` be even, let

\[
s=L(2q+1),\qquad q\ge0,
\]

and use the period-`2L` two-defect Hamilton-gauge word from the general compression theorem. Let

\[
R_{L,q}:=\max_{|z|=1}\rho(H_{L,q}(z))^2,
\qquad
g_{L,q}:=8-R_{L,q}.
\]

Put

\[
\alpha:=\arccos\frac13.
\]

### Theorem A — sharp global compressed-family gap

Uniformly with respect to the odd multiplier in the following sequential sense: for every sequence of even `L_j->infinity` and every sequence `q_j>=0`,

\[
\boxed{
L_j^2 g_{L_j,q_j}
\longrightarrow
4\alpha^2
=4\arccos^2\frac13
=6.0610443485\ldots .
}
\tag{1.1}
\]

Thus the compressed two-defect family has the sharp global gap law

\[
\boxed{
g_{L,q}\sim \frac{4\arccos^2(1/3)}{L^2}}
\tag{1.2}
\]

uniformly over arbitrary odd jump multipliers.

If `z_L=e^{it_L}` is any Bloch phase attaining `R_{L,q}`, define

\[
d_L=z_L^{2q+1}+z_L^{-(2q+1)},
\qquad
e_L=z_L+z_L^{-1}.
\]

Then every maximizing sequence also satisfies the localization laws

\[
\boxed{
L^2(2-d_L)\longrightarrow0,
\qquad e_L\longrightarrow2.
}
\tag{1.3}
\]

Thus the global optimizer asymptotically approaches both the internal periodic phase and the ordinary periodic Bloch boundary, even though exact finite-`L` equality `z_L=1` is not needed for the theorem.

---

## 2. Exact two-phase Floquet discriminant

Choose `eta` with `eta^2=z` and set

\[
\omega=z^q\eta.
\]

Define the real phase variables

\[
d:=\omega^2+\omega^{-2}
=z^{2q+1}+z^{-(2q+1)}\in[-2,2],
\]

\[
e:=z+z^{-1}\in[-2,2].
\tag{2.1}
\]

Let

\[
y=\lambda^2,
\qquad
m=\frac{L-4}{2},
\qquad
t=\frac{y-d-4}{2},
\]

and put

\[
u=U_m(t),
\qquad
w=U_{m-1}(t),
\tag{2.2}
\]

with `U_{-1}=0`.

The signed-reflection chirality theorem makes the characteristic polynomial even in `lambda`. The same four-dimensional transfer monodromy used in the general compression theorem gives more than the threshold identity: after using

\[
u^2+w^2-(y-d-4)uw=1,
\tag{2.3}
\]

the **full** characteristic equation is

\[
\boxed{
\det(\lambda I-H_{L,q}(z))
=G_L(y,d)-e.
}
\tag{2.4}
\]

Here

\[
\boxed{
G_L(y,d)=A(y,d)uw+B(y,d)w^2+C(y,d),
}
\tag{2.5}
\]

where

\[
\begin{aligned}
A(y,d)={}&(-d^2+y^2-8y+10)\\
&\times(d^3-d^2y+4d^2-dy^2+8dy-12d\\
&\hspace{33mm}+y^3-12y^2+40y-32),
\end{aligned}
\tag{2.6}
\]

\[
\boxed{
B(y,d)
=-(-d^2-d+y^2-9y+14)
(-d^2+d+y^2-7y+6),
}
\tag{2.7}
\]

and

\[
\boxed{
\begin{aligned}
C(y,d)={}&d^4-2d^2y^2+16d^2y-20d^2+4d\\
&+y^4-16y^3+84y^2-160y+90.
\end{aligned}}
\tag{2.8}
\]

At `y=8`, (2.4) reduces exactly to the previously proved threshold formula

\[
G_L(8,d)-e=F_L(d)+d-e.
\]

### Proof of the discriminant identity

Use the folded two-component chain and the transfer matrices

\[
T(A)=\begin{pmatrix}A&-I_2\\I_2&0\end{pmatrix}
\]

from the general compression theorem. The generic transfer power is

\[
T(A_g)^{L-3}
=
\begin{pmatrix}
u A_g&-(u+w)I_2\\(u+w)I_2&-wA_g\end{pmatrix},
\]

where in this display `\nu` denotes the scalar `u` from (2.2), not a new parameter. Substituting this into the fixed `4 x 4` monodromy determinant and imposing (2.3), all powers of the boundary square root cancel except the reciprocal pair `eta^2,eta^{-2}`. Their total contribution is

\[
-(\eta^2+\eta^{-2})=-e.
\]

The remaining real expression is exactly (2.5)--(2.8). This is a fixed-size symbolic determinant identity; no limiting argument is involved.

---

## 3. A localization lemma for near-eight roots

Write

\[
\delta:=8-y\ge0,
\qquad
h:=2-d\in[0,4].
\tag{3.1}
\]

Then

\[
t=1+\frac{h-\delta}{2}.
\tag{3.2}
\]

### Lemma B — internal phase localization

Fix `M<infinity`. Suppose `L_j->infinity`, `\delta_j<=M/L_j^2`, and

\[
G_{L_j}(8-\delta_j,2-h_j)=e_j
\]

with `e_j in[-2,2]`. Then

\[
\boxed{L_j^2h_j=O(1).}
\tag{3.3}
\]

#### Proof

Assume to the contrary that along a subsequence

\[
L^2h\to\infty.
\]

Since `\delta=O(L^{-2})`, this gives `\delta/h->0`, and hence eventually `h>\delta`. Thus `t>=1`, so

\[
u\ge w\ge0,
\qquad
w=U_{m-1}(t)\ge m.
\tag{3.4}
\]

Rewrite (2.6)--(2.8) in the variables `(\delta,h)`. At `\delta=0`, the two coefficients multiplying `uw` and `w^2` are

\[
A_0(h)=h(h^2-4h-6)(h^2-2h-16)>0,
\tag{3.5}
\]

\[
B_0(h)=-h(h-5)(h^2-3h-12)<0
\tag{3.6}
\]

for `0<h<=4`, and

\[
A_0(h)+B_0(h)
=h\bigl(h^4-7h^3-6h^2+73h+36\bigr).
\tag{3.7}
\]

The quartic in parentheses is uniformly positive on `[0,4]`. Indeed, after putting `h=4v`, `0<=v<=1`, its degree-four Bernstein coefficients are

\[
36,\quad109,\quad166,\quad95,\quad40,
\]

all positive. Hence

\[
A_0(h)+B_0(h)\ge36h.
\tag{3.8}
\]

Because `\delta/h->0` and the coefficients are polynomial, (3.5)--(3.8) imply for all sufficiently large indices

\[
A>0,
\qquad B<0,
\qquad A+B\ge18h.
\tag{3.9}
\]

Using `u/w>=1`,

\[
Auw+Bw^2
=w^2\left(A\frac uw+B\right)
\ge(A+B)w^2
\ge18h m^2.
\tag{3.10}
\]

The remaining polynomial `C(y,d)` is uniformly bounded for `y` in a fixed neighborhood of `8` and `d in[-2,2]`. Since `hL^2->infinity`, the right side of (3.10) tends to `+infinity`. Thus

\[
G_L(y,d)\to+\infty,
\]

contradicting `G_L(y,d)=e in[-2,2]`. This proves (3.3).

---

## 4. Continuum Chebyshev scaling

Suppose now that

\[
L^2\delta\to a,
\qquad
L^2h\to b
\tag{4.1}
\]

along a subsequence. By Lemma B, `a,b` are finite whenever `\delta=O(L^{-2})` is a Bloch root near eight.

From (3.2),

\[
t=1+\frac{b-a}{2L^2}+o(L^{-2}).
\]

The standard trigonometric/hyperbolic representation of `U_m`, with `m=(L-4)/2`, yields

\[
\frac uL,\frac wL\longrightarrow S(a,b),
\tag{4.2}
\]

where

\[
S(a,b)=
\begin{cases}
\displaystyle
\frac{\sin(\frac12\sqrt{a-b})}{\sqrt{a-b}},&a>b,\\[3mm]
\displaystyle\frac12,&a=b,\\[3mm]
\displaystyle
\frac{\sinh(\frac12\sqrt{b-a})}{\sqrt{b-a}},&b>a.
\end{cases}
\tag{4.3}
\]

For example, if `b>a`, write `t=\cosh\kappa_L`; then

\[
L\kappa_L\to\sqrt{b-a},
\qquad
U_m(t)=\frac{\sinh((m+1)\kappa_L)}{\sinh\kappa_L},
\]

which gives the third line. The trigonometric case is identical with `\kappa_L=i\theta_L`.

Expanding the exact coefficients (2.6)--(2.8) under (4.1) gives

\[
A(y,d)=\frac{-120a+96b}{L^2}+O(L^{-4}),
\tag{4.4}
\]

\[
B(y,d)=\frac{84a-60b}{L^2}+O(L^{-4}),
\tag{4.5}
\]

\[
C(y,d)=34+O(L^{-2}).
\tag{4.6}
\]

Therefore (2.5) and (4.2) imply the limiting discriminant

\[
G_L(y,d)\longrightarrow
34+36(b-a)S(a,b)^2.
\tag{4.7}
\]

Equivalently,

\[
\boxed{
G_\infty(a,b)=
\begin{cases}
16+18\cos\sqrt{a-b},&a>b,\\
34,&a=b,\\
16+18\cosh\sqrt{b-a},&b>a.
\end{cases}}
\tag{4.8}
\]

This limiting scalar discriminant is the continuum mechanism behind the sharp constant.

---

## 5. Proof of the sharp global limit

For each `L,q`, choose a Bloch phase `z_L` attaining `R_{L,q}` and set

\[
y_L=R_{L,q}=8-g_{L,q}.
\]

The periodic phase `z=1` is admissible. By `COMPRESSED_ENDPOINT_ROBIN_ASYMPTOTIC.md`,

\[
8-\rho(H_L(1))^2
=\frac{4\alpha^2}{L^2}+O(L^{-3}).
\]

Therefore

\[
0<g_{L,q}
\le\frac{4\alpha^2}{L^2}+O(L^{-3}),
\tag{5.1}
\]

uniformly in `q`. Hence

\[
a_L:=L^2g_{L,q}
\]

is bounded and

\[
\limsup a_L\le4\alpha^2.
\tag{5.2}
\]

At the maximizing phase define

\[
h_L=2-d_L,
\qquad
e_L=z_L+z_L^{-1}.
\]

The characteristic equation (2.4) gives

\[
G_L(8-g_{L,q},d_L)=e_L\in[-2,2].
\tag{5.3}
\]

Lemma B shows that

\[
b_L:=L^2h_L
\]

is bounded. Pass to an arbitrary convergent subsequence

\[
a_L\to a,
\qquad b_L\to b,
\qquad e_L\to e_*\in[-2,2].
\]

If `b>=a`, then (4.8) gives

\[
e_*\ge34,
\]

a contradiction. Hence `a>b`, and (4.8) gives

\[
e_*=16+18\cos\sqrt{a-b}\le2.
\tag{5.4}
\]

Now

\[
\alpha=\arccos\frac13
\]

satisfies

\[
\cos(2\alpha)=2\cos^2\alpha-1=-\frac79.
\tag{5.5}
\]

By (5.2),

\[
0\le\sqrt{a-b}\le\sqrt a\le2\alpha<\pi.
\]

On `[0,2\alpha]` cosine is strictly decreasing. Inequality (5.4) is equivalent to

\[
\cos\sqrt{a-b}\le-\frac79=\cos(2\alpha),
\]

so

\[
\sqrt{a-b}\ge2\alpha.
\]

Together with the preceding upper bounds, every inequality must be an equality:

\[
\boxed{
a=4\alpha^2,
\qquad b=0,
\qquad e_*=2.}
\tag{5.6}
\]

Since every convergent subsequence has the same limit, the full sequences satisfy

\[
L^2g_{L,q}\to4\alpha^2,
\qquad
L^2(2-d_L)\to0,
\qquad
e_L\to2.
\]

This proves Theorem A.

---

## 6. Interpretation

The compressed family now has a complete leading-order global Bloch theory:

\[
\boxed{
8-R_{L,q}
\sim
\frac{4\arccos^2(1/3)}{L^2},
}
\]

uniformly over the odd multiplier `2q+1`.

The constant comes from the limiting Robin equation

\[
3\cos x=1,
\]

not from the `\pi/2` quantization that produced the `\pi^2` constant in the older period-`4s` family. The arithmetic period compression therefore does more than shorten the cell: it produces a genuinely different spectral boundary condition and a different sharp constant.

For the `2`-adic specialization `L=2^{v_2(s)}`, this gives a sharp asymptotic in the compressed period scale. Since `L` depends only on the `2`-adic part of the jump, the resulting gap can be dramatically larger than the old `Theta(s^{-2})` gap when the odd part of `s` is large.
