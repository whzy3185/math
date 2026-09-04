# Access and full-text map

The library stores no duplicate PDF merely to create a new directory tree.
Existing lawful local copies remain in `research/related_work/papers/`; the
master index points to them.  Missing local copies are represented by stable
publisher, institutional, or arXiv sources rather than placeholder files.

## Manuscript core

| key | local full text | authoritative metadata / full text |
|---|---|---|
| `Harary1953` | not duplicated | https://doi.org/10.1307/mmj/1028989917 |
| `Zaslavsky1982` | not duplicated | https://doi.org/10.1016/0166-218X(82)90033-6 |
| `BelardoEtAl2018` | `research/related_work/papers/core/2018_Belardo_OpenProblemsSignedGraphs.pdf` | https://doi.org/10.26493/2590-9770.1286.d7b |
| `BiluLinial2006` | `research/related_work/papers/historical/2006_BiluLinial_LiftsDiscrepancy.pdf` | https://doi.org/10.1007/s00493-006-0029-7 |
| `MarcusSpielmanSrivastava2015` | `research/related_work/papers/historical/2015_Marcus_InterlacingFamiliesI.pdf` | https://doi.org/10.4007/annals.2015.182.1.7 |
| `Reff2012` | not duplicated | https://doi.org/10.1016/j.laa.2011.10.021; https://arxiv.org/abs/1110.4554 |
| `KorotyaevSaburova2017` | not duplicated | https://doi.org/10.1016/j.jfa.2016.12.015 |
| `KorotyaevSaburova2023` | `research/related_work/papers/methods/2023_Korotyaev_TraceFormulasPeriodicMagneticGraphs.pdf` | https://doi.org/10.1016/j.laa.2023.07.025 |
| `Davis1979` | book not stored | ISBN 9780471057710; WorldCat OCLC 4804321 |
| `BrunettiStanic2022` | `research/related_work/papers/core/2022_Brunetti_UnbalancedSignedGraphsExtremal.pdf` | https://doi.org/10.1007/s40314-022-01814-5 |
| `GhorbaniMajidi2024` | structured source note only | https://doi.org/10.1016/j.disc.2023.113860 |
| `HuLiu2025` | `research/related_work/papers/core/2025_Hu_VertexIsoperimetrySignedCayley.pdf` | https://doi.org/10.1016/j.ejc.2025.104200 |
| `AtayHua2016` | not duplicated | https://doi.org/10.1016/j.laa.2016.01.027; https://arxiv.org/abs/1411.6113 |
| `CedzichEtAl2021` | not duplicated | https://doi.org/10.1007/s00023-020-00982-6; https://arxiv.org/abs/2006.04634 |
| `Suvagiya2026` | `research/related_work/papers/core/2026_Suvagiya_SignedCirculants_PREPRINT.pdf` | https://arxiv.org/abs/2607.18334 |

## JGT structure corpus

Full-text sources used in the completed structure audit:

| ID | access route |
|---|---|
| `J001` | https://arxiv.org/abs/2304.06942 |
| `J002` | institutional author manuscript: University of Amsterdam repository; DOI `10.1002/jgt.23071` |
| `J003` | Ghent University accepted manuscript; DOI `10.1002/jgt.23057` |
| `J004` | author PDF at University of Denver; DOI `10.1002/jgt.23176` |
| `J005` | https://arxiv.org/abs/2210.07139 |
| `J006` | Wiley open-access full HTML; DOI `10.1002/jgt.23218` |
| `J007` | https://arxiv.org/abs/2402.11758 |
| `J008` | https://arxiv.org/abs/2406.13176 |
| `J009` | https://arxiv.org/abs/2409.15918 |
| `J010` | https://arxiv.org/abs/2405.06755 |

These PDFs were read from temporary audit storage and are not committed as a
second corpus.  Their extracted structural conclusions are preserved in
`../JGT_RECENT_STRUCTURE_AUDIT.md`.

## Access labels

- `local PDF`: a lawful source is present and may be read offline.
- `source note`: metadata/abstract and access information are stored; no claim
  of full-text possession is made.
- `not duplicated`: a stable external source exists, but a local copy is not
  required for the current claim.
- `preprint`: version status must remain visible wherever cited.
