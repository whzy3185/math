# Repository-wide reconstruction of the signed-circulant article

Date: 2026-09-09

Branch: `paper/circulant-all-jump-rebuild-20260909`

This reconstruction follows one mathematical lineage across the repository rather than treating any branch as the project boundary:

`C029 signed-circulant optimizer` -> `period-8 counterexample` -> `exact period-8 Floquet/chiral theory` -> `C_N(1,s) all-jump extension` -> `sharp quadratic gap / phase-slip / N=3s threshold classification`.

The Lonely Runner, F(0,17,1,0), and Remark-3 PDE projects are independent manuscripts and are intentionally not merged here.

## 1. Historical spine recovered from the repository

### H0. Repository initialization

Root commit `fb4375f9588b558f162d7e3f6542c35b0056eea3` (2026-08-15) created the research pipeline and candidate registry.  C029 was selected as Target A: the conjecture that the twisted signing globally minimizes the adjacency spectral radius of `C_n(1,2)` for every even `n>=8`.

### H1. First substantive discovery

Commit `21d5b848ec6222e9cca8b263dcc9cd397b86b236`, only a few hours after initialization, froze the first counterexample state.  It records the period-8 flux word

`tau=(+,+,-,+,-,-,+,-)`

and proves an infinite counterexample family for every `8|n`, `n>=32`, together with an exact `n=32` certificate and exhaustive verification through `n=22`.

This is the true beginning of the article-level mathematics.

### H2. Period-8 theory

The later period-8 branches replaced the original discovery report by a mathematical mechanism:

- Hamilton/switching coordinates and finite Bloch decomposition;
- a half-cell chiral criterion;
- exact `8 -> 4 -> 2` reduction and four dispersion branches;
- exact finite holonomy radii;
- smallest primitive sub-eight period equal to 8;
- uniqueness, up to the natural symmetry, of the period-8 sub-eight orbit;
- a finite Lean kernel for a principal comparison theorem.

The corrected English manuscript lives in
`research/paper_strengthening/manuscript_period8_jgt/` on the period-8 paper branches.

The period-8 manuscript is no longer the strongest available paper because it predates the all-jump extension.

### H3. All-jump extension

The branch `research/circulant-1s-extension` promotes the mechanism from `s=2` to `C_N(1,s)`.  The strongest reusable results are:

- parity-dependent periodic constructions for all jumps;
- a general monomial half-cell anticommutation criterion;
- for every even `s`, a primitive period-`4s` antipodal-defect word with squared Bloch edge below 8;
- quantitative gap bounds;
- exact flat-minimum classification `m(N,s)=2 iff N=2s+2` and universal lower bound `m(N,s)>=sqrt(5)` off that line.

The repository-wide status index is
`research/repository_guide/RESULTS_INDEX.md`.

### H4. Current endpoint

The branch `research/quadratic-gap-upgrade` contains the current headline theorem package in
`research/generalization/circulant_1s/quadratic_gap_20260906/FINAL_THEOREM_PACKAGE_20260907.md`.

The main proved results are:

1. for every `s>=2`, an explicit periodic signing with continuous squared Bloch radius `Rhat_s<8`;
2. with `ghat_s=8-Rhat_s`,
   `s^2 ghat_s -> pi^2`;
3. for even jumps, the optimizing Bloch phase has a boundary-layer phase slip and the first nontrivial improvement over phase zero occurs at the next asymptotic order;
4. `m(N,s)=2 iff N=2s+2`, otherwise `m(N,s)>=sqrt(5)`;
5. on the resonance line `N=3s`,
   `m(3s,s)<sqrt(8)` iff `s` is even or `s in {3,5}`;
6. for odd `s>=7`, the stronger obstruction `m(3s,s)^2 >= 8+1/70` holds.

This is substantially stronger than the old period-8 manuscript and should determine the new paper architecture.

## 2. New paper thesis

The paper should no longer be sold as an exact analysis of one exceptional period.  Its thesis should be:

> Spectral minimization over signings of step circulants exhibits an explicit parity-dependent periodic mechanism.  The mechanism first appears as a counterexample to twisted-signing optimality at `s=2`, extends to every jump, has a sharp parity-free `pi^2/s^2` Bloch-gap law, and produces a genuine finite threshold transition on the resonance line `N=3s`.

The period-8 result is then the exactly solvable base case that explains the construction and supplies rigidity, not the whole paper.

## 3. Proposed title

Preferred:

**Periodic flux phases in signed circulants: sharp spectral gaps and a finite threshold transition**

Alternative, more graph-theoretic:

**Spectral minimization in signed step circulants: counterexamples, sharp periodic gaps, and resonance thresholds**

Do not use a title implying that `m(N,s)` is known exactly for every `(N,s)`.

## 4. Main theorem hierarchy

### Theorem A — counterexample and first mechanism

State the original `C_n(1,2)` twisted-optimizer conjecture, then give the period-8 infinite counterexample family.  Use the later exact period-8 dispersion to present the cleanest proof.  This theorem motivates the problem but should not occupy most of the paper.

### Theorem B — all-jump periodic construction

For every `s>=2`, construct an explicit periodic signing with squared Bloch edge strictly below 8:

- odd `s`: period-two alternating flux;
- even `s`: primitive period-`4s` antipodal defect.

This is the conceptual generalization of the counterexample.

### Theorem C — sharp asymptotic gap

For `ghat_s=8-Rhat_s`, prove

`1/(6s(s+2)) <= ghat_s <= 4 sin^2(pi/(s+2))`

and

`s^2 ghat_s -> pi^2`.

For even `s=2r`, include the phase-slip theorem only to the rigorously audited order required to explain why the global maximum is not always at phase zero.  Higher unaudited refinements stay out of the headline theorem.

### Theorem D — exact flat minimum

For every admissible finite `C_N(1,s)`,

`m(N,s)=2 iff N=2s+2`,

and otherwise `m(N,s)>=sqrt(5)`.

This gives a global finite-graph result independent of the periodic witness asymptotics.

### Theorem E — resonance-line threshold phase transition

For `N=3s`, prove

`m(3s,s)<sqrt(8)` iff `s` is even or `s in {3,5}`,

with the uniform obstruction

`m(3s,s)^2 >= 8+1/70`

for every odd `s>=7`.

This should be the second headline theorem after the all-jump gap theorem because it is an exact finite classification, not merely a construction.

### Theorem F — exactly solvable base case `s=2`

Retain only the period-8 results that explain the general mechanism or provide a sharp rigidity statement:

- half-cell flux/chiral equivalence;
- exact four dispersion branches;
- first primitive sub-eight period is 8;
- uniqueness of the first sub-eight orbit.

Move long certificate tables and historical all-even computations to an appendix/supplement unless they are logically needed.

## 5. Six-section manuscript architecture

### 1. Introduction and main results

1. Fixed-support signing minimization and the Bilu-Linial/Ramanujan context.
2. Suvagiya's 2026 `C_n(1,2)` twisted-optimizer conjecture.
3. Counterexample mechanism, not a search narrative.
4. General question for `C_N(1,s)`.
5. Theorem B/C: all-jump periodic phases and sharp `pi^2/s^2` gap.
6. Theorem D/E: exact flat minimum and resonance threshold transition.
7. One paragraph explaining the role of exact finite computation.

### 2. Switching coordinates and periodic fibers

- signed adjacency matrices and switching;
- Hamilton gauge / local flux coordinates;
- holonomy versus local flux;
- finite Bloch decomposition;
- parity-dependent alternating reference phase;
- general half-cell anticommutation criterion.

This section should absorb only the reusable infrastructure from the old period-8 paper.

### 3. Periodic phases for arbitrary jump

- odd-jump alternating family and exact scalar dispersion;
- even-jump antipodal-defect construction;
- Chebyshev/transfer reduction;
- proof that the continuous squared edge is below 8 for every `s`.

End with the parity comparison: different constructions, same leading spectral scale.

### 4. Sharp gap asymptotics and phase slip

- uniform lower/upper gap bounds;
- localization near the maximizing phase;
- proof of `s^2 ghat_s -> pi^2`;
- even-jump boundary-layer phase slip;
- the rigorously audited second-order correction.

Do not include exploratory critical-ratio numerics as theorem evidence.

### 5. Finite circulants: flat minima and the `N=3s` transition

- exact `m=2` classification;
- universal `sqrt(5)` lower bound off the flat line;
- even `s` resonance construction;
- exact short positive cases `s=3,5`;
- odd `s>=7` obstruction;
- complete resonance phase diagram.

The exact finite scripts should appear only after the mathematical reduction proves the finite domain complete.

### 6. The exactly solvable `s=2` model and concluding problems

Compress the old period-8 paper into a final structural case study:

- exact period-8 bands;
- first occurrence and rigidity;
- how the two-defect word anticipates the general even-jump construction.

Close with the genuinely open problem:

`determine m(N,s) exactly for all admissible (N,s)`.

A second precise open problem may ask for the minimal sub-eight primitive period / equality classes for general `s`, but do not create a long conjecture list.

## 6. Material to delete from the old paper narrative

- any sentence claiming the positive-holonomy period-8 value is the global finite minimum;
- the obsolete conclusion contradicted by the negative-holonomy sector;
- project-history language (`we searched`, `the script found`, `task XX`);
- long JGT-style self-audits from the mathematical body;
- general all-even computational classifications not used by the new main theorem;
- speculative statements `R_s=rho(H_s(1))^2` or higher phase-slip asymptotics without the same audit level as the main results;
- claims that all main mathematics is Lean-formalized.

## 7. Computation policy for the new paper

Keep the evidence hierarchy explicit internally, but present it in normal mathematical style.

- General theorems must have complete analytic proofs in the paper.
- Exact computation is acceptable for the finite base cases in the `N=3s` obstruction after completeness reduction.
- Floating eigenvectors may propose certificates but cannot certify inequalities.
- The paper should state that final finite acceptance uses exact integer/rational arithmetic.
- Reproducibility code belongs in a repository supplement, not as a standalone manuscript section unless required by the journal.

## 8. Independent projects not to merge

### Lonely Runner

The repository contains a separate JCTA-oriented four-speed Lonely Runner project with an exact spectrum and additive inverse theorem, plus an independent Lean/CI branch.  Its mathematical language, background, and proof architecture are unrelated to signed circulants.

### Forbidden configuration `F(0,17,1,0)`

The branch `research/q1-discrete-full-push-20260906` has a promising partial extension with clique/Case-1 closure and an explicit `r=6` Case-2 certificate, but `r=4,5` remain unresolved.  It is not ready to be mixed into a finished paper.

### Remark-3 PDE

The 2026-09-08 branches contain a complete analytic PDE manuscript with exact symbolic checks, but it is a complex-analysis/PDE paper and requires its own novelty audit and venue.

## 9. Immediate pre-submission checklist for this paper

1. Re-derive and audit the all-jump theorem from a clean notation layer independent of research task files.
2. Recheck the `pi^2` asymptotic and even phase-slip proof with no dependence on exploratory scripts.
3. Re-run the exact finite certificates used in the `N=3s` theorem and archive checksums.
4. Perform a direct literature audit for signed circulants, periodic signed/magnetic graph spectra, and recent fixed-support signing minimization.
5. Rewrite the old period-8 introduction so that Suvagiya's conjecture is the entry point, not the entire problem.
6. Build one English master LaTeX manuscript from this six-section architecture.
7. Keep the original period-8 manuscript as a historical frozen artifact rather than editing it in place.
