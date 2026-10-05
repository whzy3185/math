# General analytic Hall bounds and the M6 census

This version centers the analytic theorem

χ_f(G)<3 ⇒ ρ(μ(G))≤3 and ρ(μ²(G))≤10/3

for every nonempty finite simple graph G. It includes analytic equality restrictions, an explicit29/10 fractional coloring applying the result to M6, the small exact lower-witness certificate, and the previously audited199-orbit census.

The general upper and equality proofs are analytic. The20-vertex witness independence number and the census remain explicitly identified finite checks. Earlier273-node and22-node branch certificates are preserved as verification history, but are no longer proof premises. Prior manuscript versions remain unchanged.

## Deliverables

- `mycielski_hall_v2.tex`: editable source
- `output/pdf/mycielski_hall_v2.pdf`: compiled PDF with Chinese abstract
- `chinese_abstract.md`: standalone Chinese abstract
- `SOURCECHECK.md`: bounded primary-source and overlap check

The proof and local witness artifacts are in the sibling `mycielski_k5_nine_profiles` package. The full census and its independent enumeration remain in `mycielski_strengthening`.

## Build

```
bash build.sh
```

Requires XeLaTeX, ordinary mathematical LaTeX packages, Latin Modern fonts, and Noto Serif CJK SC. The helper uses only a local fallback if the installed TeX format database is incomplete. No format files, caches, compiler logs or rendered page images are needed in publication.

The strict fractional hypothesis is a sufficient condition used by the proof, not a claimed necessary or optimal threshold. No publication-priority, general enumeration-improvement, proof-assistant or asymptotic-resolution claim is made.

## Local witness counts

The supplied witness table has190 states because `verify_witness.py` always branches on the least-labelled remaining vertex. The separate independent audit branches on a maximum-degree remaining vertex and visits328 memoized subproblems. These are different recursion trees for the same20-vertex graph; both give independence number6. The manuscript attributes190 only to the supplied table, not to both implementations.
