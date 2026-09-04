# Candidate article narratives

## Shared mathematical core

All narratives must use the same verified core and the same scope boundary.  They differ only in the order and interpretation of the results.

### Core theorem ladder

- **A1 — Gauge coordinates.** Switching classes on the finite cycle square are encoded by the triangle-flux word (\tau) and Hamilton holonomy (\alpha).
- **A2 — General half-cell criterion.** A natural monomial half-cell chiral
  involution exists exactly when `tau_(i+m)=-tau_i`, equivalently when the
  local `Q` word is half-periodic with negative half-cell flux.
- **A3 — Finite period-eight decomposition.** The explicit witness satisfies
  \[
  A_{8L,\alpha}\simeq\bigoplus_{z^L=\alpha}H(z).
  \]
- **A4 — Complete period-eight dispersion.** The target fiber reduces to
  (P(y,c)), and all four squared branches are explicit.  In particular the
  upper squared edge is
  \[
  r(c)=4+\sqrt{8+c+\sqrt{26-3c}},
  \]
  strictly increasing on ([-2,2]).
- **A5 — Exact finite radii.** Positive holonomy gives the constant value
  \[
  \rho(A_{8L,+})^2=\eta=4+\sqrt{10+2\sqrt5},
  \]
  while negative holonomy gives the explicit (L)-dependent formula.
- **A6 — Twisted comparison.** For every (L\ge4), (\eta<\rho_-(8L)^2).
- **A7 — Minimal period.** No legal period below eight has squared Bloch edge below eight.
- **A8 — Period-eight rigidity.** The antipodal two-defect word is the unique period-eight sub-eight class modulo natural symmetries; balanced words have edge eight, all remaining classes exceed eight.
- **A9 — General obstruction.** (M_1,M_2,M_3) impose necessary defect-density and clustering inequalities on arbitrary periodic words of edge at most eight.

## Narrative 1: JGT

### One-sentence story

Spectral-radius minimization over signings of a fixed cycle square exposes a rigid period-eight triangle-flux phase: it is the first periodic phase capable of crossing the squared edge eight, its hidden chiral symmetry makes its radius exactly solvable, and it yields an infinite family that beats the natural twisted signing.

### Headline theorem

State A5 and A6 together, with the explicit signing described before the formula.  The theorem should not be phrased as “the conjecture is false.”

### Second main theorem

Combine A7 and A8:

> Among legal periodic triangle-flux words, period eight is the first period admitting squared Bloch edge below eight; at period eight the sub-eight class is unique up to translation, reflection, global sign convention/lift equivalence, and cell repetition as precisely defined.

This is the result that turns the witness into a graph-theoretic phase.

### Introduction logic

1. signed adjacency spectra are invariant under switching;
2. optimizing signs on a fixed underlying graph is an exact extremal problem distinct from general signing existence;
3. cycle squares are simple enough for Fourier analysis but rich enough to possess overlapping triangle fluxes;
4. periodic flux can break one-site translation while preserving cell translation;
5. the central question is whether such local flux phases lower the signed spectral radius;
6. state the exact period-eight theorem;
7. state the minimal-period/rigidity theorem;
8. explain the proof in three sentences: finite Bloch decomposition, chiral block reduction, closed-walk moments/finite exact certificates;
9. only then mention the particular recent twisted-optimality conjecture as one consequence.

### Section movement

- A1 and the flux form of A2 before the period-eight Floquet matrix;
- A3–A5 in one exact-solution arc;
- A6 immediately after A5, so the main theorem closes early;
- A7–A8 next, answering “why eight?”;
- A9 last, broadening from the solved phase to arbitrary periodic defects.

### Risk and response

Risk: the paper is judged as an explicit computation on a narrow graph family.

Mathematical response: lead with A7–A8 as the structural explanation and make the local triangle-flux word the organizing graph object.  Do not respond with claims of broad applicability.

### Candidate titles

- *A period-eight phase in signed cycle squares with exact spectral radius*
- *The first low-edge periodic phase of a signed cycle square*
- *Switching, period-eight flux, and spectral radius in signed cycle squares*

## Narrative 2: LAA

### One-sentence story

A structured family of signed circulant Hermitian matrices has a hidden half-period chiral symmetry that yields a closed dispersion law and exact finite spectral radii under both periodic and antiperiodic holonomy.

### Headline theorem

Combine A2–A5.  The general iff is the matrix theorem; the complete
period-eight dispersion and exact (\alpha=-1) formula are its strongest
explicit realization.

### Second theorem

A7–A8 becomes a structural application showing that the exactly solved matrix is the first nonconstant periodic phase with squared edge below eight.

### Introduction logic

1. define the signed-circulant matrix family and its finite spectral-radius question;
2. explain switching as diagonal similarity and periodic words as block-circulant coefficients;
3. identify the obstacle: a nonconstant signing replaces scalar Fourier symbols by matrix-valued fibers;
4. state the general half-cell chiral criterion and dimension-halving consequence;
5. specialize it to period eight and state the exact four-branch dispersion and finite formulas;
6. state the extremal comparison and minimal-period application;
7. situate the method among signed matrices, gain graphs, and periodic magnetic graph operators.

### Section movement

- A1 and A3 compressed into matrix setup;
- A2 and A4 form the technical center;
- A5 has its own finite-quantization theorem;
- A6 is an application;
- A7–A8 are retained but shortened;
- A9 is optional and should be no more than one section.

### Risk and response

Risk: anticommuting block matrices and quartic solution are individually standard.

Mathematical response: novelty rests on the gauge-invariant iff within the
specified monomial class, the exact structured family, closed dispersion,
holonomy-dependent finite radii, and minimal-period extremal consequence.  Do
not inflate this into a classification of arbitrary chiral involutions.

### Candidate titles

- *Exact spectral radii of a period-eight family of signed circulant matrices*
- *Chiral reduction and exact spectra for period-eight signed circulants*
- *Holonomy and exact spectral edges in a signed circulant family*

## Narrative 3: SIGMA long-shot

### Gate result

The new general criterion makes this narrative mathematically viable, but the
venue audit still rates it high risk because the direct SIGMA community is
small and the paper has only one exactly solved primitive sub-eight family.

### What the story would require

The available story is now: periodic magnetic graph operators with negative
half-cell flux admit a monomial chiral involution and a general
(2m\times2m\to m\times m) squared reduction; the period-eight matrix is the
first sub-eight realization and is exactly solvable.

### Missing theorem ladder

- multiple primitive examples or a physical/topological consequence;
- a reason that the general `m x m` blocks matter to a recognized SIGMA community.

The first three former gaps—criterion, symmetry-class statement, and general
dimension halving—are closed.  The remaining community-reach gaps are not.
Therefore do not select SIGMA first and do not add speculative physics to fill
them.

## Recommended narrative

Use the **JGT narrative** for the master manuscript because it gives every theorem a conceptual role:

\[
\text{fixed graph}
\to\text{switching-invariant flux}
\to\text{general half-cell chiral mechanism}
\to\text{first possible low-edge period}
\to\text{hidden chiral exact solution}
\to\text{infinite finite-ring consequence}
\to\text{general defect obstruction}.
\]

This order preserves the author's preferred target while remaining convertible to LAA.  The exact matrix solution stays complete, but the article is not reduced to a determinant calculation.

## Treatment of the recent preprint in all viable narratives

- no title mention;
- no abstract mention unless the final abstract has room for one last consequence sentence;
- no mention in the opening three introduction paragraphs;
- one precise related-work paragraph after the independent problem and main theorems are established;
- no inherited claim is accepted without proof;
- the twisted signing is defined directly as a natural benchmark before its conjectural history is mentioned.
