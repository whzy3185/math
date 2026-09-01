# Residue-Two K-Reduction Comparison

The anticommuting operator `K` splits the residue-two family over `C` into
two `n/2` dimensional sectors and writes

```text
A=[0 B*; B 0].
```

This exactly explains the even multiplicity of `A^2` levels. It does not,
however, improve the all-length positivity propagation.

| route | propagated bulk object | coefficient field | boundary structure |
|---|---|---|---|
| real block Schur | symmetric `4 x 4` block, 10 independent entries | rational | fixed real boundary core |
| K-reduced | complex symmetric four-entry row block; study `B*B` | Gaussian rational | four nonzero long boundary links survive |

The checker reconstructs the `K` basis at two residue-two orders. The reduced
block is complex symmetric, has four generic nonzero entries per row, and
`B*B` retains exactly four cross-end links. Thus the dimension halves but the
propagation problem is not simplified to a real Jacobi/M-matrix recurrence.

Decision: retain the real block-Schur/Riccati route as the main analytic
route. The K-reduction remains a spectral-multiplicity lemma and is not used
as a second propagation program.
