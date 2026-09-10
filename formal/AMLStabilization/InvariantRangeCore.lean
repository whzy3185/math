import Mathlib

namespace AMLStabilization

/-- Strict dissipativity forces the reaction to point downward above the equilibrium. -/
theorem dissipativity_inward_above
    {F : ℝ → ℝ} {zstar beta q s : ℝ}
    (hbeta : 0 < beta) (hs : zstar < s)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q) :
    F s < 0 := by
  have hdist : 0 < |s - zstar| := abs_pos.mpr (sub_ne_zero.mpr hs.ne')
  have hpow : 0 < |s - zstar| ^ q := Real.rpow_pos_of_pos hdist q
  have hrhs : -beta * |s - zstar| ^ q < 0 := by positivity
  have hprod : (s - zstar) * F s < 0 := lt_of_le_of_lt hdiss hrhs
  have hgap : 0 < s - zstar := sub_pos.mpr hs
  nlinarith

/-- Strict dissipativity forces the reaction to point upward below the equilibrium. -/
theorem dissipativity_inward_below
    {F : ℝ → ℝ} {zstar beta q s : ℝ}
    (hbeta : 0 < beta) (hs : s < zstar)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q) :
    0 < F s := by
  have hdist : 0 < |s - zstar| := abs_pos.mpr (sub_ne_zero.mpr hs.ne)
  have hpow : 0 < |s - zstar| ^ q := Real.rpow_pos_of_pos hdist q
  have hrhs : -beta * |s - zstar| ^ q < 0 := by positivity
  have hprod : (s - zstar) * F s < 0 := lt_of_le_of_lt hdiss hrhs
  have hgap : s - zstar < 0 := sub_neg.mpr hs
  nlinarith

/-- The dissipativity hypothesis plus `F(z*)=0` gives the correct inward sign
at both endpoints of every interval containing the equilibrium. -/
theorem dissipativity_inward_at_interval_endpoints
    {F : ℝ → ℝ} {zstar beta q lo hi : ℝ}
    (hbeta : 0 < beta) (hFstar : F zstar = 0)
    (hlo : lo ≤ zstar) (hhi : zstar ≤ hi)
    (hdiss : ∀ s, (s - zstar) * F s ≤ -beta * |s - zstar| ^ q) :
    0 ≤ F lo ∧ F hi ≤ 0 := by
  constructor
  · rcases hlo.eq_or_lt with rfl | hlt
    · simp [hFstar]
    · exact (dissipativity_inward_below hbeta hlt (hdiss lo)).le
  · rcases hhi.eq_or_lt with rfl | hlt
    · simp [hFstar]
    · exact (dissipativity_inward_above hbeta hlt (hdiss hi)).le

/-- At an upper spatial contact point, a nonpositive Laplacian and nonnegative
weight make the full signal PDE right-hand side nonpositive. -/
theorem upper_contact_rhs_nonpos
    {F : ℝ → ℝ} {zstar beta q s rho lap : ℝ}
    (hbeta : 0 < beta) (hrho : 0 ≤ rho) (hlap : lap ≤ 0)
    (hFstar : F zstar = 0) (hs : zstar ≤ s)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q) :
    lap + rho * F s ≤ 0 := by
  have hF : F s ≤ 0 := by
    rcases hs.eq_or_lt with rfl | hlt
    · simpa [hFstar]
    · exact (dissipativity_inward_above hbeta hlt hdiss).le
  have hreact : rho * F s ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hrho hF
  linarith

/-- At a lower spatial contact point, a nonnegative Laplacian and nonnegative
weight make the full signal PDE right-hand side nonnegative. -/
theorem lower_contact_rhs_nonneg
    {F : ℝ → ℝ} {zstar beta q s rho lap : ℝ}
    (hbeta : 0 < beta) (hrho : 0 ≤ rho) (hlap : 0 ≤ lap)
    (hFstar : F zstar = 0) (hs : s ≤ zstar)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q) :
    0 ≤ lap + rho * F s := by
  have hF : 0 ≤ F s := by
    rcases hs.eq_or_lt with rfl | hlt
    · simpa [hFstar]
    · exact (dissipativity_inward_below hbeta hlt hdiss).le
  have hreact : 0 ≤ rho * F s := mul_nonneg hrho hF
  linarith

/-- A scalar envelope with everywhere nonpositive derivative cannot increase. -/
theorem upper_envelope_preserved
    {Y dY : ℝ → ℝ} {s t M : ℝ}
    (hYderiv : ∀ tau, HasDerivAt Y (dY tau) tau)
    (hdY : ∀ tau, dY tau ≤ 0)
    (hst : s ≤ t) (hinit : Y s ≤ M) :
    Y t ≤ M := by
  have hdiff : Differentiable ℝ Y := fun tau => (hYderiv tau).differentiableAt
  have hderiv : ∀ tau, deriv Y tau ≤ 0 := by
    intro tau
    rw [(hYderiv tau).deriv]
    exact hdY tau
  have hanti : Antitone Y := antitone_of_deriv_nonpos hdiff hderiv
  exact (hanti hst).trans hinit

/-- A scalar envelope with everywhere nonnegative derivative cannot decrease. -/
theorem lower_envelope_preserved
    {Y dY : ℝ → ℝ} {s t m : ℝ}
    (hYderiv : ∀ tau, HasDerivAt Y (dY tau) tau)
    (hdY : ∀ tau, 0 ≤ dY tau)
    (hst : s ≤ t) (hinit : m ≤ Y s) :
    m ≤ Y t := by
  have hdiff : Differentiable ℝ Y := fun tau => (hYderiv tau).differentiableAt
  have hderiv : ∀ tau, 0 ≤ deriv Y tau := by
    intro tau
    rw [(hYderiv tau).deriv]
    exact hdY tau
  have hmono : Monotone Y := monotone_of_deriv_nonneg hdiff hderiv
  exact hinit.trans (hmono hst)

/-- Scalar two-sided invariant interval once upper/lower envelope derivative
signs have been supplied by a maximum-principle argument. -/
theorem invariant_interval_from_envelope_derivatives
    {lo hi upper lower dUpper dLower s t : ℝ}
    {U L : ℝ → ℝ}
    (hUpperDeriv : ∀ tau, HasDerivAt U (dUpper tau) tau)
    (hLowerDeriv : ∀ tau, HasDerivAt L (dLower tau) tau)
    (hUpperSign : ∀ tau, dUpper tau ≤ 0)
    (hLowerSign : ∀ tau, 0 ≤ dLower tau)
    (hst : s ≤ t) (hUinit : U s ≤ hi) (hLinit : lo ≤ L s) :
    U t ≤ hi ∧ lo ≤ L t := by
  exact ⟨upper_envelope_preserved hUpperDeriv hUpperSign hst hUinit,
    lower_envelope_preserved hLowerDeriv hLowerSign hst hLinit⟩

end AMLStabilization
