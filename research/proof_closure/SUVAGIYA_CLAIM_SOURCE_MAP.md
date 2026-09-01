# Suvagiya Claim Source Map

Authoritative source inspected: Vaibhav Suvagiya, *Signed circulants at the
Ramanujan bound*, arXiv:2607.18334v1 (19 July 2026), local legal copy
`research/related_work/papers/core/2026_Suvagiya_SignedCirculants_PREPRINT.pdf`.

| Item | Exact source location | Verified statement |
|---|---|---|
| graph family | p. 1, Setup | `C_n(1,2)` has vertices `Z_n` and step-one/step-two edges; the main setup assumes even `n>=10`, with `n=8` treated separately in Remark 4. |
| signing setup | p. 1, Setup | a signing is `sigma:E -> {+1,-1}`; switching preserves the signed-adjacency spectrum. |
| switching/flux setup | p. 1, Setup; p. 2, Proposition 2 | switching classes are encoded by cycle signs; triangle signs `tau_i` and step-one Hamilton-cycle holonomy `alpha` form a cycle-space coordinate system. |
| quadrilateral system | p. 1 equation (1); p. 2 Proposition 1 | every displayed quadrilateral is unbalanced; for even `n>=10` this has exactly four switching classes. |
| twisted signing | p. 2--3, Proposition 2 | the two `alpha=-1` classes with alternating triangle flux `tau_{i+1}=-tau_i`; rotation exchanges the two choices of `tau_0`. |
| explicit spectrum | p. 2, Proposition 1; p. 2--3, Proposition 2 | the `alpha=+1` representative has spectrum `+-2 sqrt(cos^2 theta_k+cos^2 2theta_k)` and radius `2 sqrt(2)`; the twisted `alpha=-1` classes have radius `rho_-(n)=2 sqrt(cos^2(pi/n)+cos^2(2pi/n))`. |
| maximum step in formula | p. 3, Proposition 2 proof | shifted momenta are `(2k+1)pi/n`; the maximum is attained at `pi/n` for even `n>=8`. |
| exhaustive checks | p. 1 abstract; p. 3, Conjecture 3 | exhaustive enumeration is asserted only for `n in {8,10,12,14,16,18}`, over all `2^(n+1)` switching classes, with reported numerical agreement to `10^-9`. |
| exact conjecture | p. 3, Conjecture 3 | for every even `n>=8`, `min_sigma rho(A_sigma)=rho_-(n)`; the `alpha=-1` twisted class is globally optimal. |
| exceptional order eight | p. 3, Remark 4 | the all-quadrilateral interpretation differs at `n=8`, but the two twisted classes still attain the stated `rho_-(8)` and Conjecture 3 is unchanged. |
| explicitly proved there | pp. 2--3, Propositions 1--2 | consistency/four-class result, flux coordinates, spectra of the special classes, and the upper bound `m_n<=rho_-(n)`; no global lower bound beyond the listed finite enumeration. |

## Consequences for this project

1. The current work studies exactly the same fixed family and the same
   twisted benchmark.
2. It supports Suvagiya's conjecture at
   `8,10,12,14,16,18,20,22,24,26,28,30,34,36,38,42,44,46`.
3. It disproves the conjecture at `32`, `40`, and every even `n>=48` by
   explicit certified witnesses.
4. The genuinely new theorem is therefore a complete truth-value
   classification of Suvagiya's Conjecture 3, not a theorem determining all
   minimizers or the exact value of `m_n` at every failing order.

Where an old project note conflicts with the table above, the original PDF
wins.  In particular, neither a purported all-even proof nor any finite-order
claim from the preprint is inferred from its floating-point enumeration.
