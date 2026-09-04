# Notation audit

| symbol | sole role | repair |
|---|---|---|
| `sigma` | graph signing | removed as dispersion branch index |
| `a_i` | step-one edge sign | replaces `s_i` to avoid the former centered-block collision |
| `b_i` | step-two edge sign | replaces `t_i`; twisted Fourier phase is `theta` |
| `tau` | Hamilton-gauge triangle word | removed as dispersion branch index |
| `Q` | local square/defect word | former matrix block `Q(xi)` renamed `V(xi)` |
| `epsilon, delta` | the two signs indexing the four squared branches | new exclusive role |
| `alpha` | Hamilton holonomy | never used as Bloch phase |
| `z` | cell Bloch phase | finite constraint always `z^L=alpha` |
| `theta` | scalar Fourier angle in the twisted block | replaces `t` |
| `h=xi+xi^{-1}` | scalar in the period-eight squared block | separate from edge signs `a_i,b_i` |
| `d,a,b` | defect count and distance-one/two pair counts | defined once before moments |

The rigidity statement now distinguishes a dihedral orbit of `Q` from the two
global-sign lifts `tau` and `-tau`.
