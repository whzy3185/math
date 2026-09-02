# Manuscript integration assessment: the analytic period-eight route

## Decision

The period-eight material is sufficiently coherent for one analytic article.
Its natural argument is not a chronological account of repository discoveries:

\[
\text{gauge coordinates}
\longrightarrow
\text{period-eight phase selection}
\longrightarrow
\text{chiral Floquet reduction}
\longrightarrow
\text{finite-ring counterexample family}.
\]

This route has one explicit construction, one structural mechanism, and one
strict comparison with the predecessor's candidate.  That is a suitable
single-paper contribution.  It should not be expanded into a catalogue of
all experiments or an unfinished all-even classification programme.

## Recommended theorem ladder

| Article position | Mathematical content | Evidence class | Recommended placement |
|---|---|---|---|
| Main Theorem | Every \(C_{8L}(1,2)\), \(L\ge4\), has an explicit signing strictly better than the twisted signing | analytic | introduction and Section 4 |
| Proposition A | Hamilton-gauge realization and finite holonomy/Floquet decomposition | analytic | preliminaries |
| Proposition B | The target eight-periodic phase has squared edge \(4+\sqrt{10+2\sqrt5}\) | analytic | central spectral section |
| Theorem C | The target is uniquely below squared edge eight among legal eight-periodic local-flux phases | analytic plus one finite integer recurrence | secondary theorem, with its finite component deferred |
| Corollary | The original universal twisted-optimality assertion fails for infinitely many orders | analytic | end of main theorem section |

The finite closed-walk recurrence for the three non-antipodal two-defect
cases belongs in an appendix or a concise supplement.  It is small, exact,
and explanatory, but it should not interrupt the Floquet proof's main line.

## Section architecture

1. **Introduction.** State the predecessor's candidate, the infinite
   counterexample theorem, and the chiral period-eight mechanism.  Do not
   claim the exact global minimum or a complete classification.
2. **Signed-circulant coordinates and the twisted benchmark.** Define the
   graph, switching, Hamilton gauge, holonomy, and the benchmark quantity.
3. **Why the period-eight phase is distinguished.** Give the moment barrier,
   then state the period-eight trichotomy.  Move the finite two-defect table
   out of the main narrative.
4. **Chiral Floquet reduction.** Derive the fiber, involution, \(BC\) block,
   polynomial \(P\), and exact edge.
5. **Finite-holonomy consequence.** Prove the rational spectral bound and
   the Taylor comparison, then conclude the infinite counterexample family.
6. **Discussion.** Explain exactly what remains open; this is one short
   paragraph, not a computational-results section.

Appendix A contains the closed-walk recurrence and sixth-moment catalogue.
Appendix B may contain determinant arithmetic or the reproducibility/Lean
kernel plan, but no numerical witness archive is necessary for the theorem.

## Material that must stay out

The following do not form a valid progression in this article:

- exact enumeration through order \(30\) or the assertion that \(32\) is the
  first failure;
- R2 Riccati/response drafts, including finite seeds and numerical screens;
- residue-four or residue-six interface templates;
- G6 elimination or physical-branch drafts;
- the claimed all-even truth pattern;
- a large Lean development before the analytic theorem is frozen.

They either depend on computation, remain incomplete, or answer a different
and much broader classification question.  Including them would force a
reader to distinguish too many evidence levels and weaken the paper's
central story.

## When a sequel becomes reasonable

A broader paper is justified only after all of the following are independently
proved: the R2 cyclic tail theorem, parameterized R4 and R6 interface
theorems, a physical G6 edge theorem, and a transparent treatment of the
remaining equality orders.  Until then, those modules are research
infrastructure, not a sequence of publishable intermediate sections.

## Lean role

After the theorem ladder above is fixed, Lean may formalize its core as a
supplementary verification artifact.  It should validate the exact stated
theorem, not reshape the article or certify excluded claims.
