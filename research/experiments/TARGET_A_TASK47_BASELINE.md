# Target A Task 47 Baseline

Date: 2026-08-22

Task: Structure-Directed Supplementary Experiments

## Repository State

- branch: `agent/target-a-discovery-snapshot`
- baseline commit: `9d75ce04fd4509034ef65db50177d236f13479ab`
- immutable theorem-evidence snapshot:
  `bb3c8aca39a27c76e8b76bbe733b84d0fd1fafc6`
- initial working tree: clean
- theorem status: `TARGET_A_MAJOR_REVISION_READY`
- theorem scope changed by Task 47: **NO**
- formal manuscript changed by Task 47: **NO**

Task 47 is an experiment, discovery, and validation layer. Its outputs cannot
be cited as theorem statements unless a later task supplies a separate exact
proof, review, and manuscript decision.

## Runtime

- operating system: macOS 26.5.2 (build 25F84)
- architecture: arm64
- CPU: Apple M5
- Python: CPython 3.12.13
- NumPy: 2.3.5
- SymPy: 1.14.0
- C compiler: Apple clang 21.0.0 (`clang-2100.1.1.101`)

The Python executable used for recorded runs is the bundled Codex workspace
runtime at
`/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.

## Baseline Verification

The baseline runs the complete `research/scripts` test package and the current
Target A verification gates. Existing large-order checkpoint generation and
the order-30 full-space scan are not regenerated because Task 47 does not
depend on replacing their immutable evidence. The new order-22 audit is run
separately in Phase E.

Commands:

```text
python3 -m pytest -q research/scripts
python3 research/scripts/verify_target_a_minimality_certificate.py
python3 research/scripts/verify_target_a_computational_evidence.py
python3 research/scripts/verify_target_a_submission_artifact_manifest.py
```

The exact test count and gate markers are recorded in the Task 47 synthesis
after all new scripts and tests have been added.

Baseline result before Task 47 additions:

```text
268 passed, 3 skipped, 20 subtests passed
TARGET_A_MINIMALITY_CERTIFICATE_PASS
TARGET_A_COMPUTATIONAL_EVIDENCE_PASS
TARGET_A_SUBMISSION_ARTIFACT_MANIFEST_PASS
```
