# Theorem ledger — periodic-gap paper after compression upgrades

Date: 2026-09-09

Branch: `paper/circulant-periodic-gap-20260909`

This ledger separates **Proved**, **Verified**, **Observed**, and **Open** statements after the 2026-09-09 theorem push.

## A. Proved headline results

### A1. Period-two variational classification

Status: **Proved**.

- odd jump: alternating period-two word is the unique minimizer inside period dividing two and has edge below `8`;
- even jump: no period-two word goes below `8`;
- unique odd optimizing Bloch phase;
- sharp constant `pi^2` and higher odd asymptotic expansion.

Primary file: `PERIOD_TWO_VARIATIONAL_THEORY.md`.

### A2. General two-defect reflection chirality

Status: **Proved**.

For even half-period `L>=4`, the two-defect word has

\[
\tau_{3-j}=-\tau_j,
\]

and for `s=L(2q+1)` the Bloch spectrum is fiberwise symmetric about zero.

Primary file: `TWO_DEFECT_REFLECTION_CHIRAL_THEOREM.md`.

### A3. General two-defect compression

Status: **Proved**.

For every even `L>=4` and every `q>=0`, the primitive period-`2L` two-defect phase satisfies

\[
R_{L,q}<8.
\]

Elementary explicit gap:

\[
8-R_{L,q}\ge16/8^{L-1}.
\]

Primary file: `GENERAL_TWO_DEFECT_COMPRESSION_THEOREM.md`.

### A4. 2-adic period compression

Status: **Proved**.

If

\[
2^k\Vert s,
\qquad k>=2,
\]

then period

\[
2^{k+1}
\]

suffices, independently of the odd part of `s`.

This supersedes the old period-`4s` existence theorem as the shortest known general even-jump construction.

### A5. Period optimality inside the reflection-chiral two-defect ansatz

Status: **Proved**.

Compatibility requires

\[
s\equiv L\pmod{2L}
\iff L\mid s\text{ and }s/L\text{ odd}.
\]

Hence `v_2(L)=v_2(s)`, and the minimal compatible primitive period is exactly

\[
2^{v_2(s)+1}.
\]

Primary file: `TWO_DEFECT_PERIOD_OPTIMALITY.md`.

### A6. Exact two-phase characteristic equation

Status: **Proved**.

The full squared characteristic polynomial is

\[
P(y)=u^2A(y,d)+uwB(y,d)+C(y,d)-e,
\]

with explicit `A,B,C` and Chebyshev factors `u,w`.

This reduces the growing `2L x 2L` Bloch problem to a two-phase scalar equation.

Primary file: `GENERAL_TWO_PHASE_CHARACTERISTIC_EQUATION.md`.

### A7. Exact endpoint Robin equation

Status: **Proved**.

At `z=1`, the top squared root is

\[
6+2\cos(x_r/r),
\qquad r=L/2,
\]

where

\[
3\cos x_r+2\tan(x_r/(2r))\sin x_r=1.
\]

Sharp endpoint constant:

\[
L^2e_L\to4\arccos(1/3)^2.
\]

A full expansion through `L^-4` is proved.

Primary file: `COMPRESSED_ENDPOINT_SHARP_GAP.md`.

### A8. Uniform global sharp compressed gap

Status: **Proved**.

For arbitrary sequences `q=q(L)`,

\[
L^2(8-R_{L,q})
\to4\arccos(1/3)^2.
\]

Maximizing phases satisfy

\[
e=z+z^{-1}\to2,
\qquad
L^2(2-d)\to0.
\]

Primary file: `GLOBAL_COMPRESSED_SHARP_GAP.md`.

### A9. Fixed odd multiplier eventual endpoint locking

Status: **Proved**.

For each fixed odd multiplier `2q+1`, there is `L_0(q)` such that

\[
R_{L,q}=\rho(H_{L,q}(1))^2
\]

for every even `L>=L_0(q)`.

Hence the endpoint expansion becomes the exact global expansion in that regime.

Primary file: `FIXED_ODD_MULTIPLIER_ENDPOINT_DOMINANCE.md`.

### A10. Universal period-gap law

Status: **Proved**.

For compressed primitive period `p=2L`, uniformly in the residual odd multiplier,

\[
p^2(8-R)\to16\arccos(1/3)^2.
\]

Primary file: `ODD_DIVISOR_PERIOD_GAP_HIERARCHY.md`.

### A11. Odd-divisor hierarchy

Status: **Proved**.

If `s=2^k n` with `n` odd, every odd divisor `d|n` supplies a primitive compressed period

\[
p_d=2^{k+1}d
\]

with edge below `8`.

The shortest member `d=1` is period-optimal inside the ansatz and has the largest leading-order gap inside this divisor hierarchy.

### A12. Spectral moment hierarchy

Status: **Proved**.

Exact endpoint dominance for

\[
\operatorname{tr}H^{2m},\qquad m=1,2,3,
\]

holds for every even `L>=6`.

Primary files:

- `SPECTRAL_MASS_ENDPOINT_THEOREM.md`;
- `FOURTH_SPECTRAL_MOMENT_THEOREM.md`;
- `SIXTH_SPECTRAL_MOMENT_THEOREM.md`.

For every fixed `m`, endpoint dominance holds for all sufficiently large `L`.

Primary file: `ALL_FIXED_MOMENTS_ENDPOINT_DOMINANCE.md`.

---

## B. Earlier proved comparison results retained in the paper

### B1. Fixed period-eight exact class for `v_2(s)=1`

Status: **Proved**.

For every `s=2 mod 4`, one fixed period-eight phase has the exact edge

\[
4+\sqrt{10+2\sqrt5}<8.
\]

Primary file: `UNIFORM_PERIOD8_MOD4_THEOREM.md`.

### B2. Older period-`4s` even family

Status: **Proved**, but no longer the headline existence theorem.

It remains useful for:

- `s^2 g_s -> pi^2` for that explicit family;
- boundary-layer phase slip;
- higher-order phase-slip comparison.

It should be presented as a distinct asymptotic mechanism, not as the strongest short-period construction.

---

## C. Verified but not promoted to theorem

### C1. Direct determinant audits

Status: **Verified**.

The exact two-phase characteristic formula has been checked numerically against direct Bloch determinants for multiple values of `L,q,z,y`.

These checks are audits only; the analytic transfer proof is the theorem source.

### C2. Finite endpoint dominance data

Status: **Verified/Observed**, not yet a theorem.

Extensive direct optimization supports

\[
L\ge6
\Longrightarrow
z=1\text{ is globally maximizing for every odd multiplier}.
\]

Tests include large odd multipliers well beyond the original search range.

This statement must remain outside the theorem list until the one-variable positivity problem is closed.

---

## D. Main open theorem

The strongest remaining finite target is

\[
\boxed{
L\ge6
\Longrightarrow
R_{L,q}=\rho(H_{L,q}(1))^2
\text{ for every }q>=0.}
\]

Using the exact characteristic equation, it is enough to prove the endpoint discriminant inequality

\[
G_L(y_L,d)>2
\qquad(-2\le d<2),
\]

where `y_L` is the endpoint top squared root and

\[
P(y;d,e)=G_L(y,d)-e.
\]

Numerically, for `L>=6`, `G_L(y_L,d)-2` is positive on `[-2,2)` and has its unique physical zero at `d=2`.

For `L>=14`, numerical root analysis further indicates that `G_L(y_L,d)` is already monotone decreasing in `d` throughout `[-2,2]`; for `L=6,8,10,12` it has one interior critical point, which is a maximum. This suggests a feasible proof split:

1. analytic monotonicity for all sufficiently large `L`;
2. exact Bernstein/Sturm certificates for the finite small layers.

This is the next target. No claim of proof is made yet.
