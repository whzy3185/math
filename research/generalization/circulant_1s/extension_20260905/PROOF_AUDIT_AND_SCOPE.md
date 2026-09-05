# Proof audit and scope of the new results

This is an inline critical check of the author's derivation, not an external
or independent reviewer report. No subagents or external models were used.

## Scope check before proof

The user's new instruction explicitly permits conjecture generation and
mathematical extension beyond the old strengthening boundary. The old paper
is frozen; all new work is isolated in this directory and a separate worktree.
Task 60's universal square and alternating dispersion are acknowledged inputs.
The flat construction is inherited, not labelled new.

## Most important potential failure and its resolution

`det(8I-K)>0` does not imply `8I-K>0`. The proof fixes inertia at `xi=i`,
using a connected diagonally dominant Hermitian matrix with strict rows,
then uses the nonvanishing determinant on the full unit circle. This step
is required in addition to the Chebyshev calculation.

## Specific checked interfaces

| issue | resolution in the written proof |
|---|---|
| finite phase sampling vs all phases | the generating function proves positive coefficients for every `r`; continuity covers the entire circle |
| `s=2` coincident matrix channels | treated separately and checked directly; the eight-endpoint Schur calculation starts at `r=2` |
| changing the square root `xi` of `z` | exchanges isospectral squared chiral blocks; polynomial is even in `h` |
| division in chain elimination | at threshold all denominators `D_j(d)` are positive; full polynomial identity extends from the nonzero-denominator domain |
| sign of the Schur interior determinant | two copies of each positive continuant factor, exactly `c_0^2 d_0^2` |
| all-even quantifier | follows from scalar recurrence identities and convexity, not interpolation in `s` |
| positive determinant vs a quantitative gap | after inertia is established, all `C` eigenvalues lie in `(0,8]`; divide the determinant bound by `8^(2s-1)` |
| all finite rings and both holonomies | exact finite direct sum over `z^L=alpha` |
| smallest-angle assertion for the twisted maximum | not used; `theta=pi/N` is merely one allowed point giving a lower bound |
| primitive period vs minimal feasible period | the constructed word has primitive period `4s`; no optimal-period claim is made |
| flat spectra at exceptional `(8,3)` | treated as `K_(4,4)` with Hadamard sign matrices, not forced into the alternating rigidity statement |
| odd-step chirality | the half-cell sign is `(-1)^(s+1)` and differs from ordinary bipartite chirality |

## Algebraic cross-checks

`verify_extension.py` includes a symbolic five-variable verification of the
eight-endpoint determinant and an algebraic characteristic-root verification
of the fourth-order product-continuant recurrence. It separately reconstructs
the original `4s` matrix, checks the reduced chain, and compares the scalar
formula against its direct characteristic polynomial at four squared spectral
parameters and five exact phases, for even jumps 2 through 16.

It also checks the generating series through degree 12, rejects an intentionally
altered recurrence, tests the chiral criterion over short sign words, and
enumerates all Hamilton switching coordinates for orders 5 through 12 in
the flat-spectrum classification. The exact populations and outcomes are
stored in `EXACT_AUDIT.json`.

The symbolic recurrence identity supports the analytic argument. The finite
matrix cases are regression tests, not a universal formal proof. The Lean
tree was not extended, and no new result is described as Lean-checked.

## What remains unsettled

1. The all-even sub-eight theorem's external priority has not been established.
2. Sharp finite thresholds, sharp spectral gaps and the exact maximizing phase
   are not obtained by the coarse positive-determinant estimate.
3. No all-signings global minimizer is proved outside the flat resonance family.
4. The odd-jump problem uses a different reference threshold and remains open
   within this extension.
5. Further independent mathematical reading would be useful before replacing
   the frozen article's main theorem with this larger package.

The first round is closed with analytic proofs of the four recorded
conjectures. Subsequent work should start from these precise remaining
questions rather than silently strengthening their statements.
