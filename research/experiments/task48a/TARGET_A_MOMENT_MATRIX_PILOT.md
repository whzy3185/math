# Target A Moment-Matrix Pilot

For all 184 Task 47 `F16` survivors, exact moments `M0,...,M20` were computed.
The generalized support test used `H_m=(M_{i+j})` and
`S_m=(M_{i+j+1})`.  A rational polynomial witness with quotient above
`1561/200 > eta` proves that `eta H_m-S_m` is not positive semidefinite and
hence that the spectral support is not contained in `[0,eta]`.

The cumulative exact exclusions are:

| Depth | Excluded |
|---:|---:|
| 2 | 1 |
| 3 | 145 |
| 4 | 180 |
| 5 | 183 |

The sole survivor at depth 5 is the repeated period-8 target.  A direct target
sanity check is not excluded, confirming the PSD implication direction.  The
pilot therefore has `MOMENT_MATRIX_VALUE = HIGH` and supplies a potentially
cleaner certificate hierarchy for the p<=24 result.  General arbitrary-period
consequences remain unproved.
