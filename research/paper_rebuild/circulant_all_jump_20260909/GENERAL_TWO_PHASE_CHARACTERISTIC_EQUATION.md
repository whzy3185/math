# Exact two-phase characteristic equation for the compressed two-defect family

Date: 2026-09-09

Status: **Proved**. This note belongs only to Paper I. It upgrades the threshold-only identity in `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md` to an exact characteristic equation at an arbitrary squared spectral parameter.

## 1. Setup

Let `L>=4` be even, let

\[
s=L(2q+1),\qquad q\ge0,
\]

and use the period-`2L` two-defect Hamilton-gauge word

\[
\tau_0=\tau_1=1,
\qquad
\tau_2=\tau_3=-1,
\qquad
\tau_j=(-1)^j\quad(4\le j<2L).
\]

Let `H_{L,q}(z)` be the `2L x 2L` Bloch fiber, `|z|=1`.

By the signed-reflection chirality theorem,

\[
\det(\lambda I-H_{L,q}(z))
=P_{L,q,z}(\lambda^2)
\]

for a monic degree-`L` polynomial.

Choose `eta` with

\[
\eta^2=z
\]

and define

\[
\omega=z^q\eta.
\]

The two real phase coordinates are

\[
\boxed{
d=\omega^2+\omega^{-2}=z^{2q+1}+z^{-(2q+1)},
\qquad
e=z+z^{-1}.}
\tag{1.1}
\]

Thus `d,e in [-2,2]`.

---

## 2. Transfer compression

After the unitary folding and gauge used in the general compression theorem, the fiber becomes an `L`-site two-component block Jacobi problem. Put

\[
\omega=e^{i\beta},
\qquad c=\cos\beta,
\qquad r=\sin\beta.
\]

The generic and defect transfer coefficients are

\[
A_g=\lambda\sigma_z-2ic\sigma_y,
\qquad
A_d=\lambda\sigma_z+2ir\sigma_x,
\]

with

\[
A_g^2=(\lambda^2-4c^2)I_2.
\]

Write

\[
y=\lambda^2.
\]

Since

\[
4c^2=d+2,
\]

we have

\[
A_g^2=(y-d-2)I_2.
\tag{2.1}
\]

Let

\[
m=\frac{L-4}{2},
\qquad
t=\frac{y-d-4}{2},
\]

and define

\[
\boxed{
u=U_m(t),
\qquad
w=U_{m-1}(t),}
\tag{2.2}
\]

with `U_{-1}=0`.

The matrix continuants of the generic transfer satisfy

\[
D_{2m+1}=uA_g,
\qquad
D_{2m}=(u+w)I_2,
\qquad
D_{2m-1}=wA_g.
\]

Equivalently,

\[
T(A_g)^{L-3}
=
\begin{pmatrix}
 uA_g&-(u+w)I_2\\
 (u+w)I_2&-wA_g
\end{pmatrix}.
\tag{2.3}
\]

The Chebyshev identity is

\[
\boxed{
u^2+w^2-(y-d-4)uw=1.}
\tag{2.4}
\]

The full monodromy is

\[
M(\lambda)=T(A_g)^{L-3}T(A_d)^2T(A_g),
\]

and the Bloch determinant is

\[
\det(\lambda I-H_{L,q}(z))
=-\eta^{-2}\det(M(\lambda)-\eta J),
\tag{2.5}
\]

where

\[
J=\operatorname{diag}(\sigma_x,-\sigma_x).
\]

---

## 3. Exact characteristic equation

### Theorem A

For every even `L>=4`, every `q>=0`, every unit Bloch phase `z`, and every complex squared spectral parameter `y`,

\[
\boxed{
P_{L,q,z}(y)
=u^2A(y,d)+uwB(y,d)+C(y,d)-e,}
\tag{3.1}
\]

where `u,w` are given by (2.2), and

\[
\boxed{
A(y,d)=
\bigl(y^2-9y+14-d^2-d\bigr)
\bigl(y^2-7y+6-d^2+d\bigr),}
\tag{3.2}
\]

\[
\boxed{
B(y,d)=
-(d+y-4)\bigl(y^2-8y+4-d^2\bigr),}
\tag{3.3}
\]

\[
\boxed{
C(y,d)=
d^2+2dy-4d+y^2-8y+6.}
\tag{3.4}
\]

Thus the entire `2L x 2L` Bloch spectral problem is reduced to two Chebyshev functions and the two real phase variables `(d,e)`.

### Proof

Insert (2.3) into (2.5) and expand the fixed `4 x 4` determinant. Before using the Chebyshev identity, the only boundary powers are `eta^2` and `eta^{-2}`. Their coefficients simplify to `-1` after imposing (2.4); explicitly, the excess factor is

\[
\bigl((y-d-4)uw-u^2-w^2-1\bigr)
\bigl((y-d-4)uw-u^2-w^2+1\bigr),
\]

which vanishes by (2.4).

Hence the boundary contribution is exactly

\[
-(\eta^2+\eta^{-2})=-e.
\]

The remaining expression is linear in `u^2`, `uw`, and `w^2`. Eliminating `w^2` through

\[
w^2=1+(y-d-4)uw-u^2
\]

gives precisely (3.1)--(3.4).

No determinant of size depending on `L` remains.

---

## 4. Recovery of the threshold theorem

At

\[
y=8,
\]

we have

\[
t=\frac{4-d}{2},
\]

and (3.1) becomes

\[
P_{L,q,z}(8)=F_L(d)+d-e,
\]

where

\[
F_L(d)
=u^2(d^4-21d^2-8d+84)
+uw(d^3+4d^2-4d-16)
+d^2+11d+6.
\]

This is exactly the threshold identity used in the general compression theorem.

---

## 5. Endpoint specialization

At the periodic phase `z=1`,

\[
d=e=2,
\]

and (3.1) factors into the endpoint formula

\[
P_{L,q,1}(y)=p_{L/2}(y)\bigl(p_{L/2}(y)+4\bigr)
\]

recorded in `COMPRESSED_ENDPOINT_SHARP_GAP.md`.

Thus the exact Robin endpoint equation and the global two-phase transfer formula are two specializations of the same characteristic identity.

---

## 6. Independent audit

As an audit only, not as part of the proof, the formula was compared against direct determinants of the original `2L x 2L` Bloch matrix for

\[
L=4,6,8,10,12,
\]

several odd multipliers `2q+1`, several nontrivial unit phases, and squared spectral parameters including `5.5`, `7.2`, and `8`. The two sides agree to floating-point roundoff in every tested case.

---

## 7. Research consequence

The global Bloch-edge problem is now reduced to the zero set

\[
\boxed{
u^2A(y,d)+uwB(y,d)+C(y,d)=e,}
\]

subject to

\[
d=2\cos((2q+1)t),
\qquad
e=2\cos t.
\]

This is the correct starting point for proving endpoint dominance or, failing exact dominance, a uniform `L^{-2}` global-gap theorem. In particular, the question is no longer a growing-matrix spectral problem but a two-phase Chebyshev comparison problem.
