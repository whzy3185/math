# Completing the equality cases at domination numbers two and three

5 October 2026. Status: complete elementary argument; independent mathematical audit PASS on 5 October 2026, with a separately written exhaustive checker. See audit/PROOF_AUDIT.md. It does not alter the frozen seven-page manuscript or the scope of its prior audit.

## Result and prior overlap

Let G be a finite simple bipartite graph without isolated vertices, with n=3γ+1 vertices and a unique minimum-cardinality dominating set of size γ. The already audited theorem gives

e(G) ≤ γ(γ+7)/2.

**Equality completion.** If γ is 2 or 3, equality holds if and only if G is isomorphic to H(⌈γ/2⌉,⌊γ/2⌋), with H defined in `../COUNTEREXAMPLE_FAMILY.md`. Thus the same equality description extends to every γ≥2 when combined with the existing γ≥4 theorem.

The classification at n=10, γ=3, e=15 was already explicitly stated in [Koch–Narayan v1, Section 2.1, Figure 1 discussion](https://arxiv.org/html/2511.01719v1#S2.SS1). Their Theorem 11 gives the γ=2 edge bound for all orders. This note supplies the missing low-γ proof cases in the present argument; it is not advanced as a new discovery of those finite extremal graphs.

## A sharper seven-vertex lemma

Let F have bipartition {x}∪W and {y}∪U, where U={u₀,u₁} and |W|=3. Fix the five edges xU and yW. Its possible additional edges are xy and the six edges UW. Suppose {x,y} is the unique dominating set of cardinality at most two.

The seven-vertex bound already proved in the main argument says there are at most four additional edges. We sharpen its equality case:

**Lemma.** If there are exactly four additional edges, then xy is absent and the UW subgraph is a K₂,₂ on U and two members of W; the third member of W has no neighbour in U. Conversely, all three labelled choices of that third vertex give a unique minimum dominating pair {x,y}.

**Proof.** Suppose first that xy is present. A member w of W adjacent to both members of U would give the alternative dominating pair {y,w}, so every W-column has at most one UW edge. There must be exactly three UW edges, one in each column. If all three are incident with a single u, the pair {x,u} dominates F. Otherwise the row degrees are two and one. Choose the degree-two row vertex u and the unique W-neighbour w of the other row vertex. The pair {u,w} dominates x and y, both U vertices, and all three W vertices. Both cases contradict uniqueness. Hence xy is absent.

There are now four UW edges. The two row degrees are either three and one or two and two. In the first case, choose the full row vertex u and the neighbour w of the other row: {u,w} dominates F. In the second case, if the two two-element row neighbourhoods differ, choose u₀ and the unique vertex w in N(u₁)∩W outside N(u₀). Then u₀ covers its two W-neighbours, w covers itself and u₁, and x,y are covered by u₀,w respectively. Thus {u₀,w} dominates F. Uniqueness forces the two rows to have the same two-element neighbourhood, as claimed.

Conversely, write W={a,b,c}, with a and b adjacent to both members of U and c adjacent only to y. Every dominating set must meet both disjoint sets N[x]={x,u₀,u₁} and N[c]={c,y}. A dominating pair therefore selects one member of each set and no other vertices. Selecting u₀ or u₁ rather than x leaves the other U vertex undominated, since neither a nor b may be selected. Thus x is selected. Selecting c rather than y then leaves a and b undominated. The pair is exactly {x,y}. No singleton dominates, since the two forced sets are disjoint. QED.

## Reduction to the low-γ equality skeleton

Retain the notation and complete edge accounting of `../SHARP_BOUNDARY_THEOREM.md`. Select two exterior private neighbours of every member of D, leaving z. Orient the bipartition so z is on the side containing p dominators, with q on the other side.

Equality in the audited numerical optimization forces p=⌈γ/2⌉ and q=⌊γ/2⌋. For γ=2,3, this gives q=1 and p=1,2 respectively. Write the sole other-side dominator as y. Since D dominates z, z is adjacent to y. Put W=V₁∪{z}; its three vertices are all adjacent to y.

There are exactly 2p+3 fixed edges, namely each xᵢUᵢ and yW. The other edges fall into disjoint blocks indexed by i, each consisting of xᵢy and UᵢW. Every seven-vertex induced cell {xᵢ,y}∪Uᵢ∪W has {xᵢ,y} as its unique dominating set of cardinality at most two: a different such local set would extend with the retained centers D\{xᵢ,y} to a different global dominating set of size at most γ. All vertices outside the cell retain their own center. In particular, the shared leftover z is inside the cell, so no domination of it is being assumed without proof.

The maximum edge count is 2p+3+4p. Consequently every block has exactly four optional edges. The sharpened lemma shows that every center edge xᵢy is absent and each Uᵢ meets exactly two of the three columns of W, completely. Denote its omitted column by cᵢ.

## γ=2

There is one block. Its unique omitted column is a leaf adjacent to y; the other two columns each meet both U₁ vertices. Designate one active column as z and the other as v₁⁰, and the omitted column as v₁¹. The resulting graph is H(1,1). Its unique minimum pair and edge count nine also follow directly from the lemma.

## γ=3

There are two blocks. Suppose c₁≠c₂. Their two active-column sets have one common member w and together cover all of W. Choose arbitrary u₁∈U₁ and u₂∈U₂. Then

S={u₁,u₂,w}

is a dominating set: x₁,x₂ are dominated by u₁,u₂; all four U vertices are dominated by w; y is dominated by w; and every vertex of W is dominated by u₁ or u₂ or belongs to S. This is a different three-element dominating set, contrary to uniqueness.

Thus c₁=c₂. Relabel the shared omitted column v₁¹ and the two active columns z,v₁⁰. The edge set is exactly H(2,1). Its unique minimum dominating set and edge count fifteen are already proved by the construction theorem. QED.

## Supplementary exact verification

`check_low_gamma.py` is a fresh standalone enumerator on the reduced skeletons. It generates all 128 seven-vertex patterns and all 16,384 ten-vertex patterns. It tests every vertex subset of size at most γ for each pattern whose edge count reaches or exceeds the proposed equality count: 64 patterns at γ=2 and 6476 at γ=3.

Exactly three labelled patterns survive in each case; each is obtained by selecting the single common omitted W-column. The certificate is `low_gamma_certificate.json`. This is an exhaustive check of the equality skeleton justified above, not an unrestricted census of all graphs of those orders. The analytic proof does not depend on the enumeration.

## Next-regime boundary

No n=3γ+2 theorem is asserted in this note. The prior [Erlbacher artifact package](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md) already reports a 14-vertex, γ=4 example with 28 edges and an unbalanced-split construction. A future two-residual-vertex analysis must retain the joint domination obligations of both residual vertices, including their possible mutual adjacency; the one-residual proof does not directly establish such a bound.
