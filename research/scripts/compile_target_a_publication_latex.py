"""Compile and audit every Target A publication wrapper with Tectonic."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
PUB_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub"
WRAPPERS = {
    "generic": "main.tex",
    "anonymous": "main_anonymous.tex",
    "jgt": "main_jgt.tex",
    "sidma": "main_sidma.tex",
}


def find_tectonic() -> Path:
    configured = os.environ.get("TECTONIC")
    if configured and Path(configured).is_file():
        return Path(configured)
    on_path = shutil.which("tectonic")
    if on_path:
        return Path(on_path)
    candidates = sorted(
        (Path.home() / ".codex" / "plugins" / "cache").glob(
            "openai-bundled/latex/*/bin/tectonic"
        ),
        reverse=True,
    )
    if candidates:
        return candidates[0]
    raise RuntimeError("TECTONIC_NOT_FOUND")


def pdf_page_count(path: Path) -> int:
    pdfinfo = shutil.which("pdfinfo")
    if pdfinfo:
        result = subprocess.run(
            [pdfinfo, str(path)], check=True, capture_output=True, text=True
        )
        match = re.search(r"^Pages:\s+(\d+)$", result.stdout, flags=re.MULTILINE)
        if match:
            return int(match.group(1))
    data = path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page\b", data))


def compile_wrapper(tectonic: Path, variant: str, source_name: str) -> dict[str, object]:
    build_dir = PUB_DIR / "build" / variant
    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True)
    command = [
        str(tectonic),
        "-X",
        "compile",
        "--outdir",
        str(build_dir),
        "--outfmt",
        "pdf",
        "--keep-logs",
        "--keep-intermediates",
        "--print",
        "--untrusted",
        source_name,
    ]
    result = subprocess.run(command, cwd=PUB_DIR, capture_output=True, text=True)
    stem = Path(source_name).stem
    pdf_path = build_dir / f"{stem}.pdf"
    log_path = build_dir / f"{stem}.log"
    log = log_path.read_text(encoding="utf-8", errors="replace") if log_path.is_file() else ""
    chatter = result.stdout + "\n" + result.stderr
    if result.returncode or not pdf_path.is_file():
        raise RuntimeError(f"{variant.upper()}_BUILD_FAIL\n{chatter[-4000:]}")

    destination = PUB_DIR / ("main.pdf" if variant == "generic" else f"main_{variant}.pdf")
    shutil.copy2(pdf_path, destination)
    undefined_refs = len(re.findall(r"Reference `[^']+' .* undefined", log))
    undefined_citations = len(re.findall(r"Citation `[^']+' .* undefined", log))
    report = {
        "variant": variant,
        "source": source_name,
        "pdf": destination.name,
        "pdf_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "pages": pdf_page_count(destination),
        "exit_code": result.returncode,
        "overfull_boxes": len(re.findall(r"Overfull \\hbox", log)),
        "underfull_boxes": len(re.findall(r"Underfull \\hbox", log)),
        "undefined_references": undefined_refs,
        "undefined_citations": undefined_citations,
        "fatal_errors": len(re.findall(r"^! ", log, flags=re.MULTILINE)),
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keep-build-directories", action="store_true")
    args = parser.parse_args()
    tectonic = find_tectonic()
    reports = [compile_wrapper(tectonic, variant, source) for variant, source in WRAPPERS.items()]
    audit = {
        "status": "TARGET_A_PUBLICATION_BUILDS_PASS",
        "compiler": "tectonic",
        "compiler_version": subprocess.run(
            [str(tectonic), "--version"], check=True, capture_output=True, text=True
        ).stdout.strip(),
        "builds": reports,
    }
    (PUB_DIR / "build_audit.json").write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if not args.keep_build_directories:
        shutil.rmtree(PUB_DIR / "build")
    print("TARGET_A_PUBLICATION_BUILDS_PASS")
    for report in reports:
        print(
            f"{str(report['variant']).upper()}_BUILD_PASS:"
            f"pages={report['pages']}:overfull={report['overfull_boxes']}"
        )


if __name__ == "__main__":
    main()
