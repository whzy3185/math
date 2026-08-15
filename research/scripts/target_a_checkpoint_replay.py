"""Read-only replay audit for Target A minimality-search checkpoints."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from target_a_minimality_search import (
    _load_and_validate_chunks,
    _replay_checkpoint_inputs,
    expected_search_space,
)


RESEARCH_ROOT = Path(__file__).resolve().parents[1]


def replay_saved_search(n: int, research_root: Path = RESEARCH_ROOT) -> dict[str, Any]:
    result_path = research_root / "logs" / f"target_a_search_n{n}.json"
    checkpoint_dir = research_root / "logs" / "checkpoints" / f"n{n}"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    expected = expected_search_space(n)
    baseline = result.get("baseline_git_commit", result.get("git_commit"))
    chunks = _load_and_validate_chunks(
        checkpoint_dir, n, baseline, expected["shell_counts"]
    )
    states, input_digest = _replay_checkpoint_inputs(n, chunks)
    certificate_digest = hashlib.sha256()
    for chunk in chunks:
        certificate_digest.update(bytes.fromhex(chunk["ordered_certificate_sha256"]))

    shell_counts = {
        defect_count: sum(
            chunk["completed_q_bracelets"]
            for chunk in chunks
            if chunk["defect_count"] == defect_count
        )
        for defect_count in expected["shell_counts"]
    }
    final_chain = result.get(
        "final_checkpoint_chain_sha256",
        result.get("checkpoint_final_chain_sha256"),
    )
    checks = {
        "chunk_count": len(chunks) == result["checkpoint_chunks"],
        "generator_cursor_exhausted": next(states, None) is None,
        "shell_counts": shell_counts == expected["shell_counts"],
        "completed_q_bracelets": sum(
            chunk["completed_q_bracelets"] for chunk in chunks
        )
        == result["completed_q_bracelets"]
        == expected["q_bracelets"],
        "completed_spectral_states": sum(
            chunk["completed_states"] for chunk in chunks
        )
        == result["completed_spectral_states"]
        == expected["spectral_states"],
        "represented_q_vectors": sum(
            chunk["represented_q_vectors"] for chunk in chunks
        )
        == result["represented_q_vectors"]
        == expected["q_vectors"],
        "ordered_input_sha256": input_digest.hexdigest()
        == result["ordered_input_sha256"],
        "ordered_certificate_sha256": certificate_digest.hexdigest()
        == result["ordered_certificate_sha256"],
        "final_chain_sha256": chunks[-1]["chain_sha256"] == final_chain,
        "optimizer_exact_check": any(
            chunk.get("optimizer_exact_check") for chunk in chunks
        )
        and result.get("optimizer_exact_check") is not None,
        "exact_fallbacks": sum(chunk["exact_fallbacks"] for chunk in chunks)
        == result["exact_fallbacks"],
        "zero_counterexamples": sum(chunk["counterexamples"] for chunk in chunks)
        == len(result["counterexamples"])
        == 0,
    }
    return {
        "n": n,
        "result_status": result["status"],
        "checkpoint_chunks": len(chunks),
        "checks": checks,
        "status": "PASS" if all(checks.values()) else "CHECKPOINT_REPLAY_FAIL",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, nargs="+", required=True)
    args = parser.parse_args()
    reports = [replay_saved_search(n) for n in args.n]
    payload = {
        "method": "read-only direct-stream cursor and checkpoint hash-chain replay",
        "reports": reports,
        "status": "PASS" if all(item["status"] == "PASS" for item in reports) else "FAIL",
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    raise SystemExit(0 if payload["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
