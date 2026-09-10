import Mathlib

namespace AMLStabilization

/-- If `0 <= p <= d`, an exponential transient is dominated by the matching polynomial tail. -/
theorem exp_neg_mul_le_one_add_rpow_neg
    {x p d : ℝ}
    (hx : 0 ≤ x) (hp : 0 ≤ p) (hpd : p ≤ d) :
    Real.exp (-d * x) ≤ (1 + x) ^ (-p) := by
  have hbase : 0 < 1 + x := by linarith
  have hlog : Real.log (1 + x) ≤ x := by
    have h := Real.log_le_sub_one_of_pos hbase
    linarith
  have hplog : p * Real.log (1 + x) ≤ p * x :=
    mul_le_mul_of_nonneg_left hlog hp
  have hpx : p * x ≤ d * x :=
    mul_le_mul_of_nonneg_right hpd hx
  have hexpArg : -d * x ≤ Real.log (1 + x) * (-p) := by
    nlinarith [hplog, hpx]
  rw [Real.rpow_def_of_pos hbase]
  exact Real.exp_le_exp.mpr hexpArg

/-- Strict rate separation implies the non-strict comparison required above. -/
theorem exp_neg_mul_le_one_add_rpow_neg_of_lt
    {x p d : ℝ}
    (hx : 0 ≤ x) (hp : 0 ≤ p) (hpd : p < d) :
    Real.exp (-d * x) ≤ (1 + x) ^ (-p) :=
  exp_neg_mul_le_one_add_rpow_neg hx hp hpd.le

end AMLStabilization
