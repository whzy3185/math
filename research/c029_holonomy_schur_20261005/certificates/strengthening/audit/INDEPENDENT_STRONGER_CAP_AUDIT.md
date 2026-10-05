# Independent audit of the sharper one-G6 bound

Date: 2026-10-05. Exact arithmetic and parameterized proof audit: **PASS**.

The complete companion exposition `../UNIFORM_ONE_G6_CAP.md` has also passed final line audit, including the exceptional n=10 base, terminal index, all contraction constants, lower obstruction, and supremum endpoint. The independently computed center, shifted seed LDL pivots, lower-cap LDL prefix, and exact tail majorant match the primary certificate exactly.

This is a separate strengthening of the frozen residue-two result. The earlier delivery files have not been changed by this audit.

## Conclusions

For the explicit signing on n=8k+2 whose step-one signs are positive and whose step-two sequence is k copies of (+,+,-,+,-,-,+,-), followed by (+,-), the audited argument gives

    rho(A_n)^2 < 790537/100000 = 7.90537  for every k>=1.

At n=202, an independently verified strictly negative Schur pivot at the lower threshold gives

    rho(A_202)^2 > 7905369/1000000 = 7.905369.

Consequently the supremum of the squared spectral radii of this explicit family lies in

    (7.905369, 7.90537].

The interval has width 10^-6. Its upper endpoint must remain closed: strict bounds for every individual finite member do not imply a strict bound for their supremum. No global optimization over all signings is claimed.

## Parameters and finite premises

Use the same normalized block structure, E matrices, and rational P/Q weights as the earlier residue-two proof, replacing the diagonal entry 98/25 by c-4, where c=790537/100000. The retained core has dimension six. Let

    J=48, r=10^-18, eta=10^-20,
    q=3/4, theta=q^2=9/16,
    a=1/9000000000, b=12a=1/750000000,
    seed order n0=202, block count ell0=50.

The independently reproduced finite premises are:

- All 192 scalar graph pivots preceding the entrance are positive
- X_J and its next Riccati image exceed I_4/2
- (9/10)I_4 < P,Q < 2I_4
- L^T P L < P/2 and L Q L^T < Q/2 at the entrance
- The two-cell center residual has Frobenius norm below r/40
- R_J Q R_J^T < eta I_2 and W_J^T Q W_J < eta I_4
- The normalized six-dimensional seed at n=202 exceeds 10^-6 I_6
- The 24 finite graphs n=10,18,...,194 have positive cI-A_n^2

The independent implementation constructs the full original graph and performs scalar Schur elimination. It does not generate the entrance using the four-site Riccati recurrence. At n=202, after 192 scalar eliminations, it reads X_J and R_J from the remaining ten-dimensional matrix and subtracts the physical E_+ coupling from its current-to-terminal block to obtain W_J. All comparisons use exact rational arithmetic.

The n=10 base is handled directly as a full graph. It needs no claim that the nonadjacent first-to-last wrap block is disjoint from the physical nearest-block coupling. For n>=18 the usual block template has no such overlap.

## Local analytic audit

On the radius-r ball in the P order-unit norm, the Euclidean center perturbation is at most e=2r. The same inverse bootstrap as in the earlier proof gives

    ||X^-1||, ||F_+(X)^-1|| <= 3,
    ||X^-1-X_J^-1|| <= 6e,
    ||F_+(X)-F_+(X_J)|| <= 84e,
    ||F_+(X)^-1-F_+(X_J)^-1|| <= 504e.

Since both E matrices have squared Frobenius norm 14, the two-cell transfer perturbation has Euclidean norm at most 14364e. Conversion to either weighted transfer norm costs less than 3/2. Therefore its weighted norm is less than

    43092r < 10^-4.

The exact rational comparison

    (3/4-10^-4)^2 > 1/2

proves uniform response contraction by q=3/4 and uniform positive-map Riccati contraction by theta=9/16. The center residual has order-unit norm below r/36, and

    1/36 + 9/16 = 85/144 < 1.

Thus the ball is invariant and the fixed point X_* exists. Conservatively,

    ||X_(J+2h)-X_*|| <= 4r theta^h.

Both even and intermediate odd pivots remain positive, with inverse norm at most three. Together with the finite entrance this covers every required pivot.

## Response conversion and complete Schur tail

The exact inequality

    a^2 > (10/9)eta

converts the entrance bounds into ordinary spectral-norm bounds a q^h at even indices J+2h. The one-step bound 3sqrt(14)<12 gives b q^h for both members of each pair.

For even block count ell>=50, the terminal index is

    p=ell-2=J+2h.

It has E_+ parity. Define the limiting core by summing the actual infinite trajectory, retaining the pure terminal form E_+^T X_*^-1 E_+. Each of the three Schur-series suffixes is bounded by

    T_h = 6b^2 q^(2h)/(1-q^2).

This counts both increments in every pair. The terminal C correction is bounded by 12a q^h, both terminal H cross terms together by 24a q^h, and the pure inverse-limit correction by 576r theta^h. Therefore the full six-dimensional core satisfies

    ||S_ell-S_inf|| <= B_h
                    := 4T_h + 48a q^h + 576r theta^h
                    <= B_0
                    = 583333407/109375000000000000
                    < 10^-8.

All displayed comparisons have been checked exactly. There is no omitted pivot-inverse error in the Schur series: the limiting sums use the actual pivot trajectory, so common initial terms cancel.

Two tail errors are needed to transfer the finite seed. Hence, for every even ell>=50,

    ||S_ell-S_50|| < 2*10^-8,
    S_ell > (10^-6-2*10^-8)I_6 = (49/50000000)I_6.

Together with positive pivots and the 24 direct finite bases, this proves cI-A_n^2>0 for every k>=1. The core margin is not asserted as an eigenvalue lower bound for the original matrix; only positivity transfers under Schur congruence.

## Independent lower obstruction

At c_low=7905369/1000000 and n=202, direct full-graph elimination produces 196 positive scalar interior pivots. The remaining core has a scalar LDL prefix with positive predecessors and a strictly negative next pivot. Exact rational values are stored in the replay certificate.

By Schur congruence, the full matrix c_low I-A_202^2 has a negative direction. Therefore its least eigenvalue is strictly negative and rho(A_202)^2>c_low. A failed positive-definiteness test alone would not justify this strict conclusion; the stored strictly negative pivot and positive predecessors do.

## Reproduction

Run `python replay_stronger_cap.py` with Python 3 and SymPy. It writes `stronger_cap_independent_replay.json`; `verification_stdout.json` records the fresh execution output. The code constructs the signed graph independently and imports no historical or primary-verifier modules. This is exact-arithmetic-assisted mathematical audit, not proof-assistant formalization.
