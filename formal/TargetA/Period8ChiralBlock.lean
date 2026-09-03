import Mathlib
import TargetA.Period8Polynomial

namespace TargetA

noncomputable def period8Q (xi : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1 + xi⁻¹, 2;
     2, 1 - xi⁻¹]

noncomputable def period8R (xi : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  !![1 + xi, 2;
     2, 1 - xi]

noncomputable def period8SquaredChiralBlock (xi : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![4 - (xi + xi⁻¹), 0, 1 + xi⁻¹, 2;
     0, 4 - (xi + xi⁻¹), 2, 1 - xi⁻¹;
     1 + xi, 2, 4 + (xi + xi⁻¹), 0;
     2, 1 - xi, 0, 4 + (xi + xi⁻¹)]

noncomputable def period8PositiveToNegative (xi : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![0, 1, 1 - xi⁻¹, xi⁻¹;
     1, 0, 1, 1 - xi⁻¹;
     xi + 1, 1, 0, 1;
     -xi, xi + 1, 1, 0]

noncomputable def period8NegativeToPositive (xi : ℝ) : Matrix (Fin 4) (Fin 4) ℝ :=
  !![0, 1, 1 + xi⁻¹, -xi⁻¹;
     1, 0, 1, 1 + xi⁻¹;
     1 - xi, 1, 0, 1;
     xi, 1 - xi, 1, 0]

set_option maxHeartbeats 1500000 in
theorem period8_squared_chiral_block {xi : ℝ} (hxi : xi ≠ 0) :
    period8PositiveToNegative xi * period8NegativeToPositive xi =
      period8SquaredChiralBlock xi := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8PositiveToNegative, period8NegativeToPositive,
      period8SquaredChiralBlock, hxi]
  all_goals field_simp [hxi] <;> ring

noncomputable def period8ChiralDeterminant (y xi : ℝ) : ℝ :=
  let s := xi + xi⁻¹
  let scalar := (y - 4)^2 - s^2
  (scalar • (1 : Matrix (Fin 2) (Fin 2) ℝ) - period8R xi * period8Q xi).det

theorem period8_chiral_determinant {y xi : ℝ} (hxi : xi ≠ 0) :
    period8ChiralDeterminant y xi =
      period8Polynomial y (xi^2 + xi⁻¹^2) := by
  simp [period8ChiralDeterminant, period8Q, period8R, period8Polynomial,
    Matrix.det_fin_two]
  field_simp
  ring

end TargetA
