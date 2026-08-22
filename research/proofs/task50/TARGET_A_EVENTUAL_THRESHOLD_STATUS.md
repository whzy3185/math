# Target A Eventual Threshold Status

The elementary threshold estimate is rigorous:

\[
T_n=4\left(\cos^2\frac\pi n+\cos^2\frac{2\pi}n\right)
\ge 8-\frac{20\pi^2}{n^2}
>8-\frac{200}{n^2}.
\]

Indeed `sin x<=x` gives `cos^2 x=1-sin^2x>=1-x^2`, and
`pi^2<10` gives the final strict inequality.

The exact interface theorem provides rational positive gaps

\[
8-c_6>8-\frac{7905369311620328}{10^{15}}>0,
\]

\[
8-c_{10}>8-\frac{7977104370400547}{10^{15}}>0.
\]

If the single-tail and two-tail finite-ring bounds were available, these
gaps and the threshold inequality would yield explicit values of
`N_2,N_6,N_4,N_12`.  Gate 4 and Gate 5 are incomplete, so those values cannot
currently be defined rigorously.

| Residue | Required input | Status |
|---|---|---|
| 0 mod 8 | Existing period-eight theorem | proved |
| 2 mod 8 | G6 finite-ring spectral-radius bound | incomplete |
| 6 mod 8 | G10 finite-ring spectral-radius bound | incomplete |
| 4 mod 16 | symmetric two-G6 bound | incomplete |
| 12 mod 16 | shifted two-G6 bound | incomplete |

Gate decision: `ALL_EVEN_THEOREM_INCOMPLETE`.

No global `N` is asserted.
