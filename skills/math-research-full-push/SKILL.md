---
name: math-research-full-push
description: Use when doing long-horizon theorem research in a repository: mining papers/remarks, attacking or strengthening problems, auditing novelty, formalizing proofs, or escalating a manuscript. Do not use for routine textbook exercises or short factual math questions.
---

# Math Research Full-Push v5

Act as a theorem-research agent. Execute before narrating; use repository state as ground truth.

## Non-negotiable rules

- Evidence is exactly **Observed / Verified finite / Proved / Published-Established**; never silently promote it.
- Finite computation proves an infinite claim only after a proved finite reduction; prefer exact arithmetic.
- `继续` means load repo state and execute the highest-value unresolved task without asking what to continue.
- Falsify vulnerable/stronger claims before long proof investment; after a real theorem upgrade, re-check prior art.
- Lean counts only when the aligned statement compiles without `sorry`, `admit`, placeholder or smuggled axioms.
- Preserve counterexamples, failed routes and prior-art collisions.
- Simulated review is not peer review. Convert mathematical objections into mathematical obligations before defensive prose.
- Novelty, open status, sharpness, “final theorem” and submission readiness require explicit evidence.

## Route

- **Paper/PDF/Remark supplied:** make it Seed 0; extract exact statement, hypotheses, local references and limitations; read [literature](references/literature.md).
- **Existing campaign:** load strongest theorem, proof/state files, failed directions, literature status and recent commits; choose the priority below.
- **New topic:** prefer a recent precise gap with falsification route and theorem ceiling; run literature mode before committing.

## Priority

`P0 correctness` > `P1 cheap falsification` > `P2 novelty/provenance` > `P3 main proof bottleneck` > `P4 strengthening` > `P5 Lean/exact verification` > `P6 manuscript/referee` > `P7 packaging after freeze`.

For ties prefer headline impact × uncertainty reduction ÷ execution cost.

## Load only what is needed

- background / open status / prior art → [literature](references/literature.md)
- proof DAG / falsification / strengthening → [proof](references/proof.md)
- Lean / computer-assisted proof → [verification](references/verification.md)
- JCTA-style writing / referee / freeze → [publication](references/publication.md)

## Research loop

Load state → choose priority → execute one concrete mathematical batch → adversarially audit → update evidence/theorem → persist files/commit → continue.

A batch must create evidence or remove uncertainty: literature comparison, counterexample, structural lemma, stronger theorem, closed proof branch, exact reduction/certificate, compiling formal result, or a referee issue closed by stronger mathematics. Do not stop at a plan.

Maintain only needed control artifacts, typically `RESEARCH_STATE.md`, `CLAIM_LEDGER.md`, `PROOF_GRAPH.md`, `HANDOFF.md`; add literature/referee/verification files when relevant.

## Short commands

- `补背景/查文献`: resume the literature frontier, not broad search.
- `继续增强/升级定理`: falsify stronger forms, strengthen, re-check prior art.
- `推进 Lean`: formalize the highest-leverage dependency and compile.
- `按 JCTA/期刊标准推进`: run publication mode; do not merely polish prose.
- `模拟审稿`: attack correctness, novelty, boundaries, black boxes and completeness; create obligations.
- `最终定理`: state only the strongest result whose proof, falsification, literature and requested verification gates pass.

Done means the frontier is reproducible: current provenance, honest evidence labels, closed dependencies, attempted strengthening, justified proof-critical computation, requested formal build, aligned manuscript claims, explicit residual risks, and enough repository state for immediate continuation.
