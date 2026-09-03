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

noncomputable def period8ChiralBasisInverse (xi : ℂ) : Matrix (Fin 8) (Fin 8) ℂ :=
  !![(2 : ℂ)⁻¹, 0, 0, 0, (2 * xi)⁻¹, 0, 0, 0;
     0, (2 : ℂ)⁻¹, 0, 0, 0, -(2 * xi)⁻¹, 0, 0;
     0, 0, (2 : ℂ)⁻¹, 0, 0, 0, (2 * xi)⁻¹, 0;
     0, 0, 0, (2 : ℂ)⁻¹, 0, 0, 0, -(2 * xi)⁻¹;
     (2 : ℂ)⁻¹, 0, 0, 0, -(2 * xi)⁻¹, 0, 0, 0;
     0, (2 : ℂ)⁻¹, 0, 0, 0, (2 * xi)⁻¹, 0, 0;
     0, 0, (2 : ℂ)⁻¹, 0, 0, 0, -(2 * xi)⁻¹, 0;
     0, 0, 0, (2 : ℂ)⁻¹, 0, 0, 0, (2 * xi)⁻¹]

set_option maxHeartbeats 1500000 in
theorem period8_chiral_basis_left_inverse {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralBasisInverse xi * period8ChiralBasis xi =
      (1 : Matrix (Fin 8) (Fin 8) ℂ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ChiralBasisInverse, period8ChiralBasis, hxi]
  all_goals field_simp [hxi] <;> ring

set_option maxHeartbeats 1500000 in
theorem period8_chiral_basis_right_inverse {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralBasis xi * period8ChiralBasisInverse xi =
      (1 : Matrix (Fin 8) (Fin 8) ℂ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ChiralBasisInverse, period8ChiralBasis, hxi]
  all_goals field_simp [hxi] <;> ring

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

theorem period8_fiber_similar_to_chiral_coordinates {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralBasisInverse xi * period8Fiber xi * period8ChiralBasis xi =
      period8ChiralCoordinateMatrix xi := by
  calc
    period8ChiralBasisInverse xi * period8Fiber xi * period8ChiralBasis xi =
        period8ChiralBasisInverse xi *
          (period8Fiber xi * period8ChiralBasis xi) := by
            rw [Matrix.mul_assoc]
    _ = period8ChiralBasisInverse xi *
          (period8ChiralBasis xi * period8ChiralCoordinateMatrix xi) := by
            rw [period8_fiber_in_chiral_basis hxi]
    _ = (period8ChiralBasisInverse xi * period8ChiralBasis xi) *
          period8ChiralCoordinateMatrix xi := by
            rw [← Matrix.mul_assoc]
    _ = period8ChiralCoordinateMatrix xi := by
            rw [period8_chiral_basis_left_inverse hxi, Matrix.one_mul]

noncomputable def period8ComplexPositiveToNegative (xi : ℂ) :
    Matrix (Fin 4) (Fin 4) ℂ :=
  !![0, 1, 1 - xi⁻¹, xi⁻¹;
     1, 0, 1, 1 - xi⁻¹;
     xi + 1, 1, 0, 1;
     -xi, xi + 1, 1, 0]

noncomputable def period8ComplexNegativeToPositive (xi : ℂ) :
    Matrix (Fin 4) (Fin 4) ℂ :=
  !![0, 1, 1 + xi⁻¹, -xi⁻¹;
     1, 0, 1, 1 + xi⁻¹;
     1 - xi, 1, 0, 1;
     xi, 1 - xi, 1, 0]

noncomputable def period8ComplexSquaredBlock (xi : ℂ) :
    Matrix (Fin 4) (Fin 4) ℂ :=
  !![4 - (xi + xi⁻¹), 0, 1 + xi⁻¹, 2;
     0, 4 - (xi + xi⁻¹), 2, 1 - xi⁻¹;
     1 + xi, 2, 4 + (xi + xi⁻¹), 0;
     2, 1 - xi, 0, 4 + (xi + xi⁻¹)]

set_option maxHeartbeats 1500000 in
theorem period8_complex_squared_block {xi : ℂ} (hxi : xi ≠ 0) :
    period8ComplexPositiveToNegative xi * period8ComplexNegativeToPositive xi =
      period8ComplexSquaredBlock xi := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ComplexPositiveToNegative, period8ComplexNegativeToPositive,
      period8ComplexSquaredBlock, hxi]
  all_goals field_simp [hxi] <;> ring

noncomputable def period8FiberPolynomialC (y c : ℂ) : ℂ :=
  y^4 - 16 * y^3 + (80 - 2 * c) * y^2 + (-128 + 16 * c) * y +
    c^2 - 13 * c + 38

set_option maxHeartbeats 4000000 in
theorem period8_complex_squared_block_annihilated {xi : ℂ} (hxi : xi ≠ 0) :
    let S := period8ComplexSquaredBlock xi
    let c := xi^2 + xi⁻¹^2
    S^4 - (16 : ℂ) • S^3 + (80 - 2 * c) • S^2 +
      (-128 + 16 * c) • S + (c^2 - 13 * c + 38) • 1 = 0 := by
  dsimp
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8ComplexSquaredBlock, pow_succ]
  all_goals field_simp [hxi] <;> ring

theorem period8_complex_matrix_power_on_eigenvector
    {S : Matrix (Fin 4) (Fin 4) ℂ}
    {y : ℂ} {v : Fin 4 → ℂ} (hv : S.mulVec v = y • v) :
    ∀ k : ℕ, (S^k).mulVec v = y^k • v
  | 0 => by simp
  | k + 1 => by
      rw [pow_succ, ← Matrix.mulVec_mulVec, hv, Matrix.mulVec_smul,
        period8_complex_matrix_power_on_eigenvector hv k]
      simp [pow_succ, smul_smul, mul_comm]

theorem period8_complex_squared_block_eigen_root {xi y : ℂ}
    (hxi : xi ≠ 0) (v : Fin 4 → ℂ)
    (hv : (period8ComplexSquaredBlock xi).mulVec v = y • v)
    (hv_ne : v ≠ 0) :
    period8FiberPolynomialC y (xi^2 + xi⁻¹^2) = 0 := by
  let S := period8ComplexSquaredBlock xi
  let c := xi^2 + xi⁻¹^2
  have hannih :
      S^4 - (16 : ℂ) • S^3 + (80 - 2 * c) • S^2 +
        (-128 + 16 * c) • S + (c^2 - 13 * c + 38) • 1 = 0 := by
    simpa [S, c] using period8_complex_squared_block_annihilated (xi := xi) hxi
  have hvS : S.mulVec v = y • v := by
    simpa [S] using hv
  have hpow :=
    period8_complex_matrix_power_on_eigenvector (S := S) (y := y) (v := v) hv
  have hvector :=
    congrArg (fun M : Matrix (Fin 4) (Fin 4) ℂ => M.mulVec v) hannih
  simp only [Matrix.add_mulVec, Matrix.sub_mulVec, Matrix.smul_mulVec,
    Matrix.zero_mulVec, Matrix.one_mulVec] at hvector
  rw [hpow 4, hpow 3, hpow 2, hvS] at hvector
  by_contra hroot
  apply hv_ne
  funext i
  have hentry := congrFun hvector i
  simp only [smul_eq_mul, Pi.add_apply, Pi.sub_apply, Pi.smul_apply,
    Pi.zero_apply] at hentry
  have hfactor : period8FiberPolynomialC y c * v i = 0 := by
    calc
      period8FiberPolynomialC y c * v i =
          y^4 * v i - 16 * (y^3 * v i) +
            (80 - 2 * c) * (y^2 * v i) +
            (-128 + 16 * c) * (y * v i) +
            (c^2 - 13 * c + 38) * v i := by
              simp [period8FiberPolynomialC]
              ring
      _ = 0 := hentry
  exact (mul_eq_zero.mp hfactor).resolve_left hroot

def period8TopEmbed (v : Fin 4 → ℂ) : Fin 8 → ℂ :=
  ![v 0, v 1, v 2, v 3, 0, 0, 0, 0]

def period8BottomEmbed (v : Fin 4 → ℂ) : Fin 8 → ℂ :=
  ![0, 0, 0, 0, v 0, v 1, v 2, v 3]

set_option maxHeartbeats 1500000 in
theorem period8_chiral_top_action (xi : ℂ) (v : Fin 4 → ℂ) :
    (period8ChiralCoordinateMatrix xi).mulVec (period8TopEmbed v) =
      period8BottomEmbed ((period8ComplexNegativeToPositive xi).mulVec v) := by
  ext i
  fin_cases i <;>
    simp [period8ChiralCoordinateMatrix, period8TopEmbed, period8BottomEmbed,
      period8ComplexNegativeToPositive, Matrix.mulVec, Matrix.vecHead,
      Matrix.vecTail]

set_option maxHeartbeats 1500000 in
theorem period8_chiral_bottom_action (xi : ℂ) (v : Fin 4 → ℂ) :
    (period8ChiralCoordinateMatrix xi).mulVec (period8BottomEmbed v) =
      period8TopEmbed ((period8ComplexPositiveToNegative xi).mulVec v) := by
  ext i
  fin_cases i <;>
    simp [period8ChiralCoordinateMatrix, period8TopEmbed, period8BottomEmbed,
      period8ComplexPositiveToNegative, Matrix.mulVec, Matrix.vecHead,
      Matrix.vecTail]

end TargetA
