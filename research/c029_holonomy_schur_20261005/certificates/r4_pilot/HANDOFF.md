# Phase lifting and the even-k R4 line

## Current status

Complete proof, all 20 primary exact checks, and 72 independent replay checks
PASS. The all-phase and all-r arguments have also passed independent line
audit. Evidence: finite-certificate-assisted analytic theorem, without Lean
formalization or external peer review. Existing analytic/ and strengthening/
packages remain unchanged.

## New results

1. A one-G6 phased Hermitian cell A_h(z), h=8j+2≥202, satisfies
   ρ(A_h(z))²<7.90537 simultaneously for every complex |z|=1
2. Repeating that cell r times with either global real holonomy gives the
   same cap for every integer r≥1, by the exact fibers z^r=α
3. The balanced R4 family with even k, N=8k+4=16j+4 and α=−1,
   satisfies the same cap for every j≥1 after 24 exact finite bases
4. For j≥3, N≥52, these signings strictly beat the twisted benchmark
5. A strict exact negative-pivot certificate at the odd-k case N=60 proves
   that the sharp cap cannot be extended to all balanced R4 orders

The equal-cell theorem is not a theorem for arbitrary arrangements of r
interfaces. No localized-mode count, old G6 edge certificate or IMS estimate
is used. The historical r→2r correction is respected by using a full
unitary spectral decomposition instead of a reduced mode count.

## Essential argument

All phase dependence in the initial normalized Schur system is
C_0(z)=conjugate(z)C_0 and W_0(z)=conjugate(z)W_0. After eliminating
the bulk, conjugation by U_z=diag(I_2,zI_4) leaves only phase factors on
the decaying terminal cross terms. The limiting six-core is therefore
exactly the old unphased S_∞, and the old rigorous tail constants are
uniform in z. The verified seed at h=202 transfers to every phase.

Repeating the coefficient cell uses all the characters z^r=α. For r=2,
α=−1 these are ±i. Twenty-four full real graph bases N=20,36,…,388
complete the R4 even-k line. The h=10/N=20 block-overlap exception is
handled as a full graph, not by assuming distinct wrap blocks.

## Files

- PHASE_UNIFORM_R4_ASSEMBLY.md: complete new mathematical argument,
  scope, finite reduction, counterexample to parity deletion and citations
- verify_r4_pilot.py: standalone standard-library exact verifier
- r4_pilot_certificate.json: all 20 required checks passed, 24 positive
  finite graph cases with exact pivot hashes, and the full strictly negative
  odd-k LDL prefix
- verification_output.json: actual primary execution output
- audit/INDEPENDENT_R4_PHASE_AUDIT.md: independent proof and exact audit
- audit/replay_r4_phase.py, independent_replay.json and
  verification_stdout.txt: independent symbolic-phase, quotient-ring and
  full-graph scalar LDL reproduction

The diagnostic float script and observations are not theorem evidence.
The primary checks include symbolic Laurent-polynomial block identities
and exact Gaussian-integer fiber embeddings, rather than phase sampling.

## Next boundary

For odd k the two-G6 half-cell has τ_(i+h)=−τ_i, not τ_(i+h)=τ_i.
Its half-length is 8j+6, and it requires a different gluing statement or a
larger retained core. The present argument does not include that case.
