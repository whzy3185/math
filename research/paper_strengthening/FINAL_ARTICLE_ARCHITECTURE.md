# Final Article Architecture

> Superseded by `FINAL_ARTICLE_ARCHITECTURE_V2.md` after the JGT authorial
> rewrite.  This file records the pre-rewrite seven-section decision only.

## Section 1. Introduction and Main Results

### 1.1 From switching to fixed-graph spectral optimization

Develop signed graphs and switching as the mature setting.  Distinguish
existence of good signings/two-lifts from exact minimization over signings of a
fixed graph.

### 1.2 Why cycle squares and periodic signings

Explain why `C_n(1,2)` is both Fourier-transparent and locally nontrivial:
overlapping triangles create cycle invariants, while periodic signings restore
cell translation after ordinary circulant symmetry is broken.

### 1.3 Main results

State, in reader-facing order:

1. exact positive-holonomy finite radius and twisted comparison;
2. general half-cell chiral criterion;
3. smallest primitive period and period-eight rigidity;
4. general moment obstruction.

### 1.4 Position in the literature and proof architecture

Integrate switching, signing optimization, circulants, periodic/magnetic graph
operators, and chiral spectral symmetry.  Mention Suvagiya only after the
independent problem and theorems.  End with a concise proof map and the seven
sections.

## Section 2. Switching Coordinates and Periodic Fibers

### 2.1 Signed cycle squares and Hamilton gauge

Define edge signs, switching, triangle flux `tau`, Hamilton holonomy `alpha`,
and the cut-open boundary condition.  Resolve local gauge versus global seam.

### 2.2 Symmetries and primitive period

Prove lift, rotation, reflection, and cell-repetition invariance.  Define
displayed and primitive period before any orbit reduction later in the paper.

### 2.3 Finite Bloch decomposition

Derive the `pL` finite direct sum over `z^L=alpha`, check Hermitian fibers and
dimensions, and record the spectral-radius maximum formula.

## Section 3. Half-Cell Chiral Symmetry

### 3.1 The natural half-cell operator

Motivate the question of zero-symmetric fiber spectra from a signed half-cell
translation; define `D`, `T_m`, and the restricted monomial class.

### 3.2 Anticommutation and flux criterion

Prove the coefficient iff `tau_(i+m)=-tau_i`, its equivalent half-periodic
negative-flux condition on `Q`, and the correct Bloch normalization.

### 3.3 Algebraic consequences

Prove equal chiral dimensions, even characteristic polynomial, and the general
`2m -> m` squared reduction.  Stop before attempting a general spectrum.

## Section 4. The Exact Period-Eight Phase

### 4.1 The target phase and chiral block

Display the word and figure, specialize Section 3, and write the `8 x 8` fiber
and `4 x 4` squared block.

### 4.2 The period-eight polynomial

Give the transparent `4 x 4 -> 2 x 2` determinant identity and derive `P(y,c)`.

### 4.3 Complete dispersion

Center the quartic, derive and order all four squared branches, state endpoint
values, simplicity, and exact gaps.

### 4.4 Finite phase quantization

Derive exact positive and negative holonomy radii from the allowed phase grids.

### 4.5 The twisted comparison

Compute the benchmark by scalar Fourier diagonalization, prove the strict
comparison for `L>=4`, and state the fixed-graph extremal consequence.  The
recent conjecture appears only as a corollary of this result.

## Section 5. First Occurrence and Rigidity

### 5.1 Local squares and moment reduction

Introduce `Q`, `d,a,b`, the first three phase-averaged moments, and the two
necessary inequalities at squared edge eight.

### 5.2 Periods below eight

Use legality and dihedral symmetry to obtain the finite survivor set.  State a
single exact-certificate lemma whose table contains all remaining cases and
the eight Rayleigh vectors.

### 5.3 Rigidity at period eight

Ask whether the first feasible period contains many low-edge phases.  Reuse
the target solution, prove the balanced case, use the compact exact recurrence
for non-antipodal two-defect cases, and close the trichotomy.

### 5.4 Unique first phase

Combine primitive-period minimality and the trichotomy in one synthesis
corollary.

## Section 6. Periodic Defect Obstructions

### 6.1 Arbitrary periodic words

Lift the moment identities from the short-period proof into a general theorem.

### 6.2 Density and clustering consequences

State exactly the two proved necessary inequalities and explain the local
geometry they exclude.  Do not claim sufficiency or classification.

## Section 7. Concluding Remarks

Summarize the mechanism-to-consequence chain in one paragraph.  State one open
problem: determine whether the exact period-eight value is the true fixed-graph
minimum on an infinite subfamily and characterize equality classes.

## Figure and table plan

| item | placement | mathematical purpose | status |
|---|---|---|---|
| Figure 1: period-eight flux cell | Section 1 and referenced in 4.1 | identify cycle square, triangle fluxes, half-cells, antipodal defects | required |
| Figure 2: finite cell decomposition | Section 2.3 | visualize `8L -> L` cells, seam holonomy, and `z^L=alpha` | required if caption remains shorter than prose replacement |
| Figure 3: half-cell chiral mechanism | Section 3.1 | show half translation, alternating signs, and negative half-cell flux | required because it explains the general theorem |
| Table 1: exact short-period closure | Section 5.2 | compress the already-reduced finite cases and exact certificates | required |
| dispersion plot | none initially | exact branches already communicate the result | omitted unless review shows a reading benefit |

## Target length allocation

| component | approximate journal pages |
|---|---:|
| front matter + Introduction | 3.5--4.5 |
| switching and Bloch setup | 2.5--3.5 |
| general chiral theorem | 2--3 |
| exact period-eight phase | 4--5 |
| first occurrence and rigidity | 4--5 |
| general obstruction + conclusion | 2--3 |
| references | 1.5--2 |

Expected total: 20--25 pages.  This is an estimate, not a quota.
