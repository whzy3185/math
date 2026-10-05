# Independent audit of the complete M6 Hall-extremizer classification

Date: 2026-10-05. Mathematical completeness audit and independent exact replay: **PASS**.

## Result

Using M2=K2 and M_(r+1)=mu(M_r), the 47-vertex M6 has exactly 1,990 labelled subsets attaining its previously certified Hall ratio 10/3. Every one has cardinality 20, independence number 6, and contains the final apex. Under the full ambient automorphism group D5, there are exactly 199 orbits, each of size 10 and each with trivial stabilizer.

The orbit counts by final original/clone/apex layer sizes are:

- (13,6,1): 109 orbits, 1,090 labelled subsets
- (14,5,1): 83 orbits, 830 labelled subsets
- (15,4,1): 7 orbits, 70 labelled subsets

The independent enumeration regenerated exactly the same 199 canonical integer masks as the primary enumeration. This audit did not merely check that the supplied representatives are valid.

These are ambient-automorphism orbits of embedded subsets, not abstract isomorphism classes of the induced graphs. No asymptotic conclusion or publication-novelty claim is supported by this finite audit. No Lean formalization is claimed.

## Dependency and scope

The baseline Hall-ratio theorem rho(M6)=10/3 was already independently certified in the sibling mycielski_pilot package. The present audit relies on that established value when calling the new equality subsets maximizers; it independently checks all additional exact exclusions and the complete equality enumeration.

The two documents reviewed are ../CLASSIFICATION.md and ../GENERAL_THEOREM.md. The general neighborhood-compression identity is valid as stated for nonempty finite simple base graphs. The empty-base exception is correctly excluded.

## Equality reduction and exact rational certificates

Equality |S|/alpha(S)=10/3 implies the possible pairs (10,3), (20,6), (30,9), or (40,12), since M6 has 47 vertices. A separately written checker rederived every rational leaf and binary split in strengthening_certificates.json:

- 19 nodes exclude size at least 10 with independence number at most 3
- One node excludes size at least 30 with independence number at most 9
- One node excludes size at least 40 with independence number at most 12
- One node excludes size at least 20 with independence number at most 6 when the apex is absent

The total is 22 nodes: nine binary splits and thirteen exact rational-dual leaves. Each leaf checks coefficient nonnegativity, coverage of every free objective variable, the residual right-hand sides after fixed-one choices, the exact objective value, and its strict comparison with the forbidden integer cardinality. Every split covers both assignments of a previously free variable. No solver status or floating tolerance is used.

It follows that every equality set has size 20, independence number 6 and contains the apex.

Write A for its M5 original indices and B for its clone indices. The apex implies alpha(M5[A])<=5; clones are independent, so |B|<=6. Since |A|+|B|=19, |A|>=13. Exhaustive exact independence values for all 2^23 M5 subsets give

    max{|A|:alpha(A)<=4}=12,
    max{|A|:alpha(A)<=5}=15.

Thus |A| is 13, 14 or 15, alpha(A)=5, and |B|=19-|A|. There is no unexamined layer profile.

## Independent complete enumeration

The primary implementation uses a least-vertex independence-number recurrence and enumerates clone subsets selected from a restrictive independent-five-set neighborhood. I checked that reduction and found it complete: every admissible B has at most one vertex outside the chosen neighborhood. Primary full-subset canonicalization correctly removes duplicates left by stabilizers of A.

The new implementation enumerate_by_capacity.cpp instead uses the following algorithms.

### Independence values by a maximum subset-zeta transform

It independently constructs M5 using edge pairs and enumerates its 7,407 independent sets with an exclude/include recursion. Initialize f(I)=|I| on those sets and f=0 elsewhere. A maximum subset-zeta transform then sets

    f(A)=max{|I|: I subseteq A and I independent}=alpha(A)

for every A. The usual induction over processed bits proves the transform identity. This differs from the primary vertex-deletion independence recurrence.

The complete original-subset counts are:

    |A|=13: 37,675 labelled, 3,843 canonical
    |A|=14: 4,925 labelled, 508 canonical
    |A|=15: 175 labelled, 19 canonical

Thus exactly 4,370 original-set representatives are examined.

### Clone search by recursive capacity propagation

For each A, every independent I contained in A gives the necessary and sufficient constraint

    |B intersect (V(M5) minus N(I))| <= 6-|I|.

Constraints with right side at least the required cardinality of B are redundant. The implementation also removes a constraint only when another has a larger support and no larger capacity, which logically implies it.

The clone search branches on including or excluding a free vertex. A saturated constraint forces all its remaining supported vertices to zero. It prunes only if there are too few free vertices, or if one constraint bounds the number of additional selectable vertices below the remaining cardinality requirement. The latter upper bound is

    free vertices outside the constraint support + remaining capacity.

These implications are exact. Every branch not rejected by an implication is searched, so no feasible B is lost. At acceptance, all original independent-set constraints are checked again.

This search used 184,588 recursive nodes. It accepted 200 pairs at canonical A representatives, with layer counts 109, 84 and 7. Full-subset canonicalization produces 199 orbits, with layer counts 109, 83 and 7. The independent sorted output is byte-for-byte identical to the primary complete_orbit_representatives.txt:

    SHA-256 cd448a35040e65254021f4e2f8981ee24ffbe86e5f793664389226af8e9282a1

The independent run finished with COMPLETE. It has no search time cutoff and uses no optimization solver. Its reported elapsed time was about 0.53 seconds on this environment; the timing is not part of the mathematical claim.

## Complete maximal-independent-set checks

A fresh set-based Bron-Kerbosch enumeration on the complement of the independently reconstructed M6 produces exactly 857 maximal independent sets. A second construction using the neighborhood-union theorem independently produces the same list.

The exact counts are

    i(M5)=7407, d(M5)=778, m(M5)=79,
    m(M6)=778+79=857.

Every generated set is explicitly checked for independence and maximality, and the complete sorted list equals the baseline certificate's row list. All 1,990 labelled equality subsets, not only their representatives, were then checked against all 857 rows; each has maximum intersection exactly six and size exactly twenty.

The checker also verifies every supplied orbit member, representative minimum, layer-index list, stabilizer size, induced edge count and degree distribution.

## Full ambient automorphism group and stabilizers

The initial five-cycle has exactly ten automorphisms. The independent code obtains these by testing all 120 permutations, rather than assuming a particular cycle orientation or the primary permutation list. Each lifts through all three subsequent Mycielski stages.

The argument that these are all automorphisms is valid. At every stage from M4 onward, the apex is the unique maximum-degree vertex and therefore is fixed. Its neighborhood is exactly the clone layer, so both clone and original layers are preserved. Restriction to originals is an automorphism of the base. Open-neighborhood twin-freeness forces the clone permutation to match this restriction uniquely. Conversely, each base automorphism lifts. The relevant degree and twin-free hypotheses are checked independently at every level.

All ten lifted permutations preserve adjacency, and their composition table is closed. Thus Aut(M6) is precisely D5, not merely a subgroup used for partial deduplication. Every resulting full-subset stabilizer has order one; all orbit sizes are therefore ten. Orbits are explicitly checked to be disjoint, giving exactly 1,990 labelled subsets.

## General theorem review

For nonempty G, a maximal independent set of mu(G) containing the apex corresponds to a maximal independent set of G. If it avoids the apex and has original part I, maximality forces all clones outside N(I). Its original part then equals

    J_N={v:N_G(v) subseteq N}, N=N_G(I).

For independent I, J_N is independent, N(J_N)=N(I), and V minus N is nonempty. The resulting set J_N union (V minus N)' is therefore maximal, including domination of the apex. The clone part determines N uniquely. This proves the asserted bijection and

    m(mu(G))=m(G)+d(G).

The induced-subset independence recurrence and independence-polynomial identity follow from the apex/no-apex split and are correct. The stated complexity is parameterized by the number of base independent sets; it does not imply polynomial-time Hall optimization.

As a finite implementation cross-check, the independent checker verifies the compression identity and independent-set count for every labelled nonempty simple graph with at most four vertices, 75 graphs in total. It also reproduces i(M6)=39,473,983 from the exact identity. These small checks supplement, rather than replace, the proof.

## Reproduction and artifacts

From this audit directory:

    g++ -O3 -std=c++17 -Wall -Wextra enumerate_by_capacity.cpp -o enumerate_by_capacity
    ./enumerate_by_capacity > enumeration_stdout.txt
    python independent_check.py > independent_check_stdout.json

The Python checker requires only the standard library and imports no primary verifier. It consumes the exact source certificates as data, freshly regenerates the graph and independent-set constraints, and compares the independently generated representatives with the source data.

- enumerate_by_capacity.cpp: independent complete enumeration
- independent_representatives.txt: its 199 canonical masks
- enumeration_stdout.txt: actual completed-run output
- independent_check.py: exact certificate, graph, MIS, orbit and metadata checker
- independent_check_result.json and independent_check_stdout.json: PASS results
- source_manifest.json and SHA256SUMS: source/artifact provenance

No blocking mathematical discrepancy was found. The baseline Mycielski proof and certificates remain unchanged.
