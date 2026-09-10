import Mathlib
import AMLStabilization.SpatialExtremumSecondDerivativeCore

open Set Filter
open scoped Topology Convex

namespace AMLStabilization

/-- The backward direction belongs to the positive tangent cone of `(-∞,t₀]`
at the endpoint `t₀`. -/
theorem neg_one_mem_posTangentCone_Iic (t0 : ℝ) :
    (-1 : ℝ) ∈ posTangentConeAt (Iic t0) t0 := by
  have hseg : segment ℝ t0 (t0 - 1) ⊆ Iic t0 := by
    rw [segment_symm, segment_eq_Icc (by linarith : t0 - 1 ≤ t0)]
    intro y hy
    exact hy.2
  have h := sub_mem_posTangentConeAt_of_segment_subset hseg
  have heq : (t0 - 1) - t0 = (-1 : ℝ) := by ring
  simpa [heq] using h

/-- At a first upper contact from the past, the time derivative is nonnegative. -/
theorem derivative_nonneg_at_past_upper_contact
    {y : ℝ → ℝ} {t0 dy : ℝ}
    (hcontact : IsLocalMaxOn y (Iic t0) t0)
    (hy : HasDerivAt y dy t0) :
    0 ≤ dy := by
  have hdir := neg_one_mem_posTangentCone_Iic t0
  have h := hcontact.hasFDerivWithinAt_nonpos
    hy.hasFDerivAt.hasFDerivWithinAt hdir
  have hmul : (-1 : ℝ) * dy ≤ 0 := by
    simpa [ContinuousLinearMap.toSpanSingleton_apply] using h
  linarith

/-- At a first lower contact from the past, the time derivative is nonpositive. -/
theorem derivative_nonpos_at_past_lower_contact
    {y : ℝ → ℝ} {t0 dy : ℝ}
    (hcontact : IsLocalMinOn y (Iic t0) t0)
    (hy : HasDerivAt y dy t0) :
    dy ≤ 0 := by
  have hdir := neg_one_mem_posTangentCone_Iic t0
  have h := hcontact.hasFDerivWithinAt_nonneg
    hy.hasFDerivAt.hasFDerivWithinAt hdir
  have hmul : 0 ≤ (-1 : ℝ) * dy := by
    simpa [ContinuousLinearMap.toSpanSingleton_apply] using h
  linarith

/-- For the tilted upper barrier `y(t)-εt`, first contact forces `y'(t₀) ≥ ε`. -/
theorem derivative_ge_epsilon_at_upper_barrier_contact
    {y : ℝ → ℝ} {t0 dy eps : ℝ}
    (hcontact : IsLocalMaxOn (fun t => y t - eps * t) (Iic t0) t0)
    (hy : HasDerivAt y dy t0) :
    eps ≤ dy := by
  have hlinear : HasDerivAt (fun t : ℝ => eps * t) eps t0 :=
    hasDerivAt_const_mul eps
  have hshift : HasDerivAt (fun t => y t - eps * t) (dy - eps) t0 :=
    hy.sub hlinear
  have hnonneg := derivative_nonneg_at_past_upper_contact hcontact hshift
  linarith

/-- For the tilted lower barrier `y(t)+εt`, first contact forces `y'(t₀) ≤ -ε`. -/
theorem derivative_le_neg_epsilon_at_lower_barrier_contact
    {y : ℝ → ℝ} {t0 dy eps : ℝ}
    (hcontact : IsLocalMinOn (fun t => y t + eps * t) (Iic t0) t0)
    (hy : HasDerivAt y dy t0) :
    dy ≤ -eps := by
  have hlinear : HasDerivAt (fun t : ℝ => eps * t) eps t0 :=
    hasDerivAt_const_mul eps
  have hshift : HasDerivAt (fun t => y t + eps * t) (dy + eps) t0 :=
    hy.add hlinear
  have hnonpos := derivative_nonpos_at_past_lower_contact hcontact hshift
  linarith

/-- A positive tilted upper-barrier first contact is incompatible with a PDE
contact inequality `y'(t₀) ≤ 0`. -/
theorem upper_barrier_contact_impossible
    {y : ℝ → ℝ} {t0 dy eps : ℝ}
    (heps : 0 < eps)
    (hcontact : IsLocalMaxOn (fun t => y t - eps * t) (Iic t0) t0)
    (hy : HasDerivAt y dy t0)
    (hPDEcontact : dy ≤ 0) : False := by
  have hge := derivative_ge_epsilon_at_upper_barrier_contact hcontact hy
  linarith

/-- A positive tilted lower-barrier first contact is incompatible with a PDE
contact inequality `0 ≤ y'(t₀)`. -/
theorem lower_barrier_contact_impossible
    {y : ℝ → ℝ} {t0 dy eps : ℝ}
    (heps : 0 < eps)
    (hcontact : IsLocalMinOn (fun t => y t + eps * t) (Iic t0) t0)
    (hy : HasDerivAt y dy t0)
    (hPDEcontact : 0 ≤ dy) : False := by
  have hle := derivative_le_neg_epsilon_at_lower_barrier_contact hcontact hy
  linarith

/--
First-contact maximum-principle closure at an upper spatial local maximum for
`z_t = Δz + rho F(z)`.  The spatial Laplacian sign is derived from the local
maximum, the reaction sign from dissipativity, and the temporal contradiction
from an `ε`-tilted past contact.
-/
theorem upper_signal_barrier_contact_impossible
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {timeTrace : ℝ → ℝ} {t0 zt eps : ℝ}
    {F : ℝ → ℝ} {zstar beta q rho : ℝ}
    (heps : 0 < eps)
    (hTimeContact : IsLocalMaxOn
      (fun t => timeTrace t - eps * t) (Iic t0) t0)
    (hTimeDeriv : HasDerivAt timeTrace zt t0)
    (hSpatialMax : IsLocalMax z x) (hSpatialCont : ContinuousAt z x)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : zstar ≤ z x)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) : False := by
  have hpdeSign := upperContact_from_spatialLocalMax hSpatialMax hSpatialCont
    hbeta hrho hFstar hs hdiss hPDE
  exact upper_barrier_contact_impossible heps hTimeContact hTimeDeriv hpdeSign

/-- Lower-barrier analogue of `upper_signal_barrier_contact_impossible`. -/
theorem lower_signal_barrier_contact_impossible
    {n : ℕ} {z : (Fin (n + 1) → ℝ) → ℝ}
    {x : Fin (n + 1) → ℝ}
    {timeTrace : ℝ → ℝ} {t0 zt eps : ℝ}
    {F : ℝ → ℝ} {zstar beta q rho : ℝ}
    (heps : 0 < eps)
    (hTimeContact : IsLocalMinOn
      (fun t => timeTrace t + eps * t) (Iic t0) t0)
    (hTimeDeriv : HasDerivAt timeTrace zt t0)
    (hSpatialMin : IsLocalMin z x) (hSpatialCont : ContinuousAt z x)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : z x ≤ zstar)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) : False := by
  have hpdeSign := lowerContact_from_spatialLocalMin hSpatialMin hSpatialCont
    hbeta hrho hFstar hs hdiss hPDE
  exact lower_barrier_contact_impossible heps hTimeContact hTimeDeriv hpdeSign

end AMLStabilization
