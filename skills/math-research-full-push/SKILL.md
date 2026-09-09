---
name: math-research-full-push
description: End-to-end rigorous mathematical research workflow for graph theory, combinatorics, discrete mathematics, algebraic combinatorics, matrix/polynomial problems, and related theorem-driven projects. Use for topic selection, open-status verification, exact computation, counterexample search, analytic proof, theorem strengthening, Lean formalization, paper construction, and independent audit.
---

# Math Research Full-Push

## Mission

Turn a mathematical research prompt into a reproducible research program that aims for a genuinely new, publication-grade theorem rather than a plausible-looking draft.

The default loop is:

> literature verification → problem formalization → baseline reproduction → exact exploration → structural conjecture → analytic proof → theorem strengthening → Lean formalization → independent audit → paper construction → render/QC → handoff

The workflow is intentionally adversarial: every important claim must survive attempts to falsify it, weaken it, locate prior art, and break the proof.

## When to use

Use this skill when the task includes one or more of:

- selecting a research problem in graph theory, combinatorics, discrete mathematics, algebraic combinatorics, matrix theory, polynomial theory, finite structures, or nearby areas;
- checking whether a conjecture/open problem is still open;
- proving a remark, lemma, special case, classification, extremal bound, or structural theorem;
- searching for a counterexample or extremal construction;
- upgrading a weak result into a stronger theorem;
- combining symbolic/exact computation with proof;
- producing Lean formalization alongside a human-readable proof;
- building a paper-quality LaTeX manuscript and validating the rendered PDF;
- auditing an existing proof or research branch.

Do not use this workflow to merely paraphrase existing literature. The goal is a traceable chain from sources and experiments to claims and proofs.

## Core epistemic contract

Every mathematical statement that matters must carry one of exactly four evidence states:

1. **Observed** — suggested by exploratory computation, numerical data, examples, or informal reasoning.
2. **Verified** — checked exactly for explicitly stated finite instances or parameter ranges.
3. **Proved** — established by a complete mathematical argument valid for the stated generality.
4. **Published/Established** — supported by a reliable public source that actually proves the stated claim.

Never silently promote a claim upward. In particular:

- finite computation is not a proof of an infinite statement;
- floating-point evidence is not an exact certificate;
- a Lean file containing `sorry`, `admit`, axioms added for convenience, or an uncompiled theorem is not a formal proof;
- a search result or abstract saying a topic is “open” is not enough to certify present-day open status;
- a plausible derivation is not a proof until all cases, domains, sign conditions, and edge cases are closed.

## Repository and branch discipline

For every independent research campaign:

1. Work on a dedicated Git branch.
2. Record the base branch/commit in the research state file.
3. Keep research artifacts under a coherent project directory rather than scattering files.
4. Commit logically separable milestones: literature audit, exact verifier, proof lemma, Lean theorem, paper update, audit.
5. Never overwrite evidence from a failed direction; archive it with the failure reason.

Recommended project layout:

```text
research/
  README.md
  RESEARCH_LOG.md
  CONJECTURE_REGISTRY.md
  literature/
  candidates/
  conjectures/
  experiments/
  counterexamples/
  proofs/
  lean/
  scripts/
  logs/
  paper/
  audit/
```

If the repository already has an established layout, preserve it and map these responsibilities onto the existing structure.

## Required control files

At minimum maintain:

- `RESEARCH_STATE.md` — current theorem target, evidence status, blockers, branch/commit, verified commands, next proof obligations;
- `CLAIM_LEDGER.md` — every paper-level claim with evidence state, proof/source location, dependencies, and audit status;
- `HANDOFF.md` — compact continuation packet for a new session or researcher;
- chronological research log — what changed, what failed, what remains.

Templates live beside this skill.

# Execution protocol

## Phase 0 — Define the research contract

Convert the user's request into a precise research objective before proving anything.

Record:

- mathematical domain;
- target object/class;
- exact desired output: counterexample, classification, inequality, extremal theorem, algorithm, formalization, etc.;
- whether novelty is required;
- expected level of theorem strength;
- whether Lean and/or a paper is required;
- constraints on repository and branch.

If the prompt is broad, do not stall on clarification unless the missing information blocks all useful work. Choose a defensible scope and document the assumption.

## Phase 1 — Literature and open-status audit

For claims of novelty or open status, use fresh literature search.

Search in layers:

1. original source of the conjecture/problem;
2. journal version and arXiv revisions;
3. citing papers and later papers by the same authors;
4. recent papers using equivalent terminology;
5. surveys, MathSciNet/zbMATH-style metadata when available, and authoritative bibliographies;
6. keyword variants induced by equivalent definitions.

Create a claim-source map. For each source record:

- bibliographic identifier and date;
- exact theorem/conjecture number if available;
- what it establishes;
- what it does **not** establish;
- relation to the proposed target;
- whether the source is primary or secondary.

A problem may be labeled “currently open” only after this audit. If status remains uncertain, say so explicitly.

### Novelty gate

Before investing deeply in a proof, answer:

- Is the exact statement already known?
- Is a stronger theorem known under different notation?
- Is the proposed proof technique already standard for this statement?
- Would the result still be interesting if the strongest nearby literature is included?

If the answer is unfavorable, pivot early.

## Phase 2 — Candidate ranking

When several problems are possible, score them rather than choosing by intuition alone.

Recommended dimensions, each 0–5:

- novelty confidence;
- tractability within available tools/time;
- theorem-strength ceiling;
- access to exact finite experiments;
- structural richness;
- formalizability in Lean;
- publication relevance;
- dependence on unavailable heavy machinery.

Prefer targets that combine a credible novelty gap with a route to exact verification and structural proof.

## Phase 3 — Formalize the statement before attacking it

Write a specification containing:

- all objects and parameter domains;
- normalization conventions;
- equivalent formulations;
- degenerate/boundary cases;
- exact quantifier order;
- what constitutes a counterexample;
- what constitutes equality/extremality;
- the intended Lean statement, even if Lean work comes later.

Ambiguous natural-language claims must not enter the proof pipeline.

## Phase 4 — Reproduce the baseline

Before extending or refuting a published result, reproduce the smallest nontrivial instances of the published setup.

Requirements:

- match definitions exactly;
- use exact arithmetic whenever possible;
- save input, output, environment, command, and code commit;
- test published examples and special cases;
- independently compute at least one invariant or quantity by a second method when feasible.

If baseline reproduction fails, do not proceed as if the new theorem were trustworthy. Resolve the discrepancy first.

## Phase 5 — Exact exploration and falsification

Computation is a conjecture generator and falsification engine.

Use it to:

- enumerate small cases;
- test boundary parameters;
- search for minimal counterexamples;
- identify equality cases;
- detect invariant patterns;
- compare alternative conjectured bounds;
- test proof lemmas before spending time proving them.

### Computation rules

- Prefer integers, rationals, finite fields, symbolic algebra, or certified combinatorial enumeration.
- If floating point is unavoidable, separate it from exact verification and state tolerances.
- Record random seeds.
- Record the complete search space and pruning rules.
- For a “smallest counterexample” claim, prove completeness of the preceding search range or weaken the wording to “smallest found in the stated search range.”
- Build a verifier independent of the generator/searcher when the result is important.

## Phase 6 — Convert patterns into structural lemmas

Do not jump directly from data to a grand theorem. Extract the mechanism.

Typical questions:

- What invariant is actually controlling the phenomenon?
- Can a minimal counterexample be reduced?
- Is there a deletion/contraction, exchange, compression, shifting, switching, symmetrization, or local-improvement move?
- Does extremality force regularity, transitivity, saturation, laminarity, convexity, or a forbidden local pattern?
- Can the object be encoded as a matrix, polynomial, generating function, flow, orientation, poset, or auxiliary graph?
- Are there monotone parameters that permit induction?
- Can equality be characterized simultaneously with the inequality?

Record each lemma as an independent proof obligation and note which later theorem depends on it.

## Phase 7 — Analytic proof campaign

For each target theorem maintain a proof dependency graph.

A valid proof draft must make explicit:

- hypotheses used at each step;
- all case splits;
- sign/nonzero/domain conditions;
- base cases and induction measure;
- why reductions preserve the required property;
- why equality cases are exhaustive;
- where an external theorem is invoked and its exact hypotheses.

### Adversarial proof checks

Before marking **Proved**, attempt to break the proof by:

1. testing the theorem and each lemma on exhaustive small cases;
2. testing boundary and degenerate cases;
3. reversing each implication to ensure no hidden biconditional was assumed;
4. checking quantifier order;
5. checking that a chosen extremal/minimal object exists;
6. checking that every recursive/reduction step terminates;
7. searching for a counterexample to each intermediate lemma, not just the final theorem;
8. rewriting the core argument independently from scratch.

If a gap is found, downgrade the claim immediately.

## Phase 8 — Theorem strengthening loop

A first theorem is usually not the final theorem. After obtaining a proof, deliberately try to strengthen it.

Use the following ladder:

- **L0**: observed phenomenon;
- **L1**: exact finite verification;
- **L2**: structural lemma or mechanism;
- **L3**: theorem for a restricted family/special case;
- **L4**: infinite family, broad class, or classification theorem;
- **L5**: sharp/optimal quantitative theorem, equality characterization, necessary-and-sufficient condition, or stability result;
- **L6**: generalized framework that subsumes multiple known/special cases.

For each strengthening attempt ask:

- Can a hypothesis be removed?
- Can a constant be improved to sharp?
- Can equality cases be classified?
- Can a finite statement become an infinite family?
- Can a case proof become a structural classification?
- Can a construction be parametrized?
- Can the result be made algorithmic or stability-type?
- Can two lemmas be unified under a stronger invariant?

Stop strengthening only when the next level is false, clearly prior art, or requires machinery disproportionate to the project. Record the obstruction.

## Phase 9 — Lean formalization

Lean is an independent proof channel, not decoration.

Formalize in this order:

1. core definitions and domains;
2. small helper lemmas;
3. structural lemmas;
4. main theorem;
5. corollaries/equality cases.

Rules:

- Keep the Lean theorem statement visibly aligned with the human theorem.
- Avoid encoding the desired conclusion as an assumption or custom axiom.
- No `sorry`, `admit`, placeholder axioms, or unverified generated code in a claimed-complete proof.
- Compile the relevant target with the repository's actual Lean/lake environment.
- Save the exact build command and successful commit SHA.
- If the human proof uses a theorem absent from mathlib, isolate it as an explicit formalization obligation rather than smuggling it in.

A theorem becomes **Lean-verified** only after successful compilation with no proof gaps.

### Lean/human cross-audit

Use mismatches productively:

- if Lean needs an extra hypothesis, inspect the human proof for a hidden assumption;
- if the human proof is dramatically shorter, check whether Lean definitions are overcomplicated;
- if Lean proves a stronger statement automatically, test whether the paper theorem can be upgraded.

## Phase 10 — Independent audit

Before paper finalization, perform a second-pass audit that does not simply reread the original argument.

Audit channels:

- independent exact computation;
- separate proof derivation;
- dependency graph review;
- literature novelty recheck;
- Lean build from clean state;
- theorem-to-paper consistency check.

The audit report must list:

- claims checked;
- methods used;
- failures or unresolved assumptions;
- whether evidence status changed;
- exact files/commits audited.

## Phase 11 — Paper construction

Build the paper around the strongest theorem, not around the chronology of discovery.

Recommended structure:

1. title and abstract stating the strongest exact contribution;
2. introduction: problem, literature gap, contributions;
3. definitions/preliminaries;
4. main theorem(s);
5. structural lemmas and proof;
6. sharpness/equality/classification/counterexamples;
7. computational or formal verification section if it materially supports the contribution;
8. discussion/generalization/open directions;
9. references;
10. optional appendix with exhaustive certificates or Lean correspondence.

Maintain a claim-source/proof ledger during writing. Every sentence asserting priority, known bounds, or previous results must have a source. Every mathematical headline in the abstract/introduction must map to a theorem proved in the body.

### Paper quality gate

Reject the manuscript as not ready if any of the following holds:

- abstract claims exceed the proved theorem;
- theorem hypotheses differ between abstract/introduction/body;
- a computational observation is phrased as a theorem;
- citations do not support the exact sentence;
- a proof uses an unproved lemma;
- notation changes silently;
- Lean formalization proves a different statement;
- PDF rendering contains broken equations, references, figures, bibliography, or overflow that changes readability.

## Phase 12 — Render and artifact QC

When producing LaTeX/PDF:

- compile from a clean-enough state using the repository's documented toolchain;
- resolve fatal errors and inspect warnings that may affect correctness;
- verify theorem/lemma numbering and cross-references;
- verify bibliography and citation resolution;
- inspect the rendered PDF page-by-page for clipped equations, bad line breaks, missing symbols, blank pages, and figure/table overflow;
- ensure the final downloadable `.tex`/`.pdf` corresponds to the audited commit.

Rendering success is not mathematical correctness; mathematical and presentation audits are separate gates.

## Phase 13 — Handoff and continuation

At the end of any substantial session update `HANDOFF.md` so another session can continue without reconstructing the project from chat history.

The handoff must contain:

- repository and branch;
- current commit if known;
- strongest theorem and exact evidence status;
- completed proof lemmas;
- unresolved proof obligations;
- exact Lean status/build command;
- latest experiment/verifier status;
- novelty/open-status conclusion and date of audit;
- paper status;
- next 3–7 concrete actions, ordered by leverage.

# Decision rules

## When to pivot

Pivot away from a target when:

- literature shows the result is already known or subsumed;
- exact computation produces a decisive counterexample to the intended theorem and no meaningful corrected theorem emerges;
- the theorem-strength ceiling is too low for the stated publication goal;
- the proof depends on a missing ingredient with no plausible route;
- formalization exposes a fundamental ambiguity or false hidden assumption.

A pivot is a research result. Record why it happened.

## When to claim a final theorem

Use “final theorem” only when:

1. the analytic proof is complete;
2. counterexample/falsification checks have been run at meaningful small scales;
3. literature novelty has been rechecked after the theorem reached its final form;
4. all paper-level dependencies are closed;
5. any requested Lean proof compiles;
6. an independent audit has not found an unresolved gap.

If one gate is missing, report the strongest current theorem and the missing gate instead.

# Interaction style

When operating this skill in an interactive research session:

- prefer doing the next high-value research step over repeatedly asking what to do next;
- expose partial findings as soon as they materially change the direction;
- distinguish facts from conjectures and proof ideas;
- keep branch/file locations explicit;
- do not promise background/asynchronous work;
- if the task is too large for one pass, leave a precise handoff with executable next steps rather than a vague “continue later.”

# Definition of done

A full-push research project is done only when the requested deliverables are present and internally consistent: source audit, exact statement, reproducible computation where used, complete proof, theorem-strength assessment, requested Lean verification, independent audit, and a paper/artifact whose claims match the proof.