import Mathlib
import AMLStabilization.GeneralPolynomialEnergyDecay
import AMLStabilization.ZeroEnergyBranch

namespace AMLStabilization

/-- The transformed energy is monotone on a finite interval under local positive-energy hypotheses. -/
theorem powerEnergyShift_monotoneOn
    {E dE : ℝ → ℝ} {theta c s t : ℝ}
    (htheta : 0 < theta)
    (hc : 0 ≤ c)
    (hst : s ≤ t)
    (hE : ∀ tau ∈ Set.Icc s t, HasDerivAt E (dE tau) tau)
    (hpos : ∀ tau ∈ Set.Icc s t, 0 < E tau)
    (hdiss : ∀ tau ∈ Set.Icc s t,
      dE tau + 2 * c * E tau ^ (1 + theta / 2) ≤ 0) :
    MonotoneOn (powerEnergyShift theta c E) (Set.Icc s t) := by
  let dShift : ℝ → ℝ := fun tau =>
    dE tau * (-theta / 2) * E tau ^ (-theta / 2 - 1) - theta * c
  have hShiftDeriv : ∀ tau ∈ Set.Icc s t,
      HasDerivAt (powerEnergyShift theta c E) (dShift tau) tau := by
    intro tau htau
    unfold powerEnergyShift
    have hrpow := (hE tau htau).rpow_const
      (Or.inl (ne_of_gt (hpos tau htau))) (p := -theta / 2)
    have hlin : HasDerivAt (fun x : ℝ => theta * c * x) (theta * c) tau :=
      hasDerivAt_const_mul (theta * c)
    exact hrpow.sub hlin
  have hcont : ContinuousOn (powerEnergyShift theta c E) (Set.Icc s t) := by
    intro tau htau
    exact (hShiftDeriv tau htau).continuousAt.continuousWithinAt
  have hdiff : DifferentiableOn ℝ (powerEnergyShift theta c E)
      (interior (Set.Icc s t)) := by
    intro tau htau
    exact (hShiftDeriv tau (interior_subset htau)).differentiableAt.differentiableWithinAt
  have hderivNonneg : ∀ tau ∈ interior (Set.Icc s t),
      0 ≤ deriv (powerEnergyShift theta c E) tau := by
    intro tau htau
    have htauI : tau ∈ Set.Icc s t := interior_subset htau
    have hEt : 0 < E tau := hpos tau htauI
    have hpowpos : 0 < E tau ^ (-theta / 2 - 1) := Real.rpow_pos_of_pos hEt _
    have hfac : 0 < (theta / 2) * E tau ^ (-theta / 2 - 1) :=
      mul_pos (by linarith) hpowpos
    have hnegd : 2 * c * E tau ^ (1 + theta / 2) ≤ -dE tau := by
      linarith [hdiss tau htauI]
    have hexp : (1 + theta / 2) + (-theta / 2 - 1) = 0 := by ring
    have hprod :
        E tau ^ (1 + theta / 2) * E tau ^ (-theta / 2 - 1) = 1 := by
      rw [← Real.rpow_add hEt, hexp, Real.rpow_zero]
    have hmul := mul_le_mul_of_nonneg_right hnegd (le_of_lt hfac)
    have hleft :
        (2 * c * E tau ^ (1 + theta / 2)) *
            ((theta / 2) * E tau ^ (-theta / 2 - 1)) = theta * c := by
      calc
        _ = theta * c *
            (E tau ^ (1 + theta / 2) * E tau ^ (-theta / 2 - 1)) := by ring
        _ = theta * c := by rw [hprod, mul_one]
    rw [hleft] at hmul
    have hright :
        (-dE tau) * ((theta / 2) * E tau ^ (-theta / 2 - 1)) =
          dE tau * (-theta / 2) * E tau ^ (-theta / 2 - 1) := by ring
    rw [hright] at hmul
    have hdshift : 0 ≤ dShift tau := by
      dsimp [dShift]
      exact sub_nonneg.mpr hmul
    rw [(hShiftDeriv tau htauI).deriv]
    exact hdshift
  exact monotoneOn_of_deriv_nonneg (convex_Icc s t) hcont hdiff hderivNonneg

/-- Local transformed-energy lower bound on `[s,t]`. -/
theorem powerEnergy_lower_of_superquadratic_dissipation_on_interval
    {E dE : ℝ → ℝ} {theta c s t : ℝ}
    (htheta : 0 < theta)
    (hc : 0 ≤ c)
    (hst : s ≤ t)
    (hE : ∀ tau ∈ Set.Icc s t, HasDerivAt E (dE tau) tau)
    (hpos : ∀ tau ∈ Set.Icc s t, 0 < E tau)
    (hdiss : ∀ tau ∈ Set.Icc s t,
      dE tau + 2 * c * E tau ^ (1 + theta / 2) ≤ 0) :
    E s ^ (-theta / 2) + theta * c * (t - s) ≤ E t ^ (-theta / 2) := by
  have hmono := powerEnergyShift_monotoneOn htheta hc hst hE hpos hdiss
  have hsMem : s ∈ Set.Icc s t := ⟨le_rfl, hst⟩
  have htMem : t ∈ Set.Icc s t := ⟨hst, le_rfl⟩
  have h := hmono hsMem htMem hst
  dsimp [powerEnergyShift] at h
  linarith

/-- Local arbitrary-order Bihari estimate on a finite interval. -/
theorem energy_le_rpow_of_superquadratic_dissipation_on_interval
    {E dE : ℝ → ℝ} {theta c s t : ℝ}
    (htheta : 0 < theta)
    (hc : 0 ≤ c)
    (hst : s ≤ t)
    (hE : ∀ tau ∈ Set.Icc s t, HasDerivAt E (dE tau) tau)
    (hpos : ∀ tau ∈ Set.Icc s t, 0 < E tau)
    (hdiss : ∀ tau ∈ Set.Icc s t,
      dE tau + 2 * c * E tau ^ (1 + theta / 2) ≤ 0) :
    E t ≤
      (E s ^ (-theta / 2) + theta * c * (t - s)) ^ (-2 / theta) := by
  have hlow := powerEnergy_lower_of_superquadratic_dissipation_on_interval
    htheta hc hst hE hpos hdiss
  have hsMem : s ∈ Set.Icc s t := ⟨le_rfl, hst⟩
  have htMem : t ∈ Set.Icc s t := ⟨hst, le_rfl⟩
  have hdt : 0 ≤ t - s := sub_nonneg.mpr hst
  have hEsPow : 0 < E s ^ (-theta / 2) :=
    Real.rpow_pos_of_pos (hpos s hsMem) _
  have hterm : 0 ≤ theta * c * (t - s) :=
    mul_nonneg (mul_nonneg (le_of_lt htheta) hc) hdt
  let A : ℝ := E s ^ (-theta / 2) + theta * c * (t - s)
  have hA : 0 < A := by
    dsimp [A]
    linarith
  have hposdiv : 0 ≤ (2 : ℝ) / theta :=
    div_nonneg (by norm_num) (le_of_lt htheta)
  have hz : -2 / theta ≤ 0 := by
    rw [neg_div]
    exact neg_nonpos.mpr hposdiv
  have hrpow := Real.rpow_le_rpow_of_nonpos hA hlow hz
  have htheta0 : theta ≠ 0 := ne_of_gt htheta
  have hexp : (-theta / 2) * (-2 / theta) = 1 := by
    field_simp [htheta0]
  have hsimp : (E t ^ (-theta / 2)) ^ (-2 / theta) = E t := by
    rw [← Real.rpow_mul (le_of_lt (hpos t htMem)), hexp, Real.rpow_one]
  rw [hsimp] at hrpow
  simpa [A] using hrpow

/-- Local `q>2` version matching the manuscript's damping exponent. -/
theorem energy_le_rpow_of_q_dissipation_on_interval
    {E dE : ℝ → ℝ} {q c s t : ℝ}
    (hq : 2 < q)
    (hc : 0 ≤ c)
    (hst : s ≤ t)
    (hE : ∀ tau ∈ Set.Icc s t, HasDerivAt E (dE tau) tau)
    (hpos : ∀ tau ∈ Set.Icc s t, 0 < E tau)
    (hdiss : ∀ tau ∈ Set.Icc s t,
      dE tau + 2 * c * E tau ^ (q / 2) ≤ 0) :
    E t ≤
      (E s ^ (-(q - 2) / 2) + (q - 2) * c * (t - s)) ^ (-2 / (q - 2)) := by
  have htheta : 0 < q - 2 := by linarith
  have hexp : 1 + (q - 2) / 2 = q / 2 := by ring
  have hdiss' : ∀ tau ∈ Set.Icc s t,
      dE tau + 2 * c * E tau ^ (1 + (q - 2) / 2) ≤ 0 := by
    intro tau htau
    rw [hexp]
    exact hdiss tau htau
  exact energy_le_rpow_of_superquadratic_dissipation_on_interval
    htheta hc hst hE hpos hdiss'

/--
Arbitrary-`q>2` Bihari decay for a merely nonnegative energy.  If the energy
hits zero on `[s,t]`, antitonicity forces the terminal energy to remain zero;
otherwise the local positive-energy theorem applies.
-/
theorem energy_le_rpow_of_q_dissipation_nonnegative
    {E dE : ℝ → ℝ} {q c s t : ℝ}
    (hq : 2 < q)
    (hc : 0 ≤ c)
    (hE : ∀ tau, HasDerivAt E (dE tau) tau)
    (hEnonneg : ∀ tau, 0 ≤ E tau)
    (hdiss : ∀ tau, dE tau + 2 * c * E tau ^ (q / 2) ≤ 0)
    (hst : s ≤ t) :
    E t ≤
      (E s ^ (-(q - 2) / 2) + (q - 2) * c * (t - s)) ^ (-2 / (q - 2)) := by
  by_cases hzero : ∃ r ∈ Set.Icc s t, E r = 0
  · rcases hzero with ⟨r, hrI, hr0⟩
    let D : ℝ → ℝ := fun tau => c * E tau ^ (q / 2)
    have hD0 : ∀ tau, 0 ≤ D tau := by
      intro tau
      dsimp [D]
      exact mul_nonneg hc (Real.rpow_nonneg (hEnonneg tau) _)
    have henergyD : ∀ tau, dE tau + 2 * D tau ≤ 0 := by
      intro tau
      dsimp [D]
      convert hdiss tau using 1 <;> ring
    have hEt0 := energy_eq_zero_after_hit hE hEnonneg hD0 henergyD hr0 hrI.2
    rw [hEt0]
    have hbase0 : 0 ≤
        E s ^ (-(q - 2) / 2) + (q - 2) * c * (t - s) := by
      apply add_nonneg
      · exact Real.rpow_nonneg (hEnonneg s) _
      · exact mul_nonneg
          (mul_nonneg (sub_nonneg.mpr (le_of_lt hq)) hc)
          (sub_nonneg.mpr hst)
    exact Real.rpow_nonneg hbase0 _
  · have hposI : ∀ tau ∈ Set.Icc s t, 0 < E tau := by
      intro tau htau
      have hne : E tau ≠ 0 := by
        intro hz
        exact hzero ⟨tau, htau, hz⟩
      exact lt_of_le_of_ne (hEnonneg tau) (Ne.symm hne)
    exact energy_le_rpow_of_q_dissipation_on_interval
      hq hc hst (fun tau _ => hE tau) hposI (fun tau _ => hdiss tau)

end AMLStabilization
