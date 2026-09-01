# Analytic Proof Red Team

## Scope

This review attacks only claims newly promoted during the analytic-first program. The existing computer-assisted classification remains backup evidence.

| Target | Attack | Result |
|---|---|---|
| period-eight family | wrong finite holonomy or use of an infinite-volume edge only | PASS: the finite Floquet theorem gives `rho(A_(8L,+1))^2=eta` for every `L`, not merely a limit. |
| period-eight family | failure at 32 hidden behind decimal comparison | PASS: `eta<1561/200<39973/5120<rho_-(32)^2`; the latter uses `cos x>1-x^2/2` and `pi^2<987/100`. |
| period-eight family | monotonicity starts outside the cosine monotonicity interval | PASS: both benchmark angles decrease from their values at `n=32` and remain in `[0,pi]`. |
| residue-specific IMS | last-failure values are merely copied metadata | PASS: `verify_target_a_task54_threshold.py` independently rebuilds every analytic upper/lower inequality through 246, the exact error formula, monotonicity, and the last-failure table. |
| bridge reduction | removed LDL rows are accidentally needed for a nonzero residue | PASS: the retained list is reconstructed as 6 residue-two, 15 residue-four, and 24 residue-six rows; no omitted original record is claimed analytic. |
| 34/36 rigidity | local language is presented as human analytic proof | REJECTED: it still depends on 13/14-bit exact local Rayleigh tables. It remains finite formal reconnaissance. |
| fourth-moment obstruction | trace formula ignores short-cycle collisions | PASS with scope `n>=9`; the independent test exhausts all lifts at `n=10,12`. The exceptional `n=8` is not included. |
| G6 scalar polynomial | `p(y)=0` is confused with physical matching | REJECTED: gap-2 and nonphysical branches prove that this implication is false. The wedge matching condition remains necessary. |
| complete classification | new analytic conclusions are used circularly | PASS: the promoted family and residue tails are direct witness theorems; they do not assume optimality/classification. |

## Verdict

The residue-zero theorem is safe to promote to `ANALYTIC_PROVED`. The residue-specific threshold compression is safe as an exact refinement of the existing IMS theorem. No equality theorem, nonzero-residue transfer theorem, or scalar global-G6 theorem is promoted by this review.
