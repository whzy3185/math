# Unequal cells and the full R4 witness range

## Current status

The complete proof, 22 primary exact checks, 119 independent replay checks,
and final mathematical line audit PASS. Evidence: finite-certificate-assisted
analytic theorem, without Lean formalization or external peer review.
Previous completed packages are unchanged.

## New structural statement

Concatenate any number r≥1 of legal cells w_j of length h=8j+2, allowing
different lengths and either global holonomy. Then

- If every h≥106, the squared spectral radius is below 198/25
- If every h≥202, it is below 790537/100000

The bounds are independent of r. They follow from an exact 6r-dimensional
block-cyclic Schur complement and a degree-two quadratic-form estimate.
They do not assume equal spacing, a localized-mode count, or Floquet
periodicity.

## Full residue-four consequence

For each k≥6 choose j_0=floor(k/2),j_1=ceil(k/2), concatenate w_(j_0)
and w_(j_1), and take holonomy−1. This gives a two-G6 signing on N=8k+4
with rho²<7.92<rho_−(N)².

Even k gives the old balanced construction. Odd k gives separations N/2−4
and N/2+4 and must be described as a changed, nearly balanced construction.
The uniform theorem covers k≥26; 20 exact finite bases k=6..25 finish the
range. The cap 7.92 is below the inherited endpoint 2679/338 by 51/8450.

The sharper 7.90537 cap fails at N=60 even for this changed construction.
A strictly negative exact LDL pivot records that falsification. There is no
claim that all legal short cells satisfy the sharp cap.

## Assembly and error

Retain K_i=(head pair of cell i, tail four of cell i−1). A chain contributes
its left self-energy to K_i, its right pure-pivot term to K_(i+1), and a
cross block F_i=U_pX_p⁻¹V, with U=[R;Wᵀ], V=[0,E_+]. All contributions
are added, including single-cell loops and two-cell parallel edges.

The limiting diagonal is the old six-core S_∞. With s the minimum number
of complete transfers past the entrance, the exact all-r error bound is

    12b²q^(2s)/(1−q²)+576r_0θ^s+32a q^s.

The first term counts both increments per transfer pair. The last term
comes from at most two chain incidences per retained core, not from summing
an error r times. Both frozen parameter sets make this error smaller than
their original epsilon, so the old positive limiting core transfers.

## Complete reproduction package

- UNEQUAL_CELL_SCHUR_THEOREM.md: complete geometry, exact assembly,
  uniform estimate, R4 finite completion and falsification boundary
- assembly.py and verify_unequal_cells.py: standard-library exact code
- unequal_cells_certificate.json and verification_output.json: actual
  primary certificate and stdout
- audit/: independent geometry, Schur, scalar-LDL and proof review

The primary verifier passes 22 required checks, including 12 exact assembly
identities and all 20 finite R4 bases. It reproduces both rational error
inequalities and the changed N=60 sharp-cap obstruction. The upstream
Riccati and response premises remain in the frozen ../analytic/ and
../strengthening/ packages, which are explicit dependencies.

## Scope and next frontier

This is an explicit witness theorem, not global minimization or rigidity.
The cell words and h≡2 mod 8 legality are required. Arbitrary defect types
and signings are not covered; the old r→2r correction remains untouched.

The same structural theorem covers any three legal cells once each is
long enough. A full R6 witness range would still require choosing three
integer cell parameters and validating its remaining finite bases. No R6
completion is claimed here.
