import Mathlib
import AMLStabilization.NonlinearIntegralCoercivity
import AMLStabilization.GeneralSignalEnergyIdentityQ
import AMLStabilization.GeneralRateAssembly
import AMLStabilization.LocalPolynomialEnergyDecay

open MeasureTheory

namespace AMLStabilization

/--
End-to-end arbitrary-`q>2` weighted-damping signal decay for a nonnegative
energy.  Unlike the earlier positive-energy endpoint, this theorem allows the
energy to hit zero: the local Bihari/zero-tail dichotomy is handled internally.
All weighted Holder, nonlinear mass-weighted coercivity, reaction dissipation,
fractional closure, and scalar decay steps are kernel-checked.  The only named
analytic interfaces are Poincare and the concrete PDE energy/Green identities.
-/
theorem generalWeightedDamping_polynomialDecay_nonnegative_from_interfaces
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega}
    {u w wt lap R : ℝ → Omega → ℝ}
    {wbar E dE grad : ℝ → ℝ}
    {m K Cp V beta q M s t : ℝ}
    (hq : 2 < q)
    (hm : 0 < m)
    (hK : 0 ≤ K)
    (hCp : 0 < Cp)
    (hV : 0 ≤ V)
    (hbeta : 0 < beta)
    (hM : 0 ≤ M)
    (hEderiv : ∀ tau, HasDerivAt E (dE tau) tau)
    (hEvalue : ∀ tau, E tau = (∫ x, w tau x ^ 2 ∂mu))
    (hEnonneg : ∀ tau, 0 ≤ E tau)
    (hEbound : ∀ tau, E tau ≤ M)
    (huNonneg : ∀ tau x, 0 ≤ u tau x)
    (hgradNonneg : ∀ tau, 0 ≤ grad tau)
    (huMeas : ∀ tau, AEStronglyMeasurable (u tau) mu)
    (hwMeas : ∀ tau, AEStronglyMeasurable (w tau) mu)
    (huInt : ∀ tau, Integrable (u tau) mu)
    (huwInt : ∀ tau, Integrable (fun x => u tau x * w tau x) mu)
    (hmass : ∀ tau, (∫ x, u tau x ∂mu) = m)
    (huL2 : ∀ tau, MemLp (u tau) 2 mu)
    (hdevL2 : ∀ tau, MemLp (fun x => w tau x - wbar tau) 2 mu)
    (huL2bound : ∀ tau, Real.sqrt (∫ x, u tau x ^ 2 ∂mu) ≤ K)
    (hwInt : ∀ tau, Integrable (w tau) mu)
    (hw2Int : ∀ tau, Integrable (fun x => w tau x ^ 2) mu)
    (honeInt : Integrable (fun _ : Omega => (1 : ℝ)) mu)
    (hvol : (∫ _ : Omega, (1 : ℝ) ∂mu) = V)
    (hmean : ∀ tau, (∫ x, w tau x ∂mu) = V * wbar tau)
    (hPoincare : ∀ tau,
      Real.sqrt (∫ x, (w tau x - wbar tau) ^ 2 ∂mu) ≤ Cp * grad tau)
    (hweightedInt : ∀ tau,
      Integrable (fun x => u tau x * |w tau x| ^ q) mu)
    (hreactionInt : ∀ tau,
      Integrable (fun x => u tau x * (w tau x * R tau x)) mu)
    (hpoint : ∀ tau x,
      w tau x * R tau x ≤ -beta * |w tau x| ^ q)
    (hEnergyDerivative : ∀ tau,
      dE tau = 2 * (∫ x, w tau x * wt tau x ∂mu))
    (hPDEPairing : ∀ tau,
      (∫ x, w tau x * wt tau x ∂mu) =
        (∫ x, w tau x * lap tau x ∂mu) +
          (∫ x, u tau x * (w tau x * R tau x) ∂mu))
    (hGreen : ∀ tau,
      (∫ x, w tau x * lap tau x ∂mu) = -(grad tau) ^ 2)
    (hst : s ≤ t) :
    E t ≤
      (E s ^ (-(q - 2) / 2) +
        (q - 2) *
          (rateGamma q
            (nonlinearMassWeightedA Cp V K m)
            (nonlinearMassWeightedB V m q) beta M) ^ (-q / 2) *
          (t - s)) ^ (-2 / (q - 2)) := by
  let weighted : ℝ → ℝ := fun tau => ∫ x, u tau x * |w tau x| ^ q ∂mu
  let gradSq : ℝ → ℝ := fun tau => (grad tau) ^ 2
  let A : ℝ := nonlinearMassWeightedA Cp V K m
  let B : ℝ := nonlinearMassWeightedB V m q
  let Gamma : ℝ := rateGamma q A B beta M
  let D : ℝ → ℝ := fun tau => gradSq tau + beta * weighted tau
  have hqge : 2 ≤ q := le_of_lt hq
  have hgradSq : ∀ tau, 0 ≤ gradSq tau := fun tau => sq_nonneg (grad tau)
  have hweighted : ∀ tau, 0 ≤ weighted tau := by
    intro tau
    exact integral_nonneg
      (fun x => mul_nonneg (huNonneg tau x) (Real.rpow_nonneg (abs_nonneg _) _))
  obtain ⟨hA0, hB0⟩ := nonlinearMassWeighted_coefficients_nonneg
    hCp.le hV hK hm (lt_trans (by norm_num) hq)
  have hApos : 0 < A := by
    dsimp [A, nonlinearMassWeightedA]
    have hm2 : 0 < m ^ 2 := pow_pos hm 2
    have hfrac0 : 0 ≤ 2 * V * K ^ 2 / m ^ 2 := by positivity
    have hbracket : 0 < 1 + 2 * V * K ^ 2 / m ^ 2 := by linarith
    exact mul_pos (pow_pos hCp 2) hbracket
  have hcoerc : ∀ tau,
      E tau ≤ A * gradSq tau + B * weighted tau ^ (2 / q) := by
    intro tau
    have hc := integralNonlinearMassWeightedCoercivity
      (mu := mu) (rho := u tau) (f := w tau)
      (m := m) (K := K) (Cp := Cp) (grad := grad tau)
      (fbar := wbar tau) (V := V) (q := q)
      hqge hm hK hCp.le (hgradNonneg tau) hV
      (huNonneg tau) (huMeas tau) (hwMeas tau)
      (huInt tau) (huwInt tau) (hweightedInt tau) (hmass tau)
      (huL2 tau) (hdevL2 tau) (huL2bound tau)
      (hwInt tau) (hw2Int tau) honeInt hvol (hmean tau) (hPoincare tau)
    rw [hEvalue tau]
    simpa [A, B, gradSq, weighted] using hc
  have henergy : ∀ tau, dE tau + 2 * D tau ≤ 0 := by
    intro tau
    have he := signalEnergyInequality_q_from_integralPDE
      (mu := mu) (u := u tau) (w := w tau) (wt := wt tau)
      (lap := lap tau) (R := R tau)
      (dE := dE tau) (gradSq := gradSq tau) (beta := beta) (q := q)
      (huNonneg tau) (hpoint tau) (hreactionInt tau) (hweightedInt tau)
      (hEnergyDerivative tau) (hPDEPairing tau)
      (by simpa [gradSq] using hGreen tau)
    simpa [D, weighted] using he
  have hD0 : ∀ tau, 0 ≤ D tau := by
    intro tau
    dsimp [D]
    exact add_nonneg (hgradSq tau)
      (mul_nonneg hbeta.le (hweighted tau))
  have hGammaPos : 0 < Gamma := by
    have hbetapow : 0 < beta ^ (2 / q) := Real.rpow_pos_of_pos hbeta _
    have hBfrac0 : 0 ≤ B / beta ^ (2 / q) := div_nonneg hB0 hbetapow.le
    dsimp [Gamma, rateGamma]
    linarith
  have hfrac : ∀ tau, E tau ≤ Gamma * D tau ^ (2 / q) := by
    intro tau
    exact nonlinearCoercivity_to_fractionalDissipation
      hq (hEnonneg tau) (hgradSq tau) (hweighted tau)
      hA0 hB0 hbeta hM
      (by rfl) (hEbound tau) (hcoerc tau)
  have hdiss : ∀ tau,
      dE tau + 2 * Gamma ^ (-q / 2) * E tau ^ (q / 2) ≤ 0 := by
    intro tau
    exact fractionalEnergy_to_qDissipation hq (hEnonneg tau) (hD0 tau)
      hGammaPos (hfrac tau) (henergy tau)
  have hc : 0 ≤ Gamma ^ (-q / 2) :=
    Real.rpow_nonneg hGammaPos.le _
  have hpoly := energy_le_rpow_of_q_dissipation_nonnegative
    (E := E) (dE := dE) (q := q) (c := Gamma ^ (-q / 2))
    (s := s) (t := t) hq hc hEderiv hEnonneg hdiss hst
  simpa [Gamma, A, B] using hpoly

end AMLStabilization
