"""Regression and evidence-boundary tests for Target A Task 48A."""

from __future__ import annotations

import csv
import json
import subprocess
from fractions import Fraction
from pathlib import Path

import numpy as np

from target_a_finite_phase_slips import _q_from_gaps
from target_a_task47_common import ETA, defect_gaps
from target_a_task48a_common import (
    dense_spectrum,
    localization_profile,
    q_from_gaps,
    signing_arrays,
    single_slip_gaps,
    sparse_exact_ldl_positive,
    sparse_radius_squared,
    two_slip_gaps,
)
from target_a_task48a_moment_matrix import hankel


RESEARCH = Path(__file__).resolve().parents[1]
REPO = RESEARCH.parent
ROOT = RESEARCH / "experiments" / "task48a"


def _rho_dense(n: int, gap: int, alpha: int = 1) -> float:
    q = q_from_gaps(n, single_slip_gaps(n, gap))
    values, _vectors = dense_spectrum(q, alpha)
    return float(max(abs(values[0]), abs(values[-1])) ** 2)


def test_task47_gap6_recovery() -> None:
    assert abs(_rho_dense(50, 6) - 7.904919714065006) < 1e-11


def test_task47_n52_exact_certificate_recovery() -> None:
    path = RESEARCH / "experiments" / "finite_phase_slips" / "certificates" / "n52_a-1.json"
    certificate = json.loads(path.read_text(encoding="utf-8"))
    assert certificate["result"] is True
    assert certificate["positive_definite_by_exact_bareiss_sylvester"] is True


def test_task47_gap10_recovery() -> None:
    assert abs(_rho_dense(94, 10) - 7.977104323314659) < 1e-11


def test_gap_reconstruction_and_legality() -> None:
    for n, gap in ((50, 6), (94, 10), (52, 8)):
        gaps = single_slip_gaps(n, gap)
        q = q_from_gaps(n, gaps)
        assert sorted(defect_gaps(q)) == sorted(gaps)
        assert np.prod(q) == 1
        assert _q_from_gaps(n, gaps) == q


def test_both_holonomies_construct() -> None:
    q = q_from_gaps(50, single_slip_gaps(50, 6))
    for alpha in (-1, 1):
        step1, step2 = signing_arrays(q, alpha)
        assert int(np.prod(step1)) == alpha
        assert set(step2) <= {-1.0, 1.0}


def test_dense_sparse_eigenvalue_agreement() -> None:
    q = q_from_gaps(58, single_slip_gaps(58, 6))
    dense = _rho_dense(58, 6)
    sparse = sparse_radius_squared(q, 1)["rho_squared"]
    assert abs(dense - sparse) < 1e-9


def test_localization_extraction() -> None:
    data = json.loads((ROOT / "interface" / "localization" / "g6_n258.json").read_text(encoding="utf-8"))
    assert data["left_fit"]["r_squared"] > 0.99
    assert data["right_fit"]["r_squared"] > 0.99
    assert 0 < data["left_fit"]["multiplier"] < 1
    assert 0 < data["right_fit"]["multiplier"] < 1


def test_high_precision_double_consistency() -> None:
    constants = json.loads((ROOT / "interface" / "constants.json").read_text(encoding="utf-8"))
    for name, filename in (("G6", "g6_spectrum.csv"), ("G10", "g10_spectrum.csv")):
        rows = list(csv.DictReader((ROOT / "interface" / filename).open()))
        assert abs(float(rows[-1]["rho_squared"]) - float(constants[name]["R_squared"])) < 2e-10


def test_remaining_set_is_59() -> None:
    payload = json.loads((ROOT / "p24_frontier" / "remaining_59.json").read_text(encoding="utf-8"))
    assert payload["counts_by_period"] == {"22": 11, "23": 14, "24": 34}
    assert payload["count"] == 59


def test_all_frontier_orbits_consumed_once() -> None:
    payload = json.loads((ROOT / "p24_frontier" / "p17_p24_partition.json").read_text(encoding="utf-8"))
    assert payload["consumed_exactly_once"] is True
    for row in payload["periods"]:
        assert sum(row["classes"].values()) == row["legal_dihedral_orbits"]
        assert row["classes"]["L"] == row["classes"]["U"] == 0


def test_moment_hankel_construction() -> None:
    moments = [1, 2, 6, 20, 70, 252]
    h, s = hankel(moments, 2)
    assert h == [[1, 2, 6], [2, 6, 20], [6, 20, 70]]
    assert s == [[2, 6, 20], [6, 20, 70], [20, 70, 252]]


def test_exact_psd_sign_sanity() -> None:
    matrix = np.asarray([[2, 1], [1, 2]], dtype=np.int64)
    result = sparse_exact_ldl_positive(matrix)
    assert result["positive"] is True
    assert result["pivots"] == [Fraction(2), Fraction(3, 2)]
    pilot = json.loads((ROOT / "moment_matrix" / "summary.json").read_text(encoding="utf-8"))
    assert pilot["target_PSD_direction_sanity"] == "PASS"


def test_residue12_exact_certificates() -> None:
    summary = json.loads((ROOT / "residue12" / "summary.json").read_text(encoding="utf-8"))
    assert summary["first_exact_order"] == 60
    assert summary["exact_counterexamples"] == 29
    assert summary["all_exact_certificates_pass"] is True


def test_task47_regression_artifacts() -> None:
    payload = json.loads((RESEARCH / "experiments" / "finite_phase_slips" / "summary.json").read_text(encoding="utf-8"))
    assert payload["certified_counterexample_count"] == 33
    assert json.loads((RESEARCH / "experiments" / "high_period_moments" / "summary.json").read_text(encoding="utf-8"))["status"] == "TARGET_A_HIGH_PERIOD_MOMENT_HIERARCHY_COMPLETE"


def test_manuscript_and_theorem_freeze() -> None:
    result = subprocess.run(
        ["git", "diff", "--name-only", "60e2e1a24d8aa584dfafa8a451c1b436df368fc7", "--", "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh"],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == ""
