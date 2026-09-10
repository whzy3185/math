# Sharp endpoint gap for arbitrary fixed even defect separation

Date: 2026-09-10

Status: **Proved**. This note belongs only to Paper I. It strengthens `GENERAL_EVEN_SEPARATION_CHIRALITY.md` from symmetry to a sharp endpoint spectral asymptotic.

## 1. Setup

Let `h=2m>=2` be fixed and even. Let `L>h` be even, let the coefficient period be `2L`, and take the two-defect flux word

\[
Q_0=Q_h=1,\qquad Q_j=-1\quad(j\ne0,h).
\]

Choose the Hamilton-gauge lift `tau_0=1`. Let

\[
s=L(2q+1),\qquad q\ge0,
\]

and let `H_{L,q,h}(z)` denote the `2L x 2L` Bloch fiber. At the periodic endpoint `z=1`, the fiber is independent of `q`; define

\[
e_{L,h}:=8-\rho(H_{L,q,h}(1))^2.
\]

Put

\[
N:=\frac{L-h}{2}.
\]

The main theorem is

### Theorem A — sharp endpoint constant for separation `h=2m`

For every fixed `m>=1`,

\[
\boxed{
L^2 e_{L,2m}
\longrightarrow
4\alpha_m^2,
\qquad
\alpha_m:=\arccos\frac1{T_m(3)}.
}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
8-\rho(H_{L,q,2m}(1))^2
=\frac{4}{L^2}
\arccos\!\left(\frac1{T_m(3)}\right)^2
+o(L^{-2}).
}
\tag{1.2}
\]

The constant is independent of the odd multiplier `2q+1`.

For `m=1`, `T_1(3)=3`, recovering the previously proved constant

\[
4\arccos(1/3)^2.
\]

---

## 2. Endpoint folding into two scalar channels

At `z=1`, pair residues `j` and `j+L`, `0<=j<L`, and write

\[
\Psi_j=(x_j,x_{j+L})^T.
\]

The long-jump coefficient between the two coordinates is

\[
c_j=\tau_j+\tau_{j+L}.
\]

Because `L` and `h` are even and `L>h`, direct reconstruction of the two-defect word gives

\[
c_0=2,
\qquad
c_j=0\quad(1\le j\le h),
\qquad
c_j=2(-1)^j\quad(h+1\le j<L).
\tag{2.1}
\]

Hence

\[
(H\Psi)_j=\Psi_{j-1}+\Psi_{j+1}+c_j\sigma_x\Psi_j
\]

on the `L`-cycle. Diagonalizing `sigma_x` decomposes the endpoint fiber as

\[
H_{L,q,h}(1)\simeq J_+\oplus J_-,
\]

where

\[
(J_\pm f)_j=f_{j-1}+f_{j+1}\pm c_jf_j.
\]

If `D_L f_j=(-1)^j f_j`, then, since `L` is even,

\[
J_-=-D_LJ_+D_L.
\]

Therefore the two scalar channels have opposite spectra and the squared endpoint edge is determined by `J_+` alone.

---

## 3. Exact transfer quantization

For a scalar potential value `v`, set

\[
T_v(\lambda)=
\begin{pmatrix}
\lambda-v&-1\\
1&0
\end{pmatrix}.
\]

In the `J_+` channel, the potential consists of one alternating bulk arc and a block of exactly `h=2m` zero sites. By cyclic invariance of trace, its monodromy has the same trace as

\[
B(\lambda)^N D(\lambda)^m,
\tag{3.1}
\]

where

\[
B=T_2T_{-2},
\qquad
D=T_0^2.
\]

Both matrices have determinant one, and with `y=lambda^2`,

\[
\operatorname{tr}B=y-6,
\qquad
\operatorname{tr}D=y-2.
\tag{3.2}
\]

A periodic scalar eigenvalue is therefore characterized by

\[
\boxed{
\operatorname{tr}(B^ND^m)=2.
}
\tag{3.3}
\]

Let

\[
a=\frac{y-2}{2}.
\]

Then

\[
A_m(y):=\operatorname{tr}D^m=2T_m(a).
\tag{3.4}
\]

Define also

\[
C_m(y):=\operatorname{tr}(BD^m).
\]

A direct `2 x 2` multiplication followed by the Cayley--Hamilton recurrence for `D` gives the exact identity

\[
\boxed{
C_m(y)-A_m(y)
=(y-8)\Bigl[U_m(a)+U_{m-1}(a)\Bigr].
}
\tag{3.5}
\]

Now write the near-edge spectral parameter as

\[
y=6+2\cos\theta,
\qquad 0<\theta<\pi.
\]

Since `tr B=2 cos theta`,

\[
B^N=U_{N-1}(\cos\theta)B-U_{N-2}(\cos\theta)I.
\]

Combining this with (3.3)--(3.5) gives the exact scalar quantization equation

\[
\boxed{
T_m(2+\cos\theta)
\frac{\cos((N-\tfrac12)\theta)}{\cos(\theta/2)}
-
\Bigl[U_m(2+\cos\theta)+U_{m-1}(2+\cos\theta)\Bigr]
\tan(\theta/2)\sin(N\theta)
=1.
}
\tag{3.6}
\]

This is the arbitrary-even-separation analogue of the Robin equation previously obtained at `h=2`.

---

## 4. Localization of the top endpoint root

The endpoint fiber is a finite-rank perturbation of the alternating bulk operator. The top squared eigenvalue lies below `8` for all sufficiently large `L`; equivalently the relevant solution of (3.6) satisfies `theta->0`.

Set

\[
x_N=N\theta_N.
\]

The test scale `theta=c/N` in (3.6) shows that `x_N` remains in a compact subinterval of `(0,pi)`. Take any convergent subsequence,

\[
x_N\to x.
\]

Since `theta_N->0`,

\[
T_m(2+\cos\theta_N)\to T_m(3),
\]

while the second term in (3.6) is `O(theta_N)` and therefore tends to zero. Also

\[
\frac{\cos((N-\tfrac12)\theta_N)}{\cos(\theta_N/2)}\to\cos x.
\]

Passing to the limit in (3.6) yields

\[
T_m(3)\cos x=1.
\]

Since the top root lies in the first oscillatory cell, `0<x<pi/2`, so necessarily

\[
\boxed{
x=\alpha_m:=\arccos\frac1{T_m(3)}.}
\tag{4.1}
\]

Every convergent subsequence has the same limit; hence

\[
\boxed{N\theta_N\to\alpha_m.}
\tag{4.2}
\]

---

## 5. Recovering the gap

The squared endpoint gap is

\[
e_{L,2m}=2-2\cos\theta_N.
\]

Since

\[
L=2N+2m
\]

and `m` is fixed,

\[
\frac{L}{N}\to2.
\]

Therefore

\[
\begin{aligned}
L^2e_{L,2m}
&=L^2\bigl(2-2\cos\theta_N\bigr)\\
&=\left(\frac{L}{N}\right)^2
(N\theta_N)^2
\left(\frac{2-2\cos\theta_N}{\theta_N^2}\right)\\
&\longrightarrow
4\alpha_m^2,
\end{aligned}
\]

which proves Theorem A.

---

## 6. Dependence on defect separation

Because `T_m(3)` is strictly increasing in `m`, the sequence

\[
\alpha_m=\arccos\frac1{T_m(3)}
\]

is strictly increasing. Moreover

\[
T_m(3)=\cosh(m\,\operatorname{arcosh}3)\to\infty,
\]

so

\[
\alpha_m\uparrow\frac\pi2.
\]

Consequently the sharp endpoint constants satisfy

\[
\boxed{
4\arccos(1/3)^2
=4\alpha_1^2
<4\alpha_2^2<\cdots<\pi^2,
}
\tag{6.1}
\]

and

\[
\boxed{4\alpha_m^2\uparrow\pi^2.}
\tag{6.2}
\]

The first values are governed by

\[
T_1(3)=3,\quad T_2(3)=17,\quad T_3(3)=99,\quad T_4(3)=577,\ldots
\]

Thus increasing a fixed even defect separation improves the leading endpoint gap, and the limiting constant approaches the Dirichlet value `pi^2` exponentially fast in `m`.

This creates a genuine internal variational problem for the periodic-phase paper: the separation geometry controls the Robin boundary constant even though all members share the same signed-reflection chirality.