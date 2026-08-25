# Task 59 Final Submission Audit

## Package inventory

| Artifact | Pages | PDF metadata author |
|---|---:|---|
| Identified main manuscript | 37 | Yicheng Zhao; Jiachen Li |
| Anonymous main manuscript | 37 | Anonymous |
| Identified supplement | 12 | Yicheng Zhao; Jiachen Li |
| Anonymous supplement | 12 | Anonymous |

The title is `When Is the Twisted Signing of an Even Cycle Square Spectrally
Optimal?`. It states the actual scope: classification of when a specified
twisted signing attains the minimum, not determination of every failing
`m_n` or classification of all minimizers.

## Editorial audit

- Main theorem caption: `Classification of the conjectured equality`.
- Truth pattern: present as a compact table immediately in the introduction.
- Introduction contains neither the degree-ten `p_6` display nor the
  15-digit isolating interval.
- Actual cited references: 22, covering the direct predecessor, fixed-graph
  signings, signed cycles, circulants, periodic graph operators, local
  defects, IMS localization, and proof-producing finite classification.
- Exact-`2r`: remark only in the main paper; theorem and proof in supplement.
- Main-source `exact*` occurrences: 51, down from the Task 58 baseline of 107.
- Main-text figures: 3; the revised Figure 2 passed rendered inspection.
- Duplicate labels: 0; undefined references: 0; undefined citations: 0.
- LaTeX warnings, overfull boxes, and underfull boxes: 0 in all four builds.
- Anonymous main and supplement leakage checks: pass.

## Reproducibility audit

- Machine manifest: `research/proofs/task59/submission_manifest.json`.
- Certificate families: 7.
- Digested certificate files: 12.
- Every family records logical role, producers, verifiers, and independence
  boundary.
- One-command entry point:
  `python3 research/scripts/verify_target_a_submission.py --full`.
- Environment: Python 3.11+, CPU only, 8 GiB minimum, 16 GiB recommended.
- Measured full runtime on the final working checkpoint: 446.35 seconds.
- Proof-grade verifiers: 13 passed.
- Focused tamper tests: 121 passed in 112.75 seconds.
- Task 59 package tests: 4 passed.

## Visual audit

Rendered checks covered the title/abstract page, truth-pattern page, revised
Figure 2, Figure 3 and IMS transition, anonymous conclusion/data/appendix
transition, and the supplement's raw-enclosure pages. No overlap, clipping,
unreadable type, black block, or incoherent page break remains.

## Frozen artifacts

- Historical English tree:
  `59e3a8f73a152ef06f994e979b7219a3365efeae`.
- Historical Chinese tree:
  `57ae03fb5b90866f84d0d72b414008678e8f5004`.
- Task 58 manuscript and supplement trees were copied, not edited in place.

## External blockers

- `PENDING_SUBMITTER_DESIGNATION`: the submitting/corresponding-author
  designation has not been supplied.
- `IMMUTABLE_ARCHIVE_PENDING`: archive DOI or equivalent persistent record.

Final verdict: `SUBMISSION_READY_MODULO_SUBMITTER_DESIGNATION_AND_ARCHIVE`.
