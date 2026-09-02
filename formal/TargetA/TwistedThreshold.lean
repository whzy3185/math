import Mathlib
import TargetA.Period8Polynomial

namespace TargetA

theorem sqrt_two_gt_141_over_100 :
    (141 / 100 : ℝ) < Real.sqrt 2 := by
  have hsquare : (Real.sqrt (2 : ℝ)) ^ 2 = 2 := by
    exact Real.sq_sqrt (by norm_num)
  have hnonneg : 0 ≤ Real.sqrt (2 : ℝ) := Real.sqrt_nonneg _
  nlinarith

theorem sqrt_two_add_sqrt_two_gt_923_over_500 :
    (923 / 500 : ℝ) < Real.sqrt (2 + Real.sqrt 2) := by
  have hsquare : (Real.sqrt (2 + Real.sqrt (2 : ℝ))) ^ 2 = 2 + Real.sqrt 2 := by
    apply Real.sq_sqrt
    positivity
  have hnonneg : 0 ≤ Real.sqrt (2 + Real.sqrt (2 : ℝ)) := Real.sqrt_nonneg _
  have htwo := sqrt_two_gt_141_over_100
  nlinarith

theorem sqrt_two_add_nested_gt_1961_over_1000 :
    (1961 / 1000 : ℝ) <
      Real.sqrt (2 + Real.sqrt (2 + Real.sqrt 2)) := by
  have hsquare :
      (Real.sqrt (2 + Real.sqrt (2 + Real.sqrt (2 : ℝ)))) ^ 2 =
        2 + Real.sqrt (2 + Real.sqrt 2) := by
    apply Real.sq_sqrt
    positivity
  have hnonneg :
      0 ≤ Real.sqrt (2 + Real.sqrt (2 + Real.sqrt (2 : ℝ))) :=
    Real.sqrt_nonneg _
  have hinner := sqrt_two_add_sqrt_two_gt_923_over_500
  nlinarith

theorem twisted_at_thirty_two_gt_bound :
    period8Bound <
      4 + 2 * Real.cos (Real.pi / 16) + 2 * Real.cos (Real.pi / 8) := by
  rw [Real.cos_pi_div_sixteen, Real.cos_pi_div_eight]
  have hfirst := sqrt_two_add_nested_gt_1961_over_1000
  have hsecond := sqrt_two_add_sqrt_two_gt_923_over_500
  norm_num [period8Bound] at *
  linarith

theorem twisted_multiple_of_eight_gt_bound (L : ℕ) (hL : 4 ≤ L) :
    period8Bound <
      4 + 2 * Real.cos (Real.pi / (4 * (L : ℝ))) +
        2 * Real.cos (Real.pi / (2 * (L : ℝ))) := by
  have hden_one : (16 : ℝ) ≤ 4 * (L : ℝ) := by
    exact_mod_cast (show 16 ≤ 4 * L by omega)
  have hden_two : (8 : ℝ) ≤ 2 * (L : ℝ) := by
    exact_mod_cast (show 8 ≤ 2 * L by omega)
  have hangle_one : Real.pi / (4 * (L : ℝ)) ≤ Real.pi / 16 :=
    div_le_div_of_nonneg_left Real.pi_pos.le (by norm_num) hden_one
  have hangle_two : Real.pi / (2 * (L : ℝ)) ≤ Real.pi / 8 :=
    div_le_div_of_nonneg_left Real.pi_pos.le (by norm_num) hden_two
  have hangle_one_nonneg : 0 ≤ Real.pi / (4 * (L : ℝ)) := by positivity
  have hangle_two_nonneg : 0 ≤ Real.pi / (2 * (L : ℝ)) := by positivity
  have hpi_sixteen : Real.pi / 16 ≤ Real.pi := by
    nlinarith [Real.pi_pos]
  have hpi_eight : Real.pi / 8 ≤ Real.pi := by
    nlinarith [Real.pi_pos]
  have hcos_one :
      Real.cos (Real.pi / 16) ≤
        Real.cos (Real.pi / (4 * (L : ℝ))) :=
    Real.cos_le_cos_of_nonneg_of_le_pi hangle_one_nonneg hpi_sixteen hangle_one
  have hcos_two :
      Real.cos (Real.pi / 8) ≤
        Real.cos (Real.pi / (2 * (L : ℝ))) :=
    Real.cos_le_cos_of_nonneg_of_le_pi hangle_two_nonneg hpi_eight hangle_two
  linarith [twisted_at_thirty_two_gt_bound]

end TargetA
