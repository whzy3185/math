import Mathlib
import AMLStabilization.BoxNeumannFluxCore

open Set Finset MeasureTheory

namespace AMLStabilization

/--
Fréchet product rule for the vector field `w * grad w`.  The derivative is
assembled coordinatewise from the derivative of `w` and the derivatives of the
gradient components, then bundled into a Pi-valued continuous linear map.
-/
theorem productGradientFlux_hasFDerivAt
    {n : ℕ}
    {w : (Fin (n + 1) → ℝ) → ℝ}
    {grad : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {dw : (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    {dgrad : Fin (n + 1) → (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    (hw : HasFDerivAt w dw x)
    (hgrad : ∀ i, HasFDerivAt (fun y => grad y i) (dgrad i) x) :
    HasFDerivAt
      (fun y i => w y * grad y i)
      (ContinuousLinearMap.pi fun i => w x • dgrad i + grad x i • dw) x := by
  apply hasFDerivAt_pi.2
  intro i
  simpa only [Pi.mul_apply] using hw.mul (hgrad i)

/--
Coordinate expansion of `div (w * grad w)` once `dw(e_i)=grad_i` and the
Laplacian is the trace of the gradient derivative.
-/
theorem productGradientFlux_divergence_identity
    {n : ℕ}
    {w lap : (Fin (n + 1) → ℝ) → ℝ}
    {grad : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {dw : (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    {dgrad : Fin (n + 1) → (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    (hgradCoord : ∀ i, dw (Pi.single i 1) = grad x i)
    (hlap : lap x = ∑ i : Fin (n + 1), dgrad i (Pi.single i 1)) :
    (∑ i : Fin (n + 1),
      (w x • dgrad i + grad x i • dw) (Pi.single i 1)) =
      (∑ i : Fin (n + 1), (grad x i) ^ 2) + w x * lap x := by
  calc
    (∑ i : Fin (n + 1),
      (w x • dgrad i + grad x i • dw) (Pi.single i 1)) =
        ∑ i : Fin (n + 1),
          (w x * dgrad i (Pi.single i 1) + (grad x i) ^ 2) := by
      apply Finset.sum_congr rfl
      intro i hi
      simp [hgradCoord i, pow_two]
    _ = w x * (∑ i : Fin (n + 1), dgrad i (Pi.single i 1)) +
        ∑ i : Fin (n + 1), (grad x i) ^ 2 := by
      rw [Finset.sum_add_distrib, Finset.mul_sum]
      ring
    _ = (∑ i : Fin (n + 1), (grad x i) ^ 2) + w x * lap x := by
      rw [← hlap]
      ring

/--
The local PDE identity used by Green's formula is obtained directly from
Fréchet derivatives: no product-rule/divergence identity is assumed.
-/
theorem productGradientFlux_local_package
    {n : ℕ}
    {w lap : (Fin (n + 1) → ℝ) → ℝ}
    {grad : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {dw : (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    {dgrad : Fin (n + 1) → (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    (hw : HasFDerivAt w dw x)
    (hgrad : ∀ i, HasFDerivAt (fun y => grad y i) (dgrad i) x)
    (hgradCoord : ∀ i, dw (Pi.single i 1) = grad x i)
    (hlap : lap x = ∑ i : Fin (n + 1), dgrad i (Pi.single i 1)) :
    HasFDerivAt
      (fun y i => w y * grad y i)
      (ContinuousLinearMap.pi fun i => w x • dgrad i + grad x i • dw) x ∧
    (∑ i : Fin (n + 1),
      (ContinuousLinearMap.pi fun j => w x • dgrad j + grad x j • dw)
        (Pi.single i 1) i) =
      (∑ i : Fin (n + 1), (grad x i) ^ 2) + w x * lap x := by
  constructor
  · exact productGradientFlux_hasFDerivAt hw hgrad
  · simpa using productGradientFlux_divergence_identity
      (w := w) (lap := lap) (grad := grad) (x := x)
      hgradCoord hlap

/--
Green's first identity on a rectangular box from local first/second derivative
data.  Compared with `boxGreenIdentity_of_zero_normalDerivative`, the local
product rule `div(w grad w)=|grad w|^2+w Δw` is now discharged internally.
-/
theorem boxGreenIdentity_from_local_derivatives
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (w lap : (Fin (n + 1) → ℝ) → ℝ)
    (grad : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (dw : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (dgrad : (Fin (n + 1) → ℝ) → Fin (n + 1) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ)
    (bad : Set (Fin (n + 1) → ℝ))
    (hbad : bad.Countable)
    (hcont : ContinuousOn (fun x i => w x * grad x i) (Icc a b))
    (hw : ∀ x, x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      HasFDerivAt w (dw x) x)
    (hgrad : ∀ x, x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad →
      ∀ i, HasFDerivAt (fun y => grad y i) (dgrad x i) x)
    (hgradCoord : ∀ x i, dw x (Pi.single i 1) = grad x i)
    (hlap : ∀ x, lap x = ∑ i : Fin (n + 1), dgrad x i (Pi.single i 1))
    (hDivInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1),
        (ContinuousLinearMap.pi fun j => w x • dgrad x j + grad x j • dw x)
          (Pi.single i 1) i) (Icc a b))
    (hfront : ∀ i (x : Fin n → ℝ), grad (i.insertNth (b i) x) i = 0)
    (hback : ∀ i (x : Fin n → ℝ), grad (i.insertNth (a i) x) i = 0)
    (hGradInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), (grad x i) ^ 2) (Icc a b))
    (hWLapInt : IntegrableOn (fun x => w x * lap x) (Icc a b)) :
    (∫ x in Icc a b, w x * lap x) =
      -(∫ x in Icc a b, ∑ i : Fin (n + 1), (grad x i) ^ 2) := by
  let flux' : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] (Fin (n + 1) → ℝ) :=
    fun x => ContinuousLinearMap.pi fun i => w x • dgrad x i + grad x i • dw x
  apply boxGreenIdentity_of_zero_normalDerivative
    hle w lap grad flux' bad hbad hcont
  · intro x hx
    exact productGradientFlux_hasFDerivAt (hw x hx) (hgrad x hx)
  · simpa [flux'] using hDivInt
  · exact hfront
  · exact hback
  · intro x
    simpa [flux'] using productGradientFlux_divergence_identity
      (w := w) (lap := lap) (grad := grad) (x := x)
      (hgradCoord x) (hlap x)
  · exact hGradInt
  · exact hWLapInt

end AMLStabilization
