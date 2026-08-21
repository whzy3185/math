# Target A Controlled High-Period Exploration

Date: 2026-08-21

Status: **EXPERIMENTAL; NO THEOREM EXTENSION**

## Protocol

For each displayed period `p=17,...,24`, the experiment enumerates every legal
quadrilateral-flux word modulo the dihedral action. The orbit-size sum is
checked against `2^(p-1)`. A separate permutation-cycle Burnside calculation
checks every orbit count. A direct full-integer-space visited-orbit partition
then compares the complete canonical record set and every orbit size for
`p=17,...,23`; the committed C full-space record audit supplies the same check
at `p=24`. For every orbit the defect statistics and the first two moment
excesses are computed exactly:

```text
F1 = 16d-12p,
F2 = 40d+96a+48b-42p.
```

A positive excess proves `R(Q)>8`; a nonpositive excess proves nothing. The
complete residual set is therefore not called spectrally classified.

Within each residual set, 256 candidates are selected by a deterministic rank
using moment excess, defect density near `p/4`, local clustering, gap
regularity, and canonical code. A 128-point Bloch grid ranks them, and the best
16 are reevaluated on a 2,048-point grid. These grid values are **NUMERICAL
ONLY**. They neither upper-bound the continuous Floquet supremum nor exclude
unselected residuals.

Machine-readable data, all refined candidate words, and the primitive-period
distributions are in `target_a_high_period_exploration.json`.

## Exact Coverage and Moment Counts

| `p` | dihedral orbits | `F1>0` | additional `F2>0` | low-moment residual |
|---:|---:|---:|---:|---:|
| 17 | 2,056 | 93 | 1,270 | 693 |
| 18 | 3,914 | 114 | 2,524 | 1,276 |
| 19 | 7,155 | 130 | 5,054 | 1,971 |
| 20 | 13,648 | 156 | 9,772 | 3,720 |
| 21 | 25,482 | 176 | 18,480 | 6,826 |
| 22 | 48,734 | 207 | 36,748 | 11,779 |
| 23 | 92,205 | 232 | 69,830 | 22,143 |
| 24 | 176,906 | 269 | 131,290 | 45,347 |

All four columns in this table are exact integer counts. For every period the
orbit multiplicities sum to the complete `2^(p-1)` legal words, the independent
Burnside count agrees, and the independent record route consumes precisely the
same canonical set with the same orbit sizes.

## Numerical Candidate Summary

| `p` | best sampled `Q` | primitive `tau` period | defect gaps | sampled squared radius |
|---:|:---|---:|:---|---:|
| 17 | `10010010001001000` | 17 | `3,3,3,4,4` | 8.052098454 |
| 18 | `100010001000100000` | 18 | `4,4,4,6` | 7.924384897 |
| 19 | `1001000100010001000` | 19 | `3,4,4,4,4` | 8.024712014 |
| 20 | `10001000001000100000` | 10 | `4,4,6,6` | 7.916381552 |
| 21 | `100010010001000100000` | 21 | `3,4,4,4,6` | 8.013292994 |
| 22 | `1001000100100010001000` | 22 | `3,3,4,4,4,4` | 7.995036411 |
| 23 | `10001001000100010000000` | 23 | `3,4,4,4,8` | 8.037993851 |
| 24 | `100010001000100010001000` | 8 | `4,4,4,4,4,4` | 7.804226065 |

The last value equals `eta` by the already proved period-eight theorem and
zone folding; it is not merely numerical. The next sampled `p=24` candidate,
`100010010001001000100000`, has numerical grid value `7.974984681` and
primitive `tau` period 24.

## Answers to the Search Questions

1. At `p=24`, the period-eight repetition is the best candidate found and is
   recognized as primitive period 8.
2. No selected candidate below `eta` was found. This is evidence, not a proof
   over the low-moment residual sets.
3. The nearest sampled non-target candidate occurs at `p=20`, with value
   `7.916381552`; the nearest sampled `p=24` non-target value is `7.974984681`.
4. `F1` and `F2` exclude the exact counts in the first table.
5. The residual counts in the first table escape both low-order filters; only
   a declared deterministic subset receives numerical Floquet evaluation.
6. The best sampled words favor separated defects with gaps mainly three to
   six. No second perfectly period-eight antipodal geometry appears.
7. The complete primitive `tau`-period distributions are stored in the JSON;
   the best odd-period rows are primitive, while repetitions are detected at
   even periods.
8. The `p=24` target row is correctly identified as a threefold displayed-cell
   representation of the primitive period-eight phase.

## Boundary

This experiment does not alter the proved primitive-period bound `p<=16`, does
not establish a `p<=24` classification, and does not support an all-period
optimality claim. Any candidate suggested by the floating search would require
a separate exact certificate and complete orbit closure before entering a
theorem.
