# Complete Mathematical Closure: Baseline Freeze

## Frozen baseline

| Field | Value |
|---|---|
| proof-closure branch | `proof/complete-mathematical-closure` |
| baseline commit | `ebc6de4fb67eeae7af961eb415a4dc1fdcc4c2c7` |
| baseline description | Task 59 submission package plus the later related-work audit; the mathematical evidence is inherited unchanged from Task 50--57 |
| submission tag | `target-a-task59-identified-v1` |
| tag commit | `80e3d94` |
| primary proof branch | `agent/target-a-discovery-snapshot` at `0ebfc7b` |
| latest task-59 prose commit in ancestry | `833face` |
| deliberately excluded adjacent project | Task 60, the general `C_N(1,s)` exploration |

The baseline is `ebc6de4`, not `main`: it contains the most recent audited
related-work branch while retaining the complete Target A proof/certificate
ancestry.  Task 60 is intentionally not a proof input for the fixed
`C_n(1,2)` classification.

## Frozen manuscript inputs (read only)

| Item | Path |
|---|---|
| identified main source | `research/paper/manuscript_tex_task59/` |
| anonymous main source | `research/paper/manuscript_tex_task59/main_anonymous.tex` |
| supplement source | `research/paper/manuscript_tex_task59_supplement/` |
| bibliography | `research/paper/manuscript_tex_task59/references.bib` |
| submission manifest | `research/proofs/task59/submission_manifest.json` |
| package verifier | `research/scripts/verify_target_a_submission.py` |

No file below either manuscript tree is modified by this proof-closure task.

## Proof and certificate inputs

| Module | Principal source | Exact checker |
|---|---|---|
| twisted spectrum and small orders through 32 | `research/proofs/TARGET_A_SMALLEST_COUNTEREXAMPLE.md` | `verify_target_a_minimality_certificate.py`, `verify_target_a_n32_certificate.py` |
| period-eight bulk | `research/proofs/TARGET_A_PERIOD8_SHARP_CONSTANT.md` | `verify_target_a_period8_sharp_constant.py` |
| G6 transfer, root, and localization | `research/proofs/task50/TARGET_A_EXACT_INTERFACE_THEOREM.md` | `verify_target_a_task50_interface.py` |
| G6 global edge and IMS | `research/proofs/task53/TARGET_A_G6_GLOBAL_EDGE_THEOREM.md`, `TARGET_A_DISCRETE_IMS_LEMMA.md` | `verify_target_a_task53_a2.py`, `verify_target_a_task53_a3.py` |
| finite bridge and analytic threshold | `research/proofs/task54/TARGET_A_TASK54_CONTINUATION_SYNTHESIS.md` | `verify_target_a_task54_threshold.py` |
| recovered equality orders | `research/proofs/task55/TARGET_A_SMALL_ORDER_EXACT_THEOREM.md` | `verify_target_a_task55_small_order_exact.py` |
| order-40 witness | `research/proofs/task55/TARGET_A_ORDERS_34_46_EXACT_CLASSIFICATION.md` | `verify_target_a_task55_orders_34_46.py` |
| abnormal single-gap hierarchy | `research/proofs/task56/TARGET_A_SINGLE_GAP_NIGHT_REPORT.md` | `verify_target_a_task56_single_gap.py` |
| uniform single-gap separation | `research/proofs/task57/TARGET_A_UNIFORM_SINGLE_GAP_SEPARATION.md` | `verify_target_a_task57_uniform_single_gap.py` |

## Baseline rule

Historical statements marked `OPEN`, `EXACT_FINITE_READ_ONLY`,
`HIGH_PRECISION_DISCOVERY`, or `FALSIFIED_AS_STATED` are preserved as
provenance but are not allowed as dependencies of the complete all-even
classification.  The evidence boundary is formalized in
`PROOF_OBLIGATION_MATRIX.md`.
