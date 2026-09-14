# Theorem ledger update — 2026-09-14

Branch: `paper/circulant-periodic-gap-20260909`

This file records the September 14 high-order push and supersedes any earlier interpretation that treated the periodic and antiperiodic wells as locally symmetric.

## H14-1. High-order endpoint expansion

Status: **Proved**.

For a macroscopic soft length `ell` at either special endpoint,

\[
\begin{aligned}
e_\ell={}&\frac{\pi^2}{4\ell^2}
-\frac{\sqrt2\pi^2}{4\ell^3}
+\frac{\pi^2(72-\pi^2)}{192\ell^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256\ell^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040\ell^6}
+O(\ell^{-7}).
\end{aligned}
\]

Primary file: `MACROSCOPIC_ENDPOINT_HIGH_ORDER_EXPANSION.md`.

## H14-2. Periodic/balanced phase-slip coefficients through sixth order

Status: **Proved**.

At the periodic soft well,

\[
|\delta_N|
=\frac\pi{4\sqrt2 N^2}
-\frac\pi{8N^3}
+\frac{\pi(32-27\sqrt2)}{192N^4}
+O(N^{-5}),
\]

and

\[
e^+_{N,m}-\Gamma
=\frac{\pi^2}{32N^4}
-\frac{3\pi^2}{32\sqrt2 N^5}
+\frac{\pi^2(32\sqrt2-3)}{768N^6}
+O(N^{-7}).
\]

For balanced `N=m=r`, these are the global phase-slip expansions.

Primary file: `HIGH_ORDER_MACROSCOPIC_PHASE_SLIP.md`.

## H14-3. Exact antiperiodic locking for `m>N`

Status: **Proved**.

If

\[
m/N\to\gamma>1,
\]

then for all sufficiently large parameters and every odd multiplier,

\[
\boxed{R_{N,m,q}=\rho(H(-1))^2.}
\]

The antiperiodic top branch is analytic and strictly quadratic in the local compressed displacement; there is no `|delta|` cusp.

Primary file: `ANTIPERIODIC_EXACT_LOCKING_AND_HIGH_ORDER_GAP.md`.

## H14-4. Antiperiodic-dominant global gap through sixth order

Status: **Proved**.

When `m/N -> gamma>1`,

\[
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4m^2}
-\frac{\sqrt2\pi^2}{4m^3}
+\frac{\pi^2(72-\pi^2)}{192m^4}\\
&+\frac{\sqrt2\pi^2(-64+3\pi^2)}{256m^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2+7200)}{23040m^6}
+O(m^{-7}).
\end{aligned}
\]

No phase-slip subtraction appears.

## H14-5. Periodic-dominant and balanced global gap through sixth order

Status: **Proved**.

For `m/N -> gamma<1`, with `N` the dominant soft length,

\[
\begin{aligned}
\Gamma_{N,m,q}={}&\frac{\pi^2}{4N^2}
-\frac{\sqrt2\pi^2}{4N^3}
+\frac{\pi^2(66-\pi^2)}{192N^4}\\
&+\frac{\sqrt2\pi^2(-52+3\pi^2)}{256N^5}\\
&+\frac{\pi^2(\pi^4-750\pi^2-960\sqrt2+7290)}{23040N^6}
+O(N^{-7}).
\end{aligned}
\]

The balanced case has the same algebraic expansion with `N=m=r` because the periodic cusp wins by `Theta(r^-4)` over the exponentially close endpoint values.

Primary file: `MACROSCOPIC_GLOBAL_GAP_HIGH_ORDER_PHASE_DIAGRAM.md`.

## Retraction / correction record

The note `MACROSCOPIC_ANTIPERIODIC_WELL_PHASE_SLIP.md` created on September 14 was removed after hostile audit. Direct Bloch evaluation and the local transfer expansion show that the antiperiodic well is analytic and exactly locked.

`BALANCED_TWO_DEFECT_PHASE_SLIP.md` was corrected accordingly: the two endpoint gaps agree algebraically, but only the periodic well carries the cusp.

## Current structural picture

The balanced transition is asymmetric beyond leading order:

- `N>m`: periodic avoided-crossing cusp, algebraic phase slip;
- `N=m`: periodic cusp beats both endpoint values and determines the global correction;
- `m>N`: antiperiodic simple root, exact locking.

The first orientation-sensitive term in the global spectral gap appears at order `ell^-4`.