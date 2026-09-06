import Mathlib

namespace QuadraticGap

noncomputable section

/-- The contracting hard-channel root `lambda⁻¹ = 3 - 2√2`. -/
def hardQ : ℝ := 3 - 2 * Real.sqrt 2

private theorem sqrtTwoSq : (Real.sqrt (2 : ℝ)) ^ 2 = 2 := by
  have h : (0 : ℝ) ≤ 2 := by norm_num
  simpa using Real.sq_sqrt h

/-- Cross-multiplied form of
`2 q / (1-q^2) = 1/(2√2) = √2/4`.
Using a denominator-free identity keeps the lemma purely algebraic. -/
theorem hardQ_cusp_identity :
    8 * hardQ = Real.sqrt 2 * (1 - hardQ ^ 2) := by
  dsimp [hardQ]
  nlinarith [sqrtTwoSq]

/-- Cross-multiplied form of
`(1+q^2)/(1-q^2) = 3√2/4`, used in the first finite-`r`
Robin correction. -/
theorem hardQ_robin_ratio_identity :
    4 * (1 + hardQ ^ 2) =
      3 * Real.sqrt 2 * (1 - hardQ ^ 2) := by
  dsimp [hardQ]
  nlinarith [sqrtTwoSq]

/-- Algebra behind the `-3π/(8r)` correction to the effective
linear coefficient. -/
theorem effective_linear_first_correction :
    2 * (-3 * Real.sqrt 2 * Real.pi / 16) * (Real.sqrt 2 / 4) +
        Real.pi * (-3 / 16 : ℝ) =
      -3 * Real.pi / 8 := by
  have hs := sqrtTwoSq
  ring_nf at hs ⊢
  nlinarith

/-- The leading minimum of the effective parabola:
`(π/(2√2))^2 / 4 = π^2/32`, written with `π√2/4`. -/
theorem effective_gain_leading :
    (Real.pi * Real.sqrt 2 / 4) ^ 2 / 4 =
      Real.pi ^ 2 / 32 := by
  rw [div_pow]
  have hs := sqrtTwoSq
  ring_nf at hs ⊢
  nlinarith

/-- First correction to the scaled gain.  The right side equals
`-3π^2/(32√2)`. -/
theorem effective_gain_first_correction :
    (Real.pi * Real.sqrt 2 / 4) * (-3 * Real.pi / 8) / 2 =
      -3 * Real.pi ^ 2 * Real.sqrt 2 / 64 := by
  ring

/-- Equivalent denominator-free representation of the leading optimizer
`π/(4√2) = π√2/8`. -/
theorem optimizer_constant_square :
    (Real.pi * Real.sqrt 2 / 8) ^ 2 = Real.pi ^ 2 / 32 := by
  rw [div_pow]
  have hs := sqrtTwoSq
  ring_nf at hs ⊢
  nlinarith

end

end QuadraticGap
