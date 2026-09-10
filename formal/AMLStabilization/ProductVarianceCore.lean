import Mathlib

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
    simpa only [Pi.sub_apply] using hfst2.sub htwocross
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
  ring

end AMLStabilization
