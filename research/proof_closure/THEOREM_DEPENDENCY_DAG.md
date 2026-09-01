# Theorem Dependency DAG

```text
switching and flux coordinates ----> twisted benchmark theorem

period-eight fiber polynomial ------> reference bulk theorem
phase-slip charge ------------------> legal residue constructions

exact G6 transfer + root isolation --> G6 interface theorem
G6 interface theorem + global candidate exclusion --> G6 edge/localization theorem
G6 edge + charge constructions + IMS identity ----------> analytic-tail theorem (n>=240)

explicit finite signing + exact LDL --------------------> failure witness theorem
failure witness theorem, 96 rows ----------------------> finite failure bridge (48<=n<240)
analytic-tail theorem + finite failure bridge ---------> contiguous failure tail (n>=48)

switching coverage + exact lower certificates ---------> small equality theorem (8<=n<=30)
window exclusion + parity closure + terminal checks ----> recovered equality theorem
explicit LDL witness ----------------------------------> order-32 and order-40 failures

small equality + recovered equality + order-32/order-40 witnesses
    + contiguous failure tail --------------------------> complete classification theorem
```

## Dependency assertions

| Theorem | Inputs | Output | Does not use |
|---|---|---|---|
| Twisted benchmark | switching coordinates, Fourier blocks | exact `rho_-(n)` formula | numerical eigensolves |
| Reference bulk | finite Floquet polynomial | exact edge `eta` | global signing optimization |
| G6 mechanism | reference bulk, transfer, Evans, global atlas | `sup sigma(H6)=c6`, rank two, localization | finite-order classification |
| Analytic tail | G6 edge, charge, IMS | failure for every even `n>=240` | exact-2r cluster count or universal interface theorem |
| Finite failure bridge | individual signings and LDL | failure for `48<=n<240` | equality enumeration |
| Equality theorems | complete representative coverage plus lower certificates | no counterexample at listed orders | failure LDL witnesses |
| Complete classification | disjoint order modules | stated truth set | any open asymptotic program |

This graph is acyclic. In particular, finite pruning never invokes the complete classification, and the G6 theorem is proved before it is used in the tail. The old rank-one `r x r` Feshbach chain is absent because it is obsolete.
