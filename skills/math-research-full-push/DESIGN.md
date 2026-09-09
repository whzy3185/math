# Math Research Full-Push v2 — redesign rationale

Date: 2026-09-09
Branch: `skill/math-research-full-push-20260909`

## Why v1 needed redesign

The first version correctly encoded rigorous research requirements, but it behaved too much like a long sequential checklist. That is not the dominant interaction pattern of this project.

The project is usually operated through short continuation commands such as:

- “继续”
- “继续推进”
- “继续增强”
- “推进 Lean”
- “出结论”
- “完成论文”

The system therefore needs to preserve state and choose the next mathematically valuable action autonomously. It should not require the user to manage phase transitions.

Recent repository work also shows that a serious campaign rarely proceeds linearly. Literature comparison, proof repair, theorem strengthening, exact verification, formalization, and manuscript updates feed back into one another. A proof audit may weaken a theorem; Lean may expose a hidden hypothesis; a literature search may force a pivot; a stronger theorem may require a new novelty audit.

## v2 design target

Turn the skill from a research checklist into a **persistent theorem-research operating system**.

The key abstraction is:

> repository state + theorem frontier + proof DAG + priority queue + evidence ledger

instead of:

> phase 0 → phase 1 → ... → phase 13

## Main changes

### 1. Linear phases replaced by a control loop

Every continuation executes:

1. load real repository state;
2. identify the highest-value unresolved bottleneck;
3. execute a concrete research batch;
4. adversarially audit it;
5. update theorem/evidence state;
6. commit;
7. repeat.

This makes “continue” well-defined.

### 2. Priority scheduler added

Research tasks are ordered by:

- `P0` correctness blockers;
- `P1` fast falsification;
- `P2` novelty/open-status risk;
- `P3` main proof bottleneck;
- `P4` theorem strengthening;
- `P5` Lean/formalization;
- `P6` paper/render/package.

This prevents polishing a paper while the theorem still has an unresolved proof gap or obvious strengthening opportunity.

### 3. Parallel tracks replace artificial stage boundaries

The campaign maintains interacting tracks:

- `N` literature/novelty;
- `X` exact exploration/falsification;
- `P` analytic proof;
- `S` theorem strengthening;
- `F` Lean formalization;
- `W` paper/artifacts;
- `A` independent audit.

The active priority can move between tracks at any time.

### 4. Theorem strengthening is now multi-axis

The old L0–L6 ladder remains as a rough headline scale, but v2 does not require strengthening to be linear.

The agent should independently probe:

- broader scope/classification;
- weaker hypotheses;
- sharper quantitative bounds;
- equality/extremizer structure;
- necessary-and-sufficient criteria;
- algorithmic decision procedures;
- stability;
- unifying frameworks.

This better reflects the way the Remark 3 work evolved from a seed problem into automatic growth, standard form, solvability criteria, counting, and explicit infinite families.

### 5. Remark-mining mode made explicit

A short remark in a paper can be a research seed rather than merely a proof exercise. The skill now asks whether one can:

- derive assumptions automatically;
- remove finite-order/genericity assumptions;
- replace examples with classification;
- obtain an iff criterion;
- generalize to weights/parameters/dimensions;
- characterize canonical decompositions.

### 6. Proof DAG becomes a first-class artifact

`PROOF_GRAPH.md` records every dependency, external theorem, falsification test, failed route, and Lean/paper mapping.

This is designed to prevent a common failure mode in long research chats: a key lemma is informally treated as finished and later disappears inside prose.

### 7. Repository state becomes the source of continuation truth

`RESEARCH_STATE.md` now records:

- exact strongest theorem;
- theorem frontier;
- priority queue;
- track dashboard;
- proof bottleneck;
- strengthening matrix;
- Lean state;
- novelty state;
- next executable batch.

A new session should be able to resume from this file without reconstructing the project from chat history.

### 8. Short user commands have explicit semantics

“Continue” resumes the highest-priority open item.

“Strengthen” moves theorem-strength work forward and falsifies stronger variants first.

“Push Lean” formalizes the highest-leverage missing dependency, rather than blindly translating the manuscript from top to bottom.

“Final theorem” triggers final-theorem gates rather than merely restating the latest conjecture.

“Write the paper” does not automatically freeze a weak theorem if meaningful strengthening remains.

## What remains unchanged

The strict evidence separation remains mandatory:

- `Observed`
- `Verified`
- `Proved`
- `Published/Established`

Likewise, exact computation, open-status verification, independent checking, Lean compilation requirements, claim-source alignment, and PDF/render QC remain part of the research standard.

## Intended usage

For a new campaign:

1. create a research branch and campaign directory;
2. copy the control templates;
3. define the exact seed problem and theorem frontier;
4. populate the initial priority queue;
5. execute the control loop until a stable theorem or justified pivot is reached;
6. only then freeze the paper-level contribution.

For an existing campaign, do not restart. Build `RESEARCH_STATE.md` and `PROOF_GRAPH.md` from the existing branch and continue from the highest-priority unresolved dependency.
