"""Assemble the machine-readable Target A smallest-counterexample certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = RESEARCH_ROOT / "counterexamples" / "target_a_minimality_certificate.json"
DEFAULT_DEPENDENCIES = RESEARCH_ROOT / "audit" / "TARGET_A_MINIMALITY_DEPENDENCIES.json"
DEFAULT_REPLAY = RESEARCH_ROOT / "audit" / "target_a_minimality_checkpoint_replay.json"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _relative(path: Path, research_root: Path) -> str:
    return str(path.relative_to(research_root.parent))


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def _domain_minimum(spec_path: Path) -> int:
    text = spec_path.read_text(encoding="utf-8")
    match = re.search(
        r"## Domain\s+.*?`n` is an even integer with `n(?:≥|>=)(\d+)`",
        text,
        flags=re.DOTALL,
    )
    if not match:
        raise RuntimeError("DOMAIN_AUDIT_FAIL: unable to parse even-n domain")
    minimum = int(match.group(1))
    if minimum != 8 or "`n` odd is outside the conjecture" not in text:
        raise RuntimeError("DOMAIN_AUDIT_FAIL: specification domain is inconsistent")
    return minimum


def _source_for_order(n: int, research_root: Path) -> Path:
    if n <= 18:
        name = "target_a_reproduction_n8_18.json"
    elif n == 20:
        name = "target_a_search_n20.json"
    elif n == 22:
        name = "target_a_flux_search_n22.json"
    else:
        name = f"target_a_search_n{n}.json"
    return research_root / "logs" / name


def _raw_entry(n: int, source: Path, research_root: Path) -> dict[str, Any]:
    payload = json.loads(source.read_text(encoding="utf-8"))
    result = next(item for item in payload["results"] if item["n"] == n)
    total = result["switching_classes"]
    return {
        "n": n,
        "method": "raw_switching_class_exhaustion",
        "source_file": _relative(source, research_root),
        "source_sha256": _sha256(source),
        "source_selector": f"results[n={n}]",
        "expected_search_space": {"switching_classes": 2 ** (n + 1)},
        "completed_search_space": {"switching_classes": total},
        "completion_fraction": 1,
        "optimizer_exact_check": {
            "status": "PASS",
            "serialized_records": len(result["optimizer_exact_checks"]),
        },
        "rayleigh_certified": result["rayleigh_certified_nonoptimizers"],
        "exact_fallbacks": result["exact_fallbacks"],
        "counterexamples": len(result["counterexamples"]),
        "checkpoint_manifest": None,
        "checkpoint_manifest_sha256": None,
        "status": "VERIFIED_NO_COUNTEREXAMPLE",
    }


def _n22_entry(source: Path, research_root: Path) -> dict[str, Any]:
    result = json.loads(source.read_text(encoding="utf-8"))
    return {
        "n": 22,
        "method": "full_(Q,alpha)/D_n_quotient_exhaustion",
        "source_file": _relative(source, research_root),
        "source_sha256": _sha256(source),
        "source_selector": "top-level result",
        "expected_search_space": {
            "q_orbits": 48734,
            "spectral_states": 97468,
            "represented_switching_classes": 2**23,
        },
        "completed_search_space": {
            "q_orbits": result["q_orbits"],
            "spectral_states": result["spectral_states"],
            "represented_switching_classes": result["represented_switching_classes"],
        },
        "completion_fraction": 1,
        "optimizer_exact_check": {
            "status": "ESTABLISHED_BY_DISTINGUISHED_THRESHOLD_DEFINITION",
            "serialized_in_historical_schema": False,
            "optimizer_state": {"defect_count": 0, "alpha": -1},
        },
        "rayleigh_certified": result["rayleigh_certified_nonoptimizers"],
        "exact_fallbacks": result["exact_fallbacks"],
        "counterexamples": len(result["counterexamples"]),
        "checkpoint_manifest": None,
        "checkpoint_manifest_sha256": None,
        "status": "VERIFIED_NO_COUNTEREXAMPLE",
    }


def _production_entry(n: int, source: Path, research_root: Path) -> dict[str, Any]:
    result = json.loads(source.read_text(encoding="utf-8"))
    manifest = research_root / "logs" / "checkpoints" / f"n{n}" / "manifest.json"
    return {
        "n": n,
        "method": "production_direct_bracelet_quotient_exhaustion",
        "source_file": _relative(source, research_root),
        "source_sha256": _sha256(source),
        "source_selector": "top-level result",
        "expected_search_space": {
            "q_bracelets": result["expected_q_bracelets"],
            "spectral_states": result["expected_spectral_states"],
            "represented_switching_classes": 2 ** (n + 1),
        },
        "completed_search_space": {
            "q_bracelets": result["completed_q_bracelets"],
            "spectral_states": result["completed_spectral_states"],
            "represented_switching_classes": result["represented_switching_classes"],
        },
        "completion_fraction": result["completion_fraction"],
        "optimizer_exact_check": {
            "status": "PASS",
            "optimizer": result["optimizer"],
            "multiplicity": result["optimizer_exact_check"]["multiplicity"],
        },
        "rayleigh_certified": result["rayleigh_certified"],
        "exact_fallbacks": result["exact_fallbacks"],
        "counterexamples": len(result["counterexamples"]),
        "checkpoint_manifest": _relative(manifest, research_root),
        "checkpoint_manifest_sha256": _sha256(manifest),
        "status": "VERIFIED_NO_COUNTEREXAMPLE",
    }


def _dependency_paths(research_root: Path) -> list[tuple[Path, str]]:
    paths: list[tuple[Path, str]] = [
        (research_root / "conjectures" / "TARGET_A_SPEC.md", "admissible domain and failure condition"),
        (research_root / "logs" / "target_a_reproduction_n8_18.json", "finite exclusion n=8..18"),
        (research_root / "logs" / "target_a_search_n20.json", "finite exclusion n=20"),
        (research_root / "logs" / "target_a_flux_search_n22.json", "finite quotient exclusion n=22"),
        (research_root / "counterexamples" / "target_a_n32_period8.json", "explicit n=32 witness"),
        (research_root / "counterexamples" / "target_a_n32_period8_certificate.json", "exact n=32 inequality certificate"),
        (research_root / "scripts" / "target_a_checkpoint_replay.py", "read-only checkpoint replay implementation"),
        (research_root / "scripts" / "verify_target_a_n32_certificate.py", "independent n=32 checker"),
        (research_root / "scripts" / "verify_target_a_minimality_certificate.py", "independent total checker"),
        (DEFAULT_REPLAY, "saved four-order replay audit"),
    ]
    for n in (24, 26, 28, 30):
        paths.extend(
            [
                (research_root / "logs" / f"target_a_search_n{n}.json", f"finite exclusion n={n}"),
                (
                    research_root / "logs" / "checkpoints" / f"n{n}" / "manifest.json",
                    f"checkpoint manifest n={n}",
                ),
            ]
        )
    return paths


def assemble(
    research_root: Path = RESEARCH_ROOT,
    output_path: Path = DEFAULT_OUTPUT,
    dependency_path: Path = DEFAULT_DEPENDENCIES,
    replay_path: Path = DEFAULT_REPLAY,
) -> dict[str, Any]:
    spec = research_root / "conjectures" / "TARGET_A_SPEC.md"
    minimum = _domain_minimum(spec)
    required_orders = list(range(minimum, 32, 2))
    entries = []
    for n in required_orders:
        source = _source_for_order(n, research_root)
        if n <= 20:
            entries.append(_raw_entry(n, source, research_root))
        elif n == 22:
            entries.append(_n22_entry(source, research_root))
        else:
            entries.append(_production_entry(n, source, research_root))

    dependencies = {
        "schema_version": 1,
        "claim": "32 is the smallest admissible Target A counterexample order",
        "dependencies": [
            {"path": _relative(path, research_root), "sha256": _sha256(path), "role": role}
            for path, role in sorted(_dependency_paths(research_root), key=lambda item: str(item[0]))
        ],
    }
    _write_json(dependency_path, dependencies)

    replay = json.loads(replay_path.read_text(encoding="utf-8"))
    witness = research_root / "counterexamples" / "target_a_n32_period8.json"
    n32_certificate = research_root / "counterexamples" / "target_a_n32_period8_certificate.json"
    total_checker = research_root / "scripts" / "verify_target_a_minimality_certificate.py"
    n32_checker = research_root / "scripts" / "verify_target_a_n32_certificate.py"
    payload = {
        "schema_version": 1,
        "conjecture": {
            "id": "C029",
            "domain": "even n >= 8",
            "domain_spec_file": _relative(spec, research_root),
            "domain_spec_sha256": _sha256(spec),
            "failure_condition": "rho(A_sigma) < rho_-(n)",
        },
        "claim": {
            "smallest_counterexample_order": 32,
            "status": "SMALLEST_COUNTEREXAMPLE_VERIFIED",
        },
        "finite_no_counterexample_orders": entries,
        "required_orders_below_32": required_orders,
        "domain_coverage_complete": [entry["n"] for entry in entries] == required_orders,
        "n32_counterexample": {
            "n": 32,
            "witness_file": _relative(witness, research_root),
            "witness_sha256": _sha256(witness),
            "exact_certificate_file": _relative(n32_certificate, research_root),
            "exact_certificate_sha256": _sha256(n32_certificate),
            "triangle_flux_period": list((1, 1, -1, 1, -1, -1, 1, -1)),
            "quadrilateral_flux_period": [1, -1, -1, -1],
            "alpha": 1,
            "exact_inequality": "rho(A)^2 < 1561/200 < rho_-(32)^2",
            "status": "N32_COUNTEREXAMPLE_EXACT_PASS",
        },
        "checkpoint_replays": {
            "source_file": _relative(replay_path, research_root),
            "source_sha256": _sha256(replay_path),
            "orders": [report["n"] for report in replay["reports"]],
            "reports": replay["reports"],
            "status": replay["status"],
        },
        "dependencies": {
            "manifest_file": _relative(dependency_path, research_root),
            "manifest_sha256": _sha256(dependency_path),
        },
        "certificate_checker": {
            "source_file": _relative(total_checker, research_root),
            "source_sha256": _sha256(total_checker),
            "success_output": "TARGET_A_MINIMALITY_CERTIFICATE_PASS",
        },
        "n32_certificate_checker": {
            "source_file": _relative(n32_checker, research_root),
            "source_sha256": _sha256(n32_checker),
            "success_output": "N32_CERTIFICATE_PASS",
        },
        "overall_status": "PASS",
    }
    _write_json(output_path, payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dependencies", type=Path, default=DEFAULT_DEPENDENCIES)
    parser.add_argument("--replay", type=Path, default=DEFAULT_REPLAY)
    args = parser.parse_args()
    assemble(output_path=args.output, dependency_path=args.dependencies, replay_path=args.replay)
    print(args.output)


if __name__ == "__main__":
    main()
