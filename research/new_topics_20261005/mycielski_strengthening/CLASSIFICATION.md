# All Hall-ratio maximizers in M6, up to ambient automorphism

Convention: M2=K2 and M_(r+1)=μ(M_r), using originals, clones, then apex in the recursive vertex ordering. The graph M6 has 47 vertices. The preceding exact certificate establishes rho(M6)=10/3.

## Finite classification theorem

Every induced subset attaining this ratio has 20 vertices and independence number 6. It contains the final apex and belongs to exactly one of three layer types:

- 13 original vertices, 6 clones, and the apex
- 14 original vertices, 5 clones, and the apex
- 15 original vertices, 4 clones, and the apex

There are exactly **1,990 labelled maximizing subsets**, in exactly **199 orbits under Aut(M6)**. Every orbit has size 10. The orbit counts by these three types are respectively **109, 83, and 7**, corresponding to 1,090, 830, and 70 labelled subsets.

These are orbits of embedded subsets under automorphisms of the ambient M6. The statement does not assert 199 abstract isomorphism types of the induced graphs.

The result combines exact rational exclusion certificates with the structurally reduced exhaustive enumeration described below. All representatives and their full orbits are supplied in `complete_orbits.json`.

## 1. Only the 20-vertex equality case survives

If |S|/alpha(S)=10/3, then alpha(S) is divisible by three. Since M6 has only 47 vertices, the possible pairs (|S|,alpha(S)) are

`(10,3), (20,6), (30,9), (40,12)`.

The file `strengthening_certificates.json` excludes subsets with

- cardinality at least 10 and independence number at most 3
- cardinality at least 30 and independence number at most 9
- cardinality at least 40 and independence number at most 12

The first exclusion has 19 rational-dual/binary-split nodes; the latter two have one each. Hence equality requires (20,6).

## 2. The apex and layer sizes are forced

One additional rational-dual leaf excludes a 20-vertex subset of independence number at most 6 when the apex variable is fixed to zero. Thus every maximizer contains the apex.

Write A for its original indices and B for its clone indices. The apex branch of the independence recurrence gives `alpha(M5[A])<=5`. The clones are independent, so |B|<=6. Since |A|+|B|=19, we have |A|>=13.

The exact M5 profile gives: every subset with independence number at most 5 has at most 15 vertices, and every subset with independence number at most 4 has at most 12 vertices. These facts are also reverified directly during the reduced enumeration. Consequently

`|A| in {13,14,15}`, `alpha(M5[A])=5`, and `|B|=19-|A|`.

This yields precisely the three layer sizes stated above.

For context, there is also a conceptual reason to expect the apex: deleting it leaves a graph homomorphic to M5, under the map taking each original and clone to its base vertex. The exact exclusion certificate is sufficient for the proof and does not rely on a separately imported fractional-coloring result.

## 3. Exact neighborhood characterization of the three families

For any independent I subseteq A, an apex-free independent set can contain I and all clones in `B minus N(I)`. Therefore, for A and B of the above sizes, the corresponding 20-set is a maximizer if and only if

`|B minus N(I)|<=6-|I|`

for every independent I subseteq A.

These inequalities are a complete finite structural family description. Since alpha(A)=5 and the apex is present, their satisfaction ensures that the full induced independence number is exactly 6.

Only independent sets with `|I|>6-|B|` need to be tested; the others satisfy the inequality automatically. In particular, an independent five-set I0 in A imposes the especially restrictive condition

`|B minus N(I0)|<=1`.

The enumeration exploits this condition before testing any other independent-set inequality.

## 4. The ambient automorphism group is D5

M3 is the five-cycle whose cyclic order in the chosen labels is `(0,1,2,4,3)`.

For every r>=4, the final apex of M_r is its unique vertex of maximum degree. Indeed, for G=M_(r-1) with n vertices, the maximum degree is (n-1)/2. In μ(G), original degrees are at most n-1, clone degrees at most (n+1)/2, and the apex degree is n. This property starts with the degree-two five-cycle and inducts.

Thus every automorphism fixes the apex and preserves its neighborhood, the clone layer. It also preserves the remaining original layer, inducing an automorphism of G. The base graph is open-neighborhood twin-free. Hence the clone permutation is uniquely forced by the original permutation: the clone of v must map to the clone of its image. Conversely, every automorphism of G extends in this way.

Twin-freeness starts with C5 and is preserved here: clones are distinguished from originals by apex adjacency; neighborhoods within each layer distinguish vertices when the base is twin-free; and the apex has its unique degree. Therefore

`Aut(M6) is isomorphic to Aut(C5)=D5`,

of order 10. Its elements are the simultaneous rotations/reflections of that initial five-cycle at every descendant layer, fixing the subsequently introduced apices.

The checker verifies the ten explicit permutations, their closure and adjacency preservation, and the unique-apex/twin-free hypotheses. A canonical orbit representative is the least integer subset mask among these ten images.

## 5. Complete reduced enumeration

The exact enumeration is not a search over 2^47 vertex subsets. It proceeds as follows.

1. Compute alpha for every subset of the 23-vertex base M5 using
   `alpha(S)=max(alpha(S-v),1+alpha(S-N[v]))`.
   This simultaneously verifies the profile bounds used in Section 2.
2. Retain only original subsets A of sizes 13, 14, or 15 with alpha(A)=5, and keep one representative under D5. There are **4,370** such original-set representatives.
3. For each A, choose an independent five-set I0 subseteq A minimizing |N(I0)|. This choice improves filtering but does not affect completeness.
4. Let b=19-|A|. Enumerate B in two disjoint cases:
   - b elements from N(I0)
   - b-1 elements from N(I0) and one from its complement
   These are exactly the B satisfying `|B minus N(I0)|<=1`.
5. Check all remaining neighborhood inequalities from Section 3. Canonicalize every accepted full 20-set under D5 and deduplicate.

The finite run tested **50,504,405** filtered clone candidates. It accepted 200 pairs at canonical A representatives, yielding **199** distinct full-subset orbits. The discrepancy occurs because canonicalizing A alone can leave a nontrivial stabilizer acting on B; full-subset canonicalization removes this duplication.

Completeness follows directly: every maximizer has one of the three proved layer sizes; a D5 image makes its A canonical; its B satisfies the chosen five-set filter; and the remaining inequalities are necessary and sufficient. Conversely, every accepted pair has alpha=6 and order 20. No numerical optimization status is used by this enumeration.

The original bounded MILP discovery run found only 137 of the orbits and was explicitly stopped at its time budget. Its output remains labelled incomplete. The complete classification comes from the different exact reduced enumeration, not from promoting that earlier solver report.

## 6. Verification and files

Run in this directory:

```
g++ -O3 -std=c++17 enumerate_extremizers.cpp -o enumerate_extremizers
./enumerate_extremizers
python check_strengthening.py
```

The C++ program regenerates the complete representative list using integer masks and exact independence dynamic programming. It has a 90-second safety limit; a limit exit does not certify completion. Successful output begins `COMPLETE` and records the counts above. The Python checker verifies all 22 rational-certificate nodes, all orbit data, graph automorphisms, and every representative against the independently generated full maximal-independent-set list.

The latter checker requires Python 3.10+ and uses only its standard library. SciPy is required solely to regenerate proposed LP weights with `certify_strengthening.py` or to rerun the separate incomplete MILP discovery.

Key artifacts:

- `GENERAL_THEOREM.md`: general compression theorem and parameterized certificate workflow
- `strengthening_certificates.json`: exact exclusion trees, 22 nodes
- `enumerate_extremizers.cpp`: complete reduced enumeration
- `complete_orbit_representatives.txt`: regenerated canonical masks
- `complete_orbits.json`: all representatives, orbit members, layer data, and graph invariants
- `check_strengthening.py`: exact rational/orbit checker
- `strengthening_check.json` and `exact_enumeration_output.txt`: verification results

The sibling pilot remains unchanged and supplies the certified baseline value 10/3 and graph/MIS data.

## Scope of claims

This is a finite exact classification under ambient automorphisms, not an asymptotic result. Publication novelty is not established. The bounded literature check and prior work are recorded in `LITERATURE_SCOPE.md`.
