# Structure Reference Audit

The following PDFs, not repository summaries, were read for theorem placement and proof organization. They are structural models only; a citation is owed only where their mathematics or historical framing is actually used.

| Paper | Main theorem timing | Theorem hierarchy and long-proof organization | Computation placement | Lesson for this paper |
|---|---|---|---|---|
| Lin--Ning (2021) | Conjecture and large-order theorem appear at the outset | structural reduction and Perron estimates settle `n>=17`; a separately marked finite regime closes all orders | small exceptional orders are part of the final theorem, not discovery narrative | state the all-even theorem immediately; prove tail and finite closure as distinct branches, then synthesize once |
| Hu--Liu (2025) | Theorems 1.1--1.3 are concentrated in the introduction | definitions lead to a general technical inequality, then Cayley/vertex-transitive applications and an extension | no computation substitutes for an implication | keep a three-level hierarchy: benchmark/formalism, G6 mechanism, all-even classification |
| Korotyaev--Saburova (2023) | Floquet setup precedes trace theorems and spectral consequences | periodic graph -> finite fibers -> exact trace identity -> band conclusions | symbolic/fiber calculation sits inside a theorem proof | introduce the reference bulk and its finite fiber before any defect calculation; derive, then use |
| Brunetti--Stanić (2022) | extremal quantities and principal results are introduced before technical sections | preliminaries and switching reductions precede separate spectral-radius and index classifications | equality cases are structural, not rhetorical | state the optimization domain and switching equivalence once, then keep the two-sided `rho` obligation visible |
| Goedgebeur--Schaudt (2018) | finite-classification claims follow an explicit generation theorem | reduction lemmas -> generator -> soundness/completeness theorem -> finite output -> classification | computation appears only after its coverage contract | the equality section must prove coverage, pruning soundness, closure, and terminal semantics before reporting certified output |

## Constraints extracted from the five papers

1. The all-even classification, not `G6`, is the main theorem and must appear in the first theorem block.
2. The G6 result is an independent mechanism theorem because it has its own exact statement, proof, and later use in the analytic tail.
3. The finite equality proof cannot be a log of enumeration. Its mathematical theorem is representative coverage plus exact terminal lower certificates.
4. The `n=32`, `n=40`, and `48<=n<240` witnesses are logically simpler than equality: each requires one certified signing, not universal search.
5. Neither the unresolved multi-gap program nor high-precision interaction exploration earns a main-line section.
