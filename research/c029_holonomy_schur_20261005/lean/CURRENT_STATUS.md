# Current formal checkpoint: 264 audited declarations

The [246-declaration constant-alignment report](constant_alignment/CONSTANT_ALIGNMENT_VERIFICATION_REPORT.md) proves that the explicit endpoint radical is the global largest real root of x^4−2x^3−6x^2+12x−4. The strict eigenvalue-modulus comparison for the raw negative-holonomy matrix is verified for every L>0, with the Conjecture 28 family statement for L>=4. This closes the algebraic naming gap left in the 237 checkpoint.

The [254-declaration terminal-Schur addendum](r2_terminal/R2_TERMINAL_VERIFICATION_REPORT.md) adds a typed Fin 10 to Fin 6 positive-definiteness equivalence under an explicit positive Fin 4 pivot, plus the exact terminal C/H corrections and actual E-plus specialization. It does not formalize the full R2 family. The pivot orbit, graph-to-block identification, finite seed, contraction, response decay and infinite tails remain obligations.

The [264-declaration finite-seed addendum](r2_seed106/R2_SEED106_VERIFICATION_REPORT.md) verifies that the explicit recorded normalized 6-by-6 rational seed minus (1/50)I is positive definite. Exact rational LDL factorization and positive pivots are kernel checked. Identification of this datum with the recurrence or raw graph remains unproved in Lean.

These increments built successfully and passed full axiom audits using only propext, Classical.choice and Quot.sound. Sources and portable audit drivers are installed under the repository formal/ directory. Reproduce the constant-alignment checkpoint first, then the incremental terminal-Schur package.

The [237-declaration exact-radius report](exact_radius/EXACT_RADIUS_VERIFICATION_REPORT.md) and earlier 165/196 bundles remain unchanged historical checkpoints. The reviewed 18-page paper remains at its explicit 237 checkpoint; these linked reports are subsequent addenda. The exact finite-radius formula includes both the universal modulus bound and an attained eigenvalue for every L>0.

Integer n32 certification, all-length R2/R4/R6 results, finite-size asymptotics and unrestricted minima are not end-to-end Lean claims here.
