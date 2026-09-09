# Theorem ledger after the geometry/global-gap upgrade

Date: 2026-09-09

Branch: `paper/circulant-periodic-gap-20260909`

This ledger supersedes the earlier status summary for the current research push. It separates proved results from the one remaining finite locking conjecture.

## I. Proved — variational and low-period theory

1. **Period-two variational classification.** Odd jumps have a unique alternating minimizer inside period dividing two; even jumps cannot go below squared edge `8` in that class.
2. **Odd sharp expansion.** The odd period-two gap has a complete high-order expansion with leading constant `pi^2`.
3. **Fixed period eight for `v_2(s)=1`.** For every `s=2 mod 4`, one period-eight phase has exact edge `4+sqrt(10+2sqrt5)`.

## II. Proved — general two-defect compression

4. **General signed-reflection chirality.** The separation-two two-defect phase has fiberwise spectral symmetry.
5. **General compression theorem.** For every even half-period `L>=4` and every jump `s=L(2q+1)`, the period-`2L` two-defect phase has global Bloch edge below `8`.
6. **2-adic compression.** If `2^k || s`, `k>=2`, period `2^(k+1)` suffices independently of the odd part.
7. **Period optimality in the reflection-chiral ansatz.** The period `2^(k+1)` is the shortest compatible primitive period.
8. **Odd-divisor period hierarchy.** Every odd divisor of the odd part of `s` produces a compatible primitive compressed period.

## III. Proved — exact spectral reduction and sharp global gap

9. **Exact two-phase characteristic equation.** The `2L x 2L` Bloch problem reduces to two Chebyshev quantities and the two real phase coordinates `(d,e)`.
10. **Exact endpoint Robin equation.** At `z=1`, the top squared root is characterized by `3 cos x_r+2 tan(x_r/(2r)) sin x_r=1`.
11. **Endpoint monotonicity.** The Robin root `x_r` strictly decreases to `arccos(1/3)`; the endpoint gap strictly decreases with `L`, and the endpoint edge strictly increases.
12. **Uniform global sharp compressed gap.** Uniformly in arbitrary varying odd multipliers,

\[
L^2(8-R_{L,q})\to4\arccos(1/3)^2.
\]

13. **Uniform quadratic finite scale.** There is an absolute `c_*>0` with

\[
c_*/L^2\le8-R_{L,q}<\pi^2/L^2
\]

for every even `L>=4` and every `q`.
14. **Multiplier-uniform eventual endpoint locking.** There exists an absolute `L_0` such that every `L>=L_0` and every odd multiplier have unique global maximizing phase `z=1`.
15. **Universal period-gap law.** For primitive period `p=2L`,

\[
p^2(8-R)\to16\arccos(1/3)^2.
\]

## IV. Proved — spectral-moment structure

16. Exact endpoint dominance for `tr H^2`, `tr H^4`, and `tr H^6` for every even `L>=6`.
17. For every fixed even moment order, endpoint dominance holds for all sufficiently large `L`.

These results explain why the compressed endpoint is spectrally preferred even before the exact edge theorem is invoked.

## V. Proved — arbitrary even defect separation

18. **Even-separation signed reflection.** Two positive local flux defects at any even separation possess the same signed-reflection chiral mechanism.
19. **Exact periodic-fiber factorization for separation `2h`.** The endpoint characteristic polynomial factors through defect polynomials `P_h,Q_h`.
20. **Defect-separation Robin hierarchy.** For fixed `h`,

\[
L^2e_{L,h}\to
\kappa_h,
\qquad
\kappa_h=4\arccos^2\!\frac1{T_h(3)}.
\]

21. **Global defect-separation hierarchy.** The same constant is the full continuous Bloch gap constant, uniformly in the odd multiplier:

\[
L^2\Gamma^{(h)}_{L,q}\to\kappa_h.
\]

22. **Fixed-separation phase rigidity and endpoint locking.** For every fixed `h`, maximizing phases satisfy `e->2`, `L^2(2-d)->0`, and for all sufficiently large `L` the exact unique maximizing phase is `z=1`, uniformly in the odd multiplier.
23. **Strict geometry ordering.** If `h_1<h_2` are fixed, then the wider separation has strictly larger global gap for all sufficiently large `L`, uniformly in the odd multiplier.
24. **Dirichlet bridge.** The constants satisfy

\[
4\arccos^2(1/3)=\kappa_1<\kappa_2<\cdots<\pi^2,
\qquad
\kappa_h\uparrow\pi^2.
\]

## VI. Proved — minimal period and the `pi^2` constant are compatible

25. For every `epsilon>0`, at sufficiently high `2`-adic valuation one can use the **minimal primitive period** `2^(k+1)` and still achieve

\[
2^{2k}(8-R)>\pi^2-\epsilon.
\]

26. There exists a slowly growing defect separation `h(k)=o(2^k)` for which the minimal-period compressed phases satisfy

\[
2^{2k}(8-R)\to\pi^2
\]

uniformly over arbitrary odd parts of the jump.

This shows that `pi^2` is a geometric Dirichlet limit of the compressed theory, not a special artifact of the old period-`4s` construction.

## VII. Verified / observed but not yet promoted

### V1. Exact finite endpoint threshold

Direct optimization and exact characteristic checks support

\[
\boxed{
L\ge6\Longrightarrow
R_{L,q}=\rho(H_{L,q}(1))^2
\quad\text{for every }q>=0.
}
\]

The proved theorem currently gives the same statement for all `L>=L_0` with an absolute but unoptimized `L_0`.

### V2. Small-layer discriminant positivity

For `L=6,8,10,12`, the relaxed endpoint discriminant is positive on `d<2`; Bernstein representations of the corresponding one-variable comparison polynomial have numerically positive coefficient certificates. These finite certificates have not yet been promoted to a human-readable exact proof package.

## VIII. Main open target

The only major finite refinement left in the separation-two compressed theory is to prove the sharp threshold

\[
\boxed{L_0=6.}
\]

Equivalently, with `y_L` the endpoint top squared root and

\[
P(y;d,e)=G_L(y,d)-e,
\]

prove

\[
\boxed{G_L(y_L,d)>2\qquad(-2\le d<2)}
\]

for every even `L>=6`.

A promising proof split is now:

1. use the multiplier-uniform limiting comparison profile to control all sufficiently large `L`;
2. convert the remaining finite layers into exact Bernstein/Sturm certificates;
3. optimize the large-`L` estimates until the finite certificate list collapses to `L=6,8,10,12` or smaller.