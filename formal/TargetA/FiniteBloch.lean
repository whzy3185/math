import Mathlib
import TargetA.HamiltonGauge

namespace TargetA

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

end TargetA
