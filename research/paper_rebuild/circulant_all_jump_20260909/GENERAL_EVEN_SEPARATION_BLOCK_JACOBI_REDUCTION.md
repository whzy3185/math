# Exact block-Jacobi reduction for arbitrary even defect separation

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I.

## 1. Statement

Let `L>h>=2` be even, let the coefficient period be `2L`, and define the two-defect flux word

\[
Q_0=Q_h=1,\qquad Q_j=-1\quad(j\ne0,h).
\]

Choose the Hamilton-gauge lift `tau_0=1`, and let

\[
s=L(2q+1),\qquad q\ge0.
\]

For a unit Bloch phase `z`, choose `eta` with

\[
\eta^2=z
\]

and set

\[
\omega=z^q\eta=e^{i\beta}.
\]

Let

\[
c=\cos\beta,\qquad r=\sin\beta.
\]

### Theorem A — two-component Jacobi normal form

The `2L x 2L` Bloch fiber `H_{L,q,h}(z)` is unitarily equivalent to an `L`-site two-component block Jacobi matrix with

- nearest-neighbor interior blocks `sigma_z`;
- onsite blocks
  \[
  \boxed{
  V_j=
  \begin{cases}
  2r\,\sigma_y,&1\le j\le h,\\
  2c\,\sigma_x,&j=0\text{ or }h+1\le j<L;
  \end{cases}}
  \tag{1.1}
  \]
- closing block
  \[
  \boxed{C=i\eta\sigma_y.}
  \tag{1.2}
  \]

Thus the two flux defects create a contiguous defect arc of length exactly `h`, while the complementary arc of length `L-h` is a uniform alternating bulk after gauge.

All dependence on the odd multiplier `2q+1` enters only through

\[
\boxed{\omega^2=z^{2q+1}.}
\tag{1.3}
\]

---

## 2. Folding the long jump

Pair residues `j` and `j+L`, `0<=j<L`. Before the final local gauge, the two long-jump amplitudes between the coordinates of the `j`th pair combine to

\[
\tau_jz^q+\tau_{j+L}z^{-(q+1)}.
\]

Multiply the second coordinate in every pair by `eta^{-1}`. The off-diagonal onsite coefficient becomes

\[
\tau_j\omega+\tau_{j+L}\omega^{-1}.
\tag{2.1}
\]

Now conjugate the `j`th pair by `sigma_z^j`. This changes the off-diagonal coefficient by `(-1)^j`, so it becomes

\[
(-1)^j\tau_j\omega+(-1)^j\tau_{j+L}\omega^{-1}.
\tag{2.2}
\]

Because `L>h` and `L` is even, the reconstruction of the two-defect word gives

\[
\tau_{j+L}=(-1)^j
\qquad(0\le j<L).
\tag{2.3}
\]

Also

\[
(-1)^j\tau_j=
\begin{cases}
-1,&1\le j\le h,\\
1,&j=0\text{ or }h+1\le j<L.
\end{cases}
\tag{2.4}
\]

Hence (2.2) equals

\[
\omega+\omega^{-1}=2c
\]

on the generic arc, and

\[
-\omega+\omega^{-1}=-2ir
\]

on the defect arc. The corresponding Hermitian onsite matrices are exactly `2c sigma_x` and `2r sigma_y`, proving (1.1).

The same pairwise conjugation changes every interior nearest-neighbor block into `sigma_z`. Tracking the single seam across the period gives the closing block `i eta sigma_y`, proving (1.2).

---

## 3. Transfer form

For an eigenvector with two-component values `psi_j`, the interior equation is

\[
\sigma_z\psi_{j-1}+V_j\psi_j+\sigma_z\psi_{j+1}=\lambda\psi_j.
\]

Set

\[
T(A)=
\begin{pmatrix}
A&-I_2\\
I_2&0
\end{pmatrix},
\qquad
A_j=\sigma_z(\lambda I_2-V_j).
\]

There are only two transfer coefficients:

\[
\boxed{
A_g=\lambda\sigma_z-2ic\sigma_y,
\qquad
A_d=\lambda\sigma_z+2ir\sigma_x.}
\tag{3.1}
\]

They satisfy

\[
\boxed{
A_g^2=(\lambda^2-4c^2)I_2,
\qquad
A_d^2=(\lambda^2-4r^2)I_2.}
\tag{3.2}
\]

With the indexing above, the full monodromy is

\[
\boxed{
M_{L,h}(\lambda)
=T(A_g)^{L-h-1}T(A_d)^hT(A_g).}
\tag{3.3}
\]

The closing block is equivalent to

\[
\psi_L=\eta\sigma_x\psi_0,
\qquad
\psi_{L-1}=-\eta\sigma_x\psi_{-1}.
\]

Thus, with

\[
J=\operatorname{diag}(\sigma_x,-\sigma_x),
\]

the exact characteristic condition is

\[
\boxed{
\det(\lambda I_{2L}-H_{L,q,h}(z))
=-\eta^{-2}
\det\bigl(M_{L,h}(\lambda)-\eta J\bigr).}
\tag{3.4}
\]

No matrix larger than `4 x 4` is needed after the two scalar-square transfer powers are evaluated by Chebyshev recurrences.

---

## 4. Threshold specialization

At the squared edge `lambda^2=8`, put

\[
d=\omega^2+\omega^{-2}=2\cos(2\beta).
\]

Then

\[
4c^2=2+d,
\qquad
4r^2=2-d,
\]

and therefore

\[
\boxed{
A_g^2=(6-d)I_2,
\qquad
A_d^2=(6+d)I_2.}
\tag{4.1}
\]

This is the key symmetric threshold structure for the general even-separation family: the two arcs are governed by complementary scalar transfer parameters `6-d` and `6+d`.

Consequently, if

\[
N=\frac{L-h}{2},
\qquad m=\frac h2,
\]

then all growing powers in (3.3) reduce to Chebyshev functions with arguments

\[
\frac{4-d}{2}
\quad\text{and}\quad
\frac{4+d}{2}.
\]

This turns the full general-separation threshold problem into a two-Chebyshev `4 x 4` determinant problem depending only on `(N,m,d,e)`, where

\[
e=z+z^{-1}.
\]

## 5. Research consequence

The earlier `h=2` compressed theorem corresponds to `m=1`; the new normal form shows that arbitrary even separation is not a different model, but the same two-phase scattering problem with a defect transfer block of length `m`.

The next classification target is therefore precise:

> determine for which pairs `(N,m)` the threshold determinant remains positive for every physical Bloch phase.

Numerical evidence indicates that the answer is controlled more naturally by the complementary bulk length `N=(L-h)/2` than by `h` alone.