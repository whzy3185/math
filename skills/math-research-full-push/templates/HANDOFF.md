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

State the exact mathematical problem and the intended strongest deliverable.

## Strongest current theorem

> Exact theorem statement.

- Evidence state: `Observed | Verified | Proved | Published/Established`
- Strength level: `L0 | L1 | L2 | L3 | L4 | L5 | L6`
- Human proof:
- Lean proof:
- Independent audit:
- Main caveat:

## Current theorem frontier

- What changed most recently:
- Current proof bottleneck:
- Best strengthening opportunity:
- Main falsification risk:
- Main novelty risk:

## Highest-priority continuation queue

1. `[P0 correctness]`
2. `[P1 falsification]`
3. `[P2 novelty]`
4. `[P3 proof]`
5. `[P4 strengthening]`
6. `[P5 Lean]`
7. `[P6 paper/QC]`

Omit irrelevant empty priorities. The next session should normally start with the highest meaningful open item.

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

### Paper / artifacts

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
- Relevant files:
- Lean mapping:

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

## Reproducibility commands

```bash
# exact experiment / independent verifier

# Lean build

# LaTeX/PDF build
```

## Literature / novelty conclusion

- Last audit date:
- Current open-status conclusion:
- Strongest nearby published result:
- What is plausibly new:
- Main prior-art collision risk:
- Next source/comparison still needed:

## Files to read first

1. `RESEARCH_STATE.md`
2. `CLAIM_LEDGER.md`
3. `PROOF_GRAPH.md`
4. main proof / theorem source
5. latest audit or verification report

## Next executable batch

Describe a batch that can start immediately.

- Target:
- Concrete action:
- Expected evidence/output:
- Files likely to change:

## Continuation semantics

If the next user message is only “继续” or “继续推进”:

1. read the current state and proof graph;
2. execute the highest-priority unresolved task;
3. falsify/audit the new result;
4. update repository state;
5. report the theorem-level delta.

Do not ask the user to restate the research goal unless repository state is genuinely insufficient to identify any useful next action.

## Non-negotiable evidence rules

- Preserve `Observed / Verified / Proved / Published/Established` distinctions.
- Finite computation is not an infinite proof without a proved finite reduction.
- “Smallest counterexample” requires search completeness for all preceding cases.
- Lean is complete only when the claimed dependency cone compiles without proof gaps or smuggled axioms.
- Recheck novelty after any material theorem strengthening.
- If a lemma fails, downgrade every dependent claim immediately.
- Keep abstract/introduction/paper claims synchronized with the strongest audited theorem.
- Local author-side checking is not external peer review.
