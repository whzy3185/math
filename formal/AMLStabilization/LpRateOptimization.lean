import Mathlib
import AMLStabilization.LpExponentCore

namespace AMLStabilization

/-- The exact algebraic-rate threshold stated in the strengthened manuscript. -/
noncomputable def manuscriptRateThreshold (theta n p : ℝ) : ℝ :=
  (1 / theta) * min 1 (2 * (p - n) / (p * n))

/-- The critical spatial exponent at which the transfer rate equals `mu`. -/
noncomputable def rateCriticalExponent (theta p mu : ℝ) : ℝ :=
  2 * p / (2 + mu * theta * p)

/--
Every target rate strictly below the manuscript threshold can be realized by
an admissible Hölder/smoothing exponent `r`.  This is the exact optimization
step behind

`mu < (1/theta) * min {1, 2(p-n)/(pn)}`.
-/
theorem exists_lpExponent_for_target_rate
    {theta n p mu : ℝ}
    (htheta : 0 < theta) (hn : 0 < n)
    (hp : max n 2 < p)
    (hmu0 : 0 < mu)
    (hmu : mu < manuscriptRateThreshold theta n p) :
    ∃ r : ℝ,
      n < r ∧ r < p ∧
      2 < holderPartner p r ∧
      1 / r = 1 / p + 1 / holderPartner p r ∧
      mu < transferRate theta p r := by
  have h2p : 2 < p := lt_of_le_of_lt (le_max_right n 2) hp
  have hp0 : 0 < p := lt_trans (by norm_num) h2p
  have hnp : n < p := lt_of_le_of_lt (le_max_left n 2) hp
  have hpn : 0 < p - n := sub_pos.mpr hnp
  have hpnprod : 0 < p * n := mul_pos hp0 hn
  let A : ℝ := 2 * (p - n) / (p * n)
  have hA0 : 0 < A := by
    dsimp [A]
    exact div_pos (mul_pos (by norm_num) hpn) hpnprod
  have hinvTheta : 0 < (1 / theta : ℝ) := one_div_pos.mpr htheta
  have hminScale :
      (1 / theta) * min 1 A =
        min ((1 / theta) * 1) ((1 / theta) * A) :=
    mul_min_of_nonneg 1 A hinvTheta.le
  have hmuMin : mu < min (1 / theta) ((1 / theta) * A) := by
    unfold manuscriptRateThreshold at hmu
    rw [show 2 * (p - n) / (p * n) = A by rfl, hminScale] at hmu
    simpa using hmu
  have hmuInv : mu < 1 / theta := (lt_min_iff.mp hmuMin).1
  have hmuScaled : mu < (1 / theta) * A := (lt_min_iff.mp hmuMin).2
  have hmuTheta : mu * theta < 1 := by
    exact (lt_div_iff₀ htheta).mp hmuInv
  have hscaledEq :
      (1 / theta) * A = 2 * (p - n) / (theta * p * n) := by
    dsimp [A]
    field_simp [ne_of_gt htheta, ne_of_gt hp0, ne_of_gt hn]
    <;> ring
  rw [hscaledEq] at hmuScaled
  have hdenScaled : 0 < theta * p * n := by positivity
  have hmuDen : mu * (theta * p * n) < 2 * (p - n) :=
    (lt_div_iff₀ hdenScaled).mp hmuScaled

  let D : ℝ := 2 + mu * theta * p
  have hD : 0 < D := by
    dsimp [D]
    positivity
  have hp2 : 0 < p + 2 := by linarith
  have hdenLt : D < p + 2 := by
    have hmul := mul_lt_mul_of_pos_right hmuTheta hp0
    dsimp [D]
    nlinarith
  have hfracCritical :
      2 * p / (p + 2) < rateCriticalExponent theta p mu := by
    unfold rateCriticalExponent
    rw [show 2 + mu * theta * p = D by rfl]
    rw [div_lt_div_iff₀ hp2 hD]
    exact mul_lt_mul_of_pos_left hdenLt (mul_pos (by norm_num) hp0)
  have hnCritical : n < rateCriticalExponent theta p mu := by
    unfold rateCriticalExponent
    rw [show 2 + mu * theta * p = D by rfl]
    rw [lt_div_iff₀ hD]
    calc
      n * D = 2 * n + mu * (theta * p * n) := by
        dsimp [D]
        ring
      _ < 2 * n + 2 * (p - n) := add_lt_add_left hmuDen (2 * n)
      _ = 2 * p := by ring
  have hCriticalP : rateCriticalExponent theta p mu < p := by
    unfold rateCriticalExponent
    rw [show 2 + mu * theta * p = D by rfl]
    rw [div_lt_iff₀ hD]
    have hposExtra : 0 < p * (mu * theta * p) := by positivity
    calc
      2 * p < 2 * p + p * (mu * theta * p) := lt_add_of_pos_right _ hposExtra
      _ = p * D := by
        dsimp [D]
        ring
  have hLowerCritical :
      lpLowerThreshold n p < rateCriticalExponent theta p mu := by
    unfold lpLowerThreshold
    exact max_lt hnCritical hfracCritical

  let r : ℝ :=
    (lpLowerThreshold n p + rateCriticalExponent theta p mu) / 2
  have hLowerR : lpLowerThreshold n p < r := by
    dsimp [r]
    linarith
  have hRCritical : r < rateCriticalExponent theta p mu := by
    dsimp [r]
    linarith
  have hrp : r < p := lt_trans hRCritical hCriticalP
  have hnr : n < r := by
    have hnLower : n ≤ lpLowerThreshold n p := by
      unfold lpLowerThreshold
      exact le_max_left _ _
    exact lt_of_le_of_lt hnLower hLowerR
  have hthresholdR : 2 * p / (p + 2) < r := by
    have hfracLower : 2 * p / (p + 2) ≤ lpLowerThreshold n p := by
      unfold lpLowerThreshold
      exact le_max_right _ _
    exact lt_of_le_of_lt hfracLower hLowerR
  have hr0 : 0 < r := lt_trans hn hnr
  have hs2 : 2 < holderPartner p r :=
    two_lt_holderPartner_of_threshold h2p hrp hthresholdR
  have hrel : 1 / r = 1 / p + 1 / holderPartner p r :=
    holderPartner_identity hr0 hrp

  have hRCritical' : r < 2 * p / D := by
    simpa [rateCriticalExponent, D] using hRCritical
  have hrD : r * D < 2 * p := (lt_div_iff₀ hD).mp hRCritical'
  have hrateNumer : mu * (theta * p * r) < 2 * (p - r) := by
    have hsum : 2 * r + mu * (theta * p * r) < 2 * p := by
      calc
        2 * r + mu * (theta * p * r) = r * D := by
          dsimp [D]
          ring
        _ < 2 * p := hrD
    linarith
  have hdenRate : 0 < theta * p * r := by positivity
  have hmurate : mu < 2 * (p - r) / (theta * p * r) :=
    (lt_div_iff₀ hdenRate).2 hrateNumer
  refine ⟨r, hnr, hrp, hs2, hrel, ?_⟩
  simpa [transferRate] using hmurate

end AMLStabilization
