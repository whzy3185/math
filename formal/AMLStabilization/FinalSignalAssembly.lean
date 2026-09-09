import AMLStabilization.PoincareMeanCore
import AMLStabilization.SignalEnergyIdentityCore

namespace AMLStabilization

/--
Final abstract assembly for the signal L2 decay proof.

The coercivity produced by `PoincareMeanCore` naturally has different
coefficients on the gradient and weighted terms.  This theorem normalizes them
to one positive constant and feeds the result, together with the PDE energy
inequality produced by `SignalEnergyIdentityCore`, into the verified Gronwall
bridge.
-/
theorem anisotropicCoercivity_to_exponentialDecay
    {E dE gradSq weighted : ℝ → ℝ}
    {A B alpha delta s t : ℝ}
    (hE : ∀ τ, HasDerivAt E (dE τ) τ)
    (hA : 0 ≤ A)
    (hB : 0 ≤ B)
    (hdelta : 0 ≤ delta)
    (hdelta1 : delta ≤ 1)
    (hdeltaAlpha : delta ≤ alpha)
    (hgrad : ∀ τ, 0 ≤ gradSq τ)
    (hweighted : ∀ τ, 0 ≤ weighted τ)
    (hcoerc : ∀ τ, E τ ≤ A * gradSq τ + B * weighted τ)
    (henergy : ∀ τ, dE τ + 2 * (gradSq τ + alpha * weighted τ) ≤ 0)
    (hst : s ≤ t) :
    E t ≤ E s *
      Real.exp (-(2 * delta / (1 + A + B)) * (t - s)) := by
  have hC : 0 < 1 + A + B := by linarith
  have hcoerc' :
      ∀ τ, E τ ≤ (1 + A + B) * (gradSq τ + weighted τ) := by
    intro τ
    have hAle : A ≤ 1 + A + B := by linarith
    have hBle : B ≤ 1 + A + B := by linarith
    have hAG := mul_le_mul_of_nonneg_right hAle (hgrad τ)
    have hBW := mul_le_mul_of_nonneg_right hBle (hweighted τ)
    calc
      E τ ≤ A * gradSq τ + B * weighted τ := hcoerc τ
      _ ≤ (1 + A + B) * gradSq τ + (1 + A + B) * weighted τ :=
        add_le_add hAG hBW
      _ = (1 + A + B) * (gradSq τ + weighted τ) := by ring
  exact pdeEnergy_to_exponentialDecay
    (E := E) (dE := dE) (gradSq := gradSq) (weighted := weighted)
    (C := 1 + A + B) (alpha := alpha) (delta := delta)
    (s := s) (t := t)
    hE hC hdelta hdelta1 hdeltaAlpha hgrad hweighted hcoerc' henergy hst

/-- Initial-time version of the final signal assembly. -/
theorem anisotropicCoercivity_to_exponentialDecay_from_zero
    {E dE gradSq weighted : ℝ → ℝ}
    {A B alpha delta t : ℝ}
    (hE : ∀ τ, HasDerivAt E (dE τ) τ)
    (hA : 0 ≤ A)
    (hB : 0 ≤ B)
    (hdelta : 0 ≤ delta)
    (hdelta1 : delta ≤ 1)
    (hdeltaAlpha : delta ≤ alpha)
    (hgrad : ∀ τ, 0 ≤ gradSq τ)
    (hweighted : ∀ τ, 0 ≤ weighted τ)
    (hcoerc : ∀ τ, E τ ≤ A * gradSq τ + B * weighted τ)
    (henergy : ∀ τ, dE τ + 2 * (gradSq τ + alpha * weighted τ) ≤ 0)
    (ht : 0 ≤ t) :
    E t ≤ E 0 *
      Real.exp (-(2 * delta / (1 + A + B)) * t) := by
  simpa using
    (anisotropicCoercivity_to_exponentialDecay
      (E := E) (dE := dE) (gradSq := gradSq) (weighted := weighted)
      (A := A) (B := B) (alpha := alpha) (delta := delta)
      (s := 0) (t := t)
      hE hA hB hdelta hdelta1 hdeltaAlpha hgrad hweighted hcoerc henergy ht)

/--
Exact coefficient package coming from the verified mass-weighted coercivity
argument.  `A` controls the gradient dissipation and `B` the weighted signal
dissipation.
-/
noncomputable def massWeightedA (m K Cp V : ℝ) : ℝ :=
  2 * Cp ^ 2 + 4 * V * (K * Cp / m) ^ 2

noncomputable def massWeightedB (m V : ℝ) : ℝ :=
  4 * V * (Real.sqrt m / m) ^ 2

/-- Positivity of the two explicit mass-weighted coefficients under the paper's
natural sign assumptions. -/
theorem massWeighted_coefficients_nonneg
    {m K Cp V : ℝ}
    (hm : 0 < m) (hK : 0 ≤ K) (hCp : 0 ≤ Cp) (hV : 0 ≤ V) :
    0 ≤ massWeightedA m K Cp V ∧ 0 ≤ massWeightedB m V := by
  constructor
  · unfold massWeightedA
    positivity
  · unfold massWeightedB
    positivity

/--
Final coefficient-specialized decay theorem.  The coercivity hypothesis is
exactly the conclusion of
`integralMassWeightedCoercivity_of_MemLp_and_Poincare`; the energy hypothesis is
exactly the conclusion of `signalEnergyInequality_from_integralPDE` (or its
production-consumption specialization).
-/
theorem massWeightedSignal_exponentialDecay
    {E dE gradSq weighted : ℝ → ℝ}
    {m K Cp V alpha delta s t : ℝ}
    (hE : ∀ τ, HasDerivAt E (dE τ) τ)
    (hm : 0 < m)
    (hK : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hV : 0 ≤ V)
    (hdelta : 0 ≤ delta)
    (hdelta1 : delta ≤ 1)
    (hdeltaAlpha : delta ≤ alpha)
    (hgrad : ∀ τ, 0 ≤ gradSq τ)
    (hweighted : ∀ τ, 0 ≤ weighted τ)
    (hcoerc : ∀ τ,
      E τ ≤ massWeightedA m K Cp V * gradSq τ +
        massWeightedB m V * weighted τ)
    (henergy : ∀ τ,
      dE τ + 2 * (gradSq τ + alpha * weighted τ) ≤ 0)
    (hst : s ≤ t) :
    E t ≤ E s *
      Real.exp (-(2 * delta /
        (1 + massWeightedA m K Cp V + massWeightedB m V)) * (t - s)) := by
  obtain ⟨hA, hB⟩ := massWeighted_coefficients_nonneg hm hK hCp hV
  exact anisotropicCoercivity_to_exponentialDecay
    (E := E) (dE := dE) (gradSq := gradSq) (weighted := weighted)
    (A := massWeightedA m K Cp V) (B := massWeightedB m V)
    (alpha := alpha) (delta := delta) (s := s) (t := t)
    hE hA hB hdelta hdelta1 hdeltaAlpha hgrad hweighted hcoerc henergy hst

end AMLStabilization
