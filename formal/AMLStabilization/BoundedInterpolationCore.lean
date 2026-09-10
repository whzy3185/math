import Mathlib

open MeasureTheory

namespace AMLStabilization

/-- Pointwise power interpolation under an `L^∞` bound. -/
theorem abs_rpow_le_sq_mul_bound
    {x R s : ℝ}
    (hs : 2 ≤ s) (hR : 0 ≤ R) (hx : |x| ≤ R) :
    |x| ^ s ≤ x ^ 2 * R ^ (s - 2) := by
  have hx0 : 0 ≤ |x| := abs_nonneg x
  have hsexp : 0 ≤ s - 2 := sub_nonneg.mpr hs
  by_cases hzero : x = 0
  · subst x
    have hs0 : s ≠ 0 := ne_of_gt (lt_of_lt_of_le (by norm_num) hs)
    simp [Real.zero_rpow hs0]
  · have hxpos : 0 < |x| := abs_pos.mpr hzero
    have hp : |x| ^ (s - 2) ≤ R ^ (s - 2) :=
      Real.rpow_le_rpow hx0 hx hsexp
    have hsplit : |x| ^ s = |x| ^ (2 : ℝ) * |x| ^ (s - 2) := by
      have hexp : (2 : ℝ) + (s - 2) = s := by ring
      rw [← Real.rpow_add hxpos, hexp]
    have hsquare : |x| ^ (2 : ℝ) = x ^ 2 := by
      rw [Real.rpow_two, sq_abs]
    rw [hsplit, hsquare]
    exact mul_le_mul_of_nonneg_left hp (sq_nonneg x)

/-- Integral interpolation: boundedness converts an `L²` moment into every finite higher moment. -/
theorem integral_abs_rpow_le_bound_mul_square
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {f : Omega → ℝ}
    {R s : ℝ}
    (hs : 2 ≤ s) (hR : 0 ≤ R)
    (hbound : ∀ x, |f x| ≤ R)
    (hsInt : Integrable (fun x => |f x| ^ s) mu)
    (h2Int : Integrable (fun x => f x ^ 2) mu) :
    (∫ x, |f x| ^ s ∂mu) ≤
      R ^ (s - 2) * (∫ x, f x ^ 2 ∂mu) := by
  have hconstInt : Integrable (fun x => R ^ (s - 2) * f x ^ 2) mu :=
    h2Int.const_mul (R ^ (s - 2))
  calc
    (∫ x, |f x| ^ s ∂mu) ≤
        ∫ x, R ^ (s - 2) * f x ^ 2 ∂mu := by
      refine integral_mono hsInt hconstInt ?_
      intro x
      have hx := abs_rpow_le_sq_mul_bound hs hR (hbound x)
      simpa [mul_comm] using hx
    _ = R ^ (s - 2) * (∫ x, f x ^ 2 ∂mu) := by
      rw [integral_const_mul]

/-- Exponential `L²` energy decay transfers to an exponential higher-moment decay under a uniform bound. -/
theorem boundedInterpolation_exponential_moment
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {f : ℝ → Omega → ℝ} {E : ℝ → ℝ}
    {R s C lambda T t : ℝ}
    (hs : 2 ≤ s) (hR : 0 ≤ R) (hC : 0 ≤ C)
    (hbound : ∀ tau x, |f tau x| ≤ R)
    (hsInt : ∀ tau, Integrable (fun x => |f tau x| ^ s) mu)
    (h2Int : ∀ tau, Integrable (fun x => f tau x ^ 2) mu)
    (hE : ∀ tau, E tau = (∫ x, f tau x ^ 2 ∂mu))
    (hdecay : E t ≤ C * Real.exp (-lambda * (t - T))) :
    (∫ x, |f t x| ^ s ∂mu) ≤
      R ^ (s - 2) * C * Real.exp (-lambda * (t - T)) := by
  have hinterp := integral_abs_rpow_le_bound_mul_square
    (mu := mu) (f := f t) hs hR (hbound t) (hsInt t) (h2Int t)
  rw [← hE t] at hinterp
  have hRpow : 0 ≤ R ^ (s - 2) := Real.rpow_nonneg hR _
  calc
    (∫ x, |f t x| ^ s ∂mu) ≤ R ^ (s - 2) * E t := hinterp
    _ ≤ R ^ (s - 2) * (C * Real.exp (-lambda * (t - T))) :=
      mul_le_mul_of_nonneg_left hdecay hRpow
    _ = R ^ (s - 2) * C * Real.exp (-lambda * (t - T)) := by ring

end AMLStabilization
