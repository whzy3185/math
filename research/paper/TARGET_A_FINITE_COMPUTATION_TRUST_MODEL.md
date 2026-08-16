# Target A Finite Computation Trust Model

Status: **TARGET_A_FINITE_COMPUTATION_BOUNDARY_RESTATED**

## Mathematical Verification

The finite theorem for `n=8,10,...,30` is an executable exhaustive
computer-assisted proof. For each canonical `(Q,alpha)` state the production
runner reconstructs the signing, computes a candidate integer Rayleigh vector,
and checks its numerator and denominator with exact integer arithmetic; the
distinguished equality state uses exact polynomial/root isolation. Completion
is accepted only after exact search-space, shell, orbit-size, and holonomy
counts close.

The fresh frozen-worktree runs at `n=24,26,28,30` repeated this mathematical
verification from an empty output directory. A referee can repeat the same
deterministic stream from the frozen source and commands in the reproduction
summary. The theorem does not require trusting a floating-point comparison.

## Integrity Replay

The committed checkpoint chunks store aggregate counts, ordered input and
certificate digests, and a chained hash. They do **not** store every integer
Rayleigh vector. Consequently `target_a_checkpoint_replay.py` is an integrity,
cursor-completeness, and provenance replay. It is not an independent
per-state mathematical-certificate replay.

The historical machine status `FULL_CERTIFICATE_REPLAY_PASS` is retained for
artifact compatibility, but the paper package renders it as
`FULL_CHECKPOINT_INTEGRITY_REPLAY_PASS`. No theorem is allowed to cite the
hash replay without also citing the executable full regeneration route.

## Coverage Levels

- `n=8,10,...,22`: separately audited exact historical runs;
- `n=24,26,28,30`: exact committed runs plus fresh frozen-worktree full
  regeneration;
- `n=32`: explicit exact witness, independent gauge reconstruction, Bareiss,
  rational `LDL^T`, and algebraic threshold comparison.

Thus C3 is classified `FINITE_COMPUTER_ASSISTED`, not
`INDEPENDENTLY_REPRODUCED` over its entire range.

## Quotient Boundary

At `n=30`, 17,929,600 canonical spectral states represent 2,147,483,648
switching classes through the proved `(Q,alpha)/D_n` quotient. The ordered
stream is not 2.147 billion independent pytest cases. Record-for-record
agreement between the visited-set reference generator and the constant-memory
FKM generator now extends through the first production order `n=24`.

## Submission Archive

The public Git commit fixes source, committed production checkpoints,
checkers, dependency hashes, commands, and compact fresh-run summaries. Full
external fresh chunks and runtime logs are reproducibility outputs, not
standalone per-state certificates. A submission supplement should package the
frozen source plus a machine-readable environment lock and command manifest;
the proof claim remains regeneration-based rather than archive-based.
