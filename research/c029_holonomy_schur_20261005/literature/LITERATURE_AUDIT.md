# C029 / Target A: primary-source literature audit

Primary-source checks: 2026-10-05, 05:51–05:58 UTC. Citation record consolidated at 07:46 UTC. This standalone audit records findings, source locations and retrieval hashes; it does not redistribute third-party full texts.

## 1. Original source and replacement

The historical citation is genuine: Vaibhav Suvagiya, *Signed circulants at the Ramanujan bound*, [arXiv:2607.18334v1](https://arxiv.org/abs/2607.18334v1), submitted 19 July 2026. [Conjecture 3](https://arxiv.org/html/2607.18334v1#S2) states exactly

m_n=min_sigma rho(A_sigma)=rho_-(n), for every even n>=8,

rho_-(n)^2=4+2 cos(2 pi/n)+2 cos(4 pi/n),

on the undirected cycle square C_n(1,2), with real edge signs ±1 and rho the largest absolute eigenvalue. Proposition 2 establishes the twisted signing's value, not the all-signing lower bound. Small-size enumeration for n=8,10,12,14,16,18 is reported to numerical tolerance 10^-9, not as an exact-arithmetic certificate. Remark 4 separates the extra quadrilaterals at n=8.

**The current 2607.18334 record is withdrawn.** [Version 2](https://arxiv.org/abs/2607.18334), dated 22 September 2026, states that the author combined it with arXiv:2607.17343.

The replacement is Vaibhav Suvagiya, *Parity families and signed spectra: kernel averaging, near-Ramanujan bounds, and exact circulant models*, [arXiv:2607.17343v2](https://arxiv.org/abs/2607.17343v2), 22 September 2026, 20 pages.

- [Theorem 26, §12.2](https://arxiv.org/html/2607.17343v2#S12.SS2), PDF pp.16–18, uses all positive step-1 signs and the repeated step-2 pattern (+,+,-,+,-,-,+,-). On n=8m, m>=4, it proves rho=r_*=2.793604493334841…<rho_-(n), where r_* is the largest root of x^4-2x^3-6x^2+12x-4
- [Conjecture 28, §12.3](https://arxiv.org/html/2607.17343v2#S12.SS3), PDF p.18, proposes m_(8m)=r_* for every m>=4, with the minimum over **all** signings
- Remark 27 explicitly says the periodic searches omitted opposite Hamilton-cycle holonomy
- Remark 29 does not claim n=32 is the first failure

The all-signing quantifier was checked in HTML, [PDF](https://arxiv.org/pdf/2607.17343v2), and author canonical TeX. No later correction was located in this bounded audit.

## 2. Exact comparison and novelty boundary

Repository claims below distinguish historical manuscript scope from the publicly posted predecessor. Their complete proof certification is a separate requirement.

| Dimension | Current external source | Historical repository | Implication |
|---|---|---|---|
| Underlying graph, signs, objective | C_n(1,2), ±1 undirected signs, operator norm | Identical | Direct comparison applies |
| Constrained family | Alternating triangle flux, two Hamilton holonomies | Same coordinates | Constrained-family spectrum is established predecessor material |
| Explicit construction | Theorem 26: tau=(+,+,-,+,-,-,+,-), alpha=+1 | Same pattern in analytic-first headline | Exact mathematical overlap; no standalone novelty claim for unchanged construction |
| Endpoint | r_* above | sqrt(4+sqrt(10+2sqrt(5))) | Same algebraic constant |
| Failure range | n divisible by 8, n>=32 | Claimed all even n=32,40 or n>=48 | Nonzero residues and full truth-set classification have strictly broader scope, conditional on verification |
| First failure | Not certified | Exact exclusions at every even n=8..30 claimed | Additional finite classification content |
| Actual m_n and all minimizers | Not determined | Also not determined whenever twisted optimality fails | Do not call truth-set classification complete spectral minimization |
| Formal proof | Analytic argument plus symbolic determinant checking | Narrower Lean all-eigenvalue theorem recorded | Formalization adds validation; it does not remove theorem overlap |

The August Git chronology does not by itself prove public priority, independence, or an explanation for overlap. No accusation is supported. Public timestamped releases must be checked before priority claims.

## 3. New conjecture and antiperiodic route

The antiperiodic formula was already present in the project repository at commit [085ea698475b7b32e0ae57457ec903a922248f69](https://github.com/whzy3185/math/blob/085ea698475b7b32e0ae57457ec903a922248f69/research/paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex), file research/paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex, Git blob a550c50c079fde48759a5aa2b18895339e22ecd5. This continuation independently reverified the formula and applied it to the newly identified Conjecture 28. The construction retains the period-eight triangle-flux word and sets Hamilton holonomy alpha=-1. The finite cell phases satisfy z^m=-1, excluding z=1. With s=z+z^-1, the eight-cell determinant is

P(x,s)=x^8-16x^6+80x^4-128x^2+38+s(-2x^4+16x^2-13)+s^2.

The determinant argument at x=r_*, with strict decrease in s, yields P(r_*,s)>P(r_*,2)=0 for s<2, while excluding |x|>r_*. The verified real seam and finite Bloch decomposition give every finite antiperiodic sample rho<r_*, contradicting Conjecture 28. This application concerns a better explicit family, not a global minimizing classification. The accompanying proof gives the exact formula and finite-size comparison.

Potential research order: exact antiperiodic spectrum and gap; test actual global optimality of the improved family; certify the all-even historical truth set; obtain matching lower bounds and rigidity.

The latest merged §12 does not present the n=8k+2 one-G6 family, an all-residue counterexample classification, or the new R2 P-order-unit Riccati/Schur-tail argument established in the accompanying analytic proof. This is a section-level comparison, not an exhaustive theorem-equivalence proof across all literature.

## 4. Closest structural primary literature

### Luo–Roy

Ye Luo and Arindam Roy, [*Homological spectral graph theory and weighted cycle counting*, arXiv:2403.01550v4](https://arxiv.org/abs/2403.01550v4), revised 4 August 2026. Exact statements read: [Theorems 3.6 and 3.13](https://arxiv.org/html/2403.01550v4). The old title in Suvagiya's bibliography is superseded.

Theorem 3.6 treats connected graphs, positive directed weights, and complex/unitary homology-character families. Theorem 3.13 treats symmetric weights, fixed sign gains and affine Bloch tori, including outer-edge attainment characterized by character membership. It precedes general gauge, antisymmetry and Bloch-endpoint language. It does not minimize over all real signings of C_n(1,2), nor determine r_* on the restricted period-eight flux slice. Specific determinant and global lower-bound arguments remain necessary.

### Chen–van Dam–Bu

Lixiang Chen, Edwin R. van Dam, Changjiang Bu, [*Spectra of power hypergraphs and signed graphs via parity-closed walks*](https://arxiv.org/abs/2302.10496), JCTA 207 (2024), 105909, [DOI](https://doi.org/10.1016/j.jcta.2024.105909). Exact read: Theorem 3.1, downloaded arXiv PDF p.9. The count of parity-closed walks of length d is the mean d-th spectral moment over all signings of a fixed graph. A uniform average cannot alone establish a lower bound for every signing; a new moment obstruction must prove that quantifier.

### Greaves–Koolen–Munemasa–Sano–Taniguchi

Gary Greaves, Jack Koolen, Akihiro Munemasa, Yoshio Sano, Tetsuji Taniguchi, [*Edge-signed graphs with smallest eigenvalue greater than -2*](https://arxiv.org/abs/1309.5178), JCTB 110 (2015), 90–111, [DOI](https://doi.org/10.1016/j.jctb.2014.07.006). Exact read: Theorem 6, arXiv v2 p.6, plus Theorem 2 and Corollary 3.

Theorem 6 requires a connected integrally represented edge-signed graph with smallest eigenvalue >-2, and classifies it by representation graph. Exceptional E8 cases require separate treatment. This does not directly classify norm-near-2.8 C029 signings. Any use on squared/transformed adjacency matrices must establish entries, component structure, eigenvalue relation and representation hypotheses.

### McKee–Smyth

James McKee and Chris Smyth, [*Integer symmetric matrices having all their eigenvalues in the interval [-2,2]*](https://doi.org/10.1016/j.jalgebra.2007.05.019), Journal of Algebra 317 (2007), 260–290. Publisher abstract checked; theorem application not audited. The classification concerns cyclotomic matrices and norm<=2, below the C029 range. It is a potential tool for low-threshold transformed components, not a classification at the twisted benchmark.

### Lieb

Elliott H. Lieb, [*The Flux-Phase of the Half-Filled Band*](https://arxiv.org/abs/cond-mat/9410025), PRL 73 (1994), 2158–2161, [DOI](https://doi.org/10.1103/PhysRevLett.73.2158). Primary abstract checked. The objective is fermionic energy/free-energy minimization under bipartite/planar/periodicity hypotheses. Cycle squares contain triangles, and operator norm is a different functional. Reflection positivity is an inspiration, not a ready-made proof of the false original conjecture.

### Latest general-signing context

Zhiqiang Xu, [arXiv:2609.15591v4](https://arxiv.org/abs/2609.15591v4), revised 29 September 2026, Theorem 1.1 constructs a finite connected simple cubic graph whose every signing has norm>2sqrt(2). The paper distinguishes the open Ramanujan-base restriction. Generic introductions should not say the unrestricted Bilu–Linial conjecture remains untouched; this preprint does not settle C029.

Fangfang Lin and Hong Zhou, [arXiv:2609.15715v1](https://arxiv.org/abs/2609.15715v1), Theorem 1.2 gives a mixed-root-conditioned signing bound rho<((3+sqrt(5))/2)sqrt(d-1) and existence. At d=4 this exceeds even 4, hence is unsharp for C029; triangle-free/girth refinements do not apply. These are author-posted claims, not independently certified journal results.

Marcus–Spielman–Srivastava's standard one-sided signing theorem does not by itself control both spectral edges of non-bipartite cycle squares.

## 5. Search coverage and caveats

Direct checks included original/replacement arXiv records and relevant complete texts; merged PDF and canonical author TeX; author public repository latest commits and PR collection; exact-ID/title/author/graph/counterexample/erratum queries; and relevant primary predecessor statements.

Author main's latest recorded commit was [7416cbd12925558785194f90b555606c5f541d26](https://github.com/Vaibhavs25/bilu-linial-parity/commit/7416cbd12925558785194f90b555606c5f541d26), 20 September 2026. The one open PR listed was an earlier submission snapshot. No later arXiv version, separate correction, or primary-source all-even C029 classification was located.

**Forward citation coverage is bounded and incomplete.** No complete MathSciNet, zbMATH, Google Scholar or Semantic Scholar citation graph was traversed. “Not located” does not prove absence. Search snippets continue returning the withdrawn July abstract, so they must not control current status.

## 6. Supported conclusion

The original conjecture has already been disproved on the 8-divisible subsequence in the revised source. The repository's all-even classification has additional claimed scope, conditional on proof verification. The latest Conjecture 28 is a sharply defined new target. Do not claim publication priority, full determination of m_n, all-minimizer classification, exhaustive absence of follow-ups, or a guaranteed journal level.

## Citation provenance

The accompanying source_manifest.json records checked URLs, theorem locations, retrieval times and SHA-256 digests of the source copies read during verification. Third-party full texts are not included in this package. Digests identify the retrieved versions and are not hashes of the present audit.
