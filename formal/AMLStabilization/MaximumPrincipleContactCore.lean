import Mathlib
import AMLStabilization.InvariantRangeCore

namespace AMLStabilization

/-- Coordinatewise negative semidefiniteness at a spatial upper contact point
implies a nonpositive Laplacian trace. -/
theorem laplacianTrace_nonpos_of_coordinate_nonpos
    {ι : Type*} [Fintype ι] {second : ι → ℝ}
    (hsecond : ∀ i, second i ≤ 0) :
    (∑ i, second i) ≤ 0 := by
  exact Finset.sum_nonpos fun i _ => hsecond i

/-- Coordinatewise positive semidefiniteness at a spatial lower contact point
implies a nonnegative Laplacian trace. -/
theorem laplacianTrace_nonneg_of_coordinate_nonneg
    {ι : Type*} [Fintype ι] {second : ι → ℝ}
    (hsecond : ∀ i, 0 ≤ second i) :
    0 ≤ ∑ i, second i := by
  exact Finset.sum_nonneg fun i _ => hsecond i

/-- At an upper contact point for the signal equation
`z_t = Δz + rho F(z)`, dissipativity makes the time derivative nonpositive. -/
theorem upperContact_timeDerivative_nonpos
    {F : ℝ → ℝ} {zstar beta q s rho lap zt : ℝ}
    (hbeta : 0 < beta) (hrho : 0 ≤ rho) (hlap : lap ≤ 0)
    (hFstar : F zstar = 0) (hs : zstar ≤ s)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q)
    (hPDE : zt = lap + rho * F s) :
    zt ≤ 0 := by
  rw [hPDE]
  exact upper_contact_rhs_nonpos hbeta hrho hlap hFstar hs hdiss

/-- At a lower contact point for the signal equation
`z_t = Δz + rho F(z)`, dissipativity makes the time derivative nonnegative. -/
theorem lowerContact_timeDerivative_nonneg
    {F : ℝ → ℝ} {zstar beta q s rho lap zt : ℝ}
    (hbeta : 0 < beta) (hrho : 0 ≤ rho) (hlap : 0 ≤ lap)
    (hFstar : F zstar = 0) (hs : s ≤ zstar)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q)
    (hPDE : zt = lap + rho * F s) :
    0 ≤ zt := by
  rw [hPDE]
  exact lower_contact_rhs_nonneg hbeta hrho hlap hFstar hs hdiss

/-- Upper contact closure with the Laplacian represented as a coordinate trace. -/
theorem upperContact_from_coordinate_secondDerivatives
    {ι : Type*} [Fintype ι]
    {F : ℝ → ℝ} {zstar beta q s rho zt : ℝ}
    {second : ι → ℝ}
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hsecond : ∀ i, second i ≤ 0)
    (hFstar : F zstar = 0) (hs : zstar ≤ s)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q)
    (hPDE : zt = (∑ i, second i) + rho * F s) :
    zt ≤ 0 := by
  exact upperContact_timeDerivative_nonpos hbeta hrho
    (laplacianTrace_nonpos_of_coordinate_nonpos hsecond)
    hFstar hs hdiss hPDE

/-- Lower contact closure with the Laplacian represented as a coordinate trace. -/
theorem lowerContact_from_coordinate_secondDerivatives
    {ι : Type*} [Fintype ι]
    {F : ℝ → ℝ} {zstar beta q s rho zt : ℝ}
    {second : ι → ℝ}
    (hbeta : 0 < beta) (hrho : 0 ≤ rho)
    (hsecond : ∀ i, 0 ≤ second i)
    (hFstar : F zstar = 0) (hs : s ≤ zstar)
    (hdiss : (s - zstar) * F s ≤ -beta * |s - zstar| ^ q)
    (hPDE : zt = (∑ i, second i) + rho * F s) :
    0 ≤ zt := by
  exact lowerContact_timeDerivative_nonneg hbeta hrho
    (laplacianTrace_nonneg_of_coordinate_nonneg hsecond)
    hFstar hs hdiss hPDE

/-- The two contact inequalities needed in a first-contact proof of invariance
are obtained simultaneously from the dissipativity hypothesis. -/
theorem invariantRange_contact_package
    {ι : Type*} [Fintype ι]
    {F : ℝ → ℝ} {zstar beta q lo hi rhoLo rhoHi ztLo ztHi : ℝ}
    {secondLo secondHi : ι → ℝ}
    (hbeta : 0 < beta) (hFstar : F zstar = 0)
    (hlo : lo ≤ zstar) (hhi : zstar ≤ hi)
    (hrhoLo : 0 ≤ rhoLo) (hrhoHi : 0 ≤ rhoHi)
    (hsecondLo : ∀ i, 0 ≤ secondLo i)
    (hsecondHi : ∀ i, secondHi i ≤ 0)
    (hdiss : ∀ s, (s - zstar) * F s ≤ -beta * |s - zstar| ^ q)
    (hPDELo : ztLo = (∑ i, secondLo i) + rhoLo * F lo)
    (hPDEHi : ztHi = (∑ i, secondHi i) + rhoHi * F hi) :
    0 ≤ ztLo ∧ ztHi ≤ 0 := by
  constructor
  · exact lowerContact_from_coordinate_secondDerivatives hbeta hrhoLo hsecondLo
      hFstar hlo (hdiss lo) hPDELo
  · exact upperContact_from_coordinate_secondDerivatives hbeta hrhoHi hsecondHi
      hFstar hhi (hdiss hi) hPDEHi

end AMLStabilization
