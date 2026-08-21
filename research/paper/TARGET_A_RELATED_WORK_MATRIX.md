# Target A Related-Work Matrix

Search refreshed: 2026-08-21

This matrix records why each source belongs in the paper. It is not a claim
that the listed literature exhausts signed-graph spectral theory. Metadata for
new journal items was checked against publisher pages or Crossref; arXiv
version statements were checked on the corresponding arXiv records.

| Reference | Object studied | Signing / flux? | Circulant? | Spectral-radius optimization? | Floquet? | Computer-assisted? | Main result | Relation to Target A |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|:---|
| Zaslavsky (1982), *Signed graphs* | Signed graphs, balance, switching, cycle invariants | Yes | No | No | No | No | Foundational switching and balance theory | Supplies the cycle-flux/switching language used throughout. |
| Belardo--Cioaba--Koolen--Wang (2019), *Open problems in the spectral theory of signed graphs* | Adjacency spectra of signed graphs | Yes | No | Yes | No | No | Surveys signed spectra and explicitly formulates signature-minimization questions | Places the fixed-underlying-graph minimization problem in the signed-spectral literature. |
| Belardo--Brunetti--Ciampella (2021), *Unbalanced unicyclic and bicyclic graphs with extremal spectral radius* | Extremal spectral radius in structural signed-graph classes | Yes | No | Yes | No | No | Determines minimizers/maximizers in unicyclic and bicyclic classes | Closest general precedent for minimizing signed spectral radius over a fixed structural family; Target A treats a four-regular circulant family by different methods. |
| Bilu--Linial (2006), *Lifts, discrepancy and nearly optimal spectral gap* | Two-lifts and signed adjacency matrices | Yes | No | Yes | No | No | Formulates the two-sided signing problem and proves a weaker general bound | Provides the broad spectral-signing context, not the fixed-circulant optimum. |
| Marcus--Spielman--Srivastava (2015), *Interlacing families I* | Signed characteristic polynomials and graph lifts | Yes | No | One-sided; two-sided for bipartite graphs | No | No | Establishes Ramanujan bipartite lifts through interlacing families | Shows why signings are central in spectral graph theory; its interlacing conclusion does not settle nonbipartite `C_n(1,2)`. |
| Mohanty--O'Donnell--Paredes (2022), *Explicit near-Ramanujan graphs of every degree* | Near-Ramanujan constructions and locally sparse graph signings | Yes | No | Approximate | No | Algorithmic | Gives explicit near-Ramanujan graphs in every degree | Records post-MSS progress around the signing/lift problem and separates that asymptotic setting from the exact flux optimization here. |
| Suvagiya (2026), *Parity families and a kernel-averaged L-function* | Short-cycle parity constraints in graph signings | Yes | No | Approximate/general signing bounds | No | Exact computational checks | Develops the parity-family framework and trace viewpoint | Supplies the companion general framework inherited by the source conjecture. |
| Suvagiya (2026), *Signed circulants at the Ramanujan bound* | Signings of `C_n(1,2)` | Yes | Yes | Yes | Finite Fourier analysis | Exhaustive through `n=18` | Derives the alternating phase and states Conjecture 3 | Direct source of the conjecture, threshold, and inherited phase family. |
| Davis (1979), *Circulant Matrices* | Circulant matrices and Fourier spectra | No | Yes | No | Finite Fourier | No | Standard diagonalization and structural theory of circulants | Background for the unsigned graph and finite Fourier viewpoint. |
| Korotyaev--Saburova (2017), *Magnetic Schrodinger operators on periodic discrete graphs* | Periodic discrete magnetic operators | Yes, unitary magnetic phases | Periodic graphs | Band estimates, not this minimization | Yes | No | Constructs magnetic Floquet fibers and studies flux-dependent bands | Direct operator-theoretic context for gauge fluxes and continuous Bloch fibers. |
| Korotyaev--Saburova (2023), *Trace formulas for magnetic Schrodinger operators on periodic graphs and their applications* | Fiber traces, cycles, and magnetic periodic operators | Yes | Periodic graphs | No | Yes | Symbolic formulas | Expresses fiber traces through cycle data | Closely parallels the use of closed-walk/Floquet moments here, while Target A derives a problem-specific defect obstruction. |
| Lieb (1994), *Flux phase of the half-filled band* | Flux phases in a fermionic Hamiltonian | Yes | No | Energy minimization | Periodic setting | No | Proves a flux-phase theorem under physical hypotheses | Motivates terminology only; Target A does not claim Lieb's variational or physical hypotheses. |
| Cvetkovic--Rowlinson--Simic (2010), *An Introduction to the Theory of Graph Spectra* | Graph spectra and spectral moments | No | No | Background | No | No | Standard treatment of traces as closed-walk counts | Supplies the classical closed-walk moment context. |
| Fredricksen--Maiorana (1978), *Necklaces of beads in k colors and k-ary de Bruijn sequences* | Canonical generation of necklaces | No | Cyclic words | No | No | Algorithmic | Gives the necklace recursion underlying the FKM family of generators | Direct algorithmic ancestry of the primary large-order representative stream. |
| Sawada (2001), *Generating bracelets in constant amortized time* | Canonical generation modulo rotation and reversal | No | Dihedral words | No | No | Algorithmic | Gives output-sensitive bracelet generation | Direct context for quotient enumeration by the dihedral action. |
| Lam (1991), *The search for a finite projective plane of order 10* | Large exhaustive combinatorial nonexistence proof | No | No | No | No | Yes | Documents a landmark proof by exhaustive computation | Methodological precedent for separating a finite coverage argument from machine execution evidence. |

## Novelty Positioning by Result

| Target A contribution | Nearest literature line | Precise distinction |
|:---|:---|:---|
| Smallest counterexample at `n=32` | Suvagiya's exact family and enumeration through `n=18`; signed-radius minimization literature | Extends complete finite exclusion through `n=30` and supplies the first exact failure, with independent record-level enumeration at every large order. |
| Infinite period-eight counterexample family | Periodic magnetic/Floquet graph operators | Uses exact finite holonomy grids and a uniform fiber inequality to turn one signing into counterexamples for all `8|n`, `n>=32`. |
| Exact period-eight spectral edge | Circulant Fourier spectra and periodic band theory | Computes the exact top band of a nontrivial signed phase and proves its unique Bloch equality point. |
| Structural defect mechanism | Signed closed-walk spectra and flux-dependent trace formulas | Identifies the local factors `1+Q_i` in `A^2`, converting cancellation into a defect geometry. |
| Period-eight trichotomy | Extremal signed spectral-radius classification | Classifies every legal period-eight phase exactly and identifies the unique optimum under natural operator equivalences. |
| General-period moment obstruction | Closed-walk trace methods | Derives explicit problem-specific moments and one-way necessary defect inequalities; it does not assert sufficiency. |
| Primitive-period `<=16` classification | Isomorph-free/canonical exhaustive enumeration | Gives a complete exact orbit/certificate partition in a stated finite periodic domain; it is not an all-period theorem. |

## Search Conclusion

The closest direct work remains Suvagiya's source preprint. The other sources
provide theory and methods but do not report the order-32 counterexample, the
period-eight exact edge, the defect trichotomy, or the bounded exact periodic
classification. This is a dated and bounded positioning statement, not an
absolute priority claim.
