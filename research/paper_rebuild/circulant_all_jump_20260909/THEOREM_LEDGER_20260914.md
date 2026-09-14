# Theorem ledger update — 2026-09-14

Branch: `paper/circulant-periodic-gap-20260909`

This file records the September 14 high-order push and supersedes any earlier interpretation that treated the periodic and antiperiodic wells as locally symmetric.

## H14-1. Universal all-orders endpoint Robin expansion

Status: **Proved**.

There is a universal coefficient sequence `a_2,a_3,...` such that, for every fixed order `K`,

\[
e^+_{N,m}=\sum_{j=2}^K a_jN^{-j}+O(N^{-K-1})+O(\Lambda^{-2m}),
\]

and

\[
e^-_{N,m}=\sum_{j=2}^K a_jm^{-j}+O(m^{-K-1})+O(\Lambda^{-2N}),
\]

uniformly on compact macroscopic ratio ranges. The coefficients are identical at the periodic and antiperiodic endpoints to every algebraic order.

The first coefficients are

\[
a_2=\frac{\pi^2}{4},\qquad
a_3=-\frac{\sqrt2\pi^2}{4},
\]

\[
a_4=\frac{\pi^2(72-\pi^2)}{192},\qquad
a_5=\frac{\sqrt2\pi^2(-64+3\pi^2)}{256},
\]

\[
a_6=\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040}.
\]

Primary file: `ALL_ORDERS_MACROSCOPIC_ROBIN_EXPANSION.md`.

## H14-2. Universal all-orders periodic phase-slip expansion

Status: **Proved**.

At the periodic soft well the improving branch admits a full analytic boundary-layer expansion. The maximizing compressed displacement has

\[
|\delta_N|
=N^{-2}\left(b_0+b_1N^{-1}+b_2N^{-2}+\cdots\right),
\]

and the phase-slip gain has

\[
e^+_{N,m}-\Gamma
=N^{-4}\left(c_0+c_1N^{-1}+c_2N^{-2}+\cdots\right).
\]

The first coefficients are

\[
b_0=\frac\pi{4\sqrt2},\qquad
b_1=-\frac\pi8,\qquad
b_2=\frac{\pi(32-27\sqrt2)}{192},
\]

and

\[
c_0=\frac{\pi^2}{32},\qquad
c_1=-\frac{3\pi^2}{32\sqrt2},\qquad
c_2=\frac{\pi^2(32\sqrt2-3)}{768}.
\]

Primary file: `ALL_ORDERS_PERIODIC_PHASE_SLIP_EXPANSION.md`.

## H14-3. Uniform integer orientation-selection theorem

Status: **Proved**.

For all sufficiently large comparable integer pairs `(N,m)`:

\[
\boxed{m\le N}
\]

selects the periodic cusp branch globally, while

\[
\boxed{m>N}
\]

selects exact antiperiodic locking:

\[
\boxed{z=-1}.
\]

Thus the physical higher-order transition is exactly on the integer hyperplane `m=N`.

Primary file: `UNIFORM_INTEGER_ORIENTATION_SELECTION.md`.

## H14-4. One-lattice-step near-balanced transition

Status: **Proved**.

For fixed integer `j=m-N`,

- `j<=-1`: periodic phase-slip branch wins;
- `j=0`: periodic cusp wins an endpoint degeneracy at order `N^-4`;
- `j>=1`: exact antiperiodic locking wins already at order `N^-3`.

The two competing gaps satisfy

\[
\Gamma_+(N)-e_-(N+j)
=
\frac{\pi^2j}{2N^3}
-
\frac{\pi^2(24j^2+24\sqrt2 j+1)}{32N^4}
+O_j(N^{-5}).
\]

The formal continuous crossover would occur at

\[
 m-N\sim\frac1{16N},
\]

which is invisible on the integer lattice. Hence the physical transition jumps directly from `j=0` to `j=1`.

Primary file: `DISCRETE_NEAR_BALANCED_TRANSITION.md`.

## H14-5. All-orders global gap phase diagram

Status: **Proved**.

Let `A(ell)=sum a_j ell^-j` be the universal Robin formal series and let `C(N)=sum c_j N^(-j-4)` be the periodic cusp-gain series. Then the full global gap is described to arbitrary algebraic order by only two universal formal series:

\[
\boxed{
\Gamma_{N,m,q}\sim A(N)-C(N),\qquad m\le N,
}
\]

and

\[
\boxed{
\Gamma_{N,m,q}\sim A(m),\qquad m>N.
}
\]

At balance, the periodic cusp branch is selected. The first orientation-sensitive coefficient occurs at fourth order.

Primary file: `ALL_ORDERS_GLOBAL_GAP_PHASE_DIAGRAM.md`.

## H14-6. Exact antiperiodic locking on the `m>N` side

Status: **Proved**.

The antiperiodic top root is analytic and strictly quadratic in local phase displacement. There is no `|delta|` cusp. Combining local analyticity with the integer endpoint advantage gives eventual exact locking at `z=-1` throughout the macroscopic `m>N` region.

Primary file: `ANTIPERIODIC_EXACT_LOCKING_AND_HIGH_ORDER_GAP.md`.

## H14-7. Sixth-order displayed global formulas

Status: **Proved**, now viewed as the first terms of H14-5.

For the periodic/balanced branch,

\[
\begin{aligned}
\Gamma={}&\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}
+\frac{\pi^2(66-\pi^2)}{192N^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256N^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2-960\sqrt2+7290)}{23040N^6}
+O(N^{-7}).
\end{aligned}
\]

For the antiperiodic branch,

\[
\begin{aligned}
\Gamma={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}
+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7}).
\end{aligned}
\]

Primary file: `MACROSCOPIC_GLOBAL_GAP_HIGH_ORDER_PHASE_DIAGRAM.md`.

## Retraction / correction record

The note `MACROSCOPIC_ANTIPERIODIC_WELL_PHASE_SLIP.md` created on September 14 was removed after hostile audit. Direct Bloch evaluation and the local transfer expansion show that the antiperiodic well is analytic and exactly locked.

`BALANCED_TWO_DEFECT_PHASE_SLIP.md` was corrected accordingly: the two endpoint gaps agree algebraically, but only the periodic well carries the cusp.

## Current structural picture

The high-order transition is now completely organized:

- `N>m`: periodic avoided-crossing cusp with an all-orders algebraic phase-slip series;
- `N=m`: the same periodic cusp resolves an endpoint degeneracy and determines the global branch;
- `m>N`: antiperiodic simple root with eventual exact locking and only the universal Robin series.

Because `m-N` is integral, the formal `O(N^-1)` continuous crossover window contains only the balanced lattice point for all sufficiently large `N`. The physical transition is therefore a one-lattice-step spectral switch rather than a broad crossover band.