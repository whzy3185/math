import Mathlib

namespace TargetA

noncomputable def twistedSymbol (t : ℝ) : ℝ :=
  Real.cos t ^ 2 + Real.cos (2 * t) ^ 2

noncomputable def twistedBlock (t : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![2 * Real.cos t, 2 * Real.cos (2 * t);
     2 * Real.cos (2 * t), -2 * Real.cos t]

theorem twisted_block_symmetric (t : ℝ) :
    Matrix.transpose (twistedBlock t) = twistedBlock t := by
  ext i j
  fin_cases i <;> fin_cases j <;> rfl

theorem twisted_block_trace_zero (t : ℝ) :
    Matrix.trace (twistedBlock t) = 0 := by
  simp [twistedBlock, Matrix.trace]

theorem twisted_block_characteristic (t x : ℝ) :
    (x • (1 : Matrix (Fin 2) (Fin 2) ℝ) - twistedBlock t).det =
      x ^ 2 - 4 * twistedSymbol t := by
  simp [twistedBlock, twistedSymbol, Matrix.det_fin_two]
  ring

end TargetA
