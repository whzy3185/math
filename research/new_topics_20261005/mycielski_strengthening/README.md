# M6 Hall-ratio strengthening

The frozen pilot proves rho(M6)=10/3. The main result of this package is the complete finite extremizer census. Its proof also uses a convenient recursive identity:

1. A general theorem for every nonempty finite graph G:
   `m(μ(G))=m(G)+#{N_G(I):I independent in G}`,
   with an implementation bound of `O(n² i(G))` elementary Boolean work; this is not an improvement on standard output-sensitive enumeration and can be exponentially worse
2. An exact classification of all M6 Hall maximizers: **1,990 labelled subsets in 199 ambient-automorphism orbits**, all with 20 vertices and independence number 6

The orbit counts by original/clone/apex layer sizes are:

- (13,6,1): 109 orbits, 1,090 subsets
- (14,5,1): 83 orbits, 830 subsets
- (15,4,1): 7 orbits, 70 subsets

Every orbit has size 10 under Aut(M6)=D5. These are embedded-subset orbits, not claimed abstract graph-isomorphism classes.

Read `GENERAL_THEOREM.md` and `CLASSIFICATION.md` for complete proofs and `LITERATURE_SCOPE.md` for sources and limits. No publication-novelty, general algorithmic-improvement, or asymptotic claim is made. `GENERAL_THEOREM.md` now includes the Tsukiyama et al. (1977) comparison and an explicit edgeless-base example.

## Exact verification

Keep this directory beside the unchanged `mycielski_pilot` directory, then run:

```
g++ -O3 -std=c++17 enumerate_extremizers.cpp -o enumerate_extremizers
./enumerate_extremizers
python check_strengthening.py
```

The first program completely regenerates the classification with integer arithmetic using the proved layer restrictions and neighborhood inequalities. The Python 3.10+ standard-library checker verifies all 22 new rational-certificate nodes, graph automorphisms, and the complete orbit data. The initial rho=10/3 certificate remains in the sibling pilot directory.

Numerical LP/MILP software was used only for discovery. Its status is not relied upon by the proof. The earlier limited solver enumeration remains explicitly labelled incomplete; it is superseded by the exact reduced enumeration for completeness.

## Reusable general module

`mycielski_structure.py` supplies the general induced-independence recurrence, compressed maximal-independent-set generation, independence polynomial, and Hall-profile constraint rows. Run `python test_general_module.py` to reproduce exact tests on all 75 simple base graphs through four vertices and 33,864 induced subsets.
