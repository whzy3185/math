# Target A Computational Re-review

Date: 2026-08-21

Role: independent referee for computer-assisted mathematics

Recommendation: **COMPUTATIONAL CORE PASS; ARCHIVAL FOLLOW-UP REQUIRED**

Severity counts: **BLOCKER 0 / MAJOR 0 / MODERATE 2 / MINOR 0**

## Scope

This is a line-by-line re-review of the six findings in the earlier Reviewer
Compute report. I reviewed the current shared worktree without modifying code or
manuscript files and without rerunning the expensive `n=30` enumeration or
spectral decision job.

The re-review covers:

- the C full-space representative stream;
- `target_a_record_set_audit.py` and its four-order evidence;
- `target_a_independent_spectral_audit.py` and its four-order evidence;
- `target_a_computational_evidence_manifest.json`;
- `verify_target_a_computational_evidence.py`, including exact optimizer-edge
  verification;
- the top-level minimality gate;
- the English and Chinese descriptions of the computational trust boundary.

## Executive Assessment

The mathematical-computational content of the two former MAJOR findings is now
closed. The repository has a genuinely separate large-order spectral decision
route: canonical records are emitted by the C full-space scanner, both
holonomies are reconstructed by a standalone Python implementation, and every
nonoptimizer is excluded by an exact integer Rayleigh quotient against a
certified algebraic upper endpoint. The recorded runs pass at all four orders
`n=24,26,28,30`, including 17,929,600 spectral states at `n=30`.

The strengthened evidence is now hash-bound and mandatory in the top-level
minimality verifier. A separate small verifier reconstructs the distinguished
optimizer and uses exact characteristic-polynomial root isolation to prove that
the threshold is the largest eigenvalue of `A^2`, rather than merely a
characteristic root.

I found no BLOCKER or MAJOR defect. Two publication-archive issues remain at
MODERATE severity. They do not invalidate the recorded exact decisions, but
they should be closed before the repository is presented as the final immutable
submission artifact.

## Disposition of Original Findings

### MAJOR 1: Search/certificate separation

**Status: RESOLVED.**

`target_a_independent_spectral_audit.py` supplies the alternative requested by
the original report: a second full decision implementation through `n=30`.
Its spectral input is the record file written by the C scanner
(`target_a_independent_spectral_audit.py`, lines 104--123 and 225--245), not the
production FKM traversal. It does not import the production signing, matrix,
threshold, or Rayleigh functions. It independently:

1. reconstructs `Q`, `tau`, both values of `alpha`, and the signed adjacency
   matrix (lines 157--181 and 245--253);
2. obtains only a proposed integer vector from the floating eigensolver;
3. computes `||Av||^2/||v||^2` with integer arithmetic (lines 184--191);
4. compares the resulting `Fraction` with a certified rational upper endpoint
   for the algebraic threshold (lines 142--154 and 264--290);
5. requires every nonoptimizer to be exactly excluded and the uncertified list
   to be empty (lines 298--310).

The four archived details report:

| `n` | canonical `Q` representatives | spectral states | exact nonoptimizer exclusions | uncertified |
|---:|---:|---:|---:|---:|
| 24 | 176,906 | 353,812 | 353,811 | 0 |
| 26 | 649,532 | 1,299,064 | 1,299,063 | 0 |
| 28 | 2,405,236 | 4,810,472 | 4,810,471 | 0 |
| 30 | 8,964,800 | 17,929,600 | 17,929,599 | 0 |

This route remains a regeneration proof rather than an archive of every vector,
but that is now a disclosed residual trust boundary, not a missing independent
decision implementation.

### MAJOR 2: Evidence absent from the trusted theorem gate

**Status: RESOLVED for the logical theorem gate.**

`verify_target_a_minimality_certificate.py` now:

- imports the strengthened evidence verifier (line 14);
- hard-codes the SHA-256 of the computational evidence manifest (lines 23--30);
- rejects a manifest-hash mismatch (lines 250--254);
- executes the strengthened verifier and requires its PASS result before
  checkpoint replay or the `n=32` witness is accepted (lines 255--261).

A fresh top-level run with checkpoint replay disabled returned
`SMALLEST_COUNTEREXAMPLE_VERIFIED` and included four PASS strengthened-evidence
reports. Thus the old theorem gate can no longer pass merely from production
counts and opaque checkpoint digests while ignoring the new record and spectral
audits.

The English and Chinese manuscripts now describe recordwise equality at all
four large orders, distinguish integrity replay from decision regeneration,
describe the second full spectral route, and disclose the remaining shared
quotient/vector-archive boundaries. Their mathematical trust-boundary accounts
are materially aligned.

The final immutable submission packaging is not yet synchronized; that is
recorded separately as MODERATE 1 below.

### MODERATE 1: Holonomy and factor-four coverage

**Status: RESOLVED.**

The independent spectral loop explicitly evaluates each C record for
`alpha=-1,+1` (lines 245--253). PASS requires exactly two decided states per
representative, a unique exact optimizer, all other states exactly excluded,
and no uncertified state (lines 298--310). The evidence verifier independently
checks the spectral-state count, both-holonomy label, representative agreement,
and the `2^(n+1)` switching-class total at each order
(`verify_target_a_computational_evidence.py`, lines 128--138).

The factor of four still uses the proved cycle-space statement that a `Q` orbit
of size `s` has two holonomies and two global-sign lifts. That is an appropriate
human-proof interface and is now exercised, rather than merely asserted, by the
second decision route.

### MODERATE 2: Overstated generator independence

**Status: RESOLVED, with correlated risk disclosed.**

The record-set summary now distinguishes unshared canonicalization code and
traversal from the necessarily shared group-action specification and binary
`Q` semantics (`target_a_record_set_audit.py`, lines 197--206). The trust map
and both manuscripts make the same distinction. The revised wording no longer
equates different source files with complete mathematical independence.

### MODERATE 3: Recorded-run provenance

**Status: RESOLVED for the recorded evidence.**

The record-set summary now binds the driver hash, primary-generator hash,
repository HEAD, command, compiler/C-source hash, and every detail-file hash
(`target_a_record_set_audit.py`, lines 185--235). The independent spectral
summary similarly binds all three source routes and every per-order detail hash
(`target_a_independent_spectral_audit.py`, lines 337--395).

The computational evidence manifest authenticates 19 sources, summaries,
details, the trust map, and production checkpoint manifests. Its verifier
checks every file hash, cross-checks summary/detail hashes, aligns the two routes
order by order, verifies all PASS predicates, and recomputes class, state,
holonomy, and optimizer conditions (`verify_target_a_computational_evidence.py`,
lines 88--148).

### MINOR 1: Odd-order input accepted under the wrong parity convention

**Status: RESOLVED.**

Both the C scanner and Python driver now reject every odd order and restrict the
interface to even `n` in `[8,30]` (`target_a_independent_orbit_scan.c`, lines
64--70; `target_a_record_set_audit.py`, lines 101--103). The regression suite
explicitly requires `audit_order(9, ...)` to raise an error.

## Exact Optimizer-Edge Verification

The independent spectral runner itself checks exact divisibility by the
threshold minimal polynomial. The small evidence verifier adds the missing
maximal-root argument. For each `n=24,26,28,30`, it reconstructs the optimizer
matrix, forms the exact integer characteristic polynomial of `A^2`, and checks
minimal-polynomial divisibility (`verify_target_a_computational_evidence.py`,
lines 53--74). It then isolates every real characteristic root. Exactly one
isolating interval contains the algebraic threshold, and for every other
interval it requires, by exact algebraic sign, that the interval's right
endpoint is strictly below the threshold (lines 75--85).

Since `A^2` is real symmetric positive semidefinite, this proves that the
threshold is its largest eigenvalue. It is stronger than checking that the
threshold is merely some eigenvalue.

## Remaining Findings

### MODERATE 1: Final immutable snapshot and submission manifest are stale

The older submission manifest still states
`recordwise_independent_generator_limit: 24` and describes `n=26,28,30` as
aggregate-only (`target_a_submission_artifact_manifest.json`, lines 19--28 and
144--147). Its verifier currently passes because it checks file hashes and
theorem coverage but does not reject this obsolete semantic limitation.

The English and Chinese manuscripts correctly describe the strengthened
evidence, but both still cite immutable snapshot `c81be34...`, which predates
the new uncommitted scanner, independent spectral audit, evidence artifacts,
and gate changes. The computational evidence manifest records HEAD `98f9815...`,
but that commit likewise does not contain the currently untracked evidence
files.

Executable resolution before publication:

1. commit the reviewed code, evidence, gate, trust map, and synchronized
   manuscripts;
2. update the submission manifest to recordwise equality and independent
   spectral decisions through `n=30`, and include the strengthened manifest;
3. replace the old immutable URL in both manuscripts with a snapshot that
   actually contains the evidence;
4. rerun both manifest verifiers and the top-level minimality gate.

### MODERATE 2: The strengthened verifier source is not hash-bound by its own evidence graph

The computational evidence manifest authenticates the scanner, both audit
drivers, the primary generator, evidence files, trust map, and checkpoint
manifests. It does not include
`research/scripts/verify_target_a_computational_evidence.py`. The top-level
minimality checker authenticates the manifest hash and trusts the imported
verifier's return value, while the older dependency graph also omits this
verifier.

The current verifier was inspected and executed successfully, so this is not a
present correctness failure. It is an archival trust-chain gap: an altered
imported verifier is not detected by the hard-coded manifest hash alone.

Executable resolution: add the strengthened verifier source to the minimality
dependency manifest, or have the top-level checker verify a hard-coded SHA-256
for that source before calling it. Include its regression test and manifest
builder in the final submission inventory as supporting provenance.

## Correlated Implementation Risk That Remains

The following risk is real and should remain disclosed even after the two
MODERATE packaging items are fixed:

- Both enumeration routes implement the same proved `(Q,alpha)/D_n` quotient,
  binary convention, and dihedral group action. Different code does not protect
  against an error in that common mathematical specification.
- Both spectral routes use the same Hamilton-gauge mathematics, the same
  algebraic threshold formula, NumPy for vector proposal, and SymPy for
  algebraic certification. Their source implementations are separate, but
  library-level and specification-level correlation remains.
- Per-state integer vectors are regenerated rather than archived. The committed
  compact evidence binds ordered decision digests and zero-uncertified counts;
  independent verification of an individual historical state still requires
  rerunning the corresponding route.
- This referee did not rerun the full `n=30` job. Confidence in that order uses
  the hash-bound recorded execution, exact aggregate checks, current verifier,
  and consistency with the freshly reproduced lower-order route.

None of these is a floating-point theorem decision: all accepted inequalities
are exact after the proposal stage.

## Referee Executions

All fresh outputs were written outside the repository.

| Check | Result |
|---|---|
| `verify_target_a_computational_evidence.py` | PASS for `n=24,26,28,30`, including exact optimizer maximum-root isolation |
| Top-level minimality verifier, checkpoint replay disabled | `SMALLEST_COUNTEREXAMPLE_VERIFIED`; strengthened evidence PASS |
| Targeted record/spectral/evidence/minimality tests | `11 passed, 3 subtests passed` |
| Fresh independent spectral audit at `n=24` | PASS; 353,812 states; 353,811 exact exclusions; zero uncertified |
| Fresh-versus-archived `n=24` C record-stream SHA-256 | exact match: `5557d593...e21f1f21` |
| Fresh-versus-archived `n=24` decision SHA-256 | exact match: `bddd4e22...a794b638` |
| Submission artifact verifier | PASS, but does not detect the stale recordwise-limit wording noted above |
| Full `n=30` rerun | not run, as instructed |

## Final Verdict

The requested target **BLOCKER=0, MAJOR=0** is met for the computational proof
core. The former large-order representative-set and per-state decision gaps are
closed by two separate full routes, exact arithmetic, four-order hash-bound PASS
evidence, exact optimizer-edge isolation, and mandatory top-level gate
integration.

The package should not yet be called the final immutable submission snapshot.
Close the two MODERATE archival items above, preserve the disclosed correlated
risk, and rerun the lightweight gates. No additional `n=30` computation is
needed to perform those fixes.
