# Detailed JGT writing plan: the period-eight analytic counterexample paper

## Editorial target

**Article type:** compact theoretical graph/spectral analysis.  
**Primary venue:** *Journal of Graph Theory*.  
**Working length:** 6,800--7,600 words excluding references, with a 180--220
word abstract.  
**Article claim:** the twisted-optimality conjecture for the fixed graph family
`C_n(1,2)` fails on every `n=8L`, `L>=4`, through an explicit period-eight
signing and a fully analytic comparison.

The main theorem is proved before any structural extension.  The trichotomy
and moment section remain short explanatory results, not a second paper or a
classification programme.

## Front matter

### Title candidates

Choose one after the direct-predecessor wording has been verified:

1. **A period-eight counterexample family for signed spectral-radius minimization**
2. **Chiral period-eight signings beat the twisted circulant benchmark**
3. **An analytic counterexample family to twisted spectral-radius optimality**

Avoid “smallest,” “complete classification,” “all even,” “Ramanujan,” or a
claim of global minimization in the title.

### Abstract (180--220 words)

Required sentence order:

1. State the fixed underlying graph and signed spectral-radius minimization
   problem.
2. Attribute the twisted candidate/conjecture to the verified predecessor.
3. State the theorem: an explicit alpha = +1 period-eight signing on every
   `C_(8L)(1,2)`, `L>=4`, has smaller spectral radius.
4. State the mechanism in one sentence: finite Bloch fibers, chiral reduction,
   and a uniform polynomial certificate.
5. State the exact comparison threshold `1561/200` and the twisted squared
   benchmark, only if notation remains readable in the abstract.
6. State the boundary: this disproves the conjectural universal optimality but
   does not solve global minimization over all signings.

Do not mention Lean, enumeration, low-order tests, the recurrence, or any
excluded residue family in the abstract.

### Keywords

Use five or six: signed graphs; spectral radius; circulant graphs; Floquet
theory; magnetic graph operators; graph signing.

## 1. Introduction and main theorem (850--1,000 words)

### 1.1 The fixed-graph signing problem

**Purpose:** define the problem in one paragraph and establish why a fixed
underlying graph changes the question from generic signing existence to a
specific spectral optimization problem.

**Content to show:**

- Define `G_n=C_n(1,2)`.
- Define a signing and the adjacency spectral radius.
- Say switching preserves the spectrum; defer the gauge proof to Section 2.
- Use one or two verified references for signed spectral context only.

**Do not show:** Bilu--Linial history beyond one sentence, generic Ramanujan
background, numerical searches, or a broad survey.

### 1.2 The twisted candidate and the conjecture

**Purpose:** state exactly the prior claim that the article overturns.

**Content to show:**

- Credit Suvagiya's verified preprint for the candidate and conjecture.
- Define the notation `rho_-(n)` for the twisted benchmark.
- State the conjecture in its original universal form only after direct
  verification of its wording and numbering.

**Do not show:** claims that the present work introduced the graph, the
candidate, flux coordinates, or the twisted Fourier formula.

### 1.3 Main theorem and consequence

**Purpose:** give the reader the exact corrected mathematical statement.

**Display:**

```text
Theorem 1.1. For every L>=4, there is an explicit alpha=+1 signing A_L of
C_(8L)(1,2) such that

rho(A_L)^2 < 1561/200 < rho_-(8L)^2.
```

Immediately state the consequence: the twisted signing is not spectrally
optimal for every multiple of eight at least 32. Then state the exact scope:
no global minimum, no all-even conclusion, and no minimizer classification.

### 1.4 Proof mechanism and article map

**Purpose:** give one compact roadmap.

**Content:** gauge coordinates -> finite fibers -> chiral reduction -> positive
polynomial -> benchmark. Mention that Sections 6--7 explain the local
period-eight mechanism but are not used to prove Theorem 1.1.

**Transition:** “We begin by putting the finite signing problem into cell
coordinates.”

## 2. Gauge coordinates and finite Bloch decomposition (950--1,100 words)

### 2.1 Switching and Hamilton gauge

**Purpose:** fix the only coordinate system used later.

**Definitions and display:**

- Step-one edges and step-two edges of `C_n(1,2)`.
- Hamilton gauge: all step-one signs are `+1`; step-two signs are `tau_i`.
- Residual Hamilton holonomy `alpha`.
- The periodic-lift operator

```text
(A_tau x)_i=x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i x_(i+2).
```

**Proof content:** a short switching lemma or a compact proof paragraph that
the gauge realization represents the desired signing class.

**Do not show:** the full cycle-space dimension discussion unless it is needed
to state the predecessor faithfully.

### 2.2 Finite cells and allowed phases

**Purpose:** make finite and infinite spectral statements visibly distinct.

**Content and display:** for period `p` and `n=pL`, write `i=pm+r` and impose
the finite relation `x_(i+n)=alpha x_i`. Derive

```text
x_(pm+r)=z^m v_r,       z^L=alpha.
```

State that the finite matrix is a direct sum over these allowed phases. State
separately that the infinite periodic operator is parameterized by `|z|=1`.

**Transition:** specialize the construction to the selected eight-site word.

### 2.3 The selected period-eight phase

**Purpose:** state the construction once, before its analysis.

**Display:**

```text
tau=(1,1,-1,1,-1,-1,1,-1).
```

State that the main theorem uses alpha = +1. The analytic fiber discussion may
retain `alpha` until the finite comparison, but the Lean verification statement
must remain alpha = +1.

## 3. The chiral period-eight fiber (1,350--1,550 words)

### 3.1 The eight-site fiber

**Purpose:** place the complete explicit object before any reduction.

**Display:** the full Hermitian `8 by 8` matrix `H(z)` with all `z` and
`z^{-1}` entries.

**Required check before final draft:** human line audit of every entry against
the Hamilton-gauge transition rule.

### 3.2 Chiral involution

**Purpose:** give the structural reason for the reduction.

**Content:** choose `xi` with `xi^2=z`; define the signed four-site shift
`J_z`; prove or verify in a compact calculation

```text
J_z^2=I,       J_z H(z)=-H(z)J_z.
```

Explain the immediate spectral symmetry about zero.

### 3.3 The off-diagonal reduction

**Purpose:** pass from `H(z)` to a four-dimensional squared block.

**Content:** choose the plus/minus basis of `J_z`, write

```text
H(z)=[[0,B],[C,0]],
```

and state that squared eigenvalues are eigenvalues of `BC`.

### 3.4 The two-by-two determinant

**Purpose:** obtain the single polynomial used in the proof.

**Display:** the matrices `Q` and `R`, then

```text
det(yI_4-BC)=det(((y-4)^2-s^2)I_2-RQ)=P(y,c),
```

with `s=xi+xi^{-1}` and `c=z+z^{-1}`. Expand `P(y,c)` in full.

### 3.5 Exact fiber edge

**Purpose:** record the sharper intrinsic period-eight value without making it
the finite-ring comparison threshold.

**Display:** factorization of `P(y,2)` and

```text
eta=4+sqrt(10+2sqrt(5)).
```

State the monotonicity in `c` used to identify this infinite-volume edge.

**Transition:** the finite theorem needs a rational uniform certificate rather
than the exact radical edge.

## 4. Uniform polynomial certificate (800--950 words)

### 4.1 Monotonicity in the phase parameter

**Purpose:** reduce all allowed phase parameters to `c=2`.

**Display:** `partial_c P(y,c)` and the elementary inequality proving it is
negative for `y>=1561/200` and `-2<=c<=2`.

### 4.2 The positive expansion

**Purpose:** make the strict bound transparent and fully analytic.

**Display in full:**

```text
P(1561/200+u,2)
 =u^4+(761/50)u^3+(1337363/20000)u^2
  +(136311081/2000000)u+84332641/1600000000.
```

Explain in two sentences why positive coefficients prove strict positivity for
all `u>=0`.

### 4.3 Finite-fiber corollary

**Purpose:** translate the polynomial statement into the strict fiber bound.

State that every squared fiber eigenvalue is less than `1561/200`. This is the
only conclusion needed from the chiral calculation in Section 5.

## 5. The infinite counterexample family (900--1,050 words)

### 5.1 The twisted shifted-grid calculation

**Purpose:** derive the benchmark rather than merely quote it.

**Content:** state the anti-periodic gauge, the two-dimensional Fourier block,
and the scalar function

```text
g(t)=cos(t)^2+cos(2t)^2.
```

Show the two elementary maximization facts: monotonicity on the initial
interval and the bound `g<=1` on the remaining interval.

### 5.2 The finite benchmark formula

**Display:**

```text
rho_-(8L)^2=4+2 cos(pi/(4L))+2 cos(pi/(2L)).
```

State why the first shifted-grid phase yields this value.

### 5.3 Strict comparison and proof of Theorem 1.1

**Content:** prove the lower bound at `L=4` by the exact radical/Taylor route,
then extend by monotonicity in `L`. Combine with Section 4 in one short proof.

### 5.4 Supplementary formal verification

**One paragraph only:** the finite alpha = +1 theorem kernel was independently
checked in Lean in Hermitian eigenvalue form. Give repository revision only at
the final preprint stage. State exactly what the check covers and does not
cover. Do not describe implementation, DFT internals, or code architecture.

## 6. Why period eight is distinguished (850--1,000 words)

### 6.1 The local square identity

**Purpose:** explain the cancellation mechanism behind the selected word.

**Display:** the local displacement row of `A_tau^2`, or a compact equivalent
table. Highlight the factor `1+Q_i` in odd couplings.

### 6.2 The period-eight trichotomy

**Purpose:** state the structural strengthening precisely.

**Theorem statement:** among legal period-eight flux phases, the antipodal
two-defect phase is the unique phase below squared edge eight, the balanced
phase is at eight, and all remaining phases are above eight, subject to the
exact symmetry convention stated in the proof.

### 6.3 The three finite recurrence cases

**Purpose:** discharge only the three configurations not removed by symbolic
arguments.

**Display:** the recurrence and the three values

```text
E_4=5504,   E_6=64336,   E_9=2872096.
```

Do not display the long intermediate table unless referees ask for it. The
caption/prose must call this an exact integer recurrence, never a computer
search or numerical certificate.

## 7. General periodic defect obstruction (650--800 words)

### 7.1 Phase-averaged moments

**Display:**

```text
M_1=4p,
M_2=20p+16d,
M_3=118p+168d+96a+48b.
```

Define `d`, `a`, and `b` immediately before the display.

### 7.2 Consequences below the eight barrier

**Display:**

```text
d<=3p/4,
40d+96a+48b<=42p.
```

Give the two-line argument `M_(k+1)<=8M_k`. State exactly that the results are
necessary conditions and do not classify all periodic phases.

### 7.3 Relation to the period-eight phase

**Purpose:** close the structural arc without duplicating Section 6.

Explain that Section 6 is a sharp period-eight application of these local
constraints, while the main counterexample theorem did not rely on this
section.

## 8. Conclusion and scope (250--350 words)

### 8.1 What is proved

Restate the infinite period-eight counterexample family and the analytic
mechanism in direct language.

### 8.2 What remains open

Name only two open directions: global minimization over arbitrary signings and
the behavior outside the multiple-of-eight family. Do not list abandoned
repository programmes.

## Figures and tables

### Figure 1. The eight-site quotient cell (recommended)

**Content:** an eight-vertex cyclic cell labelled `0,...,7`; solid edges for
step one; signed step-two edges labelled by the period-eight word; arrows or
light boundary marks for the transitions crossing into the next cell.

**Use:** placed in Section 2.3 or at the start of Section 3. It gives the
reader a visual map for the fiber entries and the four-site chiral shift.

**Style:** black/white with one restrained accent color if required. It must
remain legible when printed in grayscale. It is explanatory only, never part
of a proof.

### Figure 2. Chiral pairing schematic (optional; include only if Figure 1
cannot communicate it)

**Content:** a bipartite block diagram with the four plus and four minus
chiral coordinates, showing `H=[[0,B],[C,0]]` and `H^2` reducing to `BC`.

**Use:** Section 3.2. This should be a diagram, not a numerical band plot.

**Decision rule:** omit it if the displayed basis transformation makes the
same point more economically.

### Table 1. Exact recurrence excesses (required if Section 6 is retained)

| non-antipodal separation | first positive index | exact excess |
|---:|---:|---:|
| 1 | 4 | 5504 |
| 2 | 6 | 64336 |
| 3 | 9 | 2872096 |

This table replaces long computation logs. The recurrence defining it appears
immediately above it.

### No numerical spectral plots

Do not include a band plot, numerical eigenvalue scatter plot, enumeration
histogram, runtime chart, certificate diagram, or a screenshot of Lean. None
is needed for the proof, and each would dilute the JGT mechanism-paper story.

## Evidence and source map

| Section | Mathematical source | Literature source need |
|---|---|---|
| 1 | main theorem kernel | Suvagiya direct predecessor; one signed-spectrum context source |
| 2 | Hamilton gauge and finite Bloch proof | Zaslavsky only if switching terminology needs attribution |
| 3--4 | period-eight analytic package | Korotyaev--Saburova for general periodic fiber/trace context only |
| 5 | twisted benchmark derivation | Suvagiya for candidate attribution |
| 6 | trichotomy and exact recurrence | no external result supports the theorem |
| 7 | general moment obstruction | Korotyaev--Saburova optional for trace-moment context |

## Draft quality gates

Before a full draft is called ready for internal review:

1. Human line-check the eight-by-eight fiber, chiral basis, and determinant.
2. Verify every reference against the source actually cited.
3. Apply the writing-quality check: remove throat-clearing prose, limit em
   dashes, use consistent notation, and retain only claims supported by a
   displayed proof or a verified source.
4. Confirm that no sentence asserts a global minimum, all-even theorem,
   smallest counterexample, or alpha = -1 Lean coverage.
