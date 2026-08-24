# Dependencies: Moments and Periodic Frontier

## Mathematical DAG

[APPENDIX_REQUIRED]

```text
local signed step-one/step-two operator
  -> closed-walk expansion
  -> first three exact moment identities
  -> moment barrier F_k>0 => R(Q)>8

periodic lift criterion product Q=1
dihedral action and Burnside/bracelet counting
primitive-period reduction and zone folding
  -> finite orbit space for p<=24

moment exclusions
exact endpoint Rayleigh lemma
reference-phase edge eta<c6
  -> complete finite orbit partition
  -> unique bounded phase with R(Q)<c6.
```

Task numbers do not occur as mathematical nodes.

## Elementary dependencies

1. Hermiticity of the Laurent Bloch fiber on `|z|=1`.
2. Rayleigh's variational inequality for `A_Q(z)^*A_Q(z)`.
3. The exact reference-phase identity
   `eta=4+sqrt(10+2sqrt(5))` and the comparison `eta<c6`.
4. A certified rational upper endpoint `c6_upper` for exact witness
   comparisons.

## Provenance map

[REPRODUCIBILITY_ONLY]

```text
research/proofs/TARGET_A_GENERAL_PERIOD_MOMENT_OBSTRUCTIONS.md
research/proofs/target_a_general_period_moment_obstructions.json
research/proofs/TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER.md
research/proofs/target_a_low_period_spectral_frontier.json
research/proofs/task53/TARGET_A_P24_C6_FRONTIER_THEOREM.md
research/proofs/task53/TARGET_A_P24_C6_COMPLETENESS_AUDIT.md
research/proofs/task53/certificates/p24_c6_frontier.json
research/reproducibility/task49/p24_independent/summary.json
```

The provenance paths record the research history. The proof itself depends
only on the named mathematical lemmas and finite certificates above.
