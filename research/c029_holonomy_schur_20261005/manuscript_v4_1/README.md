# Uniform spectral bounds for signed cycle squares with unequal cells

Revised research manuscript v4.1, 5 October 2026. The author line is blank.

[Read the 20-page manuscript](manuscript.pdf). Editable TeX and TikZ sources are in `manuscript.tex` and `sections/`; the bibliography is embedded in `manuscript.tex`. See [REPRODUCTION.md](REPRODUCTION.md) for the paper build and exact computational suite.

## Scope of this revision

This revision develops the exposition of the common unequal-cell boundary model and clarifies the older order-60 obstruction. The mathematical statements, proofs, and displayed formulas are unchanged from v3: 14 theorem/lemma/proposition/corollary statements, 14 proofs, and 100 displayed-mathematics blocks. The unrestricted minimum and its minimizing signings remain undetermined.

The raw supplement contains 14 Python source files for 13 producer/replay entry points, plus their runner and pinned SymPy requirement. The formal sources retain the frozen 237-declaration exact-radius checkpoint cited by the article. Later formal extensions are outside this manuscript publication. No fresh complete Lean build or axiom-audit pass is claimed for v4.1; a fresh replay attempt stopped with exit code 130 before those checks completed.

## Reproducibility

`PUBLICATION_INVENTORY.json` records file hashes, inherited source provenance, and the two previously disclosed source normalizations. `SHA256SUMS` checks all delivered files except itself. Copy this directory before executing the suite, because the programs generate certificates beside their source files.

The source supplement is self-contained. Byte-identical existing Git blobs are reused where available; no previous repository file is replaced. This deposit is a research draft and does not constitute a journal submission.
