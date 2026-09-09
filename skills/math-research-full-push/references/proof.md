# Proof / falsification mode

Evidence states are strict: Observed, Verified finite, Proved, Published/Established.

Before long proof work, falsify cheaply: small cases, boundary/degenerate cases, hypothesis removal, equality claims and proposed equivalences. Prefer exact arithmetic.

Maintain a proof DAG. Each obligation records statement, dependencies, status, role, proof idea, failed routes, boundary checks and Lean mapping if relevant.

Prefer structural lemmas: inverse/rigidity, invariant, canonical form, decomposition, compression/switching, arithmetic obstruction, finite-reduction and equality characterization.

A claim is Proved only if every dependency is proved/sourced, all cases close, reductions preserve hypotheses and terminate, external theorem hypotheses match, and adversarial checks reveal no contradiction.

For proof-critical finite computation, prove why the remaining task is finite before treating enumeration as theorem evidence.