import Mathlib
import AMLStabilization.TimeDependentBoxMotilityCellEnergyCore
import AMLStabilization.BoxPoincareCellInterfaceCore

open Set Finset MeasureTheory Filter
open scoped Topology

namespace AMLStabilization

/-- Shifted cell `L²` energy on a rectangular box. -/
noncomputable def boxCellEnergy
    {n : ℕ} (a b : Fin (n + 1) → ℝ)
    (u : ℝ → (Fin (n + 1) → ℝ) → ℝ) (ubar t : ℝ) : ℝ :=
  ∫ x in Icc a b, (u t x - ubar) ^ 2

/-- The derivative expression naturally paired with `boxCellEnergy`. -/
noncomputable def boxCellEnergyDerivative
    {n : ℕ} (a b : Fin (n + 1) → ℝ)
    (u ut : ℝ → (Fin (n + 1) → ℝ) → ℝ) (ubar t : ℝ) : ℝ :=
  2 * ∫ x in Icc a b, (u t x - ubar) * ut t x

/-- Spatial `L²` gradient norm used in the cell energy estimate. -/
noncomputable def boxCellGradientNorm
    {n : ℕ} (a b : Fin (n + 1) → ℝ)
    (gradU : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (t : ℝ) : ℝ :=
  Real.sqrt (∫ x in Icc a b,
    ∑ i : Fin (n + 1), (gradU t x i) ^ 2)

/-- Spatial `L²` signal-gradient norm. -/
noncomputable def boxSignalGradientNorm
    {n : ℕ} (a b : Fin (n + 1) → ℝ)
    (gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (t : ℝ) : ℝ :=
  Real.sqrt (∫ x in Icc a b,
    ∑ i : Fin (n + 1), (gradV t x i) ^ 2)

/-- Manuscript forcing norm `U L_phi ||grad v||_2`. -/
noncomputable def boxMotilityForcingNorm
    {n : ℕ} (a b : Fin (n + 1) → ℝ) (U L : ℝ)
    (gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (t : ℝ) : ℝ :=
  (U * L) * boxSignalGradientNorm a b gradV t

/-- Effective Poincare constant supplied by the fully assembled box theorem. -/
noncomputable def boxPoincareConstant (n : ℕ) (C : ℝ) : ℝ :=
  Real.sqrt (n + 1 : ℝ) * C

/--
The six scalar facts expected by the downstream cell-energy ODE assembly at a
single time.  This is only a packaging structure; the box theorem below
constructs all six fields from concrete PDE, regularity, and geometric data.
-/
structure CellEnergyPointwiseInterfaces
    (Q dQ g H : ℝ → ℝ) (a Cp t : ℝ) : Prop where
  deriv : HasDerivAt Q (dQ t) t
  Q_nonneg : 0 ≤ Q t
  g_nonneg : 0 ≤ g t
  H_nonneg : 0 ≤ H t
  poincare : Q t ≤ Cp ^ 2 * g t ^ 2
  energy : dQ t + 2 * a * g t ^ 2 ≤ 2 * H t * g t

/--
At one time slice, the rectangular-box motility PDE plus the fully assembled
box Poincare theorem generate every scalar interface needed by
`CellEnergyAssembly`.

In particular, no abstract energy identity, energy derivative, Poincare
inequality, or motility forcing bound is supplied by the caller.
-/
theorem boxMotilityCell_scalarInterfaces_at
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (hside : ∀ j, a j < b j)
    {C : ℝ} (hC : 0 ≤ C)
    (hSideBound : ∀ j, b j - a j ≤ C)
    (u ut v lapProd : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (phi phiPrime : ℝ → ℝ)
    (gradU gradV : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (du : ℝ → (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgradProd : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    {ubar a0 U L t0 : ℝ} {s : Set ℝ}
    {bound : (Fin (n + 1) → ℝ) → ℝ}
    (ha0 : 0 < a0) (hU0 : 0 ≤ U) (hL0 : 0 ≤ L)
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
    (hvcont : ContinuousOn (v t0) (Icc a b))
    (hphiCont : Continuous phi)
    (hphiPrimeCont : Continuous phiPrime)
    (hgradUcont : ∀ i, ContinuousOn (fun x => gradU t0 x i) (Icc a b))
    (hgradVcont : ∀ i, ContinuousOn (fun x => gradV t0 x i) (Icc a b))
    (hudiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt (u t0) (du t0 x) x)
    (hgradProdDiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt
        (fun y => cellProductGradient
          (fun z => phi (v t0 z)) (u t0)
          (fun z j => motilityCoordinateGradient
            (fun q => phiPrime (v t0 q)) (gradV t0) z j)
          (gradU t0) y i)
        (dgradProd t0 x i) x)
    (hgradUCoord : ∀ x i, du t0 x (Pi.single i 1) = gradU t0 x i)
    (hlapProd : ∀ x, lapProd t0 x =
      ∑ i : Fin (n + 1), dgradProd t0 x i (Pi.single i 1))
    (hgradUFront : ∀ i (x : Fin n → ℝ),
      gradU t0 (i.insertNth (b i) x) i = 0)
    (hgradUBack : ∀ i (x : Fin n → ℝ),
      gradU t0 (i.insertNth (a i) x) i = 0)
    (hgradVFront : ∀ i (x : Fin n → ℝ),
      gradV t0 (i.insertNth (b i) x) i = 0)
    (hgradVBack : ∀ i (x : Fin n → ℝ),
      gradV t0 (i.insertNth (a i) x) i = 0)
    (hPDE : ∀ x ∈ Icc a b, ut t0 x = lapProd t0 x)
    (hcLower : ∀ x ∈ Icc a b, a0 ≤ phi (v t0 x))
    (hQutInt : IntegrableOn
      (fun x => (u t0 x - ubar) * ut t0 x) (Icc a b))
    (hGradULp : MemLp
      (fun x => finiteCoordinateL2Norm (gradU t0 x)) 2
      (volume.restrict (Icc a b)))
    (hGradVLp : MemLp
      (fun x => finiteCoordinateL2Norm (gradV t0 x)) 2
      (volume.restrict (Icc a b)))
    (hUBound : ∀ x ∈ Icc a b, |u t0 x| ≤ U)
    (hPhiPrimeBound : ∀ x ∈ Icc a b, |phiPrime (v t0 x)| ≤ L)
    (hmean : rectangularBoxMean a b (u t0) = ubar)
    (hULp : MemLp (u t0) 2 (rectangularBoxMeasure a b))
    (hPairDiffInt : Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        ((u t0) (fun i => (z i).1) - (u t0) (fun i => (z i).2)) ^ 2)
      (rectangularPairedBoxMeasure a b))
    (hStepInt : ∀ i : Fin (n + 1), Integrable
      (fun z : Fin (n + 1) → ℝ × ℝ =>
        (pairedCoordinateIncrement (u t0) z i.val) ^ 2)
      (rectangularPairedBoxMeasure a b))
    (hDerivInt : ∀ i : Fin (n + 1), Integrable
      (fun x : Fin (n + 1) → ℝ => (gradU t0 x i) ^ 2)
      (rectangularBoxMeasure a b))
    (hFiberDeriv : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ∀ r ∈ Icc (a i) (b i),
        HasDerivAt (fun q => (u t0) (i.insertNth q xr))
          (gradU t0 (i.insertNth r xr) i) r)
    (hFiberCont : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ContinuousOn (fun r => (u t0) (i.insertNth r xr)) (Icc (a i) (b i)))
    (hFiberDCont : ∀ i : Fin (n + 1), ∀ xr : Fin n → ℝ,
      ContinuousOn (fun r => gradU t0 (i.insertNth r xr) i)
        (Icc (a i) (b i))) :
    CellEnergyPointwiseInterfaces
      (boxCellEnergy a b u ubar)
      (boxCellEnergyDerivative a b u ut ubar)
      (boxCellGradientNorm a b gradU)
      (boxMotilityForcingNorm a b U L gradV)
      a0 (boxPoincareConstant n C) t0 := by
  have hpde := timeDependentBoxMotilityCellEnergy_raw_dissipation
    hle u ut v lapProd phi phiPrime gradU gradV du dgradProd bad
    (ubar := ubar) (a0 := a0) (U := U) (L := L) (t0 := t0)
    (s := s) (bound := bound)
    ha0 hU0 hL0 hs hSquareMeas hSquareInt hDerivMeas hDerivBound
    hBoundInt hTimeDeriv hbad hucont hvcont hphiCont hphiPrimeCont
    hgradUcont hgradVcont hudiff hgradProdDiff hgradUCoord hlapProd
    hgradUFront hgradUBack hgradVFront hgradVBack hPDE hcLower hQutInt
    hGradULp hGradVLp hUBound hPhiPrimeBound
  have hpoincare := rectangularBoxPoincare_cellEnergyForm
    hside hC hSideBound (u t0) (gradU t0) hmean hULp hPairDiffInt
    hStepInt hDerivInt hFiberDeriv hFiberCont hFiberDCont
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · change HasDerivAt
      (fun t => ∫ x in Icc a b, (u t x - ubar) ^ 2)
      (2 * ∫ x in Icc a b, (u t0 x - ubar) * ut t0 x) t0
    exact hpde.1
  · dsimp [boxCellEnergy]
    apply integral_nonneg
    intro x
    exact sq_nonneg _
  · exact Real.sqrt_nonneg _
  · dsimp [boxMotilityForcingNorm, boxSignalGradientNorm]
    exact mul_nonneg (mul_nonneg hU0 hL0) (Real.sqrt_nonneg _)
  · simpa [boxCellEnergy, boxCellGradientNorm, boxPoincareConstant] using hpoincare
  · simpa [boxCellEnergyDerivative, boxCellGradientNorm,
      boxMotilityForcingNorm, boxSignalGradientNorm] using hpde.2

end AMLStabilization
