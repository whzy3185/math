# Independent review of the M6 positioning revision

Date: 5 October 2026. **PASS; no required revisions.** This review addresses the ten replacement files, their wording patch, the primary algorithm citation and the six-page PDF. It does not rerun the unchanged mathematical certificates or claim publication priority.

## Findings

- The title and abstract now foreground the exact Hall ratio and complete finite extremizer census. The abstract explicitly disclaims a general algorithmic efficiency improvement (`mycielski_hall_note.tex`, lines 24–44).
- The introduction distinguishes embedded-subset orbits from abstract induced-graph isomorphism types, and treats general identities as convenient lemmas with unresolved priority (lines 82–95).
- Remark 2.3 accurately cites S. Tsukiyama, M. Ide, H. Ariyoshi and I. Shirakawa, *A New Algorithm for Generating All the Maximal Independent Sets*, SIAM Journal on Computing 6(3) (1977), 505–517, DOI 10.1137/0206036. The primary publisher record was checked directly: https://epubs.siam.org/doi/10.1137/0206036 . It states total time O(N M K) and space O(N+M), with K the number of maximal independent sets.
- The edgeless-base comparison is correct. For n >= 1, the Mycielskian is n isolated originals plus K_(1,n). Every maximal independent set includes all originals and either the apex or all clones, so there are exactly two. Thus N=2n+1, M=n, K=2, and the standard bound is O(n²), whereas enumerating all base independent sets visits 2^n sets. The comparison concerns row generation, not Hall optimization or the extremizer census (lines 155–168).
- The rational branch-certificate verification claim is correctly conditional on a separately established complete constraint system and polynomial in the combined explicit input/certificate bit length. It makes no claim that completeness of an arbitrary supplied MIS list can be certified in that time (lines 230–236).
- The layer condition is accurately described as an exact membership criterion. The 109/83/7 orbit counts remain attributed to complete enumeration rather than a short structural derivation (lines 294–299).
- The Chinese abstract and supporting general-theorem, classification, README and literature-scope documents agree with these limits. No frozen mathematical data or programs are among the replacement targets.

## File and rendering checks

All ten replacement files match the SHA-256 values in `PATCH_MANIFEST.json`; independently recorded values are in `checked_files.json`. The complete textual patch was reviewed. All six existing rendered PDF pages were independently inspected, including the new remark, complexity paragraph and reference. They show no clipping, missing glyphs or unreadable mathematics.

TeX SHA-256: ba8147071aca816471953c4303bd1b0e73e7479c9937f15d53bee3d8a2b5edeb

PDF SHA-256: dca206766623db21bc8c39180f0bf53d986750c689d8c16993c4089d15ba9b02

This signoff approves the revised positioning within the reviewed scope. It is not a journal recommendation, external peer review or new novelty clearance.
