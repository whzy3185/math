import Mathlib
import AMLStabilization.GeneralPolynomialEnergyDecay

namespace AMLStabilization

/-- A convenient nonoptimal coefficient for the fractional dissipation closure. -/
noncomputable def rateGamma (q A B beta M : ℝ) : ℝ :=
  A + B / beta ^ (2 / q) + M

/-- Positivity of the exponent `2/q` and its upper bound by one when `q > 2`. -/
theorem two_div_q_range {q : ℝ} (hq : 2 < q) :
    0 < 2 / q ∧ 2 / q ≤ 1 := by
  have hq0 : 0 < q := lt_trans (by norm_num) hq
  constructor
  · exact div_pos (by norm_num) hq0
  · exact (div_le_one hq0).2 (le_of_lt hq)

/-- The convenient rate coefficient is nonnegative under the natural signs. -/
theorem rateGamma_nonneg
    {q A B beta M : ℝ}
    (hq : 2 < q) (hA : 0 ≤ A) (hB : 0 ≤ B) (hbeta : 0 < beta) (hM : 0 ≤ M) :
    0 ≤ rateGamma q A B beta M := by
  have ha0 := (two_div_q_range hq).1.le
  have hbetapow : 0 < beta ^ (2 / q) := Real.rpow_pos_of_pos hbeta _
  unfold rateGamma
  positivity

/--
The nonlinear coercivity shape
`E <= A Y + B Z^(2/q)`, together with `E <= M` and
`D = Y + beta Z`, yields the fractional dissipation closure
`E <= Gamma D^(2/q)`.  This is the key algebraic step behind the
arbitrary-order polynomial branch.
-/
theorem nonlinearCoercivity_to_fractionalDissipation
    {E Y Z D A B beta M q : ℝ}
    (hq : 2 < q)
    (hE : 0 ≤ E) (hY : 0 ≤ Y) (hZ : 0 ≤ Z)
    (hA : 0 ≤ A) (hB : 0 ≤ B) (hbeta : 0 < beta) (hM : 0 ≤ M)
    (hD : D = Y + beta * Z)
    (hEM : E ≤ M)
    (hcoerc : E ≤ A * Y + B * Z ^ (2 / q)) :
    E ≤ rateGamma q A B beta M * D ^ (2 / q) := by
  obtain ⟨ha0pos, ha1⟩ := two_div_q_range hq
  have ha0 : 0 ≤ 2 / q := ha0pos.le
  have hD0 : 0 ≤ D := by rw [hD]; positivity
  have hYle : Y ≤ D := by rw [hD]; nlinarith [mul_nonneg (le_of_lt hbeta) hZ]
  have hbetaZle : beta * Z ≤ D := by rw [hD]; linarith
  have hZle : Z ≤ D / beta := by
    apply (le_div_iff₀ hbeta).2
    simpa [mul_comm] using hbetaZle
  have hZpow : Z ^ (2 / q) ≤ D ^ (2 / q) / beta ^ (2 / q) := by
    have h := Real.rpow_le_rpow hZ hZle ha0
    rw [Real.div_rpow hD0 (le_of_lt hbeta) (2 / q)] at h
    exact h
  have hG0 := rateGamma_nonneg hq hA hB hbeta hM
  by_cases hsmall : D ≤ 1
  · have hDself : D ≤ D ^ (2 / q) :=
      Real.self_le_rpow_of_le_one hD0 hsmall ha1
    have hYpow : Y ≤ D ^ (2 / q) := hYle.trans hDself
    have htermA : A * Y ≤ A * D ^ (2 / q) :=
      mul_le_mul_of_nonneg_left hYpow hA
    have htermB : B * Z ^ (2 / q) ≤ B * (D ^ (2 / q) / beta ^ (2 / q)) :=
      mul_le_mul_of_nonneg_left hZpow hB
    have hcoeff : A + B / beta ^ (2 / q) ≤ rateGamma q A B beta M := by
      unfold rateGamma
      linarith
    calc
      E ≤ A * Y + B * Z ^ (2 / q) := hcoerc
      _ ≤ A * D ^ (2 / q) + B * (D ^ (2 / q) / beta ^ (2 / q)) :=
        add_le_add htermA htermB
      _ = (A + B / beta ^ (2 / q)) * D ^ (2 / q) := by ring
      _ ≤ rateGamma q A B beta M * D ^ (2 / q) :=
        mul_le_mul_of_nonneg_right hcoeff (Real.rpow_nonneg hD0 _)
  · have hDone : 1 ≤ D := le_of_not_ge hsmall
    have hDpowone : 1 ≤ D ^ (2 / q) := Real.one_le_rpow hDone ha0
    have hMleG : M ≤ rateGamma q A B beta M := by
      unfold rateGamma
      have hbetapow : 0 < beta ^ (2 / q) := Real.rpow_pos_of_pos hbeta _
      have hfrac : 0 ≤ B / beta ^ (2 / q) := div_nonneg hB hbetapow.le
      linarith
    have hGle : rateGamma q A B beta M ≤
        rateGamma q A B beta M * D ^ (2 / q) := by
      nlinarith [mul_nonneg hG0 (sub_nonneg.mpr hDpowone)]
    exact hEM.trans (hMleG.trans hGle)

/-- Raising the fractional closure to `q/2` converts it into a linear bound by `D`. -/
theorem fractionalDissipation_to_superquadratic
    {E D Gamma q : ℝ}
    (hq : 2 < q) (hE : 0 ≤ E) (hD : 0 ≤ D) (hGamma : 0 < Gamma)
    (hfrac : E ≤ Gamma * D ^ (2 / q)) :
    Gamma ^ (-q / 2) * E ^ (q / 2) ≤ D := by
  have hq0 : 0 < q := lt_trans (by norm_num) hq
  have hhalf : 0 ≤ q / 2 := by positivity
  have hpow := Real.rpow_le_rpow hE hfrac hhalf
  have hprodnonneg : 0 ≤ Gamma * D ^ (2 / q) :=
    mul_nonneg (le_of_lt hGamma) (Real.rpow_nonneg hD _)
  have hexp : (2 / q) * (q / 2) = 1 := by
    field_simp [ne_of_gt hq0]
  have hrhs : (Gamma * D ^ (2 / q)) ^ (q / 2) = Gamma ^ (q / 2) * D := by
    rw [Real.mul_rpow (le_of_lt hGamma) (Real.rpow_nonneg hD _)]
    rw [← Real.rpow_mul hD, hexp, Real.rpow_one]
  rw [hrhs] at hpow
  have hscale0 : 0 ≤ Gamma ^ (-q / 2) := Real.rpow_nonneg (le_of_lt hGamma) _
  have hscaled := mul_le_mul_of_nonneg_left hpow hscale0
  have hcancel : Gamma ^ (-q / 2) * Gamma ^ (q / 2) = 1 := by
    have hexp0 : -q / 2 + q / 2 = 0 := by ring
    rw [← Real.rpow_add hGamma, hexp0, Real.rpow_zero]
  calc
    Gamma ^ (-q / 2) * E ^ (q / 2) ≤
        Gamma ^ (-q / 2) * (Gamma ^ (q / 2) * D) := hscaled
    _ = D := by rw [← mul_assoc, hcancel, one_mul]

/-- The PDE energy inequality plus fractional closure yields a scalar Bihari inequality. -/
theorem fractionalEnergy_to_qDissipation
    {dE E D Gamma q : ℝ}
    (hq : 2 < q) (hE : 0 ≤ E) (hD : 0 ≤ D) (hGamma : 0 < Gamma)
    (hfrac : E ≤ Gamma * D ^ (2 / q))
    (henergy : dE + 2 * D ≤ 0) :
    dE + 2 * Gamma ^ (-q / 2) * E ^ (q / 2) ≤ 0 := by
  have hsuper := fractionalDissipation_to_superquadratic hq hE hD hGamma hfrac
  linarith

/--
Time-dependent arbitrary-`q` rate assembly.  Once the PDE supplies
`E' + 2D <= 0` and the fractional coercivity closure, Lean derives the
explicit polynomial decay formula.
-/
theorem fractionalEnergy_to_polynomialDecay
    {E dE D : ℝ → ℝ} {Gamma q s t : ℝ}
    (hq : 2 < q) (hGamma : 0 < Gamma)
    (hEderiv : ∀ tau, HasDerivAt E (dE tau) tau)
    (hEpos : ∀ tau, 0 < E tau)
    (hD : ∀ tau, 0 ≤ D tau)
    (hfrac : ∀ tau, E tau ≤ Gamma * D tau ^ (2 / q))
    (henergy : ∀ tau, dE tau + 2 * D tau ≤ 0)
    (hst : s ≤ t) :
    E t ≤
      (E s ^ (-(q - 2) / 2) +
          (q - 2) * Gamma ^ (-q / 2) * (t - s)) ^ (-2 / (q - 2)) := by
  have hc : 0 ≤ Gamma ^ (-q / 2) := Real.rpow_nonneg (le_of_lt hGamma) _
  have hdiss : ∀ tau, dE tau + 2 * Gamma ^ (-q / 2) * E tau ^ (q / 2) ≤ 0 := by
    intro tau
    exact fractionalEnergy_to_qDissipation hq (le_of_lt (hEpos tau)) (hD tau)
      hGamma (hfrac tau) (henergy tau)
  exact energy_le_rpow_of_q_dissipation hq hc hEderiv hEpos hdiss hst

end AMLStabilization
