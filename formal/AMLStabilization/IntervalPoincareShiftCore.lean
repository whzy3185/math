import Mathlib
import AMLStabilization.BoxPoincareCore

open Set MeasureTheory Real intervalIntegral

namespace AMLStabilization

/-- Weak `L²` Poincare inequality on an arbitrary nondegenerate interval.
This is the translated form of `intervalPoincareL2`; the explicit constant is
the interval length `b-a`. -/
theorem intervalPoincareL2_Icc
    {a b : ℝ} (hab : a < b) {f f' : ℝ → ℝ}
    (hf : ∀ x ∈ Icc a b, HasDerivAt f (f' x) x)
    (hf_cont : ContinuousOn f (Icc a b))
    (hf'_cont : ContinuousOn f' (Icc a b)) :
    let fbar := (1 / (b - a)) * ∫ x in a..b, f x
    ∫ x in a..b, |f x - fbar| ^ 2 ≤
      (b - a) ^ 2 * ∫ x in a..b, |f' x| ^ 2 := by
  intro fbar
  let h : ℝ := b - a
  let g : ℝ → ℝ := fun t => f (t + a)
  let g' : ℝ → ℝ := fun t => f' (t + a)
  have hh : 0 < h := by
    simpa [h] using sub_pos.mpr hab
  have hmap : MapsTo (fun t : ℝ => t + a) (Icc 0 h) (Icc a b) := by
    intro t ht
    constructor <;> simp [h] at ht ⊢ <;> linarith
  have hg : ∀ t ∈ Icc 0 h, HasDerivAt g (g' t) t := by
    intro t ht
    have hx := hmap ht
    have hlin : HasDerivAt (fun s : ℝ => s + a) 1 t :=
      (hasDerivAt_id t).add_const a
    simpa [g, g'] using (hf (t + a) hx).comp t hlin
  have hg_cont : ContinuousOn g (Icc 0 h) := by
    exact hf_cont.comp (by fun_prop) hmap
  have hg'_cont : ContinuousOn g' (Icc 0 h) := by
    exact hf'_cont.comp (by fun_prop) hmap
  have hmain := intervalPoincareL2
    (h := h) (f := g) (f' := g') hh hg hg_cont hg'_cont
  dsimp only at hmain
  have hend : h + a = b := by
    simp [h]
  simpa [g, g', h, fbar, intervalIntegral.integral_comp_add_right, hend,
    add_comm, add_left_comm, add_assoc] using hmain

end AMLStabilization
