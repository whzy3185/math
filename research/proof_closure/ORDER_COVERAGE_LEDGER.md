# Complete Order Coverage Ledger

| Order set | Predicted result | Proof module | Certificate/verifier | Status |
|---|---|---|---|---|
| `8,10,12,14,16,18,20,22,24,26,28,30` | equality | complete switching/orbit exhaustion | `verify_target_a_minimality_certificate.py` | CLOSED_EXACT_COMPUTER_ASSISTED |
| `32` | strict failure | explicit period-eight signing | `verify_target_a_n32_certificate.py` | CLOSED_EXACT_COMPUTER_ASSISTED |
| `34,36,38,42,44,46` | equality | local interlacing plus parity-lifted de Bruijn closure | `verify_target_a_task55_small_order_exact.py` | CLOSED_EXACT_COMPUTER_ASSISTED |
| `40` | strict failure | explicit signing and rational LDL | `verify_target_a_task55_orders_34_46.py` | CLOSED_EXACT_COMPUTER_ASSISTED |
| every even `48<=n<240` | strict failure | 96 structured witnesses and full-matrix LDL certificates | `verify_target_a_task54_threshold.py` | CLOSED_EXACT_COMPUTER_ASSISTED |
| every even `n>=240` | strict failure | G6 local cap, residue construction, exact IMS estimate | `verify_target_a_task54_threshold.py` | CLOSED_EXACT_COMPUTER_ASSISTED |

The finite rows are pairwise disjoint. Their union together with the analytic
tail is exactly `{n: n even, n>=8}`. There is no omitted even order, no
overlap with contradictory conclusions, and no use of the non-classification
open problems listed in `PROOF_OBLIGATION_MATRIX.md`.

Consequently the equality set is exactly

```text
{8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46},
```

and the failure set is exactly `32`, `40`, and all even orders at least `48`.
