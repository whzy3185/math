import Mathlib

namespace TargetA

noncomputable def period8Fiber (xi : ℂ) : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 1, 1, 0, 0, 0, xi⁻¹ ^ 2, xi⁻¹ ^ 2;
     1, 0, 1, 1, 0, 0, 0, -xi⁻¹ ^ 2;
     1, 1, 0, 1, -1, 0, 0, 0;
     0, 1, 1, 0, 1, 1, 0, 0;
     0, 0, -1, 1, 0, 1, -1, 0;
     0, 0, 0, 1, 1, 0, 1, -1;
     xi ^ 2, 0, 0, 0, -1, 1, 0, 1;
     xi ^ 2, -xi ^ 2, 0, 0, 0, -1, 1, 0]

noncomputable def period8ChiralInvolution (xi : ℂ) : Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 0, 0, 0, xi⁻¹, 0, 0, 0;
     0, 0, 0, 0, 0, -xi⁻¹, 0, 0;
     0, 0, 0, 0, 0, 0, xi⁻¹, 0;
     0, 0, 0, 0, 0, 0, 0, -xi⁻¹;
     xi, 0, 0, 0, 0, 0, 0, 0;
     0, -xi, 0, 0, 0, 0, 0, 0;
     0, 0, xi, 0, 0, 0, 0, 0;
     0, 0, 0, -xi, 0, 0, 0, 0]

set_option maxHeartbeats 1000000 in
theorem period8_chiral_square {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralInvolution xi * period8ChiralInvolution xi =
      (1 : Matrix (Fin 8) (Fin 8) ℂ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ChiralInvolution, hxi]

set_option maxHeartbeats 1000000 in
theorem period8_chiral_anticommutes {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralInvolution xi * period8Fiber xi +
      period8Fiber xi * period8ChiralInvolution xi =
        0 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ChiralInvolution, period8Fiber]
  all_goals field_simp [hxi] <;> ring

theorem period8_chiral_maps_plus_to_minus {xi : ℂ} (hxi : xi ≠ 0)
    (v : Fin 8 → ℂ)
    (hv : (period8ChiralInvolution xi).mulVec v = v) :
    (period8ChiralInvolution xi).mulVec ((period8Fiber xi).mulVec v) =
      -((period8Fiber xi).mulVec v) := by
  let J := period8ChiralInvolution xi
  let H := period8Fiber xi
  have hjh : J * H = -(H * J) := by
    exact eq_neg_iff_add_eq_zero.mpr (period8_chiral_anticommutes hxi)
  calc
    J.mulVec (H.mulVec v) = (J * H).mulVec v :=
      Matrix.mulVec_mulVec v J H
    _ = (-(H * J)).mulVec v := by rw [hjh]
    _ = -(H * J).mulVec v := Matrix.neg_mulVec v (H * J)
    _ = -H.mulVec (J.mulVec v) := by
      rw [Matrix.mulVec_mulVec]
    _ = -H.mulVec v := by rw [hv]

noncomputable def period8ChiralBasis (xi : ℂ) : Matrix (Fin 8) (Fin 8) ℂ :=
  !![1, 0, 0, 0, 1, 0, 0, 0;
     0, 1, 0, 0, 0, 1, 0, 0;
     0, 0, 1, 0, 0, 0, 1, 0;
     0, 0, 0, 1, 0, 0, 0, 1;
     xi, 0, 0, 0, -xi, 0, 0, 0;
     0, -xi, 0, 0, 0, xi, 0, 0;
     0, 0, xi, 0, 0, 0, -xi, 0;
     0, 0, 0, -xi, 0, 0, 0, xi]

noncomputable def period8ChiralCoordinateMatrix (xi : ℂ) :
    Matrix (Fin 8) (Fin 8) ℂ :=
  !![0, 0, 0, 0, 0, 1, 1 - xi⁻¹, xi⁻¹;
     0, 0, 0, 0, 1, 0, 1, 1 - xi⁻¹;
     0, 0, 0, 0, xi + 1, 1, 0, 1;
     0, 0, 0, 0, -xi, xi + 1, 1, 0;
     0, 1, 1 + xi⁻¹, -xi⁻¹, 0, 0, 0, 0;
     1, 0, 1, 1 + xi⁻¹, 0, 0, 0, 0;
     1 - xi, 1, 0, 1, 0, 0, 0, 0;
     xi, 1 - xi, 1, 0, 0, 0, 0, 0]

theorem period8_xi_mul_inv_sq {xi : ℂ} (hxi : xi ≠ 0) :
    xi * xi⁻¹ ^ 2 = xi⁻¹ := by
  calc
    xi * xi⁻¹ ^ 2 = (xi * xi⁻¹) * xi⁻¹ := by ring
    _ = xi⁻¹ := by simp [hxi]

theorem period8_inv_sq_mul_xi {xi : ℂ} (hxi : xi ≠ 0) :
    (xi ^ 2)⁻¹ * xi = xi⁻¹ := by
  rw [← inv_pow]
  calc
    xi⁻¹ ^ 2 * xi = xi⁻¹ * (xi⁻¹ * xi) := by ring
    _ = xi⁻¹ := by simp [hxi]

theorem period8_xi_mul_inv {xi : ℂ} (hxi : xi ≠ 0) :
    xi * xi⁻¹ = 1 := by
  exact mul_inv_cancel₀ hxi

set_option maxHeartbeats 1500000 in
theorem period8_fiber_in_chiral_basis {xi : ℂ} (hxi : xi ≠ 0) :
    period8Fiber xi * period8ChiralBasis xi =
      period8ChiralBasis xi * period8ChiralCoordinateMatrix xi := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8Fiber, period8ChiralBasis, period8ChiralCoordinateMatrix,
      period8_inv_sq_mul_xi hxi, hxi]
  all_goals try ring
  all_goals try linear_combination period8_xi_mul_inv hxi
  all_goals linear_combination -(period8_xi_mul_inv hxi)

end TargetA
