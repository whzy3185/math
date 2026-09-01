# Manuscript Architecture Plan

This is a design document only. It does not modify any manuscript source.

## Proposed sections

### 1. Introduction

**Purpose:** state fixed-graph signed spectral-radius minimization, Suvagiya's conjecture, the all-even truth set, and the proof split.

**Inputs:** none.

**Outputs:** main classification theorem; brief roadmap.

**Model:** Lin--Ning for early complete theorem, Brunetti--Stanić for exact optimization domain.

### 2. Signed cycle squares, switching, and the twisted benchmark

**Purpose:** define `C_n(1,2)`, `m_n`, switching, `Q,tau,alpha`, and prove the twisted spectral formula.

**Inputs:** switching formalism.

**New result:** twisted benchmark proposition `rho_-(n)^2=4+2cos(2pi/n)+2cos(4pi/n)`.

**Output used by:** every later comparison and all finite certificates.

**Supplement material:** routine coordinate conversion tables.

**Model:** Brunetti--Stanić.

### 3. The period-eight reference phase and sector charge

**Purpose:** introduce the reference bulk only after the benchmark is fixed; derive the finite fiber polynomial and exact bulk edge; define sector charge precisely.

**Inputs:** Section 2 notation.

**New results:** reference bulk theorem and charge-additivity lemma.

**Output used by:** G6 theorem and residue constructions.

**Supplement material:** full symbolic fiber expansion and Sturm data.

**Model:** Korotyaev--Saburova.

### 4. The six-gap spectral mechanism

**Purpose:** state and prove the exact G6 interface theorem, including root selection, global edge, rank-two squared multiplicity, and localization. State the abnormal single-gap theorem only in its proved scope.

**Inputs:** Section 3 bulk and charge.

**New results:** G6 edge/localization theorem; optional single-gap corollary.

**Output used by:** analytic tail.

**Supplement material:** transfer matrices, resultants, cofactor charts, rational isolation data.

**Model:** Hu--Liu's technical-mechanism-to-application hierarchy.

### 5. Localized defects on large even cycles

**Purpose:** construct legal finite cycles, identify G6 patches, prove the discrete IMS estimate, and deduce a strict witness for every even `n>=240`.

**Inputs:** Sections 3--4.

**New result:** analytic-tail theorem.

**Output used by:** complete classification.

**Supplement material:** cutoff constants and residue geometry ledger.

**Model:** Korotyaev--Saburova's derive-then-use flow.

### 6. Exact finite failures and universal optimality at the remaining orders

**Purpose:** first give the easy existential LDL witness theorem (`32`, `40`, and `48<=n<240`); then separately give the universal equality machinery for `8..30` and `34,36,38,42,44,46`.

**Inputs:** benchmark from Section 2.

**New results:** finite failure theorem, finite reduction/completeness theorem, small/recovered equality theorem.

**Output used by:** final synthesis.

**Supplement material:** raw signings, LDL pivots, local window tables, terminal words, hashes, commands.

**Model:** Goedgebeur--Schaudt for coverage before computation; Lin--Ning for finite completion.

### 7. Completion of the classification

**Purpose:** partition all even `n>=8` into the disjoint ranges, prove the main theorem in one short synthesis, and state scope limits.

**Inputs:** Sections 5--6.

**New result:** complete classification theorem.

**Output used by:** discussion only.

**Model:** Lin--Ning.

### 8. Discussion and open problems

**Purpose:** state only genuine next questions: wider finite-core optimality, residue limits, and interface interactions.

**Inputs:** scope limits from Section 7.

**Output:** none.

**Exclude:** numerical discovery history, period-25/26 read-only search, and all unproved physical hierarchy claims.

## Future introduction function map

`P1` fixed-graph signed spectral minimization; `P2` cycle-square/non-bipartite setting; `P3` Suvagiya conjecture; `P4` complete classification theorem; `P5` nonmonotone fail/recover pattern; `P6` period-eight/G6 mechanism; `P7` analytic-plus-exact-finite proof architecture; `P8` section roadmap. No prose is drafted here.

## Compression decision

Every proposed section has one of `DEFINE`, `REDUCE`, `PROVE`, `CERTIFY`, or `SYNTHESIZE` as its primary job. There is no research-diary section and no defensive-computation section. If Section 8 grows beyond genuinely open problems, the material should be deleted rather than moved into the proof line.
