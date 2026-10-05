# A counterexample family at n = 3γ + 1

Status: complete elementary proof and exact finite checks; independent mathematical audit PASS on 5 October 2026. See audit/PROOF_AUDIT.md. Prepared 5 October 2026. This is separate from the earlier distant-range printed-cutoff discrepancy.

## 1. Exact source statement and scope

Garrison Koch and Darren Narayan, *Maximal bipartite graphs with a unique minimum dominating set*, arXiv:2511.01719v1 (3 November 2025), **Conjecture 1, PDF page 2**:

- G is a finite simple bipartite graph without isolated vertices
- γ is its domination number, γ>=2
- G has exactly one dominating set of cardinality γ
- n>=3γ

Connectedness is not required in the conjecture. The examples below are connected, so they also refute its restriction to connected graphs. “Unique minimum” means a unique cardinality-minimizer, not merely a unique inclusion-minimal set.

Source: https://arxiv.org/pdf/2511.01719v1, https://arxiv.org/html/2511.01719v1#S1

PDF SHA-256: 49a9327b22e6928b77e6bd01119179f5e4bd1cc851d3fc7f33a31c162642d43c. The formula was checked directly on page 2 of the primary PDF.

Write a=ceil(γ/2) and b=floor(γ/2). At n=3γ+1 the source conjecture specializes to

B_source(γ)=2γ+2ab+2a+1.

Indeed its min-term has first input 1 and second input 2a-b+1>=1; its printed tail count is max(0,2-2a-b)=0. The naturally repaired distant-range tail count also vanishes. Thus the comparison here is unaffected by the separately identified cutoff typo.

## 2. Construction H(p,q)

Let p,q>=1 be integers. Take the following distinct vertices:

X={x_i:1<=i<=p}, Y={y_j:1<=j<=q},

B={b_i^0,b_i^1:1<=i<=p}, A={a_j^0,a_j^1:1<=j<=q}, and z.

The bipartition is

L=X ∪ A ∪ {z}, R=Y ∪ B.

Include exactly these edges:

1. x_i b_i^0 and x_i b_i^1, for every i
2. y_j a_j^0 and y_j a_j^1, for every j
3. b_i^t a_j^0, for every i,j and t in {0,1}
4. z b_i^t, for every i,t
5. z y_j, for every j

No other edges are present. Hence

n=3(p+q)+1,

e=2p+2q+2pq+2p+q=2pq+4p+3q.

The graph is simple and bipartite by the displayed partition. It is connected: z reaches every y_j and every b_i^t; each x_i reaches a b_i^t; each a_j^t reaches y_j. In particular there are no isolated vertices.

## 3. Domination number and uniqueness

Let D=X∪Y. It dominates the graph and |D|=p+q.

For any dominating set K, the vertex x_i forces K to meet

C_i={x_i,b_i^0,b_i^1}.

The leaf a_j^1 forces K to meet

L_j={y_j,a_j^1}.

All p+q sets C_i,L_j are pairwise disjoint. Thus |K|>=p+q, proving γ(H(p,q))=p+q.

If |K|=p+q, then K contains exactly one vertex from each C_i and each L_j, and contains no other vertex. In particular z and all a_j^0 are absent from K.

Suppose K chooses b_i^0 rather than x_i from C_i. The vertex b_i^1 is then undominated: its neighbours are x_i, z, and the a_j^0, none of which lies in K. The same holds with the two b-vertices reversed. Therefore K contains every x_i and no b_i^t.

Now if K chooses a_j^1 rather than y_j from L_j, the vertex a_j^0 is undominated: its neighbours are y_j and the b_i^t, all absent. Hence K contains every y_j. Therefore K=D. This proves that D is the unique minimum dominating set.

The proof is finite-set and adjacency reasoning. It does not infer minimality or uniqueness from sampling.

## 4. Uniform violation of the source boundary

For γ>=4 set p=a=ceil(γ/2), q=b=floor(γ/2). Then

e(H(a,b))=2ab+4a+3b=2ab+3γ+a,

e(H(a,b))-B_source(γ)=b-1=floor(γ/2)-1>0.

Thus Conjecture 1 fails for every γ>=4 already at n=3γ+1. This family is not a consequence of correcting a summation index. It violates the typo-independent near-boundary specialization.

At γ=4: p=q=2, n=13, e=22, unique minimum dominating set {x_1,x_2,y_1,y_2}. The conjectured bound is 2·4+2·2·2+(2·2+1)=21.

The source's proposed extremal constructions have a perfect dominating set in its stated sense. Here z has q neighbours in D, so for q>=2 D is not perfect. This explains a concrete structural distinction, not by itself a diagnosis of every argument in the source.

## 5. Reproducibility and remaining claims

candidate13.json is the explicit labelled 13-vertex graph; its labels use indices 0 and 1 rather than 1 and 2. check_counterexample_independent.py independently reads the saved edge list, checks simplicity, bipartiteness, connectedness, no isolated vertices, and all 2^13 subsets for domination using ordinary Python sets. The generator and checker do not share domination-testing code.

The sharp replacement at n=3γ+1 and its equality classification are separate statements proved in SHARP_BOUNDARY_THEOREM.md; both have passed the independent audit in audit/PROOF_AUDIT.md. This note establishes only the explicit family, its unique minimum domination, and its contradiction to the displayed conjecture. Publication priority and absence of equivalent counterexamples require further bounded literature checks before external claims.

## Prior-work attribution update, 5 October 2026

The 13-vertex, 22-edge example and the printed-cutoff issue were already reported in John Erlbacher's public [Demonstrandum counterexample package](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md), whose Git commit is dated 13 June 2026. An explicit isomorphism and fresh exhaustive check are in extension/prior_work/. The present contribution is framed as the all-gamma sharp boundary maximum and equality theorem; no proof of that general theorem was located in the inspected prior package. This is a bounded source comparison, not an exhaustive priority claim. Mathematical statements and audit conclusions are unchanged.
