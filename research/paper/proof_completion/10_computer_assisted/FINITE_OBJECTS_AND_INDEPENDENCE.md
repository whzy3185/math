# Finite Objects, Coverage, and Checker Independence

## Coverage questions

For each computer-assisted theorem the proof package must answer four
questions.

1. **Why finite?** A mathematical parameter bound or finite-state reduction
   is stated before code is invoked.
2. **Why exhaustive?** Every mathematical object maps to a checked record,
   and every checked record maps back to an object in scope.
3. **Why the right premise?** The checker reconstructs the matrix, transfer,
   threshold, parity, holonomy, or orbit relation appearing in the theorem.
4. **Why no floating endpoint?** Acceptance is exact rational, algebraic,
   interval-certified, or a complete integer partition.

## Coverage map

| Theorem family | Finite object | Exhaustiveness bridge | Independent layer |
|---|---|---|---|
| Orders `8..30` | switching classes modulo the proved gauge/orbit reduction | record-set equality and represented-class counts | independent record and spectral reconstruction for the large orders |
| Order 32 | one explicit signed matrix and threshold algebraic number | existence needs one witness only | independent matrix, flux, LDL/Bareiss, and radical reconstruction |
| Orders `34,36,38,42,44,46` | local windows, parity-lifted de Bruijn walks, 64 terminal `(Q,alpha)` records | sound/complete overlap graph plus both holonomies | checker imports no producer and rebuilds every window and terminal |
| Order 40 | one explicit finite signed matrix | existence needs one witness only | exact rational LDL reconstruction |
| Orders `48..238` | 96 explicit matrices | one record for every even order in the interval | independent canonical reconstruction and exact LDL |
| Tail `n>=240` | four residue endpoints plus monotonicity and analytic IMS formula | residue partition of all even orders | exact endpoint reconstruction; no infinite enumeration |
| G6 global edge | finitely many isolated resultant candidates and finitely many Grassmann charts | global chart cover plus resultant candidate completeness | alternate cofactor chart and unsquared determinant checks |
| Exact `2r` | finitely many orientations, holonomies, cuts, and rational interval bounds for `r<=3` | analytic Gram/min-max argument covers every separated ring satisfying `D>=1040` | checker rebuilds transfer/interval/constants without producer imports |
| Single-gap hierarchy | six small witnesses plus three tail locality classes | all positive `g` split into `{1,2,3,5,7,8}`, `{6}`, and `g>=9`, with `g=4` reference | independent full-image integer reconstruction |
| Periodic `p<=24` | 372,726 dihedral orbit records before primitive identification | legal-word enumeration, orbit accounting, primitive normalization, zero remainder | implementation-disjoint orbit audit plus primary exact `c6` arithmetic |

## Independence is not binary

A checker may be independent in matrix construction but share a parser; in
orbit generation but not a threshold; or in a cofactor chart but share an
interval kernel. The final table records the actual mechanism rather than the
word "independent" alone.

For the `p<=24` frontier, the primary `c6` checker shares canonical/Bloch
helpers with the producer. A separate bracelet audit independently validates
the 370,100 high-period orbit partition but stores only the weaker
`1561/200` endpoint. The theorem is supported compositionally by that
coverage audit and by exact recordwise `c6` comparisons. This limitation must
remain visible in the appendix.

## Hashes

Hashes bind a certificate to source data and detect changes. They do not show
that the source data are complete or mathematically correct. Every hash in
the theorem table is accompanied by a reconstruction or an explicit statement
that only provenance is being checked.
