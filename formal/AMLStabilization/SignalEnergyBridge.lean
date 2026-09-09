import AMLStabilization.AlgebraicCore
import AMLStabilization.EnergyDecay

namespace AMLStabilization

/--
Bridge from the PDE-style energy identity plus mass-weighted coercivity to the
scalar differential inequality required by `EnergyDecay.lean`.

Interpretation for the paper:
* `E(t)` is the squared L2 signal energy;
* `gradSq(t)` is the gradient dissipation;
* `weighted(t)` is the weighted signal term;
* `alpha` is the coefficient of the weighted dissipation;
* `C` is the coercivity constant;
* `delta <= min(1, alpha)` is the common dissipation fraction.

The PDE energy identity is encoded as
`dE + 2 * (gradSq + alpha * weighted) <= 0`.
The coercivity estimate is encoded as
`E <= C * (gradSq + weighted)`.
-/
theorem pdeEnergy_to_scalarDissipation
    {E dE gradSq weighted : ℝ → ℝ}
    {C alpha delta : ℝ}
    (hC : 0 < C)
    (hdelta : 0 ≤ delta)
    (hdelta1 : delta ≤ 1)
    (hdeltaAlpha : delta ≤ alpha)
    (hgrad : ∀ t, 0 ≤ gradSq t)
    (hweighted : ∀ t, 0 ≤ weighted t)
    (hcoerc : ∀ t, E t ≤ C * (gradSq t + weighted t))
    (henergy : ∀ t, dE t + 2 * (gradSq t + alpha * weighted t) ≤ 0) :
    ∀ t, dE t + (2 * delta / C) * E t ≤ 0 := by
  intro t
  have hscaled :
      delta * E t ≤ C * (gradSq t + alpha * weighted t) := by
    exact scaledDissipationCoercivity
      (hgrad t) (hweighted t) (le_of_lt hC) hdelta hdelta1 hdeltaAlpha (hcoerc t)
  have hrate :
      (2 * delta / C) * E t ≤ 2 * (gradSq t + alpha * weighted t) := by
    rw [div_mul_eq_mul_div]
    apply (div_le_iff₀ hC).2
    nlinarith [hscaled]
  linarith [henergy t, hrate]

/--
Full abstract bridge: once the PDE supplies differentiability of the energy,
the PDE energy inequality and coercivity automatically yield exponential decay.
-/
theorem pdeEnergy_to_exponentialDecay
    {E dE gradSq weighted : ℝ → ℝ}
    {C alpha delta s t : ℝ}
    (hE : ∀ τ, HasDerivAt E (dE τ) τ)
    (hC : 0 < C)
    (hdelta : 0 ≤ delta)
    (hdelta1 : delta ≤ 1)
    (hdeltaAlpha : delta ≤ alpha)
    (hgrad : ∀ τ, 0 ≤ gradSq τ)
    (hweighted : ∀ τ, 0 ≤ weighted τ)
    (hcoerc : ∀ τ, E τ ≤ C * (gradSq τ + weighted τ))
    (henergy : ∀ τ, dE τ + 2 * (gradSq τ + alpha * weighted τ) ≤ 0)
    (hst : s ≤ t) :
    E t ≤ E s * Real.exp (-(2 * delta / C) * (t - s)) := by
  apply energy_le_exp_of_differential_inequality
    (E := E) (dE := dE) (c := 2 * delta / C) (s := s) (t := t)
  · exact hE
  · exact pdeEnergy_to_scalarDissipation
      hC hdelta hdelta1 hdeltaAlpha hgrad hweighted hcoerc henergy
  · exact hst

/-- Initial-time specialization of the PDE-to-exponential-decay bridge. -/
theorem pdeEnergy_to_exponentialDecay_from_zero
    {E dE gradSq weighted : ℝ → ℝ}
    {C alpha delta t : ℝ}
    (hE : ∀ τ, HasDerivAt E (dE τ) τ)
    (hC : 0 < C)
    (hdelta : 0 ≤ delta)
    (hdelta1 : delta ≤ 1)
    (hdeltaAlpha : delta ≤ alpha)
    (hgrad : ∀ τ, 0 ≤ gradSq τ)
    (hweighted : ∀ τ, 0 ≤ weighted τ)
    (hcoerc : ∀ τ, E τ ≤ C * (gradSq τ + weighted τ))
    (henergy : ∀ τ, dE τ + 2 * (gradSq τ + alpha * weighted τ) ≤ 0)
    (ht : 0 ≤ t) :
    E t ≤ E 0 * Real.exp (-(2 * delta / C) * t) := by
  simpa using
    (pdeEnergy_to_exponentialDecay
      (E := E) (dE := dE) (gradSq := gradSq) (weighted := weighted)
      (C := C) (alpha := alpha) (delta := delta) (s := 0) (t := t)
      hE hC hdelta hdelta1 hdeltaAlpha hgrad hweighted hcoerc henergy ht)

end AMLStabilization
