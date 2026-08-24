# Dependencies

## Mathematical dependency graph

```text
one-G6 global edge + rank-two eigenspace
  -> two normalized local modes per interface.

period-eight Floquet contraction q_F=9/25 and basis bound 17
  -> tail bound 73 q_F^ell
  -> 2r-mode Gram invertibility
  -> lower spectral count.

single-G6 complement gap 1/100
  + range-four partition of unity
  + IMS error 4/845
  -> codimension-2r cap c6-1/200
  -> upper spectral count
  -> exact 2r.

Gram coordinates + complement resolvent
  -> 2r-dimensional Schur complement
  -> 3505 r q_F^ell cluster bound.
```

No node in this mathematical graph is named by a research task.

## Exact provenance

- Rank-two local correction:
  `research/proofs/task55/TARGET_A_G6_RANK_DOUBLING_CORRECTION.md`.
- Exact cluster theorem:
  `research/proofs/task55/TARGET_A_EXACT_2R_CLUSTER_THEOREM.md`.
- Correct Feshbach theorem:
  `research/proofs/task55/TARGET_A_2R_FESHBACH_THEOREM.md`.
- Explicit constants:
  `research/proofs/task55/TARGET_A_EXPLICIT_EXPONENTIAL_CONSTANTS_TASK55.md`.
- Single-interface isolation:
  `research/proofs/task54/TARGET_A_G6_SPECTRAL_ISOLATION.md`.
- Certificate:
  `research/proofs/task55/certificates/exact_2r_cluster.json`.

## Historical correction ledger

| formulation | final classification | reason |
|---|---|---|
| one squared mode per G6 | `FALSIFIED` | `dim ker(H_6-c6)=2` |
| exactly `r` squared levels | `FALSIFIED_AS_STATED` | misses the negative unsquared partner after squaring |
| codimension-`r` complement | `FALSIFIED_AS_STATED` | does not remove the full local eigenspace |
| unrestricted `r x r` Feshbach operator | `FALSIFIED_AS_STATED` | physical near-edge space has dimension `2r` |
| exact `2r` for `r=1,2,3`, `D>=1040` | `COMPUTER_ASSISTED_PROVED` | independent checker pass |

An `r x r` formula could only be valid after a separately proved invariant
symmetry-sector reduction. No such reduction is assumed here.

## Downstream use

The theorem gives quantitative separated-interface constructions and the
explicit constants used in eventual residue bounds. It does not prove a
universal interaction sign, finite-ring simplicity, or exact counting for
arbitrary numbers of interfaces.
