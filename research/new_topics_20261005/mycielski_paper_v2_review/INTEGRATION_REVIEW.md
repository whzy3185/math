# Independent integration review: Mycielski paper, version 2

Date: 5 October 2026. **PASS** on the corrected six-page manuscript and PDF identified below. No substantive mathematical or integration issue remains.

- TeX SHA-256: `4bd347f83da23b8b7b120db7ba03f28065c33154af620e1434f2fcb73b11f161`
- PDF SHA-256: `4a5a2455f82704298fbd5fa2b7f472503710710ac298ccf9da913136e2ec10fb`
- PDF: six pages, 116,894 bytes

## Analytic theorem and equality conditions

The theorem holds for every nonempty finite simple base graph G with fractional chromatic number below three. Isolated vertices and disconnected graphs are allowed. The strict hypothesis is used as a sufficient condition, with no necessity claim.

The fractional-coloring pullback applies to the four selected base layers even when their projection is not injective, and it also applies to an empty selected remainder. For a nonempty one-step subset of independence number a, the bound |U|<=ca+1<3a+1 gives |U|<=3a by integrality. For the two-step graph, deleting the three distinguished vertices gives |S|<=floor(ck)+3<=3k+2; this suffices for k>=6 and is strict in ratio for k>=7.

For k=3,4,5, the at-most-two-special-vertices case gives 3k+1. In the all-three case, Q union T is independent and the pair {z,z-prime} is independent and anticomplete to P union R. Thus their selected sizes are at most k and floor(c(k-2)), giving 4k-4. The resulting bounds 10,13,16 are correct. Triangle-freeness handles k=1,2, and the direct ten-vertex argument excludes equality at k=3. None of these steps uses finite enumeration.

Equality therefore requires order twenty and independence number six. At most two distinguished vertices would permit at most nineteen vertices. The selected P union R and Q union T must have orders eleven and six, respectively. The first has independence number four. For the final original part A, the one-step theorem gives |A|<=15 and excludes alpha(A)<=4 because |A|>=13; hence alpha(A)=5 and the three final layer profiles follow. These are necessary equality conditions, not existence assertions for every base.

The two proof paragraphs were clarified during this review to say explicitly that U and S are nonempty. This resolves the otherwise literal empty-subset exception to the strict one-step inequality without changing the intended theorem.

## Exact specialization and computation counts

A fresh set-based graph construction reproduces the recursive labels, all 236 edges of M6, the four-layer projection, and the required special nonadjacencies. The eleven fractional-coloring supports are independent and give unit coverage at every M4 vertex with total weight 29/10.

The displayed witness vertices and independent six-set match the supplied table. The independent checker reads that table without executing its generator, checks all rows against both smaller children, and verifies that its 190 states are precisely the states reachable under least-labelled branching, including the empty state and the full witness.

A separate maximum-induced-degree include/exclude recursion returns independence number six using 328 memoized states. Thus the manuscript's 190 and the earlier audit's 328 refer to different branch rules, not contradictory counts. The exact value rho(M6)=10/3 follows from the analytic upper and this local finite lower check.

## Census integration

The final-original/final-clone independence formula is exact, including the apex branch. With alpha(A)=5 it gives the necessary and sufficient clone-capacity inequalities. The original-set candidate range is now justified analytically; the independent exhaustive census audit remains the premise for the numerical orbit count.

The manuscript accurately transcribes 4,370 original representatives, 50,504,405 primary filtered clone candidates, 200 accepted pairs, 199 full-subset orbits, and 184,588 nodes in the alternate capacity-propagation search. The ambient group argument uses the unique apex, preservation of its clone neighborhood, and twin-freeness of the recursively constructed bases. The group is the full D5, of order ten. The census concerns embedded-subset orbits rather than abstract graph-isomorphism classes.

This integration replay checks all 1,990 saved labelled subsets against the new three-special-vertex and eleven/six-layer restrictions, and reproduces layer counts 1,090,830,70. It does not rerun the complete census; that completeness is established by the separately preserved independent enumeration audit. The obsolete 273-node and 22-node branch certificates are correctly identified as historical verification rather than premises of the new upper/equality proof.

## Prior-art boundaries

The bounded source positioning is accurate. The review directly checked:

- [Cropper–Gyárfás–Lehel](https://users.renyi.hu/~gyarfas/Cikkek/114_hallratio.pdf), including the known finite values, the fractional constants and the unbounded sequence result
- [Barnett's dissertation](https://etd.auburn.edu/bitstream/handle/10415/5316/Final%20Dissertation%20-%20Johnathan%20Barnett.pdf?isAllowed=y&sequence=2), Definition 2.1.1 and Chapter 4
- [Larsen–Propp–Ullman's primary bibliographic record and abstract](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190190313), for the classical fractional-coloring recurrence
- [Steiner's introduction](https://link.springer.com/article/10.1007/s00493-025-00164-0), which distinguishes the iterated-Mycielski ratio question from the general-graph results
- [Tsukiyama et al.'s primary record](https://epubs.siam.org/doi/10.1137/0206036), for the established output-sensitive maximal-independent-set enumeration bound

No equivalent specific one-/two-step Hall statement was located in the inspected CGL and Barnett material. This is not exhaustive novelty clearance. The manuscript appropriately avoids first-occurrence, new general enumeration-algorithm, threshold-necessity, asymptotic-resolution and proof-assistant claims.

## PDF and artifact verification

All six final rendered pages were visually inspected after the two nonempty-subset clarifications. Displays, tables, references and Chinese text are readable and unclipped. The final compiler log contains no LaTeX warnings, undefined references, missing glyphs or overfull/underfull boxes.

`check_integration.py` and `integration_checks.json` preserve the fresh finite replay. `source_manifest.json` identifies the reviewed sources and dependencies; `SHA256SUMS` freezes this review package. This is an independent correctness/integration audit, not external peer review or publication-priority certification.
