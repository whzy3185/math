import Mathlib
import AMLStabilization.MassConservationCore

open MeasureTheory Set Finset Filter
open scoped Topology

namespace AMLStabilization

/--
On a rectangular box, vanishing normal components on every pair of faces force
the integral of the divergence to vanish.  Unlike the abstract PDE interfaces
used elsewhere in the library, this theorem invokes mathlib's Bochner
divergence theorem directly.
-/
theorem boxIntegral_divergence_eq_zero_of_zero_face_flux
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (flux : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (flux' : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] (Fin (n + 1) → ℝ))
    (bad : Set (Fin (n + 1) → ℝ))
    (hbad : bad.Countable)
    (hcont : ContinuousOn flux (Icc a b))
    (hdiff : ∀ x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad,
      HasFDerivAt flux (flux' x) x)
    (hint : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) (Icc a b))
    (hfront : ∀ i (x : Fin n → ℝ),
      flux (i.insertNth (b i) x) i = 0)
    (hback : ∀ i (x : Fin n → ℝ),
      flux (i.insertNth (a i) x) i = 0) :
    (∫ x in Icc a b,
      ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) = 0 := by
  rw [MeasureTheory.integral_divergence_of_hasFDerivAt_off_countable
    (a := a) (b := b) hle flux flux' bad hbad hcont hdiff hint]
  apply Finset.sum_eq_zero
  intro i hi
  simp [hfront i, hback i]

/--
Differentiation of a box integral with respect to time under the standard local
dominated hypotheses.  This is the linear-mass analogue of
`hasDerivAt_integral_square_of_dominated`.
-/
theorem hasDerivAt_boxIntegral_of_dominated
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    {u ut : ℝ → (Fin (n + 1) → ℝ) → ℝ}
    {t0 : ℝ} {timeSet : Set ℝ}
    {bound : (Fin (n + 1) → ℝ) → ℝ}
    (hs : timeSet ∈ 𝓝 t0)
    (hUMeas : ∀ᶠ t in 𝓝 t0,
      AEStronglyMeasurable (u t) (volume.restrict (Icc a b)))
    (hUInt : Integrable (u t0) (volume.restrict (Icc a b)))
    (hUtMeas : AEStronglyMeasurable (ut t0) (volume.restrict (Icc a b)))
    (hDerivBound : ∀ᵐ x ∂volume.restrict (Icc a b), ∀ t ∈ timeSet,
      ‖ut t x‖ ≤ bound x)
    (hBoundInt : Integrable bound (volume.restrict (Icc a b)))
    (hTimeDeriv : ∀ᵐ x ∂volume.restrict (Icc a b), ∀ t ∈ timeSet,
      HasDerivAt (fun tau => u tau x) (ut t x) t) :
    HasDerivAt
      (fun t => ∫ x in Icc a b, u t x)
      (∫ x in Icc a b, ut t0 x) t0 := by
  exact (hasDerivAt_integral_of_dominated_loc_of_deriv_le
    (μ := volume.restrict (Icc a b))
    (F := u) (F' := ut) (bound := bound)
    hs hUMeas hUInt hUtMeas hDerivBound hBoundInt hTimeDeriv).2

/--
For a conservation law `u_t = div J` on a rectangular box, the divergence
theorem plus zero face flux imply exact conservation of the spatial mass.
The only time-calculus input is the already formalized derivative of the box
integral.
-/
theorem boxMass_conserved_from_fluxPDE
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    {u ut : ℝ → (Fin (n + 1) → ℝ) → ℝ}
    (flux : ℝ → (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (flux' : ℝ → (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] (Fin (n + 1) → ℝ))
    (bad : ℝ → Set (Fin (n + 1) → ℝ))
    (hMassDeriv : ∀ t,
      HasDerivAt (fun tau => ∫ x in Icc a b, u tau x)
        (∫ x in Icc a b, ut t x) t)
    (hPDE : ∀ t x,
      ut t x = ∑ i : Fin (n + 1), flux' t x (Pi.single i 1) i)
    (hbad : ∀ t, (bad t).Countable)
    (hcont : ∀ t, ContinuousOn (flux t) (Icc a b))
    (hdiff : ∀ t x,
      x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad t →
      HasFDerivAt (flux t) (flux' t x) x)
    (hint : ∀ t, IntegrableOn
      (fun x => ∑ i : Fin (n + 1), flux' t x (Pi.single i 1) i) (Icc a b))
    (hfront : ∀ t i (x : Fin n → ℝ),
      flux t (i.insertNth (b i) x) i = 0)
    (hback : ∀ t i (x : Fin n → ℝ),
      flux t (i.insertNth (a i) x) i = 0) :
    ∀ s t,
      (∫ x in Icc a b, u t x) = ∫ x in Icc a b, u s x := by
  have hUtIntegralZero : ∀ t, (∫ x in Icc a b, ut t x) = 0 := by
    intro t
    calc
      (∫ x in Icc a b, ut t x) =
          ∫ x in Icc a b,
            ∑ i : Fin (n + 1), flux' t x (Pi.single i 1) i := by
        apply integral_congr_ae
        filter_upwards with x
        exact hPDE t x
      _ = 0 := boxIntegral_divergence_eq_zero_of_zero_face_flux
        hle (flux t) (flux' t) (bad t) (hbad t) (hcont t) (hdiff t)
        (hint t) (hfront t) (hback t)
  have hZeroDeriv : ∀ t,
      HasDerivAt (fun tau => ∫ x in Icc a b, u tau x) 0 t := by
    intro t
    simpa [hUtIntegralZero t] using hMassDeriv t
  exact scalarConservation_of_zeroDerivative hZeroDeriv

/--
Green's first identity on a rectangular box for a scalar field with zero normal
derivative on every face.  The global integration-by-parts step is discharged
by the box divergence theorem; the remaining local input is the pointwise
product-rule identity for `div (w ∇w)`.
-/
theorem boxGreenIdentity_of_zero_normalDerivative
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    (hle : a ≤ b)
    (w lap : (Fin (n + 1) → ℝ) → ℝ)
    (grad : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (flux' : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] (Fin (n + 1) → ℝ))
    (bad : Set (Fin (n + 1) → ℝ))
    (hbad : bad.Countable)
    (hcont : ContinuousOn (fun x i => w x * grad x i) (Icc a b))
    (hdiff : ∀ x ∈ (Set.pi Set.univ fun i => Ioo (a i) (b i)) \ bad,
      HasFDerivAt (fun y i => w y * grad y i) (flux' x) x)
    (hint : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) (Icc a b))
    (hfront : ∀ i (x : Fin n → ℝ), grad (i.insertNth (b i) x) i = 0)
    (hback : ∀ i (x : Fin n → ℝ), grad (i.insertNth (a i) x) i = 0)
    (hDivIdentity : ∀ x,
      (∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) =
        (∑ i : Fin (n + 1), (grad x i) ^ 2) + w x * lap x)
    (hGradInt : IntegrableOn
      (fun x => ∑ i : Fin (n + 1), (grad x i) ^ 2) (Icc a b))
    (hWLapInt : IntegrableOn (fun x => w x * lap x) (Icc a b)) :
    (∫ x in Icc a b, w x * lap x) =
      -(∫ x in Icc a b, ∑ i : Fin (n + 1), (grad x i) ^ 2) := by
  have hDivZero :
      (∫ x in Icc a b,
        ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) = 0 := by
    apply boxIntegral_divergence_eq_zero_of_zero_face_flux
      hle (fun x i => w x * grad x i) flux' bad hbad hcont hdiff hint
    · intro i x
      rw [hfront i x, mul_zero]
    · intro i x
      rw [hback i x, mul_zero]
  have hSplit :
      (∫ x in Icc a b,
        ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) =
      (∫ x in Icc a b, ∑ i : Fin (n + 1), (grad x i) ^ 2) +
        ∫ x in Icc a b, w x * lap x := by
    calc
      (∫ x in Icc a b,
        ∑ i : Fin (n + 1), flux' x (Pi.single i 1) i) =
          ∫ x in Icc a b,
            ((∑ i : Fin (n + 1), (grad x i) ^ 2) + w x * lap x) := by
        apply integral_congr_ae
        filter_upwards with x
        exact hDivIdentity x
      _ = (∫ x in Icc a b, ∑ i : Fin (n + 1), (grad x i) ^ 2) +
          ∫ x in Icc a b, w x * lap x := by
        rw [integral_add hGradInt hWLapInt]
  linarith

end AMLStabilization
