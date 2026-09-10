import Mathlib
import AMLStabilization.LpExponentCore

open MeasureTheory

namespace AMLStabilization

/-- A real Hölder triple from the reciprocal-exponent identity used in the paper. -/
theorem realHolderTriple_of_reciprocal_identity
    {p s r : ℝ}
    (hp : 0 < p) (hs : 0 < s)
    (hrel : 1 / r = 1 / p + 1 / s) :
    Real.HolderTriple p s r := by
  refine ⟨?_, hp, hs⟩
  simpa [one_div] using hrel.symm

/-- Transfer a positive real Hölder triple to the `ENNReal` exponent system used by `MemLp`. -/
theorem ennrealHolderTriple_of_real
    {p s r : ℝ}
    (hp : 0 < p) (hs : 0 < s) (hr : 0 < r)
    (hrel : 1 / r = 1 / p + 1 / s) :
    ENNReal.HolderTriple (ENNReal.ofReal p) (ENNReal.ofReal s) (ENNReal.ofReal r) := by
  have hreal := realHolderTriple_of_reciprocal_identity hp hs hrel
  apply ENNReal.HolderTriple.of_toReal
  simpa [ENNReal.toReal_ofReal hp.le, ENNReal.toReal_ofReal hs.le,
    ENNReal.toReal_ofReal hr.le] using hreal

/-- Actual `L^p × L^s -> L^r` membership transfer for real exponents. -/
theorem memLp_mul_of_reciprocal_identity
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {f g : Omega → ℝ}
    {p s r : ℝ}
    (hp : 0 < p) (hs : 0 < s) (hr : 0 < r)
    (hrel : 1 / r = 1 / p + 1 / s)
    (hf : MemLp f (ENNReal.ofReal p) mu)
    (hg : MemLp g (ENNReal.ofReal s) mu) :
    MemLp (fun x => f x * g x) (ENNReal.ofReal r) mu := by
  letI : ENNReal.HolderTriple (ENNReal.ofReal p) (ENNReal.ofReal s) (ENNReal.ofReal r) :=
    ennrealHolderTriple_of_real hp hs hr hrel
  have h : MemLp (f * g) (ENNReal.ofReal r) mu :=
    hg.mul (r := ENNReal.ofReal r) hf
  simpa [Pi.mul_apply] using h

/-- The canonical exponents therefore give the product membership needed before smoothing. -/
theorem lpChoice_product_memLp
    {Omega : Type*} [MeasurableSpace Omega]
    {mu : Measure Omega} {f g : Omega → ℝ}
    {n p : ℝ}
    (hp : max n 2 < p)
    (hf : MemLp f (ENNReal.ofReal p) mu)
    (hg : MemLp g (ENNReal.ofReal (holderPartner p (lpChoice n p))) mu) :
    MemLp (fun x => f x * g x) (ENNReal.ofReal (lpChoice n p)) mu := by
  obtain ⟨hrn, hrp, hs2, hrel⟩ := lpChoice_exponent_package hp
  have hp0 : 0 < p := lt_trans (by norm_num) (lt_of_le_of_lt (le_max_right n 2) hp)
  have hr0 : 0 < lpChoice n p := by
    have hthreshold := two_mul_p_div_p_add_two_lt_lpChoice hp
    have h2p : 0 < 2 * p / (p + 2) := by positivity
    linarith
  have hs0 : 0 < holderPartner p (lpChoice n p) := lt_trans (by norm_num) hs2
  exact memLp_mul_of_reciprocal_identity hp0 hs0 hr0 hrel hf hg

end AMLStabilization
