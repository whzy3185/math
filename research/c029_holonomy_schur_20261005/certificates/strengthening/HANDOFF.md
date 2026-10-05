# Uniform one-G6 strengthening: final result

## Theorem

For every k≥1, n=8k+2, the alpha=+1 signing with step-two word
(1,1,−1,1,−1,−1,1,−1)^k followed by (1,−1) satisfies

    ρ(A_n)² < 790537/100000 = 7.90537.

At n=202 it also satisfies

    ρ(A_202)² > 7905369/1000000 = 7.905369.

Thus the supremum over this prescribed family belongs to
(7.905369,7.90537], an interval of width10⁻⁶. No global minimum over all
signings, exact supremum, limiting convergence, or monotonicity is asserted.

Evidence: Proved, finite-certificate-assisted analytic theorem. Primary exact
verification and independent direct-graph/analytic audit both PASS. No Lean
formalization of this theorem.

## What changed

- Improved the previous cap7.92 and extended k≥6 to all k≥1
- New cap requires fresh local data: the old index24 and2/5 metric
  inequalities fail after the cap is lowered
- New entrance J48, center metric factor1/2, response3/4, Riccati9/16,
  radius10⁻¹⁸ and response quadratic bound10⁻²⁰ work
- Seed at n202 has exact normalized six-core margin10⁻⁶
- Uniform analytic tail<10⁻⁸ and two-error transfer give core margin
  49/50000000 for all later even block counts
- Exactly24 smaller finite bases n10,18,…,194 close all k≥1
- The n10 full matrix is checked separately because two block couplings
  coincide there
- An exact negative LDL pivot at the lower cap supplies the finite lower
  obstruction and the rigorous supremum bracket

## Files and verification

UNIFORM_ONE_G6_CAP.md contains the complete strengthened argument, using the
previous proof's block identity and response formula with new fixed-energy
premises. verify_uniform_cap.py is self-contained Python standard-library
code. Its actual run passes79 required rational checks and all25 recorded
orders (24 bases plus seed). Outputs: uniform_cap_certificate.json and
uniform_cap_output.json.

Independent reproduction is under audit/. replay_stronger_cap.py builds
the full signed graphs and performs scalar Schur elimination, including the
192-step entrance and the196-step lower-obstruction core. It uses SymPy and
imports no primary-verifier modules. All local premises and finite graphs
pass, and exact center, seed LDL pivots, lower LDL prefix and tail constant
match the primary certificate. Final exposition audit found no discrepancy.

The original validated ../analytic/ files remain frozen. This package is a
separate strengthening, ready for a later manuscript/repository increment.

## Preserved tests and remaining boundaries

Preliminary floating diagnostics and unsuccessful fixed-center certificate tests are not part of the theorem certificate. Every theorem premise is independently reproduced by the included exact verifiers.

The inherited R4/R6 audit was read before selecting this target. No new
multi-interface template was constructed, and those analytic gaps remain
open. This proof uses neither the historical G6 physical-edge certificate
nor any interface multiplicity or rank assumption.
