import Mathlib
import AMLStabilization.WeightedHolderQ
import AMLStabilization.HolderCore
import AMLStabilization.PoincareMeanCore
import AMLStabilization.NonlinearCoercivityAlgebra

open MeasureTheory

namespace AMLStabilization

/-- Exact Poincare-plus-mean-decomposition estimate without the extra factor two. -/
theorem meanSquareBase_of_Poincare_exact
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {f : Omega → ℝ}
    {fbar V Cp grad : ℝ}
    (hCp : 0 ≤ Cp) (hgrad : 0 ≤ grad)
    (hdevnonneg : 0 ≤ (∫ x, (f x - fbar) ^ 2 ∂mu))
    (hPoincare :
      Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂mu) ≤ Cp * grad)
    (hdecomp :
      (∫ x, f x ^ 2 ∂mu) =
        (∫ x, (f x - fbar) ^ 2 ∂mu) + V * fbar ^ 2) :
    (∫ x, f x ^ 2 ∂mu) ≤ Cp ^ 2 * grad ^ 2 + V * fbar ^ 2 := by
  have hrhs : 0 ≤ Cp * grad := mul_nonneg hCp hgrad
  have hsquare :
      (Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂mu)) ^ 2 ≤ (Cp * grad) ^ 2 :=
    (sq_le_sq₀ (Real.sqrt_nonneg _) hrhs).2 hPoincare
  rw [Real.sq_sqrt hdevnonneg] at hsquare
  nlinarith

/-- Mass exponent simplification used after dividing the weighted Holder estimate by the mass. -/
theorem mass_rpow_div_mass
    {m q : ℝ} (hm : 0 < m) (hq : 0 < q) :
    m ^ (1 - 1 / q) / m = m ^ (-1 / q) := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  have hsplit : m ^ (1 - 1 / q) = m * m ^ (-1 / q) := by
    calc
      m ^ (1 - 1 / q) = m ^ (1 + (-1 / q)) := by congr 1 <;> ring
      _ = m ^ (1 : ℝ) * m ^ (-1 / q) := Real.rpow_add hm 1 (-1 / q)
      _ = m * m ^ (-1 / q) := by rw [Real.rpow_one]
  rw [hsplit]
  field_simp [ne_of_gt hm]

/--
Arbitrary-`q` mass-weighted mean estimate. The first weighted moment is proved
by the genuine real-exponent Holder theorem in `WeightedHolderQ`; only the
standard `L^2` fluctuation estimate and Poincare inequality remain as inputs.
-/
theorem integralMassWeightedMeanEstimate_q
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {rho f : Omega → ℝ}
    {m K Cp grad fbar q : ℝ}
    (hq : 2 ≤ q)
    (hm : 0 < m) (hK : 0 ≤ K) (hCp : 0 ≤ Cp) (hgrad : 0 ≤ grad)
    (hrho_nonneg : ∀ x, 0 ≤ rho x)
    (hrho_meas : AEStronglyMeasurable rho mu)
    (hf_meas : AEStronglyMeasurable f mu)
    (hrho_int : Integrable rho mu)
    (hrhof_int : Integrable (fun x => rho x * f x) mu)
    (hweighted_int : Integrable (fun x => rho x * |f x| ^ q) mu)
    (hmass : (∫ x, rho x ∂mu) = m)
    (hrhoL2 : MemLp rho 2 mu)
    (hdevL2 : MemLp (fun x => f x - fbar) 2 mu)
    (hrhoL2bound : Real.sqrt (∫ x, rho x ^ 2 ∂mu) ≤ K)
    (hPoincare : Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂mu) ≤ Cp * grad) :
    |fbar| ≤
      m ^ (-1 / q) * (∫ x, rho x * |f x| ^ q ∂mu) ^ (1 / q) +
        (K * Cp / m) * grad := by
  have hq1 : 1 < q := lt_of_lt_of_le (by norm_num) hq
  have hq0 : 0 < q := lt_trans (by norm_num) hq1
  have hholder := weightedFirstMoment_holder
    (mu := mu) (rho := rho) (f := f) (m := m) (q := q)
    hq1 hrho_nonneg hrho_meas hf_meas hrho_int hweighted_int hmass
  have hdev := weightedDeviation_cauchySchwarz_of_bound
    (mu := mu) (rho := rho) (f := f) (fbar := fbar) (K := K)
    hrhoL2 hdevL2 hrhoL2bound
  have hid := weightedDeviationIntegralIdentity
    (mu := mu) (rho := rho) (f := f) (fbar := fbar) hrho_int hrhof_int
  rw [hmass] at hid
  have hrearr :
      m * fbar =
        (∫ x, rho x * f x ∂mu) -
          (∫ x, rho x * (f x - fbar) ∂mu) := by
    linarith
  have habs :
      m * |fbar| ≤
        |∫ x, rho x * f x ∂mu| +
          |∫ x, rho x * (f x - fbar) ∂mu| := by
    calc
      m * |fbar| = |m * fbar| := by rw [abs_mul, abs_of_pos hm]
      _ = |(∫ x, rho x * f x ∂mu) -
          (∫ x, rho x * (f x - fbar) ∂mu)| := by rw [hrearr]
      _ ≤ |∫ x, rho x * f x ∂mu| +
          |∫ x, rho x * (f x - fbar) ∂mu| := abs_sub _ _
  have hdevP :
      |∫ x, rho x * (f x - fbar) ∂mu| ≤ K * Cp * grad := by
    calc
      _ ≤ K * Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂mu) := hdev
      _ ≤ K * (Cp * grad) := mul_le_mul_of_nonneg_left hPoincare hK
      _ = K * Cp * grad := by ring
  let W : ℝ := ∫ x, rho x * |f x| ^ q ∂mu
  have hW0 : 0 ≤ W := by
    dsimp [W]
    exact integral_nonneg (fun x => mul_nonneg (hrho_nonneg x) (Real.rpow_nonneg (abs_nonneg _) _))
  have hmul :
      m * |fbar| ≤ W ^ (1 / q) * m ^ (1 - 1 / q) + K * Cp * grad := by
    dsimp [W]
    linarith [habs, hholder, hdevP]
  have hdiv :
      |fbar| ≤ (W ^ (1 / q) * m ^ (1 - 1 / q) + K * Cp * grad) / m := by
    exact (le_div_iff₀ hm).2 (by simpa [mul_comm] using hmul)
  have hmexp := mass_rpow_div_mass hm hq0
  calc
    |fbar| ≤ (W ^ (1 / q) * m ^ (1 - 1 / q) + K * Cp * grad) / m := hdiv
    _ = m ^ (-1 / q) * W ^ (1 / q) + (K * Cp / m) * grad := by
      rw [add_div]
      rw [mul_div_assoc]
      rw [mul_comm (W ^ (1 / q)), ← mul_div_assoc, hmexp]
      ring
    _ = m ^ (-1 / q) * (∫ x, rho x * |f x| ^ q ∂mu) ^ (1 / q) +
        (K * Cp / m) * grad := by rfl

/--
Full arbitrary-real-`q >= 2` nonlinear mass-weighted coercivity with the exact
coefficients used in the strengthened manuscript.  The only external geometric
input is the Poincare estimate on the actual domain.
-/
theorem integralNonlinearMassWeightedCoercivity
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {rho f : Omega → ℝ}
    {m K Cp grad fbar V q : ℝ}
    (hq : 2 ≤ q)
    (hm : 0 < m) (hK : 0 ≤ K) (hCp : 0 ≤ Cp) (hgrad : 0 ≤ grad) (hV : 0 ≤ V)
    (hrho_nonneg : ∀ x, 0 ≤ rho x)
    (hrho_meas : AEStronglyMeasurable rho mu)
    (hf_meas : AEStronglyMeasurable f mu)
    (hrho_int : Integrable rho mu)
    (hrhof_int : Integrable (fun x => rho x * f x) mu)
    (hweighted_int : Integrable (fun x => rho x * |f x| ^ q) mu)
    (hmass : (∫ x, rho x ∂mu) = m)
    (hrhoL2 : MemLp rho 2 mu)
    (hdevL2 : MemLp (fun x => f x - fbar) 2 mu)
    (hrhoL2bound : Real.sqrt (∫ x, rho x ^ 2 ∂mu) ≤ K)
    (hf_int : Integrable f mu)
    (hf2_int : Integrable (fun x => f x ^ 2) mu)
    (hone_int : Integrable (fun _ : Omega => (1 : ℝ)) mu)
    (hvol : (∫ _ : Omega, (1 : ℝ) ∂mu) = V)
    (hmean : (∫ x, f x ∂mu) = V * fbar)
    (hPoincare : Real.sqrt (∫ x, (f x - fbar) ^ 2 ∂mu) ≤ Cp * grad) :
    (∫ x, f x ^ 2 ∂mu) ≤
      nonlinearMassWeightedA Cp V K m * grad ^ 2 +
        nonlinearMassWeightedB V m q *
          (∫ x, rho x * |f x| ^ q ∂mu) ^ (2 / q) := by
  have hq0 : 0 < q := lt_of_lt_of_le (by norm_num) hq
  have hdevnonneg : 0 ≤ (∫ x, (f x - fbar) ^ 2 ∂mu) :=
    integral_nonneg (fun x => sq_nonneg (f x - fbar))
  have htotal0 : 0 ≤ (∫ x, f x ^ 2 ∂mu) :=
    integral_nonneg (fun x => sq_nonneg (f x))
  have hW0 : 0 ≤ (∫ x, rho x * |f x| ^ q ∂mu) :=
    integral_nonneg (fun x => mul_nonneg (hrho_nonneg x) (Real.rpow_nonneg (abs_nonneg _) _))
  have hdecomp := meanSquareDecomposition
    (mu := mu) (f := f) (fbar := fbar) (V := V)
    hf_int hf2_int hone_int hvol hmean
  have hbase := meanSquareBase_of_Poincare_exact
    (mu := mu) (f := f) (fbar := fbar) (V := V) (Cp := Cp) (grad := grad)
    hCp hgrad hdevnonneg hPoincare hdecomp
  have hlin := integralMassWeightedMeanEstimate_q
    (mu := mu) (rho := rho) (f := f)
    (m := m) (K := K) (Cp := Cp) (grad := grad) (fbar := fbar) (q := q)
    hq hm hK hCp hgrad hrho_nonneg hrho_meas hf_meas hrho_int hrhof_int hweighted_int
    hmass hrhoL2 hdevL2 hrhoL2bound hPoincare
  let W : ℝ := ∫ x, rho x * |f x| ^ q ∂mu
  have hroot0 : 0 ≤ W ^ (1 / q) := Real.rpow_nonneg hW0 _
  have hbaseSq :
      (Real.sqrt (∫ x, f x ^ 2 ∂mu)) ^ 2 ≤
        Cp ^ 2 * grad ^ 2 + V * |fbar| ^ 2 := by
    rw [Real.sq_sqrt htotal0]
    simpa [sq_abs] using hbase
  have hred := nonlinearMassWeightedCoercivityReduction
    (x := Real.sqrt (∫ x, f x ^ 2 ∂mu))
    (y := grad) (z := W ^ (1 / q)) (a := |fbar|)
    (Cp := Cp) (V := V) (K := K) (m := m) (q := q)
    (Real.sqrt_nonneg _) hgrad hroot0 (abs_nonneg _)
    hCp hV hK hm hq0 hlin hbaseSq
  have hrootSq : (W ^ (1 / q)) ^ 2 = W ^ (2 / q) := by
    rw [← Real.rpow_natCast]
    rw [← Real.rpow_mul hW0]
    congr 1
    field_simp [ne_of_gt hq0]
  rw [Real.sq_sqrt htotal0, hrootSq] at hred
  exact hred

end AMLStabilization
