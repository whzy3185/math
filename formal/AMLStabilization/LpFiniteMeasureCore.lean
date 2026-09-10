import Mathlib

open MeasureTheory

namespace AMLStabilization

/-- On a finite measure space, real-exponent `L^p` membership with `p >= 2`
implies `L^2` membership. -/
theorem memLp_two_of_memLp_ofReal
    {Omega E : Type*} [MeasurableSpace Omega]
    [NormedAddCommGroup E]
    {mu : Measure Omega} [IsFiniteMeasure mu]
    {f : Omega → E} {p : ℝ}
    (hp : 2 ≤ p)
    (hfp : MemLp f (ENNReal.ofReal p) mu) :
    MemLp f 2 mu := by
  have hpq : (2 : ℝ≥0∞) ≤ ENNReal.ofReal p := by
    simpa using ENNReal.ofReal_le_ofReal hp
  exact hfp.mono_exponent hpq

/-- Explicit finite-volume seminorm transfer from `L^p` to `L^2`. -/
theorem eLpNorm_two_le_eLpNorm_ofReal_mul_volume
    {Omega E : Type*} [MeasurableSpace Omega]
    [NormedAddCommGroup E]
    {mu : Measure Omega}
    {f : Omega → E} {p : ℝ}
    (hp : 2 ≤ p)
    (hf : AEStronglyMeasurable f mu) :
    eLpNorm f 2 mu ≤
      eLpNorm f (ENNReal.ofReal p) mu *
        mu Set.univ ^ (1 / (2 : ℝ) - 1 / p) := by
  have hp0 : 0 ≤ p := le_trans (by norm_num) hp
  have hpq : (2 : ℝ≥0∞) ≤ ENNReal.ofReal p := by
    simpa using ENNReal.ofReal_le_ofReal hp
  have h := eLpNorm_le_eLpNorm_mul_rpow_measure_univ hpq hf
  simpa [ENNReal.toReal_ofReal hp0] using h

/-- If the `L^p` seminorm is bounded by `U`, the same finite-volume factor
gives an explicit `L^2` seminorm bound. -/
theorem eLpNorm_two_le_of_eventual_p_bound
    {Omega E : Type*} [MeasurableSpace Omega]
    [NormedAddCommGroup E]
    {mu : Measure Omega}
    {f : Omega → E} {p : ℝ} {U : ℝ≥0∞}
    (hp : 2 ≤ p)
    (hf : AEStronglyMeasurable f mu)
    (hU : eLpNorm f (ENNReal.ofReal p) mu ≤ U) :
    eLpNorm f 2 mu ≤
      U * mu Set.univ ^ (1 / (2 : ℝ) - 1 / p) := by
  calc
    eLpNorm f 2 mu ≤
        eLpNorm f (ENNReal.ofReal p) mu *
          mu Set.univ ^ (1 / (2 : ℝ) - 1 / p) :=
      eLpNorm_two_le_eLpNorm_ofReal_mul_volume hp hf
    _ ≤ U * mu Set.univ ^ (1 / (2 : ℝ) - 1 / p) := by
      gcongr

end AMLStabilization
