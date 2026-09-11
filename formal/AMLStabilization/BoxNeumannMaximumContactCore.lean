import Mathlib
import AMLStabilization.SpatialExtremumSecondDerivativeCore
import AMLStabilization.NeumannEndpointSecondDerivativeCore

open Set

namespace AMLStabilization

/-- Offsetting a point of a rectangular box along one coordinate by an amount
that stays between the two coordinate faces keeps the point inside the box. -/
theorem coordinateOffset_mem_box
    {n : ℕ} {a b x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b) (i : Fin (n + 1))
    {t : ℝ} (ht : t ∈ Icc (a i - x i) (b i - x i)) :
    x + t • Pi.single i 1 ∈ Icc a b := by
  constructor
  · intro j
    by_cases hji : j = i
    · subst j
      simp only [Pi.add_apply, Pi.smul_apply, Pi.single_eq_same, smul_eq_mul, mul_one]
      linarith [ht.1]
    · simp only [Pi.add_apply, Pi.smul_apply, Pi.single_eq_of_ne hji, smul_eq_mul, mul_zero,
        add_zero]
      exact hx.1 j
  · intro j
    by_cases hji : j = i
    · subst j
      simp only [Pi.add_apply, Pi.smul_apply, Pi.single_eq_same, smul_eq_mul, mul_one]
      linarith [ht.2]
    · simp only [Pi.add_apply, Pi.smul_apply, Pi.single_eq_of_ne hji, smul_eq_mul, mul_zero,
        add_zero]
      exact hx.2 j

/-- A global box maximum restricts to a global maximum of each coordinate
slice on the exact offset interval allowed by the box. -/
theorem coordinateSlice_isMaxOn_boxInterval
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b) (hmax : IsMaxOn z (Icc a b) x)
    (i : Fin (n + 1)) :
    IsMaxOn (coordinateSlice z x i)
      (Icc (a i - x i) (b i - x i)) 0 := by
  intro t ht
  have hmem := coordinateOffset_mem_box hx i ht
  have hle := hmax hmem
  simpa [coordinateSlice] using hle

/-- A global box minimum restricts to a global minimum of each coordinate
slice on the exact offset interval allowed by the box. -/
theorem coordinateSlice_isMinOn_boxInterval
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b) (hmin : IsMinOn z (Icc a b) x)
    (i : Fin (n + 1)) :
    IsMinOn (coordinateSlice z x i)
      (Icc (a i - x i) (b i - x i)) 0 := by
  intro t ht
  have hmem := coordinateOffset_mem_box hx i ht
  have hle := hmin hmem
  simpa [coordinateSlice] using hle

/-- Spatial continuity on the box gives continuity of every coordinate slice
on its full admissible offset interval. -/
theorem coordinateSlice_continuousOn_boxInterval
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b) (hcont : ContinuousOn z (Icc a b))
    (i : Fin (n + 1)) :
    ContinuousOn (coordinateSlice z x i)
      (Icc (a i - x i) (b i - x i)) := by
  apply hcont.comp (by fun_prop)
  intro t ht
  exact coordinateOffset_mem_box hx i ht

/-- At a global maximum of a nondegenerate rectangular box, each coordinate
second derivative is nonpositive provided the Neumann derivative vanishes on
coordinate faces.  Interior coordinates use the ordinary second derivative
maximum test; face coordinates use the endpoint Neumann lemmas. -/
theorem coordinateSecond_nonpos_of_boxMax_of_neumann
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ i, a i < b i)
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b)
    (hmax : IsMaxOn z (Icc a b) x)
    (hcont : ContinuousOn z (Icc a b))
    (hNeumann : ∀ i : Fin (n + 1),
      x i = a i ∨ x i = b i → deriv (coordinateSlice z x i) 0 = 0)
    (i : Fin (n + 1)) :
    deriv (deriv (coordinateSlice z x i)) 0 ≤ 0 := by
  have hsmax := coordinateSlice_isMaxOn_boxInterval hx hmax i
  have hscont := coordinateSlice_continuousOn_boxInterval hx hcont i
  have hoff : a i - x i < b i - x i := by linarith [hside i]
  by_cases hleft : x i = a i
  · have hmaxLeft : IsMaxOn (coordinateSlice z x i)
        (Icc (a i - x i) (b i - x i)) (a i - x i) := by
      simpa [hleft] using hsmax
    have hzero : deriv (coordinateSlice z x i) (a i - x i) = 0 := by
      simpa [hleft] using hNeumann i (Or.inl hleft)
    have h := secondDeriv_nonpos_at_left_endpoint_of_isMaxOn_of_deriv_zero
      hoff hmaxLeft hscont hzero
    simpa [hleft] using h
  · by_cases hright : x i = b i
    · have hmaxRight : IsMaxOn (coordinateSlice z x i)
          (Icc (a i - x i) (b i - x i)) (b i - x i) := by
        simpa [hright] using hsmax
      have hzero : deriv (coordinateSlice z x i) (b i - x i) = 0 := by
        simpa [hright] using hNeumann i (Or.inr hright)
      have h := secondDeriv_nonpos_at_right_endpoint_of_isMaxOn_of_deriv_zero
        hoff hmaxRight hscont hzero
      simpa [hright] using h
    · have hal : a i < x i := lt_of_le_of_ne (hx.1 i) (Ne.symm hleft)
      have hxb : x i < b i := lt_of_le_of_ne (hx.2 i) hright
      have h0int : (0 : ℝ) ∈ interior (Icc (a i - x i) (b i - x i)) := by
        rw [interior_Icc]
        exact ⟨sub_neg.mpr hal, sub_pos.mpr hxb⟩
      have hlocal : IsLocalMax (coordinateSlice z x i) 0 :=
        hsmax.isLocalMax (mem_interior_iff_mem_nhds.mp h0int)
      have hc0 : ContinuousAt (coordinateSlice z x i) 0 :=
        hscont.continuousAt (mem_interior_iff_mem_nhds.mp h0int)
      exact secondDeriv_nonpos_of_isLocalMax hlocal hc0

/-- Minimum analogue of `coordinateSecond_nonpos_of_boxMax_of_neumann`. -/
theorem coordinateSecond_nonneg_of_boxMin_of_neumann
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ i, a i < b i)
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b)
    (hmin : IsMinOn z (Icc a b) x)
    (hcont : ContinuousOn z (Icc a b))
    (hNeumann : ∀ i : Fin (n + 1),
      x i = a i ∨ x i = b i → deriv (coordinateSlice z x i) 0 = 0)
    (i : Fin (n + 1)) :
    0 ≤ deriv (deriv (coordinateSlice z x i)) 0 := by
  have hsmin := coordinateSlice_isMinOn_boxInterval hx hmin i
  have hscont := coordinateSlice_continuousOn_boxInterval hx hcont i
  have hoff : a i - x i < b i - x i := by linarith [hside i]
  by_cases hleft : x i = a i
  · have hminLeft : IsMinOn (coordinateSlice z x i)
        (Icc (a i - x i) (b i - x i)) (a i - x i) := by
      simpa [hleft] using hsmin
    have hzero : deriv (coordinateSlice z x i) (a i - x i) = 0 := by
      simpa [hleft] using hNeumann i (Or.inl hleft)
    have h := secondDeriv_nonneg_at_left_endpoint_of_isMinOn_of_deriv_zero
      hoff hminLeft hscont hzero
    simpa [hleft] using h
  · by_cases hright : x i = b i
    · have hminRight : IsMinOn (coordinateSlice z x i)
          (Icc (a i - x i) (b i - x i)) (b i - x i) := by
        simpa [hright] using hsmin
      have hzero : deriv (coordinateSlice z x i) (b i - x i) = 0 := by
        simpa [hright] using hNeumann i (Or.inr hright)
      have h := secondDeriv_nonneg_at_right_endpoint_of_isMinOn_of_deriv_zero
        hoff hminRight hscont hzero
      simpa [hright] using h
    · have hal : a i < x i := lt_of_le_of_ne (hx.1 i) (Ne.symm hleft)
      have hxb : x i < b i := lt_of_le_of_ne (hx.2 i) hright
      have h0int : (0 : ℝ) ∈ interior (Icc (a i - x i) (b i - x i)) := by
        rw [interior_Icc]
        exact ⟨sub_neg.mpr hal, sub_pos.mpr hxb⟩
      have hlocal : IsLocalMin (coordinateSlice z x i) 0 :=
        hsmin.isLocalMin (mem_interior_iff_mem_nhds.mp h0int)
      have hc0 : ContinuousAt (coordinateSlice z x i) 0 :=
        hscont.continuousAt (mem_interior_iff_mem_nhds.mp h0int)
      exact secondDeriv_nonneg_of_isLocalMin hlocal hc0

/-- The coordinate-trace Laplacian is nonpositive at every global maximum on a
rectangular box under the coordinate-face Neumann condition, including corner
and edge maxima. -/
theorem laplacianTrace_nonpos_of_boxMax_of_neumann
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ i, a i < b i)
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b)
    (hmax : IsMaxOn z (Icc a b) x)
    (hcont : ContinuousOn z (Icc a b))
    (hNeumann : ∀ i : Fin (n + 1),
      x i = a i ∨ x i = b i → deriv (coordinateSlice z x i) 0 = 0) :
    (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) ≤ 0 := by
  exact Finset.sum_nonpos fun i _ =>
    coordinateSecond_nonpos_of_boxMax_of_neumann hside hx hmax hcont hNeumann i

/-- The coordinate-trace Laplacian is nonnegative at every global minimum on a
rectangular box under the coordinate-face Neumann condition. -/
theorem laplacianTrace_nonneg_of_boxMin_of_neumann
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ i, a i < b i)
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    (hx : x ∈ Icc a b)
    (hmin : IsMinOn z (Icc a b) x)
    (hcont : ContinuousOn z (Icc a b))
    (hNeumann : ∀ i : Fin (n + 1),
      x i = a i ∨ x i = b i → deriv (coordinateSlice z x i) 0 = 0) :
    0 ≤ ∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0 := by
  exact Finset.sum_nonneg fun i _ =>
    coordinateSecond_nonneg_of_boxMin_of_neumann hside hx hmin hcont hNeumann i

/-- Upper PDE contact sign at an arbitrary global box maximum, including
Neumann boundary contacts. -/
theorem upperContact_from_boxMax_of_neumann
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ i, a i < b i)
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    {F : ℝ → ℝ} {zstar beta q rho zt : ℝ}
    (hx : x ∈ Icc a b)
    (hmax : IsMaxOn z (Icc a b) x)
    (hcont : ContinuousOn z (Icc a b))
    (hNeumann : ∀ i : Fin (n + 1),
      x i = a i ∨ x i = b i → deriv (coordinateSlice z x i) 0 = 0)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : zstar ≤ z x)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) :
    zt ≤ 0 := by
  exact upperContact_timeDerivative_nonpos hbeta hrho
    (laplacianTrace_nonpos_of_boxMax_of_neumann hside hx hmax hcont hNeumann)
    hFstar hs hdiss hPDE

/-- Lower PDE contact sign at an arbitrary global box minimum, including
Neumann boundary contacts. -/
theorem lowerContact_from_boxMin_of_neumann
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    (hside : ∀ i, a i < b i)
    {z : (Fin (n + 1) → ℝ) → ℝ} {x : Fin (n + 1) → ℝ}
    {F : ℝ → ℝ} {zstar beta q rho zt : ℝ}
    (hx : x ∈ Icc a b)
    (hmin : IsMinOn z (Icc a b) x)
    (hcont : ContinuousOn z (Icc a b))
    (hNeumann : ∀ i : Fin (n + 1),
      x i = a i ∨ x i = b i → deriv (coordinateSlice z x i) 0 = 0)
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hFstar : F zstar = 0) (hs : z x ≤ zstar)
    (hdiss : (z x - zstar) * F (z x) ≤ -beta * |z x - zstar| ^ q)
    (hPDE : zt =
      (∑ i : Fin (n + 1), deriv (deriv (coordinateSlice z x i)) 0) +
        rho * F (z x)) :
    0 ≤ zt := by
  exact lowerContact_timeDerivative_nonneg hbeta hrho
    (laplacianTrace_nonneg_of_boxMin_of_neumann hside hx hmin hcont hNeumann)
    hFstar hs hdiss hPDE

end AMLStabilization
