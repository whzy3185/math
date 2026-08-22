"""Regression and evidence-boundary tests for Target A Task 49."""

from __future__ import annotations

import csv
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

import mpmath as mp


RESEARCH = Path(__file__).resolve().parents[1]
TASK49 = RESEARCH / "experiments" / "task49"
REPRO = RESEARCH / "reproducibility" / "task49"
BASELINE = "8ecbc6ab5ee1dcf519c92927fc2713e1989f40aa"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def rows(path: Path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def test_task48a_regression():
    summary = load(RESEARCH / "experiments" / "task48a" / "interface" / "summary.json")
    assert summary["status"] == "TARGET_A_TASK48A_INTERFACE_RECONNAISSANCE_COMPLETE"
    assert summary["INTERFACE_THEOREM_SIGNAL"] == "STRONG"


def test_c6_finite_family_recovery():
    data = rows(TASK49 / "uniform_bounds" / "g6_uniform_error.csv")
    assert min(abs(float(row["R_squared"]) - float(row["c"])) for row in data) < 1e-10


def test_c10_finite_family_recovery():
    data = rows(TASK49 / "uniform_bounds" / "g10_uniform_error.csv")
    assert min(abs(float(row["R_squared"]) - float(row["c"])) for row in data) < 1e-10


def test_normalized_error_calculation():
    row = next(row for row in rows(TASK49 / "uniform_bounds" / "g6_uniform_error.csv") if row["normalized_error"])
    expected = abs(float(row["error"])) / abs(float(row["mu"])) ** int(row["exponent"])
    assert math.isclose(float(row["normalized_error"]), expected, rel_tol=1e-13)


def test_two_tail_normalization():
    row = next(row for row in rows(TASK49 / "uniform_bounds" / "two_interface_uniform_error.csv") if row["explicit_family_geometry"] == "True")
    mu = load(TASK49 / "uniform_and_crossing_summary.json")["envelopes"]
    mu6 = float(load(RESEARCH / "experiments" / "task48a" / "interface" / "floquet_multipliers.json")["G6"]["slow_bulk_multiplier"])
    denominator = mu6 ** int(row["left_tail_cells"]) + mu6 ** int(row["right_tail_cells"])
    assert math.isclose(float(row["two_tail_normalized"]), float(row["error_from_c6"]) / denominator, rel_tol=1e-13)
    assert mu["two_interface"]["classification"] == "TWO_TAIL_BOUND_SUPPORTED"


def test_threshold_high_precision_evaluation():
    row = next(row for row in rows(TASK49 / "threshold_crossings" / "threshold_crossings.csv") if row["n"] == "94")
    mp.mp.dps = 60
    n = mp.mpf(row["n"])
    threshold = 4 * (mp.cos(mp.pi / n) ** 2 + mp.cos(2 * mp.pi / n) ** 2)
    assert abs(threshold - mp.mpf(row["threshold_squared"])) < mp.mpf("1e-14")


def test_early_gap6_family():
    data = [row for row in rows(TASK49 / "threshold_crossings" / "threshold_crossings.csv") if row["family"] == "G6"]
    assert [int(row["n"]) for row in data[:5]] == [18, 26, 34, 42, 50]
    assert data[4]["evidence_status"] == "CERTIFIED_COUNTEREXAMPLE"


def test_early_gap10_family():
    data = [row for row in rows(TASK49 / "threshold_crossings" / "threshold_crossings.csv") if row["family"] == "G10"]
    assert next(int(row["n"]) for row in data if float(row["delta"]) < 0) == 94


def test_early_symmetric_two_slip_family():
    data = [row for row in rows(TASK49 / "threshold_crossings" / "threshold_crossings.csv") if row["family"] == "TWO_SYMMETRIC"]
    assert next(int(row["n"]) for row in data if float(row["delta"]) < 0) == 52


def test_early_shifted_two_slip_family():
    data = [row for row in rows(TASK49 / "threshold_crossings" / "threshold_crossings.csv") if row["family"] == "TWO_SHIFTED"]
    assert float(next(row for row in data if row["n"] == "44")["delta"]) > 0
    assert next(int(row["n"]) for row in data if float(row["delta"]) < 0) == 60


def test_high_precision_splitting_reproducibility():
    row = rows(TASK49 / "interface_mechanism" / "two_interface_high_precision.csv")[-1]
    ladder = json.loads(row["precision_ladder"])
    assert [item["digits"] for item in ladder] == [80, 120, 160]
    assert abs(mp.mpf(ladder[-1]["y"][0]) - mp.mpf(ladder[-2]["y"][0])) < mp.mpf("1e-90")


def test_splitting_uses_dimension_reduction():
    summary = load(TASK49 / "interface_mechanism" / "summary.json")
    assert summary["splitting_precision_digits"] == 160
    assert "4x4" in summary["splitting_route"]
    assert summary["full_arbitrary_precision_matrix_crosschecks"] == 2


def test_stable_multiplier_phase_extraction():
    data = load(TASK49 / "interface_mechanism" / "floquet_multipliers_full.json")
    assert data["G6"]["all_real_positive"] and data["G10"]["all_real_positive"]
    assert all(mp.mpf(row["argument"]) == 0 for row in data["G6"]["multipliers"])


def test_reciprocal_multiplier_sanity():
    data = load(TASK49 / "interface_mechanism" / "floquet_multipliers_full.json")
    for family in ("G6", "G10"):
        values = [mp.mpf(row["value"]) for row in data[family]["multipliers"]]
        assert max(abs(values[i] * values[-1 - i] - 1) for i in range(2)) < mp.mpf("1e-90")


def test_cut_shift_invariance():
    data = rows(TASK49 / "interface_mechanism" / "interface_invariance.csv")
    evans = [row for row in data if row["route"] == "infinite_evans_right_match"]
    assert len(evans) == 8
    assert max(float(row["difference_from_reference"]) for row in evans) < 1e-90


def test_orientation_invariance():
    data = [row for row in rows(TASK49 / "interface_mechanism" / "interface_invariance.csv") if row["route"] == "finite_ring_dense_sparse"]
    for family in ("G6", "G10"):
        values = [float(row["finite_ring_R_squared"]) for row in data if row["family"] == family]
        assert max(values) - min(values) < 1e-9


def test_equivalent_matching_construction():
    summary = load(TASK49 / "interface_mechanism" / "summary.json")
    assert summary["equivalent_stable_unstable_matching"] is True


def test_localization_window_robustness():
    summary = load(TASK49 / "localization_robustness" / "summary.json")
    data = rows(TASK49 / "localization_robustness" / "localization_robustness.csv")
    assert summary["classification"] == "LOCALIZATION_ROBUST"
    assert len(data) == 60 and min(float(row["r_squared"]) for row in data) > 0.98


def test_p24_independent_orbit_count():
    summary = load(REPRO / "p24_independent" / "summary.json")
    assert summary["totals"]["legal_dihedral_orbits"] == 370100


def test_p24_destructive_accounting():
    summary = load(REPRO / "p24_independent" / "summary.json")
    assert summary["totals"]["consumed"] == 370100
    assert summary["destructive_accounting_remaining"] == 0


def test_independent_certificate_verification():
    summary = load(REPRO / "p24_independent" / "summary.json")
    strict = next(item for period in summary["periods"] for item in period["survivors"] if item["classification"] == "STRICT")
    assert Fraction(strict["certificate"]["bound"]) > Fraction(1561, 200)
    assert strict["certificate"]["passes_1561_over_200"] is True


def test_hankel_target_sanity():
    summary = load(REPRO / "hankel_independent" / "summary.json")
    assert summary["status"] == "HANKEL_AUDIT_PASS"
    assert summary["independently_checked"] == 184
    assert summary["target_survives"] is True


def test_story_figure_data_complete():
    metadata = load(TASK49 / "figure_data" / "metadata.json")
    assert metadata["status"] == "TASK49_STORY_DATA_READY"
    assert len(metadata["datasets"]) == 6


def test_manuscript_freeze():
    root = RESEARCH.parent
    result = subprocess.run(
        ["git", "diff", "--quiet", BASELINE, "--", "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh"],
        cwd=root,
        check=False,
    )
    assert result.returncode == 0


def test_no_existing_theorem_statement_modified():
    root = RESEARCH.parent
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=MDR", BASELINE, "--", "research/proofs"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    changed = [line for line in result.stdout.splitlines() if line]
    # Later tasks may add their own proof directories.  This Task 49 freeze
    # guard only rejects modifications, deletions, and renames of pre-existing
    # proof artifacts outside Task 49.
    assert all(line.startswith("research/proofs/task49/") for line in changed)
