import Mathlib
import TargetA.Period8ChiralBlock

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

def period8TopProject (w : Fin 8 → ℂ) : Fin 4 → ℂ :=
  ![w 0, w 1, w 2, w 3]

def period8BottomProject (w : Fin 8 → ℂ) : Fin 4 → ℂ :=
  ![w 4, w 5, w 6, w 7]

theorem period8_top_project_embed (v : Fin 4 → ℂ) :
    period8TopProject (period8TopEmbed v) = v := by
  funext i
  fin_cases i <;> simp [period8TopProject, period8TopEmbed, Matrix.vecHead,
    Matrix.vecTail]

theorem period8_bottom_project_embed (v : Fin 4 → ℂ) :
    period8BottomProject (period8BottomEmbed v) = v := by
  funext i
  fin_cases i <;> simp [period8BottomProject, period8BottomEmbed, Matrix.vecHead,
    Matrix.vecTail]

theorem period8_top_project_bottom_embed (v : Fin 4 → ℂ) :
    period8TopProject (period8BottomEmbed v) = 0 := by
  funext i
  fin_cases i <;> simp [period8TopProject, period8BottomEmbed, Matrix.vecHead,
    Matrix.vecTail]

theorem period8_bottom_project_top_embed (v : Fin 4 → ℂ) :
    period8BottomProject (period8TopEmbed v) = 0 := by
  funext i
  fin_cases i <;> simp [period8BottomProject, period8TopEmbed, Matrix.vecHead,
    Matrix.vecTail]

theorem period8_embed_project_reconstruct (w : Fin 8 → ℂ) :
    period8TopEmbed (period8TopProject w) +
      period8BottomEmbed (period8BottomProject w) = w := by
  funext i
  fin_cases i <;> simp [period8TopEmbed, period8BottomEmbed,
    period8TopProject, period8BottomProject, Matrix.vecHead, Matrix.vecTail]

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

theorem period8_chiral_coordinate_action (xi : ℂ) (w : Fin 8 → ℂ) :
    (period8ChiralCoordinateMatrix xi).mulVec w =
      period8TopEmbed
        ((period8ComplexPositiveToNegative xi).mulVec (period8BottomProject w)) +
      period8BottomEmbed
        ((period8ComplexNegativeToPositive xi).mulVec (period8TopProject w)) := by
  ext i
  fin_cases i <;>
    simp [period8ChiralCoordinateMatrix, period8TopEmbed, period8BottomEmbed,
      period8TopProject, period8BottomProject, period8ComplexPositiveToNegative,
      period8ComplexNegativeToPositive, Matrix.mulVec, Matrix.vecHead,
      Matrix.vecTail]

theorem period8_chiral_top_equation {xi lambda : ℂ} {w : Fin 8 → ℂ}
    (hEig : (period8ChiralCoordinateMatrix xi).mulVec w = lambda • w) :
    (period8ComplexPositiveToNegative xi).mulVec (period8BottomProject w) =
      lambda • period8TopProject w := by
  funext i
  fin_cases i
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexPositiveToNegative, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (0 : Fin 8)
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexPositiveToNegative, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (1 : Fin 8)
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexPositiveToNegative, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (2 : Fin 8)
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexPositiveToNegative, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (3 : Fin 8)

theorem period8_chiral_bottom_equation {xi lambda : ℂ} {w : Fin 8 → ℂ}
    (hEig : (period8ChiralCoordinateMatrix xi).mulVec w = lambda • w) :
    (period8ComplexNegativeToPositive xi).mulVec (period8TopProject w) =
      lambda • period8BottomProject w := by
  funext i
  fin_cases i
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexNegativeToPositive, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (4 : Fin 8)
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexNegativeToPositive, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (5 : Fin 8)
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexNegativeToPositive, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (6 : Fin 8)
  · simpa [period8ChiralCoordinateMatrix, period8TopProject,
      period8BottomProject, period8ComplexNegativeToPositive, Matrix.mulVec,
      Matrix.vecHead, Matrix.vecTail] using congrFun hEig (7 : Fin 8)

theorem period8_chiral_top_nonzero {xi lambda : ℂ} {w : Fin 8 → ℂ}
    (hlambda : lambda ≠ 0)
    (hEig : (period8ChiralCoordinateMatrix xi).mulVec w = lambda • w)
    (hw : w ≠ 0) :
    period8TopProject w ≠ 0 := by
  intro htop
  have hbottom :=
    period8_chiral_bottom_equation (xi := xi) (lambda := lambda) hEig
  rw [htop] at hbottom
  simp at hbottom
  have hbotzero : period8BottomProject w = 0 := by
    exact (smul_eq_zero.mp hbottom.symm).resolve_left hlambda
  have hreconstruct := period8_embed_project_reconstruct w
  rw [htop, hbotzero] at hreconstruct
  apply hw
  calc
    w = period8TopEmbed 0 + period8BottomEmbed 0 := hreconstruct.symm
    _ = 0 := by
      funext i
      fin_cases i <;> simp [period8TopEmbed, period8BottomEmbed]

theorem period8_chiral_squared_top_eigen {xi lambda : ℂ} {w : Fin 8 → ℂ}
    (hxi : xi ≠ 0) (hlambda : lambda ≠ 0)
    (hEig : (period8ChiralCoordinateMatrix xi).mulVec w = lambda • w)
    (hw : w ≠ 0) :
    (period8ComplexSquaredBlock xi).mulVec (period8TopProject w) =
      (lambda^2) • period8TopProject w := by
  let x := period8TopProject w
  let y := period8BottomProject w
  have htop :=
    period8_chiral_top_equation (xi := xi) (lambda := lambda) hEig
  have hbottom :=
    period8_chiral_bottom_equation (xi := xi) (lambda := lambda) hEig
  have htop_nonzero :=
    period8_chiral_top_nonzero (xi := xi) (lambda := lambda) hlambda hEig hw
  have htop' :
      (period8ComplexPositiveToNegative xi).mulVec y = lambda • x := by
    simpa [x, y] using htop
  have hbottom' :
      (period8ComplexNegativeToPositive xi).mulVec x = lambda • y := by
    simpa [x, y] using hbottom
  have hbc :
      (period8ComplexPositiveToNegative xi *
        period8ComplexNegativeToPositive xi).mulVec x =
        (lambda^2) • x := by
    rw [← Matrix.mulVec_mulVec, hbottom', Matrix.mulVec_smul, htop']
    simp [pow_two, smul_smul, mul_comm]
  rw [← period8_complex_squared_block (xi := xi) hxi]
  simpa [x] using hbc

theorem period8_chiral_eigen_square_root {xi lambda : ℂ} {w : Fin 8 → ℂ}
    (hxi : xi ≠ 0) (hlambda : lambda ≠ 0)
    (hEig : (period8ChiralCoordinateMatrix xi).mulVec w = lambda • w)
    (hw : w ≠ 0) :
    period8FiberPolynomialC (lambda^2) (xi^2 + xi⁻¹^2) = 0 := by
  apply period8_complex_squared_block_eigen_root hxi (period8TopProject w)
  · exact period8_chiral_squared_top_eigen hxi hlambda hEig hw
  · exact period8_chiral_top_nonzero hlambda hEig hw

theorem period8_fiber_inverse_intertwines {xi : ℂ} (hxi : xi ≠ 0) :
    period8ChiralCoordinateMatrix xi * period8ChiralBasisInverse xi =
      period8ChiralBasisInverse xi * period8Fiber xi := by
  calc
    period8ChiralCoordinateMatrix xi * period8ChiralBasisInverse xi =
        (period8ChiralBasisInverse xi * period8Fiber xi *
          period8ChiralBasis xi) * period8ChiralBasisInverse xi := by
            rw [period8_fiber_similar_to_chiral_coordinates hxi]
    _ = period8ChiralBasisInverse xi * period8Fiber xi *
          (period8ChiralBasis xi * period8ChiralBasisInverse xi) := by
            rw [Matrix.mul_assoc, Matrix.mul_assoc]
    _ = period8ChiralBasisInverse xi * period8Fiber xi := by
            rw [period8_chiral_basis_right_inverse hxi, Matrix.mul_one]

theorem period8_fiber_eigen_square_root {xi lambda : ℂ} {u : Fin 8 → ℂ}
    (hxi : xi ≠ 0) (hlambda : lambda ≠ 0)
    (hEig : (period8Fiber xi).mulVec u = lambda • u)
    (hu : u ≠ 0) :
    period8FiberPolynomialC (lambda^2) (xi^2 + xi⁻¹^2) = 0 := by
  let V := period8ChiralBasisInverse xi
  let U := period8ChiralBasis xi
  let w := V.mulVec u
  have hw : w ≠ 0 := by
    intro hwzero
    apply hu
    calc
      u = (U * V).mulVec u := by
        rw [period8_chiral_basis_right_inverse hxi, Matrix.one_mulVec]
      _ = U.mulVec (V.mulVec u) := by
        rw [← Matrix.mulVec_mulVec]
      _ = 0 := by
        rw [show V.mulVec u = w by rfl, hwzero, Matrix.mulVec_zero]
  have hEigW : (period8ChiralCoordinateMatrix xi).mulVec w = lambda • w := by
    calc
      (period8ChiralCoordinateMatrix xi).mulVec w =
          (period8ChiralCoordinateMatrix xi * V).mulVec u := by
            rw [show w = V.mulVec u by rfl, ← Matrix.mulVec_mulVec]
      _ = (V * period8Fiber xi).mulVec u := by
            rw [period8_fiber_inverse_intertwines hxi]
      _ = V.mulVec ((period8Fiber xi).mulVec u) := by
            rw [← Matrix.mulVec_mulVec]
      _ = lambda • V.mulVec u := by rw [hEig, Matrix.mulVec_smul]
      _ = lambda • w := by rw [show w = V.mulVec u by rfl]
  exact period8_chiral_eigen_square_root hxi hlambda hEigW hw

theorem period8_fiber_polynomialC_eq (y c : ℂ) :
    period8FiberPolynomialC y c = period8PolynomialC y c := by
  simp [period8FiberPolynomialC, period8PolynomialC]

theorem period8_fiber_real_eigen_square_lt_bound
    {xi z alpha : ℂ} {L : ℕ} {lambda : ℝ} {u : Fin 8 → ℂ}
    (hL : L ≠ 0) (hxi_sq : xi^2 = z) (hz : z^L = alpha)
    (halpha : alpha^2 = 1)
    (hEig : (period8Fiber xi).mulVec u = (lambda : ℂ) • u)
    (hu : u ≠ 0) :
    lambda^2 < period8Bound := by
  by_cases hlambda : lambda = 0
  · rw [hlambda]
    simpa using period8_bound_positive
  · have hcast : (lambda : ℂ) ≠ 0 := by
      exact_mod_cast hlambda
    have hxi : xi ≠ 0 := by
      intro hzero
      have hzzero : z = 0 := by
        calc
          z = xi^2 := hxi_sq.symm
          _ = 0 := by simp [hzero]
      rw [hzzero] at hz
      simp [hL] at hz
      have : alpha = 0 := hz.symm
      rw [this] at halpha
      norm_num at halpha
    have hroot_fiber :=
      period8_fiber_eigen_square_root (xi := xi) (lambda := (lambda : ℂ))
        hxi hcast hEig hu
    have hroot :
        period8PolynomialC ((lambda^2 : ℝ) : ℂ) (xi^2 + xi⁻¹^2) = 0 := by
      rw [← period8_fiber_polynomialC_eq]
      simpa using hroot_fiber
    exact period8_holonomy_root_lt_bound hL hxi_sq hz halpha hroot

set_option maxHeartbeats 1500000 in
theorem period8_fiber_isHermitian {xi : ℂ}
    (hunit : xi * (starRingEnd ℂ) xi = 1) :
    (period8Fiber xi).IsHermitian := by
  have hconj := period8_unit_conj_eq_inv hunit
  rw [Matrix.IsHermitian]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8Fiber, Matrix.conjTranspose, hconj, map_pow]

end TargetA
