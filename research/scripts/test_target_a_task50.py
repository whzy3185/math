"""Proof-gate regression tests for Target A Task 50."""

from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

import sympy as sp

from target_a_task50_bulk import TAU, monodromy
from target_a_task50_interval import Interval, interval_sqrt


RESEARCH = Path(__file__).resolve().parents[1]
PROOFS = RESEARCH / "proofs" / "task50"
CERTS = PROOFS / "certificates"
REPRO = RESEARCH / "reproducibility" / "task50"
BASELINE = "7f05eddc618bb0e9d772626aa87f4f0f3c17d276"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_exact_m8_multiplication():
    lam = sp.symbols("lambda")
    matrix = monodromy(lam)
    stored = load(CERTS / "bulk_symbolic.json")
    assert stored["tau_cell"] == list(TAU)
    assert [[str(sp.factor(value)).replace("**", "^") for value in matrix.row(row)] for row in range(4)] == stored["M8_entries"]


def test_characteristic_polynomial_reproduction():
    lam, y, z = sp.symbols("lambda y z")
    actual = sp.Poly(monodromy(lam).charpoly(z).as_expr().subs(lam**2, y), z)
    expected = sp.Poly(z**4 + (-2*y**2+16*y-13)*z**3 + (y**4-16*y**3+80*y**2-128*y+40)*z**2 + (-2*y**2+16*y-13)*z + 1, z)
    assert actual == expected


def test_palindromic_reduction():
    y, z, w = sp.symbols("y z w")
    a = -2*y**2+16*y-13; b = y**4-16*y**3+80*y**2-128*y+40
    reduced = w**2+a*w+b-2
    quartic = z**4+a*z**3+b*z**2+a*z+1
    assert sp.cancel(z**2*reduced.subs(w,z+1/z)-quartic) == 0


def test_reciprocal_pairing():
    coefficients = sp.Poly(load(CERTS / "bulk_symbolic.json")["characteristic_polynomial"].replace("^", "**"), sp.symbols("z")).all_coeffs()
    assert coefficients == list(reversed(coefficients))


def test_rational_proof_intervals():
    bulk = load(CERTS / "bulk_hyperbolicity_certificates.json")
    assert list(map(Fraction, bulk["G6"]["y_interval"])) == [Fraction(1581,200), Fraction(3953,500)]
    assert list(map(Fraction, bulk["G10"]["y_interval"])) == [Fraction(7977,1000), Fraction(3989,500)]


def test_stable_unstable_count():
    bulk = load(CERTS / "bulk_hyperbolicity_certificates.json")
    assert all("two stable" in bulk[name]["root_structure"] for name in ("G6", "G10"))


def test_no_unit_circle_multiplier():
    bulk = load(CERTS / "bulk_hyperbolicity_certificates.json")
    assert all(all(item["checks"].values()) for item in (bulk["G6"], bulk["G10"]))


def test_exact_p6_transfer():
    transfer = load(CERTS / "g6_defect_transfer.json")
    assert transfer["determinant"] == "1" and transfer["cut"] == [-8,14]


def test_exact_p10_transfer():
    transfer = load(CERTS / "g10_defect_transfer.json")
    assert transfer["determinant"] == "1" and transfer["cut"] == [-8,18]


def test_g6_interval_root_enclosure():
    cert = load(CERTS / "g6_interface_certificate.json")
    assert cert["status"] == "G6_INTERFACE_THEOREM_PROVED"
    assert cert["checks"]["left_sign_negative"] and cert["checks"]["right_sign_positive"]


def test_g6_uniqueness():
    cert = load(CERTS / "g6_interface_certificate.json")
    assert cert["checks"]["derivative_positive"] and cert["checks"]["all_cofactor_vectors_nonzero"]


def test_g10_interval_root_enclosure():
    cert = load(CERTS / "g10_interface_certificate.json")
    assert cert["status"] == "G10_INTERFACE_THEOREM_PROVED"
    assert cert["checks"]["left_sign_negative"] and cert["checks"]["right_sign_positive"]


def test_g10_uniqueness():
    cert = load(CERTS / "g10_interface_certificate.json")
    assert cert["checks"]["derivative_positive"] and cert["checks"]["all_cofactor_vectors_nonzero"]


def test_c6_upper_bound_below_8():
    assert Fraction(load(CERTS / "g6_interface_certificate.json")["y_interval"][1]) < 8


def test_c10_upper_bound_below_8():
    assert Fraction(load(CERTS / "g10_interface_certificate.json")["y_interval"][1]) < 8


def test_localization_q_below_one():
    assert Fraction(load(CERTS / "g6_interface_certificate.json")["localization"]["bulk_cell_rate"]) < 1
    assert Fraction(load(CERTS / "g10_interface_certificate.json")["localization"]["bulk_cell_rate"]) < 1


def test_g6_finite_ring_gate_is_fail_closed():
    assert load(CERTS / "finite_ring_recurrence.json")["status"] == "SINGLE_INTERFACE_BOUND_INCOMPLETE"


def test_g10_finite_ring_gate_is_fail_closed():
    data = load(CERTS / "finite_ring_recurrence.json")
    assert data["family_parameters"]["G10"]["closure_distance_cells"] == "k"
    assert data["status"] == "SINGLE_INTERFACE_BOUND_INCOMPLETE"


def test_two_tail_gate_is_fail_closed():
    text = (PROOFS / "TARGET_A_TWO_INTERFACE_BOUND_STATUS.md").read_text(encoding="utf-8")
    assert "TWO_INTERFACE_BOUND_INCOMPLETE" in text


def test_both_holonomies_in_exact_closure():
    data = load(CERTS / "finite_ring_recurrence.json")
    assert {(row["family"], row["alpha"]) for row in data["exact_sanity"]} == {("G6",-1),("G6",1),("G10",-1),("G10",1)}


def test_residue_formulas():
    for r in range(1,5):
        symmetric = [6]+[4]*(2*r-1)+[6]+[4]*(2*r-1)
        shifted = [6]+[4]*(2*r-1)+[6]+[4]*(2*r+1)
        assert sum(symmetric) == 16*r+4 and len(symmetric)%2 == 0
        assert sum(shifted) == 16*r+12 and len(shifted)%2 == 0


def test_threshold_inequality_constant():
    assert Fraction(20)*Fraction(22,7)**2 < 200


def test_final_n_is_not_asserted():
    text = (PROOFS / "TARGET_A_EVENTUAL_THRESHOLD_STATUS.md").read_text(encoding="utf-8")
    assert "No global `N` is asserted" in text and "ALL_EVEN_THEOREM_INCOMPLETE" in text


def test_task49_regression():
    assert load(RESEARCH / "experiments" / "task49" / "interface_mechanism" / "summary.json")["gate"] == "INTERFACE_MECHANISM_READY_FOR_PROOF"


def test_task48a_regression():
    assert load(RESEARCH / "experiments" / "task48a" / "interface" / "summary.json")["INTERFACE_THEOREM_SIGNAL"] == "STRONG"


def test_task47_regression():
    text = (RESEARCH / "experiments" / "TARGET_A_TASK47_SYNTHESIS.md").read_text(encoding="utf-8")
    assert "TARGET_A_TASK47_EXPERIMENTS_COMPLETE" in text


def test_manuscript_freeze():
    result = subprocess.run(["git","diff","--quiet",BASELINE,"--","research/paper/manuscript_tex_pub","research/paper/manuscript_tex_pub_zh"],cwd=RESEARCH.parent)
    assert result.returncode == 0


def test_existing_theorem_statements_unchanged():
    result = subprocess.run(["git","diff","--name-only","--diff-filter=MDR",BASELINE,"--","research/proofs"],cwd=RESEARCH.parent,capture_output=True,text=True,check=True)
    assert all(path.startswith("research/proofs/task50/") for path in result.stdout.splitlines())


def test_outward_square_root_kernel():
    value = Interval.point(Fraction(2))
    root = interval_sqrt(value)
    assert root.lo**2 <= 2 <= root.hi**2 and root.lo < root.hi


def test_independent_coordinate_checker():
    assert load(REPRO / "interface_checker_output.json")["status"] == "TARGET_A_TASK50_INTERFACE_INDEPENDENT_CHECK_PASS"


def test_certificate_manifest():
    manifest = load(REPRO / "certificate_manifest.json")
    assert manifest["status"] == "TARGET_A_TASK50_CERTIFICATE_PACKAGE_READY"
    assert len(manifest["proved_gates"]) == 3 and len(manifest["incomplete_gates"]) == 3
