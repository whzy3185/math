# C029 formal progress: finite seed and conditional boundary structure

This is a source-only progress deposit dated 2026-10-05. It preserves the existing manuscript and its **237-declaration formalization claim**. It is not a completed formal proof of the full C029/R2 theorem.

## What is established

### Finite first-cap seed: cumulative 607-name coverage

The exact rational recurrence is identified with the recorded first-cap seed (cap **7.92**) and transported to the real recurrence. Its terminal core has the strict **1/50 identity-matrix margin**. The finite identification closes **51 equality premises**: one initial-state identity, 25 supplied-inverse identities, 24 open transitions (indices 0 through 23), and one terminal match at state 24. There is no open transition 24 to 25.

The 607-name ledger is cumulative evidence from successful disjoint 592-name coverage plus successful full-artifact compilation and inline axiom reports for the final modules (3, 5 and 7 new theorems). The frozen sources and imported artifacts were reconciled by hash. The numerical chain was **not freshly rebuilt when making this deposit**.

This does not establish all finite inequalities. In particular, positive definiteness of every eliminated pivot, the remaining contraction hypotheses, raw-graph/block identification, response decay, infinite tails, and the concrete unequal-cell assembly remain separate. The second constant c1 = 790537/100000 and the energy/J48 certificate are also outside this seed result.

### Generic and typed local open-Schur step

`C029OpenSchur.lean` proves five generic results, culminating in an explicit 14-by-14 block-matrix positivity criterion equivalent to positivity of its 10-by-10 retained update, under a positive-pivot hypothesis.

The typed bridge proves a two-sided equivalence with the actual `TargetA.R2RecurrenceState` over the reals, commutation with the actual update at `r2D` and `r2Coupling`, the exact retained packing, and the corresponding local positivity criterion. Its 30-name audit includes dependencies: the genuinely new bridge consists of one equivalence definition and five theorems. The original rational-recurrence source is unchanged. The structural build profile replaces only the original terminal module's umbrella Mathlib import with selective imports; every declaration and proof body is unchanged.

The bridge does not prove all pivots positive, perform graph elimination induction, identify the original graph, or close terminal and infinite-tail arguments.

### Conditional additive boundary matrix: 37 declarations

Four structural modules derive the degree-two incidence estimate, the induced-L2-norm cross estimate, the assembled quadratic lower bound, and genuine `Matrix.PosDef` after orthonormal L2 flattening. They preserve one-cell loops and two-cell parallel contributions. Symmetry is derived from the stated diagonal self-adjointness assumptions, and strict positivity follows from the explicit margin `delta + 2 M < gamma`.

The concrete C029 endpoints, their equality to the manuscript Schur complement, and their numerical/operator-norm caps have not been identified in these files. The result is a conditional generic structural theorem.

## Counts and verification boundaries

The stage counts must not be added as theorem totals. `evidence/declaration_sets.json` gives every exact name and every pairwise intersection. In particular, the generic five are already in the typed 30-name audit, and eight of those 30 names also occur in the finite 607-name ledger. The structural 37 include definitions and abbreviations as well as theorems; the 607-name ledger is a different stage's audit set.

All reported transitive axiom sets are subsets of `propext`, `Classical.choice`, and `Quot.sound`. Both the typed bridge and the four boundary modules passed independent, fresh source compilation using only newly built project objects and pinned third-party caches. This deposit additionally includes a portable runner and its own fresh eight-module source replay receipt. See `evidence/publication_replay.json` for the measured replay and `REPRODUCE.md` for the exact route and limits.

## Operational failures retained as failures

- The fresh monolithic numerical-chain/aggregate-audit route did not finish successfully within its resource limits. It is not evidence of a fresh aggregate 607-name pass
- The subsequent fresh 15-name terminal aggregate audit was terminated at 118.653 seconds before import profiling or axiom output completed; no declaration coverage is inferred from that run
- The supported 607-name statement therefore remains the cumulative, byte-matched ledger described above
- Early typed-bridge attempts failed on an unavailable notation import and on two unclosed definitional projection goals. The corrected frozen source then passed fresh compilation and independent replay
- Earlier structural proof attempts and one supplementary regression-harness attempt failed before the final frozen sources passed; these failures are not silently counted as verification

- The first publication replay compiled the generic source successfully but its new validation harness compared short and qualified declaration names incorrectly. The harness was corrected and replayed from a new output directory; the Lean source was unchanged

These are compilation/resource or proof-development outcomes, not counterexamples to the scoped results. The deposit does not contain compiled executables, cached project objects, full build archives, or a modified manuscript.

## Layout

- `finite/formal/`: exact frozen source closure and named audit programs; the 607-name audit file is also a reference inventory, with no claim that its monolithic execution passed
- `finite/data/`: minimal exact certificate input
- `structural/src/`: exact generic, typed, and boundary sources; separate from the original finite compilation profile
- `dependencies/`: pinned official Lean/Mathlib and transitive package configuration
- `reproduce/`: portable replay and validation scripts
- `evidence/`: concise name, axiom, source-hash, and verification ledgers
- `SHA256SUMS`: integrity hashes of every other public file
