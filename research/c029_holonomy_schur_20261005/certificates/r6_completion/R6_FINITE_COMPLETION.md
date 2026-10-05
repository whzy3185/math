# A complete residue-six witness family from three legal cells

Date: 2026-10-05. Scope: signed cycle squares C_N(1,2).

## Statement and evidence status

Let k≥6 and N=8k+6. Define

    j_0=floor(k/3),
    j_1=floor((k+1)/3),
    j_2=floor((k+2)/3).

For j≥1 put

    w_j=(1,1,−1,1,−1,−1,1,−1)^j || (1,−1).

Give every length-one edge sign+1, and give the length-two edges, in cyclic
order, the signs

    τ=w_(j_0)||w_(j_1)||w_(j_2).

Let A_N be the resulting real signed adjacency matrix. Then

    ρ(A_N)² < 198/25 = 7.92 < ρ_−(N)²                       (1)

for every k≥6.

The analytic infinite-length reduction follows from the independently
audited unequal-cell Schur theorem. All 33 remaining finite graphs have
passed direct exact rational LDL verification and a separate gap-based,
natural-order replay. Both the 139 primary checks and 139 independent checks
PASS, as does the complete mathematical line audit.

This is an explicit witness theorem. It does not determine the minimum
over all signings, identify minimizers, or supply new universal lower bounds.
Its completed proof is finite-certificate-assisted, not Lean-formalized or
computation-free.

## 1. The construction is well defined and has three G6 gaps

Writing k=3q+s with s∈{0,1,2} shows

    j_0+j_1+j_2=k,
    min_i j_i≥2,
    max_i j_i−min_i j_i≤1.

The three cell lengths h_i=8j_i+2 therefore sum to 8k+6=N and differ by
at most eight. The Hamilton-cycle holonomy is+1.

Within a cell w_j, the positive quadrilateral fluxes
Q_u=τ_uτ_(u+1) occur at local positions 0,4,…,8j−4. Consecutive such
positions inside a cell differ by four, and the last positive position of
one cell is six sites before the first positive position of the next cell.
Thus the cyclic gap word has exactly three entries equal to six and all
remaining entries equal to four. There are 2k positive Q positions in total.

When k is divisible by three, this is the equally spaced three-G6
construction. For the other two congruence classes, the placements may
differ from the earlier balanced-gap construction: every individual cell
here is required to have length 2 modulo 8. The finite verification below
reconstructs these new signings directly rather than importing certificates
for a different gap word.

## 2. Infinite tail from the unequal-cell theorem

The frozen theorem in
../unequal_cells/UNEQUAL_CELL_SCHUR_THEOREM.md proves that a concatenation
of any number of these legal cells has squared spectral radius below 198/25
whenever every cell has length at least 106, for either holonomy. Its proof
is an exact block-cyclic Schur assembly with an error independent of the
number of cells.

For k≥39 each j_i≥13, hence each h_i≥8·13+2=106. Applying that
theorem with three cells and holonomy+1 proves

    ρ(A_(8k+6))²<198/25              for every k≥39.          (2)

The first order in this analytic range is 318. No extrapolation from finite
eigenvalue calculations is used, and no new asymptotic or interface-mode
assumption is required.

## 3. Exact finite bases

Only the integers 6≤k≤38 remain, corresponding to the 33 graph orders

    N=54,62,70,…,310.

For each such k, verify_r6_completion.py constructs the full signed
adjacency from the displayed edge signs. It forms the integer matrix

    198I_N−25A_N²

using integer two-step walks, then applies sparse scalar LDL with exact
Fraction arithmetic. Every pivot is strictly positive at all 33 orders.
Positive definiteness implies the desired squared spectral-radius cap.

The certificate records the actual cell parameters, cell lengths, cyclic
gap word, holonomy, pivot count and pivot-list SHA256 for every graph.
All construction and coverage conditions are also checked exactly. The
complete list is precisely k=6,…,38; there is no gap between its last
order 310 and the analytic tail beginning at 318.

There are 139 passing required rational/structural checks in the primary
run. Neither the preliminary floating spectra nor an eigenvalue tolerance
is used as theorem evidence. The finite range is a consequence of the
proved minimum-cell-length theorem, not an arbitrary stopping point.

Combining these bases with (2) proves the left inequality in (1).

## 4. Comparison with the twisted benchmark

The exact benchmark is

    ρ_−(N)²=4+2cos(2π/N)+2cos(4π/N).

The elementary estimates cos x>1−x²/2 for x>0 and π²<10 give

    ρ_−(N)²>8−200/N².

For every N≥54,

    8−200/N²≥8−200/54²=5782/729>198/25.

The endpoint difference is exactly

    5782/729−198/25=208/18225>0.

This proves the right inequality in (1). In particular the cap is below the
older residue-six target 5782/729; it was not increased to accommodate
the finite cases.

## 5. Consequence for the witness side of the original problem

Together with the already established period-eight family and the R2/R4
families, this construction supplies explicit signings beating the twisted
benchmark at every even N≥48. The three nonzero residues use one, two
or three legal cells and the same unequal-cell Schur theorem, with their
finite bases stated explicitly.

This is the failure-of-optimality direction only. The equality cases at
smaller orders still depend on their separate historical certificates;
this completion does not replace those universal lower-bound arguments.
Nor does it determine the actual optimum when the twisted signing fails.

## Reproduction and dependencies

Run:

    python verify_r6_completion.py

The verifier is self-contained Python-standard-library code. Its exact
output is r6_completion_certificate.json, and verification_output.json
records the actual stdout. These files contain the new finite work only.
The already audited unequal-cell theorem, its proof dependencies and its
verification records remain in the frozen sibling packages.

The independent review checked the finite proof, floor/coverage argument,
endpoint comparison and witness-only corollary. Its report, standalone replay
code and exact outputs are in audit/. No old G6 physical-edge calculation,
IMS estimate, mode-count assertion, or unpublished companion theorem is used
as a new black box: the common Schur result is supplied in the same research
package. This independent audit is not external peer review.
