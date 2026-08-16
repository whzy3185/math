# Target A Claim-Evidence Matrix

Status: **TARGET_A_CLAIM_EVIDENCE_MATRIX_COMPLETE**

Abbreviations: `Min` = smallest-counterexample package; `P8F` = period-8
family/Floquet audit; `Sharp` = sharp-constant package; `Class` = period-8
classification; `Struct` = period-8 structural mechanism; `Gen` = general
moments; `Low` = low-period spectral frontier; `Compress` = low-period
structural frontier. Exact paths and SHA-256 values are in the claim inventory.

| Claim | Human proof | Machine certificate | Checker | Regression | Fresh reproduction | Novelty | Scope |
|---|---|---|---|---|---|---|---|
| C1 | Min | minimality certificate | minimality checker | minimality tests | n32 + n24-30 | N1 | original conjecture |
| C2 | Min | n32 exact certificate | n32/minimality checkers | n32 tests | independent n32 reconstruction | N2 | explicit `n=32` witness |
| C3 | Min | dependency manifest/chains | minimality checker | integrity replay tests | partial fresh `n=24..30` | N2 | exact `n=8..30` |
| C4 | P8F | family certificate | infinite-family checker | uniform-bound tests | n32 witness | N3 | `n>=32`, divisible by 8 |
| C5 | Floquet audit | audit JSON | independent Floquet route | Floquet tests | finite n32 cross-check | N3 | target cell |
| C6 | Floquet audit | polynomial snapshot | independent determinant | Floquet tests | coefficient match | N3 | target cell |
| C7 | Sharp | sharp JSON | sharp checker | sharp tests | n32 threshold cross-check | N4 | target phase |
| C8 | Class + Struct | classification JSON | classification checker | classification tests | not a logical premise | N5 | period 8 |
| C9 | Class + Struct | classification JSON | classification checker | classification tests | not a logical premise | N6 | period 8 |
| C10 | Struct | structural JSON | structural checker | structural tests | not a logical premise | N7 | period 8 |
| C11 | Struct/Gen | structural JSON | structural checker | local-formula tests | not needed | N8 | local identity |
| C12 | Struct | structural JSON | structural checker | moment tests | not needed | N8 | period 8 |
| C13 | Gen | general-moment JSON | general checker | implication-direction tests | not needed | N8 | periodic Bloch families |
| C14 | Struct | structural JSON | structural checker | d=2 tests | not needed | N8 | period-8 d=2 shell |
| C15 | Struct | structural JSON | structural checker | anti-periodicity tests | not needed | N9 | target/chiral classes |
| C16 | Struct | structural JSON | structural checker | involution tests | not needed | N9 | target fiber |
| C17 | Gen | general-moment JSON | general checker | small-period tests | not needed | N10 | every `p>=1` |
| C18 | Gen | general-moment JSON | general checker | small-period tests | not needed | N10 | every `p>=1` |
| C19 | Gen | general-moment JSON | general checker | collision tests | not needed | N10 | every `p>=1` |
| C20 | Gen | general-moment JSON | general checker | direction tests | not needed | N10 | necessary only |
| C21 | Gen | general-moment JSON | general checker | direction tests | not needed | N10 | necessary only |
| C22 | Low | 2626-orbit JSON | low-period checker | orbit/Burnside tests | not needed | N11 | `p<=16` representations |
| C23 | Low + Compress | frontier JSON | two independent checkers | frontier tests | not needed | N11 | primitive `tau<=16` |
| C24 | operator equivalence lemma | equivalence JSON | transition-level checker | 65,535-word audit | not needed | N11 | all periodic cells; audited `p<=16` |
| C25 | Compress + C24 | compression JSON | structural-frontier/equivalence checkers | partition tests | not needed | N11 | `p<=16` table |

Fresh reproduction is recorded only where it directly exercises the finite
minimality implementation. A blank logical role would be misleading, so other
rows explicitly say “not needed” rather than treating reproduction as a lemma.
