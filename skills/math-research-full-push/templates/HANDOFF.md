# HANDOFF

This is the compact continuation packet for a new session or researcher. It should make a short command such as “继续” executable without reconstructing the project from chat history.

## Repository state

- Repository:
- Branch:
- Base branch / commit:
- Current commit:
- Campaign directory:
- Last updated:

## Research goal

State the exact mathematical problem and intended strongest deliverable.

## Strongest current theorem

> Exact theorem statement.

- Evidence state: `Observed | Verified | Proved | Published/Established`
- Strength level: `L0 | L1 | L2 | L3 | L4 | L5 | L6`
- Human proof:
- Lean proof:
- Independent audit:
- Main caveat:

## Contribution hierarchy

- **C1 structural / inverse theorem:**
- **C2 classification / global consequence:**
- **C3 exact endpoint / spectrum / sharp bound / corollary:**

## Publication state

- Target journal / level:
- Current manuscript version:
- Manuscript maturity: `M0 | M1 | M2 | M3 | M4 | M5 | M6 | M7`
- Computer-assisted proof maturity: `CAP0 | CAP1 | CAP2 | CAP3 | CAP4 | CAP5 | n/a`
- Latest simulated-referee verdict:
- Mathematical freeze: `open frontier | provisional freeze | frozen`
- Journal progression file:

Do not describe simulated review as actual peer review/editorial status.

## Current theorem frontier

- What changed most recently:
- Latest referee-triggered mathematical change:
- Current proof bottleneck:
- Best strengthening opportunity:
- Main falsification risk:
- Main novelty risk:
- Main computation/completeness risk:

## Highest-priority continuation queue

1. `[P0 correctness]`
2. `[P1 falsification]`
3. `[P2 novelty]`
4. `[P3 proof]`
5. `[P4 strengthening]`
6. `[P5 Lean/proof-package]`
7. `[P6 publication/referee]`
8. `[P7 submission/QC]`

Omit irrelevant priorities. The next session should normally start with the highest meaningful open item.

## What is complete

### Literature / provenance

-

### Exact computation / verification

-

### Analytic proof

-

### Theorem strengthening

-

### Lean

-

### Manuscript / simulated referee

-

### Proof-critical supplement

-

### Independent audit

-

## What is not complete

List only real remaining gaps.

1.
2.
3.

## Critical proof obligations

### O1 —

- Exact statement:
- Needed for:
- Dependencies:
- Current attack:
- Failed routes:
- Small/boundary cases checked:
- Referee issue ID, if any:
- Relevant files:
- Lean mapping:

## Open referee issues

| ID | Severity | Type | Exact objection | Mathematical obligation | Target version |
|---|---|---|---|---|---|
| R001 |  |  |  |  |  |

## Known false directions / counterexamples

Do not repeat these without a genuinely new idea.

-

## Strengthening opportunities

- broader scope/classification:
- remove hypotheses:
- sharpen bound/order/degree:
- equality/extremizers:
- necessary-and-sufficient criterion:
- algorithmic/finite criterion:
- stability:
- unifying framework:

## Proof-package completeness

- proved finite-reduction theorem:
- exact endpoint/decision principle:
- canonical representation:
- generator:
- independent verifier:
- coverage equality / completeness:
- exact arithmetic:
- missing/extra count:
- deterministic commands:
- hashes/archive metadata:

## Reproducibility commands

```bash
# exact experiment / independent verifier

# Lean build

# LaTeX/PDF build
```

## Literature / novelty conclusion

- Last audit date:
- Current open-status conclusion:
- Strongest direct predecessor:
- Closest already-known family:
- Strongest bounded/computational predecessor:
- What is plausibly new in C1:
- What is plausibly new in C2:
- What is plausibly new in C3:
- Main prior-art collision risk:
- Next source/comparison still needed:

## Files to read first

1. `RESEARCH_STATE.md`
2. `CLAIM_LEDGER.md`
3. `PROOF_GRAPH.md`
4. `JOURNAL_PROGRESSION.md` if publication mode is active
5. main proof / theorem source
6. latest audit / verification report

## Next executable batch

Describe a batch that can start immediately.

- Target:
- Concrete action:
- Expected mathematical/referee evidence:
- Expected maturity delta: `L?→L?`, `M?→M?`, `CAP?→CAP?`
- Files likely to change:

## Continuation semantics

If the next user message is only “继续” or “继续推进”:

1. read state, proof graph, and journal progression if present;
2. execute the highest-priority unresolved task;
3. falsify/audit the result;
4. update repository state and relevant manuscript version records;
5. report the theorem-level/maturity delta.

If the user says “按 JCTA 方式推进” or equivalent:

1. compile/read the current manuscript as a skeptical target-journal referee;
2. record a simulated verdict;
3. convert serious mathematical objections into proof/referee obligations;
4. resolve correctness before exposition;
5. prefer theorem/reduction/completeness upgrades over defensive prose;
6. create the next meaningful version only after a real delta.

Do not ask the user to restate the research goal unless repository state is genuinely insufficient to identify any useful next action.

## Non-negotiable evidence rules

- Preserve `Observed / Verified / Proved / Published/Established` distinctions.
- Finite computation is not an infinite proof without a proved finite reduction.
- “Smallest counterexample” requires completeness of preceding cases.
- A proof-critical certificate table needs completeness/coverage, not only valid rows.
- Lean is complete only when the claimed dependency cone compiles without proof gaps or smuggled axioms.
- Recheck novelty after material theorem strengthening.
- If a lemma fails, downgrade every dependent claim immediately.
- Keep abstract/introduction/body/Lean/supplement synchronized with the strongest audited theorem.
- A sufficient certificate bound is not “optimal” unless optimality is proved.
- Local author-side or simulated-referee checking is not external peer review.
