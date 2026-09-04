# Draft text for Sections 6--7

## 6. Why period eight is distinguished

The counterexample family is not introduced as an isolated word search. Its
local mechanism is visible after squaring the Hamilton-gauge operator. Put
Q_i=tau_i tau_(i+1). The odd-displacement coefficients of A_tau^2 contain the
factor 1+Q_i. Hence a negative Q_i cancels the corresponding odd coupling,
whereas a positive Q_i activates it with amplitude of absolute value two.
This identity converts the geometry of the flux word into a constraint on the
squared Bloch spectrum.

For period eight, the resulting moment barrier separates the legal phases
into three classes. The displayed antipodal two-defect word has squared edge

    eta = 4 + sqrt(10 + 2 sqrt(5)) < 8.

The balanced phase has edge exactly eight. Every other legal period-eight
phase has edge greater than eight. Thus, up to the stated symmetries of the
eight-periodic problem, the antipodal two-defect phase is the unique
sub-eight phase.

Only three non-antipodal two-defect configurations are not eliminated by the
short symbolic moment comparison. They are handled by the following finite
integer recurrence, included here because it is part of the trichotomy rather
than an external search. For a fixed starting residue r, let f_l^(r)(j) be the
signed walk sum of length l from r to j. Then

    f_(l+1)^(r)(j) = f_l^(r)(j-1)+f_l^(r)(j+1)
                     + tau_(j-2) f_l^(r)(j-2)+tau_j f_l^(r)(j+2).

If M_k is the normalized even trace moment and E_k=M_(k+1)-8M_k, the first
positive excesses for defect separations 1, 2, and 3 are respectively

    E_4 = 5504,    E_6 = 64336,    E_9 = 2872096.

These are exact integer outputs of the displayed recurrence. A positive
excess contradicts a squared edge at most eight, since that assumption would
give M_(k+1) at most 8 M_k. This finishes the three remaining cases without
using floating-point spectra or enumeration over signings.

## 7. General periodic defect obstruction

The same squared local identity has a period-independent consequence. Let
tau have period p and put d=#{i:Q_i=1}. Let a and b count positive Q-pairs at
cyclic distances one and two. For the phase-averaged even Floquet moments,

    M_1 = 4p,
    M_2 = 20p + 16d,
    M_3 = 118p + 168d + 96a + 48b.

The first identity is the diagonal of A_tau^2. The second follows by squaring
the local row of A_tau^2. The third is obtained by the finite symbolic
closed-walk expansion of the same local identity and grouping the surviving
monomials by translation. No finite-size spectral computation is involved.

If the squared Bloch edge is at most eight, pointwise comparison of successive
even powers gives M_(k+1) at most 8 M_k. Applying this for k=1 and k=2 gives

    d <= 3p/4,
    40d + 96a + 48b <= 42p.

These inequalities are necessary conditions only. They explain why defect
density and short-range clustering matter, but they do not classify arbitrary
periodic phases or all signings of C_n(1,2).
