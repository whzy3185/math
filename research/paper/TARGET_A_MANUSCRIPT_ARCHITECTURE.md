# Target A Manuscript Architecture

Status: **TARGET_A_MANUSCRIPT_ARCHITECTURE_FROZEN**

Gate: **TARGET_A_MANUSCRIPT_READY**

This file fixes structure, theorem placement, and evidence placement only. It is
not manuscript prose. Reviewer Zero round 2 reviewed commit
`b9e00bd34222d40e9ac954d3d5c4817644650be0` and reported
`CRITICAL=0`, `MAJOR=0`; moderate and minor submission repairs remain recorded
below.

## 1. Introduction

- State the original signed-circulant optimization conjecture and its exact
  admissible domain.
- Announce Theorems A-F without all-period, all-signings, or all-finite-order
  overclaims.
- State the recorded novelty assessment with its indexing and access limits.
- Separate mathematical contributions from computer-assisted verification.

## 2. Signed Circulants and Flux Coordinates

- Define `G_n=C_n(1,2)`, `sigma`, `A_sigma`, Hamilton-gauge `tau`, flux `Q`,
  holonomy `alpha`, primitive period, and the allowed equivalences.
- Fix `R(Q)` as squared infinite-volume spectral radius.
- Prove translation, reflection, global-negation, and cell-repetition
  equivalences, including odd-cell `z -> -z` and zone folding.
- Claims: C5, C11, C24.

## 3. The Smallest Counterexample

- Theorem A: the smallest admissible even counterexample order is `n=32`.
- Present the quotient-completeness lemma, exact finite exclusions for
  `8<=n<=30`, and the exact order-32 witness.
- Label the finite exclusion as computer-assisted; move checkpoint chains,
  hashes, and runner details to Appendix A and the supplement.
- Claims: C1-C3.

## 4. Periodic Construction and Floquet Reduction

- Theorem B: an explicit counterexample exists for every `n=8L`, `L>=4`.
- Derive the finite Bloch condition `z^L=alpha` separately from the
  infinite-volume condition `|z|=1`.
- Give the exact period-8 determinant route and threshold comparison.
- Claims: C4-C6.

## 5. Exact Period-8 Spectral Edge

- Theorem C: `R(Q_*)=eta=4+sqrt(10+2sqrt(5))`, with unique band edge `z=1`.
- Include the exact polynomial, root isolation, band monotonicity, and equality
  analysis.
- Keep the finite-size `alpha=+1` equality and `alpha=-1` strict inequality
  distinct from the infinite spectral statement.
- Claims: C6-C7.

## 6. The Eight-Barrier and Structural Optimum

- Theorem D: the period-8 target is the unique minimizer and satisfies the
  complete below/equal/above trichotomy.
- Develop the local `A^2` identity, period-8 moments, one-way moment barrier,
  defect combinatorics, and two-defect separation hierarchy.
- Treat anti-period-4 symmetry and the normalized chiral involution as
  supplementary structural propositions, not sufficient optimality criteria.
- Move the 18-orbit table to Appendix B.
- Claims: C8-C16.

## 7. General-Period Closed-Walk Obstructions

- Theorem E: state the exact `M_1`, `M_2`, and `M_3` formulas for every
  `p>=1` and derive the defect-density and clustering necessary conditions.
- State only `F_k(Q)>0 => R(Q)>8`; no converse or finite-negative-excess
  inference is permitted.
- Explain short-cell Laurent collision multiplicities explicitly.
- Claims: C11, C13, C17-C21.

## 8. The Low-Period Spectral Frontier

- Theorem F: the target is uniquely optimal among primitive `tau` periods at
  most 16 under the stated equivalences.
- Prove orbit-space completeness and primitive normalization, then use the
  `2611/8/5/2` structural partition.
- State that the `p=16` equality is a doubled period-8 cell via zone folding.
- Put the five residual exact certificates in Appendix B; do not list 2,624
  witnesses in the body.
- Claims: C22-C25.

## 9. Computer-Assisted Verification

- State the executable-proof trust model and distinguish deterministic full
  regeneration from checkpoint-integrity replay.
- Record the `n=24,26,28,30` state and chunk counts, mismatch zero, independent
  checkers, negative tests, and proof classifications.
- Disclose that `2,147,483,648` represented `n=30` switching classes are covered
  through quotient completeness, not independent pytest cases.
- Preserve the accepted trust risks for smaller-order replay and largest-order
  generator independence.

## 10. Discussion and Open Problems

- Summarize the period-8 mechanism, arbitrary-period necessary obstructions,
  and bounded low-period theorem without extrapolating them.
- Re-state the novelty audit's dated, source-limited safe assessment.
- List O1-O5 without beginning new exploration in this task.

## Open Problems

- **O1.** Is the target globally optimal among all periodic phases?
- **O2.** Is it globally optimal among all signings?
- **O3.** What happens for finite `n` not divisible by 8?
- **O4.** Can the moment hierarchy classify arbitrary periods?
- **O5.** Is there a general flux-phase variational principle?

## Appendices

- **Appendix A: Burnside and orbit completeness.** Quotient lemmas, exact
  state counts, primitive-period normalization, and finite-search completeness.
- **Appendix B: Exact residual certificates.** Period-8 orbit table, the five
  low-period endpoint certificates, and radical-comparison details.
- **Appendix C: Computational verification details.** Checkers, tamper tests,
  execution model, and the boundary between regeneration and integrity replay.

## Supplement

- Source code and machine-readable JSON artifacts.
- Independent checkers and negative regression tests.
- SHA-256 manifests, checkpoint summaries, and repository-relative commands.
- Fresh-regeneration records and environment/bootstrap material when the
  submission-grade reproducibility repairs are completed.

## Submission Preflight

The drafting gate is passed, but external submission still requires disposition
of the nonblocking Reviewer Zero round-2 findings:

- `RZ2-001`: portable environment lock/bootstrap.
- `RZ2-002`: state the `r>4` branch premise in the human radical comparison.
- `RZ2-003`: bind the low-period checker to the full canonical orbit set.
- `RZ2-005`: map the final drafting/submission snapshot to the reviewed package.
- `RZ2-004`, `RZ2-006`: retain explicitly as accepted computation-trust risks
  unless stronger independent evidence is added.

Task 44 may draft the manuscript from this architecture. It must not silently
resolve, omit, or strengthen any of these boundaries.
