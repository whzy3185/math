import Mathlib

open MeasureTheory Real Set intervalIntegral Filter

namespace AMLStabilization

private lemma intervalFtcSub
    {h : ℝ} {f f' : ℝ → ℝ}
    (hf : ∀ x ∈ Icc 0 h, HasDerivAt f (f' x) x)
    (hf'_cont : ContinuousOn f' (Icc 0 h))
    {x y : ℝ} (hx : x ∈ Icc 0 h) (hy : y ∈ Icc 0 h) :
    f x - f y = ∫ t in y..x, f' t := by
  have huIcc : uIcc y x ⊆ Icc 0 h := uIcc_subset_Icc hy hx
  rw [eq_comm]
  exact integral_eq_sub_of_hasDerivAt
    (fun z hz => hf z (huIcc hz))
    ((hf'_cont.mono huIcc).intervalIntegrable)

private lemma intervalDiffAbsLe
    {h : ℝ} (hh : 0 < h) {f f' : ℝ → ℝ}
    (hf : ∀ x ∈ Icc 0 h, HasDerivAt f (f' x) x)
    (hf'_cont : ContinuousOn f' (Icc 0 h))
    {x y : ℝ} (hx : x ∈ Icc 0 h) (hy : y ∈ Icc 0 h) :
    |f x - f y| ≤ ∫ t in (0 : ℝ)..h, |f' t| := by
  rw [intervalFtcSub hf hf'_cont hx hy]
  have hf'_abs_int : IntervalIntegrable (fun t => |f' t|) volume 0 h :=
    hf'_cont.abs.intervalIntegrable_of_Icc hh.le
  have hf'_nn : 0 ≤ᵐ[volume.restrict (Ioc 0 h)] fun t => |f' t| :=
    ae_of_all _ (fun _ => abs_nonneg _)
  rcases le_or_gt y x with hyx | hyx
  · calc
      |∫ t in y..x, f' t| ≤ ∫ t in y..x, |f' t| := by
        simpa [Real.norm_eq_abs] using
          (intervalIntegral.norm_integral_le_integral_norm (μ := volume) hyx (f := f'))
      _ ≤ ∫ t in (0 : ℝ)..h, |f' t| :=
        integral_mono_interval hy.1 hyx hx.2 hf'_nn hf'_abs_int
  · rw [intervalIntegral.integral_symm, abs_neg]
    calc
      |∫ t in x..y, f' t| ≤ ∫ t in x..y, |f' t| := by
        simpa [Real.norm_eq_abs] using
          (intervalIntegral.norm_integral_le_integral_norm (μ := volume) hyx.le (f := f'))
      _ ≤ ∫ t in (0 : ℝ)..h, |f' t| :=
        integral_mono_interval hx.1 hyx.le hy.2 hf'_nn hf'_abs_int

private lemma intervalPointwiseMeanBound
    {h : ℝ} (hh : 0 < h) {f f' : ℝ → ℝ}
    (hf : ∀ x ∈ Icc 0 h, HasDerivAt f (f' x) x)
    (hf_cont : ContinuousOn f (Icc 0 h))
    (hf'_cont : ContinuousOn f' (Icc 0 h))
    {x : ℝ} (hx : x ∈ Icc 0 h) :
    |f x - (1 / h) * ∫ y in (0 : ℝ)..h, f y| ≤
      ∫ t in (0 : ℝ)..h, |f' t| := by
  set M := ∫ t in (0 : ℝ)..h, |f' t|
  have hbd : ∀ y ∈ Icc 0 h, |f x - f y| ≤ M :=
    fun y hy => intervalDiffAbsLe hh hf hf'_cont hx hy
  have hh_ne : h ≠ 0 := ne_of_gt hh
  have hf_int : IntervalIntegrable f volume 0 h :=
    hf_cont.intervalIntegrable_of_Icc hh.le
  have hfx_sub_int : IntervalIntegrable (fun y => f x - f y) volume 0 h :=
    IntervalIntegrable.sub intervalIntegrable_const hf_int
  set I := ∫ y in (0 : ℝ)..h, f y
  have h_int_diff : (∫ y in (0 : ℝ)..h, (f x - f y)) = h * f x - I := by
    have hsplit := intervalIntegral.integral_sub (μ := volume)
      (a := (0 : ℝ)) (b := h) (f := fun _ => f x) (g := f)
      intervalIntegrable_const hf_int
    simpa [intervalIntegral.integral_const, smul_eq_mul] using hsplit
  have h_rewrite :
      f x - (1 / h) * I =
        (1 / h) * ∫ y in (0 : ℝ)..h, (f x - f y) := by
    rw [h_int_diff]
    field_simp [hh_ne]
  rw [h_rewrite, abs_mul, abs_of_nonneg (by positivity : 0 ≤ (1 / h : ℝ))]
  have h_norm_bound :
      |∫ y in (0 : ℝ)..h, (f x - f y)| ≤ h * M := by
    calc
      |∫ y in (0 : ℝ)..h, (f x - f y)|
          ≤ ∫ y in (0 : ℝ)..h, |f x - f y| := by
            simpa [Real.norm_eq_abs] using
              (intervalIntegral.norm_integral_le_integral_norm
                (μ := volume) hh.le (f := fun y => f x - f y))
      _ ≤ ∫ _ in (0 : ℝ)..h, M := by
        apply integral_mono_on hh.le
        · exact hfx_sub_int.abs
        · exact intervalIntegrable_const
        · exact hbd
      _ = h * M := by
        rw [intervalIntegral.integral_const, sub_zero, smul_eq_mul]
  calc
    1 / h * |∫ y in (0 : ℝ)..h, (f x - f y)|
        ≤ 1 / h * (h * M) :=
          mul_le_mul_of_nonneg_left h_norm_bound (by positivity)
    _ = M := by field_simp [hh_ne]

/-- Cauchy--Schwarz on a finite interval, in the exact squared form needed by
Poincare: `(∫ g)^2 <= (b-a) ∫ g^2`. -/
theorem cauchySchwarzInterval
    {a b : ℝ} (hab : a ≤ b) {g : ℝ → ℝ}
    (hg_cont : ContinuousOn g (Icc a b)) :
    (∫ t in a..b, g t) ^ 2 ≤
      (b - a) * ∫ t in a..b, g t ^ 2 := by
  by_cases hab' : a = b
  · subst b
    simp
  have hab_lt : a < b := lt_of_le_of_ne hab hab'
  have hba_pos : 0 < b - a := sub_pos.mpr hab_lt
  set S := ∫ t in a..b, g t
  set c := S / (b - a)
  have hg_int : IntervalIntegrable g volume a b :=
    hg_cont.intervalIntegrable_of_Icc hab
  have hg2_cont : ContinuousOn (fun t => g t ^ 2) (Icc a b) := hg_cont.pow 2
  have hg2_int : IntervalIntegrable (fun t => g t ^ 2) volume a b :=
    hg2_cont.intervalIntegrable_of_Icc hab
  have hcba : c * (b - a) = S := div_mul_cancel₀ _ (ne_of_gt hba_pos)
  have hvar : 0 ≤ ∫ t in a..b, (g t - c) ^ 2 :=
    integral_nonneg hab (fun u _ => sq_nonneg _)
  have hgc_sub_int : IntervalIntegrable (fun t => -2 * c * g t + c ^ 2) volume a b :=
    (hg_int.const_mul _).add intervalIntegrable_const
  have hexpand :
      ∫ t in a..b, (g t - c) ^ 2 =
        (∫ t in a..b, g t ^ 2) +
          ∫ t in a..b, (-2 * c * g t + c ^ 2) := by
    have hfun : (fun t => (g t - c) ^ 2) =
        (fun t => g t ^ 2 + (-2 * c * g t + c ^ 2)) := by
      funext t
      ring
    rw [hfun, intervalIntegral.integral_add hg2_int hgc_sub_int]
  have hint_linear :
      ∫ t in a..b, (-2 * c * g t + c ^ 2) =
        -c ^ 2 * (b - a) := by
    rw [intervalIntegral.integral_add (hg_int.const_mul _) intervalIntegrable_const,
      intervalIntegral.integral_const_mul, intervalIntegral.integral_const, smul_eq_mul]
    have h_int_eq : ∫ x in a..b, g x = c * (b - a) := hcba.symm
    rw [h_int_eq]
    ring
  rw [hexpand, hint_linear] at hvar
  have h_ineq : c ^ 2 * (b - a) ≤ ∫ t in a..b, g t ^ 2 := by
    linarith
  calc
    S ^ 2 = (c * (b - a)) ^ 2 := by rw [hcba]
    _ = c ^ 2 * (b - a) * (b - a) := by ring
    _ ≤ (∫ t in a..b, g t ^ 2) * (b - a) :=
      mul_le_mul_of_nonneg_right h_ineq hba_pos.le
    _ = (b - a) * ∫ t in a..b, g t ^ 2 := by ring

/--
A genuine weak `L^2` Poincare inequality on the one-dimensional rectangular
box `[0,h]`.  The constant is the side length `h` (nonoptimal but explicit):

`∫ |f-fbar|^2 <= h^2 ∫ |f'|^2`.
-/
theorem intervalPoincareL2
    {h : ℝ} (hh : 0 < h) {f f' : ℝ → ℝ}
    (hf : ∀ x ∈ Icc 0 h, HasDerivAt f (f' x) x)
    (hf_cont : ContinuousOn f (Icc 0 h))
    (hf'_cont : ContinuousOn f' (Icc 0 h)) :
    let fbar := (1 / h) * ∫ x in (0 : ℝ)..h, f x
    ∫ x in (0 : ℝ)..h, |f x - fbar| ^ 2 ≤
      h ^ 2 * ∫ x in (0 : ℝ)..h, |f' x| ^ 2 := by
  intro fbar
  set M := ∫ t in (0 : ℝ)..h, |f' t|
  have hpw : ∀ x ∈ Icc 0 h, |f x - fbar| ^ 2 ≤ M ^ 2 := by
    intro x hx
    have hb := intervalPointwiseMeanBound hh hf hf_cont hf'_cont hx
    have h0 : 0 ≤ |f x - fbar| := abs_nonneg _
    have hM0 : 0 ≤ M := integral_nonneg hh.le (fun t _ => abs_nonneg _)
    exact (sq_le_sq₀ h0 hM0).2 hb
  have hint_bound :
      ∫ x in (0 : ℝ)..h, |f x - fbar| ^ 2 ≤ h * M ^ 2 := by
    have h1 :
        ∫ x in (0 : ℝ)..h, |f x - fbar| ^ 2 ≤
          ∫ _ in (0 : ℝ)..h, M ^ 2 := by
      apply integral_mono_on hh.le
      · exact ((hf_cont.sub continuousOn_const).abs.pow 2).intervalIntegrable_of_Icc hh.le
      · exact intervalIntegrable_const
      · exact hpw
    rwa [intervalIntegral.integral_const, sub_zero, smul_eq_mul] at h1
  have hCS : M ^ 2 ≤ h * ∫ t in (0 : ℝ)..h, |f' t| ^ 2 := by
    have h := cauchySchwarzInterval hh.le hf'_cont.abs
    simpa [M] using h
  calc
    ∫ x in (0 : ℝ)..h, |f x - fbar| ^ 2 ≤ h * M ^ 2 := hint_bound
    _ ≤ h * (h * ∫ t in (0 : ℝ)..h, |f' t| ^ 2) :=
      mul_le_mul_of_nonneg_left hCS hh.le
    _ = h ^ 2 * ∫ t in (0 : ℝ)..h, |f' t| ^ 2 := by ring

/-- Square-root form of the weak interval Poincare inequality. -/
theorem intervalPoincareL2_sqrt
    {h : ℝ} (hh : 0 < h) {f f' : ℝ → ℝ}
    (hf : ∀ x ∈ Icc 0 h, HasDerivAt f (f' x) x)
    (hf_cont : ContinuousOn f (Icc 0 h))
    (hf'_cont : ContinuousOn f' (Icc 0 h)) :
    let fbar := (1 / h) * ∫ x in (0 : ℝ)..h, f x
    Real.sqrt (∫ x in (0 : ℝ)..h, |f x - fbar| ^ 2) ≤
      h * Real.sqrt (∫ x in (0 : ℝ)..h, |f' x| ^ 2) := by
  intro fbar
  have hmain := intervalPoincareL2 hh hf hf_cont hf'_cont
  dsimp only at hmain
  have hsqrt := Real.sqrt_le_sqrt hmain
  simpa [fbar, Real.sqrt_mul (sq_nonneg h), Real.sqrt_sq_eq_abs, abs_of_pos hh] using hsqrt

end AMLStabilization
