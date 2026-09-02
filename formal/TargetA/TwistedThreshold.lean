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

end TargetA
