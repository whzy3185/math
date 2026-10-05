# R6 finite completion: current handoff

## Precise result

For every k≥6, N=8k+6, concatenate three legal one-G6 cells with parameters
floor(k/3), floor((k+1)/3), floor((k+2)/3), and use holonomy+1. The
resulting signing has rho²<7.92<rho_−(N)².

## Proof status

Primary exact finite verification PASS: 139 required checks and 33 strictly
positive full-graph rational LDL certificates at N=54,62,…,310. The
previously independently audited unequal-cell theorem covers k≥39/N≥318,
because every cell length is at least 106. Endpoint comparison is exact:
5782/729−198/25=208/18225>0.

The 33-graph independent gap-based replay and exposition audit also PASS,
with 139 independent checks. Floor identities, the exact tail threshold,
benchmark gap and witness-only scope have all passed line review. No new
asymptotic estimate is open.

## Files

- R6_FINITE_COMPLETION.md: full construction, finite reduction, proof,
  benchmark comparison and exact scope
- verify_r6_completion.py: self-contained standard-library exact verifier
- r6_completion_certificate.json: all finite parameters, gap words,
  positive pivot counts/digests and complete coverage checks
- verification_output.json: actual exact-run stdout
- audit/INDEPENDENT_R6_AUDIT.md: independent mathematical and exact audit
- audit/replay_r6.py, independent_replay.json and verification_stdout.txt:
  independent finite-graph reproduction

The floating diagnostic is not theorem evidence. The theorem depends on
the frozen ../unequal_cells/ result and its already verified R2 premises.
No completed sibling files were changed.

## Boundaries

These placements may differ from the old balanced-gap family when k is not
divisible by three. Every new finite graph was reconstructed from its own
specified edge signs. The statement is an explicit counterexample family,
not global minimization, equality rigidity, or a Lean formalization.

Combined with the known period-eight and R2/R4 witnesses, it completes the
construction side for all even N≥48. The smaller equality orders and the
actual optimum over all signings remain separate.
