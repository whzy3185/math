# Near-extremal graphs can be far from the unique extremal graph

5 October 2026. Status: complete construction and analytic estimates; independent mathematical audit PASS on 5 October 2026. See audit/OBSTRUCTION_AUDIT.md. The previously reviewed papers and equality addendum are unchanged.

## Metric and class

For graphs G,H with the same number of vertices, define the unlabelled edge-edit distance by

dist(G,H)=min over bijections φ:V(H)→V(G) of |E(G) △ φ(E(H))|.

Each edge addition or deletion costs one. Relabelling is free. The minimum ranges over all vertex bijections, without requiring preservation of the displayed bipartition or the named dominating set.

The class remains finite simple bipartite graphs without isolated vertices, with n=3γ+1 and a unique minimum-cardinality dominating set of size γ. Its sharp maximum is M₁(γ)=γ(γ+7)/2, and its sole extremal graph is H(⌈γ/2⌉,⌊γ/2⌋). The examples below are connected, so imposing connectedness does not remove the obstruction.

## Exact construction

Let k≥2 and 1≤s≤k−1. Start from H(k,k), with centers X={x₁,…,x_k}, Y={y₁,…,y_k}, private pairs Uᵢ={uᵢ⁰,uᵢ¹}, Vⱼ={vⱼ⁰,vⱼ¹}, and residual vertex z. Its edges are xᵢUᵢ, yⱼVⱼ, every U vertex to every vⱼ⁰, and z to all U vertices and all yⱼ.

Choose s rows, say i=1,…,s. In each such row:

1. Delete the k edges uᵢ⁰vⱼ⁰, for all j
2. Add the k edges xᵢyⱼ, for all j
3. Delete zuᵢ⁰

Call the resulting graph G(k,s). Crucially, the residual incidence is deleted at the same private vertex whose selected-column edges were removed. That vertex uᵢ⁰ becomes a leaf at xᵢ; its mate uᵢ¹ retains all its previous edges.

Every change respects the original bipartition. The graph stays connected: z meets every yⱼ, every unmodified U vertex and every uᵢ¹; each xᵢ meets uᵢ¹, each vⱼ⁰,vⱼ¹ meets yⱼ, and each modified uᵢ⁰ meets xᵢ. In particular, there are no isolated vertices.

The graph has γ=2k as proved below, n=6k+1, and

e(G(k,s))=M₁(2k)−s=2k²+7k−s.

Thus its exact edge deficit is t=s.

## Unique minimum domination

Every dominating set must meet each of the following mutually disjoint closed neighbourhoods:

- {xᵢ,uᵢ⁰}=N[uᵢ⁰] for a modified row
- {xᵢ,uᵢ⁰,uᵢ¹}=N[xᵢ] for an unmodified row
- {yⱼ,vⱼ¹}=N[vⱼ¹] for every column

There are 2k such sets. Hence every dominating set has at least 2k vertices, while D=X∪Y is a dominating 2k-set.

A dominating set of cardinality 2k selects exactly one vertex from every forced set and nothing else. Thus z, all vⱼ⁰, and all modified-row uᵢ¹ are absent. In an unmodified row, choosing a U vertex rather than xᵢ leaves its mate undominated. In a modified row, choosing the leaf uᵢ⁰ rather than xᵢ leaves uᵢ¹ undominated: its neighbours are xᵢ,z and the vⱼ⁰. Thus every xᵢ is selected. Finally, choosing vⱼ¹ instead of yⱼ leaves vⱼ⁰ undominated, since all its possible U neighbours have been excluded. Therefore D is the unique minimum dominating set.

The new edges inside D cause no gap in this argument: the forced neighbourhoods use the newly created leaves precisely on those rows whose centers acquire center-to-center edges.

## Degree lower bound under every relabelling

For any fixed bijection between two graphs,

Σ_v |deg_G(v)−deg_H(φ⁻¹(v))| ≤ 2|E(G) △ φ(E(H))|.

Among matchings between two degree multisets, the minimum sum of absolute differences is achieved by matching the sorted sequences. This follows by uncrossing any two reversed matches. Therefore half the sorted degree L1 distance is a lower bound on dist(G,H), independent of bipartition choices or vertex labels.

For H(k,k), the sorted degree groups, as (degree,multiplicity), are

(1,k), (2,k), (3,k), (k+2,2k), (2k+1,k), (3k,1).

For G(k,s), they are

(1,k+s), (2,k−s), (3+s,k), (k+2,2k), (2k+1−s,k), (3k−s,1).

These groups are in nondecreasing order when 1≤s≤k−1; ties are harmless. Matching sorted positions gives L1 distance

s + ks + ks + s = 2s(k+1).

Consequently

s(k+1) ≤ dist(G(k,s),H(k,k)) ≤ s(2k+1).             (1)

The upper bound is simply the displayed modification under the identity labelling: s(k+1) deletions and sk additions. Thus the order of the edit distance is γt throughout this range.

## Two consequences

**No universal square-root-deficit bound.** Take k=s² with s≥2. The lower bound in (1) is s(s²+1), whereas γ√t+t=2s²√s+s. Their ratio tends to infinity. Hence no absolute constant C can bound every graph in this class by

dist(G,H(⌈γ/2⌉,⌊γ/2⌋)) ≤ C(γ√t+t).

**Failure of dense asymptotic edit stability.** Take s=⌊k/2⌋. The edge deficit is O(k)=o(k²), so e(G(k,s))/M₁(2k) tends to one. Nevertheless

liminf dist(G(k,s),H(k,k))/(6k+1)² ≥ 1/72.

Thus near-optimal edge density does not force edit-distance closeness to the extremal graph, even within connected graphs. The meaningful absolute-deficit scale is smaller: an upper bound of order γt would imply normalized edit closeness when t=o(γ), and the construction shows this scale cannot generally be relaxed to all t=o(γ²).

This is an obstruction to edge-edit stability with free relabelling. It does not rule out a different notion based on deleting a small number of vertices, or a stronger statement under extra restrictions such as independence of the unique dominating set.
