# Discrete one-lattice-step transition across balanced defect geometry

Date: 2026-09-14

Status: **Proved; corrected beyond-all-orders scale**.

Let

\[
m=N+j,
\qquad j\in\mathbb Z
\]

with fixed `j` and `N->infinity`.

The periodic optimized branch is

\[
\Gamma_+(N)
=\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}
+\frac{\pi^2(66-\pi^2)}{192N^4}
+O(N^{-5}).
\]

The compressed-antiperiodic algebraic branch is the universal endpoint series `A(N+j)`, with a physical-seam correction beyond all powers.

## Theorem — one-lattice-step switch

For every fixed integer `j`, for all sufficiently large `N`:

- `j<=-1`: the periodic cusp branch is globally selected;
- `j=0`: the periodic cusp resolves the balanced degeneracy;
- `j>=1`: the compressed-antiperiodic branch is globally selected.

The algebraic splitting is

\[
\boxed{
\Gamma_+(N)-A(N+j)
=
\frac{\pi^2j}{2N^3}
-
\frac{\pi^2(24j^2+24\sqrt2 j+1)}{32N^4}
+O_j(N^{-5}).
}
\]

Thus a one-site imbalance costs `Theta(N^-3)`, while the balanced periodic cusp is only `Theta(N^-4)`.

Formally the continuous equality would occur at

\[
j\sim\frac1{16N},
\]

so the physical integer lattice jumps directly from `j=0` to `j=1`.

## Correct positive-side phase location

For `j>=1`, let `n=2q+1`, put

\[
U_N=U_{N-1}(3),
\]

and choose the best exact compressed-antiperiodic root

\[
z_0=e^{\pm i\pi/n}.
\]

The true maximizing phase is

\[
z_*=z_0e^{i\delta_*/n},
\]

where

\[
\boxed{
\delta_*
=-
\frac{\pi^2\sin(\pi/n)}
{64\sqrt2\,n\,U_N(N+j)^3}
(1+O(N^{-1}))
+O(U_N^{-2}N^{-6}).
}
\]

The corresponding seam correction to the gap is

\[
\boxed{
 e^-_{N,N+j}-\Gamma_{N,N+j,q}
=
\frac{(2+2\cos(\pi/n))\pi^2}
{64\sqrt2\,U_N(N+j)^3}
(1+O(N^{-1}))
+O(U_N^{-2}N^{-6}).
}
\]

This correction is exponentially smaller than the `N^-3` integer orientation splitting and does not alter the one-lattice-step transition.