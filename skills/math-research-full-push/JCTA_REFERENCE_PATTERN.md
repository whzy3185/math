# JCTA progression pattern extracted from the math repository

Source examined:

- `research/paper/LONELY_RUNNER_JCTA_WRITING_AND_REVISION_HISTORY.md`
- source commit: `c3e4460929c38d10f0b3a0e878267142303c9675`
- recorded manuscript endpoint: v1.17, dated 2026-09-08

This file does not copy the mathematics of that project. It extracts the reusable research-management pattern that turned the Lonely Runner manuscript from proof material into a JCTA-oriented publication package.

## 1. What actually drove progress

The project did not advance by a fixed “literature → proof → paper → done” sequence.

It advanced through repeated cycles in which manuscript/referee pressure exposed new mathematical obligations.

The characteristic loop was:

```text
strong current result
→ write/compile a real manuscript
→ simulate a skeptical referee
→ find the most serious mathematical weakness
→ convert it to a theorem/lemma/completeness obligation
→ strengthen or correct the mathematics
→ upgrade exact verification/supplement if needed
→ rewrite the paper around the new mathematics
→ simulate referee again
```

This is the publication-stage analogue of the research control loop in `SKILL.md`.

## 2. Version progression and what each stage changed

| Version range | Main pressure | Resulting upgrade |
|---|---|---|
| v1.6 → v1.7 | draft sounded like a work log | objective mathematical voice; Abstract/Introduction/Main Results reorganized |
| v1.7 → v1.8 | too many small construction-step sections | sections compressed; background positioned around the mathematical problem |
| v1.8 → v1.9 | manuscript still looked like a technical/submission report | clean mathematical manuscript separated from submission metadata |
| v1.9 → v1.10 | roadmap and verifier language still drove the prose | continuous mathematical narrative; engineering language reduced |
| v1.10 → v1.11 | first serious simulated referee found genuine proof issues | false equivalence fixed; relation-plane black box opened; boundary exception isolated; global bound completed; cross-reference semantics checked |
| v1.11 → v1.12 | journal-style mathematical storytelling and literature precision | headings normalized; transitions driven by mathematical obstructions; references deeply audited |
| v1.12 → v1.13 | minor but real statement/source mismatches | source/version mapping and theorem hypotheses corrected |
| v1.13 → v1.14 | request to stop defending computation and add mathematics | finite outputs promoted to exact classifications/minimality/counting statements; certificate bound made explicit |
| v1.14 → v1.15 | stronger wording exposed a conceptual rank error | invariant corrected; endpoint lemma introduced; continuous verification converted to exact finite arithmetic |
| v1.15 → v1.16 | referee questioned certificate completeness | coverage equality added; generator/verifier separated; deterministic exact proof package strengthened |
| v1.16 → v1.17 | final closure and conceptual compression | main classification theorem closed; arithmetic obstruction promoted to lemma; abstract centered on mechanism rather than technical constants |

The critical lesson is that later versions were not merely more polished. Several versions were mathematically stronger and more correct than their predecessors.

## 3. Four upgrades to reproduce in future projects

### Upgrade I — proof material → paper

The first task is not beautification. It is identifying the mathematical story:

```text
problem → gap → conceptual theorem → consequences → proof architecture
```

The manuscript should not read like a chronological lab notebook.

### Upgrade II — technical report → mathematical narrative

Remove project-management prose from the clean manuscript.

The next lemma should be forced by the obstruction left by the previous argument.

Keep submission declarations/metadata outside the clean mathematics whenever possible.

### Upgrade III — computation → structural theorem + exact finite closure

This was the decisive mathematical transformation.

Instead of saying a program checks a large search:

1. prove a structural inverse/reduction theorem;
2. identify a finite canonical object;
3. prove why checking that object is sufficient;
4. express the final test in exact arithmetic;
5. promote important finite information to propositions/classifications/minimality statements.

A numerical bound coming from a certificate remains a sufficient certificate bound unless optimality is separately proved.

### Upgrade IV — credible result → permanently checkable proof package

Row-by-row certificate validity is insufficient if coverage is not established.

For proof-critical computation, aim for:

```text
canonical representation
+ complete generator
+ independent verifier
+ coverage equality
+ exact arithmetic
+ deterministic commands
+ frozen hashes/archive metadata
```

Main manuscript owns the mathematical reduction. Supplement owns implementation/reproduction details.

## 4. The most important reusable referee rule

> Do not answer a mathematical weakness mainly with defensive prose; first ask whether the missing explanation should be a stronger theorem, a new lemma, a finite-reduction principle, or an exact completeness statement.

Examples of issue → upgrade mappings:

| Referee-style issue | Preferred research response |
|---|---|
| “equivalently” is false | correct logical statement and recheck dependent claims |
| finite plane step is black-box | define the plane object, saturation/canonicalization, and prove the finite reduction |
| boundary case breaks an inequality | isolate the boundary case and determine whether it creates a separate structural family |
| full relation lattice described incorrectly | correct the invariant; restate the actual mechanism precisely |
| program checks rows but may miss classes | prove/check coverage set equality |
| numerical value appears tuned | establish minimality/structural meaning if true, otherwise label it a sufficient certificate bound |
| prior work contains the same family | move novelty to the global inverse/classification theorem if justified |

## 5. Contribution hierarchy

The JCTA-oriented project ultimately framed value in three layers:

1. conceptual structural/inverse theorem;
2. complete primitive configuration classification;
3. exact spectrum endpoint.

This hierarchy is reusable. A paper should normally foreground the deepest mechanism rather than the most memorable numerical corollary.

## 6. Referee maturity is a state variable

Track simulated-referee status over versions, for example:

```text
Major Revision
→ Major issues closed
→ Minor Revision range
→ Accept-after-revision range
→ mathematical freeze
```

This is a local audit signal only. It must never be presented as real peer review or editorial acceptance.

A verdict improves only when the underlying reasons improve. Do not change the label because prose became smoother while a proof obligation remains open.

## 7. Freeze rule

A stable manuscript should stop receiving large structural rewrites once:

- correctness blockers are closed;
- serious simulated-referee passes have been survived;
- main contribution hierarchy is stable;
- theorem strengthening has reached diminishing returns;
- novelty framing is rechecked;
- proof-critical computation is complete and exact;
- main/supplement responsibilities are clean;
- PDF semantics have been visually inspected.

After that point, reopen the core only for a mathematical error, a real referee/editor request, new prior art, or a genuinely valuable theorem upgrade.

## 8. How this pattern changes the skill

The reusable skill therefore needs three independent maturity axes:

- `L0–L6`: theorem strength;
- `M0–M7`: manuscript/referee maturity;
- `CAP0–CAP5`: computer-assisted proof maturity.

The next action is chosen from mathematical priority, not from whichever axis happens to have the lowest number.

A manuscript referee issue can immediately jump back to a P0/P3/P4 research task. This feedback is intentional: publication work is allowed to reopen theorem discovery when the referee exposes better mathematics.
