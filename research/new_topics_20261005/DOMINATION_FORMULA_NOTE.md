# Exact check of a printed cutoff discrepancy

Source: Koch–Narayan, arXiv:2511.01719v1, Conjecture 1 and Theorem 4. Checked directly in both HTML and PDF on 5 October 2026.

Let a=ceil(γ/2), b=floor(γ/2), r=n−3γ. The printed bound is

2γ+2ab+min(r,2a−b+1)(2a+1)+sum_(i=1)^Φ (2a+1+ceil(i/2)),

with Φ=max(0,r−2a−b+1). At (n,γ)=(16,4), a=b=2 and r=4, this gives 8+8+3·5=31.

The supplied script constructs a bipartite 16-vertex graph with 36 edges and exactly one dominating set of minimum size four. The four dominators are x1,x2,y1,y2. Each xi has two private vertices bi1,bi2; each yj has two private vertices aj1,aj2. Connect b11 and b21 to all four a-vertices. Add c1,…,c4, each adjacent to x1 and all four a-vertices. This has 8+8+20=36 edges.

Proof of minimum and uniqueness: every vertex dominates at most one of the four designated dominators, so at least four vertices are needed. A four-set must choose exactly one representative from each dominator's closed neighbourhood. The leaves bi2 exclude choosing bi1 or any c as a representative. With these exclusions, the two private neighbours of each yj force yj itself. The remaining bi1 vertices then force xi rather than bi2. Thus the designated set is unique.

Independent finite check: enumerate all vertex subsets of cardinality 0,1,2,3,4 and test domination by bitset unions. The result and full edge list are in domination_formula_check.json. This exact computation confirms the analytic argument; it is not a formal Lean proof.

The natural tail count from the source's own case transition is max(0,r−(2a−b+1)). With that repaired count, the same parameter pair has proposed bound 37, which this graph does not exceed. Therefore this note identifies a likely indexing typo. It does not claim a substantive counterexample to the intended repaired extremal assertion, and it is not the recommended main research topic.
