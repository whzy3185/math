# Independent review of the version-3 attribution amendment

Date: 5 October 2026. **PASS** on the exact revised source and PDF below.

- Revised TeX SHA-256: `7d08c68d2f437496dfc6a3f3457b801cb1b7dbeb842c2cf85e7c9ba460875726`
- Revised PDF SHA-256: `ed4caa436b74d450f9fe15b1ed4457f16f5bf1c53a8e0313386f376c97d29611`
- Revised PDF: 15 pages, 381,797 bytes

The sole source change replaces the attribution sentence preceding Lemma 3.2 with:

> The six-vertex argument occurs in the proofs of Theorem 1 of [FRV] and Theorem 12 of [KN]; we recall its equality patterns.

This wording is appropriate. FRV's Theorem 1 begins on published page 199 and its proof gives the private-pair optional-edge restrictions, including the center-edge case. The same argument is corroborated in Fischermann's author thesis, Theorem 6.9, printed pages 77–78, and appears in Koch–Narayan's Theorem 12. The sentence credits the older local ingredient without changing the scope or provenance of the subsequent boundary theorems.

Sources inspected for this narrow attribution:

- [FRV published-paper reproduction](https://www.yumpu.com/en/document/view/9254319/maximum-graphs-with-a-unique-minimum-dominating-set)
- [Fischermann's official author thesis](https://publications.rwth-aachen.de/record/59635/files/Fischermann_Miranca.pdf)
- [Koch–Narayan, version 1](https://arxiv.org/pdf/2511.01719v1)

An independent literal source comparison confirms that replacing exactly this sentence in the frozen manuscript produces the revised source; no mathematical statement or proof changed. A byte comparison of every corresponding rendered page confirms that only page 4 differs. The other fourteen page images are identical to those of the fully reviewed prior version.

The revised page 4 was visually inspected. Both citations resolve to the correct bibliography entries, the new sentence is readable, and all following local lemmas and proofs retain their previous placement and content. The revised build log has no warnings, undefined references, missing characters or overfull/underfull boxes.

The frozen prior version remains unchanged:

- Prior TeX SHA-256: `3251481ac7c0567a3c6586c77618f35e809c6da45dd378a669e0885892166453`
- Prior PDF SHA-256: `0770d1fb9f1fcde75f645609b671b8ff05fc48b2f8f579eaff071f0fa5801039`

The full mathematical integration verdict in the separate `paper_v3_review` carries over with this checked provenance amendment. This review is confined to the amendment and does not assert exhaustive publication novelty.
