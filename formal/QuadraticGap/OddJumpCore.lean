import Mathlib

namespace QuadraticGap

/-- Algebraic identity behind the weighted distance estimate used for the
odd-jump coarse gap bound. -/
theorem weighted_cauchy_identity (s θ δ : ℝ) :
    (1 + s ^ 2) * (θ ^ 2 + δ ^ 2) - (s * θ - δ) ^ 2 =
      (θ + s * δ) ^ 2 := by
  ring

/-- If the affine combination `s * θ - δ` stays a distance at least `a`
from zero, then the pair `(θ,δ)` has a corresponding Euclidean lower bound.
This is the purely algebraic Cauchy step in the odd-jump argument. -/
theorem weighted_distance_lower_bound
    (s θ δ a : ℝ)
    (ha : a ^ 2 ≤ (s * θ - δ) ^ 2) :
    a ^ 2 / (1 + s ^ 2) ≤ θ ^ 2 + δ ^ 2 := by
  have hden : 0 < 1 + s ^ 2 := by
    nlinarith [sq_nonneg s]
  rw [div_le_iff₀ hden]
  nlinarith [sq_nonneg (θ + s * δ)]

/-- The odd-jump coarse bound `4/(1+s^2)` is stronger than the common
all-parity envelope `1/(6s(s+2))` once `s≥2`. -/
theorem odd_coarse_bound_dominates_unified
    (s : ℝ) (hs : 2 ≤ s) :
    1 / (6 * s * (s + 2)) ≤ 4 / (1 + s ^ 2) := by
  have hs0 : 0 < s := by linarith
  have hs2 : 0 < s + 2 := by linarith
  have hden1 : 0 < 6 * s * (s + 2) := by positivity
  have hden2 : 0 < 1 + s ^ 2 := by nlinarith [sq_nonneg s]
  apply (div_le_div_iff₀ hden1 hden2).2
  nlinarith [sq_nonneg s]

end QuadraticGap
