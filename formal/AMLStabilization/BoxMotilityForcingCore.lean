import Mathlib
import AMLStabilization.MotilityForcingCore

open Set Finset MeasureTheory

namespace AMLStabilization

/--
Rectangular-box specialization of the motility forcing estimate.

Continuity on the compact box generates the strong measurability of the drift
norm internally, while pointwise bounds on `u` and `phiPrime` are converted to
the restricted-volume a.e. bounds required by `motilityDrift_memLp_and_L2_bound`.
Thus no separate drift-measurability hypothesis is exposed.
-/
theorem boxMotilityDrift_memLp_and_L2_bound
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (u phiPrime : (Fin (n + 1) → ℝ) → ℝ)
    (gradV : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    {U L : ℝ}
    (hU0 : 0 ≤ U) (hL0 : 0 ≤ L)
    (hucont : ContinuousOn u (Icc a b))
    (hphiCont : ContinuousOn phiPrime (Icc a b))
    (hgradVcont : ∀ i, ContinuousOn (fun x => gradV x i) (Icc a b))
    (hU : ∀ x ∈ Icc a b, |u x| ≤ U)
    (hPhi : ∀ x ∈ Icc a b, |phiPrime x| ≤ L)
    (hGradLp : MemLp
      (fun x => finiteCoordinateL2Norm (gradV x)) 2
      (volume.restrict (Icc a b))) :
    MemLp
        (fun x => finiteCoordinateL2Norm
          (fun i => u x * motilityCoordinateGradient phiPrime gradV x i)) 2
        (volume.restrict (Icc a b)) ∧
      Real.sqrt (∫ x in Icc a b,
          ∑ i, (u x * motilityCoordinateGradient phiPrime gradV x i) ^ 2) ≤
        (U * L) * Real.sqrt (∫ x in Icc a b,
          ∑ i, (gradV x i) ^ 2) := by
  have hgradCcont : ∀ i,
      ContinuousOn (fun x => motilityCoordinateGradient phiPrime gradV x i)
        (Icc a b) :=
    motilityCoordinateGradient_continuousOn hphiCont hgradVcont
  have hDriftCoordCont : ∀ i,
      ContinuousOn
        (fun x => u x * motilityCoordinateGradient phiPrime gradV x i)
        (Icc a b) := by
    intro i
    exact hucont.mul (hgradCcont i)
  have hDriftSqCont : ContinuousOn
      (fun x => ∑ i : Fin (n + 1),
        (u x * motilityCoordinateGradient phiPrime gradV x i) ^ 2)
      (Icc a b) := by
    exact continuousOn_finsetSum Finset.univ fun i hi =>
      (hDriftCoordCont i).pow 2
  have hDriftNormCont : ContinuousOn
      (fun x => finiteCoordinateL2Norm
        (fun i => u x * motilityCoordinateGradient phiPrime gradV x i))
      (Icc a b) := by
    unfold finiteCoordinateL2Norm
    exact Real.continuous_sqrt.comp_continuousOn hDriftSqCont
  have hDriftMeas : AEStronglyMeasurable
      (fun x => finiteCoordinateL2Norm
        (fun i => u x * motilityCoordinateGradient phiPrime gradV x i))
      (volume.restrict (Icc a b)) :=
    hDriftNormCont.aestronglyMeasurable measurableSet_Icc
  have hUae : ∀ᵐ x ∂(volume.restrict (Icc a b)), |u x| ≤ U :=
    ae_restrict_of_forall_mem measurableSet_Icc hU
  have hPhiae : ∀ᵐ x ∂(volume.restrict (Icc a b)), |phiPrime x| ≤ L :=
    ae_restrict_of_forall_mem measurableSet_Icc hPhi
  have h := motilityDrift_memLp_and_L2_bound
    (μ := volume.restrict (Icc a b))
    u phiPrime gradV hU0 hL0 hUae hPhiae hGradLp
    (by simpa [motilityCoordinateGradient] using hDriftMeas)
  simpa [motilityCoordinateGradient] using h

end AMLStabilization
