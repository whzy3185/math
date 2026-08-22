# Target A Hankel Independent Audit

## Method

The audit rechecks all 184 survivors of the scalar moment filter.  It searches
exact principal minors of

\[
 1561 H_m-200 S_m
\]

through depth five.  It does not reuse the floating generalized eigenvector or
the Task 48A rational witness.  A negative determinant is an exact integer
certificate.

## Result

| Maximum depth | Cumulative exact exclusions |
|---:|---:|
| 2 | 1 |
| 3 | 145 |
| 4 | 180 |
| 5 | 183 |

All 184 inputs were independently checked.  The sole survivor is the
period-24 display of the repeated period-eight target.  Both the primitive
period-eight target sanity check and its displayed repetition survive, so the
second checker does not spuriously exclude the equality state.

Twenty representative records cover every period 17 through 24, low-depth
exclusions, depth-five hard cases, and the target equality.  The complete 184
record audit is stored, so the representative subset is not the acceptance
boundary.

## Verdict

`HANKEL_AUDIT_PASS`

Reproducer: `research/scripts/target_a_task49_hankel_independent.py`.
Machine-readable result:
`research/reproducibility/task49/hankel_independent/summary.json`.
