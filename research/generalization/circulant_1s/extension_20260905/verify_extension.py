#!/usr/bin/env python3
"""Finite exact audit of the analytic 1s extension (not an all-s proof).

Run: uv run --with sympy --with numpy python <this-file>
The source-of-truth fiber is assembled directly from its four displacements.
The continuant expression, reduced chain, generating function and finite
flat-signing enumeration are separate checks. No stored certificate is loaded.
"""

import argparse
from itertools import product
import json
from pathlib import Path
import subprocess

import numpy as np
import sympy as sp


BASELINE = "6766ecbc20b084c648b29b0bf3813b8c1ecf86cb"


def word(s):
    return tuple((-1) ** i * (1 if i < 2 * s else -1) for i in range(4 * s))


def fiber(tau, s, z):
    p = len(tau)
    out = sp.zeros(p)
    for i in range(p):
        for d, coefficient in ((-1, 1), (1, 1), (-s, tau[(i-s) % p]), (s, tau[i])):
            winding, j = divmod(i+d, p)
            out[i, j] += coefficient * z ** winding
    return out


def continuant(n, d):
    if n < 0:
        assert n == -1
        return sp.Integer(0)
    prev, now = sp.Integer(0), sp.Integer(1)
    for _ in range(n):
        prev, now = now, sp.expand(d*now-prev)
    return now


def polynomial(r, y, h):
    a = continuant(r-1, y-4-h)
    b = continuant(r-1, y-4+h)
    c = continuant(r-2, y-4-h)
    d = continuant(r-2, y-4+h)
    e = continuant(r, y-4-h)
    f = continuant(r, y-4+h)
    return sp.expand((e*f)**2 - 12*a*b*e*f + 38*a*a*b*b
                     - 12*a*b*c*d + c*c*d*d + (4*h-10)*b*b
                     - (4*h+10)*a*a + 4*a*b*(h*h-4) - (h*h-2))


def chain_model(s, xi):
    """8I-K, in interleaved E/O order. Coincident channels are added."""
    r = s//2
    h = xi+1/xi
    out = sp.zeros(2*s)

    def edge(i, j, a):
        out[i, j] += a
        # Laurent adjoint, valid even for the off-circle identity test.
        if a == -1/xi:
            out[j, i] += -xi
        elif a == 1/xi:
            out[j, i] += xi
        elif a == 2/xi:
            out[j, i] += 2*xi
        else:
            out[j, i] += a

    for j in range(s):
        out[2*j, 2*j] = 4-h if j < r else 4+h
        out[2*j+1, 2*j+1] = 4+h if j < r else 4-h
    for j in range(s-1):
        edge(2*j, 2*j+2, -1)
        edge(2*j+1, 2*j+3, -1)
    edge(0, 2*s-2, -1/xi)
    edge(1, 2*s-1, 1/xi)
    edge(0, 2*r-1, -2)
    edge(2*r, 2*s-1, 2/xi)
    return out.applyfunc(sp.expand)


def matrix_audit():
    phases = (sp.Integer(1), -sp.Integer(1), sp.I,
              (sp.Integer(3)+4*sp.I)/5, sp.Integer(2))
    count = 0
    lam = sp.Symbol('lambda')
    for s in range(2, 18, 2):
        p, m = 4*s, 2*s
        for xi in phases:
            z = sp.expand(xi**2)
            h = sp.simplify(xi+1/xi)
            H = fiber(word(s), s, z).applyfunc(sp.expand)
            W = sp.zeros(p, m)
            for i in range(m):
                W[i, i] = 1
                W[i+m, i] = xi*(-1)**i
            squared = H*H
            K = (squared*W)[:m, :].applyfunc(sp.simplify)
            assert (squared*W-W*K).applyfunc(sp.simplify) == sp.zeros(p, m)
            assert (8*sp.eye(m)-K-chain_model(s, xi)).applyfunc(sp.simplify) == sp.zeros(m)
            coefficients = H.charpoly(lam).all_coeffs()
            assert all(v == 0 for v in coefficients[1::2])
            for y in (sp.Integer(0), sp.Integer(7), sp.Integer(8), sp.Integer(9)):
                direct = sum(coefficients[2*j]*y**(m-j) for j in range(m+1))
                assert sp.simplify(direct-polynomial(s//2, y, h)) == 0
            if xi != 2:
                direct_at_eight = sum(coefficients[2*j]*8**(m-j) for j in range(m+1))
                lower = 16 if s == 2 else 4*s*s-4
                assert sp.simplify(direct_at_eight-lower) >= 0
            count += 1
    return {"even_jumps": list(range(2, 18, 2)), "exact_phase_cases": count,
            "squared_parameters_per_case": [0, 7, 8, 9],
            "off_circle_cases_are_algebra_only": True}


def polynomial_audit():
    h, t, w = sp.symbols('h t w')
    F = []
    for r in range(13):
        p = sp.Poly(continuant(r, 4-h)*continuant(r, 4+h), h)
        assert all(m[0] % 2 == 0 for m, _ in p.terms())
        F.append(sp.expand(sum(a*(4-t)**(m[0]//2) for m, a in p.terms())))
        S = F[r]-6*(F[r-1] if r >= 1 else 0)+(F[r-2] if r >= 2 else 0)
        assert all(a >= 0 for a in sp.Poly(S, t).all_coeffs())
        if r >= 1:
            assert S.subs(t, 0) == 2*sp.chebyshevt(r, 3)
            a, b = continuant(r-1, 4-h), continuant(r-1, 4+h)
            compact = S.subs(t, 4-h*h)**2 - 4*((2+h)*a*a+(2-h)*b*b+(4-h*h)*a*b)-h*h
            assert sp.expand(polynomial(r, 8, h)-compact) == 0
        if r >= 2:
            assert 2*sp.chebyshevt(r, 3) >= 4*(r+sp.chebyshevu(r-1, 3))
    series = sum(F[r]*w**r for r in range(len(F)))
    denominator = (1-6*w+w*w)**2-t*w*(1+w)**2
    residual = sp.Poly(sp.expand(denominator*series-(1-w*w)), w)
    assert all(residual.nth(k) == 0 for k in range(len(F)))
    for n in range(13):
        x = sp.Symbol('x')
        rhs = sum(sp.binomial(n+j+1, 2*j+1)*(2*x)**j for j in range(n+1))
        assert sp.expand(sp.chebyshevu(n, 1+x)-rhs) == 0
    # Deliberately changing the coefficient 6 must break the generating identity.
    bad_denominator = (1-5*w+w*w)**2-t*w*(1+w)**2
    assert sp.Poly(sp.expand(bad_denominator*series-(1-w*w)), w).nth(1) != 0
    return {"generating_function_degrees_checked": list(range(13)),
            "compact_determinant_identity_r": list(range(1, 13)),
            "tampered_recurrence_rejected": True}


def endpoint_audit():
    l, k, u, v, xi = sp.symbols('l k u v xi', nonzero=True)
    h = xi+1/xi
    M = sp.diag(l, l, k, k, k, k, l, l)
    for i, j, value in [(0, 1, -u), (2, 3, -v), (4, 5, -v), (6, 7, -u),
                         (1, 2, -1), (5, 6, -1), (0, 5, -2)]:
        M[i, j] = M[j, i] = value
    for i, j, sign in [(0, 3, -1), (4, 7, 1), (2, 7, 2)]:
        M[i, j], M[j, i] = sign/xi, sign*xi
    expression = ((l*l-u*u)**2*(k*k-v*v)**2
                  - 12*k*l*(l*l-u*u)*(k*k-v*v) + 38*k*k*l*l-12*k*l+1
                  - u*u*v*v*(h*h-2) + (4*h-10)*u*u*k*k
                  - (4*h+10)*v*v*l*l + 4*u*v*k*l*(h*h-4))
    assert sp.expand(M.det(method='domain-ge')-expression) == 0
    x, a, b = sp.symbols('x a b', nonzero=True)
    d1, d2 = a+1/a, b+1/b
    characteristic = sp.prod(x-root for root in (a*b, a/b, b/a, 1/(a*b)))
    recurrence = x**4-d1*d2*x**3+(d1*d1+d2*d2-2)*x*x-d1*d2*x+1
    assert sp.expand(characteristic-recurrence) == 0
    return {"eight_endpoint_determinant": "symbolic identity in all five variables",
            "product_continuant_recurrence": "symbolic characteristic-root identity"}


def flat_audit():
    rows = []
    total = 0
    for n in range(5, 13):
        for s in range(2, (n-1)//2+1):
            flat = []
            for alpha in (-1, 1):
                for tau in product((-1, 1), repeat=n):
                    A = np.zeros((n, n), dtype=np.int64)
                    for i in range(n):
                        for step, coefficient in ((1, 1), (s, tau[i])):
                            winding, j = divmod(i+step, n)
                            A[i, j] += coefficient*alpha**winding
                            A[j, i] += coefficient*alpha**winding
                    square = A@A
                    if np.array_equal(square, 4*np.eye(n, dtype=np.int64)):
                        flat.append((alpha, tau))
                    if n != 2*s+2:
                        assert square[0, 2] % 2 == 1
                    total += 1
            expected = 6 if (n, s) == (8, 3) else 2 if n == 2*s+2 else 0
            assert len(flat) == expected
            if n == 2*s+2 and s != 3:
                assert all(alpha == (-1)**(s+1) and
                           all(tau[i] == tau[0]*(-1)**i for i in range(n))
                           for alpha, tau in flat)
            rows.append({"N": n, "s": s, "flat_switching_classes": len(flat)})
    return {"switching_coordinates_checked": total, "rows": rows}


def chiral_audit():
    count = 0
    z = sp.Integer(2)
    for p in (2, 4, 6, 8):
        m = p//2
        M = sp.zeros(p)
        for i in range(p):
            winding, j = divmod(i+m, p)
            M[i, j] = (-1)**i*z**winding
        assert M*M == (-1)**m*z*sp.eye(p)
        for s in range(2, 7):
            for tau in product((-1, 1), repeat=p):
                expected = all(tau[(i+m) % p] == (-1)**(s+1)*tau[i] for i in range(p))
                Q = [tau[i]*tau[(i+1) % p] for i in range(p)]
                flux = (all(Q[(i+m) % p] == Q[i] for i in range(p)) and
                        sp.prod(Q[:m]) == (-1)**(s+1))
                H = fiber(tau, s, z)
                assert (M*H+H*M == sp.zeros(p)) == expected == flux
                count += 1
    return {"displayed_periods": [2, 4, 6, 8], "jumps": list(range(2, 7)),
            "exact_off_circle_identity_cases": count,
            "all_phase_necessity_uses_the_analytic_Laurent_argument": True}


def freeze_audit():
    root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
    protected = ['research/paper_strengthening', 'research/paper', 'formal/TargetA']
    subprocess.run(['git', 'diff', '--exit-code', BASELINE, '--', *protected], cwd=root, check=True)
    hashes = {p: subprocess.check_output(['git', 'rev-parse', f'{BASELINE}:{p}'], cwd=root, text=True).strip()
              for p in protected}
    return {"baseline_commit": BASELINE, "protected_git_trees": hashes, "unchanged": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    results = {"scope": "Finite exact regression; universal claims use the written analytic proof."}
    for name, check in [('freeze', freeze_audit), ('endpoint_identity', endpoint_audit),
                        ('continuants', polynomial_audit),
                        ('fibers', matrix_audit), ('flat_classification', flat_audit),
                        ('chiral_criterion', chiral_audit)]:
        results[name] = check()
        print(name.upper()+'_EXACT_AUDIT_PASS', flush=True)
    if args.output:
        args.output.write_text(json.dumps(results, indent=2)+'\n')
    print('CIRCULANT_1S_EXTENSION_EXACT_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
