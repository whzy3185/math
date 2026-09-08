#!/usr/bin/env python3
import argparse, json, platform
import sympy as sp


def is_zero(expr):
    return sp.simplify(sp.expand(expr)) == 0


def total_degree(expr, vars):
    return sp.Poly(sp.expand(expr), *vars).total_degree()


def leading_form(expr, vars):
    P = sp.Poly(sp.expand(expr), *vars)
    D = P.total_degree()
    out = 0
    for mon, coeff in P.terms():
        if sum(mon) == D:
            term = coeff
            for v, e in zip(vars, mon):
                term *= v**e
            out += term
    return sp.expand(out), D


def constant_ratio(f, g, vars):
    if is_zero(g):
        return None
    q = sp.cancel(f/g)
    if any(v in q.free_symbols for v in vars):
        return None
    if is_zero(q):
        return None
    return sp.simplify(q)


def direct_candidate(P, G, mus, vars, k):
    if mus[k] != 1:
        return None
    Gk = sp.diff(G, vars[k])
    if is_zero(Gk):
        return None
    thetas = {}
    for j, v in enumerate(vars):
        if j == k:
            continue
        if not is_zero(sp.diff(G, v)):
            return None
        q = constant_ratio(sp.diff(P, v), Gk, vars)
        if q is None:
            return None
        thetas[j] = q
    return thetas


def add(checks, name, cond, detail=''):
    checks.append({'name': name, 'passed': bool(cond), 'detail': detail})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', default='verification_v3.json')
    args = ap.parse_args()

    x, y, z, t = sp.symbols('x y z t')
    checks = []

    # Positive irreducible/full-direction examples (irreducibility justified in manuscript).
    P = x*y + 1; G = x**2
    cand = direct_candidate(P, G, [1,1], (x,y), 0)
    add(checks, 'direct_xy_plus_1', cand == {1: sp.Rational(1,2)}, str(cand))
    v = y*sp.exp(x**2/2) + sp.Integral(sp.exp(t**2/2), (t,0,x))
    add(checks, 'solution_xy_plus_1', is_zero(sp.diff(v,x)*sp.diff(v,y) - P*sp.exp(G)))

    P = x+y; G = 2*x
    cand = direct_candidate(P,G,[1,1],(x,y),0)
    add(checks, 'direct_linear_2d', cand == {1: sp.Rational(1,2)}, str(cand))
    v = sp.exp(x)*(x+y-1)
    add(checks, 'solution_linear_2d', is_zero(sp.diff(v,x)*sp.diff(v,y)-P*sp.exp(G)))

    P = x+y+z; G = 3*x
    cand = direct_candidate(P,G,[1,1,1],(x,y,z),0)
    add(checks, 'direct_linear_3d', cand == {1: sp.Rational(1,3), 2: sp.Rational(1,3)}, str(cand))
    v = sp.exp(x)*(x+y+z-1)
    add(checks, 'solution_linear_3d', is_zero(sp.diff(v,x)*sp.diff(v,y)*sp.diff(v,z)-P*sp.exp(G)))

    P = x+y+z; G = 6*x
    cand = direct_candidate(P,G,[1,2,3],(x,y,z),0)
    add(checks, 'weighted_direct', cand == {1: sp.Rational(1,6), 2: sp.Rational(1,6)}, str(cand))
    v = sp.exp(x)*(x+y+z-1)
    lhs = sp.diff(v,x)*sp.diff(v,y)**2*sp.diff(v,z)**3
    add(checks, 'weighted_solution', is_zero(lhs-P*sp.exp(G)))

    # Degree obstruction: deg G > deg P cannot pass the differential criterion.
    P = x+y; G = x**2
    add(checks, 'degree_obstruction_candidate_fails', direct_candidate(P,G,[1,1],(x,y),0) is None)
    add(checks, 'degree_obstruction_numeric', total_degree(G,(x,y)) > total_degree(P,(x,y)))

    # Leading-form positive D=d=2 example: P_2=x(x+y).
    P = x**2+x*y+1; G=x**2
    lead,D = leading_form(P,(x,y))
    add(checks, 'leading_D_eq_d', is_zero(lead-x*(x+y)) and D==2, str(lead))
    v = sp.exp(x**2/2)*(x+y)
    add(checks, 'leading_D_eq_d_solution', is_zero(sp.diff(v,x)*sp.diff(v,y)-P*sp.exp(G)))

    # Leading-form positive D>d example: pure power x^3.
    P = x**3+y; G=2*x
    lead,D = leading_form(P,(x,y))
    add(checks, 'leading_D_gt_d', is_zero(lead-x**3) and D==3, str(lead))
    v = sp.exp(x)*y + sp.Integral(t**3*sp.exp(t),(t,0,x))
    add(checks, 'leading_D_gt_d_solution', is_zero(sp.diff(v,x)*sp.diff(v,y)-P*sp.exp(G)))

    # Squarefree cubic leading form cannot contain a square of any coordinate.
    P = x*y*z + 1
    lead,D = leading_form(P,(x,y,z))
    sqfree_block = all(sp.rem(sp.Poly(lead,x,y,z), sp.Poly(vv**2,x,y,z)) != 0 for vv in (x,y,z))
    add(checks, 'squarefree_cubic_obstruction', D==3 and sqfree_block, str(lead))

    # Rank obstruction for nondegenerate quadratic leading part.
    q = x**2+y**2+z**2
    H = sp.hessian(q,(x,y,z))/2
    add(checks, 'quadratic_rank_obstruction', H.rank()==3, f'rank={H.rank()}')

    # Nontrivial original-coordinate test. A=[[1,1],[0,1]], D1=dx+dy, D2=dy.
    p = y; g = 2*x; u = sp.exp(x)*(y-1)
    D1 = lambda f: sp.diff(f,x)+sp.diff(f,y)
    D2 = lambda f: sp.diff(f,y)
    add(checks, 'original_direction_criterion', is_zero(D2(g)) and is_zero(D2(p)-sp.Rational(1,2)*D1(g)))
    add(checks, 'original_direction_solution', is_zero(D1(u)*D2(u)-p*sp.exp(g)))

    status = 'passed' if all(c['passed'] for c in checks) else 'failed'
    out = {
        'status': status,
        'count': len(checks),
        'python': platform.python_version(),
        'sympy': sp.__version__,
        'evidence': 'exact symbolic checks for v3 corollaries; not a formal proof',
        'checks': checks,
    }
    with open(args.output,'w',encoding='utf-8') as f:
        json.dump(out,f,ensure_ascii=False,indent=2)
    print(json.dumps({'status':status,'count':len(checks)},ensure_ascii=False))
    if status != 'passed':
        for c in checks:
            if not c['passed']:
                print('FAILED',c)
        raise SystemExit(1)

if __name__ == '__main__':
    main()
