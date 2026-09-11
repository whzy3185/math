import Mathlib
import AMLStabilization.BoxCellEnergyPDECore
import AMLStabilization.BoxMotilityForcingCore
import AMLStabilization.MotilityChainRuleCore

open Set Finset MeasureTheory

namespace AMLStabilization

/--
Rectangular-box cell-energy estimate for the signal-dependent coefficient
`c = phi(v)`.

The coefficient-gradient continuity and Neumann face conditions are generated
from `grad v`; compact-box continuity supplies the diffusion/drift
integrability; and `BoxMotilityForcingCore` generates both the drift `L²`
membership and the manuscript forcing bound `H ≤ U L ||grad v||₂`.
-/
theorem boxMotilityCellEnergy_raw_dissipation_from_PDE
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (u ut v : (Fin (n + 1) → ℝ) → ℝ)
    (phi phiPrime : ℝ → ℝ)
    (lapProd : (Fin (n + 1) → ℝ) → ℝ)
    (gradU gradV : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (du : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgradProd : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    (ubar dQ a0 U L : ℝ)
    (ha0 : 0 < a0) (hU0 : 0 ≤ U) (hL0 : 0 ≤ L)
    (hbad : bad.Countable)
    (hucont : ContinuousOn u (Icc a b))
    (hvcont : ContinuousOn v (Icc a b))
    (hphiCont : Continuous phi)
    (hphiPrimeCont : Continuous phiPrime)
    (hgradUcont : ∀ i, ContinuousOn (fun x => gradU x i) (Icc a b))
    (hgradVcont : ∀ i, ContinuousOn (fun x => gradV x i) (Icc a b))
    (hudiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt u (du x) x)
    (hgradProdDiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt
        (fun y => cellProductGradient
          (fun z => phi (v z)) u
          (fun z j => motilityCoordinateGradient
            (fun q => phiPrime (v q)) gradV z j)
          gradU y i)
        (dgradProd x i) x)
    (hgradUCoord : ∀ x i, du x (Pi.single i 1) = gradU x i)
    (hlapProd : ∀ x, lapProd x =
      ∑ i : Fin (n + 1), dgradProd x i (Pi.single i 1))
    (hgradUFront : ∀ i (x : Fin n → ℝ), gradU (i.insertNth (b i) x) i = 0)
    (hgradUBack : ∀ i (x : Fin n → ℝ), gradU (i.insertNth (a i) x) i = 0)
    (hgradVFront : ∀ i (x : Fin n → ℝ), gradV (i.insertNth (b i) x) i = 0)
    (hgradVBack : ∀ i (x : Fin n → ℝ), gradV (i.insertNth (a i) x) i = 0)
    (hPDE : ∀ x ∈ Icc a b, ut x = lapProd x)
    (hQderiv : dQ = 2 * ∫ x in Icc a b, (u x - ubar) * ut x)
    (hcLower : ∀ x ∈ Icc a b, a0 ≤ phi (v x))
    (hQutInt : IntegrableOn (fun x => (u x - ubar) * ut x) (Icc a b))
    (hGradULp : MemLp
      (fun x => finiteCoordinateL2Norm (gradU x)) 2
      (volume.restrict (Icc a b)))
    (hGradVLp : MemLp
      (fun x => finiteCoordinateL2Norm (gradV x)) 2
      (volume.restrict (Icc a b)))
    (hUBound : ∀ x ∈ Icc a b, |u x| ≤ U)
    (hPhiPrimeBound : ∀ x ∈ Icc a b, |phiPrime (v x)| ≤ L) :
    dQ + 2 * a0 *
        (Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradU x i) ^ 2)) ^ 2 ≤
      2 * ((U * L) * Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradV x i) ^ 2)) *
        Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradU x i) ^ 2) := by
  let c : (Fin (n + 1) → ℝ) → ℝ := fun x => phi (v x)
  let phiPrimeSpace : (Fin (n + 1) → ℝ) → ℝ := fun x => phiPrime (v x)
  let gradC : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ :=
    fun x i => motilityCoordinateGradient phiPrimeSpace gradV x i
  have hccont : ContinuousOn c (Icc a b) := by
    dsimp [c]
    exact hphiCont.comp_continuousOn hvcont
  have hphiPrimeSpaceCont : ContinuousOn phiPrimeSpace (Icc a b) := by
    dsimp [phiPrimeSpace]
    exact hphiPrimeCont.comp_continuousOn hvcont
  have hgradCcont : ∀ i, ContinuousOn (fun x => gradC x i) (Icc a b) := by
    dsimp [gradC]
    exact motilityCoordinateGradient_continuousOn hphiPrimeSpaceCont hgradVcont
  have hgradCFront : ∀ i (x : Fin n → ℝ), gradC (i.insertNth (b i) x) i = 0 := by
    dsimp [gradC]
    exact motilityCoordinateGradient_front_zero
      (a := a) (b := b) (phiPrime := phiPrimeSpace) (gradV := gradV) hgradVFront
  have hgradCBack : ∀ i (x : Fin n → ℝ), gradC (i.insertNth (a i) x) i = 0 := by
    dsimp [gradC]
    exact motilityCoordinateGradient_back_zero
      (a := a) (b := b) (phiPrime := phiPrimeSpace) (gradV := gradV) hgradVBack
  have hGradUSqCont : ContinuousOn
      (fun x => ∑ i : Fin (n + 1), (gradU x i) ^ 2) (Icc a b) := by
    exact continuousOn_finsetSum Finset.univ fun i hi => (hgradUcont i).pow 2
  have hDiffusionInt : IntegrableOn
      (fun x => c x * ∑ i : Fin (n + 1), (gradU x i) ^ 2) (Icc a b) :=
    (hccont.mul hGradUSqCont).integrableOn_compact isCompact_Icc
  have hDriftCoordCont : ∀ i, ContinuousOn
      (fun x => gradU x i * (u x * gradC x i)) (Icc a b) := by
    intro i
    exact (hgradUcont i).mul (hucont.mul (hgradCcont i))
  have hDriftInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)) (Icc a b) := by
    have hcont : ContinuousOn
        (fun x => ∑ i : Fin (n + 1), gradU x i * (u x * gradC x i)) (Icc a b) :=
      continuousOn_finsetSum Finset.univ fun i hi => hDriftCoordCont i
    exact hcont.integrableOn_compact isCompact_Icc
  have hforce := boxMotilityDrift_memLp_and_L2_bound
    u phiPrimeSpace gradV hU0 hL0 hucont hphiPrimeSpaceCont hgradVcont
    hUBound
    (by
      intro x hx
      simpa [phiPrimeSpace] using hPhiPrimeBound x hx)
    hGradVLp
  have hDriftLp : MemLp
      (fun x => finiteCoordinateL2Norm (fun i => u x * gradC x i)) 2
      (volume.restrict (Icc a b)) := by
    simpa [gradC, phiPrimeSpace] using hforce.1
  have hHbound :
      Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (u x * gradC x i) ^ 2) ≤
        (U * L) * Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradV x i) ^ 2) := by
    simpa [gradC, phiPrimeSpace] using hforce.2
  have hraw := boxCellEnergy_raw_dissipation_from_PDE
    hle u ut c lapProd gradU gradC du dgradProd bad
    ubar dQ a0 ha0 hbad hucont hccont hgradUcont hgradCcont hudiff
    (by simpa [c, gradC, phiPrimeSpace] using hgradProdDiff)
    hgradUCoord hlapProd hgradUFront hgradUBack hgradCFront hgradCBack
    hPDE hQderiv
    (by simpa [c] using hcLower)
    hQutInt hDiffusionInt hDriftInt hGradULp hDriftLp
  have hGradU0 : 0 ≤ Real.sqrt (∫ x in Icc a b,
      ∑ i : Fin (n + 1), (gradU x i) ^ 2) := Real.sqrt_nonneg _
  have hRhs :
      2 * Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (u x * gradC x i) ^ 2) *
        Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradU x i) ^ 2) ≤
      2 * ((U * L) * Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradV x i) ^ 2)) *
        Real.sqrt (∫ x in Icc a b,
          ∑ i : Fin (n + 1), (gradU x i) ^ 2) := by
    gcongr
  exact hraw.trans hRhs

end AMLStabilization
