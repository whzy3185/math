# Uniform hyperbolicity of the `DDGG` multi-block bulk at the separator `31/4`

Date: 2026-09-14

Status: **Proved**.

This theorem isolates the bulk mechanism behind the explicit multi-defect improvements at periods `20,24,28,32,36,40`.

---

## 1. Folded block-Jacobi setting

For jump equal to half the coefficient period, fold the Hamilton-gauge fiber into an `L`-site two-component block Jacobi chain. Write the compressed Bloch phase as

\[
\omega=e^{i\beta},
\qquad
c=\cos\beta,
\qquad
r=\sin\beta.
\]

There are two onsite types:

\[
G:\quad V_g=2c\,\sigma_x,
\]

and

\[
D:\quad V_d=2r\,\sigma_y.
\]

With

\[
T(A)=\begin{pmatrix}A&-I_2\\I_2&0\end{pmatrix},
\]

the corresponding one-site transfer coefficients are

\[
A_g=\lambda\sigma_z-2ic\sigma_y,
\qquad
A_d=\lambda\sigma_z+2ir\sigma_x.
\]

Put

\[
T_g=T(A_g),
\qquad T_d=T(A_d).
\]

The repeating multi-block background discovered in the period `20--40` constructions is the four-site motif

\[
DDGG.
\]

Up to cyclic conjugacy its transfer matrix is

\[
B=T_d^2T_g^2.
\]

---

# Theorem A — exact quadratic transfer identity

At the fixed squared energy

\[
\boxed{\lambda^2=31/4,}
\]

let

\[
d=2\cos(2\beta)=2(c^2-r^2)\in[-2,2].
\]

Then

\[
\boxed{
B^2-\mathcal A(d)B+I_4=0,
}
\tag{2.1}
\]

where

\[
\boxed{
\mathcal A(d)=\frac{129}{16}-d^2.
}
\tag{2.2}
\]

Equivalently,

\[
\det(\mu I_4-B)
=
\boxed{\left(\mu^2-\mathcal A(d)\mu+1\right)^2}.
\tag{2.3}
\]

Thus the apparent four-channel transfer problem collapses to one reciprocal scalar quadratic, with each root occurring twice.

---

## 2. Proof

The Pauli anticommutation relations give

\[
A_g^2=(\lambda^2-4c^2)I_2,
\qquad
A_d^2=(\lambda^2-4r^2)I_2.
\]

A direct multiplication of the two squared transfer factors gives

\[
\det(\mu I_4-T_d^2T_g^2)
=
\left(\mu^2-\mathcal A\mu+1\right)^2,
\]

with

\[
\begin{aligned}
\mathcal A={}&16c^2r^2
-4c^2\lambda^2+4c^2
-4r^2\lambda^2+4r^2\\
&+\lambda^4-4\lambda^2+2.
\end{aligned}
\tag{3.1}
\]

At `lambda^2=31/4`, use

\[
c^2+r^2=1,
\qquad
16c^2r^2=4-d^2.
\]

Then (3.1) simplifies to

\[
\mathcal A
=\frac{65}{16}+16c^2r^2
=\frac{129}{16}-d^2,
\]

which is (2.2).

The stronger matrix identity (2.1) follows by direct substitution using the same Pauli relations; equivalently, the two squared transfer factors preserve the same two-dimensional chiral channel decomposition, so the degree-two factor in (2.3) is the minimal polynomial on each channel.

---

# Corollary B — uniform hyperbolicity on the entire Bloch circle

For every physical compressed phase,

\[
-2\le d\le2,
\]

and therefore

\[
\boxed{
\mathcal A(d)\ge\frac{65}{16}>2.
}
\tag{4.1}
\]

Hence the two reciprocal transfer roots

\[
\rho_\pm(d)
=
\frac{\mathcal A(d)\pm\sqrt{\mathcal A(d)^2-4}}2
\]

are real and satisfy

\[
0<\rho_-(d)<1<\rho_+(d).
\]

The `DDGG` bulk is therefore uniformly hyperbolic at squared energy `31/4`, with a phase-independent positive hyperbolicity margin.

---

# Corollary C — exact power reduction

For every integer `n>=1`,

\[
\boxed{
B^n
=U_{n-1}\!\left(\frac{\mathcal A(d)}2\right)B
-U_{n-2}\!\left(\frac{\mathcal A(d)}2\right)I_4.
}
\tag{5.1}
\]

Thus arbitrarily long multi-block cells built from the `DDGG` bulk require no growing matrix powers: their dependence on bulk length is carried by a single Chebyshev pair.

---

## 5. Relation to the explicit multi-defect constructions

The folded winners/improving phases discovered so far have the following common form.

- For periods `p=8r+4`, the folded onsite word is
  \[
  G(DDGG)^rG,
  \]
  i.e. a `DDGG` background with one extra `GG` dislocation at the seam.

- For periods `p=8r`, the folded word has the same `DDGG` background but one `DD` block is lengthened to `DDDD`; this is the complementary defect-type dislocation.

Therefore the stable edge near `7.7007` seen from periods `20` through `64` is naturally interpreted as a dislocation bound state inside a uniformly hyperbolic `DDGG` bulk.

The remaining step toward an infinite-family theorem is finite-dimensional: compute the two dislocation matching determinants after replacing `B^n` by (5.1), and prove that they do not vanish for `d in [-2,2]`.