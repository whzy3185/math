# Quantitative follow-up questions

Date: 2026-09-05. Recorded after the first all-even proof and its preliminary
analytic examination, before the new large-jump numerical tests.

This is not a retrospective alteration of `CONJECTURES_BEFORE_TESTS.md`.
The earlier C1--C4 record remains unchanged. For the same explicit family,
write `g_s=8-R_s`.

* Q5 (analytic candidate): `g_s >= 1/(2s^3)` for all even `s>=2`.
  The proposed method is `lambda_min(C)>=1/tr(C^-1)`, the threshold
  determinant derivative, and coefficientwise estimates for its positive
  generating function. Preliminary work already suggests this bound.
* Q6 (sharp asymptotic conjecture): `s^2 g_s -> pi^2` through even jumps.
  This is suggested by the small-jump exploratory values, not established
  by the first-round proof. Endpoint boundary conditions require analysis.
* Q7 (phase-location conjecture): `R_s=rho(H_s(1))^2` for every even `s`.
  A denser phase sample does not prove this assertion. Flat large-jump
  dispersion also makes floating-point phase comparisons unreliable.

For this round, attempt Q5 analytically and obtain an analytic complementary
upper bound on `g_s`. Use bounded sampling only to inform Q6/Q7; record
unresolved status if their proof does not close. Do not change the frozen
paper or silently insert these conjectures as theorems.
