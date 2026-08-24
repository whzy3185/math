# Exact Classification from Order 34 through Order 46

## Setting

For even $n$, let $A$ be the signed adjacency matrix of a signing of
$C_n(1,2)$ and put

$$
\theta_n=\rho_-(n)^2
=4+2\cos\frac{2\pi}{n}+2\cos\frac{4\pi}{n}.
$$

A signing is a counterexample precisely when $\rho(A)^2<\theta_n$.

## Interval theorem

**Theorem.**

1. If $n\in\{34,36,38,42,44,46\}$, then every signing satisfies
   $\rho(A)^2\ge\theta_n$.  Hence no counterexample exists at these six
   orders.
2. At $n=40$, the normal-form data

   $$
   Q=1000100010001000100010001000100010001000,\qquad
   \alpha=-1
   $$

   define a signing $A_{40}$ such that

   $$
   \rho(A_{40})^2<\frac{15541}{2000}
   <\frac{63}{8}<\theta_{40}.
   $$

Thus the truth value is completely classified at every even order from 34
through 46.

## Finite-state theorem behind part 1

For each no-counterexample order there is a support
$L_n\in\{12,13,14\}$ and a finite set of surviving $Q$-windows of length
$L_n+1$ such that:

1. every excluded window has an exact local Rayleigh certificate forcing
   $\rho(A)^2>\theta_n$;
2. every signing without an excluded window gives a closed walk in a
   parity-lifted de Bruijn graph;
3. every such closed walk reconstructs a globally legal cyclic $Q$-word;
4. after dihedral reduction, both holonomies of every canonical word have an
   exact global certificate forcing $\rho(A)^2\ge\theta_n$.

The independent reconstruction has no unresolved local window and records
terminal_unresolved=0.

## Correct terminal total

The per-order terminal counts are

$$
2,\ 2,\ 6,\ 14,\ 20,\ 20,
$$

and therefore total

$$
2+2+6+14+20+20=64.                                    \tag{1}
$$

A historical verifier handoff wrote 84.  That is an arithmetic error: the
certificate contains 64 records and the checker requires exactly 64.  The
order-40 artifact is one separate LDL counterexample record; it does not
contain twenty omitted terminal $(Q,\alpha)$ records.

Evidence status: COMPUTER_ASSISTED_PROVED.
