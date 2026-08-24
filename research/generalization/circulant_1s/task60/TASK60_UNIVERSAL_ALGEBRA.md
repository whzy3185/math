# Task 60 Universal-Algebra Audit

| Structure | `C_N(1,2)` | General `C_N(1,s)` | Status | Proof or obstruction |
|---|---|---|---|---|
| Hamilton gauge | yes | yes | PROVED | Step-one edges form a Hamilton cycle |
| Periodic chord word `tau` | yes | yes | PROVED | Use the quasiperiodic cover |
| Local flux `Q_i` | `tau_i tau_{i+1}` | same | PROVED | Four-cycle product |
| Two `tau` lifts | yes | yes when `product Q=1` | PROVED | First-order cyclic recurrence |
| Hamilton holonomy | `alpha` | `alpha` | PROVED | Product of step-one signs |
| `(Q,alpha)` complete | not without lift | not without lift | FALSIFIED AS STATED | Need `tau_0` or the full `tau` word |
| Finite-range `A^2` | range 4 | range `2s` before cyclic reduction | PROVED | Length-two path enumeration |
| `1+Q` cancellation | yes | yes | PROVED | Mixed coefficients factor universally |
| Alternating `Q=-1` word | even `N` | even `N` | PROVED | Cyclic lift parity |
| Period-eight low bulk | yes | unknown | OPEN | No general periodic optimization has been done |
| Translation sectors | four in the Task 59 bulk | unknown | OPEN | Depends on the discovered bulk |
| Gap coordinates | reference gap 4 | unknown | OPEN | Cannot precede bulk discovery |
| Phase-slip charge | `g-4` | unknown | OPEN | No general reference gap yet |
| Rank-two defect symmetry | yes for `G_6` | unknown | OPEN | The Task 59 anticommuting symmetry has not been generalized |

The maximal universal conclusion at Task 60.0 is the Hamilton-gauge algebra,
the flux lift, the full path-sum formula, and mixed-channel cancellation. The
period-eight and defect conclusions remain deliberately outside scope.

The missing lift bit is spectrally real in general. For `N=18,s=5,alpha=1`,
the words `tau=+1` and `tau=-1` have the same `Q=+1`, but their squared
operators satisfy `tr(H^3)=8676` and `6804`, respectively.
