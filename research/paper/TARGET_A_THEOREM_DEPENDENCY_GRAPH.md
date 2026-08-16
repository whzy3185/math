# Target A Theorem Dependency Graph

Status: **TARGET_A_THEOREM_DEPENDENCY_GRAPH_COMPLETE**

The following table is the human rendering of the canonical JSON DAG. Every
dependency listed here is exact; independent reproduction is reliability
evidence, not a logical premise.

| Theorem | Conclusion | Exact claim dependencies |
|---|---|---|
| THEOREM_A | Smallest counterexample order 32 | C2, C3 |
| THEOREM_B | Infinite family for `n=8L`, `L>=4` | C4, C5, C6, C7 |
| THEOREM_C | Exact period-8 edge `eta`, unique at `z=1` | C5, C6, C7 |
| THEOREM_D | Infinite-volume period-8 trichotomy and unique optimum | C7, C8, C9, C10, C11, C12, C13, C14 |
| THEOREM_E | General-period moments and necessary obstructions | C11, C13, C17, C18, C19, C20, C21 |
| THEOREM_F | Unique low-period frontier through primitive `tau` period 16 | C7, C13, C22, C23, C24, C25 |

C15-C16 are explicitly `SUPPLEMENT_ONLY`; they explain the target chiral
mechanism but are not needed for Theorems A-F.

## Deletion Audit

- Removing C2 leaves no exact failure; removing C3 leaves a failure at 32 but
  no minimality theorem.
- Removing C5 or C6 breaks the finite/infinite Floquet route in Theorems B/C.
- Removing C7 eliminates the target upper bound and all exact comparisons
  against `eta`.
- Removing C13 invalidates every positive-moment-excess exclusion.
- Removing C24 removes the operator-level justification for translation,
  reflection, global negation, and repeated-cell equivalence.
- Removing C22 permits an omitted low-period orbit; removing C25 leaves the
  compressed exclusion partition and five residual certificates unavailable.

Per-node deletion effects and all claim edges are stored in
`target_a_theorem_dependency_graph.json`; the package-lint validator compares
this table with that structured source.
