import Mathlib
import AMLStabilization.IntervalPoincareShiftCore
import AMLStabilization.ProductVarianceCore

open Set MeasureTheory Real intervalIntegral

namespace AMLStabilization

/--
Double-copy form of the weak Poincare inequality on an interval.  It is the
fiber estimate used in the product-measure proof: the left side contains no
fiber mean, only the difference of two independent copies.
-/
theorem intervalPairDifferenceL2
    {a b : ℝ} (hab : a < b) {f f' : ℝ → ℝ}
    (hf : ∀ x ∈ Icc a b, HasDerivAt f (f' x) x)
    (hf_cont : ContinuousOn f (Icc a b))
    (hf'_cont : ContinuousOn f' (Icc a b)) :
    let μ := volume.restrict (Icc a b)
    (∫ z : ℝ × ℝ, (f z.1 - f z.2) ^ 2 ∂(μ.prod μ)) ≤
      2 * (b - a) ^ 3 * ∫ x in a..b, |f' x| ^ 2 := by
  intro μ
  let fbar : ℝ := (1 / (b - a)) * ∫ x in a..b, f x
  have hfmeas : AEStronglyMeasurable f μ := by
    dsimp only [μ]
    exact hf_cont.aestronglyMeasurable_of_isCompact isCompact_Icc measurableSet_Icc
  have hsqcont : ContinuousOn (fun x => f x ^ 2) (Icc a b) := by
    have hmul : ContinuousOn (f * f) (Icc a b) := hf_cont.mul hf_cont
    simpa only [Pi.mul_apply, pow_two] using hmul
  have hf2int : Integrable (fun x => f x ^ 2) μ := by
    dsimp only [μ]
    exact (hsqcont.locallyIntegrableOn measurableSet_Icc).integrableOn_isCompact isCompact_Icc
  have hfLp : MemLp f 2 μ :=
    (memLp_two_iff_integrable_sq hfmeas).2 hf2int
  have hvol : (∫ _ : ℝ, (1 : ℝ) ∂μ) = b - a := by
    dsimp only [μ]
    rw [MeasureTheory.integral_const]
    simp only [MeasurableSet.univ, measureReal_restrict_apply, Set.univ_inter,
      smul_eq_mul, mul_one]
    exact Real.volume_real_Icc_of_le hab.le
  have hsetIntegral : (∫ x, f x ∂μ) = ∫ x in a..b, f x := by
    dsimp only [μ]
    change (∫ x in Icc a b, f x) = ∫ x in a..b, f x
    rw [MeasureTheory.integral_Icc_eq_integral_Ioc,
      ← intervalIntegral.integral_of_le hab.le]
  have hmean : (∫ x, f x ∂μ) = (b - a) * fbar := by
    have hne : b - a ≠ 0 := sub_ne_zero.mpr hab.ne'
    have hinv : (b - a) * (1 / (b - a)) = 1 := by
      field_simp [hne]
    rw [hsetIntegral]
    dsimp only [fbar]
    calc
      (∫ x in a..b, f x) = 1 * (∫ x in a..b, f x) := by ring
      _ = ((b - a) * (1 / (b - a))) * (∫ x in a..b, f x) := by rw [hinv]
      _ = (b - a) * ((1 / (b - a)) * ∫ x in a..b, f x) := by ring
  have hpair :=
    productDifferenceSquareIntegral_eq_two_mul_volume_mul_deviation
      (μ := μ) (f := f) (fbar := fbar) (V := b - a)
      hfLp hvol hmean
  have hdevEq :
      (∫ x, (f x - fbar) ^ 2 ∂μ) =
        ∫ x in a..b, |f x - fbar| ^ 2 := by
    dsimp only [μ]
    change (∫ x in Icc a b, (f x - fbar) ^ 2) =
      ∫ x in a..b, |f x - fbar| ^ 2
    rw [MeasureTheory.integral_Icc_eq_integral_Ioc,
      ← intervalIntegral.integral_of_le hab.le]
    apply intervalIntegral.integral_congr
    intro x hx
    exact (sq_abs (f x - fbar)).symm
  have hp := intervalPoincareL2_Icc
    (a := a) (b := b) hab (f := f) (f' := f') hf hf_cont hf'_cont
  dsimp only at hp
  have hcoef : 0 ≤ 2 * (b - a) := by positivity
  calc
    (∫ z : ℝ × ℝ, (f z.1 - f z.2) ^ 2 ∂(μ.prod μ)) =
        2 * (b - a) * ∫ x, (f x - fbar) ^ 2 ∂μ := hpair
    _ = 2 * (b - a) * ∫ x in a..b, |f x - fbar| ^ 2 := by rw [hdevEq]
    _ ≤ 2 * (b - a) *
        ((b - a) ^ 2 * ∫ x in a..b, |f' x| ^ 2) :=
      mul_le_mul_of_nonneg_left hp hcoef
    _ = 2 * (b - a) ^ 3 * ∫ x in a..b, |f' x| ^ 2 := by ring

end AMLStabilization
