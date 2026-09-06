# All-`s` sharp quadratic-gap and finite-obstruction workstream

Branch: `research/quadratic-gap-upgrade`
Date: 2026-09-06

This workstream has two complementary main results:

1. a sharp periodic/Bloch theory for explicit signings for every jump
   `s>=2`;
2. a genuine finite-order all-signing obstruction family on `N=3s` for odd
   `s>=7`.

The frozen period-eight manuscript and `formal/TargetA` remain unchanged.

## Headline Bloch result

For the parity-dependent explicit periodic family, with squared Bloch radius
`Rhat_s` and gap `ghat_s=8-Rhat_s`,

\[
 \boxed{s^2\widehat g_s\to\pi^2}
\]

through all integer jumps.

For even `s=2r`, the phase slip is resolved beyond leading order:

\[
 \phi_r=
 \frac\pi{4\sqrt2\,r^2}
 -\frac{3\pi}{16r^3}
 +o(r^{-3}),
\]

\[
 e_r-g_{2r}
 =\frac{\pi^2}{32r^4}
 -\frac{3\pi^2}{32\sqrt2\,r^5}
 +o(r^{-5}).
\]

The first soft pair obeys the avoided-crossing law

\[
 r^4\bigl(g_{2r}(z/r^2)-e_r\bigr)
 \to z^2-\frac\pi{2\sqrt2}z.
\]

## Headline finite-order result

Let `m(N,s)` be the minimum spectral radius over all edge signings of
`C_N(1,s)`.  The triangular-strip theorem now proves the sharpened bound

\[
 \boxed{
 m(3s,s)^2\ge 8+\frac1{70}>8
 \qquad(s\ge7\text{ odd}).}
\]

Thus every odd resonance pair `(N,s)=(3s,s)`, `s>=7`, is an all-signing
obstruction to the sub-`sqrt(8)` regime.

The proof splits into:

- `s=7`: exhaustive exact switching-class certificate with stronger margin
  `18/131`;
- `s=9`: exact prefix-pruned exhaustive certificate covering all
  `2*8^9=268,435,456` Hamilton-gauge representatives at margin `1/70`;
- odd `s>=11`: exact nine-column signed-triangle finite-state lemma plus a
  structural seam contradiction using `tr(B^3)`.

The nine-column local rule says that either a window already has
`rho^2>=8+1/70`, or its six middle triangle transitions are exactly
`B_(j+1)=-B_j`.  The clean `1/70` constant is close to the actual local
finite-state boundary; `1/69` is numerically too strong for that local lemma.

## Current result map

### Periodic/Bloch theory

- `ALL_S_UNIFIED_THEOREM.md` — all jumps, common quadratic envelope and
  parity-free sharp `pi^2` limit.
- `ODD_JUMP_SHARP_GAP.md` — exact odd dispersion, unique optimizer and sharp
  `pi^2` limit.
- `QUADRATIC_GAP_THEOREM.md` — even `Theta(s^-2)` gap.
- `ENDPOINT_PI2_ASYMPTOTIC.md` — even phase-zero `pi^2` endpoint.
- `PHASE_SLIP_COUNTEREXAMPLE.md` — exact `s=10` Sturm certificate.
- `EVEN_GLOBAL_PI2_THEOREM.md` — global even sharp leading constant.
- `GLOBAL_PI2_LOCALIZATION_LEMMA.md` — explicit leading localization.
- `EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md` — phase scale and `pi^2/32`
  gain.
- `SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md` — `mu=O(r^-4)` bootstrap.
- `EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md` — first finite-`r` correction.

### Finite-order arithmetic theory

- `C21_S7_GLOBAL_OBSTRUCTION.md` — all-signing exact obstruction at `(21,7)`.
- `verify_c21_s7_all_signings.py` — 49,940 `Q` necklaces / 199,760 gauge
  representatives, exact integer witnesses.
- `verify_c27_s9_all_signings.py` — quantitative prefix-pruned exact
  certificate at margin `1/70` for all `C_27(1,9)` signings.
- `verify_triangle_strip_local_rule.py` — exact nine-column eight-state rule,
  margin `1/70`.
- `N3S_GLOBAL_OBSTRUCTION.md` — infinite all-signing theorem
  `m(3s,s)^2>=8+1/70` for every odd `s>=7`.
- `N3S_ONE_DEFECT_LOCAL_OBSTRUCTION.md` — simpler 18-vertex local proof for
  the one-defect subfamily, margin `1/24`.
- `ODD_ORDER_RESONANCE_MAP.md` / `explore_odd_order_resonances.py` —
  seam-safe exploratory map for other short chord-cycle lengths.

### Literature / formalization / reproducibility

- `LITERATURE_UPDATE_20260906.md` — updated boundary versus Suvagiya's
  `C_n(1,2)` paper and general block-Jacobi theory.
- `RESULTS_INDEX.md` — current theorem/evidence status.
- `../../../formal/QuadraticGap/` — separate Lean track including
  `PhaseSlipConstants.lean`; not kernel-compiled in the current environment.
- Finite exact scripts use floating eigensolvers only as witness proposers;
  certification/pruning decisions are integer quadratic inequalities.

## Research picture

The project now separates two effects that initially looked like period
compatibility:

- **periodic Bloch edge:** every jump admits a sub-`sqrt(8)` explicit periodic
  signing with sharp gap `pi^2/s^2`;
- **finite arithmetic topology:** the whole odd line `N=3s`, `s>=7`, admits no
  sub-`sqrt(8)` signing at all and in fact stays uniformly above by `1/70` in
  squared radius.

## Next targets

1. Determine exact values or large-`s` asymptotics of `m(3s,s)`.
2. Classify other chord-cycle lengths `L=N/gcd(N,s)`, especially `L=5,7,9`.
3. Seek a hand matrix proof replacing the nine-column finite-state
   certificate.
4. Remove the `4s | N` restriction for the even explicit construction where
   possible.
5. Continue Lean formalization of the signed-triangle obstruction and the
   phase-slip bootstrap.
6. Extend the magnetic/flux-phase literature audit before priority claims.

No general closed formula for `m(N,s)` and no final priority claim are made.
