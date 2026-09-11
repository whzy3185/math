import Mathlib
import AMLStabilization.CrossBoxGreenCore
import AMLStabilization.FiniteGradientCauchyCore
import AMLStabilization.CellEnergyCore

open Set Finset MeasureTheory

namespace AMLStabilization

/-- Gradient of the product coefficient `c * u`, written coordinatewise. -/
noncomputable def cellProductGradient
    {n : ℕ}
    (c u : (Fin (n + 1) → ℝ) → ℝ)
    (gradC gradU : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (x : Fin (n + 1) → ℝ) (i : Fin (n + 1)) : ℝ :=
  c x * gradU x i + u x * gradC x i

/-- Algebraic expansion of the cell-energy gradient pairing. -/
theorem cellProductGradient_pairing_expand
    {n : ℕ}
    (c u : (Fin (n + 1) → ℝ) → ℝ)
    (gradC gradU : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (x : Fin (n + 1) → ℝ) :
    (∑ i : Fin (n + 1),
      gradU x i * cellProductGradient c u gradC gradU x i) =
      c x * (∑ i : Fin (n + 1), (gradU x i) ^ 2) +
        ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i) := by
  calc
    (∑ i : Fin (n + 1),
      gradU x i * cellProductGradient c u gradC gradU x i) =
        ∑ i : Fin (n + 1),
          (c x * (gradU x i) ^ 2 + gradU x i * (u x * gradC x i)) := by
      apply Finset.sum_congr rfl
      intro i hi
      simp only [cellProductGradient]
      ring
    _ = (∑ i : Fin (n + 1), c x * (gradU x i) ^ 2) +
        ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i) := by
      rw [Finset.sum_add_distrib]
    _ = c x * (∑ i : Fin (n + 1), (gradU x i) ^ 2) +
        ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i) := by
      rw [Finset.mul_sum]

/--
Exact cell-energy identity on a rectangular box for `u_t = Δ(c u)`.

Here `q = u - ubar`.  The theorem derives the integration-by-parts identity
from the box divergence theorem through `boxCrossGreenIdentity_from_local_derivatives`;
it does not assume the global PDE energy pairing.
-/
theorem boxCellEnergy_exact_identity_from_local_derivatives
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (u ut c lapProd : (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradC : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (du : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgradProd : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    (ubar dQ : ℝ)
    (hbad : bad.Countable)
    (hucont : ContinuousOn u (Icc a b))
    (hccont : ContinuousOn c (Icc a b))
    (hgradUcont : ∀ i, ContinuousOn (fun x => gradU x i) (Icc a b))
    (hgradCcont : ∀ i, ContinuousOn (fun x => gradC x i) (Icc a b))
    (hudiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt u (du x) x)
    (hgradProdDiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt
        (fun y => cellProductGradient c u gradC gradU y i)
        (dgradProd x i) x)
    (hgradUCoord : ∀ x i, du x (Pi.single i 1) = gradU x i)
    (hlapProd : ∀ x, lapProd x =
      ∑ i : Fin (n + 1), dgradProd x i (Pi.single i 1))
    (hgradUFront : ∀ i (x : Fin n → ℝ), gradU (i.insertNth (b i) x) i = 0)
    (hgradUBack : ∀ i (x : Fin n → ℝ), gradU (i.insertNth (a i) x) i = 0)
    (hgradCFront : ∀ i (x : Fin n → ℝ), gradC (i.insertNth (b i) x) i = 0)
    (hgradCBack : ∀ i (x : Fin n → ℝ), gradC (i.insertNth (a i) x) i = 0)
    (hPDE : ∀ x ∈ Icc a b, ut x = lapProd x)
    (hQderiv : dQ = 2 * ∫ x in Icc a b, (u x - ubar) * ut x)
    (hQutInt : IntegrableOn (fun x => (u x - ubar) * ut x) (Icc a b))
    (hDiffusionInt : IntegrableOn
      (fun x => c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2) (Icc a b))
    (hDriftInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)) (Icc a b)) :
    dQ =
      -2 * (∫ x in Icc a b,
        c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2) -
      2 * (∫ x in Icc a b,
        ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)) := by
  let q : (Fin (n + 1) → ℝ) → ℝ := fun x => u x - ubar
  let gradProd : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ :=
    cellProductGradient c u gradC gradU
  have hqcont : ContinuousOn q (Icc a b) := by
    dsimp [q]
    exact hucont.sub continuousOn_const
  have hgradProdCont : ∀ i,
      ContinuousOn (fun x => gradProd x i) (Icc a b) := by
    intro i
    dsimp [gradProd, cellProductGradient]
    exact (hccont.mul (hgradUcont i)).add (hucont.mul (hgradCcont i))
  have hqdiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt q (du x) x := by
    intro x hx
    dsimp [q]
    exact (hudiff x hx).sub_const ubar
  have hgradProdCoord : ∀ x i, du x (Pi.single i 1) = gradU x i := hgradUCoord
  have hfront : ∀ i (x : Fin n → ℝ), gradProd (i.insertNth (b i) x) i = 0 := by
    intro i x
    dsimp [gradProd, cellProductGradient]
    rw [hgradUFront i x, hgradCFront i x]
    ring
  have hback : ∀ i (x : Fin n → ℝ), gradProd (i.insertNth (a i) x) i = 0 := by
    intro i x
    dsimp [gradProd, cellProductGradient]
    rw [hgradUBack i x, hgradCBack i x]
    ring
  have hPairingInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), gradU x i * gradProd x i) (Icc a b) := by
    have hsum := hDiffusionInt.add hDriftInt
    apply IntegrableOn.congr_fun hsum
    · intro x hx
      exact (cellProductGradient_pairing_expand c u gradC gradU x).symm
    · exact measurableSet_Icc
  have hQLapInt : IntegrableOn (fun x => q x * lapProd x) (Icc a b) := by
    apply IntegrableOn.congr_fun hQutInt
    · intro x hx
      dsimp [q]
      rw [hPDE x hx]
    · exact measurableSet_Icc
  have hGreen := boxCrossGreenIdentity_from_local_derivatives
    hle q lapProd gradU gradProd du dgradProd bad hbad
    hqcont hgradProdCont hqdiff
    (by
      intro x hx i
      simpa [gradProd] using hgradProdDiff x hx i)
    hgradProdCoord hlapProd hfront hback hPairingInt hQLapInt
  have hPDEint :
      (∫ x in Icc a b, q x * ut x) =
        ∫ x in Icc a b, q x * lapProd x := by
    apply integral_congr_ae
    exact ae_restrict_of_forall_mem measurableSet_Icc fun x hx => by
      exact congrArg (fun z : ℝ => q x * z) (hPDE x hx)
  have hPairingExpand :
      (∫ x in Icc a b, ∑ i : Fin (n + 1), gradU x i * gradProd x i) =
        (∫ x in Icc a b, c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2) +
          ∫ x in Icc a b,
            ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i) := by
    calc
      (∫ x in Icc a b, ∑ i : Fin (n + 1), gradU x i * gradProd x i) =
          ∫ x in Icc a b,
            (c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2 +
              ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)) := by
        apply integral_congr_ae
        filter_upwards with x
        exact cellProductGradient_pairing_expand c u gradC gradU x
      _ = (∫ x in Icc a b, c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2) +
          ∫ x in Icc a b,
            ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i) := by
        rw [integral_add hDiffusionInt hDriftInt]
  rw [hPDEint, hGreen, hPairingExpand] at hQderiv
  linarith

/--
The exact box PDE identity implies the raw coercive cell-energy inequality.
This is the functional-analytic input expected by `cellEnergy_raw_dissipation`.
-/
theorem boxCellEnergy_raw_dissipation_from_PDE
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (u ut c lapProd : (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradC : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (du : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgradProd : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    (ubar dQ a0 : ℝ)
    (ha0 : 0 < a0)
    (hbad : bad.Countable)
    (hucont : ContinuousOn u (Icc a b))
    (hccont : ContinuousOn c (Icc a b))
    (hgradUcont : ∀ i, ContinuousOn (fun x => gradU x i) (Icc a b))
    (hgradCcont : ∀ i, ContinuousOn (fun x => gradC x i) (Icc a b))
    (hudiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt u (du x) x)
    (hgradProdDiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt
        (fun y => cellProductGradient c u gradC gradU y i)
        (dgradProd x i) x)
    (hgradUCoord : ∀ x i, du x (Pi.single i 1) = gradU x i)
    (hlapProd : ∀ x, lapProd x =
      ∑ i : Fin (n + 1), dgradProd x i (Pi.single i 1))
    (hgradUFront : ∀ i (x : Fin n → ℝ), gradU (i.insertNth (b i) x) i = 0)
    (hgradUBack : ∀ i (x : Fin n → ℝ), gradU (i.insertNth (a i) x) i = 0)
    (hgradCFront : ∀ i (x : Fin n → ℝ), gradC (i.insertNth (b i) x) i = 0)
    (hgradCBack : ∀ i (x : Fin n → ℝ), gradC (i.insertNth (a i) x) i = 0)
    (hPDE : ∀ x ∈ Icc a b, ut x = lapProd x)
    (hQderiv : dQ = 2 * ∫ x in Icc a b, (u x - ubar) * ut x)
    (hcLower : ∀ x ∈ Icc a b, a0 ≤ c x)
    (hQutInt : IntegrableOn (fun x => (u x - ubar) * ut x) (Icc a b))
    (hDiffusionInt : IntegrableOn
      (fun x => c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2) (Icc a b))
    (hDriftInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)) (Icc a b))
    (hGradLp : MemLp
      (fun x => finiteCoordinateL2Norm (gradU x)) 2
      (volume.restrict (Icc a b)))
    (hDriftLp : MemLp
      (fun x => finiteCoordinateL2Norm (fun i => u x * gradC x i)) 2
      (volume.restrict (Icc a b))) :
    dQ + 2 * a0 *
        (Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradU x i) ^ 2)) ^ 2 ≤
      2 * Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (u x * gradC x i) ^ 2) *
        Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradU x i) ^ 2) := by
  let μ : Measure (Fin (n + 1) → ℝ) := volume.restrict (Icc a b)
  let G : ℝ := ∫ x in Icc a b, ∑ i : Fin (n + 1), (gradU x i) ^ 2
  let H2 : ℝ := ∫ x in Icc a b, ∑ i : Fin (n + 1), (u x * gradC x i) ^ 2
  let X : ℝ := ∫ x in Icc a b,
    ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)
  let D : ℝ := ∫ x in Icc a b,
    c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2
  have hexact := boxCellEnergy_exact_identity_from_local_derivatives
    hle u ut c lapProd gradU gradC du dgradProd bad ubar dQ hbad
    hucont hccont hgradUcont hgradCcont hudiff hgradProdDiff
    hgradUCoord hlapProd hgradUFront hgradUBack hgradCFront hgradCBack
    hPDE hQderiv hQutInt hDiffusionInt hDriftInt
  have hexact' : dQ = -2 * D - 2 * X := by
    simpa [D, X] using hexact
  have hG0 : 0 ≤ G := by
    dsimp [G]
    apply integral_nonneg
    intro x
    exact Finset.sum_nonneg fun i hi => sq_nonneg _
  have hH20 : 0 ≤ H2 := by
    dsimp [H2]
    apply integral_nonneg
    intro x
    exact Finset.sum_nonneg fun i hi => sq_nonneg _
  have hGradSqInt : Integrable
      (fun x => ∑ i : Fin (n + 1), (gradU x i) ^ 2) μ := by
    have hsquare : Integrable
        (fun x => (finiteCoordinateL2Norm (gradU x)) ^ 2) μ := by
      simpa [μ] using hGradLp.integrable_sq
    have heq :
        (fun x => (finiteCoordinateL2Norm (gradU x)) ^ 2) =ᵐ[μ]
          (fun x => ∑ i : Fin (n + 1), (gradU x i) ^ 2) :=
      ae_of_all μ fun x => finiteCoordinateL2Norm_sq (gradU x)
    exact (integrable_congr heq).mp hsquare
  have hAInt : Integrable
      (fun x => a0 * ∑ i : Fin (n + 1), (gradU x i) ^ 2) μ :=
    hGradSqInt.const_mul a0
  have hDInt : Integrable
      (fun x => c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2) μ := by
    simpa [μ, IntegrableOn] using hDiffusionInt
  have hDlower : a0 * G ≤ D := by
    calc
      a0 * G = ∫ x in Icc a b,
          a0 * ∑ i : Fin (n + 1), (gradU x i) ^ 2 := by
        dsimp [G]
        rw [integral_const_mul]
      _ ≤ ∫ x in Icc a b,
          c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2 := by
        apply integral_mono_ae
          (by simpa [μ] using hAInt)
          (by simpa [μ] using hDInt)
        exact ae_restrict_of_forall_mem measurableSet_Icc fun x hx =>
          mul_le_mul_of_nonneg_right (hcLower x hx)
            (Finset.sum_nonneg fun i hi => sq_nonneg _)
      _ = D := by rfl
  have hDriftInt' : Integrable
      (fun x => ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)) μ := by
    simpa [μ, IntegrableOn] using hDriftInt
  have hCS := integral_finiteCoordinate_dot_cauchySchwarz
    (μ := μ)
    gradU (fun x i => u x * gradC x i) hDriftInt'
    (by simpa [μ] using hGradLp) (by simpa [μ] using hDriftLp)
  have hCS' : |X| ≤ Real.sqrt G * Real.sqrt H2 := by
    simpa [μ, X, G, H2] using hCS
  have hnegX : -X ≤ Real.sqrt G * Real.sqrt H2 := by
    exact (neg_le_abs X).trans hCS'
  have hnegX' : -X ≤ Real.sqrt H2 * Real.sqrt G := by
    simpa [mul_comm] using hnegX
  have hraw : dQ + 2 * a0 * G ≤ 2 * Real.sqrt H2 * Real.sqrt G := by
    nlinarith [hexact', hDlower, hnegX']
  have hGsqrt : (Real.sqrt G) ^ 2 = G := Real.sq_sqrt hG0
  simpa [G, H2, hGsqrt, mul_comm, mul_left_comm, mul_assoc] using hraw

end AMLStabilization