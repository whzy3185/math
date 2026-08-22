# Target A Two-Defect Geometry Report

Date: 2026-08-22

Status: **EXPERIMENT COMPLETE; NO THEOREM EXTENSION**

## Coverage

The scan covers all 522 reflected separation classes for even periods
`8<=p<=64`. Every case has an adaptive continuous-Bloch numerical estimate,
exact defect statistics, primitive `Q` and `tau` periods, and exact moments
through `F_8`. Machine-readable records are in
`two_defect_geometry/summary.json` and `all_records.csv`.

## Main Findings

1. **Maximal separation principle: false.** Only `p=8` is minimized at `s=p/2`.
   Every tested `p>=10` is instead minimized numerically at the fixed
   separation `s=4`.
2. **Candidate below `eta`: none.** The unique numerical global minimum is
   `(p,s)=(8,4)`, equal to `eta` by the existing theorem. No other grid or
   adaptive estimate is below `eta`.
3. **Other sub-eight phases: yes, numerically.** The cases `(10,4)`, `(12,4)`,
   `(14,4)`, and `(16,4)` have numerical estimates below 8. Exact endpoint
   Rayleigh certificates prove all four are nevertheless strictly above
   `eta`.
4. **Monotonicity: false.** Only `p=8` is nonincreasing over the complete
   separation range. All larger tested periods have adjacent monotonicity
   violations.
5. **Period-eight anomaly: supported.** Up to the exact equivalences recorded
   in the data, `(8,4)` is the unique two-defect minimizer in the scan and the
   only case equal to `eta`.

## Scientific Interpretation

The data reject Hypotheses A and B as originally stated. They support a
different local principle: the four-step separation inherited from the target
remains preferred even after the period grows, while antipodal separation
does not. Hypothesis C receives no candidate support. Hypothesis D is true at
the numerical level for four additional periods, with exact lower comparisons
showing that none improves the target. Hypothesis E is strongly supported
experimentally but is not promoted to a theorem.

The most promising proof question is therefore not a general antipodal theorem
but an exact analysis of the fixed-`s=4` two-defect family as the complementary
arc length varies.

## Evidence Boundary

Adaptive floating maximization is labeled numerical throughout. The report
does not claim certified continuous-fiber upper bounds for non-target cases.
Its rigorous statements are only the inherited exact target equality and the
explicit endpoint Rayleigh lower comparisons. The formal manuscript and all
theorem statements remain unchanged.
