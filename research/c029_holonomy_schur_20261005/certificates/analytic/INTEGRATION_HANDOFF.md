# C029 residue-two proof increment: integration handoff

## Strongest supported claim

For every integer k≥6, put n=8k+2. Give all length-one edges sign +1;
give length-two edges signs t repeated k times followed by (1,−1), where
t=(1,1,−1,1,−1,−1,1,−1). Then

    (198/25)I−A_n² ≻ 0,
    ρ(A_n)² < 198/25 < ρ_−(n)².

Evidence: **Proved, finite-certificate-assisted analytic theorem**. The
infinite tail and local contraction are written analytic arguments. Their
fixed rational premises, seven finite base cores and one seed core have
fresh exact Fraction checks. This is a proof-method upgrade of one
constituent of the historical computer-assisted classification, not a new
classification truth set. No R2 Lean claim.

## Deliverable files

- R2_ANALYTIC_TAIL_CLOSURE.md: self-contained construction, block reduction,
  local positive-map contraction, all-term tail majorant, seed transfer,
  spectral comparison and provenance
- verify_r2_certificate.py: new standard-library-only exact verifier;
  no old repository programs imported or executed
- r2_exact_certificate.json: required-check PASS, exact center and seed
  matrices and seed LDL pivots, 46 checked finite cores, separate negative
  large-margin diagnostics
- verification_output.json: actual stdout from the final run
- ../audit/independent_schur_tail_audit.md: independent line analysis
- ../audit/: independent direct-graph scalar-Schur seed/base replay
- Frozen baseline sources: follow the exact-commit source links in R2_ANALYTIC_TAIL_CLOSURE.md; the inherited files are preserved in this branch, without duplicating superseded drafts in this package

## Mathematical delta

1. Replace the old ten-coordinate contraction estimates by the order-unit
   norm associated with the 4×4 P weight, using DΦ[H]=LᵀHL
2. Prove an explicit local perturbation constant 14364 in Euclidean norm;
   weighted perturbation <43092×10⁻¹⁰<10⁻⁴
3. Obtain Riccati contraction 4/9 and dual response contraction 2/3
4. Define the limiting Schur series using actual trajectory pivots; no
   inverse-pivot differences are needed inside those series
5. Include both increments per pair and both terminal linear corrections
6. Prove ||S_m−S_∞||<1/500 for all even m≥26 (n≥106)
7. Fresh normalized 6×6 seed at n106 has margin1/50; two-error transfer
   gives every later core margin2/125
8. Only seven finite bases n50,58,66,74,82,90,98 remain

## Corrections which must propagate into any manuscript

The inherited 9/20 seed applies to an unnormalized 8×8 core and cannot be
used in the normalized 6×6 recurrence. Fresh exact testing disproves that
margin for the actual core. Do not silently repair just the subscript I8
to I6. Use the new seed and its new margin.

S_m in the proof uses block count m=(n−2)/4. The seed at graph order106 is
S_26. Its 2/125 lower margin does not by Schur congruence alone become a
2/125 eigenvalue gap for the entire n×n matrix.

The old r→2r G6 multiplicity correction remains untouched. This proof
does not use a G6 edge level, Feshbach rank, IMS estimate or interface count.

## Reproduction and inspected baseline

Run `python verify_r2_certificate.py`. Final run: PASS, 124 required
rational checks true. Additional graph/block identity checks at n50,58,66,410
and positivity through n410 exceed what the theorem needs. Deliberately
false seed410 margin tests at 1/20,1/10,9/20 are diagnostics, not failures
of the required certificate.

Baseline: analytic-proof-first@7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2,
continuing the August Target A lineage, not the September general-step
circulant project. These files contain the proof increment and its verification.

Final independent audit: PASS. The auditor checked the assembled proof
line-by-line and independently extracted the local pivot/response state
from the actual n106 signed graph after 96 scalar eliminations, then
rechecked every P/Q, residual and entrance premise by exact symbolic matrix
arithmetic. See ../audit/direct_graph_local_replay.json and
../audit/replay_local_from_direct_graph.py. No remaining gap was identified
for the stated explicit-family theorem; this is internal audit, not external
peer review.
