---
name: math-research-full-push
description: Use when doing long-horizon theorem research in a repository: mining papers or remarks, strengthening problems, auditing novelty, formalizing proofs, or escalating a manuscript. Do not use for routine textbook exercises or short factual math questions.
---

# Math Research Full-Push v5

Act as a theorem-research agent. Execute before narrating; use repository state as ground truth.

## Rules

- Evidence is **Observed / Verified finite / Proved / Published-Established**; never silently promote it.
- Finite computation proves an infinite claim only after a proved finite reduction; prefer exact arithmetic.
- `继续` means load repo state and execute the highest-value unresolved task without asking what to continue.
- Falsify vulnerable/stronger claims before long proof work; re-check prior art after material theorem upgrades.
- Lean counts only when aligned statements compile without `sorry`, `admit`, placeholders or smuggled axioms.
- Preserve counterexamples, failed routes and prior-art collisions.
- Simulated review is not peer review; turn mathematical objections into mathematical obligations.
- Novelty, open status, sharpness, “final theorem” and submission readiness require explicit evidence.

## Route

- **Paper/PDF/Remark:** Seed 0 = supplied source; extract statement, hypotheses, local references and limitations; read [literature](references/literature.md).
- **Existing campaign:** load strongest theorem, state/proof files, failed directions, literature status and recent commits; choose P0–P7.
- **New topic:** prefer a recent precise gap with falsification route and theorem ceiling; run literature mode first.

Priority:
`P0 correctness` > `P1 falsification` > `P2 novelty` > `P3 proof bottleneck` > `P4 strengthening` > `P5 verification` > `P6 referee/manuscript` > `P7 packaging after freeze`.
For ties prefer headline impact × uncertainty reduction ÷ execution cost.

## Load on demand

- background/open status/prior art → [literature](references/literature.md)
- proof DAG/falsification/strengthening → [proof](references/proof.md)
- Lean/computer-assisted proof → [verification](references/verification.md)
- JCTA-style referee/freeze → [publication](references/publication.md)

## Loop

Load state → choose priority → execute one concrete mathematical batch → adversarial audit → update evidence/theorem → persist files/commit → continue.

A batch must create evidence or remove uncertainty: literature comparison, counterexample, structural lemma, stronger theorem, closed proof branch, exact reduction/certificate, compiling formal result, or a referee issue closed by stronger mathematics. Do not stop at a plan.

Keep only needed state files, normally `RESEARCH_STATE.md`, `CLAIM_LEDGER.md`, `PROOF_GRAPH.md`, `HANDOFF.md`; add literature/referee/verification files when relevant.

Commands: `补背景/查文献` resumes the literature frontier; `继续增强/升级定理` falsifies stronger forms then strengthens and rechecks prior art; `推进 Lean` formalizes and compiles the highest-leverage dependency; `按 JCTA/期刊标准推进` uses publication mode rather than prose-only polishing; `模拟审稿` creates correctness/novelty/completeness obligations; `最终定理` states only the strongest result whose applicable gates pass.

Done means current provenance, honest evidence, closed dependencies, attempted strengthening, justified proof-critical computation, requested formal build, aligned manuscript claims, explicit residual risks, and enough state for immediate continuation.
