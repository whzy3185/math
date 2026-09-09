# General two-defect compression theorem

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It concerns explicit periodic phases and makes no assertion about minimization over all finite signings.

This theorem closes the general `2`-adic short-period problem suggested by the first three arithmetic layers. The earlier period-eight and period-sixteen calculations become special cases of one transfer-matrix argument.

---

## 1. Statement

Let `L>=4` be even. On residues modulo `2L`, define the two-defect local flux word

\[
Q_0=Q_2=1,\qquad Q_j=-1\quad(j\ne0,2),
\]

and choose the Hamilton-gauge lift with `tau_0=1`. Thus

\[
\tau_0=\tau_1=1,\qquad
\tau_2=\tau_3=-1,\qquad
\tau_j=(-1)^j\quad(4\le j<2L).
\tag{1.1}
\]

Let

\[
s=L(2q+1),\qquad q\ge0,
\tag{1.2}
\]

and consider the `2L`-periodic signed step operator

\[
(A_{L,q}x)_j=x_{j-1}+x_{j+1}
+\tau_{j-s}x_{j-s}+\tau_jx_{j+s}.
\tag{1.3}
\]

For `|z|=1`, let `H_{L,q}(z)` be its Bloch fiber under

\[
x_{j+2L}=zx_j,
\]

and put

\[
R_{L,q}:=\max_{|z|=1}\rho(H_{L,q}(z))^2.
\]

### Theorem A — general compressed two-defect phase

For every even `L>=4` and every `q>=0`,

\[
\boxed{R_{L,q}<8.}
\tag{1.4}
\]

In fact the following completely explicit, uniform-in-`q` bound holds:

\[
\boxed{
8-R_{L,q}\ge \frac{16}{8^{L-1}}.
}
\tag{1.5}
\]

The exponential constant is deliberately elementary and is not expected to be sharp. Its role is to make strict positivity quantitative without hiding any compactness step.

### Corollary A.1 — `2`-adic period compression

Let `s` be even and suppose `v_2(s)=k>=2`. Put

\[
L=2^k,
\qquad
n=s/L\quad\text{(odd)}.
\]

Then the two-defect word of period

\[
\boxed{2L=2^{k+1}}
\]

gives a continuous squared Bloch edge strictly below `8`.

Thus for all even jumps divisible by four, the required period depends only on the `2`-adic valuation of `s`, not on the odd part of `s`.

Together with the separate fixed-period-eight theorem for `v_2(s)=1`, every even jump now has an explicit short periodic sub-eight phase whose period is controlled purely by its `2`-adic scale.

---

## 2. Fold to an `L`-site two-component chain

Fix a Bloch phase `z` and choose `eta` with

\[
\eta^2=z,
\qquad |\eta|=1.
\]

Pair the coordinates `j` and `j+L`, `0<=j<L`. Since

\[
s=L+2Lq,
\]

the two long-jump contributions between the pair `j,j+L` have combined coefficient

\[
c_j=\tau_jz^q+\tau_{j+L}z^{-(q+1)}.
\tag{2.1}
\]

Because `L` is even and `j+L>=4`,

\[
\tau_{j+L}=(-1)^j.
\]

Define

\[
\omega=z^q\eta,
\qquad
\omega^2=z^{2q+1}.
\tag{2.2}
\]

First multiply the second coordinate in every pair by `eta^{-1}`, and then conjugate the `j`th pair by `sigma_z^j`, where

\[
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Write

\[
\omega=e^{i\beta},\qquad c=\cos\beta,\qquad r=\sin\beta.
\]

After this unitary gauge, the fiber is an `L`-site block Jacobi matrix. Every interior nearest-neighbor block is `sigma_z`; the onsite blocks are

\[
V_j=\begin{cases}
2r\,\sigma_y,&j=1,2,\\
2c\,\sigma_x,&j\ne1,2,
\end{cases}
\tag{2.3}
\]

and the closing block from site `L-1` to site `0` is

\[
C=i\eta\sigma_y.
\tag{2.4}
\]

The two exceptional onsite blocks are exactly the two local flux defects. All dependence on the odd multiplier `2q+1` is compressed into the single angle `beta` through `omega^2=z^{2q+1}`.

---

## 3. Four-dimensional transfer monodromy

For an eigenvector with two-component site values `psi_j`, the interior equation is

\[
\sigma_z\psi_{j-1}+V_j\psi_j+\sigma_z\psi_{j+1}=\lambda\psi_j.
\]

Set

\[
T(A)=\begin{pmatrix}A&-I_2\\I_2&0\end{pmatrix},
\qquad
A_j=\sigma_z(\lambda I_2-V_j).
\tag{3.1}
\]

For the generic and defect sites respectively,

\[
A_g=\lambda\sigma_z-2ic\sigma_y,
\qquad
A_d=\lambda\sigma_z+2ir\sigma_x.
\tag{3.2}
\]

They satisfy the scalar-square identities

\[
A_g^2=(\lambda^2-4c^2)I_2,
\qquad
A_d^2=(\lambda^2-4r^2)I_2.
\tag{3.3}
\]

The boundary block (2.4) is equivalent to

\[
\psi_L=\eta\sigma_x\psi_0,
\qquad
\psi_{L-1}=-\eta\sigma_x\psi_{-1}.
\]

Hence, with

\[
J=\operatorname{diag}(\sigma_x,-\sigma_x),
\]

the boundary condition is

\[
\binom{\psi_L}{\psi_{L-1}}
=\eta J\binom{\psi_0}{\psi_{-1}}.
\tag{3.4}
\]

Because the onsite sequence is generic, defect, defect, then generic for the remaining `L-3` sites, the full transfer monodromy is

\[
M(\lambda)=T(A_g)^{L-3}T(A_d)^2T(A_g).
\tag{3.5}
\]

The Bloch characteristic determinant is related to this fixed `4 x 4` monodromy by

\[
\boxed{
\det(\lambda I_{2L}-H_{L,q}(z))
=-\eta^{-2}\det(M(\lambda)-\eta J).
}
\tag{3.6}
\]

This identity follows directly by propagating (3.1) and imposing (3.4). It is the dimensional compression behind the theorem.

---

## 4. Exact threshold determinant

From now on put

\[
\lambda^2=8.
\]

Define the two real phase variables

\[
d=\omega^2+\omega^{-2}\in[-2,2],
\qquad
e=z+z^{-1}\in[-2,2].
\tag{4.1}
\]

Then

\[
4c^2=d+2,
\qquad
4r^2=2-d,
\]

and therefore

\[
A_g^2=(6-d)I_2.
\tag{4.2}
\]

Let

\[
m=\frac{L-4}{2},
\qquad
t=\frac{4-d}{2}\in[1,3],
\]

and set

\[
u=U_m(t),
\qquad
w=U_{m-1}(t),
\tag{4.3}
\]

with the convention `U_{-1}=0`.

For the matrix continuants

\[
D_{-1}=0,\quad D_0=I_2,\quad D_j=A_gD_{j-1}-D_{j-2},
\]

the scalar-square identity (4.2) gives

\[
D_{2m+1}=uA_g,
\qquad
D_{2m}=(u+w)I_2,
\qquad
D_{2m-1}=wA_g.
\tag{4.4}
\]

Consequently

\[
T(A_g)^{L-3}
=
\begin{pmatrix}
u A_g&-(u+w)I_2\\(u+w)I_2&-wA_g\end{pmatrix}.
\tag{4.5}
\]

The Chebyshev identity gives

\[
\boxed{
u^2+w^2-(4-d)uw=1.}
\tag{4.6}
\]

Substitute (4.5) into the `4 x 4` determinant in (3.6), use (4.6), and collect the two boundary monomials `eta^2,eta^{-2}`. The result is

\[
\boxed{
P_{L,q,z}(8)=F_L(d)+d-e,
}
\tag{4.7}
\]

where

\[
\det(\lambda I-H_{L,q}(z))=P_{L,q,z}(\lambda^2)
\]

(the evenness follows independently from the signed-reflection chirality theorem), and

\[
\boxed{
F_L(x)=u_x^2A(x)+u_xw_xB(x)+C(x)
}
\tag{4.8}
\]

with

\[
u_x=U_m\!\left(\frac{4-x}{2}\right),
\qquad
w_x=U_{m-1}\!\left(\frac{4-x}{2}\right),
\]

\[
A(x)=x^4-21x^2-8x+84,
\]

\[
B(x)=x^3+4x^2-4x-16,
\]

\[
C(x)=x^2+11x+6.
\tag{4.9}
\]

Formula (4.7) is the general version of the previously discovered period-eight and period-sixteen threshold identities. No determinant of growing size remains.

---

## 5. Uniform lower bound for `F_L`

### Lemma B

For every even `L>=4` and every `x in [-2,2]`,

\[
\boxed{F_L(x)\ge20.}
\tag{5.1}
\]

#### Proof

Let `F_m` denote the right side of (4.8), with

\[
u=U_m((4-x)/2),\qquad w=U_{m-1}((4-x)/2).
\]

Since `(4-x)/2>=1`,

\[
0\le w\le u.
\tag{5.2}
\]

The Chebyshev recurrence gives the next numerator

\[
U_{m+1}((4-x)/2)=(4-x)u-w.
\]

A direct substitution into (4.8) factors the increment exactly as

\[
\begin{aligned}
F_{m+1}(x)-F_m(x)
={}&(x-2)
\Bigl[u(x^2-x-13)+w(x+3)\Bigr]\\
&\times
\Bigl[u(x^3-5x^2-11x+46)
+w(x^2-x-14)\Bigr].
\end{aligned}
\tag{5.3}
\]

On `[-2,2]`, the first bracket is strictly negative, because by (5.2)

\[
\frac1u\Bigl[u(x^2-x-13)+w(x+3)\Bigr]
\le x^2-10<0.
\tag{5.4}
\]

The second bracket is strictly positive. Indeed `x^2-x-14<0`, so (5.2) gives

\[
\begin{aligned}
&u(x^3-5x^2-11x+46)+w(x^2-x-14)\\
&\qquad\ge
u\Bigl[(x^3-5x^2-11x+46)+(x^2-x-14)\Bigr]\\
&\qquad=
u(x-2)(x^2-2x-16)\ge0.
\end{aligned}
\tag{5.5}
\]

For `x<2` the last expression is positive; at `x=2` the original bracket equals `12(u-w)>0` because `U_m(1)-U_{m-1}(1)=1`.

Since `x-2<=0`, (5.3)--(5.5) imply

\[
F_{m+1}(x)\ge F_m(x).
\tag{5.6}
\]

At `m=0`, equivalently `L=4`,

\[
F_4(x)=x^4-20x^2+3x+90.
\]

Moreover

\[
F_4(x)-20
=(x+2)\Bigl[3+(2-x)(16-x^2)\Bigr]\ge0
\tag{5.7}
\]

on `[-2,2]`. Combining (5.6) and (5.7) proves (5.1).

---

## 6. No threshold crossing

Since `d,e in [-2,2]`, (4.7) and Lemma B give

\[
\boxed{
P_{L,q,z}(8)\ge20-4=16>0
}
\tag{6.1}
\]

for every Bloch phase and every odd multiplier.

Thus no squared Bloch eigenvalue can cross `8`. It remains only to establish the inertia at one phase.

Take `z=1`. Then `d=e=2`, and the fiber is independent of `q`. Put

\[
r_0=L/2.
\]

A specialization of the same transfer calculation yields the exact factorization

\[
\boxed{
\det(\lambda I-H_{L,q}(1))
=p_{r_0}(y)\bigl(p_{r_0}(y)+4\bigr),
\qquad y=\lambda^2,
}
\tag{6.2}
\]

where

\[
\boxed{
\begin{aligned}
p_r(y)={}&
U_{r-2}\!\left(\frac{y-6}{2}\right)
(y^2-8y+6)\\
&-U_{r-3}\!\left(\frac{y-6}{2}\right)(y-2)-2,
\end{aligned}}
\tag{6.3}
\]

again with `U_{-1}=0`.

For `y>=8`, set

\[
u=U_{r-2}((y-6)/2),
\qquad w=U_{r-3}((y-6)/2).
\]

Then `u>=w>=0`, and in fact `u-w>=1`. Rewriting (6.3),

\[
\boxed{
p_r(y)+2
=6(u-w)+(y-8)(yu-w).}
\tag{6.4}
\]

Hence

\[
p_r(y)\ge4
\]

for every `y>=8`, with strict inequality when `y>8`. Therefore neither factor in (6.2) has a root in `[8,infinity)`. Since the fiber is Hermitian, its squared eigenvalues are real and nonnegative, so

\[
\rho(H_{L,q}(1))^2<8.
\tag{6.5}
\]

The unit circle is connected, the Hermitian fibers vary continuously, and (6.1) prevents an eigenvalue of `8I-H(z)^2` from passing through zero. The inertia is therefore constant. Combining this with (6.5) gives

\[
8I-H_{L,q}(z)^2>0
\]

for every `|z|=1`, proving (1.4).

---

## 7. Quantitative gap

By signed-reflection chirality,

\[
\det(\lambda I-H_{L,q}(z))
=\prod_{j=1}^{L}(\lambda^2-y_j(z))
\]

with

\[
0\le y_j(z)<8.
\]

At `lambda^2=8`, (6.1) gives

\[
\prod_{j=1}^{L}(8-y_j(z))\ge16.
\]

Every factor is at most `8`. If

\[
\delta(z)=8-\max_jy_j(z),
\]

then

\[
16\le \delta(z)8^{L-1}.
\]

Thus

\[
\delta(z)\ge\frac{16}{8^{L-1}}
\]

uniformly in `z`, which proves (1.5).

---

## 8. Consequences for the paper

The arithmetic hierarchy is now a theorem, not an observed pattern.

For even `s`:

- `v_2(s)=1`: use the separate fixed period-eight phase with the exact constant edge `4+sqrt(10+2sqrt(5))`;
- `v_2(s)=k>=2`: put `L=2^k` and use Theorem A, giving period `2^{k+1}` independently of the odd part of `s`.

Hence the old period-`4s` construction is no longer the strongest existence theorem for any even jump. It remains valuable for its sharp large-jump asymptotics and phase-slip analysis, but the existence/period theorem should now be organized around `2`-adic compression.

The main remaining strengthening problem is quantitative rather than existential: replace the elementary determinant bound `16/8^{L-1}` by the numerically suggested polynomial-scale gap, apparently of order `L^{-2}` for the compressed two-defect family.