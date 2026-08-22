# Target A Charge Conservation

For positive-`Q` gap word `(g_1,...,g_d)`, define `q_i=g_i-4`.  The cycle
partition and periodic lift give exactly

```text
sum g_i=n,  sum q_i=n-4d,  product Q=(-1)^(n-d)=1.
```

For even `n`, `d` is even and total charge is congruent to `n mod 8`.

| `n mod 8` | Minimal nonnegative decomposition | Nearest negative total | Other totals |
|---:|---|---:|---|
| 0 | `[]` | `-8` | `...,-8,0,8,...` |
| 2 | `[+2]` | `-6` | `...,-6,2,10,...` |
| 4 | `[+2,+2]` | `-4` | `...,-4,4,12,...` |
| 6 | `[+2,+2,+2]` | `-2` | `...,-2,6,14,...` |

Both holonomies occur in the exact closure and do not change charge.  The
table proves arithmetic minimality only; it does not prove that a listed
decomposition minimizes spectral radius.

Status: `EXACT_CHARGE_CONSERVATION_PROVED`.
