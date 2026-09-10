import Mathlib

open MeasureTheory Filter
open scoped Topology

namespace AMLStabilization

/--
A dominated-differentiation theorem for the concrete squared `L²` energy.
The assumptions are the standard local hypotheses required by mathlib's
parametric-integral calculus: local measurability, integrability at the base
time, an integrable derivative majorant, and pointwise-in-space time
differentiability.

This discharges the abstract calculus step

`d/dt ∫ w(t,x)^2 dx = 2 ∫ w(t,x) w_t(t,x) dx`

without introducing it as an axiom.  PDE regularity is responsible only for
verifying the stated domination/measurability hypotheses in a concrete
application.
-/
theorem hasDerivAt_integral_square_of_dominated
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {w wt : ℝ → Omega → ℝ}
    {t0 : ℝ} {s : Set ℝ} {bound : Omega → ℝ}
    (hs : s ∈ 𝓝 t0)
    (hSquareMeas : ∀ᶠ t in 𝓝 t0,
      AEStronglyMeasurable (fun x => w t x ^ 2) mu)
    (hSquareInt : Integrable (fun x => w t0 x ^ 2) mu)
    (hDerivMeas : AEStronglyMeasurable
      (fun x => 2 * w t0 x * wt t0 x) mu)
    (hDerivBound : ∀ᵐ x ∂mu, ∀ t ∈ s,
      ‖2 * w t x * wt t x‖ ≤ bound x)
    (hBoundInt : Integrable bound mu)
    (hTimeDeriv : ∀ᵐ x ∂mu, ∀ t ∈ s,
      HasDerivAt (fun tau => w tau x) (wt t x) t) :
    HasDerivAt
      (fun t => ∫ x, w t x ^ 2 ∂mu)
      (2 * ∫ x, w t0 x * wt t0 x ∂mu) t0 := by
  have hSquareDeriv : ∀ᵐ x ∂mu, ∀ t ∈ s,
      HasDerivAt (fun tau => w tau x ^ 2)
        (2 * w t x * wt t x) t := by
    filter_upwards [hTimeDeriv] with x hx
    intro t ht
    simpa using (hx t ht).fun_pow 2
  obtain ⟨_, hmain⟩ :=
    hasDerivAt_integral_of_dominated_loc_of_deriv_le
      (F := fun t x => w t x ^ 2)
      (F' := fun t x => 2 * w t x * wt t x)
      (bound := bound)
      hs hSquareMeas hSquareInt hDerivMeas hDerivBound hBoundInt hSquareDeriv
  have hcoeff :
      (∫ x, 2 * w t0 x * wt t0 x ∂mu) =
        2 * ∫ x, w t0 x * wt t0 x ∂mu := by
    calc
      (∫ x, 2 * w t0 x * wt t0 x ∂mu) =
          ∫ x, 2 * (w t0 x * wt t0 x) ∂mu := by
        apply integral_congr_ae
        filter_upwards with x
        ring
      _ = 2 * ∫ x, w t0 x * wt t0 x ∂mu := by
        rw [integral_const_mul]
  rw [hcoeff] at hmain
  exact hmain

/-- Pointwise version: if the dominated-differentiation hypotheses hold at
every time, the energy derivative identity is available at every time. -/
theorem integral_square_energy_derivative_identity
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {w wt : ℝ → Omega → ℝ}
    {E dE : ℝ → ℝ}
    (hE : ∀ t, E t = ∫ x, w t x ^ 2 ∂mu)
    (hdE : ∀ t, dE t = 2 * ∫ x, w t x * wt t x ∂mu)
    (hcore : ∀ t,
      HasDerivAt (fun tau => ∫ x, w tau x ^ 2 ∂mu)
        (2 * ∫ x, w t x * wt t x ∂mu) t) :
    ∀ t, HasDerivAt E (dE t) t := by
  intro t
  have hfun : E = fun tau => ∫ x, w tau x ^ 2 ∂mu := by
    funext tau
    exact hE tau
  rw [hfun, hdE t]
  exact hcore t

end AMLStabilization
