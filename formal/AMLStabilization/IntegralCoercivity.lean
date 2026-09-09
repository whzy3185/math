import Mathlib
import AMLStabilization.AlgebraicCore

open MeasureTheory

namespace AMLStabilization

/--
Integral identity behind the weighted-mean estimate.  This is the exact step
that rewrites the weighted fluctuation in terms of the weighted first moment
and the total mass.
-/
theorem weightedDeviationIntegralIdentity
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ} {fbar : ℝ}
    (hρ : Integrable ρ μ)
    (hρf : Integrable (fun x => ρ x * f x) μ) :
    (∫ x, ρ x * (f x - fbar) ∂μ) =
      (∫ x, ρ x * f x ∂μ) - fbar * (∫ x, ρ x ∂μ) := by
  have hfun :
      (fun x => ρ x * (f x - fbar)) =
        (fun x => ρ x * f x - fbar * ρ x) := by
    funext x
    ring
  rw [hfun, integral_sub hρf (hρ.const_mul fbar), integral_const_mul]

/--
Integral/Poincare layer of the mass-weighted mean estimate.

The two Cauchy-Schwarz type bounds are supplied as analytic inputs:
* weighted first moment against `ρ`;
* weighted fluctuation against `ρ`.
The theorem verifies the integral identity, triangle estimate, Poincare step,
and division by the conserved mass.
-/
theorem integralMassWeightedMeanEstimate
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ}
    {m K Cp grad fbar : ℝ}
    (hm : 0 < m)
    (hK : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hgrad : 0 ≤ grad)
    (hρ : Integrable ρ μ)
    (hρf : Integrable (fun x => ρ x * f x) μ)
    (hmass : (∫ x, ρ x ∂μ) = m)
    (hweightedCS :
      |∫ x, ρ x * f x ∂μ| ≤
        Real.sqrt m * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ))
    (hdeviationCS :
      |∫ x, ρ x * (f x - fbar) ∂μ| ≤
        K * Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ))
    (hPoincare :
      Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) ≤ Cp * grad) :
    |fbar| ≤
      (Real.sqrt m / m) * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ) +
        (K * Cp / m) * grad := by
  have hid := weightedDeviationIntegralIdentity
    (μ := μ) (ρ := ρ) (f := f) (fbar := fbar) hρ hρf
  rw [hmass] at hid
  have hrearr :
      m * fbar =
        (∫ x, ρ x * f x ∂μ) -
          (∫ x, ρ x * (f x - fbar) ∂μ) := by
    linarith
  have habs :
      m * |fbar| ≤
        |∫ x, ρ x * f x ∂μ| +
          |∫ x, ρ x * (f x - fbar) ∂μ| := by
    calc
      m * |fbar| = |m * fbar| := by
        rw [abs_mul, abs_of_pos hm]
      _ =
          |(∫ x, ρ x * f x ∂μ) -
            (∫ x, ρ x * (f x - fbar) ∂μ)| := by
          rw [hrearr]
      _ ≤
          |∫ x, ρ x * f x ∂μ| +
            |∫ x, ρ x * (f x - fbar) ∂μ| := abs_sub _ _
  have hdev :
      |∫ x, ρ x * (f x - fbar) ∂μ| ≤ K * Cp * grad := by
    calc
      |∫ x, ρ x * (f x - fbar) ∂μ| ≤
          K * Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) := hdeviationCS
      _ ≤ K * (Cp * grad) := by
        exact mul_le_mul_of_nonneg_left hPoincare hK
      _ = K * Cp * grad := by ring
  have hmul :
      m * |fbar| ≤
        Real.sqrt m * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ) +
          K * Cp * grad := by
    linarith [habs, hweightedCS, hdev]
  calc
    |fbar| ≤
        (Real.sqrt m * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ) +
          K * Cp * grad) / m := by
      apply (le_div_iff₀ hm).2
      nlinarith [hmul]
    _ =
        (Real.sqrt m / m) * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ) +
          (K * Cp / m) * grad := by
      field_simp [ne_of_gt hm]

/--
Full integral coercivity reduction.  Poincare/mean decomposition and the two
Cauchy-Schwarz bounds are explicit analytic inputs; all remaining integral
algebra and coercivity closure are checked in Lean.
-/
theorem integralMassWeightedCoercivity
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ}
    {m K Cp grad fbar V : ℝ}
    (hm : 0 < m)
    (hK : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hgrad : 0 ≤ grad)
    (hV : 0 ≤ V)
    (hρnonneg : ∀ x, 0 ≤ ρ x)
    (hρ : Integrable ρ μ)
    (hρf : Integrable (fun x => ρ x * f x) μ)
    (hmass : (∫ x, ρ x ∂μ) = m)
    (hweightedCS :
      |∫ x, ρ x * f x ∂μ| ≤
        Real.sqrt m * Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ))
    (hdeviationCS :
      |∫ x, ρ x * (f x - fbar) ∂μ| ≤
        K * Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ))
    (hPoincare :
      Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) ≤ Cp * grad)
    (hbase :
      (∫ x, f x ^ 2 ∂μ) ≤
        2 * Cp ^ 2 * grad ^ 2 + 2 * V * fbar ^ 2) :
    (∫ x, f x ^ 2 ∂μ) ≤
      (2 * Cp ^ 2 + 4 * V * (K * Cp / m) ^ 2) * grad ^ 2 +
        4 * V * (Real.sqrt m / m) ^ 2 *
          (∫ x, ρ x * f x ^ 2 ∂μ) := by
  have htotal : 0 ≤ (∫ x, f x ^ 2 ∂μ) := by
    exact integral_nonneg (fun x => sq_nonneg (f x))
  have hweighted : 0 ≤ (∫ x, ρ x * f x ^ 2 ∂μ) := by
    exact integral_nonneg (fun x => mul_nonneg (hρnonneg x) (sq_nonneg (f x)))
  have hlin := integralMassWeightedMeanEstimate
    (μ := μ) (ρ := ρ) (f := f)
    (m := m) (K := K) (Cp := Cp) (grad := grad) (fbar := fbar)
    hm hK hCp hgrad hρ hρf hmass hweightedCS hdeviationCS hPoincare
  have hbase' :
      (Real.sqrt (∫ x, f x ^ 2 ∂μ)) ^ 2 ≤
        2 * Cp ^ 2 * grad ^ 2 + 2 * V * |fbar| ^ 2 := by
    rw [Real.sq_sqrt htotal]
    simpa [sq_abs] using hbase
  have hred := massWeightedCoercivityReduction
    (x := Real.sqrt (∫ x, f x ^ 2 ∂μ))
    (y := grad)
    (z := Real.sqrt (∫ x, ρ x * f x ^ 2 ∂μ))
    (a := |fbar|)
    (Cp := Cp)
    (V := V)
    (A := Real.sqrt m / m)
    (B := K * Cp / m)
    (abs_nonneg fbar)
    (Real.sqrt_nonneg _)
    hgrad
    (div_nonneg (Real.sqrt_nonneg _) (le_of_lt hm))
    (div_nonneg (mul_nonneg hK hCp) (le_of_lt hm))
    hV
    hlin
    hbase'
  rw [Real.sq_sqrt htotal, Real.sq_sqrt hweighted] at hred
  exact hred

end AMLStabilization
