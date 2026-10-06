# Xu v4: scope, dependency reading, and C029 introduction implications

Read-only assessment, 6 October 2026. This records what the preprint states and how it bears on C029. Reading its proof is not independent certification of that proof.

## Pinned source and access

Zhiqiang Xu, *A 3-regular counterexample to the Bilu–Linial signing conjecture*, [arXiv:2609.15591v4](https://arxiv.org/pdf/2609.15591v4), 29 September 2026; DOI [10.48550/arXiv.2609.15591](https://doi.org/10.48550/arXiv.2609.15591). The [official record](https://arxiv.org/abs/2609.15591) confirms v1 on 14 September and v4 as the current revision. It supplies no journal reference. Page numbers below are printed PDF pages, starting at 1.

The public 19-page PDF was obtained legally. All mathematical prose, statements, displayed arguments, references and captions were read. Figures were not independently reconstructed. No arithmetic, graph construction, experiment, or proof verifier was run. Page 19 gives the author's affiliation as the Academy of Mathematics and Systems Science, Chinese Academy of Sciences.

## Compact primary-source ledger

Everything in this ledger is an **author claim**, not a certification by this reading.

| Location | Exact scope or dependency |
|---|---|
| pp.1–2, Conjecture 1.1 / Theorem 1.1 | σ:E(G)→{±1}; real symmetric signed adjacency. Claimed counterexample: ∃ fixed finite connected simple cubic F, ∀σ, ‖Aσ(F)‖>2√2. The objective is max|λ| |
| pp.3–4, §2 | Seed H₆₂: triangle, root, three binary trees; Q₀=H₆₂, Qⱼ₊₁=B(Qⱼ,Qⱼ); three Q₆₁ branches form J; leaf completion makes cubic F with J induced. The 28-vertex illustration is not claimed as a counterexample |
| pp.6–7 | ρ₀=2√2; gε=eₒᵀ(ρ₀I−εAσ)⁻¹eₒ; s=g₊+g₋ uses one σ |
| pp.12–16, Lemmas 6.1 / 3.5 | Tree/unicyclic positivity → switching reduction → seed s/√2=140300416/138131009>65/64 |
| pp.7,9–10, Lemma 3.3 | Assuming ‖Aσ(J)‖≤ρ₀, exterior-parent adjacency ensures branch matrices ≻0, including equality |
| pp.7,10–12, Lemma 3.4 | Both sides ≻0: gε(B)=1/(ρ₀−gε(X)−gε(Y)); s(B)≥4/(2ρ₀−s(X)−s(Y)) |
| pp.8–9, §4 | Seed + positivity + joining inequality → central Schur contradiction → induced-submatrix transfer J→F |
| pp.16–18, Proposition 7.1 / §8 | λ₂(A(F))>2√2; F non-Ramanujan. Ramanujan-base restriction and some-ℓ-lift question remain unresolved here |

## Dependency interpretation for the project

The source ledger separates premises that should not be collapsed into “Schur complements prove it.” In particular, an inverse response requires an invertible branch. C029 likewise needs its own positive pivot premises and uniform interior bounds; citing a recurrence cannot supply those hypotheses.

The common method vocabulary is useful for comparison, but it does not establish historical dependence. C029's cap-specific seed, two-step matrix recurrence, two endpoint responses, and cyclic junction assembly must be evaluated on their own hypotheses. The earlier method study already identifies this machinery as an application of established matrix tools. The present reading gives an additional recent comparison, not grounds to relabel routine elimination as a newly invented method.

The project-specific contrast is the direction and quantifiers of the target: C029 builds upper bounds for its prescribed words and handles independently chosen cell lengths; its old classification additionally needs universal lower bounds at the complementary orders. Those are separate logical duties. Neither the old truth-set statement nor the v7 upper-bound theorem follows by importing a result about a different support.

## Background statements that must be updated

1. **An unqualified present-tense claim that the general two-sided Bilu–Linial conjecture is simply open.** A new introduction should acknowledge the reported counterexample and pin the version. Until independently evaluated, describe it as Xu's preprint claim; do not turn this reading into a declaration of accepted resolution. The relevant source locations are the first and last rows of the ledger.
2. **A claim that general regular-graph signing can be treated as established Ramanujan-norm existence.** C029 cannot use that assertion as a premise. It must rely on an applicable established theorem or its explicit construction.
3. **A narrative that treats the universal sharp threshold as the endpoint of current background.** The fixed-support problem remains meaningful even when no universal threshold theorem is available. Its natural motivation is to identify the actual optimum, understand the success or failure of a prescribed candidate, and explain dependence on local cycle signs and finite holonomy.
4. **A novelty claim based only on a finite seed and Schur response recursion.** Any such claim needs a precise quantitative or structural distinction. The v7 mechanism should be described through its particular finite thresholds, independent lengths, count-uniform cyclic assembly and original-space margins.

These are conditions on a newly prepared introduction. They do not retroactively make an August manuscript historically inaccurate because a September preprint appeared later.

## Statements that can remain

- The exact two-lift spectral decomposition and its motivation for controlling both spectral edges. See the published Bilu–Linial reading in the preceding evidence cards.
- MSS's one-sided theorem and its two-sided consequence for bipartite supports. A single common signing is essential; choosing a different signing for each edge of the spectrum does not solve C029's objective.
- The fixed-graph optimization framing through Belardo–Cioabă–Koolen–Wang, Problem 3.18.
- The original manuscript's actual wording: signed spectra describe new two-lift eigenvalues; interlacing provides one-sided bounds, which become two-sided in the bipartite case; cycle squares are nonbipartite. This passage is in `aug25_intro.txt`, lines 20–28. It does not assert that the general conjecture is still open. Its existing mathematics needs no correction on that account; a current literature overview should add the new status information.
- The distinction between a periodic spectral calculation and a global minimization theorem. Both finite holonomy grids still matter in C029.

## No direct conclusion for C029

- No change to the claimed twisted-candidate truth set is established by this source reading.
- No value of μₙ, no list of minimizing cycle-square signings, and no C029 finite threshold is supplied.
- No C029 counterexample to a Ramanujan-base conjecture follows. Such an application would require checking that restriction separately.
- No loss of the need for exact finite classification: the old equality orders still require statements covering every admissible signing.
- No proof-dependency or priority transfer is established merely because two papers use seeds, switching and Schur complements.

## Limits and provenance

The source's Schur background cites Boyd–Vandenberghe; its tree/unicyclic comparison cites Stevanović and Hu while also providing its own arguments. These external originals were not re-read in this bounded round. The bibliography contains no C029/project citation; its absence cannot determine actual influence.

The actual old passage was checked against [frozen August introduction](https://github.com/whzy3185/math/tree/833face614d2e9bda09d7d7112dc89f9a78b3555/research/paper/manuscript_tex_task59). For current v7, `sections/01_problem_results.tex`, lines 155–162, already excludes the complementary-order lower bounds; `sections/02_holonomy_bulk.tex`, lines 59–91 and 100–112, separates the finite phase decomposition from prescribed-word optimality. No manuscript, earlier report, or Git state was edited.
