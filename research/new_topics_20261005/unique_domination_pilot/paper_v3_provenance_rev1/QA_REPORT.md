# Third-version quality assurance

5 October2026. The final source compiles with two pdfLaTeX passes, without warnings, undefined references or citations, overfull boxes, or underfull boxes. PDF bookmarks have plain-text section titles where needed.

The final PDF has15 A4 pages,25mm margins and11-point text. The supplementary checks were consolidated so that the bibliography shares the final page rather than occupying a mostly empty additional page. The private-neighbour lemma is kept with the beginning of its proof.

All15 final pages were rendered at1550pixels on their long edge and individually inspected. The theorem statements, exception table, stability estimates, sorted degree groups, normalized-distance limit and bibliography are legible, with no clipping, overlap or missing glyphs. The final review status and exact PDF/source hashes are recorded in PAPER_MANIFEST.json.

## Scope and mathematical alignment

- γ≥2 is explicit in the abstract, graph class and stability theorem
- The broader isolate-free class, without connectedness, is explicitly supported by the independent upper-proof audit
- Every extremal graph and lower-bound construction is connected
- The second-boundary3/1/2 counts refer to full graph-isomorphism classes; the two eight-vertex exceptions are defined and proved
- Edit distance is minimized over all vertex bijections, without a bipartition-preservation requirement
- t=0 is handled by the equality theorem; t≥1 uses the audited repair argument
- The finite trivial bound is included alongside12γt
- The obstruction deletes the residual incidence at the same private vertex whose column edges were removed
- The degree lower bound holds under arbitrary relabelling; the1/72 limit uses normalization by the actual vertex count squared
- The finite summary distinguishes164 candidates from20 survivors
- Existing source attribution is retained; no exhaustive novelty, Lean verification or journal-review claim is added

The individual mathematical components have independent audit PASS. The final integrated manuscript review and final three-page layout reconciliation also passed; see audit/INTEGRATION_REVIEW.md. The final PDF/source hashes are frozen in the manifest. Pages1–12 are render-identical to the initial integrated PASS version; the final pages13–15 were inspected again after keeping the uncrossing inequality together.

## Narrow provenance revision

Only the attribution sentence for the six-vertex estimate changed. The revised15-page document compiles without warnings or box errors. Pixel-file hashes show page4 is the only changed rendered page; the other14 pages are byte-identical to the reviewed frozen version. Page4 was visually inspected and has no layout issue. SOURCE_DIFF.patch and CHANGE_COMPARISON.json record the exact scope and old/new hashes. The targeted independent attribution and layout review passed; see audit/. The frozen predecessor is unchanged.
