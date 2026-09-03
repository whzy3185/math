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
