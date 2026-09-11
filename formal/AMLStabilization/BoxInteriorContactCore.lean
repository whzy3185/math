import Mathlib
import AMLStabilization.SpatialExtremumSecondDerivativeCore

open Set

namespace AMLStabilization

/-- A global maximum on a box is an ambient local maximum whenever the
maximizer lies in the interior of the box. -/
theorem isLocalMax_of_isMaxOn_box_of_mem_interior
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {f : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hmax : IsMaxOn f (Icc a b) x)
    (hx : x ∈ interior (Icc a b)) :
    IsLocalMax f x := by
  exact hmax.isLocalMax (mem_interior_iff_mem_nhds.mp hx)

/-- A global minimum on a box is an ambient local minimum whenever the
minimizer lies in the interior of the box. -/
theorem isLocalMin_of_isMinOn_box_of_mem_interior
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {f : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hmin : IsMinOn f (Icc a b) x)
    (hx : x ∈ interior (Icc a b)) :
    IsLocalMin f x := by
  exact hmin.isLocalMin (mem_interior_iff_mem_nhds.mp hx)

/-- Upper PDE contact sign at an interior maximizer selected globally on a box. -/
theorem upperContact_from_boxInteriorMax
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {F : ℝ → ℝ} {zstar beta q rho zt : ℝ}
    (hmax : IsMaxOn z (Icc a b) x)
    (hx : x ∈ interior (Icc a b))
    (hcont : ContinuousAt z x)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : zstar ≤ z x)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) :
    zt ≤ 0 := by
  exact upperContact_from_spatialLocalMax
    (isLocalMax_of_isMaxOn_box_of_mem_interior hmax hx) hcont
    hbeta hrho hFstar hs hdiss hPDE

/-- Lower PDE contact sign at an interior minimizer selected globally on a box. -/
theorem lowerContact_from_boxInteriorMin
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {F : ℝ → ℝ} {zstar beta q rho zt : ℝ}
    (hmin : IsMinOn z (Icc a b) x)
    (hx : x ∈ interior (Icc a b))
    (hcont : ContinuousAt z x)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : z x ≤ zstar)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) :
    0 ≤ zt := by
  exact lowerContact_from_spatialLocalMin
    (isLocalMin_of_isMinOn_box_of_mem_interior hmin hx) hcont
    hbeta hrho hFstar hs hdiss hPDE

end AMLStabilization
