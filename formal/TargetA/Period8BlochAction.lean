import TargetA.FiniteBloch
import TargetA.Period8Fiber

namespace TargetA

/-!
The three cell matrices below isolate the zero, positive, and negative cell
translations in the period-eight Hamiltonian.  Their exact sum is the fibre
symbol already used in the chiral calculation.
-/

noncomputable def period8IntraCell : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 1, 1, 0, 0, 0, 0, 0;
     1, 0, 1, 1, 0, 0, 0, 0;
     1, 1, 0, 1, -1, 0, 0, 0;
     0, 1, 1, 0, 1, 1, 0, 0;
     0, 0, -1, 1, 0, 1, -1, 0;
     0, 0, 0, 1, 1, 0, 1, -1;
     0, 0, 0, 0, -1, 1, 0, 1;
     0, 0, 0, 0, 0, -1, 1, 0]

noncomputable def period8ForwardCell : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     1, 0, 0, 0, 0, 0, 0, 0;
     1, -1, 0, 0, 0, 0, 0, 0]

noncomputable def period8BackwardCell : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 0, 0, 0, 0, 0, 1, 1;
     0, 0, 0, 0, 0, 0, 0, -1;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0;
     0, 0, 0, 0, 0, 0, 0, 0]

set_option maxHeartbeats 1500000 in
theorem period8_fiber_as_cell_symbol (xi : ℂ) :
    period8Fiber xi = period8IntraCell +
      (xi^2) • period8ForwardCell + (xi⁻¹^2) • period8BackwardCell := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8Fiber, period8IntraCell, period8ForwardCell,
      period8BackwardCell]

end TargetA
