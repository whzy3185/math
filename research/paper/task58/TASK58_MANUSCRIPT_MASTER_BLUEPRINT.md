# Task 58 Manuscript Master Blueprint

Status: `TASK58_2_BLUEPRINT_LOCKED_FOR_GATE_A`.

This blueprint fixes the first-submission narrative and placement plan. It
does not add a theorem, alter a hypothesis, or authorize import from a source
outside the Task 58 control documents and the canonical proof-completion
package. The intended paper has one question and two layers of answer:

1. a complete classification of the even orders at which the proposed
   signing is globally minimizing; and
2. a structural explanation of eventual failure through the period-eight
   reference phase and its unique least-cost abnormal single-gap interface.

The finite exact classification determines the irregular small-order pattern.
The G6 mechanism explains why failure is eventually permanent. The exact
finite bridge, not the G6 mechanism alone, places the continuous onset at
order 48.

## 1. Final Title and Ambiguity Control

Final title:

> **Spectral Radius Minimization for Signed Squares of Cycles**

The phrase “signed squares of cycles” is potentially ambiguous: it could be
read as first signing a cycle and then squaring that signed graph. The first
sentence of the abstract and the first paragraph of the Introduction must
therefore say explicitly that the underlying unsigned graph is the cycle
square

$$
G_n=C_n^2=C_n(1,2),
$$

and that its distance-one and distance-two **edges are independently assigned
signs**. The short running description, when needed, is “edge signings of
$C_n^2$.” The paper must not suggest that the signing is induced from a signed
cycle.

## 2. Abstract Logic

The abstract is one paragraph of approximately 150--190 words and follows
this six-sentence logic. It contains no citations, implementation details,
internal claim identifiers, or exact-$2r$ refinement.

1. **Object and problem.** Define $C_n^2$ and
   $m_n=\min_\sigma\rho(A_\sigma)$ for even $n\ge8$, making the edge-signing
   interpretation explicit.
2. **Conjectured value.** State
   $\rho_-(n)^2=4+2\cos(2\pi/n)+2\cos(4\pi/n)$ and say that the distinguished
   twisted signing attains this value at every even order.
3. **Complete classification.** State that equality holds exactly for
   $$
   \{8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46\},
   $$
   or, equivalently, that strict failure occurs precisely at $32$, $40$, and
   every even $n\ge48$.
4. **Structural answer.** Say that a period-eight reference phase has squared
   edge $\eta<8$, while the six-gap phase slip is the unique least-cost
   abnormal positive single gap and has an isolated rank-two squared edge
   $c_6\in(\eta,8)$.
5. **Infinite tail versus sharp onset.** State that separated G6 slips and a
   discrete IMS estimate prove eventual failure, while exact finite
   verification shows that continuous failure begins precisely at order 48.
6. **Proof boundary.** End by saying that the finite portions are reduced to
   explicitly finite exact objects and independently verified using exact
   arithmetic. Do not advertise software, tests, certificate counts, or
   hardware.

The abstract must not claim a classification of all minimizing signings, an
exact value of $m_n$ at failing orders, a common residue limit, or a universal
multi-gap theorem.

## 3. Introduction: Eleven Natural Paragraphs

The Introduction should occupy approximately four pages. The following are
eleven prose paragraphs, not eleven micro-subsections. The two displayed
results below are the only theorem boxes in the Introduction and use ordinary
theorem environments in the manuscript.

### Paragraph 1: the concrete graph problem

Define $G_n=C_n^2=C_n(1,2)$ for even $n\ge8$, an edge signing $\sigma$, its
real symmetric signed adjacency $A_\sigma$, and
$m_n=\min_\sigma\rho(A_\sigma)$. Explain switching equivalence in one
sentence. Remove the title ambiguity by saying that the edges of the already
formed cycle square are signed independently.

### Paragraph 2: general signing-minimization context

Place the problem inside fixed-graph signature minimization. Cite Bilu--Linial
for the general signing/2-lift program, Belardo--Cioaba--Koolen--Wang for the
explicit fixed-graph minimization problem, and Marcus--Spielman--Srivastava
for interlacing-family existence results. Preserve the one-sided/general
versus two-sided/bipartite distinction; $C_n^2$ is nonbipartite. If current
context is desired at submission time, cite Xu--Zhang only as a general
two-sided upper bound, not as a sharp result for this family.

### Paragraph 3: the direct predecessor

Name Suvagiya's 2026 preprint first among problem-specific sources. State that
it introduced the distinguished quadrilateral/parity family for this graph,
computed the twisted spectral formula, verified optimality through order 18,
and formulated the all-even-order assertion as Conjecture 3. The present paper
must be described as determining exactly when that candidate is globally
minimizing, thereby resolving and disproving the conjecture. Do not claim to
introduce the problem, flux coordinates, candidate, or Fourier formula.

### Paragraph 4: the surprising nonmonotone answer

Preview the truth pattern in words: the first failure is $32$, equality
returns at $34,36,38$, failure returns at $40$, equality returns at
$42,44,46$, and only from $48$ onward is failure permanent. Emphasize that the
paper determines this pattern exactly; do not claim a conceptual G6
explanation for the isolated values $32$ and $40$.

### Paragraph 5: comparison value and equality logic

Define

$$
\rho_-(n)^2=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n},
\qquad \theta_n=\rho_-(n)^2.
$$

State that the explicit $Q_i=-1$, $\alpha=-1$ signing attains
$\rho_-(n)$ at every even order. Explain in one sentence that equality needs
both this attainment direction and a universal lower bound from exhaustion.
Then insert the first result.

**Introduction theorem box 1: Complete classification.** For every even
$n\ge8$, the distinguished twisted signing attains $\rho_-(n)$, and

$$
m_n<\rho_-(n)
\quad\Longleftrightarrow\quad
n=32,\quad n=40,\quad\text{or}\quad n\ge48.
$$

Equivalently, $m_n=\rho_-(n)$ exactly for

$$
\{8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46\}.
$$

The statement must immediately note that it classifies the truth of the
proposed equality, not all minimizers or the exact failing values.

### Paragraph 6: what the classification does and does not explain

Interpret the first result. The finite classification determines the
irregular small-order truth table, whereas the phase-slip theory explains
eventual permanence. Reserve the statement “continuous failure begins at
48” for the combination of the analytic tail and the exact finite bridge.

### Paragraph 7: reference phase, gaps, and charge

Introduce the period-eight reference phase as a structural comparison bulk,
not as the attaining candidate. Mention the gap coordinate $g$, charge
$q=g-4$, the global ring law $\sum q_j\equiv n\pmod8$, and the local sector
law $\sigma_{\rm sec}(q)=q\pmod4$. Explain that one, two, and three G6 slips
provide the nonzero even residue classes, without conflating the two
congruence laws.

### Paragraph 8: exact predefinition of the structural edge

Before the second result, define

$$
\eta=4+\sqrt{10+2\sqrt5}
$$

and define $c_6$ as the unique root in the rational isolating interval

$$
\frac{7905369311620327}{10^{15}}<c_6<
\frac{7905369311620328}{10^{15}}
$$

of the degree-ten polynomial

$$
\begin{aligned}
p_6(y)={}&16y^{10}-520y^9+6913y^8-48448y^7+191768y^6\\
&-423904y^5+484528y^4-270464y^3+137856y^2\\
&-19968y+256.
\end{aligned}
$$

For the bilateral positive single-gap operator $H_g=A_g^2$, set
$E(g)=\sup\sigma(H_g)$. Only after these definitions insert the second
result.

**Introduction theorem box 2: Reference and single-gap spectral hierarchy.**
For both lifts and orientations,

$$
E(4)=\eta<c_6=E(6),
$$

$$
\sigma_{\mathrm{ess}}(H_6)=\sigma(H_{\mathrm{ref}}),
\qquad \dim\ker(H_6-c_6)=2,
$$

and, for every positive integer $g\notin\{4,6\}$,

$$
E(g)>c_6+\frac1{250}.
$$

The accompanying sentence must say that G6 is the unique minimizer among
abnormal positive single gaps only. It must not infer arbitrary multi-gap or
finite-core optimality.

Machine-auditable alias for this placement contract:
`dim ker(H_6-c_6)=2`.

### Paragraph 9: from the line defect to finite rings

Explain the local-to-global bridge: legal finite rings contain one, two, or
three separated G6 patches; patch identification imports the reference/G6
line bounds; a discrete IMS partition controls the global squared spectral
top. This proves failure for every even $n\ge240$. State explicitly that this
is the structural explanation of eventual failure, not a proof that the
onset is 48.

### Paragraph 10: the finite exact closure

Summarize the finite proof architecture in mathematical order: exact
switching-class decisions through 32; a sound, complete, terminating
parity-lifted finite-state closure for $34,36,38,42,44,46$; exact witnesses at
32 and 40; and 96 rational positive-definiteness certificates for
$48\le n<240$. Cite Goedgebeur--Schaudt and DeVos--Samal only as precedents
for theorem-backed exhaustive computation, and Lin--Ning plus
Goedgebeur--Renders--Wiener--Zamfirescu as editorial precedents for an
analytic tail combined with finite closure. These citations support proof
presentation, not novelty.

### Paragraph 11: novelty boundary and organization

Use the cautious claim: “To the best of our knowledge, no previous work gives
an all-order classification of the minimizing behavior over all real edge
signings of the fixed circulant family $C_n(1,2)$.” This sentence must follow
the explicit credit to Suvagiya. Briefly distinguish signed extremal results
where the underlying graph varies and cite Belardo--Brunetti--Ciampella and
Brunetti--Stanic. Close with a compact section roadmap. The unpublished Suda
seminar remains an internal watchlist item and is rechecked before submission,
not cited as a theorem.

## 4. Full Section and Subsection Tree

The manuscript has exactly eight numbered sections. Internal canonical claim
IDs below guide source control and review; they do not appear in publication
prose, theorem names, captions, or cross-references.

### 1. Introduction

- Follow the eleven-paragraph plan above.
- Place only the two displayed Introduction results specified above.
- Include neither a contribution list nor a proof-dependency graphic.

### 2. Switching Coordinates and the Reference Phase

#### 2.1. Edge signings, switching, and Hamilton gauge

Define $G_n$, $A_\sigma$, switching, $m_n$, $\rho_-(n)$, and $\theta_n$.
Prove the Hamilton-gauge reduction (`T1.1`).

#### 2.2. Flux words, holonomy, and the attaining candidate

Define $(\tau,Q,\alpha)$ with $Q_i=\tau_i\tau_{i+1}$ (`T1.2`). State the
explicit $Q_i=-1$, $\alpha=-1$ candidate and prove its antiperiodic Fourier
attainment formula (`T8.0`). This is the upper direction at every order.

#### 2.3. The squared local operator

Define $A_\tau$ and $H_\tau=A_\tau^2$, record the exact range-four formula
(`T1.4`), and state only the equivalences needed later (`T1.3`). Keep squared
and unsquared notation visibly separate.

#### 2.4. The period-eight reference phase

Define $\tau_{\rm ref}$, $Q_{\rm ref}$, and the four translates $B_s$.
State and prove the reference-edge theorem
$\sup_{|z|=1}\rho(A_{\rm ref}(z))^2=\eta$, with equality only at $z=1$
(`T2.1`, `T2.2`), and identify $g=4$ as reference bulk rather than an
interface (`T2.3`). Defer determinant expansion and endpoint certification to
Appendix A.

### 3. Gaps, Charges, and Translation Sectors

#### 3.1. Cyclic gaps and excess charge

Define positive-$Q$ sites, $g_j$, and $q_j=g_j-4$. Prove
$\sum g_j=n$, $\sum q_j=n-4d$, parity of $d$, and the global ring-closure law
$\sum q_j\equiv n\pmod8$ (`T3.1`). Treat the defect-free word separately.

#### 3.2. Translation sectors

Define $B_s$ and prove the local interface law
$\sigma_{\rm sec}(q)=q\pmod4$ (`T3.2`). The proof must precede any use of
sector labels in residue constructions.

#### 3.3. Composition and legal cyclic closure

Prove additivity and sector closure (`T3.3`). Derive the legal one-, two-, and
three-G6 charge patterns for residues 2, 4, and 6 modulo eight. State again
that the modulo-eight and modulo-four laws answer different questions.

### 4. The Elementary Six-Gap Phase Slip

#### 4.1. The bilateral interface and its essential spectrum

Define $A_6$ and $H_6$. Prove bounded self-adjointness, finite-rank two-tail
decoupling,
$\sigma_{\rm ess}(H_6)=\sigma(H_{\rm ref})$, discreteness above $\eta$, and
exponential decay of physical modes (`T4.0`). Essential-spectrum equality is
not presented as existence of $c_6$.

#### 4.2. Algebraic candidate and physical matching

Define $c_6$ by the degree-ten polynomial and isolating interval (`T4.1`).
Develop the stable/unstable transfer spaces and explain why their physical
intersection is necessary and sufficient. State the exact candidate
completeness and realization ingredients; move the complete chart,
resultant, Sturm, and exclusion audit (`C.6`) to Appendix A.

#### 4.3. The global G6 edge

Prove $\sup\sigma(H_6)=c_6$ for both orientations and lifts (`T4.2`). Keep
existence, discreteness, candidate completeness, physical matching, and
maximality as separate logical steps.

#### 4.4. Rank-two symmetry

Introduce $(Ku)_i=(-1)^iu_{9-i}$ and prove
$K^2=-I$, $KA_6=-A_6K$, and $KH_6=H_6K$. Deduce
$\dim\ker(H_6-c_6)=2$ and the simple unsquared partners
$\pm\sqrt{c_6}$ (`T4.3`). Never call $c_6$ simple for $H_6$.

### 5. Optimality Among Single-Gap Interfaces

#### 5.1. Canonical single-gap operators

Define $H_g$ for every positive gap, both lifts, and both orientations.
Separate $g=4$ as the reference phase and $g=6$ as G6.

#### 5.2. Exact finite-gap comparisons

Give the mathematical partition of the finitely treated gap classes and the
Rayleigh-quotient principle. Print only the exact rational comparisons needed
to establish the uniform margin; move full integer vectors and reconstruction
metadata (`C.8`) to the supplement.

#### 5.3. Uniform control of the large gaps

Give the finite-support witness that covers the infinite large-$g$ tail and
prove its support is unaffected by the remote interface boundary.

#### 5.4. Reference and single-gap hierarchy

Synthesize (`T5.1`, `T5.2`):
$E(4)=\eta<c_6=E(6)$ and
$E(g)>c_6+1/250$ for $g\notin\{4,6\}$. End with the explicit single-gap-only
scope statement.

### 6. Phase Slips on Finite Rings

#### 6.1. Legal residue constructions

Define the displayed one-, two-, and three-G6 gap words and prove their gap
sums, lift parity, holonomy, charge closure, sector closure, and separation
formulas (`T7.1`).

#### 6.2. Identification of local patches

Prove that every enlarged localization window is either reference bulk or a
forward/reflected G6 patch, including seam, wraparound, lift, orientation,
and holonomy cases (`T6.0`). This proposition is a required analytic bridge,
not part of the optional exact-$2r$ proof.

#### 6.3. Discrete IMS localization

Prove the exact double-commutator identity, cyclic tent partition, support
conditions, and range-four error estimate (`T6.1`). Combine patch
identification with the bulk and G6 edges to obtain the fixed-interface cap
(`T6.2`).

#### 6.4. Residue upper bounds and the analytic tail

Derive only
$\limsup_{k\to\infty}m_{8k+s}^2\le c_6$ for
$s\in\{2,4,6\}$ (`T7.2`). Then use the explicit threshold comparison and
endpoint monotonicity to prove strict failure at every even $n\ge240$, the
analytic part of (`T7.3`). Make clear that no lower bound, limit, common
liminf, or minimizer classification follows.

#### 6.5. Structural refinement for separated interfaces

Give a single theorem statement and one short proof overview for (`T6.3`):
for $r\in\{1,2,3\}$ and $D\ge1040$, the fixed window around $c_6$ contains
exactly $2r$ squared levels, counted with multiplicity. Say that truncated
localized modes, Gram control, and a complement estimate underlie the result.
Do not print the Feshbach formula, decay constants, complement proof,
$N_{\rm exp}=3120$, or one-G6 finite-ring corollary. The result is explicitly
not used to prove the sharp onset 48. Full exact-$2r$ material
(`T6.4`--`T6.6`, `C.7`) belongs only to the separate reproducibility
supplement.

### 7. Finite Completion of the Classification

#### 7.1. Exact-computation protocol

State the four-step contract: mathematical reduction, finite exact object,
independent machine verification, mathematical consequence. Explain exact
arithmetic and fail-closed acceptance without listing hashes, commands,
test counts, or schemas.

#### 7.2. Orders 8 through 32

State the switching/dihedral exhaustion and its completeness (`C.1`), derive
the universal lower bounds through 30, combine them with candidate attainment
for equality, and give the exact order-32 witness (`T8.1`, `C.2`).

#### 7.3. Orders 34 through 46

Prove soundness, completeness, termination, cyclic closure, and both-holonomy
coverage of the parity-lifted de Bruijn reduction. Report exactly 64 terminal
$(Q,\alpha)$ records and zero unresolved records, obtaining equality at
$34,36,38,42,44,46$ (`T8.2`, `C.3`). Treat the exact $n=40$ witness and
rational $LDL^{\mathsf T}$ consequence separately (`T8.3`, `C.4`).

#### 7.4. The exact bridge from 48 to 238

State the deterministic residue families and the 96 exact rational
positive-definiteness certificates (`C.5`). Prove strict failure for every
even $48\le n<240$. This subsection, together with Section 6.4, establishes
(`T7.3`) and the sharp continuous onset $N_\star=48$.

#### 7.5. Exhaustive synthesis

Partition all even $n\ge8$ into

$$
\{8,10,\ldots,30\},\quad\{32\},\quad
\{34,36,38,42,44,46\},\quad\{40\},
$$

$$
\{48,50,\ldots,238\},\quad\{240,242,244,\ldots\}.
$$

Combine candidate attainment with the finite lower bounds on valid orders
and the explicit strict witnesses on failing orders. Restate the complete
classification (`T8.4`) as the final theorem of the proof.

### 8. Concluding Remarks

Give a short mathematical summary, not a second Introduction. Permit at most
three carefully delimited open questions: classification of minimizing
signings, arbitrary multi-interface competition, and sharper asymptotic
information beyond the proved residue `limsup`. Do not report research-stage
scans or speculate that currently open statements are expected theorems.

## 5. Theorem Placement and Dependency Order

The publication hierarchy is deliberately smaller than the canonical
registry. The paper exposes one headline theorem, one structural hierarchy,
and the propositions/lemmas required to prove them.

1. **Main theorem:** complete even-order classification (`T8.0`, `T8.4`).
   Announced in Section 1 and proved last in Section 7.5.
2. **Supporting theorem:** reference edge (`T2.1`--`T2.3`), Section 2.4.
3. **Supporting theorem:** gap/charge and sector laws (`T3.1`--`T3.3`),
   Section 3.
4. **Supporting theorem:** G6 edge and rank two (`T4.0`--`T4.3`), Section 4.
5. **Supporting theorem:** single-gap hierarchy (`T5.1`, `T5.2`), Section 5.
6. **Lemmas/propositions:** patch identification and IMS cap (`T6.0`--`T6.2`),
   Sections 6.2--6.3.
7. **Supporting theorem:** residue constructions, `limsup`, and eventual tail
   (`T7.1`--`T7.3`), Sections 6.1 and 6.4, completed in Section 7.4.
8. **Overview-only strengthening:** exact-$2r$ count (`T6.3`), Section 6.5;
   it has no outgoing dependency to the main classification.
9. **Computer-assisted lemmas:** (`C.1`--`C.6`, `C.8`) are stated where their
   mathematical consequences are used and proved at the appropriate level in
   Appendices A--B. Their reproducibility payload is separate.

The mathematical dependency order is:

$$
\begin{gathered}
\text{switching and candidate attainment}
\longrightarrow \text{upper direction for all even orders},\\
\text{reference phase}
+\text{charge/sector laws}
\longrightarrow \text{legal G6 constructions},\\
\text{reference edge}
+\text{G6 essential spectrum and matching}
\longrightarrow \text{G6 global edge},\\
\text{G6 edge}+\text{single-gap witnesses}
\longrightarrow \text{single-gap hierarchy},\\
\text{G6 edge}+\text{patch identification}+\text{IMS}
\longrightarrow \text{eventual failure }(n\ge240),\\
\text{finite exact bridge}
\longrightarrow \text{failure for }48\le n<240,\\
\text{candidate attainment}+\text{finite lower bounds}
+\text{all strict witnesses}
\longrightarrow \text{complete classification}.
\end{gathered}
$$

The narrative reveal is different from this dependency order: the
Introduction first gives the surprising complete answer and only then the
structural explanation. No publication figure should depict either map as an
infographic.

## 6. Appendices and Reproducibility Supplement

### Appendix A. Exact spectral certification of the reference phase and G6

Include the period-eight Bloch determinant and endpoint factorization behind
`T2.1`--`T2.2`; then give the complete mathematical certification architecture
for `T4.1`--`T4.3` and `C.6`: degree-ten elimination, rational root isolation,
complete Grassmann-chart coverage, Sturm decisions, unsquared physical
matching, and rank-two symmetry. The appendix must explain why the finite
algebraic object is exhaustive. Hashes, command lines, and tamper tests stay
out.

### Appendix B. Exact finite classification and completeness

Include the mathematical completeness proofs and exact consequence statements
for `C.1`--`C.5` and `C.8`: switching/dihedral coverage, local compression,
parity-lifted de Bruijn soundness and completeness, cyclic closure, both
holonomies, rational positive-definiteness logic, and the exhaustive order
partition. Full certificate payloads do not appear here.

### Separate reproducibility supplement

The supplement contains schemas, manifests, immutable hashes, checker
commands and versions, expected outputs, tamper tests, resource notes, full
integer witness vectors, and machine-readable certificates. It also contains
the full exact-$2r$ package (`T6.4`--`T6.6`, `C.7`), including Gram,
codimension-$2r$ complement, $2r\times2r$ Feshbach, decay constants, and
$N_{\rm exp}=3120$. These materials are removable without changing the main
classification proof.

No optional exact-$2r$ appendix is planned for the first submission. This is
the primary page-control decision.

## 7. Figure Plan: Three Main Figures Maximum

All three figures are black-and-white TikZ vector drawings, legible in
grayscale at ordinary print scale. Mathematical distinctions use solid/dashed
edges, line weight, node fill, and explicit $+$/$-$ labels; none relies on
color. No exact-$2r$ geometry, software pipeline, plot, or proof flowchart is
permitted.

### Figure 1. Edge signings and switching coordinates

**Purpose.** Make the object unambiguous and show how a signing of $C_n^2$
passes to Hamilton gauge, step-two signs $\tau_i$, quadrilateral fluxes
$Q_i=\tau_i\tau_{i+1}$, and holonomy $\alpha$.

**TikZ plan.** Two compact panels: (a) a short cyclic arc with distance-one
and distance-two edges distinguished geometrically and signs shown by
solid/dashed strokes; (b) the same arc in Hamilton gauge with $\tau$, $Q$,
and a single seam/holonomy marker. Use open circular vertices and no shaded
background.

**Caption draft.** “An edge signing of $C_n^2$ and its Hamilton-gauge
coordinates. Solid and dashed edges denote positive and negative signs;
$Q_i=\tau_i\tau_{i+1}$ is switching invariant, while $\alpha$ records the
cyclic Hamilton holonomy.”

### Figure 2. Reference phase and legal G6 residue constructions

**Purpose.** Display the period-eight reference phase, one elementary G6
shift, and the one-, two-, and three-slip rings used for residues 2, 4, and 6
modulo eight. Visually separate global charge closure from local translation
sector shift.

**TikZ plan.** Panel (a) is a linear positive-$Q$ site diagram with reference
gaps 4 and one gap 6. Panels (b)--(d) are small cyclic gap-word diagrams for
one, two, and three slips. A brace below the panels states
$\sum q_j\equiv n\pmod8$; a directed sector arrow local to the interface
states $\sigma_{\rm sec}(q)=q\pmod4$. Use different dash patterns rather than
different colors.

**Caption draft.** “The period-eight reference phase and the legal one-,
two-, and three-G6 constructions. The global ring condition
$\sum_jq_j\equiv n\pmod8$ selects the residue class, whereas the local law
$\sigma_{\rm sec}(q)=q\pmod4$ records the translation-sector change across an
interface.”

### Figure 3. Finite-ring localization and infinite patches

**Purpose.** Make the patch-identification and IMS step readable without
turning it into a proof diagram: every enlarged support sees pure reference
bulk or one oriented G6 model.

**TikZ plan.** A single ring carrying three well-separated marked G6 cores,
with two representative tent supports enlarged by the range-four interaction
radius. Below, align each cut-open support with its bilateral reference or G6
patch. Use thin gray support boundaries, black graph lines, and distinct
solid/dashed interface marks.

**Caption draft.** “Localization on a separated phase-slip ring. After the
range-four enlargement, each tent support is identified with either the
period-eight reference operator or one orientation of the bilateral G6
operator; the separation hypotheses prevent a patch from meeting two
interfaces.”

## 8. Table Plan: One Main Table

Use only one table in the entire main paper; a second table is not currently
authorized. It appears near Section 7.5 and has three columns: even orders,
classification conclusion, and proof mechanism. Its six rows are the
immutable partition

```text
8--30 even                 equality       exact exhaustion + attainment
32                         strict failure exact witness
34,36,38,42,44,46         equality       finite-state closure + attainment
40                         strict failure exact LDL witness
48--238 even               strict failure 96 exact bridge certificates
all even n>=240            strict failure G6 constructions + IMS
```

**Caption draft.** “The complete even-order classification and the logically
distinct mechanisms closing its six parts.”

No certificate hash table, software metadata table, periodic-frontier table,
moment table, or exact-$2r$ constant table appears in the paper. Detailed
machine metadata belongs in the reproducibility supplement.

## 9. Verified Literature Placement

The bibliography is built only from verified metadata in the Task 58 direct
literature matrix. Placement is controlled as follows.

- **Problem and direct predecessor, Introduction paragraphs 2--3:**
  Bilu--Linial; Belardo--Cioaba--Koolen--Wang; Marcus--Spielman--Srivastava;
  Suvagiya's *Signed circulants at the Ramanujan bound*; and, if needed for
  parity context, Suvagiya's companion parity-family preprint.
- **Signed spectral and Fourier context, Sections 2 and 4:** Akbari et al. on
  signed cycles; Reff on gain-cycle spectra; Gavrilyuk et al. for JGT
  switching language; Korotyaev--Saburova for standard periodic-graph Floquet
  machinery. Lieb may be cited only as conceptual flux-minimization
  motivation and never as a theorem applicable to $C_n^2$.
- **Extremal-classification boundary, Introduction paragraph 11:**
  Belardo--Brunetti--Ciampella and Brunetti--Stanic, with the explicit
  distinction that their underlying graphs vary.
- **Computer-assisted proof architecture, Introduction paragraph 10 and
  Section 7.1:** Goedgebeur--Schaudt, DeVos--Samal, Lin--Ning, and
  Goedgebeur--Renders--Wiener--Zamfirescu. Acharya--Jiang may be cited in the
  appendix as a recent spectral classification analogue. These works are
  methodological precedents, not novelty evidence.
- **Internal editorial precedents only:** Fang--Lin--Shi, Zhai--Lin--Shu,
  Kim--Park, and Wigderson need not be cited unless a sentence directly uses
  their mathematical context.
- **Submission watchlist:** recheck the Suda seminar and rerun targeted
  searches for `C_n(1,2)`, `cycle square`, `signed circulant`, and `minimum
  spectral radius` immediately before submission.

All “first” language remains prohibited. The narrow “to the best of our
knowledge” sentence in Introduction paragraph 11 is the strongest permitted
novelty formulation.

## 10. Page Budget and Cut Rules

Target layout at normal article typography:

- Introduction: 4 pages.
- Section 2: 4 pages.
- Section 3: 2 pages.
- Section 4: 5--6 pages.
- Section 5: 3 pages.
- Section 6: 4--5 pages.
- Section 7: 5--6 pages.
- Section 8 plus data/code availability and acknowledgments: 1--2 pages.
- Main narrative target: **28--34 pages**.
- Appendix A: 4--5 pages.
- Appendix B: 4--5 pages.
- Total paper with essential appendices: **at most 45 pages**.
- Reproducibility supplement: counted separately.

If a complete draft exceeds 45 pages, cut in this order:

1. shorten the exact-$2r$ overview to its statement and one interpretive
   paragraph; its proof already lives in the supplement;
2. move every full single-gap integer vector and margin table to the
   supplement;
3. move all schemas, hashes, commands, expected outputs, resource notes, and
   tamper tests to the supplement;
4. compress algebraic-certificate exposition while preserving polynomial,
   isolating interval, finiteness, chart coverage, physical matching, and
   endpoint logic;
5. remove a nonessential contextual citation paragraph before compressing any
   proof.

Never meet the budget by reducing font size, narrowing margins, tightening
line spacing, adding negative vertical space, deleting candidate attainment,
weakening the G6 or single-gap statements, conflating the two congruence laws,
or abbreviating finite-state completeness.

## 11. Locked Deletion List

The following material is omitted from the first-submission manuscript,
appendices, abstract, figures, and tables.

1. `A.1`: full/general moment identities and machinery.
2. `A.2`: the period-eight moment trichotomy.
3. `A.3`: the primitive periodic frontier for `p<=24`.
4. `A.4`: the bounded-support multi-gap census.
5. `A.5`: the arbitrary-length $(3,3)$ local obstruction.
6. `A.6`: the remaining multi-gap finite-alphabet reduction.
7. `C.9`: the finite certificate for the `p<=24` frontier.
8. Period-25/26 read-only scans, the reference graph, interaction fits, and
   exploratory multi-interface asymptotics.
9. General moments not explicitly required by an imported proof.
10. Common-liminf, common-limit, universal finite-core, arbitrary multi-gap,
    and all-period uniqueness programs.
11. Research chronology, correction history, task numbers, review status
    labels, obsolete exact-$r$ claims, and every formula imported from a
    blacklisted or historical-only source.
12. Full exact-$2r$ Gram, complement, Feshbach, decay-constant, and onset
    proofs from the paper itself; these are supplement-only. The main paper
    retains only the scoped exact-$2r$ statement and short overview in
    Section 6.5.
13. JSON excerpts, certificate schemas, hashes, command transcripts, test
    counts, hardware notes, discovery scans, and floating-point evidence.
14. Decorative theorem boxes, footnotes, software diagrams, proof
    flowcharts, color-dependent graphics, and numerical plots.

The omission of `A.1`--`A.6` and `C.9` is unconditional for the first
submission. None may re-enter merely to fill exposition, motivate the
reference phase, or strengthen a novelty claim.

## 12. Gate A Acceptance Conditions

Task 58.3 may begin only after the title, abstract logic, eleven-paragraph
Introduction plan, exactly two Introduction results, eight-section tree,
appendix/supplement split, three-figure ceiling, one-table plan, literature
placement, page budget, and deletion list have been approved together.

The future manuscript must preserve these invariants:

- candidate attainment and finite exhaustion remain distinct;
- the candidate and reference phase remain distinct;
- $m_n$ is compared with $\rho_-(n)$ and $m_n^2$ with $\theta_n$;
- modulo-eight ring closure and modulo-four sector shift remain distinct;
- $c_6$ is a squared edge defined algebraically before use;
- $\dim\ker(H_6-c_6)=2$ and separated interfaces have exact $2r$, not exact
  $r$, local dimension;
- single-gap optimality is not expanded to arbitrary interfaces;
- residue conclusions remain `limsup` only;
- phase-slip theory proves eventual failure, while finite exact verification
  places the continuous onset at 48;
- exact-$2r$ remains an overview-only strengthening and is not a dependency of
  the complete classification.
