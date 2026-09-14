# Exact all-energy characteristic formula for arbitrary even defect separation

Date: 2026-09-14

Status: **Proved**. This upgrades `GENERAL_SEPARATION_THRESHOLD_FORMULA.md` from the single energy `y=8` to an arbitrary squared spectral parameter.

## 1. Setup

Write

\[
L=2(N+m),\qquad h=2m,
\qquad N,m\ge1.
\]

For a unit Bloch phase `z`, put

\[
d=z^{2q+1}+z^{-(2q+1)},
\qquad
e=z+z^{-1}.
\]

Let

\[
y=\lambda^2
\]

be an arbitrary squared spectral parameter and define

\[
x=\frac{y-d-4}{2},
\qquad
a=\frac{y+d-4}{2}.
\tag{1.1}
\]

Set

\[
u=U_{N-1}(x),
\qquad X=T_N(x),
\]

\[
p=U_{m-1}(a),
\qquad Y=T_m(a).
\tag{1.2}
\]

## Theorem A — exact scalar characteristic equation

For every `N,m>=1`, every `q>=0`, every unit phase `z`, and every complex `y`,

\[
\boxed{
P_{N,m,q,z}(y)
=A(y,d)u^2p^2
-2K(y,d)XYup
+B(y,d)p^2
+C(y,d)u^2
-e+2,
}
\tag{1.3}

where

\[
\det(\lambda I-H_{N,m,q}(z))
=P_{N,m,q,z}(\lambda^2)
\]

and

\[
\boxed{
K(y,d)=d^2-y^2+8y-4,
}
\tag{1.4}

\[
\boxed{
\begin{aligned}
A(y,d)=\frac12(&d^4-2d^2y^2+16d^2y-24d^2\\
&+y^4-16y^3+80y^2-128y+80),
\end{aligned}}
\tag{1.5}

\[
\boxed{
B(y,d)=d^2+2dy-4d+y^2-8y+4,
}
\tag{1.6}

and

\[
\boxed{
C(y,d)=(d-y+2)(d-y+6).
}
\tag{1.7}

Thus the entire `2L x 2L` Bloch spectral problem is reduced to four scalar Chebyshev quantities and the two real Bloch coordinates `(d,e)`.

In particular, the seam coordinate enters **only linearly**:

\[
\boxed{
P(y;d,e)=\mathcal G_{N,m}(y,d)-e.
}
\tag{1.8}

This is the all-energy analogue of the threshold identity.

---

## 2. Transfer derivation

Use the block-Jacobi reduction. The generic and defect transfer coefficients are

\[
A_g=\lambda\sigma_z-2ic\sigma_y,
\qquad
A_d=\lambda\sigma_z+2ir\sigma_x,
\]

with

\[
4c^2=d+2,
\qquad
4r^2=2-d.
\]

They satisfy

\[
A_g^2=(y-d-2)I,
\qquad
A_d^2=(y+d-2)I.
\]

The odd generic transfer power of length `2N-1` is

\[
\begin{pmatrix}
 uA_g&-(u+w)I\\
 (u+w)I&-wA_g
\end{pmatrix},
\]

where

\[
w=U_{N-2}(x),
\]

while the even defect power of length `2m` is

\[
\begin{pmatrix}
 (U_m(a)+p)I&-pA_d\\
 pA_d&-(p+v)I
\end{pmatrix},
\]

with

\[
v=U_{m-2}(a).
\]

The monodromy is the product of these two blocks followed by one final generic transfer. The Bloch closing condition is

\[
-\eta^{-2}\det(M-\eta J),
\qquad
\eta^2=z,
\qquad
J=\operatorname{diag}(\sigma_x,-\sigma_x).
\]

Expand this fixed `4 x 4` determinant. The two Chebyshev identities

\[
u^2+w^2-2xuw=1,
\qquad
p^2+v^2-2apv=1
\tag{2.1}
\]

remove `w^2` and `v^2`. Writing

\[
w=xu-X,
\qquad
v=ap-Y
\tag{2.2}
\]

then reduces the remaining expression to the four monomials

\[
u^2p^2,\qquad XYup,\qquad p^2,\qquad u^2.
\]

The boundary powers collapse exactly to

\[
-(\eta^2+\eta^{-2})=-e,
\]

and coefficient collection gives (1.4)--(1.7), proving (1.3).

No determinant whose size depends on `N` or `m` remains.

---

## 3. Recovery of earlier formulas

At

\[
y=8,
\]

we have

\[
K(8,d)=d^2-4.
\]

Substitution into (1.3) gives exactly the compact threshold formula

\[
P(8,z)=\mathcal F_{N,m}(d)-e
\]

from `GENERAL_SEPARATION_THRESHOLD_FORMULA.md`.

For `m=1`, formula (1.3) reduces to the earlier exact two-phase characteristic equation for the separation-two compressed family.

Thus (1.3) simultaneously contains both earlier reductions.

---

## 4. Direct audit

The identity has been independently checked against direct Bloch determinants for multiple tuples

\[
(N,m,q)=(1,1,0),(2,3,1),(3,2,2),(4,4,3),(5,1,7)
\]

at generic nonendpoint phases and generic energies. The direct `2L x 2L` determinants and (1.3) agree to numerical roundoff. These evaluations are an audit only; the theorem source is the transfer derivation above.

## 5. Role in the all-layer quarter-period problem

For the balanced geometry `N=m=r`, choose the comparison energy

\[
y_*=6+2\cos\frac{\pi}{2(r+1)}.
\]

The universal competitor theorem shows that every unbalanced geometry in the same period has full Bloch edge strictly larger than `y_*`. Therefore proving quarter-period optimality for a given `r` is now equivalent to the one-variable relaxed inequality

\[
\boxed{
\mathcal G_{r,r}(y_*,d)>2
\qquad(-2\le d\le2),
}
\]

with inertia fixed at one reference phase. This is a scalar Chebyshev problem rather than a growing matrix problem.
