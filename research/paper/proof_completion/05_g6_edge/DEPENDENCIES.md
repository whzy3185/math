# Dependencies

## Mathematical dependency graph

```text
period-eight bulk edge eta
  -> hyperbolic 2+2 Floquet splitting above eta
  -> coordinate-free stable/unstable matching.

exact G6 core transfer + physical matching
  -> one simple positive root in the c6 interval
  -> algebraic identification by p_6.

global Grassmann cover
  -> complete resultant candidate list
  -> unsquared physical exclusions
  -> no positive level above c6.

G6 reflection identities
  -> K^2=-I and KA=-AK
  -> simple negative partner
  -> rank-two H_6 level and full global edge.
```

## Essential upstream theorems

- Exact period-eight edge `eta` and its unique unit-circle location.
- Finite-defect matching for a fourth-order recurrence.
- Exact Sturm theory and interval arithmetic, applied only to the finite
  objects identified in the proof.

## Exact provenance

- Interface transfer and local Evans isolation:
  `research/proofs/task50/G6_DEFECT_TRANSFER.md` and
  `research/proofs/task50/TARGET_A_EXACT_INTERFACE_THEOREM.md`.
- Degree-ten polynomial:
  `research/proofs/task51/TARGET_A_C6_ALGEBRAIC_THEOREM.md`.
- Root geometry:
  `research/proofs/task52/TARGET_A_C6_POLYNOMIAL_ROOT_GEOMETRY.md`.
- Hyperbolicity, physical branch, atlas, and global exclusion:
  `research/proofs/task53/TARGET_A_G6_GLOBAL_HYPERBOLICITY.md`,
  `research/proofs/task53/TARGET_A_G6_PHYSICAL_BRANCH_DEFINITION.md`,
  `research/proofs/task53/TARGET_A_G6_GRASSMANN_ATLAS.md`, and
  `research/proofs/task53/TARGET_A_G6_GLOBAL_EDGE_THEOREM.md`.
- Rank-two correction:
  `research/proofs/task55/TARGET_A_G6_RANK_DOUBLING_CORRECTION.md`.

These paths are provenance. The dependency graph itself uses only
mathematical theorem names and contains no task-number edge.

## Downstream use

The theorem supplies the equality case in the abnormal single-gap hierarchy,
the two local modes in the exact-`2r` theorem, and the isolated complement
gap used in multi-interface counting.
