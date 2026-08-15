"""Build the observed n=24/26/28 period-4 diagnostic from saved logs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from target_a_minimality_search import distance_to_period4_q_pattern


RESEARCH_ROOT = Path(__file__).resolve().parents[1]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _distance(item: dict[str, Any]) -> int:
    if "distance_to_period4_Q_pattern" in item:
        return int(item["distance_to_period4_Q_pattern"])
    return distance_to_period4_q_pattern(tuple(item["canonical_Q"]))


def _summary(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "canonical_q_code": item["canonical_q_code"],
        "alpha": item["alpha"],
        "defect_count": item["defect_count"],
        "distance_to_period4_Q_pattern": _distance(item),
        "numeric_rho_preview": item["numeric_rho_preview"],
        "numeric_gap_preview": item["numeric_gap_preview"],
    }


def build_diagnostic(research_root: Path = RESEARCH_ROOT) -> dict[str, Any]:
    entries = []
    for n in (24, 26, 28):
        path = research_root / "logs" / f"target_a_search_n{n}.json"
        result = json.loads(path.read_text(encoding="utf-8"))
        top = result["top_near_minimizers"]
        best = min(top, key=lambda item: item["numeric_rho_preview"])
        entry = {
            "n": n,
            "source": str(path.relative_to(research_root.parent)),
            "source_sha256": _sha256(path),
            "best_observed_nonoptimizer": _summary(best),
        }
        if n == 28:
            entry["best_observed_by_period4_distance"] = [
                _summary(item)
                for item in result["best_numeric_by_period4_distance"]
            ]
            if any(
                item["distance_to_period4_Q_pattern"] == 0
                for item in result["top_near_minimizers"]
            ):
                raise AssertionError("n=28 top diagnostics contain impossible distance 0")
        entries.append(entry)
    return {
        "schema_version": 1,
        "status": "OBSERVED_NUMERIC_DIAGNOSTIC",
        "claim_scope": "numeric ranking only; no exact extremal theorem",
        "entries": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_diagnostic()
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        temporary = args.output.with_suffix(args.output.suffix + ".tmp")
        temporary.write_text(text, encoding="utf-8")
        temporary.replace(args.output)
    print(text, end="")


if __name__ == "__main__":
    main()
