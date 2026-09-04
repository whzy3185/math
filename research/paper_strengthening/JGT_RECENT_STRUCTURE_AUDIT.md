# Recent JGT structure and proof-architecture audit

## Purpose and evidence boundary

This audit determines the manuscript architecture from ten full-text papers
published in, or accepted by, the *Journal of Graph Theory* in 2024--2025.
It records structural practice rather than copying prose.  Publisher HTML,
author manuscripts, and arXiv versions were used only where the complete
section and proof structure was accessible.

## Full-text corpus

| paper | JGT data | pages inspected | main sections | structural pattern relevant here |
|---|---|---:|---:|---|
| Fang--Lin--Shi, *Extremal spectral results of planar graphs without vertex-disjoint cycles* | 106 (2024), 496--524, DOI `10.1002/jgt.23084` | 25-page author version | 5 | long introduction with two problem lines; thereafter one proof section per headline theorem; no separate conclusion |
| Guo--Spiro, *New eigenvalue bound for the fractional chromatic number* | 106 (2024), DOI `10.1002/jgt.23071` | 16 | 4 | introduction states theorem and comparisons; a general fiber-partition method is one proof section; technical lemma isolated; final open-problem section |
| Goedgebeur--Renders--Wiener--Zamfirescu, *K2-Hamiltonian graphs: II* | 105 (2024), 580--611, DOI `10.1002/jgt.23057` | 31 | 4 + appendix | constructions and order-classification separated; computation appears after mathematical reduction; certificates and algorithms are disclosed in appendix in the published architecture |
| Horn--Purcilly--Stevens, *Graph curvature and local discrepancy* | 108 (2025), 337--360, DOI `10.1002/jgt.23176` | 17-page author version | 4 | preliminaries immediately follow introduction; general inequality has its own section; graph applications and examples are grouped together; no independent conclusion |
| Lato, *Polynomial characterizations of distance-biregular graphs* | 109 (2025), 282--293, DOI `10.1002/jgt.23227` | 28-page preprint | 7 | preliminaries followed by a sequence of characterization/application sections; general tools are separated only when reused materially |
| Billig, *Eigenvalue approach to dense clusters in hypergraphs* | 109 (2025), 353--365, DOI `10.1002/jgt.23218` | complete publisher HTML | 7 | introduces a matrix tool only after the graph optimization problem; theory, duality, algorithm, and spectral application each receive one coherent section |
| Steinerberger--Thomas, *Conformally rigid graphs* | 109 (2025), 366--386, DOI `10.1002/jgt.23229` | 31-page preprint | 6 | extended motivation and related work; main-results section; general certificate machinery; family applications and proof sections; computation presented as exact SDP certificates |
| Li--Feng--Peng, *A spectral Erdős--Faudree--Rousseau theorem* | 110 (2025), 408--425, DOI `10.1002/jgt.23280` | 32-page preprint | 7 | introduction leads to main-results/approach section; preliminaries precede the general method; headline theorems receive separate proof sections; concluding problems |
| Li--Zhao--Zou, *Spectral extrema of graphs with fixed size: forbidden a fan graph, a friendship graph, or a theta graph* | 110 (2025), 483--495, DOI `10.1002/jgt.23287` | 22-page preprint | 5 | introduction states several exact extrema; preliminaries; one structural characterization section; one proof-synthesis section; short concluding remarks |
| Albrechtsen--Jacobs--Knappe--Pitz, *Counterexamples regarding linked and lean tree-decompositions of infinite graphs* | 110 (2025), 398--407, DOI `10.1002/jgt.23279` | 18-page preprint | 5 | problem sequence in the introduction; preliminaries; related counterexamples grouped into two proof sections; final structural extension rather than a generic conclusion |

## Corpus answers to the requested questions

### Number of sections

The observed range is four to seven main sections.  The median architecture is
about five sections, with seven used when the theorem package genuinely
contains several reusable layers.  A nine-section paper is possible but would
make the present package look more fragmented than comparable JGT work.

### What follows the introduction

Six of the ten papers move immediately to preliminaries, setup, or a compact
main-results section.  None inserts a detached literature-review chapter.
Related work is concentrated inside the introduction near the problem it
supports.

### General lemma versus application

A general tool receives its own section when it either:

1. produces several consequences; or
2. explains the structural mechanism of the headline theorem.

Guo--Spiro, Horn--Purcilly--Stevens, Billig, Steinerberger--Thomas, and
Li--Feng--Peng all use this pattern.  The half-cell chiral criterion qualifies:
it is an iff in a general even period, gives dimension halving for every
admissible word, and explains the period-eight reduction.  It should therefore
be a section, not a lemma hidden inside an eight-site calculation.

### Shape of a complete proof arc

The recurring pattern is

```text
problem-specific coordinates
 -> structural reduction
 -> exact inequality/calculation
 -> equality or exceptional-case analysis
 -> stated graph consequence.
```

The articles do not interrupt a proof arc with broad discussion.  Secondary
results are grouped with the mechanism that proves them.

### Structural theorem versus exact computation

When the structural result is reusable, it precedes the special computation.
When the calculation only evaluates a candidate, it stays inside the candidate
section.  For the present paper this means:

- general half-cell chiral symmetry is Section 3;
- the period-eight polynomial, four bands, finite phase grids, and twisted
  comparison form one Section 4;
- minimal-period and period-eight uniqueness form one Section 5.

### Finite and computational cases

The closest computational exemplar is *K2-Hamiltonian graphs: II*.  It first
proves structural reductions and describes the finite domain, then reports
counts/certificates; the algorithm is not allowed to substitute for the
mathematical contract.  The counterexample and spectral-extremal papers also
name the remaining configurations before checking them.

The appropriate presentation here is:

```text
moment inequalities
 -> legality and dihedral quotient
 -> a named finite survivor lemma
 -> one compact exact-certificate table
 -> minimal-period theorem.
```

The table is part of the proof of the survivor lemma.  It is not introduced as
computer evidence.  The eight short Rayleigh vectors should be printed because
they make the rows independently checkable; the `p=3` determinant is written
in prose.  The period-eight recurrence is stated as a compact exact lemma with
the three required positive values, not as a data table or search report.

### Conclusion, figures, and tables

Five papers contain a concluding/open-problem section and five close with the
last application/proof.  A short concluding section is justified here because
the paper joins two mechanisms and leaves one precise fixed-graph minimization
question.

Figures appear only when they encode a construction, configuration, or
geometric interpretation.  Tables compress exact finite classes or enumerative
outcomes after the reduction has been established.  This supports three
structural vector figures and one certificate table; a dispersion plot is
optional and presently omitted because the complete formula is clearer.

## Proof-architecture extraction from the closest papers

| exemplar | reusable organizational lesson | application here |
|---|---|---|
| Guo--Spiro | state the graph consequence early, then isolate the general spectral mechanism | exact finite theorem appears before the chiral proof; chiral criterion remains an independent section |
| Horn--Purcilly--Stevens | general local analytic inequality followed by graph applications | general flux criterion first, period-eight exact application second |
| Fang--Lin--Shi | one uninterrupted proof section per headline theorem | keep exact period-eight dispersion and finite comparison in one arc |
| Li--Feng--Peng | state approach before technical preliminaries and use one general method for several consequences | Introduction explains the chiral/moment division before setup |
| Li--Zhao--Zou | structural reduction before final exact extremal synthesis | moment and orbit reductions precede finite certificates |
| Goedgebeur et al. | finite verification is credible only after completeness and symmetry reduction are explicit | define survivor set and exact verification rule before the certificate table |
| Steinerberger--Thomas | an exact certificate can be a theorem-bearing mathematical object when its meaning and verification are exposed | certificate rows are human-checkable algebra, not screenshots or code output |
| Albrechtsen et al. | a counterexample paper gains depth by grouping constructions around the limits of one structural principle | twisted conjecture remains a corollary; the article is organized around the flux mechanism |

## Final architecture decision

Use seven main sections:

1. Introduction and Main Results
2. Switching Coordinates and Periodic Fibers
3. Half-Cell Chiral Symmetry
4. The Exact Period-Eight Phase
5. First Occurrence and Rigidity
6. Periodic Defect Obstructions
7. Concluding Remarks

This is the smallest section count that preserves three independent proof
arcs: general chiral structure, exact period-eight solution, and first-period
rigidity.  It follows the upper end of recent JGT practice without splitting
secondary results into artificial sections.
