import Mathlib

namespace AMLStabilization

/-- Local integrating-factor comparison on a finite time interval. -/
theorem local_forcedHomogeneous_exp_bound
    {Y dY : ℝ → ℝ} {a s t : ℝ}
    (ha : 0 < a) (hst : s ≤ t)
    (hY : ∀ τ ∈ Set.Icc s t, HasDerivAt Y (dY τ) τ)
    (hdiss : ∀ τ ∈ Set.Icc s t, dY τ + a * Y τ ≤ 0) :
    Y t ≤ Y s * Real.exp (-a * (t - s)) := by
  let Z : ℝ → ℝ := fun τ => Y τ * Real.exp (a * τ)
  let dZ : ℝ → ℝ := fun τ => Real.exp (a * τ) * (dY τ + a * Y τ)
  have hZderiv : ∀ τ ∈ Set.Icc s t, HasDerivAt Z (dZ τ) τ := by
    intro τ hτ
    have hlin : HasDerivAt (fun x : ℝ => a * x) a τ := hasDerivAt_const_mul a
    have hexp := hlin.exp
    have hmul := (hY τ hτ).mul hexp
    dsimp [Z, dZ]
    apply hmul.congr_deriv
    ring
  have hZcont : ContinuousOn Z (Set.Icc s t) := by
    intro τ hτ
    exact (hZderiv τ hτ).continuousAt.continuousWithinAt
  have hZdiff : DifferentiableOn ℝ Z (interior (Set.Icc s t)) := by
    intro τ hτ
    exact (hZderiv τ (interior_subset hτ)).differentiableAt.differentiableWithinAt
  have hZderivNonpos : ∀ τ ∈ interior (Set.Icc s t), deriv Z τ ≤ 0 := by
    intro τ hτ
    have hτI := interior_subset hτ
    have hz := (hZderiv τ hτI).deriv
    rw [hz]
    dsimp [dZ]
    exact mul_nonpos_of_nonneg_of_nonpos (Real.exp_nonneg _) (hdiss τ hτI)
  have hanti : AntitoneOn Z (Set.Icc s t) :=
    antitoneOn_of_deriv_nonpos (convex_Icc s t) hZcont hZdiff hZderivNonpos
  have hzs : s ∈ Set.Icc s t := ⟨le_rfl, hst⟩
  have hztMem : t ∈ Set.Icc s t := ⟨hst, le_rfl⟩
  have hzt : Z t ≤ Z s := hanti hzs hztMem hst
  dsimp [Z] at hzt
  have het : 0 < Real.exp (a * t) := Real.exp_pos _
  have hdiv : Y t ≤ Y s * Real.exp (a * s) / Real.exp (a * t) :=
    (le_div_iff₀ het).2 (by simpa [mul_assoc] using hzt)
  calc
    Y t ≤ Y s * Real.exp (a * s) / Real.exp (a * t) := hdiv
    _ = Y s * Real.exp (a * s - a * t) := by
      rw [Real.exp_sub]
      ring
    _ = Y s * Real.exp (-a * (t - s)) := by congr 2 <;> ring

/-- Polynomial barrier coefficient for `Q' + aQ <= C(1+t-T)^(-b)`. -/
noncomputable def polynomialBarrier (a b C : ℝ) : ℝ := C / (a - b)

/-- The standard polynomial barrier has the required derivative on `t >= T`. -/
theorem polynomialBarrier_hasDerivAt
    {a b C T t : ℝ}
    (ha : 0 < a) (hb : 0 < b) (hba : b < a) (hTt : T ≤ t) :
    HasDerivAt
      (fun τ : ℝ => polynomialBarrier a b C * (1 + (τ - T)) ^ (-b))
      (-b * polynomialBarrier a b C * (1 + (t - T)) ^ (-b - 1)) t := by
  have hbase : 0 < 1 + (t - T) := by linarith
  have hinner : HasDerivAt (fun τ : ℝ => 1 + (τ - T)) 1 t := by
    simpa using ((hasDerivAt_id t).sub_const T).const_add 1
  have hr := hinner.rpow_const (Or.inl (ne_of_gt hbase)) (p := -b)
  have hc := hr.const_mul (polynomialBarrier a b C)
  apply hc.congr_deriv
  ring

/-- On `t >= T`, the polynomial barrier is a supersolution of the scalar forcing. -/
theorem polynomialBarrier_supersolution
    {a b C T t : ℝ}
    (ha : 0 < a) (hb : 0 < b) (hba : b < a)
    (hC : 0 ≤ C) (hTt : T ≤ t) :
    (-b * polynomialBarrier a b C * (1 + (t - T)) ^ (-b - 1)) +
      a * (polynomialBarrier a b C * (1 + (t - T)) ^ (-b)) ≥
        C * (1 + (t - T)) ^ (-b) := by
  have hab : 0 < a - b := sub_pos.mpr hba
  have hbase : 1 ≤ 1 + (t - T) := by linarith
  have hbase0 : 0 < 1 + (t - T) := lt_of_lt_of_le zero_lt_one hbase
  have hinv : (1 + (t - T))⁻¹ ≤ 1 := by
    exact (inv_le_one₀ hbase0).2 hbase
  have hbar0 : 0 ≤ polynomialBarrier a b C := by
    unfold polynomialBarrier
    exact div_nonneg hC hab.le
  have hfactor : b / (1 + (t - T)) ≤ b := by
    have hmul := mul_le_mul_of_nonneg_left hinv (le_of_lt hb)
    simpa [div_eq_mul_inv] using hmul
  have hpowrel :
      (1 + (t - T)) ^ (-b - 1) =
        (1 + (t - T)) ^ (-b) / (1 + (t - T)) := by
    rw [show -b - 1 = -b + (-1) by ring, Real.rpow_add hbase0]
    rw [Real.rpow_neg_one]
    simp [div_eq_mul_inv]
  have hcoef : (a - b) * polynomialBarrier a b C = C := by
    unfold polynomialBarrier
    field_simp [ne_of_gt hab]
  rw [hpowrel]
  have hpownonneg : 0 ≤ (1 + (t - T)) ^ (-b) := Real.rpow_nonneg hbase0.le _
  have hmultnonneg :
      0 ≤ polynomialBarrier a b C * (1 + (t - T)) ^ (-b) :=
    mul_nonneg hbar0 hpownonneg
  have hdiff : a - b ≤ a - b / (1 + (t - T)) :=
    sub_le_sub_left hfactor a
  calc
    (-b * polynomialBarrier a b C * ((1 + (t - T)) ^ (-b) / (1 + (t - T)))) +
        a * (polynomialBarrier a b C * (1 + (t - T)) ^ (-b)) =
      polynomialBarrier a b C * (1 + (t - T)) ^ (-b) *
        (a - b / (1 + (t - T))) := by ring
    _ ≥ polynomialBarrier a b C * (1 + (t - T)) ^ (-b) * (a - b) := by
      exact mul_le_mul_of_nonneg_left hdiff hmultnonneg
    _ = ((a - b) * polynomialBarrier a b C) * (1 + (t - T)) ^ (-b) := by ring
    _ = C * (1 + (t - T)) ^ (-b) := by rw [hcoef]

/--
Polynomial forcing is inherited by a linearly damped energy.  The exponential
transient and the polynomial barrier are both explicit.
-/
theorem forcedEnergy_polynomial_bound
    {Q dQ : ℝ → ℝ} {a b C T t : ℝ}
    (ha : 0 < a) (hb : 0 < b) (hba : b < a) (hC : 0 ≤ C)
    (hTt : T ≤ t)
    (hQ : ∀ τ ∈ Set.Icc T t, HasDerivAt Q (dQ τ) τ)
    (hforce : ∀ τ ∈ Set.Icc T t,
      dQ τ + a * Q τ ≤ C * (1 + (τ - T)) ^ (-b)) :
    Q t ≤
      (Q T - polynomialBarrier a b C) * Real.exp (-a * (t - T)) +
        polynomialBarrier a b C * (1 + (t - T)) ^ (-b) := by
  let P : ℝ → ℝ := fun τ => polynomialBarrier a b C * (1 + (τ - T)) ^ (-b)
  let dP : ℝ → ℝ := fun τ => -b * polynomialBarrier a b C * (1 + (τ - T)) ^ (-b - 1)
  let Y : ℝ → ℝ := fun τ => Q τ - P τ
  let dY : ℝ → ℝ := fun τ => dQ τ - dP τ
  have hYderiv : ∀ τ ∈ Set.Icc T t, HasDerivAt Y (dY τ) τ := by
    intro τ hτ
    have hp := polynomialBarrier_hasDerivAt
      (a := a) (b := b) (C := C) (T := T) (t := τ) ha hb hba hτ.1
    dsimp [Y, dY, P, dP]
    exact (hQ τ hτ).sub hp
  have hYdiss : ∀ τ ∈ Set.Icc T t, dY τ + a * Y τ ≤ 0 := by
    intro τ hτ
    have hsup := polynomialBarrier_supersolution
      (a := a) (b := b) (C := C) (T := T) (t := τ) ha hb hba hC hτ.1
    dsimp [Y, dY, P, dP]
    linarith [hforce τ hτ]
  have hdec := local_forcedHomogeneous_exp_bound
    (Y := Y) (dY := dY) (a := a) (s := T) (t := t)
    ha hTt hYderiv hYdiss
  dsimp [Y, P] at hdec
  simpa using hdec

end AMLStabilization
