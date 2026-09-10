import Mathlib
import AMLStabilization.CellEnergyEnvelope
import AMLStabilization.RateRootCore

namespace AMLStabilization

/--
Exponential full-stabilization rate assembly after the two genuinely deep
parabolic analytic inputs have been supplied:
1. a signal `W^{1,∞}` rate (Neumann semigroup smoothing interface), and
2. a Choi-type local `L² -> L∞` estimate for the cell equation.
The coefficient forcing, cell `L²` decay, square-root conversion, and final
rate bookkeeping are all discharged internally.
-/
theorem fullExponentialStabilization_from_analytic_interfaces
    {Vnorm H Q dQ g U : ℝ → ℝ}
    {a Cp CV L Cq Ch lambda T t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCV : 0 ≤ CV) (hL : 0 ≤ L)
    (hCq : 0 ≤ Cq) (hCh : 0 ≤ Ch) (hlambda : 0 < lambda)
    (hrate : 2 * lambda < a / Cp ^ 2)
    (hTt : T ≤ t)
    (hVrate : ∀ tau,
      Vnorm tau ≤ CV * Real.exp (-lambda * (tau - T)))
    (hH0 : ∀ tau, 0 ≤ H tau)
    (hHbyV : ∀ tau, H tau ≤ L * Vnorm tau)
    (hQderiv : ∀ tau, HasDerivAt Q (dQ tau) tau)
    (hQ0 : ∀ tau, 0 ≤ Q tau)
    (hg0 : ∀ tau, 0 ≤ g tau)
    (hPoincare : ∀ tau, Q tau ≤ Cp ^ 2 * g tau ^ 2)
    (henergy : ∀ tau, dQ tau + 2 * a * g tau ^ 2 ≤ 2 * H tau * g tau)
    (hChoi : U t ≤ Cq * Real.sqrt (Q t) + Ch * H t) :
    Vnorm t ≤ CV * Real.exp (-lambda * (t - T)) ∧
    U t ≤
      (Cq * Real.sqrt
          (Q T + exponentialBarrier (a / Cp ^ 2) (2 * lambda) ((L * CV) ^ 2 / a)) +
        Ch * (L * CV)) *
        Real.exp (-lambda * (t - T)) := by
  have hCH : 0 ≤ L * CV := mul_nonneg hL hCV
  have hHrate : ∀ tau,
      H tau ≤ (L * CV) * Real.exp (-lambda * (tau - T)) := by
    intro tau
    calc
      H tau ≤ L * Vnorm tau := hHbyV tau
      _ ≤ L * (CV * Real.exp (-lambda * (tau - T))) :=
        mul_le_mul_of_nonneg_left (hVrate tau) hL
      _ = (L * CV) * Real.exp (-lambda * (tau - T)) := by ring
  have hQenv := cellEnergy_exponentialEnvelope_from_gradientRate
    (Q := Q) (dQ := dQ) (g := g) (H := H)
    (a := a) (Cp := Cp) (CH := L * CV) (lambda := lambda)
    (T := T) (t := t)
    ha hCp hCH hlambda hrate hTt hQderiv hQ0 hg0 hH0 hPoincare henergy hHrate
  let CQ2 : ℝ :=
    Q T + exponentialBarrier (a / Cp ^ 2) (2 * lambda) ((L * CV) ^ 2 / a)
  have hden : 0 < a / Cp ^ 2 - 2 * lambda := sub_pos.mpr hrate
  have hbar0 : 0 ≤ exponentialBarrier (a / Cp ^ 2) (2 * lambda) ((L * CV) ^ 2 / a) := by
    unfold exponentialBarrier
    exact div_nonneg (div_nonneg (sq_nonneg (L * CV)) ha.le) hden.le
  have hCQ2 : 0 ≤ CQ2 := by
    dsimp [CQ2]
    exact add_nonneg (hQ0 T) hbar0
  have hrootQ :
      Real.sqrt (Q t) ≤ Real.sqrt CQ2 * Real.exp (-lambda * (t - T)) := by
    apply sqrt_exponential_energy_bound (hQ0 t) hCQ2
    simpa [CQ2] using hQenv
  have hU := parabolicUpgrade_exponential_rate
    (U := U t) (rootQ := Real.sqrt (Q t)) (H := H t)
    (Cq := Cq) (Ch := Ch) (CQ := Real.sqrt CQ2) (CH := L * CV)
    (lambda := lambda) (T := T) (t := t)
    hCq hCh (Real.sqrt_nonneg _) hCH hrootQ (hHrate t) hChoi
  exact ⟨hVrate t, by simpa [CQ2] using hU⟩

/--
Polynomial full-stabilization rate assembly for the degenerate branch.  The
exponential cell transient is absorbed into the same polynomial rate before
the Choi-type interface is used.
-/
theorem fullPolynomialStabilization_from_analytic_interfaces
    {Vnorm H Q dQ g U : ℝ → ℝ}
    {a Cp CV L Cq Ch b T t : ℝ}
    (ha : 0 < a) (hCp : 0 < Cp) (hCV : 0 ≤ CV) (hL : 0 ≤ L)
    (hCq : 0 ≤ Cq) (hCh : 0 ≤ Ch) (hb : 0 < b)
    (hrate : 2 * b < a / Cp ^ 2)
    (hTt : T ≤ t)
    (hVrate : ∀ tau ∈ Set.Icc T t,
      Vnorm tau ≤ CV * (1 + (tau - T)) ^ (-b))
    (hH0 : ∀ tau ∈ Set.Icc T t, 0 ≤ H tau)
    (hHbyV : ∀ tau ∈ Set.Icc T t, H tau ≤ L * Vnorm tau)
    (hQderiv : ∀ tau ∈ Set.Icc T t, HasDerivAt Q (dQ tau) tau)
    (hQ0 : ∀ tau ∈ Set.Icc T t, 0 ≤ Q tau)
    (hg0 : ∀ tau ∈ Set.Icc T t, 0 ≤ g tau)
    (hPoincare : ∀ tau ∈ Set.Icc T t, Q tau ≤ Cp ^ 2 * g tau ^ 2)
    (henergy : ∀ tau ∈ Set.Icc T t,
      dQ tau + 2 * a * g tau ^ 2 ≤ 2 * H tau * g tau)
    (hChoi : U t ≤ Cq * Real.sqrt (Q t) + Ch * H t) :
    Vnorm t ≤ CV * (1 + (t - T)) ^ (-b) ∧
    U t ≤
      (Cq * Real.sqrt
          (Q T + polynomialBarrier (a / Cp ^ 2) (2 * b) ((L * CV) ^ 2 / a)) +
        Ch * (L * CV)) *
        (1 + (t - T)) ^ (-b) := by
  have htMem : t ∈ Set.Icc T t := ⟨hTt, le_rfl⟩
  have hCH : 0 ≤ L * CV := mul_nonneg hL hCV
  have hHrate : ∀ tau ∈ Set.Icc T t,
      H tau ≤ (L * CV) * (1 + (tau - T)) ^ (-b) := by
    intro tau htau
    calc
      H tau ≤ L * Vnorm tau := hHbyV tau htau
      _ ≤ L * (CV * (1 + (tau - T)) ^ (-b)) :=
        mul_le_mul_of_nonneg_left (hVrate tau htau) hL
      _ = (L * CV) * (1 + (tau - T)) ^ (-b) := by ring
  have hQenv := cellEnergy_polynomialEnvelope_from_gradientRate
    (Q := Q) (dQ := dQ) (g := g) (H := H)
    (a := a) (Cp := Cp) (CH := L * CV) (b := b) (T := T) (t := t)
    ha hCp hCH hb hrate hTt hQderiv hQ0 hg0 hH0 hPoincare henergy hHrate
  let CQ2 : ℝ :=
    Q T + polynomialBarrier (a / Cp ^ 2) (2 * b) ((L * CV) ^ 2 / a)
  have hden : 0 < a / Cp ^ 2 - 2 * b := sub_pos.mpr hrate
  have hbar0 : 0 ≤ polynomialBarrier (a / Cp ^ 2) (2 * b) ((L * CV) ^ 2 / a) := by
    unfold polynomialBarrier
    exact div_nonneg (div_nonneg (sq_nonneg (L * CV)) ha.le) hden.le
  have hCQ2 : 0 ≤ CQ2 := by
    dsimp [CQ2]
    exact add_nonneg (hQ0 T ⟨le_rfl, hTt⟩) hbar0
  have hrootQ :
      Real.sqrt (Q t) ≤ Real.sqrt CQ2 * (1 + (t - T)) ^ (-b) := by
    apply sqrt_polynomial_energy_bound (hQ0 t htMem) hCQ2 hTt
    simpa [CQ2] using hQenv
  have hU := parabolicUpgrade_polynomial_rate
    (U := U t) (rootQ := Real.sqrt (Q t)) (H := H t)
    (Cq := Cq) (Ch := Ch) (CQ := Real.sqrt CQ2) (CH := L * CV)
    (b := b) (T := T) (t := t)
    hCq hCh (Real.sqrt_nonneg _) hCH hrootQ (hHrate t htMem) hChoi
  exact ⟨hVrate t htMem, by simpa [CQ2] using hU⟩

end AMLStabilization
