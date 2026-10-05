# Two vertices above the unique-domination threshold

5 October 2026. **Status: complete analytic proof; independent mathematical audit PASS on 5 October 2026. See audit/PROOF_AUDIT.md.** The previously audited one-extra-vertex paper is unchanged.

## Theorem

For every integer γ≥2, let G range over finite simple bipartite graphs without isolated vertices, of order n=3γ+2, with a unique minimum-cardinality dominating set of size γ. Then

max e(G) = M₂(γ) := ⌈γ²/2⌉ + 5γ.

Connected graphs attain the maximum. For every even γ≥4 there are at least two nonisomorphic connected extremal graphs. No complete equality classification is asserted here.

The values at γ=2,3,4,5 are 12,20,28,38. The γ=2 value is already a special case of Koch–Narayan's Theorem 11. Erlbacher previously reported the γ=4 value 28 by a finite exhaustive search, with a single-implementation qualification, and supplied a directly checkable extremal example. Precise overlap is recorded in `SOURCE_COMPARISON.md`.

## 1. Private neighbours and local cells

Let D be the unique minimum dominating set. Every d∈D has at least two exterior private neighbours: vertices v outside D with N(v)∩D={d}. The standard replacement proof, included in the audited one-extra-vertex argument, uses no assumption beyond the absence of isolated vertices. Choose two such vertices for every d. These 2γ vertices are distinct. There are exactly two residual vertices z,w outside D and the selected pairs.

Consider a cell with centers x,y in opposite parts, private sets U,V of sizes a,b, all edges xU and yV, and no cross-center/private incidences. Its only other possible edges are xy and UV. In each application below, the retained centers outside the cell dominate every vertex outside the cell. Therefore a second dominating set of size at most two inside the cell would extend to a global dominating set of size at most γ, violating minimum cardinality or uniqueness. This condition is justified separately for every cell type; it is not assumed merely because the vertices are private.

Write L(a,b) for an upper bound on the number of optional edges xy and UV in a cell whose only dominating set of size at most two is {x,y}.

**Local bounds:**

L(2,2)=2, L(2,3)=4, L(2,4)=6, and L(3,3)=6.

Here equality means that each displayed upper bound can be attained; the global argument only uses the inequalities.

**Proof for (2,2).** If xy is absent, any three UV edges contain two disjoint edges. Opposite endpoints of those two edges give an alternative dominating pair. If xy is present, two UV edges either are disjoint, with the same consequence, or form a two-edge star. A star centered at u∈U gives the alternative {x,u}, and one centered at v∈V gives {y,v}. Thus there are at most two optional edges.

**Proof for (2,s), s=3,4.** If xy is absent and there are at least 2s−1 UV edges, one U row is full and the other has a neighbour v. Select the full row vertex u and v. They dominate both centers, all of V, and both members of U. This contradicts uniqueness. Thus there are at most 2s−2 UV edges. If xy is present, a full V-column gives the alternative pair {y,v}. Every column consequently has at most one UV edge, so there are at most s+1≤2s−2 optional edges.

**Proof for (3,3).** Suppose there are at least seven optional edges. If xy is absent, the 3×3 UV matrix has at most two missing entries. It therefore has a full row and a full column. Their vertices form an alternative dominating pair. If xy is present, there are at least six UV edges. A full U row gives {x,u}, and a full V-column gives {y,v}. Otherwise every row and column has degree at most two. Six UV edges force all row and column degrees to be exactly two; the missing edges form a perfect matching. The endpoints of any missing edge form an alternative dominating pair, since each covers every opposite private vertex other than the selected endpoint. This is again impossible.

The bounds are attained by: a two-edge star for (2,2); K₂,₂ with an unused third column for (2,3); K₂,₃ with an unused fourth column for (2,4); and K₂,₃ with an unused third row for (3,3). A direct forced-neighbourhood check proves the center pair unique in each example. The exact local enumeration in `local_patterns.json` independently corroborates all four bounds.

## 2. Both residual vertices in the same part

Orient the bipartition as A∪B with z,w∈A. Write D∩A=X={x₁,…,xₚ} and D∩B=Y={y₁,…,y_q}; p+q=γ. Let Uᵢ⊂B be the selected private pair of xᵢ and Vⱼ⊂A the selected private pair of yⱼ. Since D dominates each residual vertex, each has a nonempty D-neighbourhood contained in Y. In particular q≥1; p=0 is permitted.

Call a residual vertex singleton-dominated if it has exactly one neighbour in D. Let S∈{0,1,2} be the number of such residual vertices, and rⱼ the number whose sole D-neighbour is yⱼ. Thus Σrⱼ=S.

For each i,j, take the cell with centers xᵢ,yⱼ, private set Uᵢ of size two, and opposite private set consisting of Vⱼ plus the rⱼ residual vertices owned by yⱼ. Every vertex outside the cell retains domination from D\{xᵢ,yⱼ}:

- each selected private vertex outside has its own retained center;
- a singleton-dominated residual outside is owned by a different retained y-center;
- a residual with at least two D-neighbours retains one, since only one Y-center is removed.

The cell bound is therefore L(2,2+rⱼ)≤2+2rⱼ. These cell optional-edge sets are pairwise disjoint. The 2γ selected private incidences are counted once. Each singleton residual contributes its one center edge separately. Each of the other 2−S residuals has degree at most 2p+q, because it can meet only the selected U vertices and Y; the residuals have no edge between them. Consequently

e(G) ≤ 2γ + S + Σᵢ,ⱼ(2+2rⱼ) + (2−S)(2p+q)

       = 2γ+2pq+4p+2q − S(q−1)

       ≤ 2pq+6p+4q.                                      (1)

This accounting includes p=0, when no cells occur. With d=p−q, the final expression is

γ²/2 + 5γ + 1/2 − (d−1)²/2.

If γ is even, d is even and (d−1)²≥1. If γ is odd, (d−1)²≥0. In either case (1) is at most M₂(γ).

## 3. Residual vertices in opposite parts

Now z∈A and w∈B, with the same center and private-pair notation. Put J=N(z)∩D⊆Y and K=N(w)∩D⊆X. Both are nonempty, so p,q≥1. An edge zw is possible and must be included in the accounting.

### 3.1 Both residuals have at least two D-neighbours

For every i,j the ordinary six-vertex cell {xᵢ,yⱼ}∪Uᵢ∪Vⱼ is valid: outside selected private vertices keep their centers, z retains a Y-neighbour, and w retains an X-neighbour. The cells contribute at most 2pq optional edges. The incidences of z other than zw number at most 2p+q; those of w other than zw number at most 2q+p. Count zw once. Hence

e(G) ≤ 2γ+2pq+(2p+q)+(2q+p)+1

       = 2pq+5γ+1.                                      (2)

For odd γ, 2pq≤⌊γ²/2⌋ immediately gives e(G)≤M₂(γ).

For even γ, the right side of (2) is at most M₂(γ)+1. An actual violation of the desired bound would, by integrality, force equality in (2), p=q, and saturation of every residual degree bound. In particular, z is adjacent to all Y and all Uᵢ, and w to all X and all Vⱼ. Choose any i,j. Then

(D\{xᵢ,yⱼ}) ∪ {z,w}

is a different dominating γ-set. The removed centers are covered by w,z respectively; Uᵢ is covered by z and Vⱼ by w; other private pairs keep their centers; both residuals are selected. This contradiction excludes the sole possible one-edge excess and proves the required bound.

### 3.2 Exactly one residual is singleton-dominated

After interchanging the bipartition sides if necessary, suppose J={yⱼ₀}, while |K|≥2. For j≠j₀ the ordinary six-vertex cells are valid. For j=j₀ include z, giving a (2,3) private cell for every i. Outside any of these cells, w retains a member of K and every other omitted vertex keeps its center. The optional blocks therefore contribute at most 2p(q−1)+4p.

Count zyⱼ₀ once separately, and bound the remaining incidences of w by 2q+p, plus at most one edge zw. Then

e(G) ≤ 2γ+1+2p(q−1)+4p+(2q+p)+1

       = 2pq+5γ+2−q.                                    (3)

If q≥2, (3) is at most 2pq+5γ≤M₂(γ). If q=1, then p≥2 because |K|≥2, so γ≥3. The difference between M₂(γ) and the right side of (3) is

⌈γ²/2⌉−2γ+1 ≥ 0.

It is zero at γ=3 and positive for γ≥4. Thus (3) always gives the required bound.

### 3.3 Both residuals are singleton-dominated

Write J={yⱼ₀}, K={xᵢ₀}. Partition optional edges into the following cells:

- for i≠i₀,j≠j₀, a (2,2) cell;
- for i=i₀,j≠j₀, a (3,2) cell that includes w;
- for i≠i₀,j=j₀, a (2,3) cell that includes z;
- for i=i₀,j=j₀, a (3,3) cell that includes both z and w.

Every residual whose owner is removed is included in that cell. Every residual outside the cell retains its owner. All selected private vertices outside likewise retain their centers. Hence each local uniqueness condition is legitimate.

The edge zw belongs only to the (3,3) cell, so it is neither lost nor counted twice. The two residual-to-owner edges are fixed incidences, counted once each. All other optional edge sets are disjoint. The four local bounds yield

e(G) ≤ 2γ+2 + 2(p−1)(q−1) + 4(q−1) + 4(p−1) + 6

       = 2pq+4γ+2

       ≤ ⌊γ²/2⌋+4γ+2 ≤ M₂(γ),                            (4)

because γ≥2. This completes the candidate upper-bound proof.

## 4. Attainment by a twin-residual family

For p,q≥1 construct H₂(p,q) from centers X,Y and private pairs Uᵢ,Vⱼ as in the one-extra-vertex family, with two additional vertices z,w in the X-side. The exact edge list is:

1. xᵢ joined to both vertices of Uᵢ;
2. yⱼ joined to both vertices of Vⱼ;
3. every Uᵢ vertex joined to vⱼ⁰, for every i,j;
4. each of z,w joined to every Uᵢ vertex and every yⱼ;
5. no other edges, in particular no edge zw.

This graph has 3(p+q)+2 vertices and

e(H₂(p,q))=2pq+6p+4q.                                    (5)

It is connected and bipartite. Every dominating set must meet each of the p disjoint closed neighbourhoods N[xᵢ]={xᵢ,uᵢ⁰,uᵢ¹} and each of the q disjoint closed neighbourhoods N[vⱼ¹]={yⱼ,vⱼ¹}. These p+q sets are mutually disjoint, so at least γ=p+q choices are necessary. The set D=X∪Y dominates and has that size.

A dominating γ-set selects exactly one vertex of each forced set and no other vertices. Thus z,w and every vⱼ⁰ are absent. Selecting uᵢ⁰ or uᵢ¹ in place of xᵢ leaves its mate undominated, forcing every xᵢ. Then selecting vⱼ¹ instead of yⱼ leaves vⱼ⁰ undominated, forcing every yⱼ. Therefore D is the unique minimum dominating set.

Choose p=⌈γ/2⌉, q=⌊γ/2⌋. Formula (5) equals M₂(γ), proving attainment for every γ≥2.

For even γ=2k≥4, both (p,q)=(k,k) and (k+1,k−1) attain (5). Their connected bipartition size pairs are respectively {3k,3k+2} and {3k+1,3k+1}. Connected bipartite graphs have their bipartition unique up to swapping sides, so these graphs are nonisomorphic. This establishes nonuniqueness of equality, without asserting that these are all equality graphs.

## 5. Verification and limits

`check_two_extra.py` enumerates every optional pattern in the four required cells: 32,128,512,1024 patterns. For each it enumerates all vertex subsets of size at most two. The admissible counts are 14,58,254,548, and the maximum optional-edge counts are 2,4,6,6.

It also checks all vertex subsets in every H₂(p,q) with p,q≥1 and 2≤p+q≤5, at most 17 vertices. The unique minimum dominating set, connectivity, bipartiteness and exact edge count are verified for all ten parameter pairs. It explicitly maps H₂(3,1) to Erlbacher's prior 14-vertex certificate and rechecks its minimum dominating sets.

These computations corroborate the local inequalities and the proposed constructions. They are not a complete enumeration of all global graphs, and they do not substitute for independent review of Sections 2–3. No general result for three or more residual vertices, complete equality classification, Lean verification, or publication priority is claimed.
