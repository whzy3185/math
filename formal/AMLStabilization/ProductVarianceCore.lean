import Mathlib
import AMLStabilization.PoincareMeanCore

open MeasureTheory
open scoped ProbabilityTheory

namespace AMLStabilization

/--
Independent-copy variance identity on a probability space:

`∫∫ (f(x)-f(y))² dμ(x)dμ(y) = 2 Var_μ(f)`.

This is the starting point for a finite-product Efron--Stein/telescoping proof
of a rectangular-box Poincare inequality.
-/
theorem productDifferenceSquareIntegral_eq_two_variance
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} [IsProbabilityMeasure μ]
    {f : Ω → ℝ} (hf : MemLp f 2 μ) :
    (∫ z : Ω × Ω, (f z.1 - f z.2) ^ 2 ∂(μ.prod μ)) =
      2 * ProbabilityTheory.variance f μ := by
  have hf1 : Integrable f μ := hf.integrable one_le_two
  have hf2 : Integrable (fun x => f x ^ 2) μ := hf.integrable_sq
  have hfst2 : Integrable (fun z : Ω × Ω => f z.1 ^ 2) (μ.prod μ) :=
    hf2.comp_fst μ
  have hsnd2 : Integrable (fun z : Ω × Ω => f z.2 ^ 2) (μ.prod μ) :=
    hf2.comp_snd μ
  have hcross : Integrable (fun z : Ω × Ω => f z.1 * f z.2) (μ.prod μ) :=
    hf1.mul_prod hf1
  have htwocross : Integrable (fun z : Ω × Ω => 2 * (f z.1 * f z.2)) (μ.prod μ) :=
    hcross.const_mul 2
  have hleft : Integrable
      (fun z : Ω × Ω => f z.1 ^ 2 - 2 * (f z.1 * f z.2)) (μ.prod μ) := by
    change Integrable
      ((fun z : Ω × Ω => f z.1 ^ 2) -
        (fun z : Ω × Ω => 2 * (f z.1 * f z.2))) (μ.prod μ)
    exact hfst2.sub htwocross
  have hexpand :
      (fun z : Ω × Ω => (f z.1 - f z.2) ^ 2) =
        (fun z => f z.1 ^ 2 - 2 * (f z.1 * f z.2) + f z.2 ^ 2) := by
    funext z
    ring
  have hfstIntegral :
      (∫ z : Ω × Ω, f z.1 ^ 2 ∂(μ.prod μ)) = ∫ x, f x ^ 2 ∂μ := by
    rw [integral_prod _ hfst2]
    simp
  have hsndIntegral :
      (∫ z : Ω × Ω, f z.2 ^ 2 ∂(μ.prod μ)) = ∫ x, f x ^ 2 ∂μ := by
    rw [integral_prod _ hsnd2]
    simp
  have hcrossIntegral :
      (∫ z : Ω × Ω, f z.1 * f z.2 ∂(μ.prod μ)) =
        (∫ x, f x ∂μ) ^ 2 := by
    rw [integral_prod_mul]
    ring
  have hadd :
      (∫ z : Ω × Ω,
        (f z.1 ^ 2 - 2 * (f z.1 * f z.2)) + f z.2 ^ 2 ∂(μ.prod μ)) =
      (∫ z : Ω × Ω, f z.1 ^ 2 - 2 * (f z.1 * f z.2) ∂(μ.prod μ)) +
        ∫ z : Ω × Ω, f z.2 ^ 2 ∂(μ.prod μ) := by
    simpa only using integral_add hleft hsnd2
  have hsub :
      (∫ z : Ω × Ω, f z.1 ^ 2 - 2 * (f z.1 * f z.2) ∂(μ.prod μ)) =
      (∫ z : Ω × Ω, f z.1 ^ 2 ∂(μ.prod μ)) -
        ∫ z : Ω × Ω, 2 * (f z.1 * f z.2) ∂(μ.prod μ) := by
    simpa only using integral_sub hfst2 htwocross
  rw [hexpand, hadd, hsub, integral_const_mul]
  rw [hfstIntegral, hsndIntegral, hcrossIntegral]
  rw [ProbabilityTheory.variance_eq_sub hf]
  simp only [Pi.pow_apply]
  ring

/--
Finite-measure independent-copy identity.  If `V = ∫ 1 dμ` and
`fbar` is the integral mean (`∫ f = V fbar`), then

`∫∫ (f(x)-f(y))² dμ(x)dμ(y) = 2 V ∫ (f-fbar)² dμ`.

Keeping the volume factor explicit is convenient for rectangular boxes: no
probability normalization is needed, and the factor cancels after the
coordinatewise Poincare estimates are summed.
-/
theorem productDifferenceSquareIntegral_eq_two_mul_volume_mul_deviation
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} [IsFiniteMeasure μ]
    {f : Ω → ℝ} {fbar V : ℝ}
    (hf : MemLp f 2 μ)
    (hvol : (∫ _ : Ω, (1 : ℝ) ∂μ) = V)
    (hmean : (∫ x, f x ∂μ) = V * fbar) :
    (∫ z : Ω × Ω, (f z.1 - f z.2) ^ 2 ∂(μ.prod μ)) =
      2 * V * (∫ x, (f x - fbar) ^ 2 ∂μ) := by
  have hf1 : Integrable f μ := hf.integrable one_le_two
  have hf2 : Integrable (fun x => f x ^ 2) μ := hf.integrable_sq
  have hone : Integrable (fun _ : Ω => (1 : ℝ)) μ := integrable_const 1
  have hfst2 : Integrable (fun z : Ω × Ω => f z.1 ^ 2) (μ.prod μ) :=
    hf2.comp_fst μ
  have hsnd2 : Integrable (fun z : Ω × Ω => f z.2 ^ 2) (μ.prod μ) :=
    hf2.comp_snd μ
  have hcross : Integrable (fun z : Ω × Ω => f z.1 * f z.2) (μ.prod μ) :=
    hf1.mul_prod hf1
  have htwocross : Integrable (fun z : Ω × Ω => 2 * (f z.1 * f z.2)) (μ.prod μ) :=
    hcross.const_mul 2
  have hleft : Integrable
      (fun z : Ω × Ω => f z.1 ^ 2 - 2 * (f z.1 * f z.2)) (μ.prod μ) := by
    change Integrable
      ((fun z : Ω × Ω => f z.1 ^ 2) -
        (fun z : Ω × Ω => 2 * (f z.1 * f z.2))) (μ.prod μ)
    exact hfst2.sub htwocross
  have hexpand :
      (fun z : Ω × Ω => (f z.1 - f z.2) ^ 2) =
        (fun z => f z.1 ^ 2 - 2 * (f z.1 * f z.2) + f z.2 ^ 2) := by
    funext z
    ring
  have hfstIntegral :
      (∫ z : Ω × Ω, f z.1 ^ 2 ∂(μ.prod μ)) =
        (∫ x, f x ^ 2 ∂μ) * V := by
    calc
      (∫ z : Ω × Ω, f z.1 ^ 2 ∂(μ.prod μ)) =
          (∫ x, f x ^ 2 ∂μ) * ∫ _ : Ω, (1 : ℝ) ∂μ := by
            simpa using
              (integral_prod_mul (μ := μ) (ν := μ)
                (fun x => f x ^ 2) (fun _ : Ω => (1 : ℝ)))
      _ = (∫ x, f x ^ 2 ∂μ) * V := by rw [hvol]
  have hsndIntegral :
      (∫ z : Ω × Ω, f z.2 ^ 2 ∂(μ.prod μ)) =
        V * (∫ x, f x ^ 2 ∂μ) := by
    calc
      (∫ z : Ω × Ω, f z.2 ^ 2 ∂(μ.prod μ)) =
          (∫ _ : Ω, (1 : ℝ) ∂μ) * ∫ x, f x ^ 2 ∂μ := by
            simpa using
              (integral_prod_mul (μ := μ) (ν := μ)
                (fun _ : Ω => (1 : ℝ)) (fun x => f x ^ 2))
      _ = V * (∫ x, f x ^ 2 ∂μ) := by rw [hvol]
  have hcrossIntegral :
      (∫ z : Ω × Ω, f z.1 * f z.2 ∂(μ.prod μ)) =
        (∫ x, f x ∂μ) ^ 2 := by
    rw [integral_prod_mul]
    ring
  have hadd :
      (∫ z : Ω × Ω,
        (f z.1 ^ 2 - 2 * (f z.1 * f z.2)) + f z.2 ^ 2 ∂(μ.prod μ)) =
      (∫ z : Ω × Ω, f z.1 ^ 2 - 2 * (f z.1 * f z.2) ∂(μ.prod μ)) +
        ∫ z : Ω × Ω, f z.2 ^ 2 ∂(μ.prod μ) := by
    simpa only using integral_add hleft hsnd2
  have hsub :
      (∫ z : Ω × Ω, f z.1 ^ 2 - 2 * (f z.1 * f z.2) ∂(μ.prod μ)) =
      (∫ z : Ω × Ω, f z.1 ^ 2 ∂(μ.prod μ)) -
        ∫ z : Ω × Ω, 2 * (f z.1 * f z.2) ∂(μ.prod μ) := by
    simpa only using integral_sub hfst2 htwocross
  have hdecomp := meanSquareDecomposition
    (μ := μ) (f := f) (fbar := fbar) (V := V)
    hf1 hf2 hone hvol hmean
  rw [hexpand, hadd, hsub, integral_const_mul]
  rw [hfstIntegral, hsndIntegral, hcrossIntegral, hmean]
  rw [hdecomp]
  ring

end AMLStabilization
