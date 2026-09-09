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
- Campaign mode: `topic discovery | open problem | remark mining | counterexample | strengthening | formalization | paper audit`

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

## Current research frontier

Summarize only what changed recently and what currently blocks the next theorem upgrade.

- Latest mathematical delta:
- Current bottleneck:
- Best strengthening opportunity:
- Main falsification risk:
- Main novelty risk:

## Priority queue

Always keep this ordered. `P0` dominates lower priorities.

| Priority | Task | Why it matters | Expected output | Status |
|---|---|---|---|---|
| P0 |  | correctness blocker |  | open |
| P1 |  | falsification |  | open |
| P2 |  | novelty/open-status risk |  | open |
| P3 |  | main proof bottleneck |  | open |
| P4 |  | theorem strengthening |  | open |
| P5 |  | Lean/formalization |  | open |
| P6 |  | paper/render/package |  | open |

Delete empty rows when not relevant. A continuation turn should normally execute the highest meaningful open row.

## Track dashboard

| Track | Current state | Evidence/files | Next meaningful move |
|---|---|---|---|
| N — literature/novelty |  |  |  |
| X — exact exploration/falsification |  |  |  |
| P — analytic proof |  |  |  |
| S — theorem strengthening |  |  |  |
| F — Lean formalization |  |  |  |
| W — paper/artifacts |  |  |  |
| A — independent audit |  |  |  |

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
- Next attack:

## Falsification status

- Strongest theorem tested on:
- Most vulnerable lemma tested on:
- Boundary/degenerate cases:
- Counterexamples found:
- Independent verifier:
- Exact search completeness statement:

## Computation status

- Generator/searcher:
- Independent verifier:
- Arithmetic: `exact | symbolic | floating auxiliary only`
- Search space:
- Pruning:
- Seed(s):
- Last successful command:
- Output/log/certificate:
- Code commit:

## Literature / novelty status

- Original source:
- Strongest nearby published result:
- Latest audit date:
- Equivalent terminology searched:
- Current conclusion: `open | known | partially known | uncertain`
- What is plausibly new:
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

Record failed upgrades with the explicit obstruction/counterexample rather than deleting them.

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

## Paper / artifact status

- Main `.tex`:
- Abstract aligned with theorem: yes/no
- Claim ledger current: yes/no
- Literature claims sourced: yes/no
- References resolved: yes/no
- Latest PDF/build command:
- Page-by-page render inspected: yes/no
- Known mathematical/expository mismatches:

## Independent audit status

- Audit method(s):
- Last audited commit:
- Claims independently checked:
- Open audit findings:
- External expert/peer-review status:

## Stop / pivot logic

- Why the campaign should continue:
- What would trigger a pivot:
- What would justify freezing the theorem for paper finalization:

## Next executable batch

State one concrete batch that can be started immediately without asking the user to restate context.

- Target:
- Action:
- Expected evidence/output:
- Files likely to change:
