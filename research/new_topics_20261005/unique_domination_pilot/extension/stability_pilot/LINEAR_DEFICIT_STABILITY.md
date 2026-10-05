# An absolute-deficit stability estimate

5 October 2026. Status: complete analytic proof; independent mathematical audit PASS on 5 October 2026. See audit/linear_upper/UPPER_BOUND_AUDIT.md. This result concerns only n=3γ+1. It does not alter the frozen papers.

## Theorem

Let G be a finite simple bipartite graph without isolated vertices, of order 3γ+1, with a unique minimum-cardinality dominating set of size γ≥2. Put

t=γ(γ+7)/2−e(G)≥0,

and let H*=H(⌈γ/2⌉,⌊γ/2⌋), the unique extremal graph. For unlabelled edge-edit distance, with one cost per edge addition or deletion and arbitrary free vertex relabelling,

dist(G,H*) ≤ 12γt.                                      (1)

At t=0 the right side is zero, as supplied by the audited equality theorem. The construction in EDIT_STABILITY_OBSTRUCTION.md gives a matching order Ω(γt) for even γ and 1≤t≤γ/2−1. Thus the dependence on γ and t in (1) has the correct order in that regime, although the constant 12 is not claimed optimal.

Connectedness is not assumed for the upper bound. The lower-bound examples are connected.

## 1. Exact slack decomposition when the residual has several owners

Choose two exterior private neighbours per center in the unique minimum dominating set D, leaving a residual vertex z. Put z in side A, with p centers X in A and q centers Y in B. Let Uᵢ and Vⱼ be the selected private pairs. Then p+q=γ and q≥1. Suppose first |N(z)∩D|≥2.

The audited six-cell argument gives kᵢⱼ≤2 optional edges in each block consisting of xᵢyⱼ and Uᵢ–Vⱼ. Define

B=(p−q)(p−q−1)/2,

L=Σᵢ,ⱼ(2−kᵢⱼ),

R=(2p+q)−deg(z).

All three are nonnegative integers. Complete edge accounting gives the exact identity

t=B+L+R.                                             (2)

No degree outside the allowable residual neighbourhood is omitted: z can meet only Y and the U vertices.

## 2. Repair to a coherent template at the same split

For this intermediate step, allow p=0 and define T(p,q) by the same adjacency rule as H(p,q), with its X-side center collection empty when p=0. The final balanced target still has both center sides nonempty.

Call row i bad if z misses a member of Uᵢ, and column j bad if z misses yⱼ. Write their counts as b_X,b_Y. If R_U and R_Y count the corresponding missing residual edges, then

b_X≤R_U, b_Y≤R_Y, R_U+R_Y=R.

On a good row, no edge xᵢyⱼ can occur: replacing xᵢ by z covers its private pair, while xᵢ is dominated by the retained yⱼ. Every other vertex keeps its owner.

Consider a block in a good row and good column with kᵢⱼ=2. Its cross-edges must form a two-edge star. A star centered at u∈Uᵢ would allow the replacement of xᵢ,yⱼ by u,z, because z covers all Uᵢ and yⱼ. Hence the block is a column star, joining both Uᵢ vertices to one member of Vⱼ.

For each good column, the selected member of Vⱼ is the same in every such good, saturated row. Otherwise choose two good rows i,h with opposite choices, and choose uᵢ∈Uᵢ, u_h∈U_h. The set

(D\{xᵢ,x_h,yⱼ}) ∪ {z,uᵢ,u_h}

is another dominating γ-set. The removed X-centers are covered by their chosen U vertices; both U pairs are covered by z; yⱼ is covered by z; the two Vⱼ vertices are covered by the differing column choices. All other private pairs retain their centers. This contradiction proves coherence without requiring any information about the other rows.

Choose this common column for each good column, choosing arbitrarily when no good saturated row is available. Choose arbitrary target columns for the bad columns. These choices define a labelled T(p,q).

The fixed center/private edges already agree. Add the R missing residual incidences. A block touching a bad row or column costs at most four edits, since each graph has at most two optional edges there. The same bound applies to an unsaturated good block, and the number of such blocks is at most L. Every other block already agrees with the template. Therefore

dist(G,T(p,q)) ≤ R+4L+4(qb_X+pb_Y)

                 ≤ (4γ+1)R+4L

                 ≤ (4γ+1)t.                              (3)

The first distance here may use the displayed common labelling; minimizing over relabellings can only reduce it. The argument also includes p=0, when there are no cross blocks.

## 3. Balance the template

Let a=⌈γ/2⌉, b=⌊γ/2⌋, and h=|p−a|. From the parity of p−q and the definition of B,

h²≤B≤t.                                                (4)

Indeed writing p=a+m gives B=2m²−m for even γ and B=2m²+m for odd γ. For integer m, either expression is at least m².

Move h center/private triples from the larger-than-target center side to the other role. Keep the residual and all remaining triples fixed, and use the same selected-column labels on unchanged Y-triples. This defines a bijection to T(a,b)=H*. The two templates agree on every edge whose endpoints both lie outside the moved triples.

For a moved X-triple, the sum of its three vertex degrees in the old template is 2q+6; in its new Y-role the sum is 2a+5. Their sum is 2γ−2h+11. For a moved Y-triple, the old sum is 2p+5 and the new X-role sum is 2b+6, again giving 2γ−2h+11. Counting every changed edge by an incident moved vertex, and allowing repeated counting for an upper bound, gives

dist(T(p,q),H*) ≤ h(2γ−2h+11) ≤ (2γ+11)√t.               (5)

Combining (3) and (5), the multiple-owner case satisfies the more explicit estimate

dist(G,H*) ≤ (4γ+1)t+(2γ+11)√t.                          (6)

For integer t≥1, √t≤t, so this is at most (6γ+12)t≤12γt because γ≥2.

## 4. A single owner

Suppose N(z)∩D consists of one Y-center. The audited upper bound yields

t≥B+q−1=((p−q−1)²+γ−3)/2.

Using the parity of p−q gives

t≥⌊(γ−2)/2⌋.                                         (7)

If t=0, the audited equality classification already gives G≅H*. If t≥1 and γ=2 or 3, the trivial estimate dist(G,H*)≤e(G)+e(H*)≤γ(γ+7) is at most 12γt. If γ≥4, (7) and the elementary inequality

γ+7≤12⌊(γ−2)/2⌋

give the same conclusion. Thus (1) holds in every case.

## 5. Interpretation and audit boundary

The upper proof isolates three exact sources of edge deficit: split imbalance B, optional-cell deficit L, and residual-incidence deficit R. Good saturated blocks have a common column orientation by a three-center replacement. All arbitrary behaviour is confined to the blocks meeting missing residual incidences or deficient cells; repairing that region costs order γt.

The lower construction makes one missing residual incidence per modified row while changing an entire row of edge types. This explains why a single local deficit can carry order γ global edit cost, and why summing those costs is genuinely necessary.

The proof is analytic. Bounded numerical checks of the construction and arithmetic accompany it; they do not establish the all-graph upper estimate. No corresponding second-boundary stability theorem is claimed here.
