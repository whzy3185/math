import Mathlib
import AMLStabilization.BoxCellEnergyPDECore
import AMLStabilization.EnergyDifferentiationCore

open Set Finset MeasureTheory Filter
open scoped Topology

namespace AMLStabilization

/--
Time-dependent rectangular-box cell-energy endpoint for `u_t = Δ(c u)`.

The derivative of the shifted square energy is generated internally from
mathlib's dominated parametric-integral calculus and then fed into the
pointwise-PDE/cross-Green cell-energy estimate.  Thus the caller no longer
supplies an abstract `hQderiv` identity.
-/
theorem timeDependentBoxCellEnergy_raw_dissipation
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (u ut c lapProd : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradC : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (du : ℝ → (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgradProd : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    {ubar a0 t0 : ℝ} {s : Set ℝ}
    {bound : (Fin (n + 1) → ℝ) → ℝ}
    (ha0 : 0 < a0)
    (hs : s ∈ 𝓝 t0)
    (hSquareMeas : ∀ᶠ t in 𝓝 t0,
      AEStronglyMeasurable (fun x => (u t x - ubar) ^ 2)
        (volume.restrict (Icc a b)))
    (hSquareInt : Integrable (fun x => (u t0 x - ubar) ^ 2)
      (volume.restrict (Icc a b)))
    (hDerivMeas : AEStronglyMeasurable
      (fun x => 2 * (u t0 x - ubar) * ut t0 x)
      (volume.restrict (Icc a b)))
    (hDerivBound : ∀ᵐ x ∂(volume.restrict (Icc a b)),
      ∀ t ∈ s, ‖2 * (u t x - ubar) * ut t x‖ ≤ bound x)
    (hBoundInt : Integrable bound (volume.restrict (Icc a b)))
    (hTimeDeriv : ∀ᵐ x ∂(volume.restrict (Icc a b)),
      ∀ t ∈ s, HasDerivAt (fun tau => u tau x) (ut t x) t)
    (hbad : bad.Countable)
    (hucont : ContinuousOn (u t0) (Icc a b))
    (hccont : ContinuousOn (c t0) (Icc a b))
    (hgradUcont : ∀ i, ContinuousOn (fun x => gradU t0 x i) (Icc a b))
    (hgradCcont : ∀ i, ContinuousOn (fun x => gradC t0 x i) (Icc a b))
    (hudiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt (u t0) (du t0 x) x)
    (hgradProdDiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt
        (fun y => cellProductGradient (c t0) (u t0) (gradC t0) (gradU t0) y i)
        (dgradProd t0 x i) x)
    (hgradUCoord : ∀ x i, du t0 x (Pi.single i 1) = gradU t0 x i)
    (hlapProd : ∀ x, lapProd t0 x =
      ∑ i : Fin (n + 1), dgradProd t0 x i (Pi.single i 1))
    (hgradUFront : ∀ i (x : Fin n → ℝ),
      gradU t0 (i.insertNth (b i) x) i = 0)
    (hgradUBack : ∀ i (x : Fin n → ℝ),
      gradU t0 (i.insertNth (a i) x) i = 0)
    (hgradCFront : ∀ i (x : Fin n → ℝ),
      gradC t0 (i.insertNth (b i) x) i = 0)
    (hgradCBack : ∀ i (x : Fin n → ℝ),
      gradC t0 (i.insertNth (a i) x) i = 0)
    (hPDE : ∀ x ∈ Icc a b, ut t0 x = lapProd t0 x)
    (hcLower : ∀ x ∈ Icc a b, a0 ≤ c t0 x)
    (hQutInt : IntegrableOn
      (fun x => (u t0 x - ubar) * ut t0 x) (Icc a b))
    (hDiffusionInt : IntegrableOn
      (fun x => c t0 x * ∑ i : Fin (n + 1), (gradU t0 x i) ^ 2) (Icc a b))
    (hDriftInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1),
        gradU t0 x i * (u t0 x * gradC t0 x i)) (Icc a b))
    (hGradLp : MemLp
      (fun x => finiteCoordinateL2Norm (gradU t0 x)) 2
      (volume.restrict (Icc a b)))
    (hDriftLp : MemLp
      (fun x => finiteCoordinateL2Norm (fun i => u t0 x * gradC t0 x i)) 2
      (volume.restrict (Icc a b))) :
    HasDerivAt
      (fun t => ∫ x in Icc a b, (u t x - ubar) ^ 2)
      (2 * ∫ x in Icc a b, (u t0 x - ubar) * ut t0 x) t0 ∧
    (2 * ∫ x in Icc a b, (u t0 x - ubar) * ut t0 x) +
        2 * a0 *
          (Real.sqrt (∫ x in Icc a b,
            ∑ i : Fin (n + 1), (gradU t0 x i) ^ 2)) ^ 2 ≤
      2 * Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (u t0 x * gradC t0 x i) ^ 2) *
        Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradU t0 x i) ^ 2) := by
  let mu : Measure (Fin (n + 1) → ℝ) := volume.restrict (Icc a b)
  have hShiftTimeDeriv : ∀ᵐ x ∂mu, ∀ t ∈ s,
      HasDerivAt (fun tau => u tau x - ubar) (ut t x) t := by
    filter_upwards [show ∀ᵐ x ∂mu, ∀ t ∈ s,
        HasDerivAt (fun tau => u tau x) (ut t x) t by
      simpa [mu] using hTimeDeriv] with x hx
    intro t ht
    exact (hx t ht).sub_const ubar
  have hderivMu := hasDerivAt_integral_square_of_dominated
    (mu := mu)
    (w := fun t x => u t x - ubar)
    (wt := ut)
    (t0 := t0) (s := s) (bound := bound)
    hs
    (by simpa [mu] using hSquareMeas)
    (by simpa [mu] using hSquareInt)
    (by simpa [mu] using hDerivMeas)
    (by simpa [mu] using hDerivBound)
    (by simpa [mu] using hBoundInt)
    hShiftTimeDeriv
  have hderiv :
      HasDerivAt
        (fun t => ∫ x in Icc a b, (u t x - ubar) ^ 2)
        (2 * ∫ x in Icc a b, (u t0 x - ubar) * ut t0 x) t0 := by
    simpa [mu] using hderivMu
  have hineq := boxCellEnergy_raw_dissipation_from_PDE
    hle (u t0) (ut t0) (c t0) (lapProd t0)
    (gradU t0) (gradC t0) (du t0) (dgradProd t0) bad
    ubar (2 * ∫ x in Icc a b, (u t0 x - ubar) * ut t0 x) a0
    ha0 hbad hucont hccont hgradUcont hgradCcont hudiff hgradProdDiff
    hgradUCoord hlapProd hgradUFront hgradUBack hgradCFront hgradCBack
    hPDE rfl hcLower hQutInt hDiffusionInt hDriftInt hGradLp hDriftLp
  exact ⟨hderiv, hineq⟩

end AMLStabilization
