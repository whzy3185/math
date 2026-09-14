# All-orders global gap phase diagram across the balanced transition

Date: 2026-09-14

Status: **Proved; corrected beyond-all-orders scale**.

Let

\[
L=2(N+m),
\qquad N,m\to\infty,
\]

with comparable ratio, and let `n=2q+1`.

Define the universal endpoint Robin series

\[
A(\ell)=\sum_{j\ge2}a_j\ell^{-j}
\]

and the periodic cusp-gain series

\[
C(N)=\sum_{j\ge0}c_jN^{-j-4}.
\]

## Theorem A — periodic/balanced branch

If

\[
\boxed{m\le N,}
\]

then to every algebraic order

\[
\boxed{
\Gamma_{N,m,q}\sim A(N)-C(N).
}
\]

The maximizing compressed phase has the all-orders periodic phase-slip series.

## Theorem B — compressed-antiperiodic branch

If

\[
\boxed{m>N,}
\]

then to every algebraic order

\[
\boxed{
\Gamma_{N,m,q}\sim A(m).
}
\]

The first beyond-all-orders correction is explicit. Put

\[
U_N=U_{N-1}(3).
\]

Then

\[
\boxed{
\Gamma_{N,m,q}
=A(m)-S_{N,m,n}
+\text{higher algebraic truncation error},
}
\]

where

\[
\boxed{
S_{N,m,n}
=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_Nm^3}
\left(1+O(m^{-1})\right)
+O(U_N^{-2}m^{-6}).
}
\]

The maximizing physical phase is exponentially close to

\[
z_0=e^{\pm i\pi/n},
\]

with compressed displacement

\[
\boxed{
\delta_*
=-
\frac{\pi^2\sin(\pi/n)}
{64\sqrt2\,n\,U_Nm^3}
(1+O(m^{-1}))
+O(U_N^{-2}m^{-6}).
}
\]

Thus the first odd-multiplier dependence lives at scale

\[
U_N^{-1}m^{-3}=\Theta((3+2\sqrt2)^{-N}m^{-3}),
\]

beyond every algebraic order.

## First coefficients

The endpoint series begins

\[
\begin{aligned}
A(\ell)={}&\frac{\pi^2}{4\ell^2}
-\frac{\sqrt2\pi^2}{4\ell^3}
+\frac{\pi^2(72-\pi^2)}{192\ell^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256\ell^5}
+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040\ell^6}
+\cdots,
\end{aligned}
\]

and

\[
C(N)=\frac{\pi^2}{32N^4}
-\frac{3\pi^2}{32\sqrt2N^5}
+\frac{\pi^2(32\sqrt2-3)}{768N^6}
+\cdots.
\]

Hence the periodic/balanced global branch begins

\[
\begin{aligned}
A(N)-C(N)={}&\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}
+\frac{\pi^2(66-\pi^2)}{192N^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256N^5}
+\cdots.
\end{aligned}
\]

## Algebraic switch

The integer geometry selects

\[
\boxed{
\begin{cases}
A(N)-C(N),&m\le N,\\
A(m),&m>N,
\end{cases}}
\]

to every algebraic order. The balanced point belongs to the periodic-cusp side. The physical seam on the `m>N` side changes only the transseries sector, not the algebraic coefficients.

Primary supporting files:

- `ALL_ORDERS_MACROSCOPIC_ROBIN_EXPANSION.md`;
- `ALL_ORDERS_PERIODIC_PHASE_SLIP_EXPANSION.md`;
- `ANTIPERIODIC_SEAM_TUNNELING_ASYMPTOTIC.md`.