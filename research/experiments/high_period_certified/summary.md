# High-Period Candidate Certification Summary

Status: **EXACT SELECTED-CANDIDATE COMPARISON COMPLETE**

The source pool consists exactly of the 184 orbit representatives surviving
all moment tests `F_1,...,F_16` at periods 17 through 24. For each period, at
most 20 candidates are selected by the deterministic tuple:

1. lowest 128-point Bloch-grid estimate;
2. lower defect density;
3. larger maximum defect separation;
4. larger primitive `tau` period;
5. smaller canonical integer code.

This selects all survivors at `p=17,...,21` and the first 20 at each of
`p=22,23,24`, for 125 candidates total. The 2,048-point values are numerical
diagnostics only.

## Exact Classifications

| classification | count |
|:---|---:|
| `CERTIFIED_R_GT_ETA` | 124 |
| `CERTIFIED_R_EQ_ETA` | 1 |
| `CERTIFIED_R_LT_ETA` | 0 |
| `UNRESOLVED` | 0 |
| `NUMERICAL_ONLY` | 0 |

The unique equality is the threefold displayed period-24 repetition of the
period-eight target. Every other selected candidate has an exact integer
Rayleigh quotient at `z=+1` or `z=-1` strictly above `1561/200`, while
`1561/200>eta` is checked exactly. Hence all 124 strict classifications prove
`R(Q)>eta` without treating a grid maximum as the continuous supremum.

The lowest non-target numerical estimate is the primitive-period-10 row shown
at `p=20`, approximately `7.9163815517`; it is rigorously above `eta`. The
previously highlighted primitive `p=24` candidate with gaps
`3,3,4,4,4,6` is also certified strictly above `eta`.

This experiment closes every selected dangerous candidate, not all 184
moment survivors and not all high-period phases. It therefore strengthens the
period-eight structural signal but does not extend the proved `p<=16`
classification.
