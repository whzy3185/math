import Mathlib
import AMLStabilization.ProductVarianceCore
import AMLStabilization.PairedProductMeasureCore
import AMLStabilization.IntegratedCoordinateTelescopingCore
import AMLStabilization.BoxHybridFiberPoincareCore
import AMLStabilization.BoxVolumeFactorCore

open Set MeasureTheory Real

namespace AMLStabilization

/-- Product Lebesgue measure on a closed rectangular box, represented as a
finite product of one-dimensional restricted Lebesgue measures. -/
noncomputable def rectangularBoxMeasure
    {m : ℕ} (a b : Fin m → ℝ) : Measure (Fin m → ℝ) :=
  Measure.pi (fun j => volume.restrict (Icc (a j) (b j)))

/-- Paired-copy product measure used in the independent-copy/telescoping proof. -/
noncomputable def rectangularPairedBoxMeasure
    {m : ℕ} (a b : Fin m → ℝ) : Measure (Fin m → ℝ × ℝ) :=
  Measure.pi (fun j =>
    (volume.restrict (Icc (a j) (b j))).prod
      (volume.restrict (Icc (a j) (b j))))

/-- Product of the side lengths of a rectangular box. -/
def rectangularBoxVolume {m : ℕ} (a b : Fin m → ℝ) : ℝ :=
  ∏ j, (b j - a j)

/-- Integral mean over a nondegenerate rectangular box. -/
noncomputable def rectangularBoxMean
    {m : ℕ} (a b : Fin m → ℝ) (f : (Fin m → ℝ) → ℝ) : ℝ :=
  (rectangularBoxVolume a b)⁻¹ * ∫ x, f x ∂rectangularBoxMeasure a b

/--
A genuine finite-dimensional `L²` Poincare inequality on a nondegenerate
rectangular box, derived from one-dimensional FTC/Poincare, independent-copy
variance, finite-coordinate telescoping, and product-measure Fubini.

The constant is explicit but nonoptimal: if every side length is at most `C`,
then

`∫ |f-f̄|² ≤ N C² ∑ᵢ ∫ |∂ᵢ f|²`,

where `N = n+1`.  In particular there is no external variance-decomposition or
Poincare hypothesis at this layer. -/
theorem rectangularBoxPoincareL2
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C : ℝ} (hC : 0 ≤ C)
    (hSideBound : ∀ j, b j - a j ≤ C)
    (f : (Fin (n + 1) → ℝ) → ℝ)
    (df : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (hfLp : MemLp f 2 (rectangularBoxMeasure a b))
    (hDiffInt : Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2)
      (rectangularPairedBoxMeasure a b))
    (hStepInt : ∀ i : Fin (n + 1), Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        (pairedCoordinateIncrement f z i.val) ^ 2)
      (rectangularPairedBoxMeasure a b))
    (hDerivInt : ∀ i : Fin (n + 1), Integrable
      (fun x : Fin (n + 1) → ℝ => (df x i) ^ 2)
      (rectangularBoxMeasure a b))
    (hFiberDeriv : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ∀ t ∈ Icc (a i) (b i),
        HasDerivAt (fun s => f (i.insertNth s xr))
          (df (i.insertNth t xr) i) t)
    (hFiberCont : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ContinuousOn (fun t => f (i.insertNth t xr)) (Icc (a i) (b i)))
    (hFiberDCont : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ContinuousOn (fun t => df (i.insertNth t xr) i) (Icc (a i) (b i))) :
    (∫ x : Fin (n + 1) → ℝ,
        (f x - rectangularBoxMean a b f) ^ 2
        ∂rectangularBoxMeasure a b) ≤
      (n + 1 : ℝ) * C ^ 2 *
        ∑ i : Fin (n + 1),
          ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2
            ∂rectangularBoxMeasure a b := by
  let μ : Fin (n + 1) → Measure ℝ :=
    fun j => volume.restrict (Icc (a j) (b j))
  let μbox : Measure (Fin (n + 1) → ℝ) := rectangularBoxMeasure a b
  let ν : Measure (Fin (n + 1) → ℝ × ℝ) := rectangularPairedBoxMeasure a b
  let V : ℝ := rectangularBoxVolume a b
  let fbar : ℝ := rectangularBoxMean a b f
  have hVpos : 0 < V := by
    dsimp [V, rectangularBoxVolume]
    apply Finset.prod_pos
    intro i hi
    exact sub_pos.mpr (hside i)
  have hVne : V ≠ 0 := ne_of_gt hVpos
  have hvol : (∫ _ : Fin (n + 1) → ℝ, (1 : ℝ) ∂μbox) = V := by
    simpa [μbox, V, rectangularBoxMeasure, rectangularBoxVolume] using
      (integralOne_piBox_eq_prod_side hside)
  have hmean : (∫ x : Fin (n + 1) → ℝ, f x ∂μbox) = V * fbar := by
    change (∫ x : Fin (n + 1) → ℝ, f x ∂μbox) =
      V * (V⁻¹ * ∫ x : Fin (n + 1) → ℝ, f x ∂μbox)
    have hinv : V * V⁻¹ = 1 := by
      field_simp [hVne]
    calc
      (∫ x : Fin (n + 1) → ℝ, f x ∂μbox) =
          1 * (∫ x : Fin (n + 1) → ℝ, f x ∂μbox) := by ring
      _ = (V * V⁻¹) * (∫ x : Fin (n + 1) → ℝ, f x ∂μbox) := by rw [hinv]
      _ = V * (V⁻¹ * ∫ x : Fin (n + 1) → ℝ, f x ∂μbox) := by ring
  letI : IsFiniteMeasure μbox := by
    dsimp [μbox, rectangularBoxMeasure]
    infer_instance
  have hpairProd :=
    productDifferenceSquareIntegral_eq_two_mul_volume_mul_deviation
      (μ := μbox) (f := f) (fbar := fbar) (V := V)
      hfLp hvol hmean
  have htransport := integral_pairedCoordinateDifference_sq μ f
  have hpairPaired :
      (∫ z : Fin (n + 1) → ℝ × ℝ,
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2 ∂ν) =
        2 * V * ∫ x : Fin (n + 1) → ℝ, (f x - fbar) ^ 2 ∂μbox := by
    calc
      (∫ z : Fin (n + 1) → ℝ × ℝ,
          (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2 ∂ν) =
          ∫ p : (Fin (n + 1) → ℝ) × (Fin (n + 1) → ℝ),
            (f p.1 - f p.2) ^ 2 ∂(μbox.prod μbox) := by
              simpa [ν, μbox, μ, rectangularPairedBoxMeasure,
                rectangularBoxMeasure] using htransport
      _ = 2 * V * ∫ x : Fin (n + 1) → ℝ, (f x - fbar) ^ 2 ∂μbox := hpairProd
  have hStepNat : ∀ k ∈ Finset.range (n + 1), Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        (pairedCoordinateIncrement f z k) ^ 2) ν := by
    intro k hk
    have hklt : k < n + 1 := Finset.mem_range.mp hk
    simpa [ν] using hStepInt ⟨k, hklt⟩
  have htel := integral_coordinateTelescoping_sq_le ν f hDiffInt hStepNat
  have htelFin :
      (∫ z : Fin (n + 1) → ℝ × ℝ,
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2 ∂ν) ≤
        (n + 1 : ℝ) *
          ∑ i : Fin (n + 1),
            ∫ z : Fin (n + 1) → ℝ × ℝ,
              (pairedCoordinateIncrement f z i.val) ^ 2 ∂ν := by
    simpa only [Finset.sum_range, Nat.cast_add, Nat.cast_one] using htel
  have hcoord : ∀ i : Fin (n + 1),
      (∫ z : Fin (n + 1) → ℝ × ℝ,
        (pairedCoordinateIncrement f z i.val) ^ 2 ∂ν) ≤
        2 * V * C ^ 2 *
          (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
    intro i
    have hi := boxHybridCoordinateIncrement_sq_le
      hside f df i
      (by simpa [ν, rectangularPairedBoxMeasure] using hStepInt i)
      (by simpa [μbox, rectangularBoxMeasure] using hDerivInt i)
      (hFiberDeriv i) (hFiberCont i) (hFiberDCont i)
    have hfactor := boxSideCube_mul_restMass_eq_volume_mul_sideSq hside i
    have hiV :
        (∫ z : Fin (n + 1) → ℝ × ℝ,
          (pairedCoordinateIncrement f z i.val) ^ 2 ∂ν) ≤
          2 * V * (b i - a i) ^ 2 *
            (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
      calc
        (∫ z : Fin (n + 1) → ℝ × ℝ,
            (pairedCoordinateIncrement f z i.val) ^ 2 ∂ν) ≤
            2 * (b i - a i) ^ 3 *
              (∏ j : Fin n,
                (volume.restrict
                  (Icc (a (i.succAbove j)) (b (i.succAbove j))) Set.univ)).toReal *
              (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
                simpa [ν, μbox, rectangularPairedBoxMeasure,
                  rectangularBoxMeasure] using hi
        _ = 2 *
              ((b i - a i) ^ 3 *
                (∏ j : Fin n,
                  (volume.restrict
                    (Icc (a (i.succAbove j)) (b (i.succAbove j))) Set.univ)).toReal) *
              (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by ring
        _ = 2 * (V * (b i - a i) ^ 2) *
              (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
                rw [show
                  (b i - a i) ^ 3 *
                    (∏ j : Fin n,
                      (volume.restrict
                        (Icc (a (i.succAbove j)) (b (i.succAbove j))) Set.univ)).toReal =
                    V * (b i - a i) ^ 2 by
                      simpa [V, rectangularBoxVolume] using hfactor]
        _ = 2 * V * (b i - a i) ^ 2 *
              (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by ring
    have hEi0 : 0 ≤ ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox := by
      apply integral_nonneg_of_ae
      exact Filter.Eventually.of_forall fun x => sq_nonneg _
    have hsq : (b i - a i) ^ 2 ≤ C ^ 2 := by
      nlinarith [sub_pos.mpr (hside i), hSideBound i]
    have h2V0 : 0 ≤ 2 * V := by positivity
    calc
      (∫ z : Fin (n + 1) → ℝ × ℝ,
          (pairedCoordinateIncrement f z i.val) ^ 2 ∂ν) ≤
          2 * V * (b i - a i) ^ 2 *
            (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := hiV
      _ = (2 * V) *
          ((b i - a i) ^ 2 *
            (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox)) := by ring
      _ ≤ (2 * V) *
          (C ^ 2 *
            (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox)) := by
              exact mul_le_mul_of_nonneg_left
                (mul_le_mul_of_nonneg_right hsq hEi0) h2V0
      _ = 2 * V * C ^ 2 *
          (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by ring
  have hsum :
      (∑ i : Fin (n + 1),
        ∫ z : Fin (n + 1) → ℝ × ℝ,
          (pairedCoordinateIncrement f z i.val) ^ 2 ∂ν) ≤
        ∑ i : Fin (n + 1),
          2 * V * C ^ 2 *
            (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
    exact Finset.sum_le_sum fun i hi => hcoord i
  have htelBound :
      (∫ z : Fin (n + 1) → ℝ × ℝ,
        (f (fun i => (z i).1) - f (fun i => (z i).2)) ^ 2 ∂ν) ≤
        (n + 1 : ℝ) *
          (2 * V * C ^ 2 *
            ∑ i : Fin (n + 1),
              ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
    calc
      _ ≤ (n + 1 : ℝ) *
          ∑ i : Fin (n + 1),
            ∫ z : Fin (n + 1) → ℝ × ℝ,
              (pairedCoordinateIncrement f z i.val) ^ 2 ∂ν := htelFin
      _ ≤ (n + 1 : ℝ) *
          ∑ i : Fin (n + 1),
            2 * V * C ^ 2 *
              (∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
                exact mul_le_mul_of_nonneg_left hsum (by positivity)
      _ = (n + 1 : ℝ) *
          (2 * V * C ^ 2 *
            ∑ i : Fin (n + 1),
              ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
                rw [← Finset.mul_sum]
  rw [hpairPaired] at htelBound
  have hcancel :
      (2 * V) *
        (∫ x : Fin (n + 1) → ℝ, (f x - fbar) ^ 2 ∂μbox) ≤
      (2 * V) *
        ((n + 1 : ℝ) * C ^ 2 *
          ∑ i : Fin (n + 1),
            ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by
    calc
      (2 * V) *
          (∫ x : Fin (n + 1) → ℝ, (f x - fbar) ^ 2 ∂μbox) =
          2 * V *
            (∫ x : Fin (n + 1) → ℝ, (f x - fbar) ^ 2 ∂μbox) := by ring
      _ ≤ (n + 1 : ℝ) *
          (2 * V * C ^ 2 *
            ∑ i : Fin (n + 1),
              ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := htelBound
      _ = (2 * V) *
          ((n + 1 : ℝ) * C ^ 2 *
            ∑ i : Fin (n + 1),
              ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox) := by ring
  have hfinal :
      (∫ x : Fin (n + 1) → ℝ, (f x - fbar) ^ 2 ∂μbox) ≤
        (n + 1 : ℝ) * C ^ 2 *
          ∑ i : Fin (n + 1),
            ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μbox := by
    exact le_of_mul_le_mul_left hcancel (show 0 < 2 * V by positivity)
  simpa [μbox, V, fbar, rectangularBoxMean, rectangularBoxVolume] using hfinal

end AMLStabilization
