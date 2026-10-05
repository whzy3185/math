# Independent audit: sharp unique-domination boundary

Date: 2026-10-05. Mathematical proof audit and independent finite replay: **PASS**.

The complete proposed proofs in `../COUNTEREXAMPLE_FAMILY.md` and `../SHARP_BOUNDARY_THEOREM.md` have been checked. No gap was found in the following claims:

1. For every integer gamma>=2, the largest number of edges in a finite simple bipartite graph without isolated vertices, with n=3gamma+1 and a unique minimum dominating set of size gamma, is gamma(gamma+7)/2
2. The connected construction H(ceil(gamma/2),floor(gamma/2)) attains this bound, so imposing connectedness does not change the maximum
3. For gamma>=4, that extremizer is unique up to graph isomorphism
4. At n=13 and gamma=4, the construction has 22 edges and contradicts the source conjecture's bound 21

This audit does not assert literature novelty or extend the equality classification to gamma=2,3. The general theorem has an elementary proof; the finite checks below are supplementary verification, rather than a substitute for the proof.

## Source statement

The assumptions and formula of [Koch–Narayan, arXiv:2511.01719v1, Conjecture 1](https://arxiv.org/html/2511.01719v1#S1) were checked directly. At n=3gamma+1, its proposed bound reduces to

    2gamma + 2ab + 2a + 1,
    a=ceil(gamma/2), b=floor(gamma/2).

The min-term selects one, and its printed summation cutoff is zero. Therefore the comparison is unaffected by the separately noted distant-range cutoff issue. At gamma=4 the proposed value is 21.

## 1. Two private vertices per dominator

Let D be the unique minimum dominating set. If d in D has exactly one exterior private neighbor u, replacing d by u preserves domination: u dominates itself and d, and every other outside vertex retains a different dominator. This contradicts uniqueness.

If d has no exterior private neighbor, then either another vertex of D dominates d, allowing d to be deleted, or d has no neighbor in D. In the latter case, the no-isolate assumption supplies an outside neighbor u and replacing d by u again preserves domination. Thus every dominator has at least two exterior private neighbors.

Choose two for each dominator. The chosen pairs are disjoint because an exterior private vertex has exactly one neighbor in D. They account for 2gamma vertices, leaving exactly one vertex z besides the gamma dominators.

## 2. Complete edge accounting

Orient the bipartition so z lies on its left side. Let X be the p left-side dominators and Y the q right-side dominators, p+q=gamma. Let U_i be the two right-side private vertices of x_i and V_j the two left-side private vertices of y_j.

The only possible edges are:

- the 2gamma fixed center-to-private edges
- x_i y_j and U_i–V_j edges, grouped by pairs (i,j)
- z–Y and z–U edges

This list includes all edges within D. Every other center-to-private edge is excluded by privacy; every other vertex pair is excluded by bipartiteness. Since D dominates z, z has at least one neighbor in Y, so q>=1. This argument does not require connectedness.

## 3. Local six- and seven-vertex bounds

For a six-vertex cell with two private vertices on each side, there are four fixed edges and five optional edges: xy and the four U–V edges.

If xy is absent, two disjoint U–V edges provide an alternative dominating pair by choosing opposite endpoints. Thus three U–V edges are impossible, and an allowed two-edge pattern must be a star. If xy is present, two U–V edges either contain a disjoint pair or form a star. In the star case, a suitable center together with the star center is an alternative dominating pair. Thus xy can accompany at most one U–V edge. The optional-edge bound is two.

For a seven-vertex cell with two U vertices and three V vertices, there are five fixed edges and seven optional edges. Without xy, five U–V edges force a full U row and another row with at least two entries. The full-row vertex and a V neighbor of the other row form an alternative dominating pair. With xy, a V column containing both U vertices gives the alternative pair consisting of y and that V vertex. Therefore each column has at most one entry, giving at most three U–V edges plus xy. The optional-edge bound is four.

These arguments prove the bounds for every local pattern, independently of enumeration.

## 4. Why local replacements extend globally

This is the principal reduction requiring care.

If z has at least two neighbors in D, removing x_i and y_j from D leaves z dominated by another Y center. Every private vertex outside the six-vertex cell retains its own center. Therefore any other dominating set of size at most two in the induced cell extends to a competing dominating set of size at most gamma in G. The cell must have {x_i,y_j} as its unique dominating set of size at most two, so its optional-edge bound is two.

If z has only one neighbor y_j0 in D, the same argument works for cells with j!=j0. For the distinguished pair (i,j0), use a seven-vertex cell containing z as the third private vertex of y_j0. Then every outside vertex retains its own center, and the same extension argument applies.

Cross-cell edges cause no obstruction: all outside vertices already retain specified dominators, and extra edges can only assist domination. The unique z–y_j0 edge in the second case is counted once globally, not once per seven-vertex cell.

## 5. Upper bound and attainment

If z has at least two D-neighbors, the complete accounting gives

    e(G) <= 2gamma + 2pq + 2p + q.

If it has one, the distinguished seven-cells and remaining six-cells give

    e(G) <= 2gamma + 1 + 4p + 2p(q-1)
          = 2gamma + 1 + 2pq + 2p
          <= 2gamma + 2pq + 2p + q.

The p=0 case is covered directly by the same accounting. Writing d=p-q,

    2gamma+2pq+2p+q = gamma(gamma+7)/2 - d(d-1)/2.

The final term is nonnegative for every integer d. Equality requires d=0 or 1; parity fixes p=ceil(gamma/2), q=floor(gamma/2).

The proposed H(p,q) construction has precisely 2pq+4p+3q edges. Its unique domination proof is valid: the disjoint sets {x_i,b_i^0,b_i^1} and {y_j,a_j^1} force any dominating set to have at least p+q vertices. At equality, choosing a b vertex leaves its mate undominated, so all x_i are selected; choosing a_j^1 then leaves a_j^0 undominated, so all y_j are selected. This also proves attainment and connectedness for every gamma>=2.

## 6. Equality rigidity for gamma>=4

At equality, balanced p,q have q>=2. The one-neighbor case loses q-1 edges and is therefore impossible. Saturation then forces all z–Y and z–U edges and exactly two optional edges in every six-cell.

Three replacement arguments exhaust the remaining freedom:

1. Any center edge x_i y_j allows replacement of x_i by z, contradicting uniqueness. Thus D is independent
2. A two-edge U_i–V_j star centered in U_i allows replacement of x_i,y_j by that U vertex and z. Therefore each cell is a column-star centered at one vertex of V_j
3. If two cells in the same j column choose different V_j vertices, select z, one vertex from each U_i, and every Y center except y_j. This is another dominating set of cardinality 1+p+q-1=gamma

The third alternative dominates all X via the selected U vertices, all U and Y via z, both V_j vertices via the different star choices, and all other private pairs via retained Y centers. Therefore the chosen V_j vertex is constant across i. Renaming the two vertices of each V_j now yields exactly H(p,q). This proves the stated uniqueness up to isomorphism.

## 7. Independent finite replay

The independently authored `independent_check.py` imports no primary checker and uses adjacency bitsets and closed-neighborhood unions. It verifies:

- all 32 six-cell and 128 seven-cell patterns, including each complete list of dominating sets of size at most two
- exactly 14 admissible six-cell patterns, maximum two optional edges
- exactly 58 admissible seven-cell patterns, maximum four optional edges
- all 8192 subsets of the saved 13-vertex graph: it is simple, connected, bipartite, has 22 edges, domination number four, and exactly one minimum dominating set
- balanced H instances for gamma=2,3,4,5,6, with edge counts 9,15,22,30,39 and unique minimum dominating sets
- all 4096 saturated local-pattern assemblies for p=q=2: exactly four labeled graphs remain uniquely dominated, corresponding precisely to the consistent column choices in H(2,2)

Results and input hashes are in `independent_check_result.json`; the fresh execution output is saved separately. These checks corroborate every local finite assertion and the first equality case. The all-gamma proof rests on the arguments above, not on extrapolation from those instances.
