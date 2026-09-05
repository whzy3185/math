#!/usr/bin/env python3
"""Exact derivative-bound checks, with an optional separate numerical probe.

The finite tests are not the proof of the universal estimates.
Run with --numerical only to regenerate the labelled conjecture evidence.
"""

import argparse
import json
from pathlib import Path

import sympy as sp

from verify_extension import chain_model, fiber, freeze_audit, word


def path_dual(n, d):
    prev, value = sp.Integer(0), sp.Integer(1)
    prev_derivative, derivative = sp.Integer(0), sp.Integer(0)
    for _ in range(n):
        prev, value, prev_derivative, derivative = (
            value, d*value-prev, derivative, value+d*derivative-prev_derivative)
    return value, derivative


def values(r, h):
    vals, derivatives = [], []
    for j in range(r+1):
        a, ap = path_dual(j, 4-h)
        b, bp = path_dual(j, 4+h)
        vals.append(a*b)
        derivatives.append(ap*b+a*bp)
    S = vals[r]-6*vals[r-1]+vals[r-2]
    Sp = derivatives[r]-6*derivatives[r-1]+derivatives[r-2]
    a, ap = path_dual(r-1, 4-h)
    b, bp = path_dual(r-1, 4+h)
    q = S*S-4*((2+h)*a*a+(2-h)*b*b+(4-h*h)*a*b)-h*h
    qp = 2*S*Sp-4*((2+h)*2*a*ap+(2-h)*2*b*bp+(4-h*h)*(ap*b+a*bp))
    return vals, derivatives, S, Sp, q, qp


def inequality_audit():
    phases = [sp.Rational(x) for x in (-2, -1, 0, 1, 2)] + [sp.Rational(-8, 5), sp.Rational(8, 5)]
    count = 0
    for r in range(2, 25):
        for h in phases:
            F, Fp, S, Sp, q, qp = values(r, h)
            assert q >= S*S/3
            assert F[r-1] <= sp.Rational(r, 2)*S
            for j in range(r+1):
                assert 0 <= Fp[j] <= sp.Rational(j*(j+2), 3)*F[j]
            assert 0 < Sp <= sp.Rational(r*(r+2)*(1+3*r), 3)*S
            assert 0 < qp/q <= 14*r**3
            assert q/qp >= sp.Rational(1, 14*r**3) >= sp.Rational(1, 2*(2*r)**3)
            count += 1
    return {"r": [2, 24], "exact_h_values": [str(h) for h in phases],
            "rational_inequality_cases": count}


def determinant_derivative_audit():
    count = 0
    for s in (4, 6, 8, 10, 12):
        for xi in (sp.Integer(1), sp.I, (sp.Integer(3)+4*sp.I)/5):
            h = sp.simplify(xi+1/xi)
            H = fiber(word(s), s, sp.expand(xi*xi)).applyfunc(sp.expand)
            coefficients = H.charpoly().all_coeffs()
            m = 2*s
            direct_q = sum(coefficients[2*j]*8**(m-j) for j in range(m+1))
            direct_qp = sum(coefficients[2*j]*(m-j)*8**(m-j-1) for j in range(m))
            *_, q, qp = values(s//2, h)
            assert sp.simplify(q-direct_q) == sp.simplify(qp-direct_qp) == 0
            C = chain_model(s, xi)
            assert sp.simplify(sp.trace(C.inv())-qp/q) == 0
            count += 1
    return {"even_jumps": [4, 6, 8, 10, 12], "exact_phase_cases": count,
            "inverse_trace_equals_log_determinant_derivative": True}


def numerical_probe():
    import numpy as np
    from scipy.sparse import lil_matrix
    from scipy.sparse.linalg import eigsh

    def C_numeric(s, theta):
        r, xi = s//2, np.exp(0.5j*theta)
        h = 2*np.cos(0.5*theta)
        C = lil_matrix((2*s, 2*s), dtype=complex)
        for j in range(s):
            C[2*j, 2*j] = 4-h if j < r else 4+h
            C[2*j+1, 2*j+1] = 4+h if j < r else 4-h
        entries = [(2*j, 2*j+2, -1) for j in range(s-1)]
        entries += [(2*j+1, 2*j+3, -1) for j in range(s-1)]
        entries += [(0, 2*s-2, -1/xi), (1, 2*s-1, 1/xi),
                    (0, 2*r-1, -2), (2*r, 2*s-1, 2/xi)]
        for i, j, a in entries:
            C[i, j] += a
            C[j, i] += np.conjugate(a)
        return C.tocsr()

    endpoint_rows = []
    for s in (4, 8, 16, 32, 64, 128, 256):
        C = C_numeric(s, 0)
        eigenvalues, eigenvectors = eigsh(C, k=1, which='SA', tol=1e-11,
                                         v0=np.linspace(1, 2, 2*s))
        gap = float(eigenvalues[0])
        residual = float(np.linalg.norm(C@eigenvectors[:, 0]-gap*eigenvectors[:, 0]))
        endpoint_rows.append({"s": s, "gap_at_z_1": gap, "s_squared_times_gap": s*s*gap,
                              "scaled_over_pi_squared": s*s*gap/np.pi**2,
                              "eigenpair_residual": residual})
    phase_rows = []
    for s in (4, 8, 16, 32):
        gaps = [float(np.linalg.eigvalsh(C_numeric(s, theta).toarray())[0])
                for theta in np.linspace(0, 2*np.pi, 65)]
        phase_rows.append({"s": s, "phase_points": 65, "sample_min_gap": min(gaps),
                           "endpoint_gap": gaps[0], "endpoint_minus_sample_min": gaps[0]-min(gaps)})
    return {"status": "NUMERICAL_EVIDENCE_ONLY; Q6 and Q7 remain unproved",
            "endpoint_values_are_not_global_Bloch_gap_certificates": True,
            "endpoint_rows": endpoint_rows, "phase_rows": phase_rows}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--numerical', action='store_true')
    args = parser.parse_args()
    result = {"scope": "Finite exact audit of the analytic polynomial-gap proof", "freeze": freeze_audit()}
    result['rational_inequalities'] = inequality_audit()
    print('QUANTITATIVE_RATIONAL_INEQUALITIES_PASS', flush=True)
    result['derivative_identity'] = determinant_derivative_audit()
    print('DETERMINANT_DERIVATIVE_EXACT_AUDIT_PASS', flush=True)
    if args.numerical:
        result['numerical_conjecture_evidence'] = numerical_probe()
        print('NUMERICAL_CONJECTURE_PROBE_RECORDED_NOT_A_PROOF', flush=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('POLYNOMIAL_GAP_EXACT_AUDIT_PASS', flush=True)


if __name__ == '__main__':
    main()
