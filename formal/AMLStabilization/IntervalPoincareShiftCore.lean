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
    dsimp [g, g']
    exact (hf (t + a) hx).comp t ((hasDerivAt_id t).add_const a)
  have hg_cont : ContinuousOn g (Icc 0 h) := by
    exact hf_cont.comp (by fun_prop) hmap
  have hg'_cont : ContinuousOn g' (Icc 0 h) := by
    exact hf'_cont.comp (by fun_prop) hmap
  have hmain := intervalPoincareL2
    (h := h) (f := g) (f' := g') hh hg hg_cont hg'_cont
  dsimp only at hmain
  have hgint :
      (∫ x in (0 : ℝ)..h, g x) = ∫ x in a..b, f x := by
    change (∫ x in (0 : ℝ)..h, f (x + a)) = ∫ x in a..b, f x
    rw [intervalIntegral.integral_comp_add_right]
    simp [h]
  have hdev (c : ℝ) :
      (∫ x in (0 : ℝ)..h, |g x - c| ^ 2) =
        ∫ x in a..b, |f x - c| ^ 2 := by
    change (∫ x in (0 : ℝ)..h, |f (x + a) - c| ^ 2) =
      ∫ x in a..b, |f x - c| ^ 2
    rw [intervalIntegral.integral_comp_add_right]
    simp [h]
  have hderiv :
      (∫ x in (0 : ℝ)..h, |g' x| ^ 2) =
        ∫ x in a..b, |f' x| ^ 2 := by
    change (∫ x in (0 : ℝ)..h, |f' (x + a)| ^ 2) =
      ∫ x in a..b, |f' x| ^ 2
    rw [intervalIntegral.integral_comp_add_right]
    simp [h]
  rw [hgint] at hmain
  rw [hdev, hderiv] at hmain
  simpa [h, fbar] using hmain

end AMLStabilization
