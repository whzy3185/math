# Target A Four-Step Local Stability

A 128-site period-eight bulk gap word is perturbed locally while preserving
total length.  Both holonomies are tested for each pattern.

| Local pattern | Minimum squared radius | Penalty from bulk |
|---|---:|---:|
| `(4,4)` bulk | 7.8008653777 | 0 |
| `(3,5)` | 8.3845291206 | 0.5836637429 |
| `(2,6)` | 8.2750293774 | 0.4741639996 |
| `(3,4,5)` | 8.3182898220 | 0.5174244443 |
| `(2,5,5)` | 8.7113917702 | 0.9105263925 |

Every tested minimal perturbation incurs a positive penalty.

Classification: `LOCALLY_STABLE_SIGNAL`.

The result is finite and numerical.  It supplies reserve evidence for the
four-step-order narrative but is neither local convexity nor a classification
of all perturbations.  Raw data are in `insurance/four_step_stability.json`.
