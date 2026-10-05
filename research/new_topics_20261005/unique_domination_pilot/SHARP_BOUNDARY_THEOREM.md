# Sharp edge extremality one vertex above the unique-domination threshold

Status: complete elementary proof; independent mathematical audit PASS on 5 October 2026. See audit/PROOF_AUDIT.md. The explicit counterexample family and source comparison are separately frozen in COUNTEREXAMPLE_FAMILY.md. The stated equality classification for gamma>=4 passed that audit.

## Theorem

For every integer γ>=2, among all finite simple bipartite graphs G without isolated vertices, with |V(G)|=3γ+1 and exactly one minimum dominating set of size γ,

max |E(G)| = γ(γ+7)/2.

The same maximum holds when connectedness is additionally required. For γ>=4, equality holds, up to graph isomorphism, only for H(ceil(γ/2),floor(γ/2)), the connected graph defined in COUNTEREXAMPLE_FAMILY.md.

The assertions at γ=2,3 give maxima 9,15, respectively. The uniqueness-of-isomorphism assertion here is restricted to γ>=4.

## Lemma 1: two exterior private neighbours

If D is a unique minimum dominating set in a graph without isolated vertices, every d∈D has at least two exterior private neighbours, that is, vertices u∉D with N(u)∩D={d}.

Proof. If exactly one exists, call it u; replacing d with u gives a different dominating set of the same size. If none exists and d has a neighbour in D, delete d to get a smaller dominating set. If none exists and d has no neighbour in D, choose any neighbour u outside D, which exists by the no-isolate assumption; replace d with u. Every vertex other than d that could lose domination was an exterior private neighbour, and in the replacement case d is dominated by u. Each case contradicts minimum cardinality or uniqueness. QED.

## Lemma 2: the six-vertex cell

Take two centers x,y in opposite bipartition classes, two private vertices U={u0,u1} adjacent to x, and two private vertices V={v0,v1} adjacent to y. No cross-center/private incidences are allowed. In addition to those four fixed edges, the only possible edges are xy and the four edges between U and V. If {x,y} is the unique dominating set of size at most two in this induced cell, at most two additional edges are present.

More precisely, when exactly two additional edges occur:

- without xy, the U–V edges form a two-edge star
- with xy, exactly one U–V edge occurs

Proof. Without xy, two disjoint U–V edges give an alternative dominating pair: choose opposite endpoints of the two edges. Three U–V edges necessarily contain a pair of disjoint edges, so at most two are possible, and a two-edge configuration must be a star. With xy, two U–V edges either are disjoint, giving the same alternative, or form a star. A star centered at u∈U gives the alternative pair {x,u}; a star centered at v∈V gives {y,v}. Thus at most one U–V edge can accompany xy. QED.

## Lemma 3: the seven-vertex cell

Use the same setup but |U|=2 and |V|=3, with the five center/private edges fixed. If {x,y} is the unique dominating set of size at most two, at most four additional edges (xy plus U–V edges) occur.

Proof. Without xy, five U–V edges force one of the two U rows to meet all three V vertices and the other row to meet at least two. Let u be the full row and choose v adjacent to the other U vertex. Then {u,v} dominates the cell, contradiction. Therefore at most four U–V edges occur. With xy, any v adjacent to both U vertices gives the alternative dominating pair {y,v}. Each V column therefore has at most one edge, giving at most three U–V edges and at most four additional edges in total. QED.

**Exhaustive local certificate.** check_local_cells.py independently enumerates all 32 six-vertex and all 128 seven-vertex edge patterns, testing every vertex subset of size at most two. The certificate lists every pattern and every qualifying dominating set. There are 14 admissible six-vertex patterns, with maximum two additional edges, and 58 admissible seven-vertex patterns, with maximum four. In the seven-vertex case, the maximum patterns are precisely K_(2,2) between U and two of the three V vertices, with the third V column empty and xy absent. The proof of the global upper bound needs only the displayed upper bounds, not this stronger seven-vertex equality description.

## Global reduction

Let D be the unique minimum dominating set of G, |D|=γ. Select two exterior private neighbours for each d∈D. These 2γ selected vertices are distinct, so there is exactly one vertex z outside D and outside the selected pairs.

Orient the bipartition as A∪B so that z∈A. Write

D∩A={x1,…,xp}, D∩B={y1,…,yq}; p+q=γ.

Let U_i⊂B be the chosen private pair of x_i and V_j⊂A the pair of y_j. Since D dominates z, the set J=N(z)∩D is a nonempty subset of D∩B, so q>=1. Put t=|J|.

The only edges of G are:

- 2γ fixed center/private incidences
- edges x_i y_j and edges between U_i and V_j
- edges from z to the y_j in J and to the U_i

Private-neighbourhood definitions exclude all other center/private edges. Bipartiteness excludes all same-part incidences. Thus this accounting is complete, including edges inside D.

### Case I: t>=2

Fix i,j and let K_ij={x_i,y_j}∪U_i∪V_j. The set D\{x_i,y_j} dominates every vertex outside K_ij: selected private vertices outside the cell have their own retained center, and z retains at least one neighbour in J because only one y-center was removed.

Consequently any alternative dominating pair in G[K_ij] would extend, together with D\{x_i,y_j}, to a different dominating γ-set in G. A dominating set of smaller size in the cell would give one of size <γ in G. Therefore Lemma 2 applies, and the additional edges in each pair block total at most two.

The pair blocks partition every edge not incident with z or one of the fixed private incidences. Also deg(z)<=2p+q. Hence

e(G)<=2γ+2pq+2p+q.                                          (1)

This argument includes p=0, when the sum of pair blocks is empty.

### Case II: t=1

Write J={y_j0}. For j≠j0, the same six-vertex argument works, because y_j0 is retained and dominates z.

For each i, use instead the seven-vertex cell

L_i={x_i,y_j0}∪U_i∪V_j0∪{z}.

It has private-set sizes two and three. The set D\{x_i,y_j0} dominates every vertex outside L_i, so Lemma 3 applies. Its additional edges comprise x_i y_j0 and the U_i incidences to V_j0∪{z}. These sets of additional edges are disjoint over i. The edge zy_j0 is counted once separately, not once per cell. Therefore

e(G)<=2γ+1+2p(q−1)+4p
     =2γ+1+2pq+2p
     <=2γ+2pq+2p+q,                                        (2)

using q>=1. If p=0, the graph has only the 2γ fixed edges plus zy_j0 and the same bound holds.

### Optimization

Let d=p−q. Since p+q=γ,

2γ+2pq+2p+q = γ(γ+7)/2 − d(d−1)/2.

For every integer d, d(d−1)>=0. This proves the upper bound γ(γ+7)/2. Equality in this numerical optimization requires d=0 or d=1; parity then forces

p=ceil(γ/2), q=floor(γ/2).

## Attainment

The graph H(p,q) from COUNTEREXAMPLE_FAMILY.md is connected, bipartite and has a unique minimum dominating set of size p+q. Its edge count is 2pq+4p+3q. Set p=ceil(γ/2), q=floor(γ/2). The optimized expression equals γ(γ+7)/2, proving attainment for every γ>=2 and for the connected subclass.

## Equality rigidity when γ>=4

Suppose e(G)=γ(γ+7)/2 and γ>=4. Optimization gives p=ceil(γ/2), q=floor(γ/2)>=2. Case II is strictly below the bound by q−1, so Case I applies.

Every inequality in (1) is now an equality. In particular,

- z is adjacent to every y_j and to both vertices of every U_i
- every pair block has exactly two additional edges

First, no edge x_i y_j can exist. Otherwise (D\{x_i})∪{z} is a different dominating set of size γ: the removed x_i is dominated by the retained y_j; U_i is dominated by z; all other private pairs keep their centers. Hence D is independent.

Lemma 2 now says each U_i–V_j block is a two-edge star. It cannot be centered at u∈U_i: replacing x_i,y_j by u,z gives a different dominating γ-set. The two vertices of V_j are dominated by u, both vertices of U_i by z or membership in the set, x_i by u, and y_j by z; other vertices are covered by the retained centers. Therefore the two-edge star is centered at one of the two vertices of V_j. Denote its chosen center by v_j^(i).

For a fixed j these centers cannot differ with i. Suppose both V_j vertices occur among the v_j^(i). Choose one vertex u_i from each U_i and set

K={z} ∪ {u_i:1<=i<=p} ∪ (D∩B\{y_j}).

Then |K|=1+p+(q−1)=γ. Every x_i is dominated by u_i; every U_i vertex by z; all y-centers by z; the pair V_j is dominated because both star choices occur; all other V_l pairs retain y_l. Thus K is another minimum dominating set, contradiction.

For each j, swap the labels in V_j if necessary so all blocks choose v_j^0. The resulting adjacency description is exactly H(p,q). This proves the stated isomorphism uniqueness for γ>=4.

## Source comparison

At n=3γ+1 the source proposes 2γ+2ab+2a+1, whereas the sharp expression above is γ(γ+7)/2=2ab+3γ+a. The gap is b−1. Thus the first failure in this particular n=3γ+1 family occurs at γ=4. This is not a claim that n=13 is the smallest counterexample in the source's entire n,γ domain.

## Audit boundary

The local-pattern classifications and the 13-vertex graph have exact independently coded finite checks. The general upper bound and equality proof above passed independent mathematical review at the stated scope. No claim of Lean verification or publication novelty is made here.

## Prior-work attribution update, 5 October 2026

The 13-vertex, 22-edge example and the printed-cutoff issue were already reported in John Erlbacher's public [Demonstrandum counterexample package](https://github.com/demonstrandum-research/artifacts/blob/94db9ed50d48a57aae5ccb72e6a95a2b8f8f39d3/problems/p2-factory/kills/koch-narayan/WRITEUP.md), whose Git commit is dated 13 June 2026. An explicit isomorphism and fresh exhaustive check are in extension/prior_work/. The present contribution is framed as the all-gamma sharp boundary maximum and equality theorem; no proof of that general theorem was located in the inspected prior package. This is a bounded source comparison, not an exhaustive priority claim. Mathematical statements and audit conclusions are unchanged.
