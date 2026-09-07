# Beyond-circulants workstream

Date: 2026-09-07.
Branch: `research/quadratic-gap-upgrade`.

This directory extends the signed spectral-radius program beyond the
`C_N(1,s)` family.

## New analytic results

1. `GENERAL_CLIFFORD_PRODUCT_THEOREM.md`
   - arbitrary Cartesian products of bipartite signed graphs;
   - pairwise anticommuting directional adjacencies;
   - exact square-spectrum formula;
   - closure theorem for exact flat minima.
2. `EVEN_TORI_HYPERCUBES_AND_HADAMARD_PRODUCTS.md`
   - explicit signed spectra for all even-cycle tori;
   - exact minima `m(C_4^{square d})=sqrt(2d)`;
   - exact hypercube minimum `m(Q_d)=sqrt(d)`;
   - exact-minimum mixed products and Hadamard `K_(q,q)` factors.
3. `GRID_BOX_AND_CYLINDER_COROLLARIES.md`
   - explicit formulas for signed boxes, rectangles and even cylinders.
4. `UNIT_GENERATOR_CIRCULANT_TRANSFER.md`
   - transfers the full `C_N(1,s)` theorem package to every unit-generated
     four-regular two-generator circulant `Cay(Z_N,{+-a,+-b})`.
5. `TWO_GENERATOR_LATTICE_QUOTIENT.md`
   - represents every connected two-generator cyclic Cayley graph as a skew
     square-lattice quotient `Z^2/L`;
   - gives an exact bipartiteness criterion and the natural cycle-length
     resonance parameters.
6. `verify_clifford_product_families.py`
   - exact integer checks of anticommutation/flat identities and numerical
     regression of representative torus spectral formulas.

## Main product theorem

For bipartite factors `G_j` with signed adjacencies `A_j`, the Clifford
Cartesian signing satisfies

\[
A^2=\sum_j I\otimes\cdots\otimes A_j^2\otimes\cdots\otimes I
\]

and therefore

\[
\rho(A)^2=\sum_j\rho(A_j)^2.
\]

If each `G_j` is `k_j`-regular and has a flat signing `A_j^2=k_jI`, then

\[
\boxed{m(G_1\square\cdots\square G_d)=\sqrt{\sum_j k_j}.}
\]

This produces exact-minimum families far beyond circulants.

## Literature boundary

Several special cases have substantial prior overlap: Huang's signed
hypercube, signed Cartesian-product constructions, signed toral tessellations,
and general two-eigenvalue signed graphs.  The current value of this workstream
is the unified algebraic framework, the exact-minimum closure statement, and
its integration with the circulant arithmetic program.  No priority claim is
made for known special cases.

## Next targets

- skew torus quotients with neither cyclic generator a unit;
- signed pentagon/heptagon strip analogues of the `N=3s` triangle obstruction;
- multi-generator circulants `C_N(1,s,t)`;
- formalization of the Clifford anticommutation theorem in Lean.
