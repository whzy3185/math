# Occurrence Classification and Import Policy

The authoritative line-by-line table is
`../TARGET_A_STALE_RANK_CLAIM_AUDIT.md`.

The authoritative manuscript-import decisions are in
`../TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`.

## Canonical rule

For the squared interface operator,

```text
dim ker(H_6-c6)=2.
```

For `r in {1,2,3}` sufficiently separated G6 interfaces, the certified
near-`c6` cluster contains exactly `2r` squared eigenvalues counted with
multiplicity, the complement has codimension `2r`, and the problem-specific
Feshbach operator is `2r x 2r`.

The positive unsquared root `+sqrt(c6)` may be simple. That does not make the
squared eigenvalue `c6` simple: anticommutation supplies the simple negative
partner, and both square to the same level.

## Import policy

1. Import current theorem prose only from a `CANONICAL_IMPORT` source.
2. A more specific exact-path rule overrides every directory default.
3. Historical exact-`r` files are `HISTORICAL_ONLY`: they may be cited only as
   provenance of a retraction, never as a theorem dependency.
4. The two exact paths below are `DO_NOT_IMPORT_CURRENT_CLAIMS`, not merely
   sentences to be rewritten:

   ```text
   research/proofs/task52/TARGET_A_MULTI_SLIP_INTERACTION_ASYMPTOTICS.md
   research/proofs/task54/TARGET_A_COMMON_RESIDUE_LIMIT_SCOPE.md
   ```

   No formula, theorem, or proof step from either path may be imported as a
   current claim.
5. Retraction producers, certificates, and forbidden-token tests remain in
   the repository because they prevent regression.
6. A reduced `r x r` model would require a separately proved invariant
   symmetry sector. No such reduction is currently claimed.

## Current proof-package status

The new proof-completion packages use `t` for interface count in the IMS
argument and `2t` wherever spectral multiplicity matters. They contain no
accepted rank-one or exact-`t` squared-mode statement.

This classification is a producer-side audit. It does not claim independent
verification of the underlying spectral theorems.
