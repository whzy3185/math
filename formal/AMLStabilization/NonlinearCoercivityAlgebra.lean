import Mathlib
import AMLStabilization.AlgebraicCore

namespace AMLStabilization

/-- Gradient coefficient in the nonlinear mass-weighted coercivity estimate. -/
noncomputable def nonlinearMassWeightedA (Cp V K m : ℝ) : ℝ :=
  Cp ^ 2 * (1 + 2 * V * K ^ 2 / m ^ 2)

/-- Weighted-moment coefficient in the nonlinear mass-weighted coercivity estimate. -/
noncomputable def nonlinearMassWeightedB (V m q : ℝ) : ℝ :=
  2 * V * m ^ (-2 / q)

/-- Squared coefficient identity used in the arbitrary-`q` mean estimate. -/
theorem rpow_neg_inv_sq
    {m q : ℝ} (hm : 0 < m) (hq : 0 < q) :
    (m ^ (-1 / q)) ^ 2 = m ^ (-2 / q) := by
  have hexp : (-1 / q) * (2 : ℝ) = -2 / q := by
    field_simp [ne_of_gt hq]
  calc
    (m ^ (-1 / q)) ^ 2 = (m ^ (-1 / q)) ^ (2 : ℝ) := by
      rw [Real.rpow_natCast]
    _ = m ^ ((-1 / q) * (2 : ℝ)) := by
      rw [← Real.rpow_mul (le_of_lt hm)]
    _ = m ^ (-2 / q) := by rw [hexp]

/--
Pure algebraic closure behind the arbitrary-`q` nonlinear mass-weighted coercivity lemma.
Here `z` represents `(int rho |f|^q)^(1/q)` and `a` represents `|f_bar|`.
-/
theorem nonlinearMassWeightedCoercivityReduction
    {x y z a Cp V K m q : ℝ}
    (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) (ha : 0 ≤ a)
    (hCp : 0 ≤ Cp) (hV : 0 ≤ V) (hK : 0 ≤ K)
    (hm : 0 < m) (hq : 0 < q)
    (hlin : a ≤ m ^ (-1 / q) * z + (K * Cp / m) * y)
    (hbase : x ^ 2 ≤ Cp ^ 2 * y ^ 2 + V * a ^ 2) :
    x ^ 2 ≤
      nonlinearMassWeightedA Cp V K m * y ^ 2 +
        nonlinearMassWeightedB V m q * z ^ 2 := by
  have hm0 : 0 ≤ m := le_of_lt hm
  have hmq : 0 ≤ m ^ (-1 / q) := Real.rpow_nonneg hm0 _
  have hB : 0 ≤ K * Cp / m := by positivity
  have ha2 := squareOfLinearBound ha hz hy hmq hB hlin
  have hscaled := mul_le_mul_of_nonneg_left ha2 hV
  have hrpow := rpow_neg_inv_sq hm hq
  rw [hrpow] at hscaled
  have hstep :
      Cp ^ 2 * y ^ 2 + V * a ^ 2 ≤
        Cp ^ 2 * y ^ 2 +
          V * (2 * m ^ (-2 / q) * z ^ 2 + 2 * (K * Cp / m) ^ 2 * y ^ 2) :=
    add_le_add_left hscaled _
  calc
    x ^ 2 ≤ Cp ^ 2 * y ^ 2 + V * a ^ 2 := hbase
    _ ≤ Cp ^ 2 * y ^ 2 +
          V * (2 * m ^ (-2 / q) * z ^ 2 + 2 * (K * Cp / m) ^ 2 * y ^ 2) := hstep
    _ = nonlinearMassWeightedA Cp V K m * y ^ 2 +
          nonlinearMassWeightedB V m q * z ^ 2 := by
      unfold nonlinearMassWeightedA nonlinearMassWeightedB
      field_simp [ne_of_gt hm]
      ring

/-- The explicit coefficients are nonnegative under the natural sign assumptions. -/
theorem nonlinearMassWeighted_coefficients_nonneg
    {Cp V K m q : ℝ}
    (hCp : 0 ≤ Cp) (hV : 0 ≤ V) (hK : 0 ≤ K)
    (hm : 0 < m) (hq : 0 < q) :
    0 ≤ nonlinearMassWeightedA Cp V K m ∧
      0 ≤ nonlinearMassWeightedB V m q := by
  constructor
  · unfold nonlinearMassWeightedA
    have hm2 : 0 < m ^ 2 := pow_pos hm 2
    have hfrac : 0 ≤ 2 * V * K ^ 2 / m ^ 2 := by positivity
    positivity
  · unfold nonlinearMassWeightedB
    exact mul_nonneg (mul_nonneg (by norm_num) hV)
      (Real.rpow_nonneg (le_of_lt hm) _)

end AMLStabilization
