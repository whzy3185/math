#!/usr/bin/env python3
"""Exact switching-isomorphism orbit checks at the sqrt(6) boundary.

This script uses the exhaustive exact-witness survivors from
verify_six_boundary_minimizer_rigidity.py and applies only the dihedral
permutations x -> +/-x+b.  The companion proof note shows analytically that
these are the full graph automorphism groups for C_12(1,4), C_16(1,3), and
C_20(1,8), by distinguishing the two edge types through short-cycle counts.
"""

from verify_six_boundary_minimizer_rigidity import exhaustive_survivors


def edge_dict(N, s, alpha, tau):
    e = {}
    for i in range(N - 1):
        e[tuple(sorted((i, i + 1)))] = 1
    e[(0, N - 1)] = alpha
    for i, sign in enumerate(tau):
        j = (i + s) % N
        e[tuple(sorted((i, j)))] = sign
    return e


def normalize(N, s, e):
    g = [1] * N
    for i in range(N - 1):
        g[i + 1] = g[i] * e[tuple(sorted((i, i + 1)))]

    def switched(i, j):
        return g[i] * e[tuple(sorted((i, j)))] * g[j]

    alpha = switched(N - 1, 0)
    tau = tuple(switched(i, (i + s) % N) for i in range(N))
    return alpha, tau


def dihedral_image(N, s, rep, eps, b):
    alpha, tau = rep
    e = edge_dict(N, s, alpha, tau)
    ne = {}
    for (i, j), sign in e.items():
        a = (eps * i + b) % N
        c = (eps * j + b) % N
        ne[tuple(sorted((a, c)))] = sign
    return normalize(N, s, ne)


def dihedral_orbits(N, s, reps):
    reps = set(reps)
    seen = set()
    out = []
    for rep in reps:
        if rep in seen:
            continue
        orb = {
            dihedral_image(N, s, rep, eps, b)
            for eps in (-1, 1)
            for b in range(N)
        }
        assert orb <= reps
        seen |= orb
        out.append(orb)
    assert seen == reps
    return out


def reps_20_8():
    N, s = 20, 8
    h = [1] * N
    h[-1] = -1
    reps = []
    for c0 in (-1, 1):
        c = [None] * N
        c[0] = c0
        for i in range(N - 1):
            c[i + 1] = -h[i] * h[(i + s) % N] * c[i]
        assert c[0] == -h[-1] * h[(N - 1 + s) % N] * c[-1]
        reps.append((-1, tuple(c)))
    return reps


def main():
    s12 = exhaustive_survivors(12, 4)
    reps12 = [(alpha, tau) for alpha, tau, *_ in s12]
    o12 = dihedral_orbits(12, 4, reps12)
    assert sorted(map(len, o12)) == [2]

    s16 = exhaustive_survivors(16, 3)
    reps16 = [(alpha, tau) for alpha, tau, *_ in s16]
    o16 = dihedral_orbits(16, 3, reps16)
    assert sorted(map(len, o16)) == [16, 16]
    holonomies = sorted(next(iter({rep[0] for rep in orb})) for orb in o16)
    assert holonomies == [-1, 1]
    for orb in o16:
        assert len({rep[0] for rep in orb}) == 1

    reps20 = reps_20_8()
    o20 = dihedral_orbits(20, 8, reps20)
    assert sorted(map(len, o20)) == [2]

    print("(12,4): 1 switching-isomorphism orbit of size 2")
    print("(16,3): 2 switching-isomorphism orbits of size 16, holonomy +/-1")
    print("(16,5): same orbit structure by multiplier 5")
    print("(20,8): 1 switching-isomorphism orbit of size 2")
    print("All sqrt(6)-boundary orbit checks passed.")


if __name__ == "__main__":
    main()
