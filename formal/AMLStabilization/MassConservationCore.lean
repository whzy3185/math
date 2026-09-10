import Mathlib

open MeasureTheory

namespace AMLStabilization

/-- A differentiable scalar quantity with zero derivative is conserved. -/
theorem scalarConservation_of_zeroDerivative
    {M : ℝ → ℝ}
    (hM : ∀ t, HasDerivAt M 0 t) :
    ∀ s t, M t = M s := by
  have hdiff : Differentiable ℝ M := fun t => (hM t).differentiableAt
  have hderiv : ∀ t, deriv M t = 0 := fun t => (hM t).deriv
  intro s t
  exact is_const_of_deriv_eq_zero hdiff hderiv t s

/-- If the spatial integral of a density is represented by a differentiable
scalar mass functional whose time derivative vanishes, then the integral is
constant in time.  This isolates the calculus step from the PDE-specific
Neumann flux identity that supplies the zero derivative. -/
theorem integralMass_conserved_of_zeroDerivative
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {u : ℝ → Omega → ℝ} {M : ℝ → ℝ}
    (hMvalue : ∀ t, M t = ∫ x, u t x ∂mu)
    (hMderiv : ∀ t, HasDerivAt M 0 t) :
    ∀ s t, (∫ x, u t x ∂mu) = ∫ x, u s x ∂mu := by
  intro s t
  have hc := scalarConservation_of_zeroDerivative hMderiv s t
  simpa [← hMvalue s, ← hMvalue t] using hc

/-- Initial positive mass plus zero time derivative gives the positive fixed
mass hypothesis used by the weighted-damping coercivity theorem at every time. -/
theorem integralMass_fixed_positive
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {u : ℝ → Omega → ℝ} {M : ℝ → ℝ}
    {T mass : ℝ}
    (hmass : 0 < mass)
    (hMvalue : ∀ t, M t = ∫ x, u t x ∂mu)
    (hMderiv : ∀ t, HasDerivAt M 0 t)
    (hinitial : (∫ x, u T x ∂mu) = mass) :
    ∀ t, (∫ x, u t x ∂mu) = mass := by
  intro t
  calc
    (∫ x, u t x ∂mu) = ∫ x, u T x ∂mu :=
      integralMass_conserved_of_zeroDerivative hMvalue hMderiv T t
    _ = mass := hinitial

end AMLStabilization
