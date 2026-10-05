import TargetA.Period8Polynomial

namespace TargetA

/-- The exact squared top edge of the continuous period-eight family. -/
noncomputable def period8Edge : ℝ := 4 + Real.sqrt (10 + 2 * Real.sqrt 5)

theorem period8_edge_lt_bound : period8Edge < period8Bound := by
  exact period8_root_lt_bound (by norm_num : (2 : ℝ) ≤ 2)
    period8_edge_is_boundary_root

theorem period8_edge_ge_fifteen_halves : (15 / 2 : ℝ) ≤ period8Edge := by
  have h5 : (Real.sqrt 5)^2 = (5 : ℝ) := Real.sq_sqrt (by norm_num)
  have h5n := Real.sqrt_nonneg (5 : ℝ)
  have h5l : (2 : ℝ) ≤ Real.sqrt 5 := by nlinarith
  have hsn := Real.sqrt_nonneg (10 + 2 * Real.sqrt 5)
  have hs : (Real.sqrt (10 + 2 * Real.sqrt 5))^2 =
      10 + 2 * Real.sqrt 5 := Real.sq_sqrt (by positivity)
  unfold period8Edge
  nlinarith

theorem period8_edge_quadratic :
    period8Edge^2 - 8 * period8Edge + 6 - 2 * Real.sqrt 5 = 0 := by
  have hs : (Real.sqrt (10 + 2 * Real.sqrt 5))^2 =
      10 + 2 * Real.sqrt 5 := Real.sq_sqrt (by positivity)
  unfold period8Edge
  nlinarith

theorem period8_at_two_nonneg_of_edge_le {y : ℝ} (hy : period8Edge ≤ y) :
    0 ≤ period8Polynomial y 2 := by
  have he := period8_edge_ge_fifteen_halves
  have hf : 0 ≤ y^2 - 8 * y + 6 - 2 * Real.sqrt 5 := by
    have hm : 0 ≤ (y - period8Edge) * (y + period8Edge - 8) :=
      mul_nonneg (by linarith) (by linarith)
    nlinarith [period8_edge_quadratic]
  rw [period8_boundary_factorization]
  exact mul_nonneg hf (by linarith [Real.sqrt_nonneg (5 : ℝ)])

theorem period8_at_two_pos_of_edge_lt {y : ℝ} (hy : period8Edge < y) :
    0 < period8Polynomial y 2 := by
  have he := period8_edge_ge_fifteen_halves
  have hf : 0 < y^2 - 8 * y + 6 - 2 * Real.sqrt 5 := by
    have hm : 0 < (y - period8Edge) * (y + period8Edge - 8) :=
      mul_pos (by linarith) (by linarith)
    nlinarith [period8_edge_quadratic]
  rw [period8_boundary_factorization]
  exact mul_pos hf (by linarith [Real.sqrt_nonneg (5 : ℝ)])

theorem period8_flux_factor_pos {y c : ℝ}
    (hy : period8Edge ≤ y) (hc : c ≤ 2) :
    0 < 2 * y^2 - 16 * y + 11 - c := by
  have he := period8_edge_ge_fifteen_halves
  nlinarith [sq_nonneg (y - (15 / 2 : ℝ))]

theorem period8_polynomial_ge_at_two_of_edge_le {y c : ℝ}
    (hy : period8Edge ≤ y) (hc : c ≤ 2) :
    period8Polynomial y 2 ≤ period8Polynomial y c := by
  have hm : 0 ≤ (2 - c) * (2 * y^2 - 16 * y + 11 - c) :=
    mul_nonneg (by linarith) (le_of_lt (period8_flux_factor_pos hy hc))
  have hid : period8Polynomial y c - period8Polynomial y 2 =
      (2 - c) * (2 * y^2 - 16 * y + 11 - c) := by
    unfold period8Polynomial
    ring
  linarith

theorem period8_polynomial_pos_of_edge_le_flux_lt {y c : ℝ}
    (hy : period8Edge ≤ y) (hc : c < 2) :
    0 < period8Polynomial y c := by
  have hm : 0 < (2 - c) * (2 * y^2 - 16 * y + 11 - c) :=
    mul_pos (by linarith) (period8_flux_factor_pos hy (le_of_lt hc))
  have hid : period8Polynomial y c - period8Polynomial y 2 =
      (2 - c) * (2 * y^2 - 16 * y + 11 - c) := by
    unfold period8Polynomial
    ring
  have hb := period8_at_two_nonneg_of_edge_le hy
  linarith

/-- A root with a strictly non-endpoint flux is strictly below the exact edge. -/
theorem period8_root_lt_edge {y c : ℝ} (hc : c < 2)
    (hroot : period8Polynomial y c = 0) : y < period8Edge := by
  by_contra h
  have hp := period8_polynomial_pos_of_edge_le_flux_lt (le_of_not_gt h) hc
  linarith

/-- Endpoint-inclusive sharp bound, without a nonnegativity assumption on the root. -/
theorem period8_root_le_edge {y c : ℝ} (hc : c ≤ 2)
    (hroot : period8Polynomial y c = 0) : y ≤ period8Edge := by
  by_contra h
  have hy : period8Edge < y := lt_of_not_ge h
  have hp := period8_at_two_pos_of_edge_lt hy
  have hm := period8_polynomial_ge_at_two_of_edge_le (le_of_lt hy) hc
  linarith

/-- Among allowed flux parameters, the exact upper edge occurs only at c = 2. -/
theorem period8_edge_root_iff {c : ℝ} (hc : c ≤ 2) :
    period8Polynomial period8Edge c = 0 ↔ c = 2 := by
  constructor
  · intro hroot
    by_contra hne
    have hlt : c < 2 := lt_of_le_of_ne hc hne
    have h := period8_root_lt_edge hlt hroot
    exact (lt_irrefl period8Edge) h
  · intro h
    subst c
    exact period8_edge_is_boundary_root

end TargetA
