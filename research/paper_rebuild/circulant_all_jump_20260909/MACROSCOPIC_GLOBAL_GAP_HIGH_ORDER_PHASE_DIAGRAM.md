# High-order global gap phase diagram across the balanced transition

Date: 2026-09-14

Status: **Proved; corrected beyond-all-orders term**.

Let

\[
L=2(N+m),
\qquad N,m\to\infty,
\]

with comparable ratio, and put `n=2q+1`.

## Theorem A — periodic-dominant expansion

If

\[
m/N\to\gamma\in(0,1),
\]

then

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}
+\frac{\pi^2(66-\pi^2)}{192N^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256N^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2-960\sqrt2+7290)}{23040N^6}
+O(N^{-7}).
\end{aligned}}
\]

## Theorem B — compressed-antiperiodic-dominant expansion

If

\[
m/N\to\gamma\in(1,\infty),
\]

then

\[
\boxed{
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}
+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7})-S_{N,m,n},
\end{aligned}}
}
\]

where

\[
\boxed{
S_{N,m,n}
=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_{N-1}(3)m^3}
\left(1+O(m^{-1})\right)
+O(U_{N-1}(3)^{-2}m^{-6}).
}
\]

Thus all displayed algebraic coefficients are independent of the odd multiplier; its first effect is the positive tunneling subtraction `S_(N,m,n)` beyond every algebraic order.

## Theorem C — balanced expansion

For

\[
N=m=r,
\]

the periodic cusp resolves the endpoint degeneracy, giving

\[
\boxed{
\begin{aligned}
\Gamma_r={}&\frac{\pi^2}{4r^2}
-\frac{\sqrt2\pi^2}{4r^3}
+\frac{\pi^2(66-\pi^2)}{192r^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256r^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2-960\sqrt2+7290)}{23040r^6}
+O(r^{-7}).
\end{aligned}}
}
\]

## Structural consequence

The endpoint Robin series is orientation-independent.  The periodic side acquires an algebraic cusp beginning at fourth order, while the compressed-antiperiodic side acquires only the exponentially small seam-tunneling term above.  Hence the first algebraic orientation-sensitive coefficient occurs at order four, and the first odd-multiplier-sensitive coefficient occurs beyond all algebraic orders.