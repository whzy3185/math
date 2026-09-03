import Mathlib
import TargetA.Period8Polynomial

namespace TargetA

noncomputable def period8PolynomialC (y c : ℂ) : ℂ :=
  y^4 - 16 * y^3 + (80 - 2 * c) * y^2 + (-128 + 16 * c) * y +
    c^2 - 13 * c + 38

noncomputable def period8QC (xi : ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![1 + xi⁻¹, 2;
     2, 1 - xi⁻¹]

noncomputable def period8RC (xi : ℂ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![1 + xi, 2;
     2, 1 - xi]

noncomputable def period8ChiralDeterminantC (y xi : ℂ) : ℂ :=
  let s := xi + xi⁻¹
  let scalar := (y - 4)^2 - s^2
  (scalar • (1 : Matrix (Fin 2) (Fin 2) ℂ) - period8RC xi * period8QC xi).det

theorem period8_chiral_determinant_complex {y xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralDeterminantC y xi =
      period8PolynomialC y (xi^2 + xi⁻¹^2) := by
  simp [period8ChiralDeterminantC, period8QC, period8RC,
    period8PolynomialC, Matrix.det_fin_two]
  field_simp
  ring

theorem period8_unit_conj_eq_inv {xi : ℂ}
    (hunit : xi * (starRingEnd ℂ) xi = 1) :
    (starRingEnd ℂ) xi = xi⁻¹ := by
  have hxi : xi ≠ 0 := by
    intro hz
    simp [hz] at hunit
  field_simp [hxi]
  exact mul_comm xi _ ▸ hunit

theorem period8_unit_parameter_real {xi : ℂ}
    (hunit : xi * (starRingEnd ℂ) xi = 1) :
    (starRingEnd ℂ) (xi^2 + xi⁻¹^2) = xi^2 + xi⁻¹^2 := by
  have hconj := period8_unit_conj_eq_inv hunit
  simp [map_add, map_pow, hconj]
  ring

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
