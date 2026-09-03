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

theorem period8_unit_of_pow_eq_one {xi : ℂ} {m : ℕ}
    (hm : m ≠ 0) (hpow : xi^m = 1) :
    xi * (starRingEnd ℂ) xi = 1 := by
  have hnorm : ‖xi‖ = 1 :=
    Complex.norm_eq_one_of_pow_eq_one hpow hm
  have hnormsq : Complex.normSq xi = 1 := by
    rw [← Complex.norm_mul_self_eq_normSq, hnorm]
    norm_num
  simpa [Complex.mul_conj] using hnormsq

theorem period8_xi_unit_from_holonomy {xi z alpha : ℂ} {L : ℕ}
    (hL : L ≠ 0) (hxi : xi^2 = z) (hz : z^L = alpha)
    (halpha : alpha^2 = 1) :
    xi * (starRingEnd ℂ) xi = 1 := by
  apply period8_unit_of_pow_eq_one (m := 4 * L)
  · omega
  · calc
      xi^(4 * L) = (xi^2)^(2 * L) := by ring_nf
      _ = z^(2 * L) := by rw [hxi]
      _ = (z^L)^2 := by ring_nf
      _ = alpha^2 := by rw [hz]
      _ = 1 := halpha

theorem period8_unit_parameter_real {xi : ℂ}
    (hunit : xi * (starRingEnd ℂ) xi = 1) :
    (starRingEnd ℂ) (xi^2 + xi⁻¹^2) = xi^2 + xi⁻¹^2 := by
  have hconj := period8_unit_conj_eq_inv hunit
  simp [map_add, map_pow, hconj]
  ring

theorem period8_unit_parameter_re_le_two {xi : ℂ}
    (hunit : xi * (starRingEnd ℂ) xi = 1) :
    (xi^2 + xi⁻¹^2).re ≤ 2 := by
  have hnormsq : Complex.normSq xi = 1 := by
    have hr := congrArg Complex.re hunit
    simpa [Complex.normSq_apply, Complex.mul_re, Complex.conj_re,
      Complex.conj_im] using hr
  have hnorm : ‖xi‖ = 1 := by
    have hsquare : ‖xi‖ ^ 2 = 1 := by
      rw [Complex.sq_norm, hnormsq]
    nlinarith [norm_nonneg xi]
  have hnormpow : ‖xi^2‖ = 1 := by
    rw [norm_pow, hnorm]
    norm_num
  have hinv : xi⁻¹ = (starRingEnd ℂ) xi := by
    exact (period8_unit_conj_eq_inv hunit).symm
  have hc : xi^2 + xi⁻¹^2 = xi^2 + (starRingEnd ℂ) (xi^2) := by
    rw [hinv]
    simp [map_pow]
  have hcre : (xi^2 + xi⁻¹^2).re = 2 * (xi^2).re := by
    rw [hc, Complex.add_conj]
    simp
  rw [hcre]
  nlinarith [Complex.re_le_norm (xi^2)]

theorem period8_polynomialC_ofReal (y c : ℝ) :
    period8PolynomialC (y : ℂ) (c : ℂ) =
      (period8Polynomial y c : ℂ) := by
  simp [period8PolynomialC, period8Polynomial]

theorem period8_complex_root_is_real_root {y c : ℝ}
    (hroot : period8PolynomialC (y : ℂ) (c : ℂ) = 0) :
    period8Polynomial y c = 0 := by
  apply Complex.ofReal_injective
  rw [← period8_polynomialC_ofReal]
  simpa using hroot

theorem period8_unit_complex_root_is_real_root {xi : ℂ} {y : ℝ}
    (hunit : xi * (starRingEnd ℂ) xi = 1)
    (hroot : period8PolynomialC (y : ℂ) (xi^2 + xi⁻¹^2) = 0) :
    period8Polynomial y (xi^2 + xi⁻¹^2).re = 0 := by
  have hreal := period8_unit_parameter_real hunit
  have hcast : ((xi^2 + xi⁻¹^2).re : ℂ) = xi^2 + xi⁻¹^2 :=
    Complex.conj_eq_iff_re.mp hreal
  rw [← hcast] at hroot
  exact period8_complex_root_is_real_root hroot

theorem period8_unit_complex_root_lt_bound {xi : ℂ} {y : ℝ}
    (hunit : xi * (starRingEnd ℂ) xi = 1)
    (hroot : period8PolynomialC (y : ℂ) (xi^2 + xi⁻¹^2) = 0) :
    y < period8Bound := by
  apply period8_root_lt_bound (period8_unit_parameter_re_le_two hunit)
  exact period8_unit_complex_root_is_real_root hunit hroot

theorem period8_holonomy_root_lt_bound {xi z alpha : ℂ} {L : ℕ} {y : ℝ}
    (hL : L ≠ 0) (hxi : xi^2 = z) (hz : z^L = alpha)
    (halpha : alpha^2 = 1)
    (hroot : period8PolynomialC (y : ℂ) (xi^2 + xi⁻¹^2) = 0) :
    y < period8Bound := by
  apply period8_unit_complex_root_lt_bound
  exact period8_xi_unit_from_holonomy hL hxi hz halpha
  exact hroot

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
  all_goals
    field_simp [hxi] <;> ring

set_option maxHeartbeats 4000000 in
theorem period8_squared_block_annihilated {xi : ℝ} (hxi : xi ≠ 0) :
    let S := period8SquaredChiralBlock xi
    let c := xi^2 + xi⁻¹^2
    S^4 - (16 : ℝ) • S^3 + (80 - 2 * c) • S^2 +
      (-128 + 16 * c) • S + (c^2 - 13 * c + 38) • 1 = 0 := by
  dsimp
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [period8SquaredChiralBlock, pow_succ]
  all_goals
    field_simp [hxi] <;> ring

theorem period8_matrix_power_on_eigenvector {S : Matrix (Fin 4) (Fin 4) ℝ}
    {y : ℝ} {v : Fin 4 → ℝ} (hv : S.mulVec v = y • v) :
    ∀ k : ℕ, (S^k).mulVec v = y^k • v
  | 0 => by simp
  | k + 1 => by
      rw [pow_succ, ← Matrix.mulVec_mulVec, hv, Matrix.mulVec_smul,
        period8_matrix_power_on_eigenvector hv k]
      simp [pow_succ, smul_smul, mul_comm]

theorem period8_squared_block_eigen_root {xi y : ℝ}
    (hxi : xi ≠ 0) (v : Fin 4 → ℝ)
    (hv : (period8SquaredChiralBlock xi).mulVec v = y • v)
    (hv_ne : v ≠ 0) :
    period8Polynomial y (xi^2 + xi⁻¹^2) = 0 := by
  let S := period8SquaredChiralBlock xi
  let c := xi^2 + xi⁻¹^2
  have hannih :
      S^4 - (16 : ℝ) • S^3 + (80 - 2 * c) • S^2 +
        (-128 + 16 * c) • S + (c^2 - 13 * c + 38) • 1 = 0 := by
    simpa [S, c] using period8_squared_block_annihilated (xi := xi) hxi
  have hvS : S.mulVec v = y • v := by
    simpa [S] using hv
  have hpow := period8_matrix_power_on_eigenvector (S := S) (y := y) (v := v) hv
  have hvector := congrArg (fun M : Matrix (Fin 4) (Fin 4) ℝ => M.mulVec v) hannih
  simp only [Matrix.add_mulVec, Matrix.sub_mulVec, Matrix.smul_mulVec,
    Matrix.zero_mulVec, Matrix.one_mulVec] at hvector
  rw [hpow 4, hpow 3, hpow 2, hvS] at hvector
  by_contra hroot
  apply hv_ne
  funext i
  have hentry := congrFun hvector i
  simp only [smul_eq_mul, Pi.add_apply, Pi.sub_apply, Pi.smul_apply,
    Pi.zero_apply] at hentry
  have hpoly : period8Polynomial y c ≠ 0 := hroot
  have hfactor : period8Polynomial y c * v i = 0 := by
    calc
      period8Polynomial y c * v i =
          y^4 * v i - 16 * (y^3 * v i) +
            (80 - 2 * c) * (y^2 * v i) +
            (-128 + 16 * c) * (y * v i) +
            (c^2 - 13 * c + 38) * v i := by
              simp [period8Polynomial]
              ring
      _ = 0 := hentry
  exact (mul_eq_zero.mp hfactor).resolve_left hpoly

theorem period8_squared_block_eigen_lt_bound {xi y : ℝ}
    (hxi : xi ≠ 0) (hc : xi^2 + xi⁻¹^2 ≤ 2)
    (v : Fin 4 → ℝ) (hv : (period8SquaredChiralBlock xi).mulVec v = y • v)
    (hv_ne : v ≠ 0) :
    y < period8Bound := by
  apply period8_root_lt_bound hc
  exact period8_squared_block_eigen_root hxi v hv hv_ne

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
