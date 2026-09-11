import Mathlib
import AMLStabilization.FirstContactBarrierCore

open Set Filter
open scoped Topology Convex

namespace AMLStabilization

/-- At the right-hand point `t0` of a nontrivial interval beginning at `s`,
the vector from `t0` back to `s` belongs to the positive tangent cone. -/
theorem sub_start_mem_posTangentCone_Icc
    {s T t0 : ℝ} (hs : s < t0) (ht0 : t0 ≤ T) :
    s - t0 ∈ posTangentConeAt (Icc s T) t0 := by
  have hseg : segment ℝ t0 s ⊆ Icc s T := by
    rw [segment_symm, segment_eq_Icc hs.le]
    intro y hy
    exact ⟨hy.1, hy.2.trans ht0⟩
  exact sub_mem_posTangentConeAt_of_segment_subset hseg

/-- If `y(t)-eps*(t-s)` has a maximum on `[s,T]` at a time `t0>s`, then
`y'(t0) >= eps`. -/
theorem derivative_ge_epsilon_at_upper_Icc_max
    {y : ℝ → ℝ} {s T t0 dy eps : ℝ}
    (hs : s < t0) (ht0 : t0 ≤ T)
    (hmax : IsMaxOn (fun t => y t - eps * (t - s)) (Icc s T) t0)
    (hy : HasDerivAt y dy t0) :
    eps ≤ dy := by
  have hcontact : IsLocalMaxOn (fun t => y t - eps * (t - s)) (Icc s T) t0 :=
    IsMaxOn.isLocalMaxOn hmax
  have hlin : HasDerivAt (fun t : ℝ => eps * (t - s)) eps t0 := by
    simpa [mul_one] using ((hasDerivAt_id t0).sub_const s).const_mul eps
  have hshift : HasDerivAt (fun t => y t - eps * (t - s)) (dy - eps) t0 :=
    hy.sub hlin
  have hdir := sub_start_mem_posTangentCone_Icc hs ht0
  have h := hcontact.hasFDerivWithinAt_nonpos
    hshift.hasFDerivAt.hasFDerivWithinAt hdir
  have hmul : (s - t0) * (dy - eps) ≤ 0 := by
    simpa [ContinuousLinearMap.toSpanSingleton_apply] using h
  have hneg : s - t0 < 0 := sub_neg.mpr hs
  nlinarith

/-- Lower-barrier analogue of `derivative_ge_epsilon_at_upper_Icc_max`. -/
theorem derivative_le_neg_epsilon_at_lower_Icc_min
    {y : ℝ → ℝ} {s T t0 dy eps : ℝ}
    (hs : s < t0) (ht0 : t0 ≤ T)
    (hmin : IsMinOn (fun t => y t + eps * (t - s)) (Icc s T) t0)
    (hy : HasDerivAt y dy t0) :
    dy ≤ -eps := by
  have hcontact : IsLocalMinOn (fun t => y t + eps * (t - s)) (Icc s T) t0 :=
    IsMinOn.isLocalMinOn hmin
  have hlin : HasDerivAt (fun t : ℝ => eps * (t - s)) eps t0 := by
    simpa [mul_one] using ((hasDerivAt_id t0).sub_const s).const_mul eps
  have hshift : HasDerivAt (fun t => y t + eps * (t - s)) (dy + eps) t0 :=
    hy.add hlin
  have hdir := sub_start_mem_posTangentCone_Icc hs ht0
  have h := hcontact.hasFDerivWithinAt_nonneg
    hshift.hasFDerivAt.hasFDerivWithinAt hdir
  have hmul : 0 ≤ (s - t0) * (dy + eps) := by
    simpa [ContinuousLinearMap.toSpanSingleton_apply] using h
  have hneg : s - t0 < 0 := sub_neg.mpr hs
  nlinarith

/-- Compact-cylinder upper-contact selection. -/
theorem exists_upper_tilted_contact_on_box
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {s T hi eps : ℝ}
    (hside : ∀ i, a i ≤ b i) (hsT : s < T)
    (z : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (hzcont : ContinuousOn
      (fun p : ℝ × (Fin (n + 1) → ℝ) => z p.1 p.2)
      (Icc s T ×ˢ Icc a b))
    (hinit : ∀ x ∈ Icc a b, z s x ≤ hi)
    (hviol : ∃ t ∈ Icc s T, ∃ x ∈ Icc a b,
      hi + eps * (t - s) < z t x) :
    ∃ t0 ∈ Icc s T, ∃ x0 ∈ Icc a b,
      s < t0 ∧
      hi + eps * (t0 - s) < z t0 x0 ∧
      IsMaxOn (z t0) (Icc a b) x0 ∧
      IsMaxOn (fun t => z t x0 - eps * (t - s)) (Icc s T) t0 := by
  let cyl : Set (ℝ × (Fin (n + 1) → ℝ)) := Icc s T ×ˢ Icc a b
  let barrier : (ℝ × (Fin (n + 1) → ℝ)) → ℝ :=
    fun p => hi + eps * (p.1 - s)
  let phi : (ℝ × (Fin (n + 1) → ℝ)) → ℝ :=
    fun p => z p.1 p.2 - barrier p
  have hcyl : IsCompact cyl := by
    dsimp [cyl]
    exact isCompact_Icc.prod isCompact_Icc
  have hboxne : (Icc a b).Nonempty := by
    refine ⟨a, ?_⟩
    exact ⟨fun _ => le_rfl, hside⟩
  have hcylne : cyl.Nonempty := by
    rcases hboxne with ⟨x, hx⟩
    exact ⟨(s, x), ⟨⟨le_rfl, hsT.le⟩, hx⟩⟩
  have hbar : Continuous barrier := by
    dsimp [barrier]
    fun_prop
  have hphiCont : ContinuousOn phi cyl := by
    simpa [phi, cyl] using hzcont.sub hbar.continuousOn
  obtain ⟨p0, hp0, hpmax⟩ := hcyl.exists_isMaxOn hcylne hphiCont
  rcases hviol with ⟨tw, htw, xw, hxw, hw⟩
  have hwphi : 0 < phi (tw, xw) := by
    dsimp [phi, barrier]
    linarith
  have hmaxpos : 0 < phi p0 := by
    exact lt_of_lt_of_le hwphi (hpmax (a := (tw, xw)) ⟨htw, hxw⟩)
  have ht0gt : s < p0.1 := by
    have hsle : s ≤ p0.1 := hp0.1.1
    rcases hsle.eq_or_lt with hEq | hlt
    · have hz0 := hinit p0.2 hp0.2
      have hphi0 : phi p0 ≤ 0 := by
        dsimp [phi, barrier]
        rw [← hEq]
        simp
        exact hz0
      linarith
    · exact hlt
  have hcontactval : hi + eps * (p0.1 - s) < z p0.1 p0.2 := by
    dsimp [phi, barrier] at hmaxpos
    linarith
  have hsp : IsMaxOn (z p0.1) (Icc a b) p0.2 := by
    intro x hx
    have h := hpmax (a := (p0.1, x)) ⟨hp0.1, hx⟩
    dsimp [phi, barrier] at h
    linarith
  have htime : IsMaxOn
      (fun t => z t p0.2 - eps * (t - s)) (Icc s T) p0.1 := by
    intro t ht
    have h := hpmax (a := (t, p0.2)) ⟨ht, hp0.2⟩
    dsimp [phi, barrier] at h
    linarith
  exact ⟨p0.1, hp0.1, p0.2, hp0.2, ht0gt, hcontactval, hsp, htime⟩

/-- Compact-cylinder lower-contact selection, symmetric to the upper case. -/
theorem exists_lower_tilted_contact_on_box
    {n : ℕ} {a b : Fin (n + 1) → ℝ}
    {s T lo eps : ℝ}
    (hside : ∀ i, a i ≤ b i) (hsT : s < T)
    (z : ℝ → (Fin (n + 1) → ℝ) → ℝ)
    (hzcont : ContinuousOn
      (fun p : ℝ × (Fin (n + 1) → ℝ) => z p.1 p.2)
      (Icc s T ×ˢ Icc a b))
    (hinit : ∀ x ∈ Icc a b, lo ≤ z s x)
    (hviol : ∃ t ∈ Icc s T, ∃ x ∈ Icc a b,
      z t x < lo - eps * (t - s)) :
    ∃ t0 ∈ Icc s T, ∃ x0 ∈ Icc a b,
      s < t0 ∧
      z t0 x0 < lo - eps * (t0 - s) ∧
      IsMinOn (z t0) (Icc a b) x0 ∧
      IsMinOn (fun t => z t x0 + eps * (t - s)) (Icc s T) t0 := by
  let cyl : Set (ℝ × (Fin (n + 1) → ℝ)) := Icc s T ×ˢ Icc a b
  let barrier : (ℝ × (Fin (n + 1) → ℝ)) → ℝ :=
    fun p => lo - eps * (p.1 - s)
  let phi : (ℝ × (Fin (n + 1) → ℝ)) → ℝ :=
    fun p => barrier p - z p.1 p.2
  have hcyl : IsCompact cyl := by
    dsimp [cyl]
    exact isCompact_Icc.prod isCompact_Icc
  have hboxne : (Icc a b).Nonempty := by
    refine ⟨a, ?_⟩
    exact ⟨fun _ => le_rfl, hside⟩
  have hcylne : cyl.Nonempty := by
    rcases hboxne with ⟨x, hx⟩
    exact ⟨(s, x), ⟨⟨le_rfl, hsT.le⟩, hx⟩⟩
  have hbar : Continuous barrier := by
    dsimp [barrier]
    fun_prop
  have hphiCont : ContinuousOn phi cyl := by
    simpa [phi, cyl] using hbar.continuousOn.sub hzcont
  obtain ⟨p0, hp0, hpmax⟩ := hcyl.exists_isMaxOn hcylne hphiCont
  rcases hviol with ⟨tw, htw, xw, hxw, hw⟩
  have hwphi : 0 < phi (tw, xw) := by
    dsimp [phi, barrier]
    linarith
  have hmaxpos : 0 < phi p0 := by
    exact lt_of_lt_of_le hwphi (hpmax (a := (tw, xw)) ⟨htw, hxw⟩)
  have ht0gt : s < p0.1 := by
    have hsle : s ≤ p0.1 := hp0.1.1
    rcases hsle.eq_or_lt with hEq | hlt
    · have hz0 := hinit p0.2 hp0.2
      have hphi0 : phi p0 ≤ 0 := by
        dsimp [phi, barrier]
        rw [← hEq]
        simp
        linarith
      linarith
    · exact hlt
  have hcontactval : z p0.1 p0.2 < lo - eps * (p0.1 - s) := by
    dsimp [phi, barrier] at hmaxpos
    linarith
  have hsp : IsMinOn (z p0.1) (Icc a b) p0.2 := by
    intro x hx
    have h := hpmax (a := (p0.1, x)) ⟨hp0.1, hx⟩
    dsimp [phi, barrier] at h
    linarith
  have htime : IsMinOn
      (fun t => z t p0.2 + eps * (t - s)) (Icc s T) p0.1 := by
    intro t ht
    have h := hpmax (a := (t, p0.2)) ⟨ht, hp0.2⟩
    dsimp [phi, barrier] at h
    linarith
  exact ⟨p0.1, hp0.1, p0.2, hp0.2, ht0gt, hcontactval, hsp, htime⟩

end AMLStabilization
