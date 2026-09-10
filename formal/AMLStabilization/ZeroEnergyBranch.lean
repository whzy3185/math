import Mathlib

namespace AMLStabilization

/-- A nonnegative dissipation in `E' + 2D <= 0` makes the energy antitone. -/
theorem energy_antitone_of_nonnegative_dissipation
    {E dE D : ℝ → ℝ}
    (hE : ∀ t, HasDerivAt E (dE t) t)
    (hD : ∀ t, 0 ≤ D t)
    (henergy : ∀ t, dE t + 2 * D t ≤ 0) :
    Antitone E := by
  refine antitone_of_hasDerivAt_nonpos hE ?_
  intro t
  linarith [henergy t, hD t]

/-- If a nonnegative antitone energy reaches zero, it remains exactly zero. -/
theorem energy_eq_zero_after_hit
    {E dE D : ℝ → ℝ} {s t : ℝ}
    (hE : ∀ tau, HasDerivAt E (dE tau) tau)
    (hEnonneg : ∀ tau, 0 ≤ E tau)
    (hD : ∀ tau, 0 ≤ D tau)
    (henergy : ∀ tau, dE tau + 2 * D tau ≤ 0)
    (hEs : E s = 0)
    (hst : s ≤ t) :
    E t = 0 := by
  have hanti := energy_antitone_of_nonnegative_dissipation hE hD henergy
  have hle : E t ≤ E s := hanti hst
  rw [hEs] at hle
  exact le_antisymm hle (hEnonneg t)

/-- Pointwise version: all later times stay on the zero branch. -/
theorem energy_zero_tail_after_hit
    {E dE D : ℝ → ℝ} {s : ℝ}
    (hE : ∀ tau, HasDerivAt E (dE tau) tau)
    (hEnonneg : ∀ tau, 0 ≤ E tau)
    (hD : ∀ tau, 0 ≤ D tau)
    (henergy : ∀ tau, dE tau + 2 * D tau ≤ 0)
    (hEs : E s = 0) :
    ∀ t ≥ s, E t = 0 := by
  intro t hst
  exact energy_eq_zero_after_hit hE hEnonneg hD henergy hEs hst

end AMLStabilization
