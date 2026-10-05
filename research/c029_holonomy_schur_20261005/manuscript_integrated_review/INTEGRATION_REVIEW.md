# Independent integration review of the signed cycle-square manuscript

Date: 2026-10-05. Corrected manuscript source and rendered PDF: **PASS**.

Reviewed deliverable: *Uniform Schur bounds and holonomy in signed cycle squares*, 18-page integrated manuscript. The checked source/PDF hashes are recorded in source_manifest.json. This review checks integration and transcription against the separately audited mathematical packages; it is not external peer review or a new claim of formalization.

## Mathematical integration

The main statements preserve the exact hypotheses and scopes of the audited results:

- Unequal prescribed cells, arbitrary positive cell count, either holonomy, and minimum cell lengths 106 or 202 for the two caps
- The one-cell sharper cap for every positive parameter, with supremum interval (7.905369,7.90537] and no unjustified strict supremum bound or convergence claim
- Correctly signed one-, two- and three-cell constructions for the nonzero even residues
- The inherited period-eight formula and its constrained switching-class statement
- The witness range 32, 40 and every even order at least 48, without a universal lower-bound or global-minimum claim

Both parameter columns were checked against the exact source certificates. The two centers, transfer factors, entrance indices, Riccati radii, response thresholds, q/theta factors, seed margins, tail tolerances and minimum graph orders agree. The Euclidean and Frobenius norm conventions are explicit.

The block matrices D, E_+, E_-, R_0, W_0 and C_0 and the positive rational weights P,Q agree with the audited definitions. The terminal index is ell-2, with E_+ parity; the normalized six-dimensional seed has block count J+2 and graph order 4(J+2)+2. The old normalization/dimension mismatch is not reintroduced.

The common analytic argument retains the dual response orientation TQT^T, both increments in each two-step pair, the mixed C correction, both H cross terms and two seed-transfer errors. All four displayed rational tail constants were recomputed exactly and agree:

    one-cell: 251089/156250000 and 583333407/109375000000000000
    unequal-cell: 501647/468750000 and 700000123/196875000000000000.

The common limiting core is defined along the actual pivot trajectory. The manuscript does not replace the pivots inside its Schur sums by the limit or transfer a core margin as a full-matrix Euclidean spectral gap.

The complex phase conjugation uses U_z=diag(I_2,zI_4) and keeps every finite phase-bearing terminal term. The unequal-cell retained coordinates combine a cell's head pair with the preceding tail four. The outgoing L and incoming P terms are assigned to the correct blocks. Both parallel-chain contributions at r=2 and the loop cross terms at r=1 remain in the additive assembly. The degree-two quadratic-form estimate is independent of the number of cells.

## Finite completion and comparisons

The finite ranges and first analytic orders are correct and exhaustive:

- One cell at the sharp cap: k=1,...,24, orders 10,...,194; analytic from 202
- Two equal cells at the sharp cap: j=1,...,24, orders 20,...,388 in steps of 16; analytic from 404
- Two near-equal cells at 7.92: k=6,...,25, orders 52,...,204; analytic from 212
- Three near-equal cells at 7.92: k=6,...,38, orders 54,...,310; analytic from 318

The order-ten coincident-coupling exception is checked directly. The sharper-cap failures at the changed order-60 and order-76 words remain distinct from the older balanced order-60 obstruction.

The benchmark gaps 51/8450 and 208/18225 agree with the endpoints 52 and 54. The additional period-eight comparison at order 32 is exact: the separator 999/128 and the integer identity 73329^2-5*32768^2=8433121 were recomputed. The finite-radius radical, determinant coefficients and asymptotic coefficient agree with their previously reviewed versions.

## Provenance and formal-verification scope

The manuscript attributes the period-eight formula and historical witness range to earlier project sources and states what the new common analytic proof contributes. The changed odd-k residue-four and non-divisible-by-three residue-six placements are identified. The source theorem's period-eight hypothesis m>=4 and the exact unrestricted scope of the revised Conjecture 28 are preserved.

During integration, the exact finite-radius Lean checkpoint completed. The final paragraph was checked against the actual theorem declarations, expanded radical identity, successful build log and all 237 axiom-audit entries in the new verified package. It correctly states an upper bound for every Hermitian eigenvalue modulus and attainment by a positive eigenvalue of the raw graph matrix, including every positive cell count.

The final text correctly excludes the separate quartic naming identification, asymptotic coefficient, integer principal-minor certificate and all Riccati/Schur/residue-completion arguments from that formal checkpoint. The axiom union is the stated propext, Classical.choice and Quot.sound. This integration review did not rerun the Lean build; it verified the supplied successful checkpoint and its actual theorem scope.

## Corrections resolved during review

The corrected source now contains:

- Multiplication spacing in the stacked-response sqrt(2) bounds, replacing stray commas
- J+2 recurrence steps for the center residual calculation
- An accurate description of normalized versus denominator-cleared finite verification
- Accurate distinctions between reconstructed and stored response matrices
- Explicit norm definitions and the correct sibling location of the earliest independent replay

No unresolved theorem, hypothesis or proof-transcription issue remains.

## Rendered-document check

All 18 pages were inspected. Equations, radicals, matrices, parameter and coverage tables, theorem statements and references are readable and unclipped. Cross-references resolve. The final build log contains no warnings, overfull boxes or underfull boxes. The final reference continuation is complete.

The paper's mathematical statements remain supported at their stated evidence levels. No literature-wide novelty, complete smaller-order classification, or unrestricted spectral minimization claim is endorsed.
