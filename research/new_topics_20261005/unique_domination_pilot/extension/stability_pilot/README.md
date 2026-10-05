# Stability pilot at the first boundary

This separate pilot studies unlabelled edge-edit distance to the unique extremal graph at n=3γ+1. A cost of one is assigned to each edge addition or deletion; all vertex relabellings are allowed. The graph class is unchanged, and the lower-bound examples are connected.

Results with separate independent mathematical audit PASS:

- An explicit graph with exact edge deficit t=s has edit distance between s(γ/2+1) and s(γ+1), for even γ and1≤s≤γ/2−1
- Consequently no universal O(γ√t+t) bound holds
- Even dense asymptotic edit stability fails: relative edge deficit tends to zero while normalized edit distance stays at least1/72 in the constructed sequence
- A complete analytic upper proof gives dist≤12γt for every graph in the class, the matching order of dependence

EDIT_STABILITY_OBSTRUCTION.md and LINEAR_DEFICIT_STABILITY.md contain the proofs. check_stability.py and exact_results.json provide bounded exact verification of the construction and template arithmetic; they do not replace the all-graph proof. LITERATURE_SCOPE.md distinguishes the precise edge-edit question from parameter stability and leaf-deletion results. Previously reviewed papers remain unchanged.

The independent reports are audit/OBSTRUCTION_AUDIT.md and audit/linear_upper/UPPER_BOUND_AUDIT.md. The upper scope includes disconnected graphs without isolates; the examples witnessing the lower bound are connected.
