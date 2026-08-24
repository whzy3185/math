# Dependencies

## Mathematical dependency graph

```text
signed Hamilton gauge
  -> canonical period-eight triangle word
  -> Bloch decomposition
  -> exact polynomial P(y,c)
  -> positive expansion at (eta,2)
  -> unique global squared band edge eta
  -> identification of gap four as zero charge.
```

The nodes in this graph are mathematical objects, not research-task labels.

## Imported facts

- Switching preserves the spectrum of a signed adjacency matrix.
- A periodic finite-range self-adjoint operator admits the elementary Bloch
  decomposition used in the proof.
- Eigenvalues of a Hermitian matrix depend continuously on its entries.

All three facts are standard and are also proved or instantiated directly in
the frozen reference manuscript.

## Exact provenance

- Canonical gauge and flux convention:
  `research/paper/manuscript_tex_pub/sections/03_preliminaries.tex`.
- Fiber matrix and determinant:
  `research/paper/manuscript_tex_pub/sections/05_periodic_floquet.tex`.
- Exact edge and positive identity:
  `research/paper/manuscript_tex_pub/sections/06_period8_spectral_edge.tex`.
- Independent arithmetic audit:
  `research/audit/period8_floquet_independent_audit.json`.

These paths record provenance only. The proof in this package is
self-contained.

## Downstream use

The reference phase supplies the bulk sectors, the zero-charge gap `g=4`,
the essential edge `eta`, and the strict inequality `eta<c6` used in the G6
and single-gap packages.
