# Current headline theorem architecture — Paper I

Date: 2026-09-09

Branch: `paper/circulant-periodic-gap-20260909`

This file is the current headline theorem package after the compression, geometry, and bound-state pushes. It supersedes earlier editorial theorem lists. All statements below concern explicit periodic phases only; none concerns minimization over all finite signings.

## Headline I — exact smallest-period variational bifurcation

Among signings with period dividing two, the alternating phase is the unique minimizer up to translation. It is sub-eight exactly for odd jumps. Its gap has a full asymptotic expansion beginning

\[
g_s=\frac{\pi^2}{s^2}
-\frac{\pi^2(\pi^2+12)}{12s^4}+O(s^{-6}).
\]

This establishes an exact parity bifurcation in the smallest nontrivial periodic sector.

## Headline II — two-defect signed reflection and exact transfer compression

For even half-period `L`, two positive local flux defects at even separation give a signed-reflection chiral symmetry whenever

\[
s=L(2q+1).
\]

For the separation-two family the full `2L x 2L` Bloch characteristic equation reduces to two Chebyshev functions and two real phase coordinates. The threshold and arbitrary-energy equations are exact.

## Headline III — 2-adic minimal-period compression

If

\[
2^k\Vert s,
\qquad k\ge2,
\]

then an explicit separation-two phase of primitive period

\[
\boxed{2^{k+1}}
\]

has global continuous squared Bloch edge below `8`. This period is minimal inside the natural reflection-chiral two-defect mechanism.

Thus the required existence period depends only on the `2`-adic valuation, not on the odd part of the jump.

## Headline IV — sharp global compressed gap

For the period-`2L` separation-two compressed phase,

\[
\boxed{
L^2(8-R_{L,q})
\to4\arccos^2(1/3)
}
\]

uniformly over arbitrary varying odd multipliers. The true finite gap has uniform quadratic scale

\[
\frac{c_*}{L^2}\le8-R_{L,q}<\frac{\pi^2}{L^2}.
\]

Maximizing phases are rigid, and there is an absolute multiplier-independent threshold beyond which the unique maximizing Bloch phase is exactly `z=1`.

The endpoint Robin roots are strictly monotone and obey explicit finite localization estimates.

## Headline V — exact small-layer endpoint locking

For

\[
L=6,8,10,12
\]

and every odd multiplier, `z=1` is already the unique global maximizing phase. The proof uses exact algebraic endpoint isolation and positive rational bivariate Bernstein certificates.

The layer `L=4` is genuinely exceptional.

The remaining finite refinement is to prove that the universal locking threshold is exactly

\[
\boxed{L_0=6.}
\]

## Headline VI — global defect-separation Robin hierarchy

For fixed defect separation `2h`, define

\[
C_h=T_h(3),
\qquad
\kappa_h=4\arccos^2(1/C_h).
\]

Then, uniformly over arbitrary odd multipliers,

\[
\boxed{
L^2(8-R^{(h)}_{L,q})\to\kappa_h.
}
\]

For every fixed `h`, maximizing phases are asymptotically rigid and eventually lock exactly to `z=1` with a threshold independent of the odd multiplier.

The constants are strictly ordered:

\[
4\arccos^2(1/3)=\kappa_1<\kappa_2<\cdots<\pi^2.
\]

Hence wider **fixed** defect blocks are eventually spectrally better.

## Headline VII — sharp geometry-to-Dirichlet rate

Let

\[
q_*=3-2\sqrt2.
\]

Then

\[
\boxed{
\pi^2-\kappa_h
=8\pi q_*^h
-16q_*^{2h}
-\frac{8\pi}{3}q_*^{3h}
+O(q_*^{4h}).
}
\]

Thus the Robin hierarchy approaches the Dirichlet constant exponentially fast, with exact transfer multiplier `3-2sqrt2`.

## Headline VIII — minimal period and the Dirichlet constant are compatible

For jumps with high `2`-adic valuation, one can keep the primitive period at the minimum allowed value

\[
2^{k+1}
\]

while choosing the defect width slowly enough that

\[
\boxed{
2^{2k}(8-R)\to\pi^2
}
\]

uniformly over arbitrary odd parts of the jump.

Therefore `pi^2` is not an artifact of the old period-`4s` family. It is the limiting Dirichlet constant of the compressed geometry itself.

## Headline IX — fixed-complement bound-state obstruction

The geometry hierarchy has a sharp limitation. If

\[
L=2r,
\qquad h=r-k
\]

with fixed `k>=1`, so that only `2k` generic sites remain, then for all sufficiently large `r` the antiperiodic fiber has a squared eigenvalue above `8`.

For each fixed `k`, its limiting above-edge bound state is parametrized by a physical root `a_k in (0,1)` of an explicit Chebyshev secular polynomial, with

\[
y_k=6+a_k+a_k^{-1}>8.
\]

As `k->infinity`,

\[
1-a_k\sim\frac2{T_k(3)},
\]

and

\[
\boxed{
y_k-8
\sim\frac4{T_k(3)^2}
\sim16(3-2\sqrt2)^{2k}.}
\]

The extreme `k=1` value is

\[
\boxed{
y_1=\frac{38+10\sqrt{13}}9.}
\]

Thus the fixed-width sub-eight hierarchy and the macroscopic-width above-edge hierarchy are separated by a genuine scaling problem.

## New open phase-transition problem

The current central open geometry question is no longer whether larger fixed width improves the gap. That is proved. It is:

> If the defect width `h=h(L)` and generic complement `r-h` both vary, determine the precise growth window separating sub-eight compressed phases from antiperiodic above-edge bound states.

The fixed-complement theorem shows failure when `r-h` is bounded. The exponential law

\[
(3-2\sqrt2)^{2(r-h)}
\]

suggests a logarithmic transition when compared with the `L^-2` finite-size gap, but no logarithmic threshold theorem is claimed yet.

## Editorial thesis

The paper should now be organized around a two-sided periodic phase diagram:

\[
\text{period-two parity bifurcation}
\to
\text{2-adic period compression}
\to
\text{Robin gap hierarchy}
\to
\text{Dirichlet limit}
\to
\text{wide-defect bound-state obstruction}.
\]

This is substantially stronger than the earlier story of a single parity-dependent family with a `pi^2/s^2` gap.