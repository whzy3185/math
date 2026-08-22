# Target A JCTB Fact Inventory

This inventory is the sole Task 49 source for deciding how a future manuscript
may phrase the mechanism story.  `Status` describes the strongest present
claim, not the desired theorem.

## Core Facts

| # | Claim | Status | Source and raw data | Evidence / independent check | Safe wording | Unsafe overclaim |
|---:|---|---|---|---|---|---|
| 1 | `n=32` is the smallest failure of the original conjecture. | COMPUTER-ASSISTED PROVED | `research/review/TARGET_A_FINITE_MINIMALITY_TRUST_MAP.md`; finite certificates | Exact exhaustive finite verification; independent reconstruction and verifiers | "The first failure occurs at order 32." | "A numerical search suggests 32." |
| 2 | Four-step spacing is the preferred local organization. | EXPERIMENTAL SIGNAL | `insurance/four_step_stability.json`; Task 47 moment/gap data | Five deterministic local perturbations and exact bounded-period structure agree | "The evidence identifies four-step local order as the preferred bulk organization." | "Every local perturbation is rigorously penalized." |
| 3 | The period-eight bulk edge is `eta=4+sqrt(10+2sqrt(5))`. | PROVED | `research/proofs/TARGET_A_PERIOD8_SHARP_CONSTANT.md` | Symbolic derivation plus independent verifier | "The period-eight edge equals eta exactly." | Any decimal-only presentation as the proof |
| 4 | The legal period-eight phases satisfy the proved target/runner-up/strict-above-8 trichotomy. | PROVED | `research/proofs/TARGET_A_PERIOD8_PATTERN_CLASSIFICATION.md` | Complete exact orbit classification | "The period-eight trichotomy is exact up to the established equivalences." | Extending the trichotomy to arbitrary period |
| 5 | Up to displayed period 24, the target repetition is the unique optimum. | COMPUTER-ASSISTED PROVED | `reproducibility/task49/p24_independent/summary.json` | Two implementations; exact destructive accounting of 370,100 orbits | "Among legal displayed periods at most 24, equality is unique up to equivalence and repetition." | "The target is optimal among all periods." |
| 6 | A gap-6 interface has limiting squared level `c6=7.905369311620327...`. | HIGH-PRECISION EVIDENCE | `task48a/interface/constants.json` | 220-digit Evans root, boundary-margin check, finite-family convergence | "High-precision Evans computation gives c6..." | Calling the PSLQ polynomial or c6 exact |
| 7 | A gap-10 interface has limiting squared level `c10=7.977104370400546...`. | HIGH-PRECISION EVIDENCE | `task48a/interface/constants.json` | 220-digit Evans root and independent boundary margin | "High-precision Evans computation gives c10..." | Claiming an accepted exact polynomial |
| 8 | Single-interface finite corrections decay exponentially. | HIGH-PRECISION EVIDENCE | `uniform_bounds/g6_uniform_error.csv`, `g10_uniform_error.csv` | Stable normalized envelopes through about 1024 sites; double-resolution failures retained | "The finite-size data support exponential convergence with the slow Floquet multiplier." | "A uniform exponential inequality is proved." |
| 9 | G6 and G10 states are exponentially localized. | HIGH-PRECISION EVIDENCE | `localization_robustness/raw/`, `localization_robustness.csv` | Six raw profiles, both tails, five windows, all fits `R^2>0.98` | "The computed interface eigenvectors are robustly exponentially localized." | "An exact localization theorem holds." |
| 10 | Localization decay matches the slow bulk Floquet multiplier. | HIGH-PRECISION EVIDENCE | `interface_mechanism/floquet_multipliers_full.json`; localization CSV | Full reciprocal multiplier calculation and multiple fit windows | "The observed tail rate agrees with the slow stable Floquet multiplier." | Exact equality inferred from fitted FP64 vectors |
| 11 | Two gap-6 interface levels split on the `mu6^L` scale. | HIGH-PRECISION EVIDENCE | `interface_mechanism/two_interface_high_precision.csv` | 80/120/160-digit 4x4 Evans roots; two full-matrix checks | "The splitting ratio converges numerically to the slow multiplier." | "The leading coefficient and remainder are proved." |
| 12 | The preferred two-slip geometry alternates between the symmetric and shifted families modulo 16. | EXACT FINITE DATA | Task 48A scan and Task 49 crossing/splitting data | All inequivalent separations over the prescribed finite range, both holonomies | "The finite scan exhibits a robust mod16 geometry selection." | "Floquet phase alone proves the mod16 rule." |
| 13 | The shifted residue-12 family has 29 exact counterexamples from 60 through 508 in steps of 16. | EXACT FINITE DATA | Task 48A residue-12 certificates | Exact rational certificate verification for every listed order | "All 29 prescribed residue-12 instances are certified." | "Every order 12 mod16 is covered without a uniform proof." |
| 14 | Explicit structural candidates exist in every even residue class. | EXACT FINITE DATA | `figure_data/figure4_residue_patterns.csv` | Family formulas and representative exact finite certificates | "No even residue class lacks an explicit phase-slip candidate family." | "All sufficiently large even orders are proved counterexamples." |
| 15 | The four explicit families first cross numerically and exactly at 50, 94, 52, and 60. | EXACT FINITE DATA | `threshold_crossings/threshold_crossings.csv` | Exact counterexample certificates at and after each onset | "These are first certified crossings of the named families." | Calling them residue-class minimality results |
| 16 | Single-tail and two-tail formulas are the correct candidate uniform bounds. | EXPERIMENTAL SIGNAL | `uniform_and_crossing_summary.json` | Normalized-error stability and model comparison | "The data select these templates for the next proof." | Publishing empirical constants as theorem constants |
| 17 | The exact Hankel hierarchy reduces 184 moment survivors to the unique target repetition. | COMPUTER-ASSISTED PROVED | `reproducibility/task49/hankel_independent/summary.json` | Independent exact principal-minor search on all 184 inputs | "The exact depth-five Hankel audit leaves one target repetition." | Turning the bounded input set into arbitrary-period rigidity |
| 18 | Separated +2 slips are favored for total excess 4 and 6 among tested charges. | EXPERIMENTAL SIGNAL | `insurance/charge_landscape.json` | Both holonomies, deterministic large-separation comparisons | "The tested charge landscape favors separated +2 slips." | A general charge-selection theorem |
| 19 | Minimal tested perturbations of four-step order have positive finite-ring penalties. | EXPERIMENTAL SIGNAL | `insurance/four_step_stability.json` | Both holonomies for four perturbation types | "All tested local perturbations raise the finite-ring level." | Local convexity or exhaustive stability |
| 20 | The interface method has not been tested on a nearby graph model. | OPEN | `insurance/interface_portability.json` | Explicit resource stop | "Portability is outside the present scope." | Claiming either universality or model-specific failure |

## Additional Publication Facts

| # | Claim | Status | Source and raw data | Evidence / independent check | Safe wording | Unsafe overclaim |
|---:|---|---|---|---|---|---|
| 21 | The period-eight family gives infinitely many failures in its proved congruence class. | PROVED | `research/proofs/TARGET_A_PERIOD8_FAMILY.md` | Exact Floquet polynomial, uniform spectral bound, threshold comparison | "The period-eight construction is an infinite proved family." | Using it to cover other even residues |
| 22 | The relevant bulk multipliers at c6 and c10 are positive real reciprocal pairs. | HIGH-PRECISION EVIDENCE | `interface_mechanism/floquet_multipliers_full.json` | 120-digit eigensolve; reciprocal errors below `3e-118` | "The computed multipliers are positive real and reciprocal." | Exact sign/phase theorem without symbolic isolation |
| 23 | Transfer cut and orientation do not change the physical interface values. | HIGH-PRECISION EVIDENCE | `interface_mechanism/interface_invariance.csv` | Four cuts, two orientations, dense/sparse/Evans checks | "The constants are invariant under the tested representations." | General gauge theorem derived solely from numerics |
| 24 | Adversarial periods 25--40 are strongly filtered by depth-five Hankel tests. | EXPERIMENTAL SIGNAL | `insurance/hankel_beyond_p24_stress.json` | 80 deterministic states, 8 survivors | "A bounded adversarial stress test supports the hierarchy." | Classification of periods 25--40 |

## Status Counts

- `PROVED`: 3
- `COMPUTER-ASSISTED PROVED`: 3
- `EXACT FINITE DATA`: 4
- `HIGH-PRECISION EVIDENCE`: 7
- `EXPERIMENTAL SIGNAL`: 6
- `OPEN`: 1

The count is by the 24 entries above.  A future manuscript writer must cite
the exact row and preserve its evidence qualifier.
