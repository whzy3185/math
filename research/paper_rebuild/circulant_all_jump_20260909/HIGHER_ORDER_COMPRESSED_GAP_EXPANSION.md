# Higher-order expansion for the compressed two-defect spectral gap

Date: 2026-09-09

Status: **Proved**. This note uses the eventual exact phase-selection theorem: for all sufficiently large even `L`, the global compressed Bloch gap equals the periodic-phase endpoint gap exactly.

Let

\[
a:=\arccos\frac13.
\]

For sufficiently large even `L`, write

\[
g_{L,q}=8-R_{L,q}.
\]

The result is uniform in `q` because the exact maximizing phase is `z=1`, where the fiber is independent of the odd multiplier.

---

## 1. Scalar endpoint equation

Put

\[
r=L/2.
\]

The top squared eigenvalue at `z=1` is

\[
6+2\cos\theta_r,
\]

where the unique soft angle is characterized by

\[
3\cos(r\theta_r)
+2\tan(\theta_r/2)\sin(r\theta_r)=1.
\tag{1.1}
\]

Set

\[
a_r=r\theta_r.
\]

Then

\[
\boxed{
3\cos a_r
+2\tan\left(\frac{a_r}{2r}\right)\sin a_r=1.
}
\tag{1.2}
\]

Since

\[
\partial_x(3\cos x-1)|_{x=a}=-3\sin a\ne0,
\]

the analytic implicit-function theorem gives a full convergent/asymptotic power series for `a_r` in `r^{-1}` near infinity.

---

## 2. Expansion of the Robin angle

Substitute

\[
a_r
=a+\frac{c_1}{r}+\frac{c_2}{r^2}+\frac{c_3}{r^3}+O(r^{-4})
\]

into (1.2) and compare powers of `r^{-1}`. Using

\[
\cos a=\frac13,
\qquad
\sin a=\frac{2\sqrt2}{3},
\]

one obtains

\[
\boxed{c_1=\frac a3,}
\tag{2.1}
\]

\[
\boxed{
c_2=\frac{a(\sqrt2\,a+8)}{72},
}
\tag{2.2}
\]

and

\[
\boxed{
c_3=
\frac{a(10a^2+9\sqrt2\,a+24)}{648}.
}
\tag{2.3}
\]

Thus

\[
\boxed{
\begin{aligned}
a_r={}&a+\frac{a}{3r}
+\frac{a(\sqrt2\,a+8)}{72r^2}\\
&+\frac{a(10a^2+9\sqrt2\,a+24)}{648r^3}
+O(r^{-4}).
\end{aligned}}
\tag{2.4}
\]

The coefficients at every subsequent order are obtained recursively because the coefficient multiplying the new unknown is always `-3 sin a`, which is nonzero.

---

## 3. Expansion of the global gap

For all sufficiently large even `L`, exact phase selection gives

\[
g_{L,q}=4\sin^2\left(\frac{a_r}{2r}\right).
\tag{3.1}
\]

Since `L=2r`, substitution of (2.4) gives

\[
\boxed{
L^2g_{L,q}
=\Gamma_0+rac{\Gamma_1}{L}
+\frac{\Gamma_2}{L^2}
+\frac{\Gamma_3}{L^3}
+O(L^{-4}),
}
\tag{3.2}
\]

where

\[
\boxed{\Gamma_0=4a^2,}
\tag{3.3}
\]

\[
\boxed{\Gamma_1=\frac{16a^2}{3},}
\tag{3.4}
\]

\[
\boxed{
\Gamma_2
=\frac{16a^2}{3}
+\frac{4\sqrt2\,a^3}{9}
-\frac{4a^4}{3},
}
\tag{3.5}
\]

and

\[
\boxed{
\Gamma_3
=\frac{16a^2}{81}
\left(24+6\sqrt2\,a-13a^2\right).
}
\tag{3.6}
\]

Numerically,

\[
\Gamma_0=6.0610443485\ldots,
\]

\[
\Gamma_1=8.0813924647\ldots,
\]

\[
\Gamma_2=6.1924048518\ldots,
\]

\[
\Gamma_3=4.4138299511\ldots .
\]

Equivalently,

\[
\boxed{
\begin{aligned}
g_{L,q}={}&
\frac{4a^2}{L^2}
+\frac{16a^2}{3L^3}\\
&+\frac{1}{L^4}
\left(
\frac{16a^2}{3}
+\frac{4\sqrt2\,a^3}{9}
-\frac{4a^4}{3}
\right)\\
&+\frac{16a^2(24+6\sqrt2\,a-13a^2)}{81L^5}
+O(L^{-6}).
\end{aligned}}
\tag{3.7}
\]

All displayed coefficients are independent of the odd multiplier `2q+1`.

---

## 4. All-order consequence

The exact phase-selection theorem reduces the full large-period spectral problem to the analytic scalar equation (1.2). Therefore, for every fixed integer `M>=0`, there exist explicit constants

\[
\Gamma_0,\Gamma_1,\ldots,\Gamma_M
\]

such that, uniformly in `q`,

\[
\boxed{
L^2g_{L,q}
=\sum_{j=0}^{M}\Gamma_jL^{-j}
+O_M(L^{-M-1}).
}
\tag{4.1}
\]

The coefficients are generated recursively by formal substitution into (1.2), followed by the elementary expansion of `4 sin^2(a_r/(2r))`.

Thus the compressed family has not only a sharp leading constant but a complete algebraic asymptotic expansion controlled by a one-dimensional Robin quantization law.
