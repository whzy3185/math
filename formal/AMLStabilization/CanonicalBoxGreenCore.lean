import Mathlib
import AMLStabilization.ProductRuleGreenCore

open Set Finset MeasureTheory

namespace AMLStabilization

/-- Coordinate gradient extracted from the Fréchet derivative of a scalar field. -/
noncomputable def derivativeCoordinateGradient
    {n : ℕ}
    (dw : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (x : Fin (n + 1) → ℝ) (i : Fin (n + 1)) : ℝ :=
  dw x (Pi.single i 1)

/-- Laplacian trace extracted from derivatives of the coordinate gradient. -/
noncomputable def derivativeTraceLaplacian
    {n : ℕ}
    (dgrad : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (x : Fin (n + 1) → ℝ) : ℝ :=
  ∑ i : Fin (n + 1), dgrad x i (Pi.single i 1)

/--
Canonical Green endpoint on a rectangular box.  The gradient and Laplacian are
not supplied as independent functions: they are defined from first and second
Fréchet derivative data.  The local product rule and the integrability of the
divergence flux are both derived internally.
-/
theorem boxGreenIdentity_from_frechet_data
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (w : (Fin (n + 1) → ℝ) → ℝ)
    (dw : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgrad : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    (hbad : bad.Countable)
    (hwcont : ContinuousOn w (Icc a b))
    (hgradcont : ∀ i, ContinuousOn
      (fun x => derivativeCoordinateGradient dw x i) (Icc a b))
    (hwdiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt w (dw x) x)
    (hgradDiff : ∀ x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt
        (fun y => derivativeCoordinateGradient dw y i) (dgrad x i) x)
    (hfront : ∀ i (x : Fin n → ℝ),
      derivativeCoordinateGradient dw (i.insertNth (b i) x) i = 0)
    (hback : ∀ i (x : Fin n → ℝ),
      derivativeCoordinateGradient dw (i.insertNth (a i) x) i = 0)
    (hGradInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1),
        (derivativeCoordinateGradient dw x i) ^ 2) (Icc a b))
    (hWLapInt : IntegrableOn
      (fun x => w x * derivativeTraceLaplacian dgrad x) (Icc a b)) :
    (∫ x in Icc a b, w x * derivativeTraceLaplacian dgrad x) =
      -(∫ x in Icc a b,
        ∑ i : Fin (n + 1), (derivativeCoordinateGradient dw x i) ^ 2) := by
  let grad : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ :=
    fun x i => derivativeCoordinateGradient dw x i
  let lap : (Fin (n + 1) → ℝ) → ℝ :=
    fun x => derivativeTraceLaplacian dgrad x
  let flux' : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] (Fin (n + 1) → ℝ) :=
    fun x => ContinuousLinearMap.pi fun i => w x • dgrad x i + grad x i • dw x
  have hfluxcont : ContinuousOn (fun x i => w x * grad x i) (Icc a b) := by
    rw [continuousOn_pi]
    intro i
    exact hwcont.mul (by simpa [grad] using hgradcont i)
  have hdivIdentity : ∀ x,
      (∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) =
        (∑ i : Fin (n + 1), (grad x i) ^ 2) + w x * lap x := by
    intro x
    simpa [flux', grad, lap, derivativeCoordinateGradient,
      derivativeTraceLaplacian] using
      (productGradientFlux_divergence_identity
        (w := w) (lap := lap) (grad := grad) (x := x)
        (dw := dw x) (dgrad := dgrad x)
        (fun i => rfl) rfl)
  have hRhsInt : IntegrableOn
      (fun x => (∑ i : Fin (n + 1), (grad x i) ^ 2) + w x * lap x)
      (Icc a b) := by
    exact (by simpa [grad] using hGradInt).add (by simpa [lap] using hWLapInt)
  have hDivInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i)
      (Icc a b) := by
    apply IntegrableOn.congr_fun hRhsInt
    · intro x hx
      exact (hdivIdentity x).symm
    · exact measurableSet_Icc
  have hgreen := boxGreenIdentity_from_local_derivatives
    hle w lap grad dw dgrad bad hbad hfluxcont
    hwdiff
    (by
      intro x hx i
      simpa [grad] using hgradDiff x hx i)
    (by intro x i; rfl)
    (by intro x; rfl)
    (by simpa [flux'] using hDivInt)
    (by simpa [grad] using hfront)
    (by simpa [grad] using hback)
    (by simpa [grad] using hGradInt)
    (by simpa [lap] using hWLapInt)
  simpa [grad, lap] using hgreen

end AMLStabilization
