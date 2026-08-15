# Target A Reproduction

Date: 2026-08-15
Overall Prompt 6 status: **PASS**

## Environment

- Python 3.12.13 in local `.venv`
- NumPy 2.3.5 from the Codex bundled runtime via `PYTHONPATH`
- SymPy 1.14.0
- Exact decision method: real algebraic threshold, integer characteristic polynomials, Sylvester criterion
- Exhaustive rejection certificates: rational Rayleigh quotients compared with a certified rational upper bound for the algebraic threshold

## Completed checks

### n = 8, 10, 12, 14, 16, 18

Full reproduction of the source paper's reported numerical range now passes.
For every tested even `n`, the switching-class count is `2^(n+1)`,
the quadrilateral constraint rank is `n-1`, and the quadrilateral-family
solution count is exactly 4.

| n | switching classes | optimizer classes | non-optimizers certified by rational Rayleigh bounds | exact fallbacks | counterexamples | status |
|---:|---:|---:|---:|---:|---:|---|
| 8 | 512 | 2 | 510 | 0 | 0 | PASS |
| 10 | 2,048 | 2 | 2,046 | 0 | 0 | PASS |
| 12 | 8,192 | 2 | 8,190 | 0 | 0 | PASS |
| 14 | 32,768 | 2 | 32,766 | 0 | 0 | PASS |
| 16 | 131,072 | 2 | 131,070 | 0 | 0 | PASS |
| 18 | 524,288 | 2 | 524,286 | 0 | 0 | PASS |

The full JSON report is saved at `research/logs/target_a_reproduction_n8_18.json`.
SHA-256:

```text
141d0253159acde39473cf4f825f65d438cd56e8433e407c3302fe048ad3715e  research/logs/target_a_reproduction_n8_18.json
```

## First n = 20 Search

After Prompt 6 passed, the same exhaustive workflow was run for `n=20`.
No counterexample was found.

| n | switching classes | optimizer classes | non-optimizers certified by rational Rayleigh bounds | exact fallbacks | counterexamples | status | elapsed seconds |
|---:|---:|---:|---:|---:|---:|---|---:|
| 20 | 2,097,152 | 2 | 2,097,150 | 0 | 0 | PASS | 98.4565 |

The full JSON report is saved at `research/logs/target_a_search_n20.json`.
SHA-256:

```text
20a0d812a268d51c4c52188c63827732216815f20901ef83ad680816d82fbcc4  research/logs/target_a_search_n20.json
```

Evidence status: **Verified for the finite enumerated ranges above**.
This is not a proof for all even `n`.

## Flux quotient search and disproof

The follow-up search enumerated binary bracelets in `(Q,alpha)` coordinates.
At `n=20`, 27,296 spectral states reproduced the raw 2,097,152-class minimum,
including the same smallest non-optimizer.  At `n=22`, all 97,468 spectral
states, representing all 8,388,608 switching classes, were checked.  All
97,467 non-optimizer states had exact rational Rayleigh exclusion
certificates; there were no exact fallbacks and no counterexamples.

The `n=20` atlas showed that the smallest non-optimizer is a `d=4` pattern,
not a `d=2` domain-wall state.  Its cyclic defect gaps `(4,6,4,6)` suggested
a periodic structured attack.  Searching periodic Q-patterns of period at
most 12 found the stronger pattern `Q=(+,-,-,-)`, with triangle-flux period 8.

This pattern yields a proved infinite counterexample family for every
multiple of 8 with `n≥32`.  The symbolic Floquet proof certifies

`rho(A)^2 < 1561/200 < rho_-(n)^2`.

The explicit `n=32` witness is independently certified by both fraction-free
Bareiss/Sylvester minors and a rational `LDL^T` decomposition.  Accordingly,
Target A is now **DISPROVED**.  The remaining `n=24,26,28,30` range is open
only as a smallest-counterexample question.

## Commands

```bash
PYTHONPATH=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages \
  .venv/bin/python research/scripts/target_a_reproduce.py \
  --max-n 18 \
  --output research/logs/target_a_reproduction_n8_18.json

PYTHONPATH=/Users/muelsyse/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages \
  .venv/bin/python - <<'PY'
import json
from pathlib import Path
import sys
sys.path.insert(0, 'research/scripts')
from target_a_reproduce import reproduce_n
result = reproduce_n(20, True)
payload = {
    'method': 'exact optimizer roots + rational Rayleigh certificates + exact fallback',
    'results': [result],
    'overall': result['status'],
}
Path('research/logs/target_a_search_n20.json').write_text(
    json.dumps(payload, ensure_ascii=False, indent=2) + '\n',
    encoding='utf-8',
)
print(json.dumps(payload, ensure_ascii=False, indent=2))
raise SystemExit(0 if result['status'] == 'PASS' else 1)
PY
```

## Implementation Note

The optimizer equality check now tests whether the threshold's minimal
polynomial divides the characteristic polynomial of `A^2`.  This avoids a
SymPy simplification failure observed at `n=14`, where direct substitution was
numerically zero but not simplified to the exact integer `0`.
