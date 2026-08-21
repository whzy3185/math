# Target A Computational Final Re-review

Date: 2026-08-21

Role: independent referee for computer-assisted mathematics

Reviewed repository HEAD:
`d4df8dfdd00493d8051577e4d42ce04cf55bb6df`

Immutable content snapshot:
`bb3c8aca39a27c76e8b76bbe733b84d0fd1fafc6`

Recommendation: **PUBLICATION-READY COMPUTATIONAL EVIDENCE**

Severity counts: **BLOCKER 0 / MAJOR 0 / MODERATE 0 / MINOR 0**

## Scope

This short final re-review addresses the two MODERATE archival findings in the
previous report. I inspected the shared worktree, ran only lightweight
verification and targeted tests, and did not rerun the expensive `n=30`
enumeration or spectral decision job. No code or manuscript file was modified.

## MODERATE 1: Final immutable snapshot and submission manifest

**Status: RESOLVED.**

`research/reproducibility/target_a_submission_artifact_manifest.json` now:

- identifies the complete immutable snapshot
  `bb3c8aca39a27c76e8b76bbe733b84d0fd1fafc6`;
- contains exactly 35 authenticated files;
- records independent representative equality and the independent full
  spectral decision at all four large orders `n=24,26,28,30`;
- no longer contains the obsolete `n=24` recordwise limit.

`research/scripts/verify_target_a_submission_artifact_manifest.py` authenticates
each listed file by reading it from the named commit with `git show`, requires
the 35-file inventory and both four-order lists, and explicitly rejects the old
`recordwise_independent_generator_limit` field. A direct negative test obtained
`VERIFY_THEOREM_A_OBSOLETE_RECORDWISE_LIMIT_FAIL` after that field was inserted
into an in-memory copy of the valid manifest.

The English and Chinese immutable-snapshot references and computational trust
boundary statements consistently point to `bb3c8aca...`. The snapshot therefore
contains the complete synchronized manuscripts, evidence, verifiers, and
submission inventory that its public reference promises.

## MODERATE 2: Strengthened verifier absent from the trusted evidence graph

**Status: RESOLVED.**

`research/reproducibility/target_a_computational_evidence_manifest.json` now
authenticates 22 files and includes all three previously missing trust-chain
components:

- `research/scripts/verify_target_a_computational_evidence.py`;
- `research/scripts/test_target_a_computational_evidence.py`;
- `research/scripts/build_target_a_computational_evidence_manifest.py`.

I independently read every one of the 22 files from immutable snapshot
`bb3c8aca...` and recomputed its SHA-256. All 22 hashes match the computational
evidence manifest.

`research/audit/TARGET_A_MINIMALITY_DEPENDENCIES.json` also includes
`verify_target_a_computational_evidence.py`. Its recorded digest
`9916cbb68151e58592c5c531076f0db11ae0cac153d5abd10fe9658a302910fd`
matches the verifier source in the immutable snapshot. The top-level
minimality verifier imports and requires this strengthened verifier, so the
logical theorem gate and the archival dependency graph now bind the same
implementation.

## Lightweight Verification

| Check | Result |
|---|---|
| Submission artifact manifest verifier | PASS: hashes, Theorem A coverage, Theorem F coverage, and final manifest gate |
| Obsolete `n=24` limit negative test | PASS: rejected with `VERIFY_THEOREM_A_OBSOLETE_RECORDWISE_LIMIT_FAIL` |
| Computational evidence verifier | PASS for `n=24,26,28,30`, including exact maximum-root isolation |
| Immutable-snapshot recomputation of all 22 computational evidence hashes | PASS: zero mismatches |
| Minimality dependency digest for the strengthened verifier | PASS: exact match |
| Top-level minimality verifier with checkpoint replay disabled | `SMALLEST_COUNTEREXAMPLE_VERIFIED`; strengthened evidence PASS |
| Targeted submission/evidence/minimality regression tests | `11 passed` |
| Full `n=30` recomputation | Not run, as instructed |

The computational evidence verifier's `n=30` report in the table above is a
verification of the committed exact evidence, counts, hashes, and optimizer
root certificate. It is not a fresh rerun of the 17,929,600-state decision job.

## Residual Correlated Risk

The following disclosed trust boundaries remain, but no longer constitute a
review finding:

- Both enumeration routes implement the same proved `(Q,alpha)/D_n` quotient,
  binary convention, and dihedral action. Source-level independence cannot
  detect an error in that common mathematical specification.
- Both spectral routes share the Hamilton-gauge mathematics, algebraic
  threshold specification, NumPy proposal layer, and SymPy certification
  library. The final accepted inequalities are nevertheless exact.
- Per-state integer proposal vectors are regenerated rather than archived. The
  immutable evidence binds ordered decision digests and zero-uncertified
  counts; historical state-level inspection requires regeneration.
- This referee did not rerun the full `n=30` computation. The conclusion for
  that order relies on the immutable hash-bound execution record, exact
  aggregate identities, independent decision evidence, and current exact
  verifiers.

These correlations are accurately disclosed in the trust map and manuscripts.
They are ordinary residual assumptions of this computer-assisted proof, not an
unreported search/certificate gap or a floating-point theorem decision.

## Final Verdict

Both former MODERATE findings are closed. The immutable submission snapshot is
complete and semantically current; the strengthened verifier, its test, and its
builder are hash-bound; and the verifier itself is mandatory in the minimality
dependency graph and top-level theorem gate.

Final assessment:
**BLOCKER 0 / MAJOR 0 / MODERATE 0 / MINOR 0**.

From the computational-referee perspective, Target A is ready for publication.
No additional `n=30` rerun is required for this conclusion.
