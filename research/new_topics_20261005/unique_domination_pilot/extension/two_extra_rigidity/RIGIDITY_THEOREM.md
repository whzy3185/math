# Equality classification two vertices above the threshold

5 October 2026. **Status: complete elementary proof; independent mathematical audit PASS on 5 October 2026. See audit/PROOF_AUDIT.md.** The independently reviewed ten-page paper_v2 remains unchanged and does not assert this classification.

## Statement

Let G be a finite simple bipartite graph without isolated vertices, of order 3γ+2, with a unique minimum-cardinality dominating set of size γ≥2. The independently audited sharp maximum is

M₂(γ)=⌈γ²/2⌉+5γ.

**Equality theorem.** Up to graph isomorphism, the graphs with e(G)=M₂(γ) are exactly:

- γ=2: the three graphs H₂(1,1), F₀ and F₁ defined below
- odd γ=2k+1≥3: the single graph H₂(k+1,k)
- even γ=2k≥4: the two graphs H₂(k,k) and H₂(k+1,k−1)

Thus all equality graphs are connected. The number of isomorphism classes is three at γ=2, one at every odd γ≥3, and two at every even γ≥4.

H₂(p,q) is the twin-residual construction in `../two_extra/CANDIDATE_BOUNDARY_THEOREM.md`: centers X,Y, two private vertices per center, all Uᵢ joined to the selected column vⱼ⁰ for each j, and two nonadjacent residual vertices each joined to every U vertex and every Y-center. Its unique minimum dominating set is X∪Y and its edge count is 2pq+6p+4q.

For F₀ and F₁ use eight vertices x,y,U={u₀,u₁,u₂},V={v₀,v₁,v₂}, with bipartition {x}∪V and {y}∪U. Both have the six edges xU and yV.

- F₀ has no edge xy and has all six edges between {u₀,u₁} and V, with no other edges
- F₁ has xy, all four edges between {u₀,u₁} and {v₀,v₁}, and the edge u₂v₂, with no other edges

Both have 12 edges and unique minimum dominating set {x,y}. F₀ has degree sequence (1,3,3,3,3,3,4,4); F₁ has (2,2,3,3,3,3,4,4). They are therefore nonisomorphic. Both have bipartition sizes 4,4, while H₂(1,1) has sizes 3,5, distinguishing the third class.

## 1. Equality data from the audited upper bound

Select two exterior private neighbours per member of D, leaving residual vertices z,w. Write p=|D∩A|, q=|D∩B|, p+q=γ, with centers X,Y and private pairs Uᵢ⊂B, Vⱼ⊂A.

If z,w lie in A, q≥1. Let S be the number with exactly one D-neighbour. The audited bound is

e(G) ≤ 2pq+6p+4q − S(q−1) ≤ M₂(γ).                 (1)

Its numerical equality condition is p−q=1 when γ is odd and p−q∈{0,2} when γ is even. Thus the only positive splits are those in the theorem statement; for γ=2 the formal split q=0 is excluded by domination of the residuals.

If z∈A,w∈B, put J=N(z)∩D⊆Y and K=N(w)∩D⊆X; both are nonempty. The three audited estimates are

- |J|,|K|≥2: e(G)≤2pq+5γ+1
- J singleton, |K|≥2, after swapping sides if necessary: e(G)≤2pq+5γ+2−q
- J,K both singleton: e(G)≤2pq+4γ+2

Every optional two-center block is legitimate because every residual whose owner is removed is included, or retains another owner. All selected private vertices outside a block keep their own centers. Those conditions were proved in the audited bound and are retained throughout this equality argument.

## 2. Opposite-side residuals cannot attain equality when γ≥3

### Both residuals have several D-neighbours

For odd γ, equality in the first estimate requires a balanced split and saturation of every residual incidence bound. Both residuals then cover all centers and all selected private vertices on the opposite side. Replacing any xᵢ,yⱼ by z,w gives another dominating γ-set, a contradiction.

For even γ, equality e(G)=M₂(γ) requires p=q=k≥2. Indeed an unbalanced split loses at least two in 2pq, making the first estimate strictly smaller than M₂(γ). The sum of deficits from the six-cell bounds and the residual-incidence bounds is exactly one. In particular, among the allowable edges from z to Y∪⋃Uᵢ, from w to X∪⋃Vⱼ, and the possible edge zw, at most one is missing.

If the missing edge, when there is one, is incident with an X-center or one of its private vertices, select a different X-center xᵢ. If it is incident with a Y-center or one of its private vertices, select a different Y-center yⱼ. These choices are possible because k≥2. If the only deficit is a cell edge or zw, choose any i,j. Then

(D\{xᵢ,yⱼ})∪{z,w}

dominates: the two removed centers and their private pairs have all needed residual incidences, every other private pair retains its center, and the residuals are selected. A missing incidence to a retained center or its private pair is harmless. This contradicts uniqueness.

### Exactly one residual has one D-neighbour

Assume J={yⱼ₀} and |K|≥2. The difference between the target and the second estimate is

⌈γ²/2⌉−2pq+q−2.                                  (2)

If q≥2, this can be zero only when γ is even, p=q and q=2; hence (p,q)=(2,2). For odd γ the first two terms in (2) are at least one. If q=1, |K|≥2 implies γ≥3 and (2) becomes ⌈γ²/2⌉−2γ+1, which vanishes only at γ=3. Thus equality is possible numerically only for (p,q)=(2,1) or (2,2).

In either split, saturation forces w adjacent to every X-center, every V vertex, and z. The two special seven-cells on x₁,yⱼ₀ and x₂,yⱼ₀ each have four optional edges. The audited seven-cell equality lemma says that each Uᵢ is complete to two members of the common three-set

W=Vⱼ₀∪{z}.

Two two-element subsets of a three-set intersect. Choose c in their intersection. Then

{w,c} ∪ (Y\{yⱼ₀})

is a dominating set of size q+1=γ−1. The vertex c covers both U pairs and yⱼ₀; w covers X, all V vertices and z; the remaining Y-centers are selected. This contradicts the domination number. Thus neither numerical exception gives an equality graph.

### Both residuals have one D-neighbour

The third estimate is strictly below the target for γ≥3, since

M₂(γ)−(2pq+4γ+2)=⌈γ²/2⌉−2pq+γ−2≥γ−2>0.

Consequently all extremal graphs with γ≥3 have their two residual vertices on the same side. The argument applies to any selection of two exterior private neighbours per center, and does not assume a preferred selection exists.

## 3. Same-side equality with q≥2

Equality in (1) forces S=0. Both residuals are therefore multiply dominated, and saturation gives all edges from each of them to every Y-center and every U vertex. Every ordinary six-cell has exactly two optional edges.

No center edge xᵢyⱼ can occur: replacing xᵢ by z gives a different dominating γ-set. The removed center is covered by yⱼ, its private pair by z, the other residual by a retained Y-center, and all other private pairs keep their centers.

The six-cell equality lemma now makes each Uᵢ–Vⱼ block a two-edge star. A star centered at u∈Uᵢ would allow the replacement of xᵢ,yⱼ by u,z. This covers the two removed centers and both private pairs, while w retains a Y-neighbour because q≥2. Hence every block is a column star: both Uᵢ vertices meet one vertex of Vⱼ.

For a fixed j, that selected column must be independent of i. Otherwise select one uᵢ from every Uᵢ and consider

{z} ∪ {uᵢ:1≤i≤p} ∪ (Y\{yⱼ}).

This has γ vertices. All X-centers are covered by the chosen U vertices; every U vertex and Y-center is covered by z; the two Vⱼ vertices are covered because both column choices occur; other V pairs keep their owners. The residual w retains a Y-neighbour because q≥2. Thus this is another minimum dominating set, a contradiction.

After relabelling each Vⱼ pair so the common column is vⱼ⁰, the entire edge list is exactly H₂(p,q). No edges remain unaccounted for. Together with the equality splits in Section 1, this proves the stated classification whenever q≥2.

## 4. Same-side equality with q=1

The numerical equality splits restrict this case to p=1,2,3, corresponding to γ=2,3,4. Both residuals have the sole Y-center y as owner. Put W=V₁∪{z,w}, so |W|=4.

Each two-center cell has private sizes (2,4), and equality forces six optional edges. We need its equality pattern.

**Eight-cell lemma.** A (2,4) cell with unique center dominating pair and six optional edges has no center edge and consists of K₂,₃ between U and three columns of W, with the fourth column empty.

**Proof.** If xy is present, uniqueness excludes any full W-column, leaving at most four cross-edges and hence five optional edges. Thus xy is absent. Six cross-edges have row degrees (4,2) or (3,3). A full row vertex and a neighbour of the other row exclude (4,2). If the two three-element row neighbourhoods differ, choose one row vertex and the other row's unique neighbour outside it; these two vertices dominate the cell. Thus the row neighbourhoods agree. Conversely, the unused W-column and x have disjoint closed neighbourhoods forcing the center pair, by the same argument as the seven-cell equality lemma. QED.

Each Uᵢ is therefore complete to W minus one column cᵢ. If the omitted columns differ, the active columns together cover W. Because p≤3<4, some column c is active for every Uᵢ. Choose one uᵢ∈Uᵢ for each i. The set {c,u₁,…,uₚ} has size p+1=γ and dominates every center, all U vertices and all of W. It is different from D, contradicting uniqueness.

All omitted columns are consequently equal. Relabel the common omitted column v₁¹, one active column v₁⁰, and the other two active columns z,w. The graph is H₂(p,1), completing all same-side cases.

## 5. The balanced eight-vertex exceptions at γ=2

For γ=2 with residual vertices on opposite sides, p=q=1 and both are singleton-dominated. The whole graph is the (3,3) private cell. It has six fixed edges and, at equality, six optional edges. We classify those optional edges without relying on a computation.

First suppose xy is absent, so the cross-edge matrix has six entries. If no row or column is full, all row and column degrees are two; the endpoints of a missing edge give an alternative dominating pair. Thus there is a full row or column. By symmetry assume a full row. No column can be full, or the full row and column vertices would dominate. The remaining three cross-edges occupy each column once in the other two rows. If those row degrees are (2,1), the degree-two row vertex and the other row's neighbour dominate the cell. The degrees must therefore be (3,0), giving K₂,₃ and an unused row, exactly F₀ up to interchange of sides.

Now suppose xy is present. There are five cross-edges, with no full row or column, since a full row gives {x,u} and a full column gives {y,v}. Thus all row and column degrees are (2,2,1). The cross-edge graph, on six vertices, has maximum degree two, no isolated vertices, and five edges. Its only possible component types are P₆ or C₄ disjoint union K₂. In P₆, written u₀v₀u₁v₁u₂v₂, the pair {u₂,v₀} dominates the cell. Hence only C₄ disjoint union K₂ remains, giving F₁.

For completeness, both displayed exceptions satisfy the uniqueness hypothesis. In F₀, the unused U vertex is a leaf at x. A dominating pair must meet its closed neighbourhood {u₂,x} and the disjoint set N[y]={y,v₀,v₁,v₂}. Selecting u₂ leaves either an active U vertex or a V vertex undominated, forcing x; selecting a V vertex rather than y then leaves the other V vertices undominated. Thus {x,y} is the only pair.

In F₁, no U row or V-column is full. A pair with one center other than {x,y} cannot cover the opposite private set. A pair inside U misses y, and a pair inside V misses x. For {u,v} with u∈U,v∈V to dominate, both cross-degrees must be two and uv must be a nonedge. The only cross-degree-two vertices lie in the C₄ component, where every such opposite pair is adjacent. Hence no alternative pair exists. A singleton cannot dominate an eight-vertex graph with these bipartition sizes. Both exceptions are connected, bipartite, and have 12 edges.

Section 4 gives the remaining γ=2 graph H₂(1,1). The degree sequences and bipartition sizes stated above separate all three classes.

## 6. Attainment and isomorphism counts

Every listed H₂ graph has a unique minimum dominating set and attains M₂(γ), by the audited construction theorem. The two exceptions were verified above. For even γ=2k≥4, H₂(k,k) has bipartition sizes {3k,3k+2} while H₂(k+1,k−1) has {3k+1,3k+1}; since both are connected, they are nonisomorphic. For odd γ there is only one allowed split. This proves the stated isomorphism-class counts, with independent mathematical review completed.

## 7. Exact checks and provenance boundary

`check_rigidity.py` gives a complete exact orbit check for the 15 maximal (3,3) patterns at γ=2, using exhaustive permutations of each bipartition class; these form two classes of labelled multiplicities 6 and 9. The same-side H₂(1,1) has a different canonical code. Explicit edge lists and degree sequences appear in `rigidity_certificate.json`.

The checker also enumerates all 164 remaining same-side equality patterns after the proved star reductions for γ=2,3,4,5. It verifies every surviving labelled graph by an explicit bijection to its H₂ representative, and supplies an alternative dominating set for each rejected pattern. The mixed opposite-side cases contain 9 candidates at γ=3 and 576 at γ=4; every one has the explicit (γ−1)-set from Section 2. Sparse residual-incidence checks corroborate the even one-deficit replacement and the odd saturation replacement.

These are exhaustive checks of the analytically reduced cases. They are not unrestricted enumerations of all graphs. No bound for three residual vertices is asserted. This extension inherits the source credits in paper_v2: Koch–Narayan's finite γ=2 results and Erlbacher's prior 13-/14-vertex examples and q=1 subfamily remain prior work. The currently inspected prior write-up does not give this all-γ equality classification; no exhaustive priority claim is made.
