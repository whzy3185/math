import Mathlib
import AMLStabilization.MaximumPrincipleContactCore

open Filter
open scoped Topology

namespace AMLStabilization

/-- A twice-differentiable real function has nonpositive second derivative at
a local maximum.  This is proved from mathlib's second-derivative test: a
strictly positive second derivative would also make the point a local minimum,
forcing the function to be locally constant and hence the second derivative to
vanish. -/
theorem secondDeriv_nonpos_of_isLocalMax
    {f : ℝ → ℝ} {x : ℝ}
    (hmax : IsLocalMax f x) (hcont : ContinuousAt f x) :
    deriv (deriv f) x ≤ 0 := by
  by_contra hnot
  have hpos : 0 < deriv (deriv f) x := lt_of_not_ge hnot
  have hd0 : deriv f x = 0 := hmax.deriv_eq_zero
  have hmin : IsLocalMin f x := isLocalMin_of_deriv_deriv_pos hpos hd0 hcont
  have heq : f =ᶠ[𝓝 x] (fun _ : ℝ => f x) := by
    filter_upwards [hmax, hmin] with y hymax hymin
    exact le_antisymm hymax hymin
  have hderivEq : deriv f =ᶠ[𝓝 x] deriv (fun _ : ℝ => f x) := heq.deriv
  have hsec : deriv (deriv f) x = deriv (deriv (fun _ : ℝ => f x)) x :=
    hderivEq.deriv_eq
  have hzero : deriv (fun _ : ℝ => f x) = (fun _ : ℝ => 0) := by
    funext y
    simp
  rw [hzero] at hsec
  simp at hsec
  linarith

/-- A twice-differentiable real function has nonnegative second derivative at
a local minimum. -/
theorem secondDeriv_nonneg_of_isLocalMin
    {f : ℝ → ℝ} {x : ℝ}
    (hmin : IsLocalMin f x) (hcont : ContinuousAt f x) :
    0 ≤ deriv (deriv f) x := by
  by_contra hnot
  have hneg : deriv (deriv f) x < 0 := lt_of_not_ge hnot
  have hd0 : deriv f x = 0 := hmin.deriv_eq_zero
  have hmax : IsLocalMax f x := isLocalMax_of_deriv_deriv_neg hneg hd0 hcont
  have heq : f =ᶠ[𝓝 x] (fun _ : ℝ => f x) := by
    filter_upwards [hmax, hmin] with y hymax hymin
    exact le_antisymm hymax hymin
  have hderivEq : deriv f =ᶠ[𝓝 x] deriv (fun _ : ℝ => f x) := heq.deriv
  have hsec : deriv (deriv f) x = deriv (deriv (fun _ : ℝ => f x)) x :=
    hderivEq.deriv_eq
  have hzero : deriv (fun _ : ℝ => f x) = (fun _ : ℝ => 0) := by
    funext y
    simp
  rw [hzero] at hsec
  simp at hsec
  linarith

/-- Coordinate line through `x` in direction `i`. -/
noncomputable def coordinateSlice
    {n : ℕ} (z : (Fin (n + 1) → ℝ) → ℝ)
    (x : Fin (n + 1) → ℝ) (i : Fin (n + 1)) (t : ℝ) : ℝ :=
  z (x + t • Pi.single i 1)

/-- A spatial local maximum restricts to a local maximum on every coordinate
line through the point. -/
theorem coordinateSlice_isLocalMax
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    (hmax : IsLocalMax z x) (i : Fin (n + 1)) :
    IsLocalMax (coordinateSlice z x i) 0 := by
  let g : ℝ → (Fin (n + 1) → ℝ) := fun t => x + t • Pi.single i 1
  have hg : ContinuousAt g 0 := by fun_prop
  have hg0 : g 0 = x := by simp [g]
  have hmax' : IsLocalMax z (g 0) := by simpa [hg0] using hmax
  have hcomp : IsLocalMax (z ∘ g) 0 := hmax'.comp_continuous hg
  change IsLocalMax (fun t => z (x + t • Pi.single i 1)) 0
  simpa [g, Function.comp_def] using hcomp

/-- A spatial local minimum restricts to a local minimum on every coordinate
line through the point. -/
theorem coordinateSlice_isLocalMin
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    (hmin : IsLocalMin z x) (i : Fin (n + 1)) :
    IsLocalMin (coordinateSlice z x i) 0 := by
  let g : ℝ → (Fin (n + 1) → ℝ) := fun t => x + t • Pi.single i 1
  have hg : ContinuousAt g 0 := by fun_prop
  have hg0 : g 0 = x := by simp [g]
  have hmin' : IsLocalMin z (g 0) := by simpa [hg0] using hmin
  have hcomp : IsLocalMin (z ∘ g) 0 := hmin'.comp_continuous hg
  change IsLocalMin (fun t => z (x + t • Pi.single i 1)) 0
  simpa [g, Function.comp_def] using hcomp

/-- Continuity of the spatial field at `x` gives continuity of every coordinate
slice at the origin. -/
theorem coordinateSlice_continuousAt
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    (hz : ContinuousAt z x) (i : Fin (n + 1)) :
    ContinuousAt (coordinateSlice z x i) 0 := by
  let g : ℝ → (Fin (n + 1) → ℝ) := fun t => x + t • Pi.single i 1
  have hg : ContinuousAt g 0 := by fun_prop
  have hg0 : g 0 = x := by simp [g]
  have hcomp : ContinuousAt (z ∘ g) 0 := hz.comp_of_eq hg hg0
  change ContinuousAt (fun t => z (x + t • Pi.single i 1)) 0
  simpa [g, Function.comp_def] using hcomp

/-- The coordinate-trace Laplacian is nonpositive at a spatial local maximum. -/
theorem laplacianTrace_nonpos_of_isLocalMax
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    (hmax : IsLocalMax z x) (hcont : ContinuousAt z x) :
    (∑ i : Fin (n + 1),
      deriv (deriv (coordinateSlice z x i)) 0) ≤ 0 := by
  apply Finset.sum_nonpos
  intro i hi
  exact secondDeriv_nonpos_of_isLocalMax
    (coordinateSlice_isLocalMax hmax i)
    (coordinateSlice_continuousAt hcont i)

/-- The coordinate-trace Laplacian is nonnegative at a spatial local minimum. -/
theorem laplacianTrace_nonneg_of_isLocalMin
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    (hmin : IsLocalMin z x) (hcont : ContinuousAt z x) :
    0 ≤ ∑ i : Fin (n + 1),
      deriv (deriv (coordinateSlice z x i)) 0 := by
  apply Finset.sum_nonneg
  intro i hi
  exact secondDeriv_nonneg_of_isLocalMin
    (coordinateSlice_isLocalMin hmin i)
    (coordinateSlice_continuousAt hcont i)

/-- Full upper-contact PDE sign derived from an actual spatial local maximum,
with the Laplacian represented by coordinate second derivatives. -/
theorem upperContact_from_spatialLocalMax
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {F : ℝ → ℝ} {zstar beta q rho zt : ℝ}
    (hmax : IsLocalMax z x) (hcont : ContinuousAt z x)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : zstar ≤ z x)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) :
    zt ≤ 0 := by
  exact upperContact_timeDerivative_nonpos hbeta hrho
    (laplacianTrace_nonpos_of_isLocalMax hmax hcont)
    hFstar hs hdiss hPDE

/-- Full lower-contact PDE sign derived from an actual spatial local minimum. -/
theorem lowerContact_from_spatialLocalMin
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {F : ℝ → ℝ} {zstar beta q rho zt : ℝ}
    (hmin : IsLocalMin z x) (hcont : ContinuousAt z x)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : z x ≤ zstar)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) :
    0 ≤ zt := by
  exact lowerContact_timeDerivative_nonneg hbeta hrho
    (laplacianTrace_nonneg_of_isLocalMin hmin hcont)
    hFstar hs hdiss hPDE

end AMLStabilization
