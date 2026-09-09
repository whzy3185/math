# Literature audit (2026-09-09)

This note records external public literature relevant to the finite-global extremal problem. It is intentionally conservative about novelty and distinguishes a fixed underlying graph with arbitrary signatures from the more restrictive notion of a translation-invariant signed Cayley graph.

## 1. The natural general problem: minimize over signatures of a fixed graph

Francesco Belardo, Sebastian M. Cioabă, Jack H. Koolen and Jianfeng Wang, **Open problems in the spectral theory of signed graphs**, *The Art of Discrete and Applied Mathematics* 1 (2018), #P2.10, DOI 10.26493/2590-9770.1286.d7b.

Problem 3.18 asks, for a fixed simple connected graph `G`, to determine the signature(s) minimizing the signed spectral radius. This is the cleanest broad framing for the present quantity

`m(N,s)=min_sigma rho(C_N(1,s),sigma)`.

The introduction should therefore present this paper as an exact/family-specific study of that fixed-underlying-graph optimization problem, not primarily as a response to one recent preprint.

The same survey makes two writing distinctions that should be copied carefully:

- **switching equivalence** means changing signs by a diagonal `+-1` switching matrix;
- **switching isomorphism** additionally allows a vertex permutation / graph isomorphism.

This matters for our flat equality classification: at `(8,3)` there are six labelled switching classes but one orbit after graph automorphisms.

The survey also stresses that for signed graphs the spectral radius need not equal the largest eigenvalue; Perron--Frobenius does not apply to the signed adjacency matrix. In the manuscript, `rho(A)=max |lambda_i(A)|` must be defined explicitly before any use of `lambda_max`.

## 2. Average-degree lower bound and weighing-matrix equality

The Belardo--Cioabă--Koolen--Wang survey records Gregory's theorem: if a signed graph has average degree `k`, then every signature has spectral radius at least `sqrt(k)`, with equality exactly when the underlying graph is `k`-regular and the signed adjacency matrix is a symmetric weighing matrix of weight `k`.

For our 4-regular circulants this immediately gives `rho(A_sigma)>=2`, and equality means `A_sigma^2=4I`. We may still give the one-line trace proof because it is elementary and because our contribution is the exact parameter/signature classification within `C_N(1,s)`, not the general lower bound itself.

This also means that the phrases "flat signing", "orthogonal signing", or "weighing-matrix equality" should be connected explicitly to established weighing-matrix language.

## 3. Spectral radius two, cyclotomic signed graphs, and toral tessellations

James McKee and Chris Smyth, **Integer symmetric matrices having all their eigenvalues in the interval [-2,2]**, *Journal of Algebra* 317 (2007), 260--290, DOI 10.1016/j.jalgebra.2007.05.019; arXiv:0705.3599.

They classify integer symmetric matrices, including signed graphs, whose spectra lie in `[-2,2]`. Their maximal cyclotomic signed graphs include the infinite 4-regular toral tessellation family `T_{2k}` with spectrum `{+-2}`. Therefore our theorem

`m(N,s)=2 iff N=2s+2`

must be advertised only as an exact classification *inside the two-step circulant family*, together with its direct arithmetic proof and its labelled switching rigidity. We do not claim the general spectral-radius-two theory or the existence of 4-regular `A^2=4I` signings.

Yaoping Hou, Zikai Tang and Dijian Wang, **On signed graphs with just two distinct adjacency eigenvalues**, *Discrete Mathematics* 342 (2019), 111615, DOI 10.1016/j.disc.2019.111615, completely characterize connected signed graphs of maximum degree at most 4 having two adjacency eigenvalues. This is direct ambient overlap with our equality equation `A^2=4I` and must be cited in the flat section.

Zoran Stanić, **Signed Toral Tessellations Whose Spectrum Consists of Exactly Two Symmetric Eigenvalues**, *Discrete Mathematics Letters* 17 (2026), 70--74, DOI 10.47443/dml.2025.225, revisits the known 4-regular toral tessellations and generalizes their repeating-pattern construction. The paper explicitly notes `A(T_{2k})^2=4I` and develops block conditions for larger repeating patterns.

**Outstanding identification check.** Before submission, do not state without proof that every flat `C_{2s+2}(1,s)` signing is literally one of the standard drawn `T_{2k}` toral tessellations. The external literature establishes that our equality signings live inside the known degree-4/two-eigenvalue classification, but the exact graph-isomorphism identification with the conventional `T_{2k}` notation should be verified from the published drawing/definition. The safe statement is that the ambient `A^2=4I` phenomenon is established, while our contribution is the exact step-circulant parameter criterion and switching-class accounting.

## 4. Signings, 2-lifts, and Ramanujan background

Noga Bilu and Nathan Linial, **Lifts, discrepancy and nearly optimal spectral gap**, *Combinatorica* 26 (2006), 495--519, DOI 10.1007/s00493-006-0029-7.

Adam Marcus, Daniel Spielman and Nikhil Srivastava, **Interlacing families I: Bipartite Ramanujan graphs of all degrees**, *Annals of Mathematics* 182 (2015), 307--325, DOI 10.4007/annals.2015.182.1.7.

These works motivate spectral control by signatures and 2-lifts. The manuscript must be precise about the quantifier and about one-sided versus two-sided control: the MSS signing theorem controls the largest new eigenvalue in general, while the bipartite setting supplies spectral symmetry and hence the Ramanujan two-sided conclusion. It does not determine `min_sigma rho(A_sigma)` for a fixed nonbipartite step circulant.

Thus write these references as conceptual background, not as a black box for any theorem here.

## 5. Standard switching reference

Thomas Zaslavsky, **Signed graphs**, *Discrete Applied Mathematics* 4 (1982), 47--74, DOI 10.1016/0166-218X(82)90033-6.

Use this as a primary signed-graph reference for balance/switching. The spanning-tree normalization used in our Hamilton gauge is standard: on a connected graph, switching can prescribe the signs on a fixed spanning tree. We nevertheless prove the particular Hamilton-path normalization in one sentence so that all finite enumeration counts are visibly complete.

## 6. Recent extremal signed-graph writing models

Several papers are useful less for theorem overlap than for presentation style.

- Dijian Wang, Wenkuan Dong, Yaoping Hou and Deqiong Li, **On signed graphs whose spectral radius does not exceed `sqrt(2+sqrt(5))`**, *Discrete Mathematics* 346 (2023), 113358, DOI 10.1016/j.disc.2023.113358. It treats spectral radius (not merely index) and cleanly isolates hereditary/interlacing reductions.
- Wang, Hou and Li, **Extremal results for `C_3^-`-free signed graphs**, *Linear Algebra and its Applications* 681 (2024), 47--65. Its theorem statements put the extremal inequality and equality/switching condition together.
- Brunetti and Stanić, **Unbalanced signed graphs with extremal spectral radius or index**, *Computational and Applied Mathematics* 41 (2022), 118. It defines the extremal family/quantity early and separates spectral radius from index.
- Ghorbani and Majidi, **Complete signed graphs with largest maximum or smallest minimum eigenvalue**, *Discrete Mathematics* 347 (2024), 113860. Its introduction explicitly warns that signed spectral radius and index need not coincide.

For our manuscript the preferred style is therefore: define `m(N,s)` on page 1, state the exact theorems immediately, and postpone gauge/flux machinery to the proof sections.

## 7. Signed Cayley/circulant literature: scope distinction

There is a growing literature on signed Cayley graphs, including work on arithmetic spectra and strongly regular signed Cayley graphs. Those papers typically impose group structure on the **signature itself** (translation-invariant or generated from a Cayley datum).

Our optimization is different: the *underlying graph* is the Cayley/circulant graph `C_N(1,s)`, but the minimum ranges over **all** signatures. Any literature comparison must say this explicitly; otherwise a reader can mistakenly think the all-signing extremum has already been reduced to translation-invariant signatures.

Finite Fourier analysis appears in our all-even-order construction only after we explicitly choose one finite signing. It is a proof of an upper bound for the all-signing minimum, not a restriction of the optimization domain.

## 8. Signed circulants in 2026

Vaibhav Suvagiya, **Signed circulants at the Ramanujan bound**, arXiv:2607.18334 (submitted 19 July 2026).

The current v1 abstract studies `C_n(1,2)` for even `n`, an `F_2` quadrilateral/triangle-flux system, four switching classes inside that system, explicit spectra, and exhaustive switching-class computations for `n in {8,10,12,14,16,18}`. It conjectures the computed twisted value to be the global minimum for all even `n`; for odd `n` the quadrilateral system is inconsistent.

Relevance to this paper:

- useful very recent motivation for fixed-circulant spectral minimization and flux coordinates;
- its finite `s=2` computations overlap a motivating corner of our parameter space;
- our paper must not be framed as a counterexample note to it;
- our all-even-order theorem concerns every admissible step `s` but gives a threshold upper bound, not the claimed exact `s=2` global formula;
- our main exact results are instead the flat/equality hierarchy and the complete all-signing threshold transition on `N=3s`.

Any statement that a theorem here settles, improves, or contradicts Suvagiya's conjecture must be checked against the full primary text and exact quantifiers, not inferred from an abstract or from numerical values.

## 9. A useful new narrative after the rebuild

The flat/off-flat part now has a stronger structure than the original draft. The paper can state a **finite spectral hierarchy**:

1. `m(N,s)=2` exactly on the flat line `N=2s+2`;
2. the first off-flat value `sqrt(5)` occurs exactly at `(5,2)` and `(10,3)`;
3. every remaining parameter pair satisfies `m(N,s)>=sqrt(4+sqrt(2))`, and `(8,2)` attains this second gap.

The matrix engine is the integral defect

`B=A_sigma^2-4I`.

This is a much stronger introductory story than presenting `sqrt(5)` merely as a universal bound. It also interfaces naturally with the weighing-matrix/two-eigenvalue literature without duplicating its general classification.

A second independent axis is the `sqrt(8)` threshold:

- every even order admits a finite signing below `sqrt(8)`;
- on `N=3s`, the exact iff classification is `s` even or `s in {3,5}`;
- odd `s>=7` satisfy the quantitative all-signing obstruction `m(3s,s)^2>=8+2/139`.

The introduction should present these as two finite-global phenomena: a **low-end spectral hierarchy** and a **Ramanujan-scale threshold transition**.

## 10. Suggested theorem-first wording

Safe wording:

> For a fixed two-step circulant `C_N(1,s)` we minimize the spectral radius over all edge signatures. We first determine the bottom of this finite extremal problem: the trace bound is attained exactly on `N=2s+2`; the first off-flat value `sqrt(5)` occurs only for two parameter pairs; and all remaining pairs are separated by a further universal gap. We then turn to the threshold `sqrt(8)`, proving a finite construction for every even order and an exact transition on the resonance line `N=3s`.

Avoid:

- "we introduce spectral minimization of signed graphs";
- "we discover all 4-regular two-eigenvalue signed graphs";
- "MSS gives a spectral-radius signing for every graph";
- "signed Cayley results cover arbitrary signatures";
- "first", "sharpest known", or "previously unknown" before final priority checks.

For equality statements, write `if and only if` in the theorem statement and separately specify whether classification is by labelled switching equivalence or switching isomorphism.

For the computer-assisted odd obstruction, the global theorem should remain an ordinary mathematical theorem; the finite computation belongs in an isolated exact lemma with a complete state space, exact integer acceptance inequality, certificate format, and reproducibility script.

## 11. Novelty claims presently safe to make

Subject to a final primary-source search, the manuscript can safely describe its *mathematical content* without claiming priority:

1. an exact parameter and switching classification of trace-bound equality within signed two-step circulants;
2. a sharp low-end hierarchy `2`, `sqrt(5)`, then `sqrt(4+sqrt(2))` for the finite minimization problem;
3. a finite all-even-order sub-`sqrt(8)` theorem;
4. a complete threshold classification on `N=3s`, including exact exceptional cases and a uniform all-signing odd obstruction;
5. a local signed-triangle finite-state mechanism that propagates a finite exact certificate to infinitely many finite graphs.

Do **not** write “first”, “new”, “sharpest known”, or “previously unknown” until the final literature sweep is complete.

## 12. Journal-level assessment

With the strengthened package (exact flat theorem + complete `sqrt(5)` equality + universal sharp second gap + universal even-order theorem + complete `N=3s` threshold theorem + local rigidity mechanism), realistic targets are:

- *Journal of Graph Theory*;
- *European Journal of Combinatorics*;
- *Linear Algebra and its Applications*;
- *Electronic Journal of Combinatorics*.

The new low-end hierarchy materially improves the structural content and should help JGT/EJC positioning. The hard negative `sqrt(8)` classification is still concentrated on chord-cycle length 3, so a JCTB-level claim remains premature unless a genuinely broader odd-`k` theorem or a substantially more conceptual replacement of the nine-column certificate is obtained.
