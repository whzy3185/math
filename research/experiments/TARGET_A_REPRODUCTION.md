# Target A Reproduction

Date: 2026-08-15
Overall Prompt 6 status: **IN PROGRESS**

## Environment

- Python 3.13.5
- SymPy 1.14.0
- Exact decision method: real algebraic threshold, integer characteristic polynomials, Sylvester criterion
- Exhaustive rejection certificates: rational Rayleigh quotients compared with a certified rational upper bound for the algebraic threshold

## Completed checks

### n = 8

- Switching classes: 512 (`2^(n+1)`)
- Quadrilateral constraint rank: 7 (`n−1`)
- Quadrilateral-family solution classes: 4
- Distinguished `α=−1` optimizer classes: independently reconstructed in spanning-tree gauge
- Optimizer equality: certified by the characteristic polynomial of `A²` and exact algebraic root isolation
- Exhaustive global enumeration: PASS
- Non-optimizer classes certified by rational Rayleigh bounds: 510
- Exact fallbacks required: 0
- Counterexamples: 0

## Remaining checks

The same exhaustive workflow must still be run for `n=10,12,14,16,18`. Until all five sizes pass and their logs/checksums are saved, Prompt 6 is not marked PASS and no `n=20` search is authorized.

## Commands

```powershell
python research/scripts/target_a_reproduce.py --max-n 8
python research/scripts/target_a_reproduce.py --max-n 18 --output research/logs/target_a_reproduction.json
```
