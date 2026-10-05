import TargetA.Period8AntiperiodicCells
import TargetA.Period8ExactRoot

namespace TargetA

/-- Real part of the standard finite Fourier character. -/
theorem period8_std_char_re (N : ℕ) [NeZero N] (k : ZMod N) :
    (ZMod.stdAddChar k).re = Real.cos (2 * Real.pi * (k.val : ℝ) / (N : ℝ)) := by
  rw [ZMod.stdAddChar_apply, ZMod.toCircle_apply]
  have he : 2 * (Real.pi : ℂ) * Complex.I * (k.val : ℂ) / (N : ℂ) =
      ((2 * Real.pi * (k.val : ℝ) / (N : ℝ) : ℝ) : ℂ) * Complex.I := by
    push_cast
    ring
  rw [he, Complex.exp_ofReal_mul_I_re]

/-- Every nontrivial phase on the doubled cycle is at least one grid spacing from 1. -/
theorem period8_nonzero_phase_re_le_first (L : ℕ) (hL : 0 < L)
    [NeZero (2 * L)] (k : ZMod (2 * L)) (hk : k ≠ 0) :
    (ZMod.stdAddChar k).re ≤ Real.cos (Real.pi / (L : ℝ)) := by
  have hLr : (0 : ℝ) < (L : ℝ) := by exact_mod_cast hL
  have hkpos : 0 < k.val := by
    by_contra h
    have hz : k.val = 0 := by omega
    apply hk
    rw [← ZMod.natCast_zmod_val k, hz]
    simp
  have hku : k.val + 1 ≤ 2 * L := by have h := ZMod.val_lt k; omega
  have hkone : (1 : ℝ) ≤ (k.val : ℝ) := by exact_mod_cast hkpos
  have hkup : (k.val : ℝ) + 1 ≤ 2 * (L : ℝ) := by exact_mod_cast hku
  rw [period8_std_char_re]
  have hangle : 2 * Real.pi * (k.val : ℝ) / ((2 * L : ℕ) : ℝ) =
      Real.pi * (k.val : ℝ) / (L : ℝ) := by
    push_cast
    field_simp <;> ring
  rw [hangle]
  let theta := Real.pi * (k.val : ℝ) / (L : ℝ)
  have hlo : Real.pi / (L : ℝ) ≤ theta := by
    dsimp [theta]
    apply (div_le_div_iff_of_pos_right hLr).mpr
    nlinarith [Real.pi_pos]
  have hhi : theta ≤ 2 * Real.pi - Real.pi / (L : ℝ) := by
    apply (le_sub_iff_add_le).mpr
    dsimp [theta]
    rw [← add_div]
    apply (div_le_iff₀ hLr).mpr
    nlinarith [Real.pi_pos]
  have hzero : 0 ≤ Real.pi / (L : ℝ) := le_of_lt (div_pos Real.pi_pos hLr)
  change Real.cos theta ≤ Real.cos (Real.pi / (L : ℝ))
  by_cases ht : theta ≤ Real.pi
  · exact Real.cos_le_cos_of_nonneg_of_le_pi hzero ht hlo
  · have href : 2 * Real.pi - theta ≤ Real.pi := by linarith
    have hreflo : Real.pi / (L : ℝ) ≤ 2 * Real.pi - theta := by linarith
    have hh := Real.cos_le_cos_of_nonneg_of_le_pi hzero href hreflo
    have he : Real.cos (2 * Real.pi - theta) = Real.cos theta := by
      rw [Real.cos_sub]
      simp
    rwa [he] at hh

theorem period8_antiperiodic_phase_re_le_first (L : ℕ) (hL : 0 < L)
    [NeZero (2 * L)] (k : ZMod (2 * L))
    (hk : (ZMod.stdAddChar k)^L = -1) :
    (ZMod.stdAddChar k).re ≤ Real.cos (Real.pi / (L : ℝ)) := by
  apply period8_nonzero_phase_re_le_first L hL k
  intro hz
  subst k
  norm_num at hk

/-- The first positive phase is allowed by the antiperiodic boundary condition. -/
theorem period8_first_phase_antiperiodic (L : ℕ) (hL : 0 < L)
    [NeZero (2 * L)] :
    (ZMod.stdAddChar (1 : ZMod (2 * L)))^L = -1 := by
  rw [← AddChar.map_nsmul_eq_pow]
  simp only [nsmul_eq_mul, mul_one]
  have hc : ZMod.stdAddChar (L : ZMod (2 * L)) =
      Complex.exp (2 * (Real.pi : ℂ) * Complex.I * (L : ℂ) / ((2 * L : ℕ) : ℂ)) := by
    simpa using ZMod.stdAddChar_coe (N := 2 * L) (L : ℤ)
  rw [hc]
  have hLc : (L : ℂ) ≠ 0 := by exact_mod_cast (Nat.ne_of_gt hL)
  have he : 2 * (Real.pi : ℂ) * Complex.I * (L : ℂ) / ((2 * L : ℕ) : ℂ) =
      (Real.pi : ℂ) * Complex.I := by
    push_cast
    field_simp [hLc] <;> ring
  rw [he, Complex.exp_pi_mul_I]

/-- The maximum phase parameter is attained, including L=1. -/
theorem period8_first_phase_re (L : ℕ) (hL : 0 < L) [NeZero (2 * L)] :
    (ZMod.stdAddChar (1 : ZMod (2 * L))).re = Real.cos (Real.pi / (L : ℝ)) := by
  rw [period8_std_char_re]
  have hv : (1 : ZMod (2 * L)).val = 1 := by
    rw [ZMod.val_one_eq_one_mod, Nat.mod_eq_of_lt (by omega)]
  rw [hv]
  congr 1
  push_cast
  field_simp <;> ring

end TargetA
