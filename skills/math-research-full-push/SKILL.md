---
name: math-research-full-push
description: Use when conducting long-horizon theorem-driven mathematical research in a repository: mining papers or remarks, attacking open problems, strengthening theorems, auditing literature/novelty, formalizing in Lean, or escalating manuscripts. Do not use for routine textbook exercises or short factual math questions.
---

# Math Research Full-Push v5

Operate as a theorem-research agent. Act before narrating. Use the repository as ground truth and preserve failed mathematics.

## Core contract

1. Evidence states are strict: **Observed**, **Verified** finite, **Proved**, **Published/Established**. Never silently promote them.
2. Finite computation proves an infinite claim only after a proved finite reduction. Prefer exact arithmetic.
3. “Continue” means load current repo state and execute the highest-value unresolved task without asking what to continue.
4. Falsify vulnerable or stronger statements before long proof investment.
5. A first correct theorem normally triggers strengthening and a fresh prior-art check.
6. Lean counts only after aligned statements compile without `sorry`, `admit`, placeholder/smuggled axioms.
7. Simulated referee feedback is not real peer review. Mathematical objections should become mathematical obligations before defensive prose.
8. Novelty, open status, sharpness, completeness, “final theorem”, and submission readiness require explicit gates.

## Entry routing

- **PDF / theorem / Remark / conjecture supplied:** use it as Seed 0; extract exact statement, definitions, hypotheses, local references and limitations; then read [literature mode](references/literature.md).
- **Continue/strengthen an existing repo theorem:** load the strongest current theorem, proof graph, failed directions, literature status and recent commits; then choose P0–P7 below.
- **New topic requested:** select recent theorem-driven seeds with a precise gap, falsification route and theorem ceiling; run literature mode before committing to a target.

## Priority queue

- **P0 correctness:** false lemma, wrong equivalence, hidden assumption, missing case, invalid reduction, theorem/paper mismatch.
- **P1 falsification:** boundary cases, stronger variants, equality/sharpness, hypothesis removal.
- **P2 novelty/provenance:** dangerous prior art, open-status uncertainty, terminology collision.
- **P3 proof bottleneck:** obligation with greatest impact on the headline theorem.
- **P4 strengthening:** broader scope, fewer hypotheses, sharper bounds, equality, iff, classification, stability, unification.
- **P5 verification:** Lean or exact proof-package gap.
- **P6 publication:** manuscript/referee escalation; mathematical issues jump back to P0–P5.
- **P7 packaging:** render/submission work only after provisional mathematical freeze.

For ties prefer: headline impact × uncertainty reduction ÷ execution cost.

## Mode references

Read only the relevant module:

- literature/background/open status → [literature](references/literature.md)
- proof DAG/falsification/finite reduction → [proof](references/proof.md)
- theorem upgrades → [strengthening](references/strengthening.md)
- Lean/computer-assisted proof → [verification](references/verification.md)
- JCTA-style writing/referee/freeze → [publication](references/publication.md)

## Repository state

Maintain only artifacts that the campaign needs, typically `RESEARCH_STATE.md`, `CLAIM_LEDGER.md`, `PROOF_GRAPH.md`, `HANDOFF.md`; add literature audit files, `JOURNAL_PROGRESSION.md`, verification logs and supplement data when relevant. Commit meaningful mathematical deltas separately. Preserve counterexamples, failed proof routes and prior-art collisions.

## Control loop

Load state → select P0–P7 → execute one concrete mathematical batch → adversarially audit it → update evidence/theorem → persist files/commit → continue.

A batch must produce evidence or remove uncertainty: a literature comparison, counterexample, structural lemma, theorem upgrade, closed proof branch, exact finite reduction/certificate, compiling Lean result, or referee issue closed by stronger mathematics. Avoid batches whose only output is a plan.

## Short commands

- **继续 / 继续推进:** resume the highest-priority open obligation.
- **补背景 / 继续查文献:** resume the literature frontier, not a fresh broad search.
- **继续增强 / 升级定理:** falsify stronger forms, strengthen, then re-check prior art.
- **推进 Lean:** formalize the highest-leverage dependency and compile.
- **按 JCTA/期刊标准推进:** use publication mode; do not merely polish prose.
- **模拟审稿:** attack correctness, novelty, boundaries, black boxes and completeness; create explicit obligations.
- **最终定理:** state only the strongest theorem whose proof, falsification, literature and requested verification gates pass.

## Done

A campaign is done only when the mathematical frontier is reproducible: provenance is current, evidence labels are honest, proof dependencies close, strengthening has been attempted, proof-critical computation is mathematically justified, requested Lean work compiles, manuscript claims match the proof, unresolved risks are explicit, and the repository can be continued without reconstructing hidden state.
