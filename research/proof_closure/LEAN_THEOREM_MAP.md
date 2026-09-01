# Lean Theorem Map

No Lean declaration is claimed until it compiles in a pinned Lean/mathlib project. This map freezes only the intended statement/dependency interface.

| Human result | Planned declaration | Planned file | Dependencies | Formal status |
|---|---|---|---|---|
| switching conjugacy | `switching_spectrum` | `TargetA/Switching.lean` | finite matrices, diagonal signs | FORMALIZATION_OPEN |
| twisted Fourier block | `twisted_spectrum` | `TargetA/Twisted.lean` | cyclic shift/Fourier API | FORMALIZATION_OPEN |
| phase-slip endpoint charge | `gap_charge_additive` | `TargetA/PhaseSlip.lean` | finite words, `ZMod 4` | FORMALIZATION_OPEN |
| fourth moment | `trace_fourth_eq` | `TargetA/Equality.lean` | finite sums/matrices | FORMALIZATION_OPEN |
| period-eight residue-zero failure | `periodEight_failure_of_dvd_eight` | `TargetA/Failure.lean` | Floquet theorem, cosine inequalities | FORMALIZATION_OPEN |
| G6 algebraic interval | `g6_root_isolated` | `TargetA/G6.lean` | polynomials, Sturm certificate verifier | FORMALIZATION_OPEN |
| discrete IMS | `ims_identity` | `TargetA/IMS.lean` | finite-range matrices and partitions | FORMALIZATION_OPEN |
| complete classification | `completeClassification` | `TargetA/Classification.lean` | all prior modules plus unavoidable finite certificates | FORMALIZATION_OPEN |

The final declaration must not introduce an axiom equivalent to the classification. Any residual finite enumeration, if retained, will have the explicit status `FINITE_FORMAL_PROVED`, not `ANALYTIC_PROVED`.
