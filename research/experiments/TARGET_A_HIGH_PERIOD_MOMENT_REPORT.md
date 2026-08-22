# Target A High-Period Moment Report

Date: 2026-08-22

Status: **EXACT EXPERIMENT COMPLETE; NO THEOREM EXTENSION**

## Coverage and Method

Every legal `Q` orbit for `p=17,...,24` is processed in canonical integer
order. The exact integer hierarchy

```text
F_k(Q)=M_(k+1)(Q)-8M_k(Q)
```

is evaluated adaptively through `k=16`: evaluation stops as soon as `F_k>0`,
which rigorously implies `R(Q)>8`. A state surviving through `F_16` is not
declared sub-eight. Orbit multiplicities independently sum to `2^(p-1)` at
every period.

## Survival Curves

| `p` | after `F1` | after `F2` | after `F4` | after `F8` | after `F16` |
|---:|---:|---:|---:|---:|---:|
| 17 | 1,963 | 693 | 77 | 17 | 7 |
| 18 | 3,800 | 1,276 | 142 | 34 | 10 |
| 19 | 7,025 | 1,971 | 193 | 41 | 10 |
| 20 | 13,492 | 3,720 | 399 | 67 | 19 |
| 21 | 25,306 | 6,826 | 590 | 93 | 19 |
| 22 | 48,527 | 11,779 | 948 | 143 | 31 |
| 23 | 91,973 | 22,143 | 1,439 | 189 | 34 |
| 24 | 176,637 | 45,347 | 2,639 | 323 | 54 |
| **total** | **368,723** | **93,755** | **6,427** | **907** | **184** |

Thus `F3,F4` remove 87,328 of the 93,755 states left by `F1,F2`, and extending
from `F8` to `F16` removes another 723. The hierarchy has not saturated by
`F8`, although the marginal exclusions become smaller at larger depth.

## Survivor Geometry

The 184 final survivors have 822 cyclic gaps in total; 647 of them (78.7%)
lie between 3 and 6. Even-period survivors are concentrated at defect counts
near `p/4`; odd periods show the corresponding parity-constrained counts.
Most survivors retain primitive `tau` period `p`: 50 of 54 at `p=24`, 29 of
31 at `p=22`, and all survivors at odd periods except the single period-3 row
at `p=21`.

The data therefore support concentration toward sparse defects and local
four-step spacing, but not collapse to one repeated period-eight phase. The
most persistent non-target motifs combine several gaps 3 or 4 with one longer
compensating gap. The all-negative phase and a few low-period repetitions also
survive, as expected from the one-way nature of moment exclusion.

## Answers

1. After `F1,F2`, 93,755 residual orbits remain; after `F16`, 184 remain.
2. The totals after `F4`, `F8`, and `F16` are 6,427, 907, and 184.
3. Survivors strongly favor low defect density and gaps near four, while most
   remain genuinely high-period.
4. There is no complete saturation through `F16`; new exclusions occur at
   every tested depth.
5. The difficult motifs are mixtures of 3/4-spaced defects with a longer
   balancing gap, not a single new universal word.
6. A plausible structural conjecture is that bounded moment depth forces most
   gaps toward a finite neighborhood of four, but the present data do not
   establish such a statement.

Complete curves, first-positive histograms, and final structural records are
stored under `high_period_moments/`. All values are exact integers; no
quadrature or floating spectral computation enters this experiment.
