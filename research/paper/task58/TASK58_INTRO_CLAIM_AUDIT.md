# Task 58 Introduction Claim Audit

Status: `TASK58_4_DRAFT_AUDIT`.

This audit covers the abstract and Introduction in
`research/paper/manuscript_tex_task58/`. Canonical proof sources, rather than
historical manuscript prose or research-stage reports, control every
mathematical statement.

| Claim | Canonical source | Evidence level | Publication wording | Overclaim risk and control |
|---|---|---|---|---|
| Object is the independently edge-signed cycle square (C_n^2=C_n(1,2)) | `proof_completion/03_reference_phase/FULL_PROOF.md`, T1.1 | `PURE_ANALYTIC_PROVED` | The already formed cycle square is signed | Prevents the title from suggesting that a signed cycle is squared |
| Switching preserves the spectrum and defines the quotient domain | `proof_completion/03_reference_phase/FULL_PROOF.md`, T1.1 | `PURE_ANALYTIC_PROVED` | Diagonal conjugacy preserves the spectrum | No claim that switching lists every further operator equivalence |
| The twisted candidate attains (ho_-(n)) at every even order | `proof_completion/01_even_order_classification/CANDIDATE_ATTAINMENT_LEMMA.md`, T8.0 | `PURE_ANALYTIC_PROVED` | Direct antiperiodic Fourier calculation; (m_n\leq\rho_-(n)) | Kept logically separate from exhaustive lower bounds |
| Complete validity and failure sets | `proof_completion/01_even_order_classification/FULL_PROOF.md`, T8.4 | `COMPUTER_ASSISTED_PROVED` | Failure exactly at (32), (40), and every even (n\geq48) | The theorem classifies equality truth, not all minimizers or exact failing values |
| Finite classification determines the irregular small-order pattern | `proof_completion/01_even_order_classification/FULL_PROOF.md`, T8.1, T8.4; `proof_completion/02_small_order_34_46/FULL_PROOF.md`, T8.2, T8.3 | `COMPUTER_ASSISTED_PROVED` | "determines" | No conceptual attribution of the isolated failures to G6 |
| Reference edge (eta=4+\sqrt{10+2\sqrt5}<8) | `proof_completion/03_reference_phase/FULL_PROOF.md`, T2.2 | `EXACT_ALGEBRAIC_PROVED` | Exact radical, not a decimal | The reference phase is not called the attaining candidate |
| Charge and sector laws | `proof_completion/04_charge_sector/FULL_PROOF.md`, T3.1--T3.3 | `PURE_ANALYTIC_PROVED` | (sum q_j\equiv n\pmod8), (sigma_{\rm sec}(q)=q\pmod4) | Global mod 8 closure and local mod 4 sector are explicitly distinguished |
| Exact definition and isolation of (c_6) | `proof_completion/05_g6_edge/THEOREM_STATEMENT.md`, T4.1 | `COMPUTER_ASSISTED_PROVED` | Degree-ten polynomial and rational isolating interval printed before use | No decimal comparison is used as proof |
| G6 squared edge and rank | `proof_completion/05_g6_edge/FULL_PROOF.md`, T4.2--T4.3 | `COMPUTER_ASSISTED_PROVED`; analytic corollary | (E(6)=c_6), (dim\ker(H_6-c_6)=2) | Never calls (c_6) simple for (H_6); both lifts and orientations retained |
| Complete abnormal single-gap hierarchy | `proof_completion/06_single_gap/FULL_PROOF.md`, T5.1--T5.2 | `ANALYTIC_COROLLARY_OF_CERTIFIED_INPUTS` | Every positive (g\notin\{4,6\}) has (E(g)>c_6+1/250) | Restricted to positive single gaps; no multi-gap or finite-core extrapolation |
| Patch/IMS theory proves eventual failure | `proof_completion/08_residue_ims/FULL_PROOF.md`, T6.0--T6.2, T7.1--T7.3 | Analytic with certified G6 input | Explains eventual uninterrupted failure and proves the tail (n\geq240) | Does not claim that the mechanism alone places the onset at 48 |
| Continuous failure begins at 48 | `proof_completion/01_even_order_classification/FULL_PROOF.md`, T7.3, T8.4 | `COMPUTER_ASSISTED_PROVED` | Analytic tail plus exact finite bridge | The 96-order bridge is described by its mathematical role, not marketed as a data set |
| Finite proof architecture | component `COMPUTER_ASSISTED_BOUNDARY.md` files C.1--C.6 | `COMPUTER_ASSISTED_PROVED` | Reduction, finite exact object, independent verification, consequence | No JSON, hashes, test counts, hardware, or floating-point decision appears |
| Direct predecessor and novelty | `TASK58_DIRECT_LITERATURE_MATRIX.md`; `TASK58_NOVELTY_POSITIONING.md` | Verified literature audit dated 2026-08-24 | Complete resolution and disproof of Suvagiya's Conjecture 3 | Does not claim to introduce the problem, candidate, flux coordinates, or Fourier formula |

## Introduction-level exclusions

The Introduction contains no exact-(2r) refinement, moment argument,
bounded-period frontier, multi-gap classification, Grassmann-chart count,
certificate schema, hash, test count, internal claim identifier, or immutable
archive claim. The Wiley/JGT methodological analogues are used only to place
the proof architecture, not to support mathematical novelty.
