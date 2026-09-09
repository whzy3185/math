# RESEARCH_STATE

This file is the live control surface for a research campaign. Keep it short enough to read at the start of every continuation turn.

## Project identity

- Project/topic:
- Repository:
- Research branch:
- Base branch / commit:
- Current commit:
- Started:
- Last updated:
- Mathematical domain:
- Target deliverable / publication ambition:
- Campaign mode: `topic discovery | open problem | remark mining | counterexample | strengthening | formalization | publication escalation | paper audit`
- Target journal / level, if any:

## Exact research objective

State the current mathematical objective in 2–5 precise sentences. Include objects, parameter domains, quantifiers, and what would constitute success.

## Strongest current theorem

> Exact current theorem statement.

- Evidence state: `Observed | Verified | Proved | Published/Established`
- Strength level: `L0 | L1 | L2 | L3 | L4 | L5 | L6`
- Human proof:
- Lean theorem/file:
- Independent audit:
- Main unresolved caveat:

## Contribution hierarchy

When publication is intended, rank the contribution conceptually rather than chronologically.

- **C1 structural / inverse theorem:**
- **C2 classification / global consequence:**
- **C3 exact endpoint / spectrum / sharp bound / corollary:**

The abstract, introduction, and cover-letter framing should not reduce C1 to C3 when C1 is the real conceptual advance.

## Publication maturity

- Manuscript version:
- Manuscript maturity: `M0 | M1 | M2 | M3 | M4 | M5 | M6 | M7`
- Computer-assisted proof maturity: `CAP0 | CAP1 | CAP2 | CAP3 | CAP4 | CAP5 | n/a`
- Latest simulated-referee verdict: `not assessed | reject-range | major revision | minor revision | accept-after-revision range`
- Mathematical freeze: `open frontier | provisional freeze | frozen`
- Journal progression file:
- Latest serious referee/audit date:

Do not present a simulated-referee verdict as actual peer review or editorial status.

## Current research frontier

Summarize only what changed recently and what currently blocks the next theorem or maturity upgrade.

- Latest mathematical delta:
- Latest referee-triggered delta:
- Current bottleneck:
- Best strengthening opportunity:
- Main falsification risk:
- Main novelty risk:
- Main proof-package/completeness risk:

## Priority queue

Always keep this ordered. Higher priority dominates lower priority.

| Priority | Task | Why it matters | Expected output | Status |
|---|---|---|---|---|
| P0 |  | correctness blocker | corrected theorem/proof | open |
| P1 |  | falsification | counterexample or strengthened confidence | open |
| P2 |  | novelty/open-status risk | source comparison | open |
| P3 |  | main proof bottleneck | lemma/reduction | open |
| P4 |  | theorem strengthening | stronger theorem or obstruction | open |
| P5 |  | Lean/proof-package completeness | compile/certificate/coverage | open |
| P6 |  | publication/referee escalation | closed referee issues / new version | open |
| P7 |  | render/submission/package | final artifacts | open |

Delete irrelevant empty rows. A continuation turn should normally execute the highest meaningful open row.

## Track dashboard

| Track | Current state | Evidence/files | Next meaningful move |
|---|---|---|---|
| N — literature/novelty |  |  |  |
| X — exact exploration/falsification |  |  |  |
| P — analytic proof |  |  |  |
| S — theorem strengthening |  |  |  |
| F — Lean formalization |  |  |  |
| W — manuscript/artifacts |  |  |  |
| A — independent audit |  |  |  |
| R — simulated-referee/version escalation |  |  |  |

## Proof dependency snapshot

Keep the full DAG in `PROOF_GRAPH.md`; record only the headline chain here.

```text
Main theorem
├── O1 — [status]
├── O2 — [status]
│   ├── O2.1 — [status]
│   └── O2.2 — [status]
└── External E1 — [source/hypothesis status]
```

## Open proof obligations

### O1 —

- Exact statement:
- Needed for:
- Dependencies:
- Current idea:
- Failed routes:
- Boundary/small cases checked:
- Hidden-condition risk:
- Referee issue ID, if applicable:
- Next attack:

## Falsification status

- Strongest theorem tested on:
- Most vulnerable lemma tested on:
- Boundary/degenerate cases:
- Claimed equivalences checked:
- Counterexamples found:
- Independent verifier:
- Exact search completeness statement:

## Computation / proof-package status

- Generator/searcher:
- Independent verifier:
- Arithmetic: `exact | symbolic | floating auxiliary only`
- Search space:
- Mathematical finite-reduction theorem:
- Endpoint/decision principle:
- Canonical representation:
- Coverage equality / completeness check:
- Missing / extra count, if applicable:
- Pruning:
- Seed(s):
- Last successful command:
- Output/log/certificate:
- Code commit:
- Checksums/archive metadata:

## Literature / novelty status

- Original source:
- Strongest direct predecessor:
- Closest already-known family:
- Strongest bounded/computational predecessor:
- Latest audit date:
- Equivalent terminology searched:
- Current conclusion: `open | known | partially known | uncertain`
- What is plausibly new in C1:
- What is plausibly new in C2:
- What is plausibly new in C3:
- Main prior-art collision risk:
- Next source/comparison required:

## Strengthening matrix

| Axis | Current theorem | Proposed upgrade | Status/evidence |
|---|---|---|---|
| Scope/classification |  |  |  |
| Remove hypotheses |  |  |  |
| Sharp constant/order/degree |  |  |  |
| Equality/extremizers |  |  |  |
| Necessary-and-sufficient |  |  |  |
| Algorithmic/finite criterion |  |  |  |
| Stability |  |  |  |
| Unified framework |  |  |  |

Record failed upgrades with explicit obstruction/counterexample instead of deleting them.

## Lean status

- Lean/toolchain version:
- Main file:
- Main theorem:
- Statement aligned with human theorem: yes/no
- Remaining `sorry`/`admit` in dependency cone:
- Custom axioms:
- Last successful build command:
- Last successful commit:
- Current formalization bottleneck:
- Human-proof assumption exposed by Lean, if any:

## Manuscript / simulated-referee status

- Clean manuscript source:
- Submission source, if separate:
- Abstract aligned with C1/C2/C3: yes/no
- Main Results closed: yes/no
- Engineering/work-log headings removed where unnecessary: yes/no
- Mathematical transitions drive section flow: yes/no
- Latest simulated-referee verdict:
- Open major referee issues:
- Open minor referee issues:
- Latest version delta:
- Next proposed version:

## Paper / artifact QC

- Claim ledger current: yes/no
- Literature claims sourced: yes/no
- References resolved: yes/no
- Latest PDF/build command:
- Page-by-page render inspected: yes/no
- Cross-reference semantics checked: yes/no
- Main/supplement responsibility split checked: yes/no
- Known mathematical/expository mismatches:

## Independent audit status

- Audit method(s):
- Last audited commit:
- Claims independently checked:
- Open audit findings:
- External expert/peer-review status:

## Stop / pivot / freeze logic

- Why the campaign should continue:
- What would trigger a pivot:
- What would justify provisional mathematical freeze:
- What would reopen a frozen proof:
- Submission-only tasks remaining after freeze:

## Next executable batch

State one concrete batch that can begin immediately without asking the user to restate context.

- Target:
- Action:
- Expected mathematical/referee evidence:
- Expected maturity delta: `L?→L?`, `M?→M?`, `CAP?→CAP?`
- Files likely to change:
