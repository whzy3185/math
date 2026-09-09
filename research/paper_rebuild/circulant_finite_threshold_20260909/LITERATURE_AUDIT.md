# Literature audit (2026-09-09)

This note records external public literature relevant to the finite-global extremal problem. It is intentionally conservative about novelty.

## 1. Spectral radius two and cyclotomic signed graphs

James McKee and Chris Smyth, **Integer symmetric matrices having all their eigenvalues in the interval [-2,2]**, *Journal of Algebra* 317 (2007), 260--290, DOI 10.1016/j.jalgebra.2007.05.019; arXiv:0705.3599.

They classify integer symmetric matrices, including signed graphs, whose spectra lie in `[-2,2]`. Therefore our theorem
`m(N,s)=2 iff N=2s+2` must be advertised only as an exact classification *inside the two-step circulant family*, together with its switching/equality description and the elementary off-flat `sqrt(5)` gap. We do not claim the general spectral-radius-two theory.

## 2. Signings and Ramanujan/2-lift background

Adam Marcus, Daniel Spielman and Nikhil Srivastava, **Interlacing families I: Bipartite Ramanujan graphs of all degrees**, *Annals of Mathematics* 182 (2015), 307--325, DOI 10.4007/annals.2015.182.1.7.

This proves existence of good signings/2-lifts via interlacing families in a broad setting. It is conceptual background for spectral control by signs, but it does not determine
`min_sigma rho(A_sigma)` on a fixed nonbipartite step circulant and does not imply our exact finite equality or resonance obstruction.

Related 2-lift work of Bilu--Linial should be cited in the final bibliography after bibliographic verification; the manuscript should distinguish a signing used as a lift datum from the present direct signed-adjacency minimization problem.

## 3. Signed circulants in 2026

Vaibhav Suvagiya, **Signed circulants at the Ramanujan bound**, arXiv:2607.18334 (July 2026).

The current public abstract studies `C_n(1,2)` for even `n`, an F2 quadrilateral/triangle-flux system, explicit spectra of its classes, and exhaustive switching-class computations for `n in {8,10,12,14,16,18}`. The abstract states a conjectural global-minimum extension beyond the enumerated finite orders.

Relevance to this paper:

- useful recent motivation for fixed-circulant spectral minimization and flux coordinates;
- its finite `s=2` computations overlap the motivating corner of our parameter space;
- our paper must not be framed as a counterexample note to it;
- the present paper instead emphasizes the family-wide finite extremum, the exact flat line, a universal even-order sub-threshold construction, and an all-signing obstruction/phase transition on the odd `N=3s` line.

Any claim that our all-even-order theorem resolves or contradicts a specific conjecture in the full Suvagiya text must be checked against the primary arXiv PDF before submission; the abstract alone is not enough for a priority claim.

## 4. Signed graph switching

The basic switching invariance used here is standard signed-graph theory. The final bibliography should include a primary signed-graph reference (e.g. Zaslavsky's foundational work) rather than presenting switching as new. Our contribution is the exact use of switching coordinates in the fixed circulant extremal problem.

## 5. Circulant/Cayley spectra

Finite Fourier diagonalization of ordinary or signed translation-invariant operators on cyclic groups is standard. The all-even-order theorem is not novel because it uses Fourier analysis; its content is the explicit finite signing and the resulting uniform strict inequality for every admissible step `s` on every even order `N`.

A targeted pre-submission search is still needed for phrases such as:
- signed Cayley graph spectral radius minimization;
- signed circulant minimum spectral radius;
- magnetic/flux adjacency on cyclic Cayley graphs;
- weighing matrices / orthogonal signed adjacency matrices in 4-regular circulants.

## 6. Novelty claims presently safe to make

Subject to a final primary-source search, the manuscript can safely describe its *mathematical content* without claiming priority:

1. a family-specific exact flat/off-flat dichotomy for signed `C_N(1,s)`;
2. a finite all-even-order sub-`sqrt(8)` theorem;
3. a complete threshold classification on `N=3s`, including exact exceptional cases and a uniform all-signing odd obstruction;
4. a local signed-triangle finite-state mechanism that propagates a finite exact certificate to infinitely many finite graphs.

Do **not** write “first”, “new”, “sharpest known”, or “previously unknown” until the final literature sweep is complete.

## 7. Journal-level assessment

With the current package (exact flat theorem + universal even-order theorem + complete `N=3s` threshold theorem + local rigidity mechanism), realistic targets remain:
- *Journal of Graph Theory*;
- *European Journal of Combinatorics*;
- *Linear Algebra and its Applications*;
- *Electronic Journal of Combinatorics*.

The all-even-order theorem materially strengthens the scope beyond a single resonance line, but the hard negative classification is still concentrated on chord-cycle length 3. On present evidence, a JCTB-level claim would be premature. A genuine classification for odd `N=ks` with general odd `k`, or a hand structural replacement for the nine-column certificate, would materially change that assessment.
