# Final Mathematical Proof Status

| Module | Status | Proof type | Main theorem dependency | Remaining issue |
|---|---|---|---|---|
| switching and normalization | CLOSED_ANALYTIC | diagonal gauge and cycle coordinates | yes | none |
| twisted spectrum | CLOSED_ANALYTIC | Fourier block computation | yes | none |
| period-eight bulk | CLOSED_EXACT_COMPUTER_ASSISTED | symbolic Floquet polynomial and exact positivity | yes | none |
| phase-slip charge | CLOSED_ANALYTIC | endpoint-sector arithmetic | yes | none |
| G6 spectral theorem | CLOSED_EXACT_COMPUTER_ASSISTED | exact transfer/Evans/Sturm plus global atlas | yes | none |
| G6 localization | CLOSED_EXACT_COMPUTER_ASSISTED | stable/unstable matching and multiplier bound | yes | none |
| abnormal single-gap theorem | CLOSED_EXACT_COMPUTER_ASSISTED | finite-support rational Rayleigh witnesses | supporting | no multi-gap extension claimed |
| large-cycle construction | CLOSED_EXACT_COMPUTER_ASSISTED | residue words and local patch identification | yes | none |
| IMS | CLOSED_ANALYTIC plus exact geometry | commutator identity and tent estimate | yes | none |
| analytic threshold | CLOSED_EXACT_COMPUTER_ASSISTED | threshold ledger, `N_an=240` | yes | none |
| `n=32` | CLOSED_EXACT_COMPUTER_ASSISTED | explicit signing and two exact PD checks | yes | none |
| `n=40` | CLOSED_EXACT_COMPUTER_ASSISTED | explicit signing and rational LDL | yes | none |
| finite failure bridge | CLOSED_EXACT_COMPUTER_ASSISTED | 96 exact full-matrix LDL rows | yes | none |
| small equality orders | CLOSED_EXACT_COMPUTER_ASSISTED | exhaustive switching/orbit coverage | yes | none |
| recovered equality orders | CLOSED_EXACT_COMPUTER_ASSISTED | sound local pruning and complete de Bruijn closure | yes | none |
| equality certificate semantics | CLOSED_EXACT_COMPUTER_ASSISTED | terminal lower certificates in both holonomies | yes | none |
| order coverage | CLOSED_EXACT_COMPUTER_ASSISTED | disjoint complete partition | yes | none |
| universal finite-core interface theorem | OPEN | bounded and motif subclasses only | no | unbounded primitive cores |
| unrestricted common nonzero-residue limit | OPEN | only upper bounds/restricted lower bounds | no | tight/dichotomy/vanishing/aperiodic cases |
| interaction coefficients and simplicity | OPEN | high-precision evidence only | no | certified leading terms |

## Classification decision

`CLASS` is `CLOSED_EXACT_COMPUTER_ASSISTED`:

```text
m_n < rho_-(n) iff n=32, n=40, or n is even and n>=48.
```

The statement does not assert all minimizers, exact `m_n` at failing orders, a universal multi-gap lower theorem, or a common nonzero-residue limit. Those are intentionally excluded rather than silently weakened.

## Independent verification run

On this branch, `/tmp/target-a-proof-venv/bin/python research/scripts/verify_target_a_proof_closure.py --full` passed all 13 exact verifiers: Task 50 interface, Task 51 algebra, Task 53 global-edge checks, Task 55 exact-2r/single-gap/small-order/order-34--46 checks, Task 56--57 single-gap checks, the minimality and order-32 certificates, and Task 54 threshold verification.
