# Target A Full Slow Reproduction

Status: **TARGET_A_FULL_SLOW_REPRODUCTION_PASS**

Component statuses:

- **FULL_FINITE_SEARCH_REGENERATION_PASS**
- **FULL_CERTIFICATE_REPLAY_PASS**
- **FULL_SLOW_REGRESSION_PASS**

The complete slow lane was run from the frozen commit
`c5cadf3ec7e160fc994453907fe83c579dc89646` and tree
`dc08b21bbb5d641e8f525c844b208fe9e1d9d93b` in a detached worktree. The
active repository was never used as an output directory. This document imports
only a compact result and hash manifest; fresh chunks and full logs remain
external to Git.

## 1. What Was Regenerated

The production search was started from external checkpoint directories for
each of `n=24,26,28,30`. It freshly enumerated canonical `Q` bracelets,
evaluated both holonomy states, generated spectral certificates, and wrote new
checkpoint chunks and result manifests. This is a **regeneration**, not a
replay of the committed result files.

| n | Q bracelets | Spectral states | Represented Q vectors | Represented switching classes | Chunks | Seconds | Result |
|---:|---:|---:|---:|---:|---:|---:|---|
| 24 | 176,906 | 353,812 | 8,388,608 | 33,554,432 | 28 | 25.289 | no counterexample |
| 26 | 649,532 | 1,299,064 | 33,554,432 | 134,217,728 | 76 | 117.171 | no counterexample |
| 28 | 2,405,236 | 4,810,472 | 134,217,728 | 536,870,912 | 250 | 414.872 | no counterexample |
| 30 | 8,964,800 | 17,929,600 | 536,870,912 | 2,147,483,648 | 908 | 1542.272 | no counterexample |

The `2^31` switching classes represented at `n=30` are covered through the
proved quotient/completeness mechanism. They are not 2,147,483,648 separate
pytest cases. Every fresh run completed its expected bracelet, spectral-state,
and defect-shell counts, with zero exact fallbacks and zero counterexamples.

## 2. Chain Comparison

The decisive logical fingerprints agree with the committed searches:

| n | Final checkpoint chain SHA-256 | Ordered input/certificate agreement |
|---:|---|---|
| 24 | `2dde869aea5da4f040e67a4fef3e93b5f35f5fb42d75f6d48820439f418c83c1` | PASS |
| 26 | `c515350b8bea840c04448086fbc98523615364c05ca837553c93efb933bc0c4e` | PASS |
| 28 | `7ba200b05590b2a9c0ea1121f25f89ddf1d294d0c043417e69f78f764f6e8ee1` | PASS |
| 30 | `b7fd264eece645eead187424152ae810a9ff940e37ffc5649b5ddf65aa31d59d` | PASS |

The fresh checkpoint-manifest file hashes differ from the historical manifest
file hashes. This is expected: the fresh files record the frozen baseline
commit, fresh timing/run metadata, and newly written chunk metadata. The
comparison therefore requires equality of all mathematical counts, ordered
input hashes, ordered certificate hashes, and final checkpoint-chain hashes.
All those comparisons pass; mismatch count is zero.

## 3. Read-Only Replay

After regeneration, the committed `n=24,26,28,30` checkpoint directories were
replayed without modification. For every order, all 12 replay checks passed:

- chunk count and exhausted generator cursor;
- shell, bracelet, spectral-state, and represented-vector counts;
- ordered input and ordered certificate hashes;
- final checkpoint chain and exact optimizer checks;
- zero exact fallbacks and zero counterexamples.

The replay output SHA-256 is
`bcfcb67f6b1e67f7d7ec36552c99aeebfcd8811a46ef697de7314b4ad2311d57`.

## 4. Default-Skipped Tests

The three default-skipped direct-generator/Burnside audits were explicitly
enabled for `n=26,28,30`. The correct class-qualified pytest selectors produced
`3 passed in 154.54s`.

An earlier selector-only invocation used module-level node IDs and exited with
pytest return code 4 because no tests were selected. The command was corrected
and rerun. This was an operational invocation error, not a test failure or a
mathematical mismatch. The manager was also restarted once; `n=24` safely
resumed from four validated chunks and completed.

## 5. Environment and Commands

The run used Python 3.12.13, NumPy 2.3.5, SymPy 1.14.0, and
macOS-26.5.2-arm64 on an Apple M5. Three independent order-level workers ran
with `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`, `MKL_NUM_THREADS`, and
`VECLIB_MAXIMUM_THREADS` all fixed to 1.

Portable command templates, result-file hashes, committed-file hashes,
manifest hashes, script hashes, timings, memory peaks, and incident records are
stored in `target_a_full_slow_reproduction_summary.json`.

## 6. Scope

This reproduction strengthens confidence in the already certified finite
minimality range. It does not enlarge the theorem beyond the repository's
frozen claim scope. In particular, it does not claim all-period optimality,
finite-size global optimality for arbitrary signings, or any result for periods
above the separately proved bounds.

With the novelty audit complete, stable new theorems recorded, default tests
passing, slow evidence mismatch-free, and claim scope frozen, the project gate
is now **PAPER_PACKAGE_READY**. The next stage is Reviewer Zero, theorem
dependency graph construction, proof compression, and notation normalization.
No manuscript drafting is started by this status change.

`TARGET_A_FULL_SLOW_REPRODUCTION_PASS`
