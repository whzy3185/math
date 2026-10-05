# Independent audit of absolute-deficit edge-edit stability

Date: 2026-10-05. General analytic proof and independent constructive checks: **PASS**.

## Audited statement

Let G be finite, simple, bipartite and without isolated vertices, with n=3 gamma+1, gamma>=2, and a unique minimum-cardinality dominating set of cardinality gamma. Put

    t=gamma(gamma+7)/2-e(G).

Then, for unrestricted unlabelled edge-edit distance with unit cost per edge addition or deletion,

    dist(G,H(ceil(gamma/2),floor(gamma/2))) <=12 gamma t.

The edge deficit is a nonnegative integer by the audited sharp-boundary theorem. At t=0, the already audited equality classification gives distance zero. Connectedness is not required for the upper bound.

This report audits LINEAR_DEFICIT_STABILITY.md separately from the frozen obstruction report. The lower examples establish matching order Omega(gamma t) for even gamma and 1<=t<=gamma/2-1. No assertion of a matching lower bound for every possible deficit, an optimal constant, or a corresponding second-boundary stability theorem is made.

## Reduction and exact slack

Select two exterior private neighbors per center of the unique minimum dominating set, leaving residual z. Orient the bipartition with z on the side containing p centers and q opposite centers, p+q=gamma and q>=1.

When z has at least two center-neighbors, every ordinary six-cell is valid: after removing one center from each side, z still has an owner outside the cell. Thus each optional block x_i y_j together with U_i-V_j has at most two edges.

With

    B=(p-q)(p-q-1)/2,
    L=sum_(i,j)(2-k_ij),
    R=(2p+q)-deg(z),

all terms are nonnegative integers. Fixed center/private incidences contribute 2 gamma; optional cells and residual incidences account for every remaining edge. Direct subtraction from the sharp maximum gives the exact identity

    t=B+L+R.

It is essential that this identity uses the multiple-owner case. The singleton-owner case is not silently subjected to the ordinary six-cell bounds; it is handled separately.

## Coherence on good saturated blocks

A row is good if both its U vertices meet z, and a column is good if its Y-center meets z.

On a good row, a center edge x_i y_j would allow the replacement D-x_i+z: x_i is covered by retained y_j, its private pair by z, and every other selected private vertex keeps its own center. Hence no such edge exists.

A good-row/good-column block with exactly two optional edges must consequently be a private-private star. A row-centered star would allow the replacement of x_i,y_j by its U-center and z. The good-row and good-column assumptions provide exactly the residual incidences required to cover the removed centers and private pairs. Thus every such block is a column star.

Suppose two good saturated rows choose different private columns of the same good Y-column. Replacing those two X-centers and that Y-center by z and one vertex from each of the two U pairs gives a distinct dominating gamma-set. Both U pairs are covered by z, both removed X-centers by their chosen U vertices, the removed Y-center by z, and both V vertices by the differing column choices. All other private pairs keep their owners. This argument requires no information about other rows.

Therefore every good column has a coherent target orientation on all its good saturated rows. If there are no such rows, its target orientation can be chosen arbitrarily. This proves the repair rule for every configuration, not only a dense or nearly balanced one.

## Labelled repair at the original split

The intermediate template T(p,q) uses the H adjacency rule, with p=0 explicitly permitted. Its fixed private incidences are already present in G.

Add the R missing residual edges. Let b_X and b_Y be the numbers of bad rows and columns. A block touching one of them costs at most four edits: G has at most two optional edges there and T has exactly two. The same conservative bound covers an unsaturated good block, and the number of such blocks is at most L. All other blocks already agree with the coherent target.

Counting the union of bad-row and bad-column blocks by an upper bound, allowing overlaps, gives

    dist(G,T(p,q)) <=R+4L+4(q b_X+p b_Y).

Since b_X<=R_U, b_Y<=R_Y and R_U+R_Y=R,

    dist(G,T(p,q)) <=(4 gamma+1)R+4L
                   <=(4 gamma+1)t.

No edges are omitted from this repair accounting. Double-counting overlapping exceptional blocks only increases the bound. The proof also covers p=0, when the block family is empty.

## Balancing by an explicit vertex bijection

Let a=ceil(gamma/2), b=floor(gamma/2), and h=|p-a|. Writing p=a+m gives

    B=2m^2-m for even gamma,
    B=2m^2+m for odd gamma.

For integral m each expression is at least m^2. Hence h^2<=B<=t.

Move h center/private triples to the other center role, preserve residual z and the roles of all other triples, and match the selected private-column labels of unchanged Y-triples. This is a genuine full vertex bijection; it need not preserve the original bipartition because the metric allows arbitrary relabelling.

Under this bijection, all edges between unchanged vertices agree. Every differing edge therefore touches a moved triple. The old X-triple degree sum is 2q+6 and the new Y-role sum is 2a+5. In the reverse move the sums are 2p+5 and 2b+6. In either direction their sum is

    2 gamma-2h+11.

Summing over moved triples bounds the symmetric difference by

    h(2 gamma-2h+11) <=(2 gamma+11)sqrt(t).

Repeated counting of edges incident with multiple moved vertices is harmless in this upper bound. The proof does not assume an edit path remains in the extremal graph class.

The triangle inequality, or composition of the displayed labelled repairs and bijection, now gives in the multiple-owner case

    dist(G,H*) <=(4 gamma+1)t+(2 gamma+11)sqrt(t).

For the integer t>=1, sqrt(t)<=t. The result is at most (6 gamma+12)t<=12 gamma t for gamma>=2.

## Singleton-owner case and small parameters

The already audited singleton-owner upper bound gives

    t>=B+q-1=((p-q-1)^2+gamma-3)/2.

Parity of p-q yields

    t>=floor((gamma-2)/2).

If t=0, use the equality classification. For t>=1 and gamma=2 or 3, the trivial bound dist<=e(G)+e(H*)<=gamma(gamma+7) is at most 12 gamma t. For gamma>=4,

    gamma+7<=12 floor((gamma-2)/2),

including the tight arithmetic checks at gamma=4,5. Combining this with the deficit lower bound proves the same estimate. This handles every singleton-owner graph and does not import the multiple-owner coherence assumptions into that case.

## Independent computations

The computations below import no primary checker. They corroborate the stated proof and test its constructive maps; the universal conclusion is the analytic argument above.

### Slack, coherence and repair

check_repair.cpp reconstructs and checks:

- Every selected-private-pair skeleton at gamma=2 and gamma=3
- Every gamma=4, p=q=2 multiple-owner skeleton whose four six-cells satisfy the necessary local uniqueness condition, with all sixteen choices of residual-U incidences

The local cell palette is generated by a separate exact enumeration, not imported from certificate flags. Altogether this covers 643,466 candidate graphs. Exact tests find 178,632 graphs with the specified unique minimum dominating set: 174,411 multiple-owner cases and 4,221 singleton-owner cases. Ten representations have zero deficit.

For every applicable graph the code checks the exact slack identity, nonnegative deficits, good-row center-edge exclusion, good-block column-star structure, coherence, and the actual symmetric-difference cost to the repaired labelled template. All claimed bounds pass. Singleton-owner deficit and trivial-distance inequalities also pass in their tested range.

### Balancing maps

check_balancing.py constructs an explicit full bijection for all 819 splits 0<=p<gamma with 2<=gamma<=40, including p=0 and both directions of movement. Alternating selected-column labels exercise relabelling inside unchanged Y-triples.

Every changed edge has a moved endpoint; the sum of old and new moved-triple degrees equals the stated bound exactly. The actual map cost is even smaller, h(2 gamma-2h+3), in these checks. The audited proof uses only the valid weaker bound with +11. All imbalance and final constant inequalities pass.

## Reproduction and status separation

From this directory:

    g++ -O3 -std=c++17 -Wall -Wextra check_repair.cpp -o check_repair
    ./check_repair > repair_stdout.txt
    python check_balancing.py > balancing_stdout.json

Python requires only the standard library. The outputs are repair_stdout.txt, balancing_result.json and balancing_stdout.json. The source note and these audit artifacts have separate manifests/checksums from the obstruction package.

No blocking mathematical discrepancy was found. The 12 gamma t theorem is supported for the stated one-residual graph class. The previously audited obstruction is a separate result and was not assumed in proving this upper bound.
