# Target A Task 47 Synthesis

Date: 2026-08-22

Task: Structure-Directed Supplementary Experiments

Baseline: `9d75ce04fd4509034ef65db50177d236f13479ab`

Existing theorem scope changed: **NO**

Formal manuscript changed: **NO**

## Question 1: Is There a Periodic Phase Below `eta`?

**NO SUCH PHASE APPEARED; GLOBAL QUESTION REMAINS UNRESOLVED.**

The complete two-defect scan through period 64 has no numerical value below
`eta`. Among the 125 most dangerous `F_16` survivors selected at periods
17 through 24, 124 are exactly certified above `eta` and the sole equality is
the zone-folded period-eight target. This is not an all-period classification.

## Question 2: Does Maximal Two-Defect Separation Minimize the Radius?

**FALSE.**

Only `p=8` is minimized at maximal separation. For every tested even
`p=10,...,64`, the numerical minimum occurs at the fixed separation `s=4`.
Simple monotonicity with separation also fails at every `p>=10`.

## Question 3: Is Period Eight Exceptional in the Two-Defect Family?

**YES, WITHIN THE EXPERIMENTAL RANGE.**

The target `(p,s)=(8,4)` is the unique global minimum among 522 cases. The
same local separation produces numerical sub-eight values at `p=10,12,14,16`,
but exact endpoint Rayleigh certificates put all four strictly above `eta`.
The exceptional feature is the interaction between separation four and the
period-eight closure, not antipodality by itself.

## Question 4: Are There Exact Counterexamples Outside `8Z`?

**YES.**

Twenty exactly certified finite examples lie outside `8Z`:

```text
50, 52, 58, 66, 68, 74, 82, 84, 90, 94,
98, 100, 102, 106, 110, 114, 116, 118, 122, 126.
```

Some overlap the repository's earlier period-10 family. Sixteen are divisible
by neither 8 nor 10. The first such order is `n=52`, with `alpha=-1`, two
gap-6 phase slips, and

```text
Q = 1000100010001000100010000010001000100010001000100000.
```

Its exact certificate proves

```text
rho(A)^2 < 79049/10000 < 2679/338 < rho_-(52)^2,
```

so the certified rational lower bound on the squared-radius gap is
`35719/1690000`.

## Question 5: Is There an Infinite Residue-Class Signal?

**YES, AS A CONJECTURAL FAMILY CANDIDATE ONLY.**

Three deterministic sequences appear:

- one gap 6 at `n=50,58,...,122`, residue 2 modulo 8;
- two gaps 6 at `n=52,68,...,116`, residue 52 modulo 16;
- one gap 10 at `n=94,102,...,126`, residue 6 modulo 8.

Every displayed finite instance is exact. No infinite continuation is proved.

## Question 6: What Does the Moment Hierarchy Select?

**SPARSE, NEAR-FOUR-STEP GEOMETRY, BUT NOT A SINGLE MOTIF.**

Across 370,100 complete high-period orbits, survivor totals fall from 93,755
after `F2` to 6,427 after `F4`, 907 after `F8`, and 184 after `F16`. Of 822
final-survivor gaps, 78.7% lie from 3 through 6. Most final rows retain genuine
primitive high period, so the hierarchy concentrates geometry without reducing
everything to a period-eight repetition.

## Question 7: Are the Most Dangerous High-Period Candidates Above `eta`?

**YES FOR EVERY SELECTED CANDIDATE.**

The explicit rule selects 125 candidates. Exact classifications are
`124 GT`, `1 EQ`, `0 LT`, and `0 UNRESOLVED`. This closes the selected danger
set, not all 184 `F16` survivors and not all higher periods.

## Question 8: What Should Happen to Theorem 1.6?

**Recommendation A: KEEP IT AS AN IMPORTANT THEOREM.**

The new evidence does not justify changing `p<=16`. It does show that the
moment method is stronger than the current low-order summary and that a future
theorem may instead arise from one of the explicit phase-slip families. Any
extension should wait for a uniform exact Floquet or finite-family proof.

## Decision Tree Outcome

Primary outcome: **OUTCOME C, FINITE FAMILY EXTENSION CANDIDATE.**

Secondary outcome: **OUTCOME D, MOMENT METHOD STRONGER THAN THE CURRENT
EXPERIMENTAL PRESENTATION.**

The two-defect maximal-separation narrative is rejected. The period-eight
structural narrative remains strong, but the next highest-value proof task is
the residue-class phase-slip family, especially the gap-6 and gap-10 words.

## Phase Summary

### Experiment A: Two-Defect Geometry

- period range: even `8..64`
- cases: 522
- numerical candidates below `eta`: 0
- certified candidates below `eta`: 0
- non-`p=8` numerical cases below 8: 4
- maximal-separation principle: false
- monotonic separation evidence: false beyond `p=8`
- principal anomaly: fixed `s=4` wins every tested period

### Experiment B: Finite Phase Slips

- order range: even `32..128`
- residues: 0, 2, 4, 6 modulo 8
- numerical counterexamples: 33
- exact counterexamples: 33
- exact examples outside `8Z`: 20
- smallest outside `8Z`: 50
- first outside both known 8- and 10-divisible directions: 52
- potential infinite-family signal: strong but unproved

### Experiment C: Moment Hierarchy

- periods: `17..24`
- maximum depth: `F16`
- survivors after `F1/F2/F4/F8/F16`:
  `368723 / 93755 / 6427 / 907 / 184`
- most persistent motifs: sparse gaps concentrated near 3 and 4 with longer
  balancing gaps
- period-eight-like concentration: mixed, local rather than global

### Experiment D: High-Period Certification

- candidates checked: 125
- `CERTIFIED_R_GT_ETA`: 124
- `CERTIFIED_R_EQ_ETA`: 1
- `CERTIFIED_R_LT_ETA`: 0
- `UNRESOLVED`: 0

### Experiment E: Independent Order-22 Audit

- record-level equality: PASS
- missing / duplicate / orbit mismatch: `0 / 0 / 0`
- both holonomies: checked
- spectral states: 97,468
- uncertified: 0

### Optional Local Stability Experiment

Phase VI was not run. Experiments A through E already produced two stronger
follow-up directions, and no theorem claim depends on a local stability scan.

## Final Experimental Status

`TARGET_A_TASK47_EXPERIMENTS_COMPLETE`

The next action should be a separate proof task for the explicit residue-class
families. The formal manuscript must remain frozen until that proof task and a
new review determine the narrative.
