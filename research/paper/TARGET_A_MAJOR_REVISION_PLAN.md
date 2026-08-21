# Target A Major Revision Plan

Baseline: `d1f219d30d387c4c31a4de57d259e804e862f210`

Immutable evidence snapshot:
`bb3c8aca39a27c76e8b76bbe733b84d0fd1fafc6`

Remote packaging checkpoint:
`d4df8dfdd00493d8051577e4d42ce04cf55bb6df`

Primary manuscript: `research/paper/manuscript_tex_pub/`

Derived Chinese manuscript: `research/paper/manuscript_tex_pub_zh/`

The mathematical scope is frozen at the theorems proved in the canonical V2
manuscript. Experimental work motivates further questions but does not enlarge
any theorem without complete exact closure and an independent review.

| ID | Review comment | Closure and evidence | Status |
|:---|:---|:---|:---|
| R1 | Large-order finite verification lacked independent record-level validation at `n=26,28,30`. | The implementation-language-independent scanner and destructive set audit establish exact record equality at `n=24,26,28,30`. The `n=30` audit consumes all 8,964,800 primary representatives and accounts for all 2,147,483,648 switching classes. The strengthened spectral checker independently certifies every nonoptimizer and is hash-bound into the evidence graph. See `research/reproducibility/target_a_large_order_completeness/summary.json`, `research/review/TARGET_A_FINITE_MINIMALITY_TRUST_MAP.md`, and `research/review/TARGET_A_COMPUTATIONAL_REVIEW.md`. | **CLOSED**. Reviewer Compute: `BLOCKER 0 / MAJOR 0 / MODERATE 0 / MINOR 0`. |
| R2 | Related-work coverage and novelty positioning were too thin. | `TARGET_A_RELATED_WORK_MATRIX.md` assigns a verified contribution to every added reference. `TARGET_A_PUBLIC_CONFLICT_UPDATE.md` records a dated, bounded public search and states the non-priority publication boundary. The introduction and bibliography now position the contribution around the exact period-eight phase and structural mechanism. | **CLOSED**. No direct public conflict was found in the bounded 2026-08-21 search; the manuscript retains the qualified phrase “to the best of our knowledge.” |
| R3 | The manuscript did not adequately explain why `C_n(1,2)` is a useful model problem. | Both introductions now motivate the model through cycle coordinates, overlapping short cycles, Floquet reduction, and the cancellation identity in `A^2`. The discussion is explicitly model-specific and makes no universal-model claim. | **CLOSED**. Reviewer Three and both language reviews found no remaining framing issue. |
| R4 | The manuscript lacked explanatory mathematical figures. | Two black-and-white vector figures explain local flux coordinates and the period-eight target/defect geometry. All English wrappers and the Chinese A4 manuscript were compiled and every rendered page inspected. See `TARGET_A_VISUAL_AUDIT_MAJOR_REVISION.md`. | **CLOSED**. Generic/anonymous/JGT: 35 pages; SIDMA: 37 pages; Chinese: 33 pages; zero overfull boxes and zero visual defects. |
| R5 | Controlled evidence above period 16 would improve the discussion. | `target_a_high_period_exploration.json` covers `p=17,...,24` under an explicit `EXPERIMENTAL NON-THEOREM` boundary. Fresh Burnside counts and direct record equality close `p=17,...,23`; an independent C record audit closes `p=24`. The discussion does not extend Theorem F. | **CLOSED AS NON-THEOREM**. Coverage, exact-count, and status gates pass at every sampled period. |
| R6 | Previous reviews identified terminology, notation, cross-reference, certificate-display, and publication issues. | Both manuscripts were synchronized without changing theorem scope. The English publication gate, Chinese publication gate, reference checks, terminology checks, and artifact checks pass. Author, affiliation, funding, DOI, and archive metadata remain explicitly author-supplied submission fields. | **CLOSED**. Language Reviewer and Chinese Reviewer each report `BLOCKER 0 / MAJOR 0 / MODERATE 0 / MINOR 0`. |
| R7 | Zone folding, finite/infinite Floquet domains, one-way moment logic, classification completeness, and the computer-assisted trust boundary were high-risk interfaces. | Focused invariant and artifact validators recheck each interface. The immutable 35-file submission manifest is reachable on the remote branch and pins the theorem evidence at `bb3c8ac`. | **CLOSED**. Reviewer Three reports `BLOCKER 0 / MAJOR 0 / MODERATE 0 / MINOR 0`; no theorem-scope drift. |

## Final Gates

The following gates define closure and are all required:

1. `python3 -m pytest -q research/scripts`
2. `python3 research/scripts/verify_target_a_minimality_certificate.py`
3. `python3 research/scripts/verify_target_a_computational_evidence.py`
4. `python3 research/scripts/verify_target_a_submission_artifact_manifest.py`
5. `python3 research/scripts/verify_target_a_publication_latex.py`
6. `python3 research/scripts/verify_target_a_chinese_latex.py`
7. `git diff --check`
8. Full-page Poppler render and visual inspection of all five final PDFs
9. Reviewer Compute, Reviewer Three, Language Reviewer, and Chinese Reviewer:
   `BLOCKER=0`, `MAJOR=0`, `MODERATE=0`, `MINOR=0`

All seven revision items are closed. Once the final tracked edits are committed,
pushed, and verified equal to the remote branch tip, the release marker is
`TARGET_A_MAJOR_REVISION_READY`.
