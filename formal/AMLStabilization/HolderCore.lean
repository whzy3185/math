import Mathlib
import AMLStabilization.IntegralCoercivity

open MeasureTheory

namespace AMLStabilization

/--
Real-valued Cauchy-Schwarz inequality for Bochner integrals, derived from
mathlib's Holder inequality with exponents `2` and `2`.
-/
theorem integral_mul_cauchySchwarz
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {f g : Ω → ℝ}
    (hf : MemLp f 2 μ) (hg : MemLp g 2 μ) :
    |∫ x, f x * g x ∂μ| ≤
      Real.sqrt (∫ x, f x ^ 2 ∂μ) * Real.sqrt (∫ x, g x ^ 2 ∂μ) := by
  have hpq : (2 : ℝ).HolderConjugate 2 := by
    rw [Real.holderConjugate_iff]
    norm_num
  have hfabs : MemLp (fun x => |f x|) (ENNReal.ofReal (2 : ℝ)) μ := by
    simpa using hf.abs
  have hgabs : MemLp (fun x => |g x|) (ENNReal.ofReal (2 : ℝ)) μ := by
    simpa using hg.abs
  have hholder :=
    integral_mul_le_Lp_mul_Lq_of_nonneg
      (μ := μ) (p := (2 : ℝ)) (q := (2 : ℝ)) hpq
      (f := fun x => |f x|) (g := fun x => |g x|)
      (ae_of_all μ fun x => abs_nonneg (f x))
      (ae_of_all μ fun x => abs_nonneg (g x))
      hfabs hgabs
  calc
    |∫ x, f x * g x ∂μ| = ‖∫ x, f x * g x ∂μ‖ := by
      simp [Real.norm_eq_abs]
    _ ≤ ∫ x, ‖f x * g x‖ ∂μ := norm_integral_le_integral_norm _
    _ = ∫ x, |f x| * |g x| ∂μ := by
      apply integral_congr_ae
      filter_upwards with x
      simp [Real.norm_eq_abs]
    _ ≤
        (∫ x, |f x| ^ (2 : ℝ) ∂μ) ^ (1 / (2 : ℝ)) *
          (∫ x, |g x| ^ (2 : ℝ) ∂μ) ^ (1 / (2 : ℝ)) := hholder
    _ = Real.sqrt (∫ x, f x ^ 2 ∂μ) * Real.sqrt (∫ x, g x ^ 2 ∂μ) := by
      simp [Real.sqrt_eq_rpow, sq_abs]

/--
Weighted first-moment Cauchy-Schwarz estimate used in the mass-weighted mean
argument.  It is obtained by applying the previous theorem to
`sqrt(rho)` and `sqrt(rho) * f`.
-/
theorem weightedFirstMoment_cauchySchwarz
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ}
    (hρnonneg : ∀ x, 0 ≤ ρ x)
    (hsqrtρ : MemLp (fun x => Real.sqrt (ρ x)) 2 μ)
    (hsqrtρf : MemLp (fun x => Real.sqrt (ρ x) * f x) 2 μ) :
    |∫ x, ρ x * f x ∂μ| ≤
      Real.sqrt (∫ x, ρ x ∂μ) * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ) := by
  have hcs := integral_mul_cauchySchwarz
    (μ := μ)
    (f := fun x => Real.sqrt (ρ x))
    (g := fun x => Real.sqrt (ρ x) * f x)
    hsqrtρ hsqrtρf
  have hleft :
      (∫ x, Real.sqrt (ρ x) * (Real.sqrt (ρ x) * f x) ∂μ) =
        ∫ x, ρ x * f x ∂μ := by
    apply integral_congr_ae
    filter_upwards with x
    rw [← mul_assoc, Real.mul_self_sqrt (hρnonneg x)]
  have hrhoSq :
      (∫ x, (Real.sqrt (ρ x)) ^ 2 ∂μ) = ∫ x, ρ x ∂μ := by
    apply integral_congr_ae
    filter_upwards with x
    exact Real.sq_sqrt (hρnonneg x)
  have hweightedSq :
      (∫ x, (Real.sqrt (ρ x) * f x) ^ 2 ∂μ) =
        ∫ x, ρ x * f x ^ 2 ∂μ := by
    apply integral_congr_ae
    filter_upwards with x
    rw [mul_pow, Real.sq_sqrt (hρnonneg x)]
  simpa [hleft, hrhoSq, hweightedSq] using hcs

/-- Standard deviation Cauchy-Schwarz bound in `L2`. -/
theorem weightedDeviation_cauchySchwarz
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ} {fbar : ℝ}
    (hρ : MemLp ρ 2 μ)
    (hdev : MemLp (fun x => f x - fbar) 2 μ) :
    |∫ x, ρ x * (f x - fbar) ∂μ| ≤
      Real.sqrt (∫ x, ρ x ^ 2 ∂μ) *
        Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) := by
  exact integral_mul_cauchySchwarz (μ := μ) hρ hdev

/-- If the `L2` norm of `rho` is bounded by `K`, the deviation estimate has
exactly the form required by `IntegralCoercivity.lean`. -/
theorem weightedDeviation_cauchySchwarz_of_bound
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ} {fbar K : ℝ}
    (hρ : MemLp ρ 2 μ)
    (hdev : MemLp (fun x => f x - fbar) 2 μ)
    (hK : Real.sqrt (∫ x, ρ x ^ 2 ∂μ) ≤ K) :
    |∫ x, ρ x * (f x - fbar) ∂μ| ≤
      K * Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) := by
  calc
    |∫ x, ρ x * (f x - fbar) ∂μ| ≤
        Real.sqrt (∫ x, ρ x ^ 2 ∂μ) *
          Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) :=
      weightedDeviation_cauchySchwarz (μ := μ) hρ hdev
    _ ≤ K * Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) := by
      exact mul_le_mul_of_nonneg_right hK (Real.sqrt_nonneg _)

/--
Mean estimate with both Cauchy-Schwarz inputs discharged by `MemLp` hypotheses.
Only the Poincare estimate remains an external analytic input.
-/
theorem integralMassWeightedMeanEstimate_of_MemLp
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ}
    {m K Cp grad fbar : ℝ}
    (hm : 0 < m)
    (hK0 : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hgrad : 0 ≤ grad)
    (hρnonneg : ∀ x, 0 ≤ ρ x)
    (hρint : Integrable ρ μ)
    (hρfint : Integrable (fun x => ρ x * f x) μ)
    (hmass : (∫ x, ρ x ∂μ) = m)
    (hsqrtρ : MemLp (fun x => Real.sqrt (ρ x)) 2 μ)
    (hsqrtρf : MemLp (fun x => Real.sqrt (ρ x) * f x) 2 μ)
    (hρL2 : MemLp ρ 2 μ)
    (hdevL2 : MemLp (fun x => f x - fbar) 2 μ)
    (hρL2bound : Real.sqrt (∫ x, ρ x ^ 2 ∂μ) ≤ K)
    (hPoincare :
      Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) ≤ Cp * grad) :
    |fbar| ≤
      (Real.sqrt m / m) * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ) +
        (K * Cp / m) * grad := by
  apply integralMassWeightedMeanEstimate
    (μ := μ) (ρ := ρ) (f := f)
    (m := m) (K := K) (Cp := Cp) (grad := grad) (fbar := fbar)
    hm hK0 hCp hgrad hρint hρfint hmass
  · simpa [hmass] using
      (weightedFirstMoment_cauchySchwarz
        (μ := μ) (ρ := ρ) (f := f) hρnonneg hsqrtρ hsqrtρf)
  · exact weightedDeviation_cauchySchwarz_of_bound
      (μ := μ) (ρ := ρ) (f := f) (fbar := fbar) hρL2 hdevL2 hρL2bound
  · exact hPoincare

end AMLStabilization
