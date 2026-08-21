# Independent Large-Order Spectral Audit

This directory records a second complete decision route for Target A orders
`n=24,26,28,30`.

The canonical records are emitted by the independent C full-space scanner.
`target_a_independent_spectral_audit.py` then reconstructs both Hamilton
holonomies without importing the production signing, matrix, threshold, or
certificate routines. A floating eigensolver proposes an integer vector; the
accepted Rayleigh comparison is evaluated with exact integer and rational
arithmetic. The distinguished state is checked by exact characteristic-
polynomial divisibility.

Run from the repository root with the pinned Python environment:

```bash
.venv-target-a/bin/python \
  research/scripts/target_a_independent_spectral_audit.py \
  --n 24 26 28 30
```

The per-order JSON files contain counts, exact threshold intervals, decision
digests, source-independent scanner summaries, and all PASS conditions. The
summary binds the driver, C scanner, comparison generator, environment, and
detail-file hashes. The authenticated cross-manifest is
`research/reproducibility/target_a_computational_evidence_manifest.json`.

The integer Rayleigh vectors are regenerated rather than archived one file per
state. This is an execution and storage boundary, not a floating-point theorem
decision.
