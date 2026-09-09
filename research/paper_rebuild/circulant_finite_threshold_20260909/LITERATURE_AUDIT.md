# Literature audit (updated 2026-09-09)

This audit is deliberately conservative about novelty.  The paper studies a fixed underlying graph

\[
C_N(1,s)
\]

and minimizes spectral radius over **all** edge signatures.  This is not the same problem as studying translation-invariant signed Cayley graphs, nor is it the same as analyzing one prescribed periodic signing.

## 1. The correct broad problem

Francesco Belardo, Sebastian M. Cioabă, Jack H. Koolen and Jianfeng Wang, **Open problems in the spectral theory of signed graphs**, *The Art of Discrete and Applied Mathematics* 1 (2018), #P2.10, DOI `10.26493/2590-9770.1286.d7b`.

Problem 3.18 asks, for a fixed connected graph `G`, for signatures minimizing signed spectral radius.  This is the cleanest general framing for

\[
m(N,s)=\min_\sigma\rho(A_\sigma).
\]

Recommended introduction language:

> We study the fixed-underlying-graph signing problem for the two-step circulants `C_N(1,s)`, seeking exact extrema and switching rigidity rather than optimizing within a prescribed structured family of signatures.

Do **not** write that spectral minimization over signatures is introduced here.

The same literature distinguishes carefully between switching and graph isomorphism.  Our paper should use:

- **labelled switching class**: diagonal `+-1` switching on the fixed labelled graph;
- **switching-isomorphism orbit**: switching followed by a graph automorphism/isomorphism.

This distinction is essential at `(8,3)`, where the flat minimum has six labelled switching classes but one orbit after automorphisms.

Also define explicitly

\[
\rho(A)=\max_i|\lambda_i(A)|,
\]

because a signed adjacency matrix has no Perron--Frobenius reason for its spectral radius to equal its largest eigenvalue.

## 2. The trace floor and weighing matrices

The signed-graph literature records the average-degree lower bound: for average degree `k`, every signature has spectral radius at least `sqrt(k)`, with weighing-matrix equality in the regular case.  For our 4-regular graphs this gives `rho(A)>=2`, and equality is

\[
A^2=4I.
\]

We should still give the one-line trace proof

\[
\operatorname{tr}A^2=4N,
\]

because it is shorter and makes the equality condition immediate.  But the paper must describe the ambient equality phenomenon as established weighing-matrix/two-eigenvalue theory.

## 3. Spectral radius two and two-eigenvalue signed graphs

James McKee and Chris Smyth, **Integer symmetric matrices having all their eigenvalues in the interval `[-2,2]`**, *Journal of Algebra* 317 (2007), 260--290, DOI `10.1016/j.jalgebra.2007.05.019`.

They classify the ambient cyclotomic integer-symmetric/signed-graph phenomenon.  Therefore

\[
m(N,s)=2\iff N=2s+2
\]

is to be advertised as an exact classification **inside the two-step circulant family**, not a general classification of signed graphs with spectral radius two.

Yaoping Hou, Zikai Tang and Dijian Wang, **On signed graphs with just two distinct adjacency eigenvalues**, *Discrete Mathematics* 342 (2019), 111615, DOI `10.1016/j.disc.2019.111615`, gives further direct ambient overlap with `A^2=4I` in maximum degree four.

Zoran Stanić, **Signed Toral Tessellations Whose Spectrum Consists of Exactly Two Symmetric Eigenvalues**, *Discrete Mathematics Letters* 17 (2026), 70--74, revisits the known 4-regular toral-tessellation examples.  We should not identify every flat `C_{2s+2}(1,s)` with a standard named toral tessellation unless the graph-isomorphism identification is checked explicitly.

## 4. The key literature input for the new `sqrt(6)` theorem

Gary Greaves, Jack Koolen, Akihiro Munemasa, Yoshio Sano and Tetsuji Taniguchi, **Edge-signed graphs with smallest eigenvalue greater than `-2`**, *Journal of Combinatorial Theory, Series B* 110 (2015), 90--111, DOI `10.1016/j.jctb.2014.07.006`; arXiv:1309.5178.

This is now the most important external theorem used in the paper.

Their paper classifies connected edge-signed graphs with smallest eigenvalue strictly greater than `-2`.  In particular:

- Theorem 6 classifies the integrally represented cases through tree, unicyclic and one doubled-edge representation graphs;
- Theorem 19 shows that every exceptional class has order `6`, `7`, or `8` (respectively 32, 233 and 1242 switching classes).

Our use is sharply delimited.  Under the hypothesis

\[
\rho(A_\sigma)^2<6,
\]

we first prove internally that the integral defect

\[
B=A_\sigma^2-4I
\]

is exactly a `+-1` signing of a forced 4-regular parity graph.  Therefore `-B` has smallest eigenvalue greater than `-2`.  Greaves et al. are invoked only to rule out large connected 4-regular defect components.  An elementary degree audit of their representation-graph cases then leaves only `K_5`; the exceptional cases are automatically of order at most eight.

Everything after this reduction--orders 5,6,7,8, the cubic `x^3-7x+7`, and the order-14 lifting--is proved explicitly in our paper.

This is the correct way to write the dependency.  Avoid phrases such as “by the classification, our theorem follows”: the circulant-specific defect reduction and liftability are the actual new mathematical work.

### Audit note on the doubled-edge case

The line-graph degree of either parallel edge is

\[
d_H(a)+d_H(b)-3,
\]

not `d_H(a)+d_H(b)-2`, because the other parallel edge would otherwise be counted twice.  Thus 4-regularity gives `d_H(a)+d_H(b)=7`.  This correction has been incorporated into the proof source.

## 5. Current signed-graph reference for terminology

Zoran Stanić, **Spectra of Signed Graphs**, London Mathematical Society Lecture Note Series 504, Cambridge University Press, 2026, DOI `10.1017/9781009853316`.

The book was published online 15 May 2026 and in print in June 2026.  It is a useful current secondary source for:

- balance and switching terminology;
- adjacency spectral conventions;
- signed line graphs and the `-2` boundary;
- signed graphs with few eigenvalues.

Use primary papers for theorem dependence (especially Greaves et al.); use the monograph for modern terminology and context.

## 6. Signatures, 2-lifts and Ramanujan motivation

Noga Bilu and Nathan Linial, **Lifts, discrepancy and nearly optimal spectral gap**, *Combinatorica* 26 (2006), 495--519.

Adam Marcus, Daniel Spielman and Nikhil Srivastava, **Interlacing families I: Bipartite Ramanujan graphs of all degrees**, *Annals of Mathematics* 182 (2015), 307--325.

These papers motivate controlling spectra by signs and lifts.  They do **not** determine

\[
\min_\sigma\rho(A_\sigma)
\]

for a prescribed nonbipartite circulant.  In particular, do not write that MSS supplies a two-sided spectral-radius bound for every fixed graph/signature problem; the quantifiers are different.

## 7. Standard switching reference

Thomas Zaslavsky, **Signed graphs**, *Discrete Applied Mathematics* 4 (1982), 47--74.

The Hamilton-path gauge is standard spanning-tree switching.  We should nevertheless prove its completeness in one sentence because every exact enumeration count depends on it.

## 8. Recent extremal-paper writing models

Useful presentation models include:

- Wang--Dong--Hou--Li, **On signed graphs whose spectral radius does not exceed `sqrt(2+sqrt(5))`**, *Discrete Mathematics* 346 (2023), 113358;
- Wang--Hou--Li, **Extremal results for `C_3^-`-free signed graphs**, *Linear Algebra and its Applications* 681 (2024), 47--65;
- Brunetti--Stanić, **Unbalanced signed graphs with extremal spectral radius or index**, *Computational and Applied Mathematics* 41 (2022), 118;
- Ghorbani--Majidi, **Complete signed graphs with largest maximum or smallest minimum eigenvalue**, *Discrete Mathematics* 347 (2024), 113860.

The stylistic lesson is consistent:

1. define the extremal quantity immediately;
2. state exact inequality and equality/rigidity together;
3. isolate interlacing/reduction lemmas before classifications;
4. distinguish spectral radius from index;
5. keep computational classification in a self-contained lemma/certificate section.

Our manuscript should imitate that theorem-first architecture.

## 9. Signed Cayley/circulant scope

A signed Cayley graph in the literature often requires the **signature itself** to come from group/Cayley data.  Our problem does not: only the underlying graph is circulant, while `sigma` ranges over all edge signatures.

Thus finite Fourier diagonalization is used only after selecting an explicit signing for an upper bound or a finitely reduced equality case.  It is never a reduction of the global minimization domain.

This sentence should appear explicitly in the introduction or preliminaries, because otherwise a reader may incorrectly interpret `m(N,s)` as a translation-invariant optimization.

## 10. Suvagiya 2026

Vaibhav Suvagiya, **Signed circulants at the Ramanujan bound**, arXiv:2607.18334v1 (19 July 2026).

The preprint studies `C_n(1,2)` for even `n`, a quadrilateral/alternating-triangle-flux system, four switching classes inside that system, explicit spectra, and exhaustive enumeration for `n in {8,10,12,14,16,18}`.  It conjectures the twisted value to be the global minimum for all even `n`; the abstract states that the quadrilateral system is inconsistent for odd `n`.

Correct relation to our paper:

- it is recent motivation for fixed-circulant signing questions and flux coordinates;
- it concerns the special step `s=2` and a particular constrained flux system;
- our paper minimizes over all signatures for all admissible `s`;
- our exact results include the complete strict sub-`sqrt(6)` classification, the exact `N=4s` resonance, the universal odd-order `sqrt(6)` floor, and the complete `N=3s` `sqrt(8)` transition.

Do not frame the paper as a counterexample note, and do not claim to settle Suvagiya's all-even `s=2` exact conjecture unless a theorem explicitly does so.

## 11. Revised theorem-first narrative

The previous “flat minimum + gap + resonance” narrative is now too weak.  The introduction should present two threshold scales.

### Threshold I: complete finite spectrum below `sqrt(6)`

Let `beta` be the largest root of `x^3-7x+7`.  The paper proves

```text
m(N,s)^2 < 6 iff

N=2s+2,                         with m^2=4; or
(N,s)=(5,2),(10,3),             with m^2=5; or
N=4s,                           with m^2=4+2 cos(pi/(2s)); or
N=14 and s=3,4,5,               with m^2=4+beta.
```

Every other parameter pair lies at or above `sqrt(6)`.  In particular,

\[
N\ge7\text{ odd}\quad\Longrightarrow\quad m(N,s)\ge\sqrt6
\]

for every admissible step.

This is the strongest opening theorem and should precede the `N=3s` material.

### Threshold II: transition at `sqrt(8)`

- every even order has an explicit finite signing below `sqrt(8)`;
- on `N=3s`,
  \[
  m(3s,s)<\sqrt8\iff s\text{ is even or }s\in\{3,5\};
  \]
- odd `s>=7` obey
  \[
  m(3s,s)^2\ge8+2/139.
  \]

This makes the role of the triangle resonance conceptually cleaner: odd order already forces a `sqrt(6)` floor globally, while the chord triangles on `N=3s` drive an additional phase transition through `sqrt(8)`.

## 12. Suggested abstract/introduction wording

Safe wording:

> For the two-step circulant `C_N(1,s)` we minimize the spectral radius over all edge signatures.  Using the integral two-walk defect `A_sigma^2-4I`, we completely classify the parameter pairs whose minimum lies below `sqrt(6)`, including an exact resonance family and a sporadic order-14 defect class.  As a consequence every odd order at least seven has minimum at least `sqrt(6)`.  At the larger threshold `sqrt(8)`, every even order admits a finite sub-threshold signing, whereas the resonance family `N=3s` exhibits an exact parity transition, with a uniform quantitative obstruction for all odd `s>=7`.

Avoid before final priority checking:

- “first complete classification”;
- “sharpest known”;
- “new signed-line-graph classification”;
- “MSS implies our construction”;
- “all signed Cayley graphs”.

## 13. Novelty boundary after the new theorem

Subject to final primary-source searching, the manuscript can safely describe the following content without a priority adjective:

1. exact trace-floor parameter and switching classification within `C_N(1,s)`;
2. complete classification of every parameter pair with `m(N,s)<sqrt(6)`;
3. exact `N=4s` finite-global extremum and rigidity;
4. the order-14 root `x^3-7x+7` exception and its two minimizing labelled switching classes;
5. universal odd-order `sqrt(6)` lower bound;
6. all-even-order finite sub-`sqrt(8)` construction;
7. exact `N=3s` threshold transition and the uniform odd obstruction;
8. finite-state local-to-global propagation for the odd triangle resonance.

## 14. Journal assessment

The complete sub-`sqrt(6)` theorem materially strengthens the paper because it is no longer organized around a single resonance line.  The package now contains a global finite classification plus a second, sharper threshold transition.

Reasonable targets remain:

- *Journal of Graph Theory*;
- *European Journal of Combinatorics*;
- *Linear Algebra and its Applications*;
- *Electronic Journal of Combinatorics*.

The case for JGT/EJC is now substantially stronger than before.  A JCTB submission would still be ambitious because the `sqrt(8)` negative theorem remains computer-assisted and special to triangle resonance; a conceptual classification at the equality boundary `m^2=6` or a broader odd-`k` `sqrt(8)` theorem would strengthen that case further.