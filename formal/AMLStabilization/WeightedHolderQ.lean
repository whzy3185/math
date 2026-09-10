import Mathlib

open MeasureTheory

namespace AMLStabilization

/-- Hölder conjugate exponent associated with `q > 1`. -/
noncomputable def qConjugate (q : ℝ) : ℝ := q / (q - 1)

/-- The explicit conjugate exponent `q/(q-1)` is Hölder-conjugate to `q`. -/
theorem q_holderConjugate_qConjugate
    {q : ℝ} (hq : 1 < q) :
    q.HolderConjugate (qConjugate q) := by
  rw [Real.holderConjugate_iff]
  refine ⟨hq, ?_⟩
  unfold qConjugate
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans (by norm_num) hq)
  have hqm1 : q - 1 ≠ 0 := ne_of_gt (sub_pos.mpr hq)
  field_simp [hq0, hqm1]
  ring

/-- The reciprocal of the conjugate exponent is `1 - 1/q`. -/
theorem inv_qConjugate
    {q : ℝ} (hq : 1 < q) :
    1 / qConjugate q = 1 - 1 / q := by
  unfold qConjugate
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans (by norm_num) hq)
  have hqm1 : q - 1 ≠ 0 := ne_of_gt (sub_pos.mpr hq)
  field_simp [hq0, hqm1]

/-- Pointwise splitting of the weighted first moment into Hölder factors. -/
theorem weightedHolder_product_identity
    {rho f q : ℝ} (hrho : 0 ≤ rho) (hq : 0 < q) :
    rho * |f| =
      (rho ^ (1 / q) * |f|) * rho ^ (1 - 1 / q) := by
  have hexp : 1 / q + (1 - 1 / q) = 1 := by ring
  have hrpow :
      rho ^ (1 / q) * rho ^ (1 - 1 / q) = rho := by
    rw [← Real.rpow_of_add_eq hrho one_ne_zero hexp, Real.rpow_one]
  calc
    rho * |f| = (rho ^ (1 / q) * rho ^ (1 - 1 / q)) * |f| := by rw [hrpow]
    _ = (rho ^ (1 / q) * |f|) * rho ^ (1 - 1 / q) := by ring

/-- The `q`-power of the first Hölder factor is exactly `rho * |f|^q`. -/
theorem weightedHolder_firstFactor_rpow
    {rho f q : ℝ} (hrho : 0 ≤ rho) (hq : 0 < q) :
    (rho ^ (1 / q) * |f|) ^ q = rho * |f| ^ q := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  rw [Real.mul_rpow (Real.rpow_nonneg hrho _) (abs_nonneg f)]
  rw [← Real.rpow_mul hrho]
  have hexp : (1 / q) * q = 1 := by field_simp [hq0]
  rw [hexp, Real.rpow_one]

/-- The conjugate power of the second Hölder factor is exactly `rho`. -/
theorem weightedHolder_secondFactor_rpow
    {rho q : ℝ} (hrho : 0 ≤ rho) (hq : 1 < q) :
    (rho ^ (1 - 1 / q)) ^ qConjugate q = rho := by
  have hq0 : q ≠ 0 := ne_of_gt (lt_trans (by norm_num) hq)
  have hqm1 : q - 1 ≠ 0 := ne_of_gt (sub_pos.mpr hq)
  rw [← Real.rpow_mul hrho]
  have hexp : (1 - 1 / q) * qConjugate q = 1 := by
    unfold qConjugate
    field_simp [hq0, hqm1]
  rw [hexp, Real.rpow_one]

/--
Weighted Hölder estimate for arbitrary real `q > 1`, with all `MemLp`
hypotheses derived from integrability of `rho` and `rho*|f|^q`.
-/
theorem weightedFirstMoment_holder
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {rho f : Omega → ℝ}
    {m q : ℝ}
    (hq : 1 < q)
    (hrho_nonneg : ∀ x, 0 ≤ rho x)
    (hrho_meas : AEStronglyMeasurable rho mu)
    (hf_meas : AEStronglyMeasurable f mu)
    (hrho_int : Integrable rho mu)
    (hweighted_int : Integrable (fun x => rho x * |f x| ^ q) mu)
    (hmass : (∫ x, rho x ∂mu) = m) :
    |∫ x, rho x * f x ∂mu| ≤
      (∫ x, rho x * |f x| ^ q ∂mu) ^ (1 / q) * m ^ (1 - 1 / q) := by
  let a : Omega → ℝ := fun x => rho x ^ (1 / q) * |f x|
  let b : Omega → ℝ := fun x => rho x ^ (1 - 1 / q)
  have hq0 : 0 < q := lt_trans (by norm_num) hq
  have hqc : 1 < qConjugate q := (q_holderConjugate_qConjugate hq).symm.lt
  have hqc0 : 0 < qConjugate q := lt_trans (by norm_num) hqc
  have h1q : 0 ≤ 1 / q := by positivity
  have hrest : 0 ≤ 1 - 1 / q := by
    apply sub_nonneg.mpr
    exact (div_le_one hq0).2 (le_of_lt hq)
  have ha_nonneg : ∀ x, 0 ≤ a x := fun x =>
    mul_nonneg (Real.rpow_nonneg (hrho_nonneg x) _) (abs_nonneg _)
  have hb_nonneg : ∀ x, 0 ≤ b x := fun x => Real.rpow_nonneg (hrho_nonneg x) _
  have ha_meas : AEStronglyMeasurable a mu := by
    dsimp [a]
    fun_prop
  have hb_meas : AEStronglyMeasurable b mu := by
    dsimp [b]
    fun_prop
  have haLp : MemLp a (ENNReal.ofReal q) mu := by
    apply (integrable_norm_rpow_iff ha_meas
      (ENNReal.ofReal_ne_zero_iff.mpr hq0) (by simp)).mp
    have heq : (fun x => |a x| ^ q) = fun x => rho x * |f x| ^ q := by
      funext x
      rw [abs_of_nonneg (ha_nonneg x)]
      exact weightedHolder_firstFactor_rpow (hrho_nonneg x) hq0
    simpa [ENNReal.toReal_ofReal hq0.le, Real.norm_eq_abs, heq] using hweighted_int
  have hbLp : MemLp b (ENNReal.ofReal (qConjugate q)) mu := by
    apply (integrable_norm_rpow_iff hb_meas
      (ENNReal.ofReal_ne_zero_iff.mpr hqc0) (by simp)).mp
    have heq : (fun x => |b x| ^ qConjugate q) = rho := by
      funext x
      rw [abs_of_nonneg (hb_nonneg x)]
      exact weightedHolder_secondFactor_rpow (hrho_nonneg x) hq
    simpa [ENNReal.toReal_ofReal hqc0.le, Real.norm_eq_abs, heq] using hrho_int
  have hholder := integral_mul_le_Lp_mul_Lq_of_nonneg
    (μ := mu) (p := q) (q := qConjugate q)
    (q_holderConjugate_qConjugate hq)
    (f := a) (g := b)
    (ae_of_all mu ha_nonneg) (ae_of_all mu hb_nonneg) haLp hbLp
  have hab : (fun x => a x * b x) = fun x => rho x * |f x| := by
    funext x
    symm
    exact weightedHolder_product_identity (hrho_nonneg x) hq0
  have haPow : (fun x => a x ^ q) = fun x => rho x * |f x| ^ q := by
    funext x
    exact weightedHolder_firstFactor_rpow (hrho_nonneg x) hq0
  have hbPow : (fun x => b x ^ qConjugate q) = rho := by
    funext x
    exact weightedHolder_secondFactor_rpow (hrho_nonneg x) hq
  calc
    |∫ x, rho x * f x ∂mu| = ‖∫ x, rho x * f x ∂mu‖ := by
      simp [Real.norm_eq_abs]
    _ ≤ ∫ x, ‖rho x * f x‖ ∂mu := norm_integral_le_integral_norm _
    _ = ∫ x, rho x * |f x| ∂mu := by
      apply integral_congr_ae
      filter_upwards with x
      rw [norm_mul, Real.norm_of_nonneg (hrho_nonneg x), Real.norm_eq_abs]
    _ = ∫ x, a x * b x ∂mu := by rw [hab]
    _ ≤ (∫ x, a x ^ q ∂mu) ^ (1 / q) *
        (∫ x, b x ^ qConjugate q ∂mu) ^ (1 / qConjugate q) := hholder
    _ = (∫ x, rho x * |f x| ^ q ∂mu) ^ (1 / q) *
        m ^ (1 - 1 / q) := by
      rw [haPow, hbPow, hmass, inv_qConjugate hq]

end AMLStabilization
