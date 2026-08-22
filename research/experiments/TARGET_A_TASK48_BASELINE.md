# Target A Task 48 Baseline

## Immutable starting point

- Branch: `agent/target-a-discovery-snapshot`
- Local and remote HEAD: `981499eceb6e34461c7b6c4d703d677c27674e19`
- Ahead/behind at entry: `0/0`
- Previous manuscript baseline: `9d75ce04fd4509034ef65db50177d236f13479ab`
- Immutable theorem-evidence snapshot: `bb3c8aca39a27c76e8b76bbe733b84d0fd1fafc6`
- Task 47 status: `TARGET_A_TASK47_EXPERIMENTS_COMPLETE`
- Working tree at entry: clean

## Runtime

- Architecture: `arm64`
- System Python: `3.9.6`
- Experiment runtime: bundled Codex Python
- Compiler: `Apple clang 21.0.0`
- Numerical libraries are recorded again in each generated summary.

## Entry verification

- Full script tests: `275 passed, 3 skipped, 20 subtests passed`
- Task 47 verifier: `TARGET_A_TASK47_VERIFICATION_PASS`
- Minimality verifier: `TARGET_A_MINIMALITY_CERTIFICATE_PASS`
- Computational-evidence verifier: `TARGET_A_COMPUTATIONAL_EVIDENCE_PASS`
- Submission artifact verifier: `TARGET_A_SUBMISSION_ARTIFACT_MANIFEST_PASS`

## Freeze rule

Task 48 is discovery, structural experimentation, exact certification, and
proof preparation only.  The following directories are frozen relative to
the Task 48 entry commit:

- `research/paper/manuscript_tex_pub/`
- `research/paper/manuscript_tex_pub_zh/`

No theorem statement or formal manuscript file may change in this task.
