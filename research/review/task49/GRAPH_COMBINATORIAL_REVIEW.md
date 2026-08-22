# Task 49 Independent Graph/Combinatorial Review

## Findings

### MODERATE 1: all-even coverage is a proof program, not a theorem

The five residue rows give explicit gap words and the four non-bulk families
have exact finite crossing certificates.  What remains absent is one uniform
lemma proving that each prescribed gap word is legal and below threshold for
all orders beyond an explicit bound.  The future theorem must state the
families algebraically, including small-order degeneracies.

### MODERATE 2: finite Evans closure needs a formal switching lemma

The computation correctly places `alpha` in
`det(M_n(lambda)-alpha I)=0` after switching the step-one edges to `+1`.
This gauge/holonomy reduction should be proved once in the paper, with the
index convention for `Q_i=tau_i tau_{i+1}` and the reflected word stated
explicitly.

### MINOR 1: displayed and primitive periods require consistent terminology

The p=24 equality has displayed Q period 24 but primitive Q period 8 after
zone folding, while tau has its own primitive period.  Tables should retain
all three fields and reserve "unique" for the declared equivalence relation.

## Positive Checks

The independent audit generates bracelets from necklaces, checks orbit
multiplicity against all `2^(p-1)` legal words, independently lifts Q to tau,
constructs both holonomies, and detects primitive repetitions.  Destructive
accounting consumes every one of the 370,100 orbits once.  The odd-period
legality parity issue discovered by the second implementation was corrected
and documented.  The period-eight classification and exact eta are already
proved outside Task 49.

## Verdict

- BLOCKER: 0
- MAJOR: 0
- MODERATE: 2
- MINOR: 1

The bounded-period combinatorial theorem is ready for formal statement.  The
all-even conclusion remains conditional on the uniform spectral estimates.
