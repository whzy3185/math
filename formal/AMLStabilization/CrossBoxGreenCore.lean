import Mathlib
import AMLStabilization.BoxNeumannFluxCore

open Set Finset MeasureTheory

namespace AMLStabilization

/-- Product rule for the cross flux `w * grad h`. -/
theorem crossGradientFlux_hasFDerivAt
    {n : ℕ}
    {w : (Fin (n + 1) → ℝ) → ℝ}
    {gradH : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {dw : (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    {dgradH : Fin (n + 1) → (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    (hw : HasFDerivAt w dw x)
    (hgradH : ∀ i, HasFDerivAt (fun y => gradH y i) (dgradH i) x) :
    HasFDerivAt
      (fun y i => w y * gradH y i)
      (ContinuousLinearMap.pi fun i => w x • dgradH i + gradH x i • dw) x := by
  apply hasFDerivAt_pi.2
  intro i
  convert! hw.mul (hgradH i)

/-- Coordinate expansion of `div (w * grad h)`. -/
theorem crossGradientFlux_divergence_identity
    {n : ℕ}
    {w lapH : (Fin (n + 1) → ℝ) → ℝ}
    {gradW gradH : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {dw : (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    {dgradH : Fin (n + 1) → (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    (hgradWCoord : ∀ i, dw (Pi.single i 1) = gradW x i)
    (hlapH : lapH x = ∑ i : Fin (n + 1), dgradH i (Pi.single i 1)) :
    (∑ i : Fin (n + 1),
      (w x • dgradH i + gradH x i • dw) (Pi.single i 1)) =
      (∑ i : Fin (n + 1), gradW x i * gradH x i) + w x * lapH x := by
  calc
    (∑ i : Fin (n + 1),
      (w x • dgradH i + gradH x i • dw) (Pi.single i 1)) =
        ∑ i : Fin (n + 1),
          (w x * dgradH i (Pi.single i 1) + gradH x i * gradW x i) := by
      apply Finset.sum_congr rfl
      intro i hi
      simp [hgradWCoord i]
    _ = w x * (∑ i : Fin (n + 1), dgradH i (Pi.single i 1)) +
        ∑ i : Fin (n + 1), gradH x i * gradW x i := by
      rw [Finset.sum_add_distrib, Finset.mul_sum]
    _ = (∑ i : Fin (n + 1), gradW x i * gradH x i) + w x * lapH x := by
      rw [← hlapH]
      congr 1
      apply Finset.sum_congr rfl
      intro i hi
      ring

/--
Cross Green identity on a rectangular box from local first/second derivative
data.  The zero-normal condition is imposed on `h`, since the boundary flux is
`w * grad h`.
-/
theorem boxCrossGreenIdentity_from_local_derivatives
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (w lapH : (Fin (n + 1) → ℝ) → ℝ)
    (gradW gradH : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (dw : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgradH : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    (hbad : bad.Countable)
    (hwcont : ContinuousOn w (Icc a b))
    (hgradHcont : ∀ i, ContinuousOn (fun x => gradH x i) (Icc a b))
    (hwdiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt w (dw x) x)
    (hgradHdiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt (fun y => gradH y i) (dgradH x i) x)
    (hgradWCoord : ∀ x i, dw x (Pi.single i 1) = gradW x i)
    (hlapH : ∀ x, lapH x =
      ∑ i : Fin (n + 1), dgradH x i (Pi.single i 1))
    (hfront : ∀ i (x : Fin n → ℝ), gradH (i.insertNth (b i) x) i = 0)
    (hback : ∀ i (x : Fin n → ℝ), gradH (i.insertNth (a i) x) i = 0)
    (hCrossInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), gradW x i * gradH x i) (Icc a b))
    (hWLapInt : IntegrableOn (fun x => w x * lapH x) (Icc a b)) :
    (∫ x in Icc a b, w x * lapH x) =
      -(∫ x in Icc a b,
        ∑ i : Fin (n + 1), gradW x i * gradH x i) := by
  let flux' : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] (Fin (n + 1) → ℝ) :=
    fun x => ContinuousLinearMap.pi fun i =>
      w x • dgradH x i + gradH x i • dw x
  have hfluxcont : ContinuousOn (fun x i => w x * gradH x i) (Icc a b) := by
    rw [continuousOn_pi]
    intro i
    exact hwcont.mul (hgradHcont i)
  have hDivIdentity : ∀ x,
      (∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) =
        (∑ i : Fin (n + 1), gradW x i * gradH x i) + w x * lapH x := by
    intro x
    simpa [flux'] using
      (crossGradientFlux_divergence_identity
        (w := w) (lapH := lapH) (gradW := gradW) (gradH := gradH) (x := x)
        (dw := dw x) (dgradH := dgradH x)
        (hgradWCoord x) (hlapH x))
  have hRhsInt : IntegrableOn
      (fun x => (∑ i : Fin (n + 1), gradW x i * gradH x i) + w x * lapH x)
      (Icc a b) := hCrossInt.add hWLapInt
  have hDivInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i)
      (Icc a b) := by
    apply IntegrableOn.congr_fun hRhsInt
    · intro x hx
      exact (hDivIdentity x).symm
    · exact measurableSet_Icc
  have hDivZero :
      (∫ x in Icc a b,
        ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) = 0 := by
    apply boxIntegral_divergence_eq_zero_of_zero_face_flux
      hle (fun x i => w x * gradH x i) flux' bad hbad hfluxcont
    · intro x hx
      exact crossGradientFlux_hasFDerivAt (hwdiff x hx) (hgradHdiff x hx)
    · exact hDivInt
    · intro i x
      rw [hfront i x, mul_zero]
    · intro i x
      rw [hback i x, mul_zero]
  have hSplit :
      (∫ x in Icc a b,
        ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) =
      (∫ x in Icc a b,
        ∑ i : Fin (n + 1), gradW x i * gradH x i) +
        ∫ x in Icc a b, w x * lapH x := by
    calc
      (∫ x in Icc a b,
        ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) =
          ∫ x in Icc a b,
            ((∑ i : Fin (n + 1), gradW x i * gradH x i) + w x * lapH x) := by
        apply integral_congr_ae
        filter_upwards with x
        exact hDivIdentity x
      _ = (∫ x in Icc a b,
            ∑ i : Fin (n + 1), gradW x i * gradH x i) +
          ∫ x in Icc a b, w x * lapH x := by
        rw [integral_add hCrossInt hWLapInt]
  linarith

end AMLStabilization
