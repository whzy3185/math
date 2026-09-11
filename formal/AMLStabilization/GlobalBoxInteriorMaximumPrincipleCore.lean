import Mathlib
import AMLStabilization.GlobalBoxContactSelectionCore
import AMLStabilization.BoxInteriorContactCore

open Set

namespace AMLStabilization

/-- No positive upper tilted violation can occur if every selected spatial
maximum is an interior point and the pointwise PDE has the dissipative contact
sign there. -/
theorem no_upper_tilted_violation_on_box_of_interior_maxima
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {s T hi eps zstar beta q : ℝ}
    (hside : ∀ i, a i ≤ b i) (hsT : s < T) (heps : 0 < eps)
    (z rho zt : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (F : ℝ → ℝ)
    (hzcont : ContinuousOn
      (fun p : ℝ × (Fin (n + 1) → ℝ) => z p.1 p.2)
      (Icc s T ×ˢ Icc a b))
    (hinit : ∀ x ∈ Icc a b, z s x ≤ hi)
    (hMaxInterior : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      IsMaxOn (z t) (Icc a b) x → x ∈ interior (Icc a b))
    (hSpatialCont : ∀ t ∈ Icc s T, ∀ x ∈ interior (Icc a b),
      ContinuousAt (z t) x)
    (hTimeDeriv : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      HasDerivAt (fun tau => z tau x) (zt t x) t)
    (hrho : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b, 0 ≤ rho t x)
    (hbeta : 0 < beta) (hFstar : F zstar = 0) (hzstarhi : zstar ≤ hi)
    (hdiss : ∀ r, (r - zstar) * F r ≤ -beta * |r - zstar| ^ q)
    (hPDE : ∀ t ∈ Ioc s T, ∀ x ∈ interior (Icc a b),
      zt t x =
        (∑ i : Fin (n + 1),
          deriv (deriv (coordinateSlice (z t) x i)) 0) +
          rho t x * F (z t x)) :
    ¬ ∃ t ∈ Icc s T, ∃ x ∈ Icc a b,
      hi + eps * (t - s) < z t x := by
  intro hviol
  obtain ⟨t0, ht0, x0, hx0, hst, hval, hsp, htime⟩ :=
    exists_upper_tilted_contact_on_box hside hsT z hzcont hinit hviol
  have ht0oc : t0 ∈ Ioc s T := ⟨hst, ht0.2⟩
  have hxint : x0 ∈ interior (Icc a b) :=
    hMaxInterior t0 ht0oc x0 hx0 hsp
  have htd := hTimeDeriv t0 ht0oc x0 hx0
  have htimeSign : eps ≤ zt t0 x0 :=
    derivative_ge_epsilon_at_upper_Icc_max hst ht0.2 htime htd
  have htilt0 : 0 ≤ eps * (t0 - s) :=
    mul_nonneg heps.le (sub_nonneg.mpr hst.le)
  have hzstar : zstar ≤ z t0 x0 := by
    linarith
  have hpdeSign : zt t0 x0 ≤ 0 :=
    upperContact_from_boxInteriorMax hsp hxint
      (hSpatialCont t0 ht0 x0 hxint)
      hbeta (hrho t0 ht0oc x0 hx0) hFstar hzstar (hdiss (z t0 x0))
      (hPDE t0 ht0oc x0 hxint)
  linarith

/-- Lower tilted violations are impossible under the analogous interior-minimum
hypothesis. -/
theorem no_lower_tilted_violation_on_box_of_interior_minima
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {s T lo eps zstar beta q : ℝ}
    (hside : ∀ i, a i ≤ b i) (hsT : s < T) (heps : 0 < eps)
    (z rho zt : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (F : ℝ → ℝ)
    (hzcont : ContinuousOn
      (fun p : ℝ × (Fin (n + 1) → ℝ) => z p.1 p.2)
      (Icc s T ×ˢ Icc a b))
    (hinit : ∀ x ∈ Icc a b, lo ≤ z s x)
    (hMinInterior : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      IsMinOn (z t) (Icc a b) x → x ∈ interior (Icc a b))
    (hSpatialCont : ∀ t ∈ Icc s T, ∀ x ∈ interior (Icc a b),
      ContinuousAt (z t) x)
    (hTimeDeriv : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      HasDerivAt (fun tau => z tau x) (zt t x) t)
    (hrho : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b, 0 ≤ rho t x)
    (hbeta : 0 < beta) (hFstar : F zstar = 0) (hlozstar : lo ≤ zstar)
    (hdiss : ∀ r, (r - zstar) * F r ≤ -beta * |r - zstar| ^ q)
    (hPDE : ∀ t ∈ Ioc s T, ∀ x ∈ interior (Icc a b),
      zt t x =
        (∑ i : Fin (n + 1),
          deriv (deriv (coordinateSlice (z t) x i)) 0) +
          rho t x * F (z t x)) :
    ¬ ∃ t ∈ Icc s T, ∃ x ∈ Icc a b,
      z t x < lo - eps * (t - s) := by
  intro hviol
  obtain ⟨t0, ht0, x0, hx0, hst, hval, hsp, htime⟩ :=
    exists_lower_tilted_contact_on_box hside hsT z hzcont hinit hviol
  have ht0oc : t0 ∈ Ioc s T := ⟨hst, ht0.2⟩
  have hxint : x0 ∈ interior (Icc a b) :=
    hMinInterior t0 ht0oc x0 hx0 hsp
  have htd := hTimeDeriv t0 ht0oc x0 hx0
  have htimeSign : zt t0 x0 ≤ -eps :=
    derivative_le_neg_epsilon_at_lower_Icc_min hst ht0.2 htime htd
  have htilt0 : 0 ≤ eps * (t0 - s) :=
    mul_nonneg heps.le (sub_nonneg.mpr hst.le)
  have hzstar : z t0 x0 ≤ zstar := by
    linarith
  have hpdeSign : 0 ≤ zt t0 x0 :=
    lowerContact_from_boxInteriorMin hsp hxint
      (hSpatialCont t0 ht0 x0 hxint)
      hbeta (hrho t0 ht0oc x0 hx0) hFstar hzstar (hdiss (z t0 x0))
      (hPDE t0 ht0oc x0 hxint)
  linarith

/-- Global upper invariant bound on a compact box, provided all relevant
spatial maxima are interior.  The epsilon tilt is chosen automatically from a
hypothetical violation. -/
theorem upper_invariant_on_box_of_interior_maxima
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {s T hi zstar beta q : ℝ}
    (hside : ∀ i, a i ≤ b i) (hsT : s < T)
    (z rho zt : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (F : ℝ → ℝ)
    (hzcont : ContinuousOn
      (fun p : ℝ × (Fin (n + 1) → ℝ) => z p.1 p.2)
      (Icc s T ×ˢ Icc a b))
    (hinit : ∀ x ∈ Icc a b, z s x ≤ hi)
    (hMaxInterior : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      IsMaxOn (z t) (Icc a b) x → x ∈ interior (Icc a b))
    (hSpatialCont : ∀ t ∈ Icc s T, ∀ x ∈ interior (Icc a b),
      ContinuousAt (z t) x)
    (hTimeDeriv : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      HasDerivAt (fun tau => z tau x) (zt t x) t)
    (hrho : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b, 0 ≤ rho t x)
    (hbeta : 0 < beta) (hFstar : F zstar = 0) (hzstarhi : zstar ≤ hi)
    (hdiss : ∀ r, (r - zstar) * F r ≤ -beta * |r - zstar| ^ q)
    (hPDE : ∀ t ∈ Ioc s T, ∀ x ∈ interior (Icc a b),
      zt t x =
        (∑ i : Fin (n + 1),
          deriv (deriv (coordinateSlice (z t) x i)) 0) +
          rho t x * F (z t x)) :
    ∀ t ∈ Icc s T, ∀ x ∈ Icc a b, z t x ≤ hi := by
  intro t ht x hx
  by_contra hnot
  have hvi : hi < z t x := lt_of_not_ge hnot
  have htne : t ≠ s := by
    intro hts
    subst t
    exact (not_lt_of_ge (hinit x hx)) hvi
  have hst : s < t := lt_of_le_of_ne ht.1 (Ne.symm htne)
  let gap : ℝ := z t x - hi
  let dt : ℝ := t - s
  let eps : ℝ := gap / (2 * dt)
  have hgap : 0 < gap := by simpa [gap] using sub_pos.mpr hvi
  have hdt : 0 < dt := by simpa [dt] using sub_pos.mpr hst
  have heps : 0 < eps := by
    dsimp [eps]
    exact div_pos hgap (mul_pos (by norm_num) hdt)
  have heq : eps * (t - s) = gap / 2 := by
    dsimp [eps, dt]
    field_simp [ne_of_gt hdt]
    <;> ring
  have htilt : hi + eps * (t - s) < z t x := by
    rw [heq]
    dsimp [gap]
    linarith
  have himpossible := no_upper_tilted_violation_on_box_of_interior_maxima
    hside hsT heps z rho zt F hzcont hinit hMaxInterior hSpatialCont
    hTimeDeriv hrho hbeta hFstar hzstarhi hdiss hPDE
  exact himpossible ⟨t, ht, x, hx, htilt⟩

/-- Global lower invariant bound on a compact box, under the analogous
interior-minimum hypothesis. -/
theorem lower_invariant_on_box_of_interior_minima
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {s T lo zstar beta q : ℝ}
    (hside : ∀ i, a i ≤ b i) (hsT : s < T)
    (z rho zt : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (F : ℝ → ℝ)
    (hzcont : ContinuousOn
      (fun p : ℝ × (Fin (n + 1) → ℝ) => z p.1 p.2)
      (Icc s T ×ˢ Icc a b))
    (hinit : ∀ x ∈ Icc a b, lo ≤ z s x)
    (hMinInterior : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      IsMinOn (z t) (Icc a b) x → x ∈ interior (Icc a b))
    (hSpatialCont : ∀ t ∈ Icc s T, ∀ x ∈ interior (Icc a b),
      ContinuousAt (z t) x)
    (hTimeDeriv : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      HasDerivAt (fun tau => z tau x) (zt t x) t)
    (hrho : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b, 0 ≤ rho t x)
    (hbeta : 0 < beta) (hFstar : F zstar = 0) (hlozstar : lo ≤ zstar)
    (hdiss : ∀ r, (r - zstar) * F r ≤ -beta * |r - zstar| ^ q)
    (hPDE : ∀ t ∈ Ioc s T, ∀ x ∈ interior (Icc a b),
      zt t x =
        (∑ i : Fin (n + 1),
          deriv (deriv (coordinateSlice (z t) x i)) 0) +
          rho t x * F (z t x)) :
    ∀ t ∈ Icc s T, ∀ x ∈ Icc a b, lo ≤ z t x := by
  intro t ht x hx
  by_contra hnot
  have hvi : z t x < lo := lt_of_not_ge hnot
  have htne : t ≠ s := by
    intro hts
    subst t
    exact (not_lt_of_ge (hinit x hx)) hvi
  have hst : s < t := lt_of_le_of_ne ht.1 (Ne.symm htne)
  let gap : ℝ := lo - z t x
  let dt : ℝ := t - s
  let eps : ℝ := gap / (2 * dt)
  have hgap : 0 < gap := by simpa [gap] using sub_pos.mpr hvi
  have hdt : 0 < dt := by simpa [dt] using sub_pos.mpr hst
  have heps : 0 < eps := by
    dsimp [eps]
    exact div_pos hgap (mul_pos (by norm_num) hdt)
  have heq : eps * (t - s) = gap / 2 := by
    dsimp [eps, dt]
    field_simp [ne_of_gt hdt]
    <;> ring
  have htilt : z t x < lo - eps * (t - s) := by
    rw [heq]
    dsimp [gap]
    linarith
  have himpossible := no_lower_tilted_violation_on_box_of_interior_minima
    hside hsT heps z rho zt F hzcont hinit hMinInterior hSpatialCont
    hTimeDeriv hrho hbeta hFstar hlozstar hdiss hPDE
  exact himpossible ⟨t, ht, x, hx, htilt⟩

/-- Two-sided invariant interval on a compact box when upper and lower spatial
contacts occur in the interior. -/
theorem invariant_interval_on_box_of_interior_extrema
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {s T lo hi zstar beta q : ℝ}
    (hside : ∀ i, a i ≤ b i) (hsT : s < T)
    (z rho zt : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (F : ℝ → ℝ)
    (hzcont : ContinuousOn
      (fun p : ℝ × (Fin (n + 1) → ℝ) => z p.1 p.2)
      (Icc s T ×ˢ Icc a b))
    (hinit : ∀ x ∈ Icc a b, lo ≤ z s x ∧ z s x ≤ hi)
    (hMaxInterior : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      IsMaxOn (z t) (Icc a b) x → x ∈ interior (Icc a b))
    (hMinInterior : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      IsMinOn (z t) (Icc a b) x → x ∈ interior (Icc a b))
    (hSpatialCont : ∀ t ∈ Icc s T, ∀ x ∈ interior (Icc a b),
      ContinuousAt (z t) x)
    (hTimeDeriv : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b,
      HasDerivAt (fun tau => z tau x) (zt t x) t)
    (hrho : ∀ t ∈ Ioc s T, ∀ x ∈ Icc a b, 0 ≤ rho t x)
    (hbeta : 0 < beta) (hFstar : F zstar = 0)
    (hlozstar : lo ≤ zstar) (hzstarhi : zstar ≤ hi)
    (hdiss : ∀ r, (r - zstar) * F r ≤ -beta * |r - zstar| ^ q)
    (hPDE : ∀ t ∈ Ioc s T, ∀ x ∈ interior (Icc a b),
      zt t x =
        (∑ i : Fin (n + 1),
          deriv (deriv (coordinateSlice (z t) x i)) 0) +
          rho t x * F (z t x)) :
    ∀ t ∈ Icc s T, ∀ x ∈ Icc a b, lo ≤ z t x ∧ z t x ≤ hi := by
  have hupper := upper_invariant_on_box_of_interior_maxima
    hside hsT z rho zt F hzcont (fun x hx => (hinit x hx).2)
    hMaxInterior hSpatialCont hTimeDeriv hrho hbeta hFstar hzstarhi hdiss hPDE
  have hlower := lower_invariant_on_box_of_interior_minima
    hside hsT z rho zt F hzcont (fun x hx => (hinit x hx).1)
    hMinInterior hSpatialCont hTimeDeriv hrho hbeta hFstar hlozstar hdiss hPDE
  intro t ht x hx
  exact ⟨hlower t ht x hx, hupper t ht x hx⟩

end AMLStabilization
