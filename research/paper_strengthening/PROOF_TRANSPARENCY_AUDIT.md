# Proof transparency audit

| item | manuscript-level derivation | script dependence |
|---|---|---|
| chiral iff | explicit two-coefficient anticommutator plus normalization square | none |
| flux iff | telescoping product and constant ratio argument | none |
| quartic | explicit `RQ`, its trace and determinant, then scalar quadratic | none |
| four bands/gaps | positive `W_delta`, monotonicity, endpoint values, exact gap inequalities | none |
| finite radii | finite phase grid plus unique monotone maximum | none |
| twisted radius | block eigenvalues, grid symmetries, polynomial in `cos^2 theta`, derivative | none |
| `M3` | four closed-step support classes with coefficients `238,156,24,12`, followed by conversion to `d,a,b` | verifier is regression only |
| survivor completeness | parity, density bound, cyclic gap compositions, `(d,a,b)` table, dihedral quotient | verifier is regression only |
| certificates | every vector, phase, and exact negative Rayleigh value printed | none |
| recurrence | initial state, integer recurrence, moment readout, exact positive excesses | verifier is regression only |

The body contains enough information to reproduce every decisive calculation.
Repository scripts audit the displayed identities; they are not cited as proof.
