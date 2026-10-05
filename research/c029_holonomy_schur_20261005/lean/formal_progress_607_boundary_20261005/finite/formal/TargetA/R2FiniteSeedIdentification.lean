import TargetA.R2TerminalIdentificationCertificate
namespace TargetA
open scoped Matrix
set_option maxHeartbeats 300000

/-- Explicit finite witness; only indices through 24 are certified or used. -/
def r2CertifiedStates : ℕ → R2RecurrenceState ℚ
  | 0 => r2StepState0
  | 1 => r2StepState1
  | 2 => r2StepState2
  | 3 => r2StepState3
  | 4 => r2StepState4
  | 5 => r2StepState5
  | 6 => r2StepState6
  | 7 => r2StepState7
  | 8 => r2StepState8
  | 9 => r2StepState9
  | 10 => r2StepState10
  | 11 => r2StepState11
  | 12 => r2StepState12
  | 13 => r2StepState13
  | 14 => r2StepState14
  | 15 => r2StepState15
  | 16 => r2StepState16
  | 17 => r2StepState17
  | 18 => r2StepState18
  | 19 => r2StepState19
  | 20 => r2StepState20
  | 21 => r2StepState21
  | 22 => r2StepState22
  | 23 => r2StepState23
  | _ => r2StepState24

def r2CertifiedInverses : ℕ → Matrix (Fin 4) (Fin 4) ℚ
  | 0 => r2FirstInverseQ
  | 1 => r2SecondInverseQ
  | 2 => r2ThirdInverseQ
  | 3 => r2FourthInverseQ
  | 4 => r2FifthInverseQ
  | 5 => r2SixthInverseQ
  | 6 => r2SeventhInverseQ
  | 7 => r2EighthInverseQ
  | 8 => r2NinthInverseQ
  | 9 => r2TenthInverseQ
  | 10 => r2EleventhInverseQ
  | 11 => r2TwelfthInverseQ
  | 12 => r2ThirteenthInverseQ
  | 13 => r2FourteenthInverseQ
  | 14 => r2FifteenthInverseQ
  | 15 => r2SixteenthInverseQ
  | 16 => r2SeventeenthInverseQ
  | 17 => r2EighteenthInverseQ
  | 18 => r2NineteenthInverseQ
  | 19 => r2TwentiethInverseQ
  | 20 => r2TwentyFirstInverseQ
  | 21 => r2TwentySecondInverseQ
  | 22 => r2TwentyThirdInverseQ
  | 23 => r2TwentyFourthInverseQ
  | _ => r2FinalInverseQ

theorem r2_finite_certificate_initial : r2CertifiedStates 0 = r2InitialState ℚ :=
  r2_first_recorded_initial

theorem r2_finite_certificate_inverses :
    ∀ j, j ≤ 24 → (r2CertifiedStates j).X * r2CertifiedInverses j = 1 := by
  intro j hj
  interval_cases j
  · change r2StepState0.X * r2FirstInverseQ = 1
    rw [r2_first_recorded_initial]
    exact r2_first_inverse_product
  · exact r2_second_inverse_product
  · exact r2_third_inverse_product
  · exact r2_fourth_inverse_product
  · exact r2_fifth_inverse_product
  · exact r2_sixth_inverse_product
  · exact r2_seventh_inverse_product
  · exact r2_eighth_inverse_product
  · exact r2_ninth_inverse_product
  · exact r2_tenth_inverse_product
  · exact r2_eleventh_inverse_product
  · exact r2_twelfth_inverse_product
  · exact r2_thirteenth_inverse_product
  · exact r2_fourteenth_inverse_product
  · exact r2_fifteenth_inverse_product
  · exact r2_sixteenth_inverse_product
  · exact r2_seventeenth_inverse_product
  · exact r2_eighteenth_inverse_product
  · exact r2_nineteenth_inverse_product
  · exact r2_twentieth_inverse_product
  · exact r2_twentyfirst_inverse_product
  · exact r2_twentysecond_inverse_product
  · exact r2_twentythird_inverse_product
  · exact r2_twentyfourth_inverse_product
  · exact r2_final_inverse_product

theorem r2_finite_certificate_transitions :
    ∀ j, j < 24 → r2CertifiedStates (j+1) =
      r2UpdateWithInverse ℚ j (r2CertifiedStates j) (r2CertifiedInverses j) := by
  intro j hj
  interval_cases j
  · exact r2_first_recorded_transition
  · exact r2_second_recorded_transition
  · exact r2_third_recorded_transition
  · exact r2_fourth_recorded_transition
  · exact r2_fifth_recorded_transition
  · exact r2_sixth_recorded_transition
  · exact r2_seventh_recorded_transition
  · exact r2_eighth_recorded_transition
  · exact r2_ninth_recorded_transition
  · exact r2_tenth_recorded_transition
  · exact r2_eleventh_recorded_transition
  · exact r2_twelfth_recorded_transition
  · exact r2_thirteenth_recorded_transition
  · exact r2_fourteenth_recorded_transition
  · exact r2_fifteenth_recorded_transition
  · exact r2_sixteenth_recorded_transition
  · exact r2_seventeenth_recorded_transition
  · exact r2_eighteenth_recorded_transition
  · exact r2_nineteenth_recorded_transition
  · exact r2_twentieth_recorded_transition
  · exact r2_twentyfirst_recorded_transition
  · exact r2_twentysecond_recorded_transition
  · exact r2_twentythird_recorded_transition
  · exact r2_twentyfourth_recorded_transition

theorem r2_finite_certificate_terminal :
    r2CoreWithInverse ℚ (r2CertifiedStates 24) (r2CertifiedInverses 24) = r2Seed106CoreQ :=
  r2_final_terminal_recorded

theorem r2_core26_eq_seed_rat : r2Core26 ℚ = r2Seed106CoreQ := by
  rw [r2_core26_eq_of_certificates r2CertifiedStates r2CertifiedInverses
    r2_finite_certificate_initial r2_finite_certificate_inverses r2_finite_certificate_transitions]
  exact r2_finite_certificate_terminal

theorem r2_core26_eq_seed_real : r2Core26 ℝ = r2Seed106Core := by
  rw [r2_real_core26_eq_of_certificates r2CertifiedStates r2CertifiedInverses
    r2_finite_certificate_initial r2_finite_certificate_inverses r2_finite_certificate_transitions,
    r2_finite_certificate_terminal]
  rfl

theorem r2_core26_margin_posDef :
    (r2Core26 ℝ - (1/50 : ℝ) • (1 : Matrix (Fin 6) (Fin 6) ℝ)).PosDef := by
  exact r2_core26_margin_of_rational_seed_certificate r2CertifiedStates r2CertifiedInverses
    r2_finite_certificate_initial r2_finite_certificate_inverses
    r2_finite_certificate_transitions r2_finite_certificate_terminal

#print axioms r2_finite_certificate_initial
#print axioms r2_finite_certificate_inverses
#print axioms r2_finite_certificate_transitions
#print axioms r2_finite_certificate_terminal
#print axioms r2_core26_eq_seed_rat
#print axioms r2_core26_eq_seed_real
#print axioms r2_core26_margin_posDef
end TargetA
