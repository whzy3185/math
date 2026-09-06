# All-`s` sharp quadratic-gap and finite-obstruction workstream

Branch: `research/quadratic-gap-upgrade`
Date: 2026-09-06

This workstream now has two complementary main results:

1. a sharp periodic/Bloch theory for explicit signings of `C_N(1,s)` for
   every jump `s>=2`;
2. a genuine finite-order all-signing obstruction family on `N=3s` for odd
   `s>=7`.

The frozen period-eight manuscript and `formal/TargetA` remain unchanged.

## Headline Bloch result

For the parity-dependent explicit periodic family, write `Rhat_s` for the
continuous squared Bloch radius and `ghat_s=8-Rhat_s`.  Then

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

and

\[
 e_r-g_{2r}
 =\frac{\pi^2}{32r^4}
 -\frac{3\pi^2}{32\sqrt2\,r^5}
 +o(r^{-5}).
\]

The lower soft branch is governed by the avoided-crossing law

\[
 r^4\bigl(g_{2r}(z/r^2)-e_r\bigr)
 \to z^2-\frac\pi{2\sqrt2}z.
\]

## Headline finite-order result

Let `m(N,s)` be the minimum spectral radius over all edge signings of
`C_N(1,s)`.  The new triangular-strip theorem proves

\[
 \boxed{
 m(3s,s)^2\ge 8+\frac1{1038}>8
 \qquad(s\ge7\text{ odd}).}
\]

Thus every odd resonance pair

\[
 (N,s)=(3s,s),\qquad s=7,9,11,\ldots
\]

is an all-signing obstruction to the sub-`sqrt(8)` regime.

This is qualitatively stronger than a failed construction: **no signing at
all** works on this infinite arithmetic line.

The proof splits into:

- `s=7`: exhaustive exact switching-class certificate with stronger margin
  `18/131`;
- `s=9`: exact prefix-pruned exhaustive certificate covering all
  `2*8^9=268,435,456` Hamilton-gauge representatives;
- odd `s>=11`: a nine-column signed-triangle finite-state lemma plus a
  structural seam contradiction using `tr(B^3) != tr((-B)^3)`.

The finite-state lemma has a uniform exact forbidden-word margin `1/1038`.

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
- `verify_c27_s9_all_signings.py` — pruned exhaustive exact certificate for
  all `C_27(1,9)` signings.
- `verify_triangle_strip_local_rule.py` — exact nine-column eight-state rule.
- `N3S_GLOBAL_OBSTRUCTION.md` — infinite all-signing theorem
  `m(3s,s)^2>=8+1/1038` for every odd `s>=7`.
- `N3S_ONE_DEFECT_LOCAL_OBSTRUCTION.md` — simpler 18-vertex local proof for
  the one-defect subfamily, with margin `1/24`.
- `ODD_ORDER_RESONANCE_MAP.md` and `explore_odd_order_resonances.py` —
  seam-safe exploratory map for other short chord-cycle lengths.

### Formalization / reproducibility

- `../../../formal/QuadraticGap/` — separate Lean track including
  `PhaseSlipConstants.lean`; it is not yet kernel-compiled in the current
  environment.
- Exact finite scripts use floating eigensolvers only as **witness proposers**;
  pruning/certification decisions are checked by integer quadratic forms.

## Research picture

The project now separates two phenomena that initially looked similar:

- **periodic Bloch edge:** every jump admits a sub-`sqrt(8)` explicit periodic
  signing with sharp gap `pi^2/s^2`;
- **finite arithmetic topology:** some finite circulants, including the whole
  odd line `N=3s`, admit no sub-`sqrt(8)` signing at all.

So finite-order compatibility is not just a Fourier-grid or period-divisibility
issue.  Short chord cycles can create a robust obstruction that survives
optimization over every signing.

## Next targets

1. Classify other chord-cycle lengths
   `L=N/gcd(N,s)`, especially `L=5,7,9`.
2. Determine the exact values or asymptotics of `m(3s,s)` rather than only the
   uniform lower bound.
3. Seek a hand matrix proof replacing the exact nine-column finite-state
   certificate.
4. Remove the `4s | N` restriction for the even explicit construction where
   possible.
5. Continue the Lean track for the signed-triangle obstruction and the
   phase-slip bootstrap.
6. Extend the publication-priority audit before making novelty claims.

No general closed formula for `m(N,s)` and no final priority claim are made.
