import Mathlib

open Set

namespace AMLStabilization

/-- Coordinate gradient attached to a scalar coefficient `c = phi(v)`. -/
def motilityCoordinateGradient
    {n : ℕ}
    (phiPrime : (Fin (n + 1) → ℝ) → ℝ)
    (gradV : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ)
    (x : Fin (n + 1) → ℝ) (i : Fin (n + 1)) : ℝ :=
  phiPrime x * gradV x i

/--
Frechet chain rule for a signal-dependent motility coefficient `phi ∘ v`.
The scalar derivative of `phi` is composed with the spatial Frechet derivative
of `v`, so no coefficient-gradient identity is assumed.
-/
theorem motilityComposition_hasFDerivAt
    {n : ℕ}
    {phi : ℝ → ℝ}
    {v : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {phiPrime : ℝ}
    {dv : (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    (hphi : HasDerivAt phi phiPrime (v x))
    (hv : HasFDerivAt v dv x) :
    HasFDerivAt (fun y => phi (v y)) (phiPrime • dv) x := by
  simpa [Function.comp_def] using hphi.comp_hasFDerivAt x hv

/-- Coordinate evaluation of the chain-rule Frechet derivative. -/
theorem motilityComposition_coordinateGradient
    {n : ℕ}
    {phiPrime : ℝ}
    {dv : (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    {gradV : Fin (n + 1) → ℝ}
    (hcoord : ∀ i, dv (Pi.single i 1) = gradV i)
    (i : Fin (n + 1)) :
    (phiPrime • dv) (Pi.single i 1) = phiPrime * gradV i := by
  simp [hcoord i]

/--
Pointwise package: the coefficient derivative and all coordinate-gradient
identities for `c(x)=phi(v(x))` are generated from the scalar/spatial chain rule.
-/
theorem motilityComposition_local_package
    {n : ℕ}
    {phi : ℝ → ℝ}
    {phiPrime : (Fin (n + 1) → ℝ) → ℝ}
    {v : (Fin (n + 1) → ℝ) → ℝ}
    {dv : (Fin (n + 1) → ℝ) →
      (Fin (n + 1) → ℝ) →L[ℝ] ℝ}
    {gradV : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    {x : Fin (n + 1) → ℝ}
    (hphi : HasDerivAt phi (phiPrime x) (v x))
    (hv : HasFDerivAt v (dv x) x)
    (hcoord : ∀ i, dv x (Pi.single i 1) = gradV x i) :
    HasFDerivAt (fun y => phi (v y)) (phiPrime x • dv x) x ∧
      ∀ i, (phiPrime x • dv x) (Pi.single i 1) =
        motilityCoordinateGradient phiPrime gradV x i := by
  constructor
  · exact motilityComposition_hasFDerivAt hphi hv
  · intro i
    simpa [motilityCoordinateGradient] using
      motilityComposition_coordinateGradient hcoord i

/-- Continuity of the coordinate motility gradient follows from its two factors. -/
theorem motilityCoordinateGradient_continuousOn
    {n : ℕ}
    {s : Set (Fin (n + 1) → ℝ)}
    {phiPrime : (Fin (n + 1) → ℝ) → ℝ}
    {gradV : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    (hphiPrime : ContinuousOn phiPrime s)
    (hgradV : ∀ i, ContinuousOn (fun x => gradV x i) s) :
    ∀ i, ContinuousOn (fun x => motilityCoordinateGradient phiPrime gradV x i) s := by
  intro i
  change ContinuousOn (fun x => phiPrime x * gradV x i) s
  exact hphiPrime.mul (hgradV i)

/-- Zero normal signal derivative on a front face is inherited by `phi(v)`. -/
theorem motilityCoordinateGradient_front_zero
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    {phiPrime : (Fin (n + 1) → ℝ) → ℝ}
    {gradV : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    (hfront : ∀ i (x : Fin n → ℝ), gradV (i.insertNth (b i) x) i = 0) :
    ∀ i (x : Fin n → ℝ),
      motilityCoordinateGradient phiPrime gradV (i.insertNth (b i) x) i = 0 := by
  intro i x
  simp [motilityCoordinateGradient, hfront i x]

/-- Zero normal signal derivative on a back face is inherited by `phi(v)`. -/
theorem motilityCoordinateGradient_back_zero
    {n : ℕ}
    {a b : Fin (n + 1) → ℝ}
    {phiPrime : (Fin (n + 1) → ℝ) → ℝ}
    {gradV : (Fin (n + 1) → ℝ) → Fin (n + 1) → ℝ}
    (hback : ∀ i (x : Fin n → ℝ), gradV (i.insertNth (a i) x) i = 0) :
    ∀ i (x : Fin n → ℝ),
      motilityCoordinateGradient phiPrime gradV (i.insertNth (a i) x) i = 0 := by
  intro i x
  simp [motilityCoordinateGradient, hback i x]

end AMLStabilization
