# Target A Stale Rank-Claim Audit

## Canonical correction

The current theorem is

```text
rank P_(H_6,{c6})=2,
exactly 2r near-c6 squared levels for r=1,2,3 and D>=1040,
codimension-2r complement,
2r x 2r problem-specific Feshbach operator.
```

The historical exact-`r`, codimension-`r`, rank-one G6, and `r x r`
statements are false as stated.

For checker-facing plain-text compatibility, the four category labels are:

```text
CURRENT CORRECT
HISTORICAL SUPERSEDED
MUST UPDATE BEFORE MANUSCRIPT
SAFE INTERNAL ARCHIVE
```

The tables below use underscore-separated machine identifiers for the same
four categories.

## Audit totals

The case-insensitive fixed-string scan of the tracked tree at `e6a01d8`
found 111 relevant line occurrences in 46 files:

| Classification | Lines | Meaning |
|---|---:|---|
| `CURRENT_CORRECT` | 51 | corrected theorem, explicit rejection, or non-spectral use of `r` |
| `HISTORICAL_SUPERSEDED` | 52 | retained old proof/review with canonical supersession |
| `MUST_UPDATE_BEFORE_MANUSCRIPT` | 2 | source wording must not be imported unchanged |
| `SAFE_INTERNAL_ARCHIVE` | 6 | retraction certificate/checker or fail-closed tamper token |

## Complete file-and-line classification

| File and relevant lines | Classification | Reason / action |
|---|---|---|
| `research/proofs/task52/TARGET_A_FIXED_R_ELEMENTARY_SLIP_THEOREM.md:50` | `CURRENT_CORRECT` | Says only "at least `r`" and explicitly denies exact count; weak but true. |
| `research/proofs/task52/TARGET_A_MULTI_SLIP_INTERACTION_ASYMPTOTICS.md:18` | `MUST_UPDATE_BEFORE_MANUSCRIPT` | Displays the heuristic `H_eff=c6 I_r+T+R` without the later rank-doubling correction. Do not import; replace by a `2r` formulation if used. |
| `research/proofs/task53/TARGET_A_FESHBACH_EFFECTIVE_MATRIX.md:3,11,26` | `HISTORICAL_SUPERSEDED` | File now carries an explicit supersession banner and the corrected `2r` statement. |
| `research/proofs/task53/TARGET_A_FIXED_R_PATCH_CLASSIFICATION.md:3` | `CURRENT_CORRECT` | "Exactly `r` gaps" counts combinatorial G6 defects, not spectral multiplicity. |
| `research/proofs/task53/TARGET_A_TASK53_REVIEWS.md:8,17` | `HISTORICAL_SUPERSEDED` | Pre-correction review language; not a current theorem dependency. |
| `research/proofs/task53/TARGET_A_TASK53_SYNTHESIS.md:185,197,319,328` | `CURRENT_CORRECT` | Explicitly labels exact-`r` falsified and exact-`2r` proved. |
| `research/proofs/task54/TARGET_A_BULK_AND_INTERFACE_GREEN_DECAY.md:17` | `CURRENT_CORRECT` | Corrects the pole from rank one to rank two. |
| `research/proofs/task54/TARGET_A_COMMON_RESIDUE_LIMIT_SCOPE.md:23` | `MUST_UPDATE_BEFORE_MANUSCRIPT` | The open-liminf conclusion is valid, but the phrase "exact-`r` theory" names a false theory. Replace by the corrected separated exact-`2r` theorem if reused. |
| `research/proofs/task54/TARGET_A_COMPLEMENT_GAP_THEOREM.md:5` | `HISTORICAL_SUPERSEDED` | Banner withdraws the codimension-`r` argument. |
| `research/proofs/task54/TARGET_A_EFFECTIVE_COUPLING_FORMULAS.md:3` | `HISTORICAL_SUPERSEDED` | Banner identifies the one-mode-per-interface application as superseded. |
| `research/proofs/task54/TARGET_A_EXACT_R_PHASE_SLIP_EXCITATION_THEOREM.md:1,4,16` | `HISTORICAL_SUPERSEDED` | Original false theorem retained under an explicit retraction notice. |
| `research/proofs/task54/TARGET_A_EXACT_R_RIESZ_THEOREM.md:1,4,20` | `HISTORICAL_SUPERSEDED` | Original count retained only as retracted history. |
| `research/proofs/task54/TARGET_A_EXPONENTIAL_EVENTUAL_THRESHOLD.md:4` | `HISTORICAL_SUPERSEDED` | States that its old dependency is invalid; current threshold is elsewhere. |
| `research/proofs/task54/TARGET_A_EXPONENTIAL_FIXED_R_GLOBAL_CAP.md:4,9` | `HISTORICAL_SUPERSEDED` | Old proof is marked superseded by the exact-`2r` cap. |
| `research/proofs/task54/TARGET_A_EXPONENTIAL_RESIDUE_BOUNDS.md:3` | `HISTORICAL_SUPERSEDED` | Explicit supersession notice. |
| `research/proofs/task54/TARGET_A_FESHBACH_EFFECTIVE_HAMILTONIAN.md:6,41` | `HISTORICAL_SUPERSEDED` | Abstract Schur identity survives, but the problem-specific `r`-dimensional application is withdrawn. |
| `research/proofs/task54/TARGET_A_GEOMETRIC_RESOLVENT_GLUE.md:13,16` | `HISTORICAL_SUPERSEDED` | Rank-`r` route is expressly withdrawn. |
| `research/proofs/task54/TARGET_A_TASK54_CONTINUATION_BASELINE.md:8` | `HISTORICAL_SUPERSEDED` | Historical task scope, not a current claim. |
| `research/proofs/task54/TARGET_A_TASK54_CONTINUATION_DEPENDENCY_GRAPH.md:10,12,16,18` | `HISTORICAL_SUPERSEDED` | Historical graph records false/open statuses; canonical DAG excludes these nodes. |
| `research/proofs/task54/TARGET_A_TASK54_CONTINUATION_MASTER_LEDGER.md:5,17,18,19,20,21,48` | `HISTORICAL_SUPERSEDED` | Retains withdrawn rows and a supersession notice for provenance. |
| `research/proofs/task54/TARGET_A_TASK54_CONTINUATION_SYNTHESIS.md:35,40,43,46,62,213,214,216,242,254,256,262,297` | `HISTORICAL_SUPERSEDED` | Records the failure and then-pending repair at its historical checkpoint. |
| `research/proofs/task54/certificates/exact_r_complement_gap.json:27,28` | `SAFE_INTERNAL_ARCHIVE` | Machine-readable retraction artifact; both fields say `NOT_PROVED`. |
| `research/proofs/task54/lanes/exponential_cap/HANDOFF.md:15,24,40,61,69` | `HISTORICAL_SUPERSEDED` | Historical handoff explicitly points to the invalid dependency and later supersession. |
| `research/proofs/task55/BASELINE.md:72,73` | `CURRENT_CORRECT` | Canonical rank-doubling correction. |
| `research/proofs/task55/TARGET_A_COMMON_LIMINF_TASK55.md:18,73` | `CURRENT_CORRECT` | Explicitly disclaims dependence on exact-`r` and records exact-`2r` as proved but unused. |
| `research/proofs/task55/TARGET_A_G6_RANK_DOUBLING_CORRECTION.md:13,14,15,125` | `CURRENT_CORRECT` | Authoritative correction to rank two and `2r x 2r`. |
| `research/proofs/task55/TARGET_A_PHASE_SLIP_INTERACTION_THEOREM.md:8,126` | `CURRENT_CORRECT` | Rejects the former one-mode model as a dependency. |
| `research/proofs/task55/TARGET_A_REFERENCE_RELATIVE_COST.md:76` | `CURRENT_CORRECT` | Explicit nondependence statement. |
| `research/proofs/task55/TARGET_A_SIMPLICITY_CONDITIONS.md:106` | `CURRENT_CORRECT` | Rejects old claims and does not infer finite-ring simplicity. |
| `research/proofs/task55/TARGET_A_TASK55_DEPENDENCY_GRAPH.md:41,110,111,112` | `CURRENT_CORRECT` | Marks all three stale nodes falsified and blocks their arrows. |
| `research/proofs/task55/TARGET_A_TASK55_MASTER_LEDGER.md:43,44,45` | `CURRENT_CORRECT` | Final falsified-claim ledger. |
| `research/proofs/task55/TARGET_A_TASK55_SYNTHESIS.md:31,165` | `CURRENT_CORRECT` | Canonical synthesis rejects inherited dimensions. |
| `research/proofs/task55/lanes/exact_2r/VERIFIER_HANDOFF.md:84,150` | `CURRENT_CORRECT` | Fail-closed forbidden-field policy. |
| `research/proofs/task56/BASELINE.md:34,35` | `CURRENT_CORRECT` | Uses the corrected `2r` baseline. |
| `research/proofs/task56/TARGET_A_LIMINF_NIGHT_REPORT.md:297` | `CURRENT_CORRECT` | Explicit exclusion from dependencies. |
| `research/proofs/task56/TARGET_A_SINGLE_GAP_NIGHT_REPORT.md:76` | `CURRENT_CORRECT` | States rank two, not rank one. |
| `research/proofs/task56/TARGET_A_TASK56_NIGHT_SYNTHESIS.md:5,7` | `CURRENT_CORRECT` | Records exact-`2r` replacement and no stale dependency. |
| `research/review/task53/REVIEW_F_JCTB_EDITOR.md:11` | `HISTORICAL_SUPERSEDED` | Pre-correction editorial recommendation; no theorem status. |
| `research/review/task54/MASTER_CONTINUATION_REVIEW.md:11,20,46` | `CURRENT_CORRECT` | Hostile review records and verifies the retraction. |
| `research/review/task55/MASTER_REVIEW.md:24,48,160,161,199` | `CURRENT_CORRECT` | Independent review identifies exact-`r` as false and rank two as correct. |
| `research/scripts/target_a_task54_exact_r.py:1,81,85` | `SAFE_INTERNAL_ARCHIVE` | Retraction producer; emits only `NOT_PROVED` records. |
| `research/scripts/test_target_a_task55_exact_2r.py:76` | `CURRENT_CORRECT` | Tamper input ensures an `I_r` regression is rejected. |
| `research/scripts/verify_target_a_task54_exact_r.py:1` | `SAFE_INTERNAL_ARCHIVE` | Verifies the retraction, not the false theorem. |
| `research/scripts/verify_target_a_task55_exact_2r.py:646,647,651` | `CURRENT_CORRECT` | Forbidden-token scanner rejects `I_r`, `r x r`, and `r times r`. |
| `research/scripts/verify_target_a_task56_one_g6_degeneracy.py:136,137` | `CURRENT_CORRECT` | Contract rejects withdrawn exact-`r` phrases. |
| `research/scripts/verify_target_a_task56_single_gap.py:81` | `CURRENT_CORRECT` | Requires the theorem to say rank two, not rank one. |

## Formal manuscript result

The scan found zero relevant stale-rank occurrences in

```text
research/paper/manuscript_tex_pub/
research/paper/manuscript_tex_pub_zh/
```

The manuscripts remain frozen. No historical file was rewritten during this
audit.

## Final disposition

There is no dangerous positive stale-rank theorem in the canonical-current
proof layer. The two `MUST_UPDATE_BEFORE_MANUSCRIPT` lines are source-import
hazards, not accepted claims; both are barred from direct reuse. Historical
and retraction artifacts remain intentionally preserved.
