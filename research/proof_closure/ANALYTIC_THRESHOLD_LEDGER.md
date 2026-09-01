# Analytic Threshold Ledger

`N_an` denotes the start of the analytic IMS construction, not the first
counterexample order. The verified finite exact bridge then lowers the final
contiguous witness threshold to 48.

| Constraint | Exact role | Bound used | Closed by |
|---|---|---:|---|
| `N_charge` | residue-two/four/six gap words have the required sector shift and cyclic lift | absorbed by the explicit construction for `n>=240` | `TARGET_A_RESIDUE_CLASS_THEOREM.md` |
| `N_embedding` | each G6 patch lies in a bulk region matching the infinite model | absorbed by separation geometry at `n>=240` | Task 53 patch classification |
| `N_separation` | chosen patches do not overlap and the cyclic tent condition holds | `n>=240` | exact cyclic placement audit |
| `N_localization` | G6 local cap is available on every patch | no additional order bound after the G6 edge theorem | Task 53 global edge |
| `N_IMS` | exact tent error is below the strict benchmark margin | `240` | `verify_target_a_task54_threshold.py` |
| `N_residue` | all four even residue classes are represented | `240` | Task 54 residue geometry |

Thus

```text
N_an=max(N_charge,N_embedding,N_separation,N_localization,N_IMS,N_residue)=240.
```

For every even `n>=240`, the certified construction supplies a signing with
`rho(A)^2<rho_-(n)^2`.  The separate finite bridge supplies the same strict
inequality for every even `48<=n<240`, using 96 exact rational LDL rows.
Therefore

```text
N_star=48,
```

but this is a composite analytic-plus-finite threshold, not a claim that the
analytic IMS proof begins at 48. The former historical bound `2500` is
superseded by the exact Task 54 tent arithmetic; it remains provenance only.
