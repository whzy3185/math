import TargetA.Period8SharpEdge

namespace TargetA

/-- Largest squared fiber eigenvalue at real phase parameter c. -/
noncomputable def period8TopRoot (c : ℝ) : ℝ :=
  4 + Real.sqrt (8 + c + Real.sqrt (26 - 3 * c))

theorem period8_polynomial_shift_identity (y c : ℝ) :
    period8Polynomial y c = ((y - 4)^2 - (8 + c))^2 - (26 - 3 * c) := by
  unfold period8Polynomial
  ring

theorem period8_inner_discriminant_pos {c : ℝ} (hc : c ≤ 2) :
    0 < 26 - 3 * c := by linarith

theorem period8_inner_sqrt_ge_four {c : ℝ} (hc : c ≤ 2) :
    (4 : ℝ) ≤ Real.sqrt (26 - 3 * c) := by
  have h := Real.sqrt_le_sqrt (by linarith : (16 : ℝ) ≤ 26 - 3 * c)
  norm_num at h
  exact h

theorem period8_top_radicand_pos {c : ℝ} (hc : -2 ≤ c) :
    0 < 8 + c + Real.sqrt (26 - 3 * c) := by
  linarith [Real.sqrt_nonneg (26 - 3 * c)]

theorem period8_top_root_gt_four {c : ℝ} (hc : -2 ≤ c) :
    4 < period8TopRoot c := by
  unfold period8TopRoot
  have h := Real.sqrt_pos.mpr (period8_top_radicand_pos hc)
  linarith

/-- The displayed radical is an actual polynomial root throughout the phase interval. -/
theorem period8_top_root_is_root {c : ℝ} (hcl : -2 ≤ c) (hcu : c ≤ 2) :
    period8Polynomial (period8TopRoot c) c = 0 := by
  rw [period8_polynomial_shift_identity]
  have hi : (Real.sqrt (26 - 3 * c))^2 = 26 - 3 * c :=
    Real.sq_sqrt (le_of_lt (period8_inner_discriminant_pos hcu))
  have ho : (Real.sqrt (8 + c + Real.sqrt (26 - 3 * c)))^2 =
      8 + c + Real.sqrt (26 - 3 * c) :=
    Real.sq_sqrt (le_of_lt (period8_top_radicand_pos hcl))
  unfold period8TopRoot
  rw [show 4 + Real.sqrt (8 + c + Real.sqrt (26 - 3 * c)) - 4 =
    Real.sqrt (8 + c + Real.sqrt (26 - 3 * c)) by ring, ho]
  rw [show 8 + c + Real.sqrt (26 - 3 * c) - (8 + c) =
    Real.sqrt (26 - 3 * c) by ring, hi]
  ring

/-- Every real polynomial root is at most the exact largest radical root. -/
theorem period8_root_le_top_root {y c : ℝ}
    (hroot : period8Polynomial y c = 0) : y ≤ period8TopRoot c := by
  have hq : ((y - 4)^2 - (8 + c))^2 = 26 - 3 * c := by
    rw [period8_polynomial_shift_identity] at hroot
    linarith
  have hqle : (y - 4)^2 - (8 + c) ≤ Real.sqrt (26 - 3 * c) := by
    calc
      (y - 4)^2 - (8 + c) ≤ |(y - 4)^2 - (8 + c)| := le_abs_self _
      _ = Real.sqrt (26 - 3 * c) := by rw [← Real.sqrt_sq_eq_abs, hq]
  have hs : (y - 4)^2 ≤ 8 + c + Real.sqrt (26 - 3 * c) := by linarith
  have habs : |y - 4| ≤ Real.sqrt (8 + c + Real.sqrt (26 - 3 * c)) := by
    rw [← Real.sqrt_sq_eq_abs]
    exact Real.sqrt_le_sqrt hs
  unfold period8TopRoot
  linarith [le_abs_self (y - 4)]

/-- The inner radicand grows strictly with c on the full phase interval. -/
theorem period8_top_radicand_strict_mono {a b : ℝ}
    (hb : b ≤ 2) (hab : a < b) :
    8 + a + Real.sqrt (26 - 3 * a) < 8 + b + Real.sqrt (26 - 3 * b) := by
  have ha : a ≤ 2 := by linarith
  have hsa := period8_inner_sqrt_ge_four ha
  have hsb := period8_inner_sqrt_ge_four hb
  have hsqa : (Real.sqrt (26 - 3 * a))^2 = 26 - 3 * a :=
    Real.sq_sqrt (le_of_lt (period8_inner_discriminant_pos ha))
  have hsqb : (Real.sqrt (26 - 3 * b))^2 = 26 - 3 * b :=
    Real.sq_sqrt (le_of_lt (period8_inner_discriminant_pos hb))
  have hdiff : Real.sqrt (26 - 3 * b) < Real.sqrt (26 - 3 * a) :=
    Real.sqrt_lt_sqrt (le_of_lt (period8_inner_discriminant_pos hb)) (by linarith)
  have hp : 0 < (Real.sqrt (26 - 3 * a) - Real.sqrt (26 - 3 * b)) *
      (Real.sqrt (26 - 3 * a) + Real.sqrt (26 - 3 * b) - 3) :=
    mul_pos (by linarith) (by linarith)
  nlinarith

theorem period8_top_root_strict_mono {a b : ℝ}
    (ha : -2 ≤ a) (hb : b ≤ 2) (hab : a < b) :
    period8TopRoot a < period8TopRoot b := by
  unfold period8TopRoot
  apply add_lt_add_right
  exact Real.sqrt_lt_sqrt (le_of_lt (period8_top_radicand_pos ha))
    (period8_top_radicand_strict_mono hb hab)

theorem period8_top_root_at_two : period8TopRoot 2 = period8Edge := by
  have hs : Real.sqrt (20 : ℝ) = 2 * Real.sqrt 5 := by
    rw [show (20 : ℝ) = 4 * 5 by norm_num, Real.sqrt_mul (by norm_num)]
    norm_num
  norm_num [period8TopRoot, period8Edge, hs]

end TargetA
