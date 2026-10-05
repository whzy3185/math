# Five independent topic screens and two bounded pilots

Later attribution update: the isolated n13 unique-domination counterexample and printed-cutoff issue were already reported in Erlbacher's public artifacts. See unique_domination_pilot/extension/prior_work/PRIOR_WORK_ADDENDUM.md for the pinned source and exact isomorphism verification. The new-topic branch now also includes the audited199-orbit M6 classification. The source screen below is preserved as the earlier selection record; current claims are in README.md and CLAIM_LEDGER.md.

Date: 5 October 2026 UTC. This screening is separate from the ongoing C029 signed-cycle-square work. It concerns extremal domination, directed matchings, induced-subgraph density, additive packing, and tournament quasirandomness. Status claims below are bounded by the primary sources actually checked, not a complete citation database.

## Update after the bounded pilot

The unique-domination pilot has now produced an independently audited sharp theorem: at n=3gamma+1, the maximum is gamma(gamma+7)/2; for gamma>=4 the extremizer is unique up to isomorphism. It disproves the originally proposed near-boundary value, independently of the printed cutoff issue. See unique_domination_pilot/STATUS.md and audit/PROOF_AUDIT.md. The screening and proposed target below are preserved as the earlier research record.

## Recommendation

1. **Primary pilot: sharp extremal unique domination at n=3γ+1.** Small excess gives a strong structural reduction, exact finite checks are inexpensive after reduction, and the first proof target is an infinite parameter family. First repair a printed summation-cutoff issue; do not market that typo as the main result.
2. **Secondary pilot: induced-subgraph Hall profiles in iterated Mycielski graphs.** Exact M2–M5 baselines have now been computed; aim for a symmetry/layer-compressed M6 certificate and a structural description of extremal subsets. An all-k asymptotic theorem is a later goal, not a promised short project.
3. **Reserve: matching-strengthened Seymour in restricted tournaments.** A current genuine conjecture, but the whole tournament problem has substantial difficulty and an active competing construction programme. Start only from a sharply restricted Hall-obstruction lemma.

The arithmetic-packing and H9/H16 targets below should not be pursued in their old “open conjecture” forms: recent primary sources already address them.

## 1. Unique minimum domination: near-critical edge extremality

**Primary source.** Garrison Koch and Darren Narayan, [*Maximal bipartite graphs with a unique minimum dominating set*, arXiv:2511.01719v1](https://arxiv.org/abs/2511.01719). [Full text](https://arxiv.org/html/2511.01719v1). The current record checked still lists the November 2025 version. Relevant locations: Conjecture 1, Theorem 2, Theorem 4, Theorems 11–12. Exact-title, author and counterexample searches located no later primary resolution.

**Definitions and established boundary.** G is finite, simple, bipartite, has no isolated vertices, and has a unique minimum dominating set D of size γ>=2. Necessarily n>=3γ. The source proves its extremal bound for γ=2 and for n=3γ. At n=3γ the bound is 2γ+2 ceil(γ/2) floor(γ/2), and a construction attains it. The full bound remains presented as a conjecture, but its literal printed formula has an issue described below.

**Precise proposed pilot statement.** For every γ>=3 and every such G on 3γ+1 vertices, prove or refute

|E(G)| <= B1(γ) := 2γ + 2 ceil(γ/2) floor(γ/2) + 2 ceil(γ/2) + 1.

Then determine the equality structures. This is the r=1 specialization of the source's conjecture, unaffected by the defective distant-range cutoff. The source supplies an attaining construction. It does not supply an all-γ proof at this excess.

**First reduction.** Each d in D has at least two exterior private neighbours. With just 2γ+1 vertices outside D, there are only two types:

- one dominator has three private neighbours and all others have two
- every dominator has two, and one residual vertex has at least two neighbours in D

Edges inside D must remain allowed; silently assuming D is independent would change the problem. The n=3γ argument bounds each opposite-part pair of dominator cells by a six-vertex replacement obstruction. The extra vertex is exactly where that replacement must be rechecked.

**Bounded pilot output and stop.** Prove a complete reduction for those two types, independently verify the local replacement catalogue, and settle γ=3,4 exactly before extrapolating. Attempt a uniform aggregate inequality in |D∩A| and |D∩B|. Stop the pilot at a complete proof, an explicit counterexample, or a documented irreducible obstruction showing why the r=1 reduction cannot yet close. Finite success alone is not the all-γ theorem.

**Novelty/tractability/Lean.** Moderate novelty risk: the 2003 general-graph predecessor and 2025 bipartite paper must be compared at theorem level before a publication claim. Tractability is comparatively good because excess one leaves only the two structures above. Lean potential is high: finite sets, domination, unique minimum cardinality, local replacement maps and integer edge counting; no numerical spectral analysis.

**Source correction found during this screen.** The PDF and HTML print a tail cutoff Φ=max(0,r−2a−b+1), where a=ceil(γ/2), b=floor(γ/2), r=n−3γ, but the preceding case transition occurs at r=2a−b+1. Their own Case 1–2 construction pattern with γ=4 and four additional vertices gives a bipartite n=16 graph with 36 edges and a unique minimum dominating 4-set, whereas the literal printed bound is 31. An independently written exact checker examined every subset of size 0 through 4. This is a verified finite discrepancy; the natural repaired cutoff r−(2a−b+1) gives 37, so the example does not refute that repaired bound. Treat it as a likely indexing typo and proof-reading prerequisite, not a major extremal breakthrough.

Files: check_domination_formula.py, domination_formula_check.json, DOMINATION_FORMULA_NOTE.md.

## 2. Mycielski Hall ratios and extremal induced subsets

**Convention.** M2=K2 and M_(k+1)=μ(M_k), hence χ(M_k)=k and |V(M_k)|=3·2^(k−2)−1. This is shifted from papers writing M2=C5. Define

h(G)=max over nonempty S⊆V(G) of |S|/α(G[S]),

q_k(a)=max{|S|: S⊆V(M_k), α(M_k[S])=a}.

Then h(M_k)=max_a q_k(a)/a. This is the Hall ratio, unrelated to C029's spectral radius despite some literature using the same letter ρ.

**Primary sources and current boundary.**

- Mathew Cropper, András Gyárfás, Jenő Lehel, [*Hall ratio of the Mycielski graphs*](https://doi.org/10.1016/j.disc.2005.09.020), Discrete Mathematics 306 (2006), 1988–1990; [author PDF](https://users.renyi.hu/~gyarfas/Cikkek/114_hallratio.pdf)
- Bonamy et al., [*Revisiting a Theorem by Folkman on Graph Colouring*](https://doi.org/10.37236/8899), EJC 27(1) (2020), introduction: exact minimum independence ratios remain uncomputed in general. Use [journal PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i1p56/pdf/) because other posted abstracts differ in a factor in Folkman's statement
- Raphael Steiner, [*Fractional Chromatic Number Vs. Hall Ratio*](https://doi.org/10.1007/s00493-025-00164-0), Combinatorica 45, 37 (2025), introduction: even for iterated Mycielskians it remains open whether χ_f/h is bounded. This is the more recent explicit open-status anchor
- Johnathan B. Barnett, [2016 dissertation](https://etd.auburn.edu/bitstream/handle/10415/5316/Final%20Dissertation%20-%20Johnathan%20Barnett.pdf?isAllowed=y&sequence=2), Chapters 2 and 4: q-style profile machinery already exists as the w-function; do not claim that reformulation as new

No 2026 exact Mycielski Hall-ratio resolution was located in the bounded follow-up searches. General-graph separation results do not resolve the explicit Mycielski sequence. The 2025 paper on independence/matching of iterated Mycielskians computes whole-graph independence, not the maximum over all induced subgraphs.

**Newly executed finite baseline, not a novelty claim.** A fresh exact subset dynamic programme gives:

| Graph | Vertices | Nonempty subsets checked | h |
|---|---:|---:|---:|
| M2 | 2 | 3 | 2 |
| M3 | 5 | 31 | 5/2 |
| M4 | 11 | 2,047 | 8/3 |
| M5 | 23 | 8,388,607 | 3 |

For M5, q_5(a) for a=1,…,11 is

2, 5, 8, 12, 15, 18, 19, 20, 21, 22, 23.

The recurrence is α(S)=max{α(S\{v}),1+α(S\N[v])}. It is evaluated on every subset in increasing bit-mask order using integer arithmetic. Witness masks and counts of maximum-cardinality subsets at each a are saved. No claim is made that these small values are new, nor that this execution is Lean-certified.

**Precise bounded pilot.** Determine q_6(a), or an equally strong exact certificate sufficient to determine h(M6), with M6 having 47 vertices; classify the maximizing induced subsets under automorphisms. Full 2^47 enumeration is not the proposed method. First compare M5's extremal subsets with the two-layer construction and test a compressed state description. Reject a candidate compression as soon as two subsets sharing a state have different continuation behaviour. An exact independently replayable upper/lower certificate is the stopping deliverable; if compression fails, preserve the counterexample to compression rather than claiming an asymptotic result.

**Longer-range mathematical target.** A recurrence or structural theorem for q_k, strong enough to sharpen the growth of h(M_k), would address a genuine gap. Proving or disproving boundedness of χ_f(M_k)/h(M_k) is much harder and is not the pilot deliverable.

**Novelty/tractability/Lean.** Medium-to-high novelty risk for isolated numerical values; lower risk for a genuinely new structural theorem. Finite experimentation is very tractable through M5, while M6 requires compression or branch-and-bound. Lean potential is high for the recurrence, graph construction and certificate checker; formalizing fractional-colouring asymptotics is a separate, larger undertaking.

Files: mycielski_profile.cpp, mycielski_profile.txt, MYCIELSKI_BASELINE.md.

## 3. Matching-strengthened Seymour: reserve programme

Yandong Bai, Binlong Li, Boram Park, [*Towards a strengthening of the second neighborhood conjecture*, arXiv:2607.18047v1](https://arxiv.org/abs/2607.18047), 20 July 2026. [Conjectures 1.2–1.3; Theorems 1.4–1.5](https://arxiv.org/html/2607.18047v1).

A strong Seymour vertex v has an arc matching saturating N+(v) into the **strict** second outneighbourhood N++(v), excluding v and N+(v). Conjecture 1.3 asks whether every tournament has such a vertex. The source proves existence when minimum outdegree is at most five, and for its 5-anti-transitive class. It also shows why minimum-outdegree and median-order shortcuts do not automatically extend. Ordinary Seymour is already proved for tournaments; that is a different statement.

**Bounded possible pilot.** Analyze 6-regular tournaments on 13 vertices: for each v, the bipartite arc graph N+(v)→N−(v) has sides of size six. Prove that at least one admits a perfect matching, or produce an explicit tournament and Hall barriers at every vertex. A structural route is to classify minimal Hall-deficient sets S of size 3–6 and show that the simultaneous barriers cannot occur. Do not quietly generalize from a symmetric subclass to all tournaments.

**Overlap warning.** The public [AustinBGibbons/ssnc notes](https://github.com/AustinBGibbons/ssnc) already develop weighted tournament substitution and report an infinite family with exactly nine strong vertices. These are public author-written, unreviewed research claims, not established theorems in this audit. They must be checked before claiming new constructions or a new matching reduction. Guo–Kang–Zwaneveld's [*Seymour-tight orientations*, arXiv:2603.29626](https://arxiv.org/abs/2603.29626) also develops lexicographic constructions for ordinary neighbourhood tightness; equality of cardinalities does not imply a matching.

**Assessment.** Potentially high mathematical upside, high difficulty and overlap risk; reserve behind the two pilots. Exact matching/Hall certificates have excellent Lean prospects, but certification of finitely many tournaments would not solve Conjecture 1.3.

## 4. Arithmetic-progression packing: old conjectures screened out

Alon, Dębski, Grytczuk, Przybyło, [*Packing arithmetic progressions*, arXiv:2603.02786](https://arxiv.org/abs/2603.02786), distinguish A_d={d,2d,…,floor(n/d)d} from B_d={d,2d,…,nd}. Integer translates must be pairwise disjoint inside an interval measured by its cardinality.

The September primary successor is Hou, Liu, Zhao, [*Simultaneous Residue-Class Selection in Prescribed-Difference Packings*, arXiv:2609.07487v2](https://arxiv.org/abs/2609.07487v2), revised 24 September 2026. [Theorems 1.2, 1.5 and Corollary 1.6](https://arxiv.org/html/2609.07487v2) prove the original bounded-diameter and prime-difference asymptotics, while the lower bound 19/108 for the full B-family exceeds the old conjectured 1/6. Mao–Wang–Wei–Yang, [arXiv:2607.06113](https://arxiv.org/abs/2607.06113), handle fixed n with k→∞. Together these preprints address all seven old conjectures, by proof or refutation.

**Decision.** Do not launch a project “proving constant 4/3” or “proving constant 1/6 for all differences.” A genuinely new question would be the correct full-family leading constant beyond 19/108, but first the recent residue-class machinery needs an independent proof audit. Tractability and formalization costs are much higher than a small finite packing search suggests. Not selected for a first pilot.

## 5. H9/H16 tournament forcing: obsolete target rejected

Jonathan A. Noel, Arjun Ranganathan, Lina M. Simbaqueba, [*Forcing Quasirandomness in a Regular Tournament*](https://igt.centre-mersenne.org/articles/10.5802/igt.20/), Innovations in Graph Theory 3 (2026), 127–169. The [published PDF](https://igt.centre-mersenne.org/item/10.5802/igt.20.pdf), Theorem 1.4 and Proposition 4.3, explicitly place H9 and its reverse H16 among the **non-forcing** tournaments. The older preprint conjecture is still reproduced on secondary open-problem pages.

The hypothesis is a nearly regular sequence of tournaments and convergence of H's homomorphism density to the random value. It is not ordinary finite regularity alone. The published counterexample uses a nonconstant regular tournament limit based on a cyclic triangle.

**Decision.** Reject the old H9/H16 conjecture as a new project. Classifying six-vertex forcing patterns might be a different question, but this screen has not established its latest coverage; it is not recommended as an open problem until that separate check is done. Rational flag-algebra certificates have formalization potential, but do not justify ignoring the final journal version.

## Coverage and stopping boundary

The screen used original primary papers, current arXiv records, final publisher versions where found, theorem-level comparisons, and targeted exact-title/ID/author/counterexample searches through 5 October 2026. Secondary aggregators served only as discovery leads. No author contact, journal submission, purchase, remote repository change or broad priority claim occurred.

Forward citations were not exhaustively traversed in MathSciNet, zbMATH, Scholar or Semantic Scholar. “No later resolution located” is therefore a bounded negative result. The two selected pilots are explicit research proposals, not claims of guaranteed novelty or publishability. Their mathematical stopping conditions are proof, counterexample, or a precise obstruction with reproducible evidence.
