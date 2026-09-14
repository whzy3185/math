# Second-best fixed-period geometry and the spectral stability gap

Date: 2026-09-14

Status: **Proved, with corrected beyond-all-orders seam term**.

This theorem quantitatively strengthens `ALL_FIXED_PERIOD_BALANCED_OPTIMALITY.md`: for large period it identifies the unique runner-up and gives the full algebraic stability expansion together with the first odd-multiplier-dependent tunneling correction.

## 1. Fixed-period setup

Fix

\[
N+m=2r,
\qquad r\to\infty,
\]

so the primitive coefficient period is

\[
p=8r.
\]

Let

\[
\Gamma_{N,m,q}
=8-\max_{|z|=1}\rho(H_{N,m,q}(z))^2,
\qquad n=2q+1.
\]

The unique optimum is `(r,r)`. Let `Gamma_r^(1)` be its gap and `Gamma_r^(2)` the largest gap among all unbalanced geometries.

## Theorem A — eventual unique second-best geometry

For all sufficiently large `r`, the unique second-best geometry is

\[
\boxed{(N,m)=(r-1,r+1).}
\]

The opposite one-step orientation `(r+1,r-1)` has the same dominant soft length but loses the algebraic periodic cusp gain.

---

## 2. Formal-series comparison

Let

\[
A(\ell)=\sum_{j\ge2}a_j\ell^{-j}
\]

be the universal endpoint Robin series and

\[
C(\ell)=\sum_{j\ge0}c_j\ell^{-j-4}
\]

the periodic cusp-gain series. Then

\[
\Gamma_r^{(1)}\sim A(r)-C(r).
\tag{2.1}
\]

For the runner-up `(r-1,r+1)`, put

\[
U_r^-:=U_{r-2}(3)
\]

(the hard length is `N=r-1`). The seam-tunneling theorem gives

\[
\boxed{
\Gamma_{r-1,r+1,q}
=A(r+1)-S_{r,n}+\text{higher algebraic truncation error},
}
\tag{2.2}

where

\[
\boxed{
S_{r,n}
=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_{r-2}(3)(r+1)^3}
\left(1+O(r^{-1})\right)
+O(U_{r-2}(3)^{-2}(r+1)^{-6}).
}
\tag{2.3}

For the opposite orientation,

\[
\Gamma_{r+1,r-1,q}
\sim A(r+1)-C(r+1).
\tag{2.4}

Since `S_(r,n)` is exponentially small and `C(r+1)~pi^2/[32(r+1)^4]`, the compressed-antiperiodic orientation remains the unique one-step runner-up for all sufficiently large `r`.

---

## 3. Excluding more distant geometries

Every other unbalanced geometry has

\[
M=\max\{N,m\}\ge r+2.
\]

The universal endpoint bound and the Robin series give a loss of order

\[
A(r+1)-A(r+2)
=
\frac{\pi^2}{2r^3}+O(r^{-4}),
\]

which dominates both the periodic cusp and the seam-tunneling correction. Hence no more distant geometry can beat `(r-1,r+1)` for large `r`.

---

## Theorem B — first-versus-second stability gap

Put

\[
\Delta_r=\Gamma_r^{(1)}-\Gamma_r^{(2)}.
\]

Then

\[
\boxed{
\Delta_r
=
A(r)-C(r)-A(r+1)+S_{r,n}
+	ext{arbitrary-order algebraic remainder}.
}
\tag{4.1}

In particular the algebraic expansion is

\[
\boxed{
\begin{aligned}
\Delta_r
={}&\frac{\pi^2}{2r^3}
-
\frac{\pi^2(25+24\sqrt2)}{32r^4}\\
&+
\frac{\pi^2}{r^5}
\left(
\frac52+\frac{99\sqrt2}{64}-\frac{\pi^2}{48}
\right)\\
&+
\frac{\pi^2}{r^6}
\left(
-\frac{1279}{256}
-\frac{91\sqrt2}{24}
+\frac{5\pi^2}{96}
+\frac{15\sqrt2\pi^2}{256}
\right)\\
&+O(r^{-7})
+S_{r,n}.
\end{aligned}}
\tag{4.2}

Thus

\[
\boxed{
\Delta_r\sim\frac{\pi^2}{2r^3}
=rac{256\pi^2}{p^3}.
}
\]

The first odd-multiplier dependence occurs only in the exponentially small positive correction `S_(r,n)`.

## 5. Variational interpretation

There are three scales:

1. balanced geometry is the unique optimum;
2. `(r-1,r+1)` is the unique runner-up;
3. the first-versus-second geometry gap is `Theta(r^-3)`, one algebraic order larger than the internal balanced phase-slip gain `Theta(r^-4)`.

The hard-channel tunneling correction lives beyond all powers and therefore does not alter the algebraic stability hierarchy.