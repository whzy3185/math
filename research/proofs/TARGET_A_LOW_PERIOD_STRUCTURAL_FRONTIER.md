# Target A Low-Period Structural Frontier

Date: 2026-08-16

Status: **LOW_PERIOD_STRUCTURAL_FRONTIER_PROVED**

## Theorem Package

For the complete 2626-orbit legal-`Q` phase space with cell length at most 16,
the Task 42B exact classification compresses as follows:

```text
2611 representations: one uniform closed-walk moment hierarchy proves R>8>eta,
   8 representations: one all-negative cancellation lemma proves R=8>eta,
   5 representations: exact endpoint Rayleigh certificates prove R>eta,
   2 representations: one Target A infinite phase has R=eta.
```

Thus every one of the 2624 competitor representations remains exactly
excluded, but only five individual endpoint certificates remain essential.
The other 832 endpoint certificates used in Task 42B are replaced by the
uniform moment hierarchy.

This is a structural compression of the bounded `p<=16` theorem. It is not an
all-period result.

## 1. Uniform Moment Hierarchy

For every periodic phase define

```text
M_k(Q)=CT_z tr(H_Q(z)^(2k)),
F_k(Q)=M_(k+1)(Q)-8M_k(Q).
```

The Task 42A moment-barrier lemma gives the single valid implication

```text
F_k(Q)>0 ==> R(Q)>8.
```

The structural classifier computes exact integer closed-walk moments. It
first checks `F_1,...,F_24` for all 2626 orbit representatives. Only the
residual set is extended to `F_25,...,F_64`. The first positive-index
distribution is:

| first positive excess | orbit count |
|---:|---:|
| `F_1` | 64 |
| `F_2` | 1723 |
| `F_3` | 493 |
| `F_4` | 178 |
| `F_5` | 56 |
| `F_6` | 11 |
| `F_7` | 19 |
| `F_8` | 15 |
| `F_9` | 8 |
| `F_10` | 5 |
| `F_11` | 3 |
| `F_12` | 4 |
| `F_13` | 4 |
| `F_14` | 6 |
| `F_15` | 4 |
| `F_16` | 2 |
| `F_17` | 2 |
| `F_19` | 1 |
| `F_21` | 1 |
| `F_23` | 1 |
| `F_25` | 2 |
| `F_27` | 6 |
| `F_29` | 1 |
| `F_48` | 1 |
| `F_64` | 1 |
| **total** | **2611** |

This hierarchy gives one coherent explanation for the overwhelming majority
of the frontier: their signed closed-walk mass eventually crosses the
eight-barrier.

The detection scale is itself structural information. Classes only slightly
above eight can require long walks: one class first crosses at `F_48`, and
one at `F_64`. Stopping at the first three moments would therefore hide much
of the low-density geometry.

No nonpositive excess is used as an upper bound. The 15 classes with no
positive `F_k` through 64 are handled independently below.

## 2. Cancellation Baseline

The eight all-negative rows are

```text
P02-0001, P04-0001, P06-0001, P08-0001,
P10-0001, P12-0001, P14-0001, P16-0001.
```

They are repeated cells for one infinite phase with primitive `tau` period
two. For `Q=(-)^p`, the lift is `tau_i=(-1)^i`. The exact operator identity
from Task 40C is period-independent:

```text
A^2=4I+S^2+S^-2+S^4+S^-4.
```

Its Fourier symbol is

```text
4+2cos(2 theta)+2cos(4 theta)<=8,
```

with equality at `theta=0`. Hence every row represents the same exact phase
with

```text
R=8>eta.
```

This replaces eight individual endpoint certificates by one cancellation
lemma.

## 3. Target Representations

The two target rows are

```text
P08-0006: Q=00010001,
P16-0512: Q=0001000100010001.
```

Both have primitive `tau` period eight and represent the same infinite phase.
Task 40A proves

```text
R=eta=4+sqrt(10+2sqrt(5)).
```

Their lack of positive excess through `F_64` is not used to prove this upper
bound; the exact Floquet theorem remains the dependency.

## 4. Five Exceptional Competitors

After removing the moment-detected, baseline, and target rows, exactly five
competitor representations remain:

| orbit | canonical `Q` | observed `R^2` | exact conclusion |
|---|---|---:|---|
| `P10-0006` | `0000010001` | 7.9163815517 | `R>eta` |
| `P12-0006` | `000000010001` | 7.9355448971 | `R>eta` |
| `P14-0006` | `00000000010001` | 7.9634702195 | `R>eta` |
| `P14-0154` | `00010010001001` | 8.0000000000 | `R>eta` |
| `P16-0006` | `0000000000010001` | 7.9955101031 | `R>eta` |

The first, second, third, and fifth rows have two positive-flux defects at
cyclic separation four, with the other gap increasing from six to twelve.
They are the finite low-period continuation of the target's separation-four
local geometry, but they are not equal-spacing target repetitions and their
primitive `tau` periods are `10,12,14,16`.

The fifth structural shape, `P14-0154`, has four defects with cyclic gaps
`3,4,3,4`. Its preview lands at eight to displayed precision.

For all five rows, the theorem uses only the stored exact endpoint integer
Rayleigh certificate from Task 42B. Each proves a rational quotient strictly
greater than `eta`. The displayed numerical values are discovery previews.
This package does not claim an exact upper bound below eight for the four
two-defect rows, nor does it claim that `P14-0154` has exact radius eight.

## 5. Compression Accounting

The exact competitor accounting is

```text
2611 moment-detected representations
   8 all-negative baseline representations
   5 exceptional endpoint-certified representations
----
2624 competitor representations.
```

Together with the two target cell representations, this covers all 2626
Task 42B orbits with no overlap and no omission.

Task 42B used 1787 moment and 837 endpoint certificates. Task 42C uses 2611
moment detections, one baseline lemma for eight repeated rows, and five
endpoint certificates. Thus

```text
837-5=832
```

individual endpoint certificates are no longer needed in the structural
proof route.

## 6. Independent Verification

The checker does not import the structural classifier. It independently:

- rebuilds signed closed walks for every Task 42B orbit;
- recomputes the adaptive first positive excess through `F_64`;
- checks every stored first index and positive integer value;
- reconstructs the 15-row residual partition;
- verifies the baseline and target repetition data;
- independently multiplies the five endpoint matrices and integer vectors;
- redoes each exact rational comparison with `eta`.

Run:

```bash
python research/scripts/target_a_low_period_structural_frontier.py
python research/scripts/verify_target_a_low_period_structural_frontier.py
python -m pytest -q research/scripts/test_target_a_low_period_structural_frontier.py
```

Expected checker status:

```text
TARGET_A_LOW_PERIOD_STRUCTURAL_FRONTIER_PASS
```

## 7. Scope

Proved:

```text
structural compression of the complete primitive-period<=16 frontier,
uniform exact moment exclusion of 2611 orbit representations,
complete exact treatment of the 15 residual representations.
```

Not claimed:

```text
negative excess implies an upper bound,
exact R<8 for the four separation-four competitors,
exact R=8 for P14-0154,
any conclusion for primitive period >=17,
all-period global optimality.
```
