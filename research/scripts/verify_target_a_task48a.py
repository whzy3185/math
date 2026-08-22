"""Verify Task 48A evidence accounting and formal-manuscript freeze."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[1]
REPO = RESEARCH.parent
ROOT = RESEARCH / "experiments" / "task48a"
BASELINE = "60e2e1a24d8aa584dfafa8a451c1b436df368fc7"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def run() -> dict:
    frontier = load(ROOT / "p24_frontier" / "closure_summary.json")
    interface = load(ROOT / "interface" / "summary.json")
    mod16 = load(ROOT / "two_interface" / "summary.json")
    residue = load(ROOT / "residue12" / "summary.json")
    moment = load(ROOT / "moment_matrix" / "summary.json")
    remaining = load(ROOT / "p24_frontier" / "remaining_59.json")
    assert remaining["count"] == 59 and remaining["counts_by_period"] == {"22": 11, "23": 14, "24": 34}
    assert frontier["status"] == "P24_EXACT_FRONTIER_CLOSED"
    assert frontier["GT_survivors"] == 183 and frontier["EQ_survivors"] == 1
    assert frontier["LT_survivors"] == frontier["UNRESOLVED_survivors"] == 0
    assert interface["INTERFACE_THEOREM_SIGNAL"] == "STRONG"
    assert float(interface["constants"]["G6"]["R_squared"]) < 8
    assert float(interface["constants"]["G10"]["R_squared"]) < 8
    assert all(row["classification"] == "INTERFACE_FLOQUET_SIGNAL_STRONG" for row in interface["floquet"].values())
    assert mod16["MOD16_INTERFACE_SIGNAL"] == "STRONG"
    assert residue["status"] == "RESIDUE12_STABLE_C_LT_8_FAMILY"
    assert residue["exact_counterexamples"] == 29 and residue["all_exact_certificates_pass"] is True
    assert moment["cumulative_exact_exclusions"] == {"2": 1, "3": 145, "4": 180, "5": 183}
    assert moment["MOMENT_MATRIX_VALUE"] == "HIGH"
    diff = subprocess.run(
        ["git", "diff", "--name-only", BASELINE, "--", "research/paper/manuscript_tex_pub", "research/paper/manuscript_tex_pub_zh"],
        cwd=REPO,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    assert not diff
    return {
        "status": "TARGET_A_TASK48A_VERIFICATION_PASS",
        "manuscript_changed": False,
        "remaining_59_resolved": frontier["remaining_resolved"],
        "interface_signal": interface["INTERFACE_THEOREM_SIGNAL"],
        "residue12_exact_counterexamples": residue["exact_counterexamples"],
        "moment_m5_exact_exclusions": moment["cumulative_exact_exclusions"]["5"],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
