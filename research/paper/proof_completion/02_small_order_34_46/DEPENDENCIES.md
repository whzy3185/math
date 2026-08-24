# Dependencies

## Mathematical dependency graph

No historical task number is a node.

    switching normal form
      -> cyclic (Q, alpha) parametrisation
      -> local compression M_W = P A^2 P
      -> exact local exclusion
      -> surviving-window overlap graph
      -> parity soundness, completeness, and cyclic closure
      -> dihedral quotient and both holonomies
      -> exact terminal discharge
      -> no counterexamples at six orders

    explicit order-40 (Q, alpha)
      -> reconstructed full matrix
      -> exact positive-definite LDL certificate
      -> strict rational threshold lower bound
      -> order-40 counterexample

The branches meet only in the interval classification.  The order-40
counterexample is not inferred from a terminal Rayleigh lower certificate.

## Mathematical inputs

| input | use |
|---|---|
| switching invariance | cyclic normal form |
| $Q_i=\tau_i\tau_{i+1}$ and $\prod_iQ_i=1$ | global legality |
| even-order lift conjugacy | fix $\tau_0=1$ |
| Rayleigh principle for $A^2$ | local and terminal lower bounds |
| exact algebraic root isolation | strict endpoints for $\theta_n$ |
| de Bruijn overlap | exact cyclic enumeration |
| positive-definite LDL criterion | order-40 spectral upper bound |

## Provenance appendix

For the six no-counterexample orders:

    producer:
      research/scripts/target_a_task55_small_order_exact.py
    certificate:
      research/proofs/task55/certificates/small_order_exact_classification.json
    independent checker:
      research/scripts/verify_target_a_task55_small_order_exact.py
    tamper suite:
      research/scripts/test_target_a_task55_small_order_exact.py

Certificate SHA-256:

    cb12d8502c6fcf31c5e8f1d23f3b9f1bb44b28b05a58f2e02067df08c04132b4

For order 40:

    producer:
      research/scripts/target_a_task55_orders_34_46.py
    certificate:
      research/proofs/task55/TARGET_A_ORDERS_34_46_CERTIFICATES.json
    independent checker:
      research/scripts/verify_target_a_task55_orders_34_46.py

Certificate SHA-256:

    6385a7e35b69ff32cba41b719faa554eef3060d020d0c54e0fd702d100cb6669

The non-40 rows in the latter artifact are bounded-search provenance only and
are not used to prove nonexistence.  The exact finite-state certificate
supersedes that historical boundary for the six no-counterexample orders.

Reference checkpoint:
e6a01d8bf30088dae1042a237398bee2df138280.

## Record-count correction

The authoritative JSON and checker both require terminal lengths

    2, 2, 6, 14, 20, 20.

Their sum is 64.  The 84 sentence in the historical handoff conflicts with
its own table.  The order-40 artifact stores one LDL row, not twenty omitted
terminal records.
