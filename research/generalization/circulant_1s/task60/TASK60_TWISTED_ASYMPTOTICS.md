# Task 60 Twisted Asymptotics

Throughout this note, `s` is fixed and `N` tends to infinity through even
orders with `2s<N`.

## Even `s`

The optimized holonomy is `alpha=-1`. Since the continuous maxima at
`theta=0 (mod pi)` are isolated, the maximizing antiperiodic grid point is
`theta=pi/N` for all sufficiently large `N`. Taylor expansion gives

```text
rho_tw(N,s)^2
 = 8
   - 4pi^2(1+s^2)/N^2
   + 4pi^4(1+s^4)/(3N^4)
   + O_s(N^(-6)).
```

The threshold limit is therefore `8`, as for `s=2`, but both correction
coefficients depend on `s`.

## Odd `s`

Both holonomy sectors converge to the interior threshold `M_s<8`. Let
`Theta_s` be the set of continuous maximizers modulo `pi`, and let
`delta_(N,alpha)` be the distance from the `alpha` Fourier grid to this set.
The maximum is nondegenerate, with

```text
kappa_s=4(cos x_s-s^2 cos(s x_s))>0.
```

For sufficiently large `N`,

```text
rho_tw(N,s,alpha)^2
 = M_s-kappa_s delta_(N,alpha)^2
   + O_s(delta_(N,alpha)^3).
```

Since `delta_(N,alpha)=O(1/N)`, each sector is `M_s+O_s(N^-2)`. Unlike the
even case, the coefficient is not a fixed function of `s`: it depends on the
arithmetic position of the interior maximizer relative to the two Fourier
grids. The optimized holonomy can therefore change with `N`.

## Proven dichotomy

| Chord parity | Continuous maximum | Best finite holonomy | Leading behavior |
|---|---|---|---|
| even | endpoint, value `8` | always antiperiodic | fixed `N^-2` coefficient eventually |
| odd | interior, value `M_s<8` | arithmetic-dependent | grid-distance correction |

This parity dichotomy is the first obstruction to a literal extension of the
Task 59 spectral story.
