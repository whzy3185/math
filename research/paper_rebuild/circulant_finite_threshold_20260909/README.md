# Finite spectral extrema in signed step circulants

Working branch: `paper/circulant-finite-threshold-20260909`.

This directory rebuilds, from proof sources and fresh exact checks, the finite-global extremal problem
\[
m(N,s)=\min_\sigma \rho(A_\sigma),\qquad 2\le s<N/2,
\]
for the signed adjacency matrices of `C_N(1,s)`.

## Scope boundary

This paper is self-contained and concerns finite graphs, minimization over **all** signings, exact equality, threshold classification, and switching/flux rigidity. It does not use any continuous Bloch optimum, large-`s` asymptotic theorem, phase-slip expansion, or theorem from the separate periodic-family project.

## Audited results as of 2026-09-09

1. **Flat/off-flat dichotomy (Proved).** Every signing has `rho(A)>=2`; equality occurs exactly on `N=2s+2`. Off this line every signing has `rho(A)>=sqrt(5)`. For `N=2s+2`, `s!=3`, equality consists of two labelled switching classes, interchanged by translation. At `(N,s)=(8,3)=K_{4,4}` there are six labelled switching classes, forming one orbit under switching plus graph automorphisms.

2. **New all-even-order finite theorem (Proved).** If `N` is even, then
\[
m(N,s)^2\le 6+2\cos(2\pi/N)<8.
\]
This is a finite Fourier theorem obtained from Hamilton holonomy `-1` and the alternating chord word. It strictly strengthens the even-`s` positive half of the old `N=3s` threshold statement.

3. **Short odd `N=3s` cases (Proved by exact certificates).** Explicit seam-safe signings for `(9,3)` and `(15,5)` have `8I-A^2>0`; the full leading-principal-minor lists were recomputed exactly with SymPy and agree with the historical certificates.

4. **Odd obstruction on `N=3s` (Proved, computer-assisted local lemma).** The historical constant `1/70` has been improved during this rebuild to
\[
 m(3s,s)^2\ge 8+\frac{2}{139}\qquad(s\ge7\text{ odd}).
\]
The nine-column prefix certificate was rerun at margin `2/139` with survivor counts `8,56,152,440,488,1016,656,1064,128`; every survivor obeys the forced middle alternation. The `s=9` cyclic base case was rerun at the same stronger margin: all `17,024` final candidates have exact integer Rayleigh witnesses. The `s=7` all-signing certificate was also rerun completely: `49,940` admissible Q-necklaces and `199,760` gauge representatives, with weakest exact witness ratio `18/131`.

Consequently the audited threshold classification is
\[
 m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\},
\]
with the stronger odd obstruction above.

## Historical proof sources actually inspected

- `research/generalization/circulant_1s/extension_20260905/FLAT_MINIMUM_AND_CHIRAL_CRITERION.md` on `research/quadratic-gap-upgrade`, blob `b6e3e5a...`.
- `.../quadratic_gap_20260906/N3S_THRESHOLD_CLASSIFICATION.md`, blob `aa5fb7d...`.
- `.../N3S_GLOBAL_OBSTRUCTION.md`, blob `9a1c958...`.
- `.../C21_S7_GLOBAL_OBSTRUCTION.md`, blob `610957d...`.
- `.../C27_S9_GLOBAL_OBSTRUCTION.md`, blob `000fd55...`.
- `.../verify_triangle_strip_local_rule.py`, blob `bc2bc59...`.
- `.../verify_n3s_short_threshold.py`, blob `289d7b8...`.
- `.../verify_c21_s7_all_signings.py`, blob `ab02fd1...`.
- `.../verify_c27_s9_all_signings.py`, blob `ca60fd7...`.

The summary file `FINAL_THEOREM_PACKAGE_20260907.md` was not used as a proof source.

## Current research frontier

The new all-even-order theorem reduces a general resonance search `N=ks` to odd `k,s`. Small exhaustive data already show that `k=5,s=3` is sub-threshold, while the `k=3`, odd-`s>=7` line is obstructed. Thus the triangle chord-cycle length `3`, not merely odd parity, is the first structural suspect. General odd-order `k>=5` remains open here and is recorded as Observed/Under investigation rather than promoted to a theorem.
