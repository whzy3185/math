"""Compile and audit the independent Chinese Target A manuscript."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from compile_target_a_publication_latex import find_tectonic, pdf_page_count


RESEARCH_ROOT = Path(__file__).resolve().parents[1]
PUB_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub_zh"
ENGLISH_PUB_DIR = RESEARCH_ROOT / "paper" / "manuscript_tex_pub"


def compile_chinese_manuscript() -> dict[str, object]:
    tectonic = find_tectonic()
    with tempfile.TemporaryDirectory(prefix="target-a-zh-") as temporary:
        build_dir = Path(temporary)
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
            "main.tex",
        ]
        result = subprocess.run(command, cwd=PUB_DIR, capture_output=True, text=True)
        built_pdf = build_dir / "main.pdf"
        log_path = build_dir / "main.log"
        log = (
            log_path.read_text(encoding="utf-8", errors="replace")
            if log_path.is_file()
            else ""
        )
        if result.returncode or not built_pdf.is_file():
            chatter = result.stdout + "\n" + result.stderr
            raise RuntimeError(f"TARGET_A_CHINESE_BUILD_FAIL\n{chatter[-4000:]}")
        destination = PUB_DIR / "main.pdf"
        shutil.copy2(built_pdf, destination)

    english_pdf = ENGLISH_PUB_DIR / "main.pdf"
    report = {
        "status": "TARGET_A_CHINESE_PUBLICATION_BUILD_PASS",
        "compiler": "tectonic",
        "compiler_version": subprocess.run(
            [str(tectonic), "--version"], check=True, capture_output=True, text=True
        ).stdout.strip(),
        "source": "main.tex",
        "pdf": "main.pdf",
        "pdf_sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "pages": pdf_page_count(destination),
        "page_format": "A4",
        "exit_code": result.returncode,
        "overfull_boxes": len(re.findall(r"Overfull \\hbox", log)),
        "underfull_boxes": len(re.findall(r"Underfull \\hbox", log)),
        "undefined_references": len(
            re.findall(r"Reference `[^']+' .* undefined", log)
        ),
        "undefined_citations": len(
            re.findall(r"Citation `[^']+' .* undefined", log)
        ),
        "fatal_errors": len(re.findall(r"^! ", log, flags=re.MULTILINE)),
        "english_source_pdf_sha256": hashlib.sha256(english_pdf.read_bytes()).hexdigest(),
    }
    (PUB_DIR / "build_audit.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report


def main() -> None:
    report = compile_chinese_manuscript()
    print(report["status"])
    print(
        f"CHINESE_BUILD_PASS:pages={report['pages']}:"
        f"overfull={report['overfull_boxes']}:format={report['page_format']}"
    )


if __name__ == "__main__":
    main()
