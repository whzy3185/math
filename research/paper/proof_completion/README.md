# Target A Canonical Proof-Completion Package

This directory is the canonical-current mathematical layer for the Target A
paper. It is intentionally separate from the frozen English and Chinese LaTeX
manuscripts.

The editorial hierarchy contains exactly seven main theorem families,
Theorems 1.1--1.7. They are the complete even-order classification, reference
phase, gap/charge sector law, elementary G6 phase slip, single-gap optimality,
separated phase slips, and residue-class upper constructions. Do not compress
this list to six families by merging Theorems 1.6 and 1.7.

## Reading Order

1. `TARGET_A_JGT_THEOREM_HIERARCHY.md`
2. `TARGET_A_FINAL_NOTATION.md`
3. `TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md`
4. `01_even_order_classification/`
5. `03_reference_phase/`, `04_charge_sector/`, and `05_g6_edge/`
6. `06_single_gap/`, `07_exact_2r/`, and `08_residue_ims/`
7. `02_small_order_34_46/` and `10_computer_assisted/` for the exact finite
   proof architecture
8. `11_stale_claim_audit/` and `12_referee_review/` for safety and hostile
   review

Every major theorem directory separates the mathematical statement and proof
from dependencies, computer-assisted boundaries, and referee checks. Internal
Task numbers occur only in provenance material, not as mathematical
dependencies.

## Logical Convention

Set `theta_n=rho_-(n)^2`. The conjecture fails at `n` precisely when
`m_n<rho_-(n)`, equivalently `m_n^2<theta_n`. A proof that every signing
satisfies `rho(A_sigma)>=rho_-(n)` establishes only `m_n>=rho_-(n)`. When the
original conjecture is stated as the equality `m_n=rho_-(n)`, equality at a
valid order also requires an explicit candidate attaining the opposite bound
`m_n<=rho_-(n)`. These two logical directions must be cited separately.

## Import Rule

The recursive default for this directory is `CANONICAL_IMPORT`, subject to
the exact-path overrides in
[TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md](TARGET_A_MANUSCRIPT_IMPORT_SAFETY.md).
Historical research documents are not canonical merely because a canonical
proof cites them as provenance.

## Evidence Rule

The package accepts a machine-assisted conclusion only after a mathematical
reduction to a finite exact object and an implementation-independent checker.
Floating-point computations may propose witnesses or intervals but are never
logical endpoints.

The minimal referee entry point is:

```bash
python3 research/scripts/verify_target_a_task575.py
```

This runs the inherited 13-checker Task 57 chain and the focused Task 57.5
proof-connection gate.
