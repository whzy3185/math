import TargetA.Period8Fiber
import TargetA.Period8ExactRoot

namespace TargetA

set_option maxRecDepth 10000

set_option maxHeartbeats 3000000 in
/-- The quartic is the actual characteristic determinant of the squared chiral block. -/
theorem period8_squared_block_characteristic_det {xi y : ℂ} (hxi : xi ≠ 0) :
    (y • (1 : Matrix (Fin 4) (Fin 4) ℂ) - period8ComplexSquaredBlock xi).det =
      period8PolynomialC y (xi^2 + xi⁻¹^2) := by
  have hm : y • (1 : Matrix (Fin 4) (Fin 4) ℂ) - period8ComplexSquaredBlock xi =
      !![y - 4 + (xi + xi⁻¹), 0, -(1 + xi⁻¹), -2;
         0, y - 4 + (xi + xi⁻¹), -2, -(1 - xi⁻¹);
         -(1 + xi), -2, y - 4 - (xi + xi⁻¹), 0;
         -2, -(1 - xi), 0, y - 4 - (xi + xi⁻¹)] := by
    ext i j
    fin_cases i <;> fin_cases j <;> simp [period8ComplexSquaredBlock, Matrix.one_apply] <;> ring
  rw [hm, Matrix.det_succ_row_zero]
  simp only [Fin.sum_univ_succ, Fin.sum_univ_zero, Matrix.det_fin_three, Matrix.submatrix_apply]
  have hcs : Fin.castSucc (2 : Fin 3) = (2 : Fin 4) := rfl
  norm_num [Fin.succAbove, Fin.lt_def, Matrix.cons_val_two, Matrix.cons_val_three,
    Matrix.vecHead, Matrix.vecTail, hcs, period8PolynomialC]
  field_simp [hxi]
  ring

/-- Every quartic root gives a genuine nonzero squared-block eigenvector. -/
theorem period8_root_gives_squared_block_eigenvector {xi y : ℂ}
    (hxi : xi ≠ 0) (hroot : period8PolynomialC y (xi^2 + xi⁻¹^2) = 0) :
    ∃ v : Fin 4 → ℂ, v ≠ 0 ∧ (period8ComplexSquaredBlock xi).mulVec v = y • v := by
  have hd : (y • (1 : Matrix (Fin 4) (Fin 4) ℂ) - period8ComplexSquaredBlock xi).det = 0 := by
    rw [period8_squared_block_characteristic_det hxi, hroot]
  obtain ⟨v, hv, he⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr hd
  refine ⟨v, hv, ?_⟩
  rw [Matrix.sub_mulVec, Matrix.smul_mulVec, Matrix.one_mulVec] at he
  exact (sub_eq_zero.mp he).symm

/-- A nonzero squared-block eigenvalue lifts to either choice of its square root. -/
theorem period8_squared_eigenvector_gives_chiral_eigenvector
    {xi lambda : ℂ} (hxi : xi ≠ 0) (hlambda : lambda ≠ 0)
    (v : Fin 4 → ℂ) (hv : v ≠ 0)
    (he : (period8ComplexSquaredBlock xi).mulVec v = lambda^2 • v) :
    ∃ w : Fin 8 → ℂ, w ≠ 0 ∧
      (period8ChiralCoordinateMatrix xi).mulVec w = lambda • w := by
  let b := (period8ComplexNegativeToPositive xi).mulVec v
  let w := period8TopEmbed v + period8BottomEmbed (lambda⁻¹ • b)
  have htop : period8TopProject w = v := by
    funext i
    fin_cases i <;> simp [w, period8TopProject, period8TopEmbed, period8BottomEmbed]
  have hw : w ≠ 0 := by
    intro hz
    apply hv
    rw [← htop, hz]
    funext i
    fin_cases i <;> simp [period8TopProject]
  refine ⟨w, hw, ?_⟩
  have hmul : (period8ComplexPositiveToNegative xi).mulVec b = lambda^2 • v := by
    change (period8ComplexPositiveToNegative xi).mulVec
      ((period8ComplexNegativeToPositive xi).mulVec v) = _
    rw [Matrix.mulVec_mulVec, period8_complex_squared_block hxi]
    exact he
  change (period8ChiralCoordinateMatrix xi).mulVec
    (period8TopEmbed v + period8BottomEmbed (lambda⁻¹ • b)) = _
  rw [Matrix.mulVec_add, period8_chiral_top_action, period8_chiral_bottom_action,
    Matrix.mulVec_smul, hmul]
  funext i
  fin_cases i <;>
    simp [w, b, period8TopEmbed, period8BottomEmbed, smul_smul, Pi.smul_apply]
  all_goals field_simp [hlambda] <;> ring

/-- Root-to-fiber attainment, the converse missing from the earlier upper-bound chain. -/
theorem period8_polynomial_root_gives_fiber_eigenvector
    {xi lambda : ℂ} (hxi : xi ≠ 0) (hlambda : lambda ≠ 0)
    (hroot : period8PolynomialC (lambda^2) (xi^2 + xi⁻¹^2) = 0) :
    ∃ u : Fin 8 → ℂ, u ≠ 0 ∧ (period8Fiber xi).mulVec u = lambda • u := by
  obtain ⟨v, hv, he⟩ := period8_root_gives_squared_block_eigenvector hxi hroot
  obtain ⟨w, hw, hwe⟩ :=
    period8_squared_eigenvector_gives_chiral_eigenvector hxi hlambda v hv he
  let u := (period8ChiralBasis xi).mulVec w
  have hu : u ≠ 0 := by
    intro hz
    apply hw
    have hh := congrArg (fun x => (period8ChiralBasisInverse xi).mulVec x) hz
    change (period8ChiralBasisInverse xi).mulVec ((period8ChiralBasis xi).mulVec w) = _ at hh
    rw [Matrix.mulVec_mulVec, period8_chiral_basis_left_inverse hxi, Matrix.one_mulVec] at hh
    simpa using hh
  refine ⟨u, hu, ?_⟩
  change (period8Fiber xi).mulVec ((period8ChiralBasis xi).mulVec w) = _
  rw [Matrix.mulVec_mulVec, period8_fiber_in_chiral_basis hxi,
    ← Matrix.mulVec_mulVec, hwe, Matrix.mulVec_smul]

/-- The real unit-phase parameter lies in the closed physical phase interval. -/
theorem period8_unit_parameter_mem_interval {xi : ℂ}
    (hunit : xi * (starRingEnd ℂ) xi = 1) :
    -2 ≤ (xi^2 + xi⁻¹^2).re ∧ (xi^2 + xi⁻¹^2).re ≤ 2 := by
  refine ⟨?_, period8_unit_parameter_re_le_two hunit⟩
  have hn2 : ‖xi‖ * ‖xi‖ = 1 := by simpa [norm_mul] using congrArg norm hunit
  have hn : ‖xi‖ = 1 := by nlinarith [norm_nonneg xi]
  have hnp : ‖xi^2‖ = 1 := by rw [norm_pow, hn]; norm_num
  have hinv : xi⁻¹ = (starRingEnd ℂ) xi := (period8_unit_conj_eq_inv hunit).symm
  have hc : xi^2 + xi⁻¹^2 = xi^2 + (starRingEnd ℂ) (xi^2) := by
    rw [hinv]
    simp [map_pow]
  have hcre : (xi^2 + xi⁻¹^2).re = 2 * (xi^2).re := by
    rw [hc, Complex.add_conj]
    simp
  rw [hcre]
  have hl := (abs_le.mp (Complex.abs_re_le_norm (xi^2))).1
  rw [hnp] at hl
  linarith

/-- Pointwise upper bound by the exact radical, including zero eigenvalues. -/
theorem period8_unit_fiber_eigen_square_le_top {xi : ℂ} {lambda : ℝ}
    (hunit : xi * (starRingEnd ℂ) xi = 1)
    (u : Fin 8 → ℂ) (hu : u ≠ 0)
    (he : (period8Fiber xi).mulVec u = (lambda : ℂ) • u) :
    lambda^2 ≤ period8TopRoot (xi^2 + xi⁻¹^2).re := by
  have hc := period8_unit_parameter_mem_interval hunit
  by_cases hlambda : lambda = 0
  · rw [hlambda]
    have htop := period8_top_root_gt_four hc.1
    simpa only [zero_pow (by decide : 2 ≠ 0)] using
      (le_trans (by norm_num : (0 : ℝ) ≤ 4) (le_of_lt htop))
  · have hxi : xi ≠ 0 := by intro hz; simp [hz] at hunit
    have hlambdaC : (lambda : ℂ) ≠ 0 := by exact_mod_cast hlambda
    have hr := period8_fiber_eigen_square_root hxi hlambdaC he hu
    rw [period8_fiber_polynomialC_eq] at hr
    have hr' : period8PolynomialC ((lambda^2 : ℝ) : ℂ) (xi^2 + xi⁻¹^2) = 0 := by
      simpa using hr
    exact period8_root_le_top_root (period8_unit_complex_root_is_real_root hunit hr')

/-- The pointwise upper bound is attained by a nonzero vector at its positive square root. -/
theorem period8_unit_fiber_top_attained {xi : ℂ}
    (hunit : xi * (starRingEnd ℂ) xi = 1) :
    ∃ u : Fin 8 → ℂ, u ≠ 0 ∧ (period8Fiber xi).mulVec u =
      (Real.sqrt (period8TopRoot (xi^2 + xi⁻¹^2).re) : ℂ) • u := by
  let c := (xi^2 + xi⁻¹^2).re
  have hc := period8_unit_parameter_mem_interval hunit
  have hcpos : 0 < period8TopRoot c := by
    have h : 4 < period8TopRoot c := period8_top_root_gt_four hc.1
    exact lt_trans (by norm_num : (0 : ℝ) < 4) h
  have hxi : xi ≠ 0 := by intro hz; simp [hz] at hunit
  have hlam : (Real.sqrt (period8TopRoot c) : ℂ) ≠ 0 := by
    exact_mod_cast (ne_of_gt (Real.sqrt_pos.mpr hcpos))
  apply period8_polynomial_root_gives_fiber_eigenvector hxi hlam
  have hsq : (Real.sqrt (period8TopRoot c) : ℂ)^2 = (period8TopRoot c : ℂ) := by
    exact_mod_cast (Real.sq_sqrt (le_of_lt hcpos))
  have hcast : (c : ℂ) = xi^2 + xi⁻¹^2 :=
    Complex.conj_eq_iff_re.mp (period8_unit_parameter_real hunit)
  rw [hsq, ← hcast, period8_polynomialC_ofReal, period8_top_root_is_root hc.1 hc.2]
  norm_num

end TargetA
