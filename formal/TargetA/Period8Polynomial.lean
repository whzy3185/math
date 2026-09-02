import Mathlib

namespace TargetA

noncomputable def period8Bound : ℝ := 1561 / 200

def period8Polynomial (y c : ℝ) : ℝ :=
  y^4 - 16 * y^3 + (80 - 2 * c) * y^2 + (-128 + 16 * c) * y +
    c^2 - 13 * c + 38

theorem period8_bound_positive : 0 < period8Bound := by
  norm_num [period8Bound]

theorem period8_boundary_factorization (y : ℝ) :
    period8Polynomial y 2 =
      (y^2 - 8 * y + 6 - 2 * Real.sqrt 5) *
        (y^2 - 8 * y + 6 + 2 * Real.sqrt 5) := by
  have hsqrt : (Real.sqrt 5)^2 = (5 : ℝ) := by
    exact Real.sq_sqrt (by norm_num)
  simp only [period8Polynomial]
  nlinarith

theorem period8_edge_is_boundary_root :
    period8Polynomial (4 + Real.sqrt (10 + 2 * Real.sqrt 5)) 2 = 0 := by
  have hsqrt_five : (Real.sqrt 5)^2 = (5 : ℝ) := by
    exact Real.sq_sqrt (by norm_num)
  have hnonneg : 0 ≤ (10 : ℝ) + 2 * Real.sqrt 5 := by positivity
  have hsqrt_edge :
      (Real.sqrt (10 + 2 * Real.sqrt 5))^2 = 10 + 2 * Real.sqrt 5 := by
    exact Real.sq_sqrt hnonneg
  rw [period8_boundary_factorization]
  nlinarith

theorem period8_at_two_positive {y : ℝ} (hy : period8Bound ≤ y) :
    0 < period8Polynomial y 2 := by
  have hu : 0 ≤ y - period8Bound := sub_nonneg.mpr hy
  have hidentity :
      period8Polynomial y 2 =
        (y - period8Bound)^4 +
        (761 / 50 : ℝ) * (y - period8Bound)^3 +
        (1337363 / 20000 : ℝ) * (y - period8Bound)^2 +
        (136311081 / 2000000 : ℝ) * (y - period8Bound) +
        (84332641 / 1600000000 : ℝ) := by
    rw [period8Polynomial, period8Bound]
    ring
  rw [hidentity]
  have hnonnegative :
      0 ≤
        (y - period8Bound)^4 +
          (761 / 50 : ℝ) * (y - period8Bound)^3 +
          (1337363 / 20000 : ℝ) * (y - period8Bound)^2 +
          (136311081 / 2000000 : ℝ) * (y - period8Bound) := by
    positivity
  have hconstant : 0 < (84332641 / 1600000000 : ℝ) := by norm_num
  linarith

theorem period8_polynomial_monotone_in_flux {y c : ℝ}
    (hy : period8Bound ≤ y) (hc : c ≤ 2) :
    period8Polynomial y 2 ≤ period8Polynomial y c := by
  have hu : 0 ≤ y - period8Bound := sub_nonneg.mpr hy
  have hquadratic : 0 ≤ 2 * y^2 - 16 * y + 9 := by
    have hidentity :
        2 * y^2 - 16 * y + 9 =
          2 * (y - period8Bound)^2 +
          (4 * period8Bound - 16) * (y - period8Bound) +
          (2 * period8Bound^2 - 16 * period8Bound + 9) := by
      rw [period8Bound]
      ring
    rw [hidentity]
    have hsquare : 0 ≤ (y - period8Bound)^2 := sq_nonneg (y - period8Bound)
    have hquadratic_term : 0 ≤ 2 * (y - period8Bound)^2 :=
      mul_nonneg (by norm_num) hsquare
    have hlinear_coefficient : 0 ≤ 4 * period8Bound - 16 := by
      norm_num [period8Bound]
    have hlinear_term : 0 ≤ (4 * period8Bound - 16) * (y - period8Bound) :=
      mul_nonneg hlinear_coefficient hu
    have hconstant : 0 ≤ 2 * period8Bound^2 - 16 * period8Bound + 9 := by
      norm_num [period8Bound]
    linarith
  have hleft : c - 2 ≤ 0 := by linarith
  have hright : c + 2 - 2 * y^2 + 16 * y - 13 ≤ 0 := by
    nlinarith
  have hproduct : 0 ≤ (c - 2) * (c + 2 - 2 * y^2 + 16 * y - 13) :=
    mul_nonneg_of_nonpos_of_nonpos hleft hright
  have hidentity :
      period8Polynomial y c - period8Polynomial y 2 =
        (c - 2) * (c + 2 - 2 * y^2 + 16 * y - 13) := by
    simp only [period8Polynomial]
    ring
  have hdifference : 0 ≤ period8Polynomial y c - period8Polynomial y 2 := by
    rw [hidentity]
    exact hproduct
  linarith

theorem period8_polynomial_positive {y c : ℝ}
    (hy : period8Bound ≤ y) (hc : c ≤ 2) :
    0 < period8Polynomial y c :=
  lt_of_lt_of_le (period8_at_two_positive hy) (period8_polynomial_monotone_in_flux hy hc)

end TargetA
