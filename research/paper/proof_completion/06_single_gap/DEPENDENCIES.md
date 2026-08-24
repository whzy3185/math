# Dependencies

## Mathematical dependency graph

```text
single-gap Q word
  -> canonical tau lift
  -> finite-support Rayleigh identity
  -> six exact small-gap witnesses
  -> one uniform large-gap witness
  -> strict uniform separation outside {4,6}.

period-eight edge eta
  -> gap four is the reference bulk.

global G6 edge and rank-two theorem
  -> equality and multiplicity at gap six.
```

## Essential inputs

- The exact upper isolating endpoint for `c6`.
- The global equality `sup sigma(H_6)=c6` and its rank-two eigenspace.
- The elementary variational principle for a bounded self-adjoint operator.

The strict inequalities for `g not in {4,6}` are otherwise self-contained in
the integer vectors printed in `FULL_PROOF.md`.

## Exact provenance

- Complete single-gap variational proof:
  `research/proofs/task56/TARGET_A_SINGLE_GAP_NIGHT_REPORT.md`.
- Canonical strict uniform corollary:
  `research/proofs/task57/TARGET_A_UNIFORM_SINGLE_GAP_SEPARATION.md`.
- Exact comparison certificate:
  `research/proofs/task57/certificates/uniform_single_gap_separation.json`.
- Independent checker and focused tests:
  `research/scripts/verify_target_a_task57_uniform_single_gap.py` and
  `research/scripts/test_target_a_task57_uniform_single_gap.py`.

## Downstream use

The theorem makes G6 the unique abnormal single-gap minimizer with a uniform
buffer. It may be used to reject any competing *single-gap* local limit. It
cannot, without an additional reduction theorem, reject arbitrary multi-gap
cores.
