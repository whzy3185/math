# Target A Finite Evans Root Exclusion

For G6/G10 and `alpha=+1,-1`, the finite Evans determinant is exactly the
Task 50 closure polynomial `f_k(y,alpha)`.  After each of the four shifts
`y=beta+u`, exact coefficient signs exclude a real zero for `u>=0` through
`k=32`; in particular, `beta=7.98` gives an exact finite-prefix exclusion on
`[7.98,16]`.

This result is stronger than a sampled winding count for the same finite
prefix, so complex Rouché and argument-principle computations were not
escalated.  It is not a uniform theorem: the alternating order-nine recurrence
does not preserve the observed coefficient cone by an established induction.

| Method | Status |
|---|---|
| Real interval coefficient exclusion, `k<=32` | EXACT_FINITE |
| Dominant/remainder finite Evans split | PROMISING |
| Rouché inequality for all `k` | WEAK |
| Interval argument principle | WEAK |
| Complex winding rectangle | NOT_APPLICABLE_WITH_REASON: exact real sign is stronger for the tested prefix |
| Uniform `k>=K` exclusion | OPEN |

No all-`k` spectral cap is claimed.
