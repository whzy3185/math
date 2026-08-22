"""Build the machine-readable Task 49 story and figure datasets."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any

from target_a_task47_common import sha256, write_json


RESEARCH = Path(__file__).resolve().parents[1]
TASK49 = RESEARCH / "experiments" / "task49"
OUTPUT = TASK49 / "figure_data"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def threshold_data() -> int:
    rows = read_csv(TASK49 / "threshold_crossings" / "threshold_crossings.csv")
    write_csv(OUTPUT / "figure1_threshold_crossings.csv", rows)
    return len(rows)


def localization_data() -> int:
    rows = []
    for family, n in (("G6", 514), ("G10", 510)):
        source = TASK49 / "localization_robustness" / "raw" / f"{family.lower()}_n{n}.json"
        payload = json.loads(source.read_text(encoding="utf-8"))
        for item in payload["cell_norms"]:
            distance = abs(int(item["cell"]))
            norm = float(item["norm"])
            if item["cell"] and norm > 0:
                rows.append(
                    {
                        "family": family,
                        "n": n,
                        "side": "left" if item["cell"] < 0 else "right",
                        "signed_cell": item["cell"],
                        "distance_cells": distance,
                        "cell_l2_norm": norm,
                        "log_cell_l2_norm": math.log(norm),
                    }
                )
    write_csv(OUTPUT / "figure2_localization.csv", rows)
    return len(rows)


def splitting_data() -> int:
    source = read_csv(TASK49 / "interface_mechanism" / "two_interface_high_precision.csv")
    rows = []
    for item in source:
        delta = float(item["abs_Delta"])
        rows.append(
            {
                "n": item["n"],
                "alpha": item["alpha"],
                "separation_bulk_cells": item["separation_bulk_cells"],
                "opposite_tail_bulk_cells": item["opposite_tail_bulk_cells"],
                "abs_Delta": item["abs_Delta"],
                "log_abs_Delta": math.log(delta),
                "evidence_status": item["evidence_status"],
            }
        )
    write_csv(OUTPUT / "figure3_two_interface_splitting.csv", rows)
    return len(rows)


def residue_patterns() -> int:
    rows = [
        {"even_residue": "0 mod 8", "family": "period-eight bulk", "special_gaps": "none", "alpha": "endpoint selected by order"},
        {"even_residue": "2 mod 8", "family": "single gap-6", "special_gaps": "6", "alpha": "+1"},
        {"even_residue": "4 mod 16", "family": "symmetric two gap-6", "special_gaps": "6,6", "alpha": "-1"},
        {"even_residue": "12 mod 16", "family": "shifted two gap-6", "special_gaps": "6,6; one-cell offset", "alpha": "-1"},
        {"even_residue": "6 mod 8", "family": "single gap-10", "special_gaps": "10", "alpha": "+1"},
    ]
    write_csv(OUTPUT / "figure4_residue_patterns.csv", rows)
    return len(rows)


def waterfall_data() -> int:
    rows = [
        {"stage": 0, "label": "legal p=17,...,24 dihedral orbits", "remaining": 370100, "evidence_status": "EXACT_FINITE_DATA"},
        {"stage": 1, "label": "after exact moment exclusion", "remaining": 184, "evidence_status": "COMPUTER_ASSISTED_PROVED"},
        {"stage": 2, "label": "after exact Hankel hierarchy through m=5", "remaining": 1, "evidence_status": "COMPUTER_ASSISTED_PROVED"},
    ]
    write_csv(OUTPUT / "figure5_moment_hankel_waterfall.csv", rows)
    return len(rows)


def p24_data() -> int:
    payload = json.loads(
        (RESEARCH / "reproducibility" / "task49" / "p24_independent" / "summary.json").read_text(encoding="utf-8")
    )
    rows = []
    for item in payload["periods"]:
        rows.append(
            {
                key: item[key]
                for key in (
                    "period",
                    "legal_dihedral_orbits",
                    "represented_legal_words",
                    "moment",
                    "strict",
                    "equality",
                    "lower",
                    "unresolved",
                    "consumed",
                )
            }
        )
    write_csv(OUTPUT / "figure6_p17_p24_classification.csv", rows)
    return len(rows)


def run() -> dict[str, Any]:
    counts = {
        "threshold_crossing_rows": threshold_data(),
        "localization_rows": localization_data(),
        "splitting_rows": splitting_data(),
        "residue_pattern_rows": residue_patterns(),
        "waterfall_rows": waterfall_data(),
        "bounded_classification_rows": p24_data(),
    }
    metadata = {
        "status": "TASK49_STORY_DATA_READY",
        "datasets": {
            "figure1_threshold_crossings.csv": {
                "source": "threshold_crossings/threshold_crossings.csv",
                "units": "squared spectral radius",
                "evidence": "mixed numerical and exact-certified rows; see evidence_status",
            },
            "figure2_localization.csv": {
                "source": "localization_robustness/raw/g6_n514.json and g10_n510.json",
                "units": "period-eight cells and eigenvector L2 norm",
                "evidence": "numerical FP64 sparse A^2 profiles",
            },
            "figure3_two_interface_splitting.csv": {
                "source": "interface_mechanism/two_interface_high_precision.csv",
                "units": "period-eight cells and squared-level splitting",
                "evidence": "80/120/160-digit 4x4 finite-ring Evans roots",
            },
            "figure4_residue_patterns.csv": {
                "source": "Task 48A structural family definitions and Task 49 crossing atlas",
                "units": "residue and cyclic gap words",
                "evidence": "explicit constructions; eventual uniform theorem remains open",
            },
            "figure5_moment_hankel_waterfall.csv": {
                "source": "Task 49 independent p24 and Hankel audits",
                "units": "dihedral orbit count",
                "evidence": "exact integer computer-assisted verification",
            },
            "figure6_p17_p24_classification.csv": {
                "source": "reproducibility/task49/p24_independent/summary.json",
                "units": "dihedral orbit count",
                "evidence": "independent exact finite audit",
            },
        },
        "row_counts": counts,
        "script_sha256": sha256(Path(__file__)),
    }
    write_json(OUTPUT / "metadata.json", metadata)
    print(json.dumps({"status": metadata["status"], **counts}, indent=2))
    return metadata


if __name__ == "__main__":
    run()
