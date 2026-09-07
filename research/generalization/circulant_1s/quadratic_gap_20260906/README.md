# Final all-`s` quadratic-gap and finite-resonance workstream

Branch: `research/quadratic-gap-upgrade`
Current status date: 2026-09-07

The current endpoint is `FINAL_THEOREM_PACKAGE_20260907.md`.

## Headline results

### 1. Sharp periodic/Bloch theory for every jump

For an explicit parity-dependent periodic family, with squared Bloch radius
`Rhat_s` and gap `ghat_s=8-Rhat_s`,

\[
 \boxed{Rhat_s<8\quad(s\ge2),}
\]

and

\[
 \boxed{s^2\,ghat_s\to\pi^2}
\]

through all integer jumps.

Odd `s` uses the period-two alternating-flux family; even `s` uses the
primitive period-`4s` antipodal defect family.

For even `s=2r`, the first nonzero phase-slip scale is also proved:

\[
 \boxed{r^2\phi_r\to\frac\pi{4\sqrt2},}
 \qquad
 \boxed{r^4(e_r-g_{2r})\to\frac{\pi^2}{32}.}
\]

The exact `s=10` Sturm certificate shows that the phase slip is real; the
second-order theorem shows it changes the gap only at order `r^-4`.

### 2. Exact finite flat minimum

For every admissible finite `C_N(1,s)`,

\[
 \boxed{m(N,s)=2\iff N=2s+2,}
\]

and otherwise every signing has radius at least `sqrt(5)`.

### 3. Complete `sqrt(8)` threshold classification on `N=3s`

For every integer `s>=2`,

\[
 \boxed{
 m(3s,s)<\sqrt8
 \iff s\text{ is even, or }s\in\{3,5\}.}
\]

More precisely:

- `s=2`: `m(6,2)=2`;
- even `s>=4`: `sqrt(5)<=m(3s,s)<sqrt(8)` by an explicit antiperiodic
  alternating signing;
- `s=3,5`: exact Sylvester certificates give `sqrt(5)<=m(3s,s)<sqrt(8)`;
- odd `s>=7`: every signing satisfies
  \[
  \boxed{m(3s,s)^2\ge8+1/70.}
  \]

Thus odd `s=7` is the genuine threshold where the resonance line becomes an
all-signing super-`sqrt(8)` obstruction.

## Main files

- `FINAL_THEOREM_PACKAGE_20260907.md` — current theorem package and scope.
- `N3S_THRESHOLD_CLASSIFICATION.md` — exact iff classification on `N=3s`.
- `verify_n3s_short_threshold.py` — exact Sylvester certificates for `s=3,5`.
- `ALL_S_UNIFIED_THEOREM.md` — all-jump sharp periodic theorem.
- `ODD_JUMP_SHARP_GAP.md` — odd exact optimizer and sharp `pi^2` gap.
- `QUADRATIC_GAP_THEOREM.md` — even `Theta(s^-2)` envelope.
- `EVEN_GLOBAL_PI2_THEOREM.md` — even global leading constant.
- `EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md` — proved phase scale and
  `pi^2/32` gain.
- `SECOND_ORDER_LOCAL_IMPLICIT_LEMMA.md` — `mu=O(r^-4)` bootstrap and local
  inverse estimate.
- `PHASE_SLIP_COUNTEREXAMPLE.md` — exact `s=10` Sturm counterexample to
  phase-zero maximality.
- `N3S_GLOBAL_OBSTRUCTION.md` — uniform all-signing obstruction for odd
  `s>=7` on `N=3s`.
- `C21_S7_GLOBAL_OBSTRUCTION.md` and `C27_S9_GLOBAL_OBSTRUCTION.md` — exact
  short base cases.
- `verify_triangle_strip_local_rule.py` — exact nine-column finite-state
  lemma with margin `1/70`.
- `RESULTS_INDEX.md` — evidence/status ledger.

## Exact reproducibility rerun on 2026-09-07

The current analysis environment independently reproduced:

- the nine-column survivor counts
  `8,56,152,440,488,1016,656,1064,128` and forced alternation for all 128
  final survivors;
- all `17,024` final cyclic `C_27(1,9)` checks at exact margin `1/70`;
- all `199,760` Hamilton-gauge representatives of `C_21(1,7)`, with weakest
  generated exact Rayleigh excess `18/131`;
- all positive leading principal minors for the explicit `C_9(1,3)` and
  `C_15(1,5)` sub-`sqrt(8)` witnesses.

Floating eigensolvers in the finite obstruction scripts are witness proposers
only; theorem decisions are exact integer/rational inequalities.

## Evidence boundary

- `EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md` derives the next `r^-3/r^-5`
  constants, but this refinement is intentionally kept outside the final
  headline theorem until its uniform `o(r^-1)` remainder bookkeeping receives
  a separate hostile audit.
- New `formal/QuadraticGap/` Lean sources remain uncompiled in the current
  environment; they are not kernel-checked claims.
- The final theorem package does not give an exact formula for `m(N,s)` for
  every admissible pair.
- Publication priority remains subject to the current literature boundary,
  especially Suvagiya's 2026 `C_n(1,2)` papers and general magnetic/block-
  Jacobi frameworks.

## Remaining research beyond the final package

1. exact values/asymptotics of `m(3s,s)` within the classified regimes;
2. other chord-cycle lengths `N/gcd(N,s)` such as `5,7,9`;
3. a hand matrix inequality replacing the nine-column finite-state lemma;
4. even-jump finite-order compatibility beyond `4s | N`;
5. full Lean compilation/formalization;
6. broader magnetic/flux-phase priority audit.
