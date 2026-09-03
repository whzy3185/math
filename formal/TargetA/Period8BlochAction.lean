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

noncomputable def period8CellTranslation {L : ℕ} (a : ZMod L)
    (F : ZMod L → Fin 8 → ℂ) : ZMod L → Fin 8 → ℂ :=
  fun m => F (a + m)

noncomputable def period8CellDFT {L : ℕ} [NeZero L]
    (F : ZMod L → Fin 8 → ℂ) (k : ZMod L) : Fin 8 → ℂ :=
  ZMod.dft F k

theorem period8_cell_dft_translation {L : ℕ} [NeZero L]
    (a k : ZMod L) (F : ZMod L → Fin 8 → ℂ) :
    period8CellDFT (period8CellTranslation a F) k =
      ZMod.stdAddChar (a * k) • period8CellDFT F k := by
  ext r
  simp only [period8CellDFT, period8CellTranslation, ZMod.dft_apply,
    Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
  exact dft_cellTranslation a k (fun m => F m r)

end TargetA
