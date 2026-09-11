import Mathlib
import AMLStabilization.FullBoxPoincareSqrtCore
import AMLStabilization.PoincareMeanCore

open Set MeasureTheory Real

namespace AMLStabilization

/--
Mass-weighted coercivity on a nondegenerate rectangular box with the geometric
Poincare input generated internally.

The effective Poincare constant is `sqrt (n+1) * C`, where `C` bounds every
side length.  Thus the former abstract `hPoincare`/variance-decomposition input
is absent from this theorem; only the genuinely weight-dependent `ρ` estimates
remain as analytic hypotheses. -/
theorem integralMassWeightedCoercivity_on_rectangularBox
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ j, a j < b j)
    {C : ℝ} (hC : 0 ≤ C)
    (hSideBound : ∀ j, b j - a j ≤ C)
    (ρ f : (Fin (n + 1) → ℝ) → ℝ)
    (df : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    {m K : ℝ}
    (hm : 0 < m)
    (hK0 : 0 ≤ K)
    (hρnonneg : ∀ x, 0 ≤ ρ x)
    (hρint : Integrable ρ (rectangularBoxMeasure a b))
    (hρfint : Integrable (fun x => ρ x * f x) (rectangularBoxMeasure a b))
    (hmass : (∫ x, ρ x ∂rectangularBoxMeasure a b) = m)
    (hsqrtρ : MemLp (fun x => Real.sqrt (ρ x)) 2 (rectangularBoxMeasure a b))
    (hsqrtρf : MemLp (fun x => Real.sqrt (ρ x) * f x) 2 (rectangularBoxMeasure a b))
    (hρL2 : MemLp ρ 2 (rectangularBoxMeasure a b))
    (hρL2bound : Real.sqrt (∫ x, ρ x ^ 2 ∂rectangularBoxMeasure a b) ≤ K)
    (hfLp : MemLp f 2 (rectangularBoxMeasure a b))
    (hdevL2 : MemLp
      (fun x => f x - rectangularBoxMean a b f) 2
      (rectangularBoxMeasure a b))
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
    (∫ x : Fin (n + 1) → ℝ, f x ^ 2 ∂rectangularBoxMeasure a b) ≤
      (2 * (Real.sqrt (n + 1 : ℝ) * C) ^ 2 +
          4 * rectangularBoxVolume a b *
            (K * (Real.sqrt (n + 1 : ℝ) * C) / m) ^ 2) *
        (∑ i : Fin (n + 1),
          ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2
            ∂rectangularBoxMeasure a b) +
      4 * rectangularBoxVolume a b * (Real.sqrt m / m) ^ 2 *
        (∫ x : Fin (n + 1) → ℝ, ρ x * f x ^ 2
          ∂rectangularBoxMeasure a b) := by
  let μ : Measure (Fin (n + 1) → ℝ) := rectangularBoxMeasure a b
  let V : ℝ := rectangularBoxVolume a b
  let fbar : ℝ := rectangularBoxMean a b f
  let G : ℝ :=
    ∑ i : Fin (n + 1),
      ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μ
  let Cp : ℝ := Real.sqrt (n + 1 : ℝ) * C
  let grad : ℝ := Real.sqrt G
  letI : IsFiniteMeasure μ := by
    dsimp [μ, rectangularBoxMeasure]
    infer_instance
  have hVpos : 0 < V := by
    dsimp [V, rectangularBoxVolume]
    apply Finset.prod_pos
    intro i hi
    exact sub_pos.mpr (hside i)
  have hV0 : 0 ≤ V := hVpos.le
  have hCp0 : 0 ≤ Cp := by
    dsimp [Cp]
    positivity
  have hEi0 : ∀ i : Fin (n + 1),
      0 ≤ ∫ x : Fin (n + 1) → ℝ, (df x i) ^ 2 ∂μ := by
    intro i
    apply integral_nonneg_of_ae
    exact Filter.Eventually.of_forall fun x => sq_nonneg _
  have hG0 : 0 ≤ G := by
    dsimp [G]
    exact Finset.sum_nonneg fun i hi => hEi0 i
  have hgrad0 : 0 ≤ grad := by
    dsimp [grad]
    exact Real.sqrt_nonneg _
  have hf : Integrable f μ := by
    simpa [μ] using hfLp.integrable one_le_two
  have hf2 : Integrable (fun x => f x ^ 2) μ := by
    simpa [μ] using hfLp.integrable_sq
  have hone : Integrable (fun _ : Fin (n + 1) → ℝ => (1 : ℝ)) μ :=
    integrable_const 1
  have hvol : (∫ _ : Fin (n + 1) → ℝ, (1 : ℝ) ∂μ) = V := by
    simpa [μ, V, rectangularBoxMeasure, rectangularBoxVolume] using
      (integralOne_piBox_eq_prod_side hside)
  have hVne : V ≠ 0 := ne_of_gt hVpos
  have hmean : (∫ x : Fin (n + 1) → ℝ, f x ∂μ) = V * fbar := by
    change (∫ x : Fin (n + 1) → ℝ, f x ∂μ) =
      V * (V⁻¹ * ∫ x : Fin (n + 1) → ℝ, f x ∂μ)
    have hinv : V * V⁻¹ = 1 := by field_simp [hVne]
    calc
      (∫ x : Fin (n + 1) → ℝ, f x ∂μ) =
          1 * (∫ x : Fin (n + 1) → ℝ, f x ∂μ) := by ring
      _ = (V * V⁻¹) * (∫ x : Fin (n + 1) → ℝ, f x ∂μ) := by rw [hinv]
      _ = V * (V⁻¹ * ∫ x : Fin (n + 1) → ℝ, f x ∂μ) := by ring
  have hPoincare :
      Real.sqrt (∫ x : Fin (n + 1) → ℝ, (f x - fbar) ^ 2 ∂μ) ≤
        Cp * grad := by
    have hp := rectangularBoxPoincareL2_sqrt
      hside hC hSideBound f df hfLp hDiffInt hStepInt hDerivInt
      hFiberDeriv hFiberCont hFiberDCont
    simpa [μ, fbar, Cp, grad, G] using hp
  have hcore := integralMassWeightedCoercivity_of_MemLp_and_Poincare
    (μ := μ) (ρ := ρ) (f := f)
    (m := m) (K := K) (Cp := Cp) (grad := grad)
    (fbar := fbar) (V := V)
    hm hK0 hCp0 hgrad0 hV0 hρnonneg
    (by simpa [μ] using hρint)
    (by simpa [μ] using hρfint)
    (by simpa [μ] using hmass)
    (by simpa [μ] using hsqrtρ)
    (by simpa [μ] using hsqrtρf)
    (by simpa [μ] using hρL2)
    (by simpa [μ, fbar] using hdevL2)
    (by simpa [μ] using hρL2bound)
    hf hf2 hone hvol hmean hPoincare
  have hgradSq : grad ^ 2 = G := by
    dsimp [grad]
    exact Real.sq_sqrt hG0
  rw [hgradSq] at hcore
  simpa [μ, V, fbar, Cp, G, rectangularBoxVolume] using hcore

end AMLStabilization
