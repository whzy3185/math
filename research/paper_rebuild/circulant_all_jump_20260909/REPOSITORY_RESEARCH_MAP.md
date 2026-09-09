# Repository-wide research map

Date: 2026-09-09

This map is included because the repository's active mathematics is distributed across multiple branches.  Branch names are not project boundaries.

## A. Signed circulants / fixed-support spectral minimization

**Earliest article-level project in the repository.**

Historical start:

- root research initialization: `fb4375f9588b558f162d7e3f6542c35b0056eea3`, 2026-08-15;
- first C029 counterexample freeze: `21d5b848ec6222e9cca8b263dcc9cd397b86b236`, same day.

Current strongest endpoint:

- branch `research/quadratic-gap-upgrade`;
- theorem package `research/generalization/circulant_1s/quadratic_gap_20260906/FINAL_THEOREM_PACKAGE_20260907.md`.

Maturity:

- **Proved:** infinite counterexample family to the original twisted-optimizer conjecture;
- **Proved:** exact period-8 dispersion and first-period rigidity results;
- **Proved:** explicit sub-threshold periodic phase for every jump `s>=2`;
- **Proved:** sharp leading gap `s^2(8-Rhat_s)->pi^2`;
- **Proved:** exact flat-minimum line `m(N,s)=2 iff N=2s+2`;
- **Proved:** complete `sqrt(8)` threshold classification on `N=3s`;
- **Verified:** finite exact certificates used in the resonance proof have recorded reruns;
- **Formalized in Lean only in part:** the old period-8 positive-holonomy comparison has a finite formal kernel; the new all-jump theorems are not yet formalized.

Paper status:

- old period-8 English paper exists and was corrected;
- the old paper is mathematically superseded as the main submission object by the all-jump theorem package;
- this branch now contains the reconstructed all-jump article architecture and manuscript skeleton.

Priority:

**Highest priority for repository consolidation because it is the oldest project and currently has a coherent upgraded theorem chain.**

## B. Four-speed Lonely Runner spectrum below 1/4

Primary record on `main`:

`research/paper/LONELY_RUNNER_JCTA_WRITING_AND_REVISION_HISTORY.md`.

Separate formalization line:

`lean-lonely-runner-ci`.

Headline results recorded by the project:

- exact description of `L_4 cap (0,1/4)`;
- additive inverse theorem: `ML(V)<1/4` forces three distinct speeds with `a+b=c`;
- classification into two infinite configuration families plus the isolated configuration `{1,3,4,14}`;
- a long JCTA-oriented editorial and proof-audit history through version v1.17;
- an active Lean/CI formalization branch.

Maturity:

**Article-level and apparently very mature, but it is a distinct project.**  The repository `main` currently stores the writing/revision history rather than the full clean manuscript in the same obvious path, so submission packaging should be checked independently before any venue decision is treated as final.

Priority:

Keep separate from signed circulants.  Its stated JCTA target should be judged on its own novelty and proof package, not used to set the venue for the graph-spectral paper.

## C. Forbidden configuration `F(0,17,1,0)`

Branch:

`research/q1-discrete-full-push-20260906`.

Current proved pieces:

- transitivity framework specialized to `p=17`, `c=21/2`;
- all clique components have nonnegative deletion cost, with one zero-cost six-row block;
- non-clique Case 1 has strictly positive cost;
- Case 2 with shortest-path parameter `r=6` is closed by an explicit integer certificate.

Current obstruction:

- `r=4` and `r=5` remain unresolved.

Maturity:

**Promising partial theorem, not yet a complete paper theorem.**

Priority:

Do not spend editorial effort on a final paper until the two remaining local cases close or a different component bound replaces them.

## D. Remark-3 product-type PDE

Main latest branch:

`research/remark3-leading-form-v3-20260908`.

Headline results recorded by the project:

- automatic finite-growth closure for the polynomial-exponential product PDE;
- finite algebraic classification for general polynomial factor;
- explicit irreducible full-direction solvability criterion;
- exact number of solutions modulo additive constants in that irreducible regime;
- degree and leading-form obstructions;
- generic nonexistence statement;
- 93 v2 and 18 v3 exact symbolic checks;
- compiled and visually audited manuscript builds.

Maturity:

**Complete analytic research manuscript, but novelty audit remains the main risk.**  The project itself records known overlap with a two-dimensional Chen-Han result and incomplete full-text comparison with a 2026 Xu-Ding paper.

Priority:

Keep independent.  Before selecting a strong journal, complete the theorem-by-theorem novelty comparison with the closest 2026 paper.

## E. Historical candidate/poset and other branches

These are useful research archives but are not currently competitive with the four article-level lines above for immediate consolidation.  Do not merge them into any current manuscript merely to increase result count.

## Overall priority ranking for repository work

1. **Signed circulants:** finish the new integrated all-jump English paper and direct literature audit.
2. **Lonely Runner:** separately verify that the clean v1.17 manuscript and formalization package are synchronized; then perform its venue-specific novelty audit.
3. **Remark-3 PDE:** finish direct novelty comparison before claiming journal level.
4. **F(0,17,1,0):** return to theorem proving (`r=4,5`) rather than manuscript polishing.

The ranking is about readiness for the next useful action, not a claim that one mathematical result is intrinsically stronger than another.
