import Mathlib
import TargetA.HamiltonGauge

namespace TargetA

/-!
The finite Fourier transform used below is Mathlib's transform on `ZMod L`.
We record explicitly the translation identity needed to turn a block-circulant
cell operator into its Bloch fibres.
-/

noncomputable def cellTranslation {L : ℕ} (a : ZMod L)
    (f : ZMod L → ℂ) : ZMod L → ℂ :=
  fun j => f (a + j)

theorem dft_cellTranslation {L : ℕ} [NeZero L] (a k : ZMod L)
    (f : ZMod L → ℂ) :
    ZMod.dft (cellTranslation a f) k =
      ZMod.stdAddChar (a * k) * ZMod.dft f k := by
  classical
  rw [ZMod.dft_apply, ZMod.dft_apply, Finset.mul_sum]
  refine Fintype.sum_equiv (Equiv.addLeft a) _ _ ?_
  intro j
  change ZMod.stdAddChar (-(j * k)) * f (a + j) =
    ZMod.stdAddChar (a * k) *
      (ZMod.stdAddChar (-((a + j) * k)) * f (a + j))
  rw [← mul_assoc, ← AddChar.map_add_eq_mul]
  congr 2
  ring

theorem stdAddChar_pow_modulus {L : ℕ} [NeZero L] (k : ZMod L) :
    (ZMod.stdAddChar k)^L = 1 := by
  rw [← AddChar.map_nsmul_eq_pow]
  have hzero : L • k = 0 := by
    rw [nsmul_eq_mul]
    simp
  rw [hzero, AddChar.map_zero_eq_one]

def cellReindex (L : ℕ) (_hL : 0 < L) :
    Fin (8 * L) ≃ Fin L × Fin 8 where
  toFun i :=
    (⟨i.val / 8, by omega⟩,
      ⟨i.val % 8, Nat.mod_lt _ (by omega)⟩)
  invFun p := ⟨8 * p.1.val + p.2.val, by omega⟩
  left_inv i := by
    apply Fin.ext
    change 8 * (i.val / 8) + i.val % 8 = i.val
    omega
  right_inv p := by
    apply Prod.ext <;> apply Fin.ext
    · change (8 * p.1.val + p.2.val) / 8 = p.1.val
      omega
    · change (8 * p.1.val + p.2.val) % 8 = p.2.val
      omega

theorem cell_reindex_forward (L : ℕ) (hL : 0 < L) (i : Fin (8 * L)) :
    (cellReindex L hL i).1.val = i.val / 8 ∧
      (cellReindex L hL i).2.val = i.val % 8 := by
  constructor <;> rfl

theorem cell_reindex_unindex (L : ℕ) (hL : 0 < L)
    (m : Fin L) (r : Fin 8) :
    (cellReindex L hL).symm (m, r) =
      ⟨8 * m.val + r.val, by omega⟩ := by
  rfl

theorem cell_unindex_next_one_interior (L : ℕ) (hL : 0 < L)
    (m : Fin L) (r : Fin 8) (hr : r.val + 1 < 8) :
    cyclicNext ((cellReindex L hL).symm (m, r)) 1 =
      (cellReindex L hL).symm
        (m, ⟨r.val + 1, by omega⟩) := by
  apply Fin.ext
  change (8 * m.val + r.val + 1) % (8 * L) = 8 * m.val + (r.val + 1)
  have hbound : 8 * m.val + r.val + 1 < 8 * L := by
    nlinarith [m.isLt]
  rw [Nat.mod_eq_of_lt hbound]
  omega

theorem cell_unindex_next_two_interior (L : ℕ) (hL : 0 < L)
    (m : Fin L) (r : Fin 8) (hr : r.val + 2 < 8) :
    cyclicNext ((cellReindex L hL).symm (m, r)) 2 =
      (cellReindex L hL).symm
        (m, ⟨r.val + 2, by omega⟩) := by
  apply Fin.ext
  change (8 * m.val + r.val + 2) % (8 * L) = 8 * m.val + (r.val + 2)
  have hbound : 8 * m.val + r.val + 2 < 8 * L := by
    nlinarith [m.isLt]
  rw [Nat.mod_eq_of_lt hbound]
  omega

theorem cell_unindex_next_one_seam (L : ℕ) (hL : 0 < L)
    (m : Fin L) :
    cyclicNext ((cellReindex L hL).symm (m, (7 : Fin 8))) 1 =
      (cellReindex L hL).symm (cyclicNext m 1, (0 : Fin 8)) := by
  apply Fin.ext
  change (8 * m.val + 7 + 1) % (8 * L) =
    8 * ((m.val + 1) % L) + 0
  rw [show 8 * m.val + 7 + 1 = 8 * (m.val + 1) by omega]
  rw [Nat.mul_mod_mul_left]
  omega

theorem cell_unindex_next_two_seam_six (L : ℕ) (hL : 0 < L)
    (m : Fin L) :
    cyclicNext ((cellReindex L hL).symm (m, (6 : Fin 8))) 2 =
      (cellReindex L hL).symm (cyclicNext m 1, (0 : Fin 8)) := by
  apply Fin.ext
  change (8 * m.val + 6 + 2) % (8 * L) =
    8 * ((m.val + 1) % L) + 0
  rw [show 8 * m.val + 6 + 2 = 8 * (m.val + 1) by omega]
  rw [Nat.mul_mod_mul_left]
  omega

theorem cell_unindex_next_two_seam_seven (L : ℕ) (hL : 0 < L)
    (m : Fin L) :
    cyclicNext ((cellReindex L hL).symm (m, (7 : Fin 8))) 2 =
      (cellReindex L hL).symm (cyclicNext m 1, (1 : Fin 8)) := by
  apply Fin.ext
  change (8 * m.val + 7 + 2) % (8 * L) =
    8 * ((m.val + 1) % L) + 1
  rw [show 8 * m.val + 7 + 2 = 8 * (m.val + 1) + 1 by omega]
  rw [Nat.add_mod, Nat.mul_mod_mul_left]
  have hone : 1 % (8 * L) = 1 := Nat.mod_eq_of_lt (by nlinarith)
  rw [hone]
  have hmod : (m.val + 1) % L < L := Nat.mod_lt _ (by omega)
  have hbound : 8 * ((m.val + 1) % L) + 1 < 8 * L := by
    nlinarith
  rw [Nat.mod_eq_of_lt hbound]

noncomputable def cellZModReindex (L : ℕ) (hL : 0 < L) :
    Fin (8 * L) ≃ ZMod L × Fin 8 := by
  haveI : NeZero L := ⟨Nat.ne_of_gt hL⟩
  exact (cellReindex L hL).trans
    (Equiv.prodCongr (ZMod.finEquiv L).toEquiv (Equiv.refl (Fin 8)))

theorem cell_zmod_reindex_residue (L : ℕ) (hL : 0 < L)
    (i : Fin (8 * L)) :
    (cellZModReindex L hL i).2.val = i.val % 8 := by
  rfl

end TargetA
