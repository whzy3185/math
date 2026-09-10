import Mathlib

namespace AMLStabilization

/-- Exponential energy decay with doubled exponent yields the corresponding square-root norm rate. -/
theorem sqrt_exponential_energy_bound
    {Q C lambda T t : ℝ}
    (hQ0 : 0 ≤ Q) (hC : 0 ≤ C)
    (hQ : Q ≤ C * Real.exp (-(2 * lambda) * (t - T))) :
    Real.sqrt Q ≤ Real.sqrt C * Real.exp (-lambda * (t - T)) := by
  have hy0 : 0 ≤ Real.sqrt C * Real.exp (-lambda * (t - T)) :=
    mul_nonneg (Real.sqrt_nonneg _) (Real.exp_nonneg _)
  rw [Real.sqrt_le_iff]
  constructor
  · exact hy0
  · have hexpsq :
        Real.exp (-lambda * (t - T)) ^ 2 =
          Real.exp (-(2 * lambda) * (t - T)) := by
      rw [pow_two, ← Real.exp_add]
      congr 1
      ring
    calc
      Q ≤ C * Real.exp (-(2 * lambda) * (t - T)) := hQ
      _ = (Real.sqrt C * Real.exp (-lambda * (t - T))) ^ 2 := by
        rw [mul_pow, Real.sq_sqrt hC, hexpsq]

/-- Polynomial energy decay with doubled exponent yields the corresponding square-root norm rate. -/
theorem sqrt_polynomial_energy_bound
    {Q C b T t : ℝ}
    (hQ0 : 0 ≤ Q) (hC : 0 ≤ C) (hTt : T ≤ t)
    (hQ : Q ≤ C * (1 + (t - T)) ^ (-(2 * b))) :
    Real.sqrt Q ≤ Real.sqrt C * (1 + (t - T)) ^ (-b) := by
  have hbase : 0 < 1 + (t - T) := by linarith
  have hy0 : 0 ≤ Real.sqrt C * (1 + (t - T)) ^ (-b) :=
    mul_nonneg (Real.sqrt_nonneg _) (Real.rpow_nonneg hbase.le _)
  rw [Real.sqrt_le_iff]
  constructor
  · exact hy0
  · have hpowsq :
        ((1 + (t - T)) ^ (-b)) ^ 2 =
          (1 + (t - T)) ^ (-(2 * b)) := by
      rw [pow_two, ← Real.rpow_add hbase]
      congr 1
      ring
    calc
      Q ≤ C * (1 + (t - T)) ^ (-(2 * b)) := hQ
      _ = (Real.sqrt C * (1 + (t - T)) ^ (-b)) ^ 2 := by
        rw [mul_pow, Real.sq_sqrt hC, hpowsq]

/-- Scalar closure of a Choi-type local boundedness interface for an exponential rate. -/
theorem parabolicUpgrade_exponential_rate
    {U rootQ H Cq Ch CQ CH lambda T t : ℝ}
    (hCq : 0 ≤ Cq) (hCh : 0 ≤ Ch) (hCQ : 0 ≤ CQ) (hCH : 0 ≤ CH)
    (hrootQ : rootQ ≤ CQ * Real.exp (-lambda * (t - T)))
    (hH : H ≤ CH * Real.exp (-lambda * (t - T)))
    (hupgrade : U ≤ Cq * rootQ + Ch * H) :
    U ≤ (Cq * CQ + Ch * CH) * Real.exp (-lambda * (t - T)) := by
  have hq := mul_le_mul_of_nonneg_left hrootQ hCq
  have hh := mul_le_mul_of_nonneg_left hH hCh
  calc
    U ≤ Cq * rootQ + Ch * H := hupgrade
    _ ≤ Cq * (CQ * Real.exp (-lambda * (t - T))) +
        Ch * (CH * Real.exp (-lambda * (t - T))) := add_le_add hq hh
    _ = (Cq * CQ + Ch * CH) * Real.exp (-lambda * (t - T)) := by ring

/-- Scalar closure of a Choi-type local boundedness interface for a polynomial rate. -/
theorem parabolicUpgrade_polynomial_rate
    {U rootQ H Cq Ch CQ CH b T t : ℝ}
    (hCq : 0 ≤ Cq) (hCh : 0 ≤ Ch) (hCQ : 0 ≤ CQ) (hCH : 0 ≤ CH)
    (hrootQ : rootQ ≤ CQ * (1 + (t - T)) ^ (-b))
    (hH : H ≤ CH * (1 + (t - T)) ^ (-b))
    (hupgrade : U ≤ Cq * rootQ + Ch * H) :
    U ≤ (Cq * CQ + Ch * CH) * (1 + (t - T)) ^ (-b) := by
  have hq := mul_le_mul_of_nonneg_left hrootQ hCq
  have hh := mul_le_mul_of_nonneg_left hH hCh
  calc
    U ≤ Cq * rootQ + Ch * H := hupgrade
    _ ≤ Cq * (CQ * (1 + (t - T)) ^ (-b)) +
        Ch * (CH * (1 + (t - T)) ^ (-b)) := add_le_add hq hh
    _ = (Cq * CQ + Ch * CH) * (1 + (t - T)) ^ (-b) := by ring

end AMLStabilization
