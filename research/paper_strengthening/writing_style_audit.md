# Writing-style audit and mathematical drafting rules

## Evidence boundary

The venue reports distinguish full-text inspection from metadata-only screening.  The rules below are derived only from the accessible full-text subset and the journals' official instructions.  They are structural regularities, not copied sentences.

## Three-venue comparison

| feature | JGT | LAA | SIGMA |
|---|---|---|---|
| opening unit | graph problem, closest theorem, exact result | matrix/operator class, missing spectral fact, exact result | established physics/geometry system and general mechanism |
| main theorem | usually very early | introduction or first substantive section | early, but after enough general formalism to show community relevance |
| related work | mostly integrated into introduction | integrated or brief dedicated discussion | often broad because a specialist formalism must be situated |
| preliminaries | short; definitions near use | can be substantial if matrix notation is reused | can be long and conceptual |
| acceptable special-family paper | yes, if complete/structural | yes, if exact matrix insight | only if it illuminates a recognized broader model |
| algebra in body | compress unless graph meaning is visible | detailed exact algebra is acceptable | must serve general symmetry/integrability/geometry |
| computation | finite, reproducible, subordinated to proof | symbolic checks acceptable but derivation required | varies; irrelevant to current fit |
| conclusion | often short or absent | short conclusions common but not mandatory | discussion tied to broader formalism common |

## Corpus-derived JGT rules

1. State the main graph theorem by page 2 or 3.
2. Name the underlying graph, admissible signings, equivalence relation, and optimized quantity before giving history.
3. Present the exact family result before the conjecture consequence.  The reader should understand the theorem without knowing the preprint.
4. Make “why period eight” a theorem, not an explanatory slogan.
5. Put graph transformations, local flux data, and symmetry classes into theorem statements or propositions; do not leave them as informal observations.
6. Keep the Floquet and chiral calculation self-contained, but interpret every reduction back in graph terms.
7. If finite exact checking is necessary, state the reduced domain, symmetry quotient, certificate type, and exact verification rule before the table.
8. Do not use a broad conclusion to repeat the abstract.  State only the achieved scope and one mathematically specific open problem.

## Corpus-derived LAA rules

1. Give the structured Hermitian matrix or fiber explicitly.
2. Separate similarity/gauge invariance from Bloch phase quantization.
3. State the block-reduction lemma in a reusable matrix form if it is actually used more than once; otherwise prove it directly for (H(z)).
4. Display the characteristic polynomial and the variable substitutions that make it solvable.
5. Replace numerical evidence by exact root ordering and monotonicity.
6. Let exact formulas carry the theorem; use graph extremality as an application.
7. Long matrix algebra is acceptable only when each displayed identity advances the reduction.  Suppress mechanical expansion.
8. Keep the negative-holonomy formula because it demonstrates that the phase grid, not only the infinite band, controls the finite radius.

## Pure-mathematics adaptation of the ARS workflow

The workflow is:

\[
\text{research}
\to\text{claim ledger}
\to\text{dependency map}
\to\text{draft}
\to\text{integrity gate}
\to\text{review panels}
\to\text{revision}
\to\text{independent re-audit}.
\]

It differs from an experimental paper workflow in four ways.

### 1. The evidence table is a theorem ledger

Every mathematical claim receives:

- exact quantifiers;
- hypotheses;
- conclusion;
- proof mechanism;
- dependency list;
- status: analytic, finite exact, Lean checked, or computational background only;
- manuscript destination.

### 2. The outline is a dependency order

Section order is not discovery order.  A statement appears only after all objects in it have been defined and all reusable mechanisms needed for its proof have been established.

### 3. Citation checks do not certify mathematics

Literature establishes terminology, prior results, and novelty boundaries.  It does not validate our determinant, root formula, finite phase grid, or strict comparison.  Those require independent proof audits.

### 4. Review is adversarial theorem checking

The key reviewers are a graph theorist, a matrix spectral theorist, and a devil's advocate looking for a stronger trivial consequence or a hidden restriction.

## Section-level argument map template

Every section plan must contain the following record.

| field | question |
|---|---|
| object | what mathematical object is introduced here? |
| assumption | what exact conditions are in force? |
| claim | what theorem/lemma is proved? |
| mechanism | switching, direct sum, chiral block, root monotonicity, moments, or finite certificate? |
| consequence | what is newly known at the end of the section? |
| later dependency | which named result uses it? |

If a paragraph has no entry in this map, it is removed.

## Integrity gate for the master draft

### Quantifiers and scope

- distinguish (L\ge1) exact witness radius from (L\ge4) strict twisted comparison;
- keep current Lean coverage explicitly at (\alpha=+1);
- never turn uniqueness among period-eight phases into global uniqueness among all signings;
- never turn minimal period among legal periodic flux words into a classification of arbitrary finite signings;
- never claim the value of (m_{8L}).

### Finite versus infinite

- prove the finite direct sum before using the infinite dispersion law;
- state (z^L=\alpha) every time the finite phase set matters;
- show explicitly that (z=1) is allowed for (\alpha=+1);
- for (\alpha=-1), identify the closest phases and why (c_{\max}=2\cos(\pi/L)).

### Spectral quantities

- keep (\rho(H)), (\rho(H)^2), (y=\lambda^2), and the upper squared edge distinct;
- state whether a formula is an eigenvalue, a squared eigenvalue, or a root of (P);
- relegate (1561/200) to an optional exact separator; it is not the main spectral value.

### Proof provenance

- “analytic” means a human-readable derivation is in the manuscript or source notes;
- “finite exact” means integer/rational/algebraic identities verify a finite reduction;
- “Lean checked” refers only to the frozen L1–L7 (\alpha=+1) comparison kernel;
- do not imply that the new exact-radius and minimal-period upgrades have been Lean formalized.

### Literature

- cite a source only for a claim it actually contains;
- do not cite recent papers merely to manufacture novelty;
- mark analogies as analogies;
- keep Suvagiya out of the independent problem formulation.

## Anti-defensive and anti-AI prose rules

“Defensive writing” is removed at drafting time, not cosmetically polished later.

### Delete these habits

- repeated sentences beginning “We emphasize that we do not…”;
- lists of everything the paper does not solve inside the introduction;
- generic claims such as “spectral graph theory has attracted much attention”;
- inflated transitions such as “It is worth noting that” and “Interestingly”;
- announcing that an elementary calculation is “highly nontrivial”;
- narrating repository history, failed approaches, or proof-search chronology;
- calling a short exact recurrence “computer-assisted proof” when the recurrence and certificates can be written down;
- overusing roadmap paragraphs and theorem summaries.

### Replace them with mathematical statements

- Put scope into theorem quantifiers.
- Put a limitation into one sentence in the conclusion only when it determines the next problem.
- Replace “surprisingly” by the identity or inequality that is surprising.
- Replace “using sophisticated Floquet theory” by the finite direct-sum formula.
- Replace “extensive computation confirms” by the nine representatives and exact certificates.

### Preferred proof verbs

Use concrete verbs: switch, decompose, anticommute, factor, eliminate, compare, attain, average, count, and bound.  Avoid empty verbs: leverage, utilize, shed light, unveil, facilitate, and showcase.

## Human-readable proof standard

A proof is ready for the manuscript only if a reader can reproduce its decisive step without running code.

- The (8\times8\) fiber: all nonzero entries and boundary phases are visible.
- Chiral symmetry: (J_z^2=I) and (J_zH(z)=-H(z)J_z) are checked on an explicit basis or edge types.
- Polynomial: the determinant identity is displayed, not only its result.
- Exact edge: the shift (y=X+4), quadratic in (W=X^2), correct root branch, and monotonicity derivative are shown.
- Minimal period: legal-word reduction is explained; exact determinant/Rayleigh certificates are tabulated; the verifier is supplementary only.
- Moments: local statistics are defined before the closed-walk identities, and inequalities follow from (0\le y\le8), not numerical observation.

## Visual policy

The manuscript should use at most three figures and one exact certificate table.

1. **Signed cell figure:** vertices (0,\ldots,7), step-one cycle, step-two chords, and the two antipodal positive defects in the local flux word.
2. **Finite Bloch figure:** an (8L)-vertex ring cut into (L) cells with seam holonomy (\alpha) and phase condition (z^L=\alpha).
3. **Optional dispersion figure:** exact (r(c)) over ([-2,2]), with positive and negative finite phase samples; explicitly illustrative.
4. **Certificate table:** periods (1\)–(7), representatives after symmetry reduction, chosen phase, and exact sign of the determinant/Rayleigh value.

No screenshots, code output, search tables, or Lean proof states belong in the article.
