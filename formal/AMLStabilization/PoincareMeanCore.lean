import Mathlib
import AMLStabilization.HolderCoercivityBridge

open MeasureTheory

namespace AMLStabilization

/--
Exact mean-square decomposition from the integral definition of the mean.
The finite-volume information is encoded by `∫ 1 = V`, and the mean relation by
`∫ f = V * fbar`.
-/
theorem meanSquareDecomposition
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {f : Ω → ℝ} {fbar V : ℝ}
    (hf : Integrable f μ)
    (hf2 : Integrable (fun x => f x ^ 2) μ)
    (hone : Integrable (fun _ : Ω => (1 : ℝ)) μ)
    (hvol : (∫ _ : Ω, (1 : ℝ) ∂μ) = V)
    (hmean : (∫ x, f x ∂μ) = V * fbar) :
    (∫ x, f x ^ 2 ∂μ) =
      (∫ x, (f x - fbar) ^ 2 ∂μ) + V * fbar ^ 2 := by
  have hcross : Integrable (fun x => (2 * fbar) * f x) μ :=
    hf.const_mul (2 * fbar)
  have hconst : Integrable (fun x : Ω => (fbar ^ 2) * (1 : ℝ)) μ :=
    hone.const_mul (fbar ^ 2)
  have hpoint :
      (fun x => (f x - fbar) ^ 2) =
        (fun x => (f x ^ 2 - (2 * fbar) * f x) + (fbar ^ 2) * (1 : ℝ)) := by
    funext x
    ring
  have hdev :
      (∫ x, (f x - fbar) ^ 2 ∂μ) =
        (∫ x, f x ^ 2 ∂μ) - V * fbar ^ 2 := by
    rw [hpoint]
    calc
      (∫ x, (f x ^ 2 - (2 * fbar) * f x) + (fbar ^ 2) * (1 : ℝ) ∂μ) =
          (∫ x, f x ^ 2 - (2 * fbar) * f x ∂μ) +
            (∫ x, (fbar ^ 2) * (1 : ℝ) ∂μ) := by
              exact integral_add (hf2.sub hcross) hconst
      _ = ((∫ x, f x ^ 2 ∂μ) - (∫ x, (2 * fbar) * f x ∂μ)) +
            (∫ x, (fbar ^ 2) * (1 : ℝ) ∂μ) := by
              rw [integral_sub hf2 hcross]
      _ = (∫ x, f x ^ 2 ∂μ) - V * fbar ^ 2 := by
              rw [integral_const_mul, integral_const_mul, hvol, hmean]
              ring
  linarith

/--
Poincare plus the exact mean-square decomposition implies the base estimate
required by the mass-weighted coercivity layer.  This theorem deliberately
keeps the geometric Poincare estimate as an explicit interface, because mathlib
currently has no general theorem for arbitrary smooth bounded connected domains.
-/
theorem meanSquareBase_of_Poincare
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {f : Ω → ℝ}
    {fbar V Cp grad : ℝ}
    (hCp : 0 ≤ Cp)
    (hgrad : 0 ≤ grad)
    (hV : 0 ≤ V)
    (hdevnonneg : 0 ≤ (∫ x, (f x - fbar) ^ 2 ∂μ))
    (hPoincare :
      Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) ≤ Cp * grad)
    (hdecomp :
      (∫ x, f x ^ 2 ∂μ) =
        (∫ x, (f x - fbar) ^ 2 ∂μ) + V * fbar ^ 2) :
    (∫ x, f x ^ 2 ∂μ) ≤
      2 * Cp ^ 2 * grad ^ 2 + 2 * V * fbar ^ 2 := by
  have hrhs : 0 ≤ Cp * grad := mul_nonneg hCp hgrad
  have hsquare :
      (Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ)) ^ 2 ≤ (Cp * grad) ^ 2 := by
    exact (sq_le_sq₀ (Real.sqrt_nonneg _) hrhs).2 hPoincare
  rw [Real.sq_sqrt hdevnonneg] at hsquare
  have hVterm : 0 ≤ V * fbar ^ 2 := mul_nonneg hV (sq_nonneg fbar)
  nlinarith [hsquare]

/--
Version of `integralMassWeightedCoercivity_of_MemLp` where the former abstract
base mean-decomposition estimate is generated internally from actual integrals.
Only the geometric Poincare estimate remains external.
-/
theorem integralMassWeightedCoercivity_of_MemLp_and_Poincare
    {Ω : Type*} [MeasurableSpace Ω]
    {μ : Measure Ω} {ρ f : Ω → ℝ}
    {m K Cp grad fbar V : ℝ}
    (hm : 0 < m)
    (hK0 : 0 ≤ K)
    (hCp : 0 ≤ Cp)
    (hgrad : 0 ≤ grad)
    (hV : 0 ≤ V)
    (hρnonneg : ∀ x, 0 ≤ ρ x)
    (hρint : Integrable ρ μ)
    (hρfint : Integrable (fun x => ρ x * f x) μ)
    (hmass : (∫ x, ρ x ∂μ) = m)
    (hsqrtρ : MemLp (fun x => Real.sqrt (ρ x)) 2 μ)
    (hsqrtρf : MemLp (fun x => Real.sqrt (ρ x) * f x) 2 μ)
    (hρL2 : MemLp ρ 2 μ)
    (hdevL2 : MemLp (fun x => f x - fbar) 2 μ)
    (hρL2bound : Real.sqrt (∫ x, ρ x ^ 2 ∂μ) ≤ K)
    (hf : Integrable f μ)
    (hf2 : Integrable (fun x => f x ^ 2) μ)
    (hone : Integrable (fun _ : Ω => (1 : ℝ)) μ)
    (hvol : (∫ _ : Ω, (1 : ℝ) ∂μ) = V)
    (hmean : (∫ x, f x ∂μ) = V * fbar)
    (hPoincare :
      Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂μ) ≤ Cp * grad) :
    (∫ x, f x ^ 2 ∂μ) ≤
      (2 * Cp ^ 2 + 4 * V * (K * Cp / m) ^ 2) * grad ^ 2 +
        4 * V * (Real.sqrt m / m) ^ 2 *
          (∫ x, ρ x * f x ^ 2 ∂μ) := by
  have hdevnonneg : 0 ≤ (∫ x, (f x - fbar) ^ 2 ∂μ) := by
    exact integral_nonneg (fun x => sq_nonneg (f x - fbar))
  have hdecomp := meanSquareDecomposition
    (μ := μ) (f := f) (fbar := fbar) (V := V)
    hf hf2 hone hvol hmean
  have hbase := meanSquareBase_of_Poincare
    (μ := μ) (f := f) (fbar := fbar) (V := V)
    (Cp := Cp) (grad := grad)
    hCp hgrad hV hdevnonneg hPoincare hdecomp
  exact integralMassWeightedCoercivity_of_MemLp
    (μ := μ) (ρ := ρ) (f := f)
    (m := m) (K := K) (Cp := Cp) (grad := grad) (fbar := fbar) (V := V)
    hm hK0 hCp hgrad hV hρnonneg hρint hρfint hmass
    hsqrtρ hsqrtρf hρL2 hdevL2 hρL2bound hPoincare hbase

end AMLStabilization
