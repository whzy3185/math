# Recommended final architecture

## Editorial configuration

- **Primary narrative:** JGT.
- **Fallback conversion:** LAA without changing the proof kernel.
- **Language:** authoritative English manuscript plus a synchronized Chinese companion draft.
- **Target length:** 24–28 JGT pages, including references.
- **Appendix:** none.
- **Main-text computation:** only the exact finite certificate table needed for periods below eight and the already closed short recurrence needed for the period-eight trichotomy.
- **Supplementary verification:** repository scripts and frozen Lean source; the body contains one factual sentence about their scope.
- **Excluded:** R2/R4/R6/G6, all-even classification, old enumeration,
  old rational-certificate narrative, global minimizer claims, arbitrary
  chiral-involution classification beyond the proved monomial half-cell class.

## Provisional title and abstract content

### Title

Preferred JGT title:

> **A period-eight phase in signed cycle squares with exact spectral radius**

It names the graph object, structural phenomenon, and exact result.  It does not make the paper dependent on a recent conjecture.

### Abstract, five-sentence design

1. Define the fixed-graph problem: vary signs on (C_n(1,2)) and minimize signed adjacency spectral radius.
2. State the exact positive-holonomy period-eight formula for every (L\ge1).
3. State the strict twisted comparison for every (L\ge4).
4. State that period eight is the first legal periodic phase with squared Bloch edge below eight and give the uniqueness qualifier.
5. Name the mechanisms: switching-invariant triangle flux, the general
   half-cell chiral criterion, finite Bloch decomposition, exact block
   reduction, and local moment constraints.

Do not mention (1561/200), Lean, the Suvagiya preprint, “computer-assisted,” or unsolved classifications in the abstract.

## 1. Introduction and main results

### 1.1 Spectral optimization on a fixed signed graph

**Object.** A signing (\sigma:E(G)\to\{\pm1\}), signed adjacency matrix (A_\sigma), and (m(G)=\min_\sigma\rho(A_\sigma)).

**Content.** Distinguish fixed-underlying-graph exact optimization from general existence results for good signings/two-lifts.  Introduce (C_n(1,2)) as the square of a cycle for the range of (n) where this description is simple.

**Function.** Establish the independent problem before any benchmark or recent conjecture.

### 1.2 Why cycle squares are a nontrivial testing ground

**Content.** Ordinary circulant symmetry gives a transparent Fourier benchmark, but arbitrary signings destroy one-site translation.  Overlapping triangles carry switching-invariant local information.  Periodic flux words retain a coarser translation symmetry.

**Transition.** The reader moves naturally from “fixed graph” to “local flux plus periodicity,” which motivates the period-eight phase.

### 1.3 The explicit period-eight phase

Display one fundamental word

\[
\tau_*=(1,1,-1,1,-1,-1,1,-1)
\]

and explain in one sentence that its associated local defect word has two antipodal defects.  Give a small signed-cell figure here, not later.

**Figure 1.** Eight vertices on a circle, step-one edges as the Hamilton skeleton, step-two edges/chords, local triangle-flux labels, and the two antipodal defect sites.  Caption defines the visual sign convention and says switching-equivalent drawings represent the same phase.

### 1.4 Main theorem: exact radius and infinite comparison

State the main theorem in two clauses:

> For every (L\ge1), the positive-holonomy repetition of (\tau_*) on (C_{8L}(1,2)) satisfies
> \[
> \rho(A_{8L,+})^2=4+\sqrt{10+2\sqrt5}.
> \]
> For every (L\ge4), this value is strictly smaller than the spectral radius squared of the twisted signing.

Define the twisted signing directly and mathematically.  Do not yet discuss who conjectured its optimality.

### 1.5 General theorem: negative half-cell flux and chiral symmetry

State the necessary-and-sufficient criterion within the natural monomial
half-cell class, first in `tau` language and then in the gauge-invariant `Q`
language.  State only the dimension-halving consequence here; defer the proof
and normalization scalar to Section 3.

### 1.6 Structural theorem: why period eight

State the combined minimal-period and period-eight-rigidity theorem with every equivalence explicitly named.  Avoid the phrase “unique signing” without qualifiers.

### 1.7 Proof ideas and organization

One paragraph, in dependency order:

1. switching gives ((\tau,\alpha));
2. periodicity gives finite (8\times8) fibers with (z^L=\alpha);
3. negative half-cell flux is equivalent to a natural monomial chiral involution;
4. the period-eight word satisfies this general criterion;
5. its block reduction yields a quartic in (y=\lambda^2);
6. a shift makes all four bands explicit and monotone;
7. moment constraints reduce periods below eight to nine exact certificates.

### 1.8 Relation to earlier work

Use four compact paragraphs:

- signed graphs and switching;
- spectral optimization over signings/two-lifts versus exact fixed-graph optimization;
- periodic and magnetic graph operators;
- the particular recent twisted-optimality conjecture, stated only here.

Suvagiya receives one precise paragraph.  The article's novelty is not described as “correcting” that paper.

## 2. Switching coordinates and finite periodic decomposition

### 2.1 Signed cycle squares and switching

Define vertices modulo (n), step-one signs (s_j), step-two signs (t_j), switching by vertex signs, and spectral conjugacy (A\mapsto DAD).

**Proposition 2.1.** Switching preserves the spectrum.

### 2.2 Triangle fluxes and Hamilton holonomy

Define

\[
\tau_j=s_js_{j+1}t_j,
\qquad
\alpha=\prod_{j=0}^{n-1}s_j.
\]

Explain which data are invariant and what residual lift ambiguity remains.  State a clean gauge-coordinate proposition: on the cut-open lift, step-one couplings are normalized; (\alpha) moves to the seam condition.

### 2.3 Hamilton gauge on the cut-open lift

Write the difference equation/operator in the normalized gauge.  Explicitly state

\[
u_{j+n}=\alpha u_j.
\]

This subsection must eliminate the old ambiguity that “all finite Hamilton edges are positive while their product is negative.”

### 2.4 Periodic cells and the finite Bloch transform

For a word of period (pmid n), divide the ring into (L=n/p) cells.  Diagonalize the unitary cell shift.  Prove the finite direct sum

\[
A_{pL,\alpha}\simeq\bigoplus_{z^L=\alpha}H_\tau(z).
\]

Check dimensions and Hermitian symmetry.  This proof is finite linear algebra; avoid unnecessary direct-integral formalism.

### 2.5 Consequences for spectral radius and multiplicity

State

\[
\rho(A_{pL,\alpha})=max_{z^L=\alpha}\rho(H_\tau(z)).
\]

Record that multiplicities add across fibers.  This is needed later to justify exact finite attainment, not just an upper bound.

**Figure 2.** Ring split into (L) eight-site cells; show the cell shift, seam holonomy (\alpha), and allowed phase condition (z^L=\alpha).

## 3. Half-cell chiral symmetry and the period-eight fiber

### 3.1 The natural monomial half-cell operator

For a general even period `p=2m`, define the alternating diagonal operator
`D`, the half-period translation `T_m`, and `K_m=D T_m` on the periodic lift.
State explicitly that only this natural monomial symmetry class is being
classified.

### 3.2 Necessary and sufficient anticommutation criterion

Compute `(A_tau K_m+K_m A_tau)x` coefficient by coefficient.  Prove the iff

```text
K_m A_tau=-A_tau K_m
  <-> tau_(i+m)=-tau_i for every i.
```

The step-one terms cancel because of `D`; the two step-two coefficients give
necessity directly.

### 3.3 Bloch normalization and the parity of the half-cell

On `x_(i+2m)=z x_i`, prove

```text
(D T_m)^2=(-1)^m z I.
```

Derive—not guess—the normalization

```text
gamma_m(z)^2=(-1)^m z^(-1),
J_z=gamma_m(z)D T_m.
```

Record the even/odd `m` choices and prove that `J_z` is a self-adjoint unitary
involution for `|z|=1`.

### 3.4 Gauge-invariant flux criterion

For `Q_i=tau_i tau_(i+1)`, prove the equivalence

```text
tau_(i+m)=-tau_i
 <-> Q_(i+m)=Q_i and prod_(j=0)^(m-1)Q_j=-1.
```

Use the ratio `r_i=tau_(i+m)/tau_i` for the converse.  This is the conceptual
statement that should be cited later: half-periodic local defects with
negative half-cell flux produce chiral symmetry.

### 3.5 General algebraic consequence

Show that the two eigenspaces of `J_z` both have dimension `m` and that, in an
adapted unitary basis,

```text
H_tau(z) ~ [[0,B(z)^*],[B(z),0]].
```

Conclude spectral symmetry, even characteristic polynomial, and the general
`2m -> m` squared reduction.  Do not investigate the general `m x m` block.

### 3.6 The target word and its (8\times8) Hermitian fiber

Write (H(z)) explicitly.  Check (H(z)^*=H(z)) for (|z|=1).  State the ordering of basis vectors so every later block can be reproduced.

### 3.7 Specialization of the half-period involution

Choose (\xi) with (\xi^2=z) and define (J_z) on the basis.  Verify

\[
J_z^2=I,
\qquad
J_zH(z)=-H(z)J_z.
\]

Do the verification by edge types or four basis-pair identities.  Explain that replacing (\xi) by (-\xi) exchanges the chiral subspaces but does not alter the final polynomial.

### 3.8 The (8\times8\to4\times4) reduction

Choose bases for the (\pm1) eigenspaces of (J_z).  Write

\[
H(z)\sim\begin{pmatrix}0&B(z)\\C(z)&0\end{pmatrix}.
\]

Then

\[
\det(\lambda I-H(z))=\det(\lambda^2I-C(z)B(z)).
\]

Identify this block as the `m=4` specialization of Subsection 3.5; do not
repeat the general argument.

### 3.9 The (4\times4\to2\times2) determinant identity

Display the remaining block symmetry/permutation and the (2\times2) determinant formula.  This subsection must be the human-readable bridge to the polynomial, replacing any opaque “CAS simplification.”

### 3.10 The squared-fiber polynomial

Derive and box

\[
P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38,
\]

where (y=\lambda^2) and (c=z+z^{-1}\in[-2,2]).

State precisely that the squared eigenvalues of the Hermitian fiber are the real nonnegative roots selected by the reduction.

## 4. Exact dispersion and finite spectral radii

### 4.1 Centering the quartic

Set (y=X+4) and derive

\[
P(X+4,c)=X^4-(16+2c)X^2+c^2+19c+38.
\]

Then set (W=X^2).  Show the quadratic discriminant and its two roots.

### 4.2 All four squared branches

Derive and order

```text
y_(sigma,tau)(c)=4+sigma sqrt(8+c+tau sqrt(26-3c)).
```

Then identify the largest branch

\[
r(c)=4+\sqrt{8+c+\sqrt{26-3c}}.
\]

Check the root branch and nonnegativity throughout (c\in[-2,2]).

### 4.3 Strict monotonicity and the unique band edge

Compute

\[
W_+'(c)=1-\frac{3}{2\sqrt{26-3c}}>0.
\]

Conclude that (r(c)) is strictly increasing and has unique maximum at (c=2), equivalently (z=1).  Evaluate

\[
r(2)=4+\sqrt{10+2\sqrt5}=\eta<8.
\]

### 4.4 Positive holonomy: exact finite attainment

Since (z^L=1) includes (z=1), combine the direct sum with the unique edge to prove

\[
\rho(A_{8L,+})^2=\eta
\]

for every (L\ge1).  Mention the simple (\pm\sqrt\eta) eigenvalues of (H(1)) and check the characteristic-polynomial derivative so finite attainment and multiplicity are explicit.

### 4.5 Negative holonomy: exact phase-grid formula

For (z^L=-1), identify

\[
c^-_L=2\cos(\pi/L)
\]

and prove

\[
\rho(A_{8L,-})^2
=4+\sqrt{8+2\cos(\pi/L)+\sqrt{26-6\cos(\pi/L)}}.
\]

Conclude strict inequality below (\eta) for finite (L) and convergence to (\eta).

### 4.6 Optional visual interpretation

**Figure 3, optional.** Plot the exact function (r(c)), with the (\alpha=+1) and (\alpha=-1) sample points for two illustrative values of (L).  Caption must say that monotonicity and all comparisons are proved analytically; the plot is not evidence.

## 5. The twisted benchmark and the infinite family

### 5.1 Definition and Fourier spectrum of the twisted signing

Define the benchmark without historical claims.  Diagonalize it by the ordinary Fourier basis and give the exact finite formula (\rho_-(n)) already proved in the repository.

### 5.2 Exact comparison for (n=8L)

Prove directly

\[
\eta<\rho_-(8L)^2,qquad L\ge4.
\]

Use the cleanest existing analytic monotonicity/algebraic comparison.  The rational separator

\[
\eta<1561/200<\rho_-(8L)^2
\]

may appear as a one-line alternative or remark, not as a section or main certificate.

### 5.3 Consequence for fixed-graph minimization

State only

\[
m(C_{8L}(1,2))\le\sqrt\eta<\rho_-(8L),qquad L\ge4.
\]

Do not change the first inequality to equality.  Then state the conjecture consequence with the exact citation.

### 5.4 Verification scope

One sentence:

> A supplementary Lean development checks the (\alpha=+1) comparison kernel L1–L7; the exact formulas and minimal-period theorem proved here are independently audited by exact symbolic scripts but are not claimed to be Lean-formalized.

No Lean code, theorem names, build logs, or proof-status table in the article.

## 6. Why period eight is distinguished

### 6.1 Local square identity and defect word

Define

\[
Q_i=\tau_i\tau_{i+1},
\]

its legality condition (\prod_iQ_i=1), positive defects, and the squared local operator identity from which the threshold eight emerges.  Explain why (Q), rather than a raw signing, is the natural object for local classification.

### 6.2 Phase-averaged moments through order six

Introduce (M_k) as the phase-averaged trace of the (k)-th power of the squared fiber.  Define (d,a,b) before stating

\[
M_1=4p,
\quad M_2=20p+16d,
\quad M_3=118p+168d+96a+48b.
\]

Give the closed-walk grouping at a conceptual level and enough local counts to make each coefficient checkable.

### 6.3 Necessary inequalities below the edge eight

From (0\le y\le8), derive

\[
M_2\le8M_1,
\qquad M_3\le8M_2,
\]

and hence

\[
d\le3p/4,
\qquad 40d+96a+48b\le42p.
\]

State these as necessary constraints.

### 6.4 Reduction of all periods below eight

Explain legality, dihedral symmetry, and moment filtering.  Display the complete survivor list for (p=1,\ldots,7).  The text should make clear why the list is complete without showing program output.

### 6.5 Nine exact certificates

Give one compact table:

- period;
- (Q)-representative;
- selected phase (z\in\{1,-1,i,e^{i\pi/3}\});
- certificate type (determinant or Rayleigh vector);
- exact negative value.

Put the short vectors either in the same table or directly after it.  They may not be hidden in an appendix because this is part of the theorem proof.

### 6.6 Minimal-period theorem

Synthesize the preceding subsections: balanced all-negative words are repetitions of the alternating period-two phase and have edge eight; every other surviving word has an exact fiber above eight; the target at period eight has edge (\eta<8).

## 7. Rigidity at period eight

### 7.1 Symmetry classes of legal period-eight words

Define translation, reflection, lift ambiguity, and cell repetition precisely.  State the classification domain; do not mention arbitrary finite signings.

### 7.2 Balanced and antipodal two-defect phases

Treat the balanced (=8) class and target (<8) class analytically.  Link the latter back to Sections 3–4 rather than repeating the chiral proof.

### 7.3 Non-antipodal two-defect phases

Present the small exact closed-walk recurrence and its three first-positive excess values.  Explain what positivity proves.  This is the only nontrivial computer-generated finite sequence retained in the main text, and every integer needed for the conclusion is printed.

### 7.4 Remaining legal classes and trichotomy

Use the already closed local/moment argument to show all remaining classes lie above eight.  State the trichotomy:

\[
\text{target}<8,\qquad\text{balanced}=8,\qquad\text{all others}>8.
\]

### 7.5 Unique first-period phase

Combine Section 6 with the trichotomy.  This is the conceptual payoff: period eight is both the first possible period and rigid at the first crossing.

## 8. General periodic defect obstruction

### 8.1 Arbitrary periodic words

Return to a general legal (p)-periodic (Q)-word.  Restate (d,a,b) and the edge functional (R_p(\tau)) without adding new statistics.

### 8.2 Density and clustering constraints

State the two inequalities as a theorem and give immediate corollaries for high defect density and adjacent/next-nearest clustering.  Every corollary must be an algebraic consequence already checked; do not imply forbidden-word completeness.

### 8.3 Interpretation and limit of the method

Explain in positive mathematical terms: a low spectral edge forces defects to be sparse and weakly clustered.  End with one sentence that the inequalities are necessary and leave longer-period sufficiency open.  Do not list abandoned M4/M5 projects.

## 9. Conclusion

### 9.1 What has been proved

One paragraph linking the exact family, minimal period, rigidity, and arbitrary-period obstruction.  Do not repeat every formula.

### 9.2 Remaining mathematical question

Ask one focused question:

> Determine whether (\sqrt\eta) is the actual minimum on (C_{8L}(1,2)) for any infinite subfamily, and characterize the switching classes attaining the minimum.

Do not promise all-even classification or a classification of arbitrary
chiral involutions.

## Theorem dependency DAG

```text
switching conjugacy
  └─> gauge coordinates (tau, alpha)
       ├─> negative half-cell flux criterion
       │    └─> monomial chiral involution
       │         └─> general 2m x 2m -> m x m squared reduction
       ├─> finite p-cell Bloch decomposition
       │    └─> explicit period-8 fiber H(z)
       │         └─> chiral involution J_z
       │              └─> 8x8 -> 4x4 -> 2x2
       │                   └─> P(y,c)
       │                        └─> exact dispersion r(c)
       │                             ├─> exact alpha=+ radius eta
       │                             │    └─> twisted comparison
       │                             └─> exact alpha=- radius
       └─> local defect word Q
            ├─> M1,M2,M3 inequalities
            │    └─> p<8 survivor reduction
            │         └─> nine exact certificates
            │              └─> minimal-period theorem
            └─> period-8 class reduction
                 ├─> target exact edge (reuse r(c))
                 ├─> balanced edge 8
                 └─> short exact recurrence for other classes
                      └─> period-8 trichotomy

minimal-period theorem + period-8 trichotomy
  └─> unique first-period sub-eight phase
```

## Result-to-section ledger

| result | first statement | proof closure | later use |
|---|---|---|---|
| general half-cell chiral criterion | 1.5 brief preview | 3.1–3.5 | 3.7–3.8, period-eight interpretation |
| exact positive radius | 1.4 | 4.4 | 5.2, 7.2 |
| negative radius | 1.4 or 4.5 preview | 4.5 | LAA conversion |
| twisted comparison | 1.4 | 5.2 | 5.3 |
| minimal period | 1.5 | 6.6 | 7.5 |
| period-eight trichotomy | 1.5 | 7.4 | 7.5 |
| moment obstruction | 1.5 brief preview | 8.2, with identities proved 6.2–6.3 | structural interpretation |

## Bilingual drafting protocol

The English text is authoritative.  For every completed English subsection, create the Chinese counterpart immediately with identical theorem labels, equation labels, and citation keys.  Mathematical revisions are first made in English and then synchronized.  The Chinese version is not a freer paraphrase and must not introduce stronger claims.

Recommended eventual files:

```text
manuscript/main_en.tex
manuscript/main_zh.tex
manuscript/sections_en/*.tex
manuscript/sections_zh/*.tex
manuscript/references.bib
manuscript/figures/period8_cell.pdf
manuscript/figures/finite_bloch_cells.pdf
manuscript/figures/dispersion_optional.pdf
```

## Drafting order

The writing order should follow proof risk rather than page order:

1. Sections 2–5, closing the exact main theorem;
2. Sections 6–7, closing minimal-period and rigidity claims;
3. Section 8, trimmed to proven general obstruction;
4. Section 1 after all theorem wording is frozen;
5. Abstract and title;
6. Section 9;
7. Chinese synchronized draft;
8. integrity gate and three-reviewer audit.

This avoids building the introduction around claims that later change during proof exposition.
