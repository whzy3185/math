# Integrated C029 claim ledger

Date:2026-10-05. This ledger distinguishes inherited results, the current proof mechanism, exact finite evidence and formalization scope. The paper's main mathematical conclusions are finite-certificate-assisted analytic theorems unless otherwise specified.

## G1 Exact period-eight holonomy formula

For m≥1, triangle word t^m with t=(+,+,−,+,−,−,+,−) has exactly two switching classes, determined by Hamilton holonomy. Their radii are R(2) and R(2cos(π/m)), where R(s)=sqrt(4+sqrt(8+s+sqrt(26−3s))). The negative class is the unique minimizing class only within this prescribed labeled triangle-word family.

Status: Proved analytically; fresh exact symbolic and direct n32 checks agree. Provenance: inherited exact formula, not a new discovery claim. Frozen earlier source: https://github.com/whzy3185/math/blob/085ea698475b7b32e0ae57457ec903a922248f69/research/paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex

New application: μ_(8m)<R(2) for every m≥4 refutes Conjecture28 of arXiv:2607.17343v2 (22September2026). The original arXiv:2607.18334 was withdrawn and merged. This is not a determination of μ_(8m).

## G2 Uniform one-cell cap and near-optimal family ceiling

For every k≥1, the positive-holonomy signing with triangle word w_k=t^k||(1,−1), on n=8k+2, has rho²<790537/100000. At n202, rho²>7905369/1000000. Thus the supremum over this prescribed family belongs to(7.905369,7.90537], with a closed upper endpoint.

Status: Proved. New fixed-energy certificate uses J48, radius10^-18, center metric factor1/2, q3/4, seed graph order202 with normalized six-core margin10^-6. Uniform tail<10^-8,24 smaller finite bases, and a strict negative-pivot lower obstruction close the statement. Independent full-graph replay and analytic audit PASS. No limit, monotonicity, exact supremum or unrestricted minimization claim.

Evidence: certificates/strengthening/UNIFORM_ONE_G6_CAP.md, verify_uniform_cap.py, uniform_cap_certificate.json, and audit/.

## G3 Unit-phase bound

For each legal cell w_j and every unit complex z, the Hermitian phased operator A_h(z) has rho²<7.92 when h≥106 and rho²<7.90537 when h≥202. Consequently any number of identical cells with either real global holonomy obeys the corresponding cap.

Status: Proved. Exact conjugated phase core retains both terminal corrections; the common limit is phase independent. No phase sampling or localized-mode assumption is used. Independent Laurent and quotient-ring checks validate the implementation.

Evidence: certificates/r4_pilot/PHASE_UNIFORM_R4_ASSEMBLY.md and audit/; shared premises are reproduced in the integrated paper.

## G4 Unequal-cell theorem

For any r≥1, concatenate legal w_(j_i), j_i≥1, and choose either Hamilton holonomy. If every h_i≥106 then rho²<198/25; if every h_i≥202 then rho²<790537/100000. Lengths may be unequal and the cap is independent of r.

Status: Proved. Retain K_i=(head pair of cell i, tail four of cell i−1). Exact additive6r-dimensional Schur assembly includes r1 loops and r2 parallel contributions. The error is bounded by12b²q^(2s)/(1−q²)+576δθ^s+32aq^s because every retained core has two chain-end incidences. Both rational parameter sets satisfy the required seed/error separation. Independent complete line audit and119 exact replay checks PASS.

Scope: legal cell words and minimum lengths are hypotheses; arbitrary defect positions or arbitrary signings are not covered. This is the new common structural proof mechanism, relative to the frozen project packages. It avoids the earlier physical G6 edge/IMS/mode-count route, but no exhaustive literature-priority claim is made.

Evidence: certificates/unequal_cells/UNEQUAL_CELL_SCHUR_THEOREM.md, assembly.py, verify_unequal_cells.py and audit/.

## G5 Full residue-four witnesses

For k≥6, n=8k+4, use w_floor(k/2)||w_ceil(k/2) with holonomy−1. Then rho²<7.92<rho_tw(n)². Analytic coverage begins k26/n212; exactly20 bases k6..25/n52..204 close the range.

Status: Proved. Odd k uses changed placements separated by n/2−4 and n/2+4. It is not the earlier balanced odd-k graph. Every finite matrix was rebuilt and independently checked.

Sharper subsequence: w_j||w_j, alpha−, obeys rho²<7.90537 for all j≥1;24 bases j1..24 and the phase theorem cover all j. Exact obstructions show rho²>7.90537 at the changed n60=(26,34) and n76=(34,42) cell pairs. A separate balanced odd-k n60 graph also violates that sharper cap. These are different specified constructions and must not be conflated.

## G6 Full residue-six witnesses

For k≥6, n=8k+6, concatenate w_floor(k/3), w_floor((k+1)/3), w_floor((k+2)/3), with holonomy+1. Then rho²<7.92<rho_tw(n)². Analytic coverage begins k39/n318; exactly33 bases k6..38/n54..310 close the range.

Status: Proved, with139 primary and139 independent exact checks and a complete line audit. When3 does not divide k, these placements may differ from the older balanced-gap family. No certificate is transferred from another signing.

Evidence: certificates/r6_completion/R6_FINITE_COMPLETION.md, verify_r6_completion.py and audit/.

## G7 All-even witness consequence

Explicit signings beat the twisted benchmark at n32,40 and every even n≥48. For the8-divisible line, eta=4+sqrt(10+2sqrt5)<999/128=8−200/32²; for the other residues,7.92≤8−200/n² from n50 onward. In each case rho_tw(n)²>8−200/n².

Status: Proved witness/existence direction. This range is inherited from earlier Target A work; the present contribution is the transparent common analytic proof and improved bounds, not a newly discovered truth set. Smaller complementary equality cases, exact unrestricted minima, and minimizer classification are not reverified here.

## Formalization

Verified checkpoint: Lean4.33.1, completed2026-10-05 at09:12:30UTC. TargetA.period8_alpha_minus_exact_finite_radius proves that every Hermitian eigenvalue modulus of the original raw negative-holonomy matrix is at most R(2cos(π/L)), and an eigenvalue attains that value, for every L>0. The positive attained eigenvalue, expanded radical, maximal phase, determinant root and raw/reverse graph bridges are all verified. The full audit covers237 declarations, with axiom union propext, Classical.choice and Quot.sound and no sorryAx or project-specific axiom.

This is formal verification of an inherited analytic formula, not a new analytic-discovery or priority claim. The older raw strict endpoint bound remains verified. The separate quartic identification of the constant used by Conjecture28, the finite-size asymptotic, the n32 integer certificate, and every Riccati/Schur/unequal-cell/R4/R6 result remain outside this formalized scope. All-even witness coverage must not be described as Lean-certified.
