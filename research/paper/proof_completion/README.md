# Target A Canonical Proof-Completion Package

This directory is the canonical-current mathematical layer for the Target A
paper. It is intentionally separate from the frozen English and Chinese LaTeX
manuscripts.

## Reading Order

1. `TARGET_A_JGT_THEOREM_HIERARCHY.md`
2. `TARGET_A_FINAL_NOTATION.md`
3. `01_even_order_classification/`
4. `03_reference_phase/`, `04_charge_sector/`, and `05_g6_edge/`
5. `06_single_gap/`, `07_exact_2r/`, and `08_residue_ims/`
6. `02_small_order_34_46/` and `10_computer_assisted/` for the exact finite
   proof architecture
7. `11_stale_claim_audit/` and `12_referee_review/` for safety and hostile
   review

Every major theorem directory separates the mathematical statement and proof
from dependencies, computer-assisted boundaries, and referee checks. Internal
Task numbers occur only in provenance material, not as mathematical
dependencies.

## Evidence Rule

The package accepts a machine-assisted conclusion only after a mathematical
reduction to a finite exact object and an implementation-independent checker.
Floating-point computations may propose witnesses or intervals but are never
logical endpoints.

The minimal referee entry point is:

```bash
python3 research/scripts/verify_target_a_task57.py
```
