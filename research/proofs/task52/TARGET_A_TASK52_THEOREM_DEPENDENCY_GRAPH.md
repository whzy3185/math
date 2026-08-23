# Task 52 Theorem Dependency Graph

## Nodes

| Node | Status |
|---|---|
| Period-eight theorem | PROVED |
| Charge conservation | PROVED |
| Translation-sector theorem | PROVED |
| G6 exact interface | COMPUTER_ASSISTED_PROVED |
| Plus/minus-two algebraic theorem | COMPUTER_ASSISTED_PROVED |
| Competitive single-charge comparisons | COMPUTER_ASSISTED_PROVED |
| Primitive-interface completeness | OPEN |
| Elementary-charge theorem | CONDITIONAL |
| Bulk propagation estimate | PROVED |
| r=2 cluster existence | PROVED |
| r=3 cluster existence | PROVED |
| r=2 exact count/global cap | OPEN |
| r=3 exact count/global cap | OPEN |
| Residue-2 upper theorem | CONDITIONAL |
| Residue-4 upper theorem | CONDITIONAL |
| Residue-6 upper theorem | CONDITIONAL |
| Unified limsup theorem | CONDITIONAL |
| Eventual all-even theorem | CONDITIONAL |
| c6-moment constraints | PROVED |
| Low-energy grammar | EXACT_FINITE |
| Dense-defect lower bound | OPEN |
| Sparse-defect reduction | OPEN |
| Truncated G6 lower bound | PROVED |
| Future common-limit theorem | OPEN |

## Edges

| From | To | Exact dependency |
|---|---|---|
| Period-eight theorem | G6 exact interface | supplies the hyperbolic bulk monodromy |
| Charge conservation | Translation-sector theorem | identifies `q=g-4` and legal concatenation |
| G6 exact interface | Plus/minus-two theorem | supplies one physical root and stable-root nondegeneracy |
| G6 exact interface | Competitive comparisons | supplies the exact c6 comparison interval |
| Competitive comparisons | Elementary-charge theorem | excludes listed single-gap competitors |
| Primitive-interface completeness | Elementary-charge theorem | required to exclude every composite primitive interface |
| G6 exact interface | Bulk propagation | supplies stable multiplier bounds and localized mode |
| Bulk propagation | r=2 cluster | controls two truncated quasimode residuals |
| Bulk propagation | r=3 cluster | controls three truncated quasimode residuals |
| Charge conservation | Residue-2 upper | supplies the legal one-slip family |
| Charge conservation | Residue-4 upper | supplies the legal two-slip family |
| Charge conservation | Residue-6 upper | supplies the legal three-slip family |
| r=2 global cap | Residue-4 upper | excludes hidden finite-ring levels |
| r=3 global cap | Residue-6 upper | excludes hidden finite-ring levels |
| r=1 global finite-ring cap | Residue-2 upper | excludes hidden finite-ring levels |
| Three residue upper theorems | Unified limsup | take balanced separation to infinity |
| Unified limsup and period-eight theorem | Eventual all-even | combine upper levels below 8 with `rho_-^2 -> 8` |
| M1-M6 identities | c6-moment constraints | form `M_(k+1)-c6 M_k` |
| c6-moment constraints | Low-energy grammar | gives local exclusion inequalities |
| Low-energy grammar | Dense-defect lower bound | would require a positive cycle penalty, currently absent |
| Charge/sector theorem | Sparse-defect reduction | labels local limits by interface charge |
| G6 exact interface | Truncated G6 lower bound | supplies the exponentially decaying test state |
| Dense lower bound, sparse reduction, truncated/interface lower bounds | Future common-limit theorem | together would prove the missing liminf |

The cluster-existence nodes do not feed an upper theorem without the separate
global-cap nodes. This separation prevents the logical error of converting
quasimodes into a spectral-radius upper bound.
