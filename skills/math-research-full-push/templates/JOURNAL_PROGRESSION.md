# JOURNAL_PROGRESSION

This file records how a research result is upgraded into a publication-grade paper. It is modeled on the successful versioned JCTA-style workflow used in this repository: each revision must state not only what was rewritten, but what mathematical responsibility was exposed, repaired, strengthened, or made reproducible.

## Journal target

- Target journal / level:
- Manuscript title:
- Current manuscript version:
- Current simulated-referee verdict: `not assessed | reject-range | major revision | minor revision | accept-after-revision range`
- Mathematical freeze status: `open frontier | provisional freeze | frozen`
- Latest assessment date:

Do not present a simulated-referee verdict as an actual editorial decision.

## Contribution hierarchy

Rank the paper's contributions by conceptual value rather than chronology.

### C1 — conceptual / structural theorem

> Exact statement or one-sentence mathematical mechanism.

Why it matters beyond the seed problem:

### C2 — classification / global structural consequence

> Exact statement.

### C3 — endpoint theorem / exact spectrum / sharp bound / corollary

> Exact statement.

A cover letter, abstract, and introduction should lead with C1 when C1 is genuinely the deepest contribution. Do not reduce a structural paper to one missing value, one numerical bound, or one computational endpoint.

## Two independent maturity axes

### Theorem strength

- `L0` observed
- `L1` exact finite verification
- `L2` structural mechanism
- `L3` restricted proved theorem
- `L4` broad family / classification
- `L5` sharp / equality / iff / stability
- `L6` unifying framework

Current level:

### Manuscript maturity

- `M0` proof material / research notes
- `M1` coherent theorem manuscript
- `M2` mathematical narrative established; technical-report voice removed
- `M3` first serious simulated-referee pass; major mathematical responsibilities exposed
- `M4` structural upgrades and major-revision issues closed
- `M5` computer-assisted or formal proof package made exact and independently checkable
- `M6` minor-revision range; only localized mathematical/presentation issues remain
- `M7` freeze / submission preparation

Current level:

Never infer theorem strength from manuscript polish, or manuscript maturity from theorem strength.

## Version ledger

Use one row per meaningful manuscript revision. Cosmetic edits alone need not create a new research version.

| Version | Simulated-referee verdict before revision | Main issue exposed | Mathematical upgrade | Writing/organization change | Verification/proof-package upgrade | Verdict after revision | Commit/artifact |
|---|---|---|---|---|---|---|---|
| v0.1 |  |  |  |  |  |  |  |

## Referee issue registry

Every serious review comment should become an explicit obligation rather than disappearing into prose.

| ID | Version found | Severity | Type | Exact issue | Mathematical obligation | Resolution | Evidence | Closed in version |
|---|---|---|---|---|---|---|---|---|
| R001 |  | major/minor | correctness / semantics / black-box reduction / boundary / prior art / computation coverage / theorem strength / exposition |  |  |  |  |  |

### Referee-resolution priority

When a referee-style objection points to a mathematical weakness, prefer resolutions in this order:

1. correct a false statement or logical error;
2. expose the missing lemma/reduction explicitly;
3. strengthen the theorem so the mechanism becomes conceptual;
4. prove why the remaining computation is finite;
5. convert the finite task to exact arithmetic / exact set equality;
6. separate generator and verifier;
7. improve wording only after the mathematical responsibility is closed.

Do not answer a mathematical objection mainly with defensive prose.

## Four publication upgrades

Track whether the project has completed each of these transformations.

### Upgrade I — proof material → paper

- [ ] Abstract states problem → exact contribution → structural mechanism → method.
- [ ] Introduction is organized by the mathematical gap, not by the author's work log.
- [ ] Main Results are concentrated and easy to locate.
- [ ] Section structure reflects mathematical objects/problems, not project-management steps.

### Upgrade II — technical report → mathematical narrative

- [ ] No unnecessary “Proof strategy”, “Role of computation”, “Verification pipeline”, or similar engineering headings.
- [ ] The next lemma is motivated by the mathematical obstruction left by the previous argument.
- [ ] Theorems are not decorated with marketing subtitles unless mathematically standard/needed.
- [ ] Clean manuscript is separated from submission metadata and declarations.

### Upgrade III — computed result → structural theorem + exact finite closure

- [ ] The infinite problem is first reduced mathematically to a finite object.
- [ ] Important finite output has been promoted to a proposition/classification/minimality statement where appropriate.
- [ ] Current numerical bounds are labeled as optimal only if optimality is proved.
- [ ] Continuous verification is reduced to exact arithmetic when possible.
- [ ] The paper explains why the finite search is complete, not merely that a program ran.

### Upgrade IV — credible result → permanently checkable proof package

- [ ] generator and verifier are separated when feasible;
- [ ] certificate coverage is checked as set equality / missing=0 / extra=0 when applicable;
- [ ] proof-critical arithmetic is deterministic and exact;
- [ ] commands, versions, checksums, expected outputs, and resource notes are preserved in supplement;
- [ ] proof-critical supplement has a frozen release/archive plan;
- [ ] main manuscript states mathematical finite propositions; implementation QA lives in supplement.

## Computer-assisted proof maturity

Mark the highest achieved level.

- `CAP0` exploratory computation only
- `CAP1` exact finite observations with stated search range
- `CAP2` proved structural reduction to a finite task
- `CAP3` finite endpoint/decision principle expressed as a mathematical lemma or proposition
- `CAP4` exact generator/verifier separation plus coverage equality or equivalent completeness check
- `CAP5` deterministic frozen proof package with reproducibility metadata and permanent-archive plan

Current CAP level:

The goal is not to eliminate computation at all costs. A clean structural theorem plus exact finite closure is preferable to pages of artificial manual casework if the latter adds no mathematics.

## Narrative audit

For each major section, answer the question that naturally forces the next section.

| Section | Mathematical question entering section | What is proved | What obstruction remains | Why next section is necessary |
|---|---|---|---|---|
| 1 |  |  |  |  |

Avoid roadmap prose of the form “Section 3 does..., Section 4 then...“ when the mathematics itself can create the transition.

## Literature and priority audit

- Original problem/source:
- Strongest direct predecessor:
- Closest structural family already studied:
- Strongest bounded/computational predecessor:
- What those papers do **not** prove:
- Exact novelty of C1:
- Exact novelty of C2:
- Exact novelty of C3:
- Last fresh literature audit date:

When prior work already contains one parameterized family, do not market the family as new. Re-center the paper on the theorem proving that all relevant configurations must globally reduce to those families, if that is the genuine new result.

## Main-manuscript / supplement division

### Main manuscript owns

- mathematical definitions;
- structural reductions;
- theorem statements;
- exact finite propositions;
- proof of finiteness/completeness mechanism;
- conceptual significance.

### Supplement owns

- source code;
- certificate tables / CSVs;
- command lines;
- runtime/memory metadata;
- hashes;
- implementation-level QA;
- deterministic reproduction instructions.

Do not let the supplement carry a missing mathematical reduction that the paper needs for correctness.

## Freeze gate

The mathematical core may be frozen only when:

- [ ] no P0 correctness blocker remains;
- [ ] first serious simulated-referee pass has been completed;
- [ ] every major referee issue is closed or explicitly accepted as a limitation;
- [ ] main contribution hierarchy is stable;
- [ ] theorem strengthening has been attempted and stopped for recorded reasons;
- [ ] latest theorem form has been rechecked against direct prior art;
- [ ] any proof-critical finite computation has reached the required CAP maturity;
- [ ] manuscript claims match proof and supplement exactly;
- [ ] rendered PDF has been inspected, not merely compiled.

After freeze, reopen the core proof only for a new mathematical error, a real referee/editor requirement, a new prior-art collision, or a clearly valuable theorem upgrade. Do not endlessly restructure a stable proof merely because another presentation is possible.

## Submission-only queue

Keep post-freeze tasks separate from mathematical research:

- permanent supplement archive / DOI (never invent one);
- author final verification;
- reference metadata;
- cover letter;
- declarations and publisher metadata;
- final clean/submission PDF synchronization.

## Current next revision

- Proposed version:
- Referee issue(s) being closed:
- Mathematical delta required:
- Verification delta required:
- Manuscript delta required:
- Expected maturity change: `L?→L?`, `M?→M?`, `CAP?→CAP?`
- Freeze impact:
