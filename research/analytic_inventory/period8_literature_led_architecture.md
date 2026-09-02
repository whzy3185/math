# Literature-led architecture for the analytic period-eight article

## Evidence used for the structural comparison

The direct predecessor, Suvagiya's 2026 preprint, proceeds from the specific
circulant family through flux coordinates and distinguished signings to a
Fourier formula, finite evidence, and then a conjecture.  The periodic
magnetic-operator work of Korotyaev--Saburova proceeds from periodic
operator/fiber setup to trace formulas and then spectral applications.  The
repository's reviewed signed-extremal and JGT classification notes show two
additional patterns: structural candidate reduction before spectral equality
analysis, and theorem-first large-regime/finite-exception synthesis.

Our article should borrow only the first two patterns.  It is a single
analytic mechanism paper, not an all-order classification or a
computer-assisted exception paper.

## Chosen non-appendix structure

### 1. Introduction: a conjectural benchmark fails

Start from the published fixed-underlying-graph signing question, then state
the direct predecessor's twisted candidate and conjecture.  Immediately state
the infinite period-eight counterexample theorem.  Give a three-sentence
roadmap:

\[
\text{gauge coordinates}\ \to\ \text{chiral fiber}\ \to\
\text{uniform finite-ring comparison}.
\]

The introduction must not begin with enumeration, low-order failures, a
large bibliography, or the phrase “smallest counterexample.”

### 2. Gauge coordinates and finite Bloch reduction

Define \(C_n(1,2)\), switching, triangle flux, Hamilton holonomy, and the
twisted benchmark.  Prove the finite Hamilton-gauge realization and the
condition \(z^L=\alpha\) for \(n=8L\).  End by displaying the chosen
period-eight word.  This section corresponds to the direct predecessor's
coordinate stage, but its purpose is now construction rather than conjecture.

### 3. A chiral period-eight fiber

This is the technical centre.  Display \(H(z)\), construct \(J_z\), reduce
to the \(BC\) block, and obtain \(P(y,c)\).  State and prove the exact edge

\[
\eta=4+\sqrt{10+2\sqrt5}.
\]

This follows the periodic-operator model: the finite fiber and its exact
algebra are the main object, rather than background for a computation.

### 4. The infinite counterexample family

Use the positive polynomial expansion at \(1561/200\), then the elementary
Taylor comparison for the twisted benchmark.  Conclude the main theorem for
every \(8L\ge32\).  This section should end the first half of the paper and
contain the only headline result needed for publication.

### 5. Why this phase is distinguished

Introduce the local square identity and the first three moment barriers.
Prove the period-eight below/equal/above-eight trichotomy.  The three
non-antipodal two-defect cases remain a compact exact integer recurrence in
the main text: display its recurrence and the three positive excesses, rather
than hide a logically necessary calculation in an appendix.  This section is
the structural strengthening, not a search report.

### 6. Closing perspective

State exactly three points: the original all-even assertion is false; the
period-eight phase has a rigid local spectral role; global minimization over
all signings and all periods remains open.  Do not describe R2, R4, R6, G6,
finite enumerations, or implementation infrastructure here.

## What this deliberately rejects

The old repository architecture made the smallest finite counterexample,
bounded-period frontier, general-period obstruction, and computer-assisted
trust model into consecutive main sections.  That structure is appropriate
only for a completed classification paper.  With the present analytic
evidence it would make the paper look like an unfinished computational
classification wrapped around one strong Floquet calculation.

The proposed six sections instead resemble a concise spectral-operator
article: one object, one exact fiber calculation, one global consequence, and
one structural explanation.
