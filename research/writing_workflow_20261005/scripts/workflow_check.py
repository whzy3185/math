#!/usr/bin/env python3
"""Conservative integrity/readiness linter. This is NOT a mathematical proof checker.
No network, no execution of manuscript scripts, no mutation of paper inputs.
Exit 0: checks passed; 2: blocked or invalid. JSON output is always explicit.
"""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess, sys
from pathlib import Path, PurePosixPath
import importlib.util
_link_spec=importlib.util.spec_from_file_location("readiness_links",Path(__file__).with_name("readiness_links.py"))
_link_mod=importlib.util.module_from_spec(_link_spec);_link_spec.loader.exec_module(_link_mod)
check_links=_link_mod.check_links

KINDS = {"Observed", "finiteVerified", "analyticProved", "computerAssistedProved", "PublishedEstablished"}
ROLES = {"manuscript_source", "manuscript_pdf", "bibliography", "figure", "code", "data", "instructions", "provenance", "dependency_configuration"}
STAGES = [f"S{i:02d}" for i in range(0,16)]
TEXT_EXT = {".txt", ".md", ".tex", ".bib", ".json", ".py", ".cpp", ".h", ".hpp", ".c", ".lean", ".toml", ".yaml", ".yml", ".sh", ".csv", ".svg", ".sty", ".cls"}
BAD_NAME = re.compile(r"(?:^|[/_.-])(referee|reviewer|verdict|response|handoff|qa_report|publication_manifest|review_registry|review_report|exposure_log)(?:$|[/_.-])", re.I)
BAD_TEXT = [
 ("status_metadata", re.compile(r'\b(?:verified_via|prior_verdict|review_status|acceptance_status|readiness_status)\b', re.I)),
 ("historical_verdict", re.compile(r'(?:independent\s+(?:manuscript\s+)?(?:review|audit|integration)|visual\s+QA)\s*[:=]?\s*(?:PASS|ACCEPTED|APPROVED)', re.I)),
 ("readiness_verdict", re.compile(r'\b(?:ready\s+for\s+(?:submission|publication|isolated\s+second\s+review)|referee\s+(?:approved|accepted)|old\s+verdict)\b', re.I)),
]
HASH_RE = re.compile(r"[0-9a-f]{64}\Z")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def safe_file(root, rel):
    if not isinstance(rel, str) or not rel or "\\" in rel:
        raise ValueError("path must be nonempty POSIX relative text")
    p = PurePosixPath(rel)
    if p.is_absolute() or any(v in {"..", "."} for v in p.parts):
        raise ValueError("absolute/traversal path forbidden")
    q = root / p
    if any(v.is_symlink() for v in [q, *q.parents] if v != root.parent):
        raise ValueError("symlinks forbidden")
    if not q.resolve().is_relative_to(root.resolve()):
        raise ValueError("path escapes root")
    if not q.is_file():
        raise ValueError("missing regular file")
    return q


def evidence(items, root, errors, label):
    if not isinstance(items, list) or not items:
        errors.append(f"{label}: missing evidence")
        return
    for row in items:
        try:
            if not isinstance(row, dict):
                raise ValueError("evidence row must be object")
            p = safe_file(root, row["path"])
            if not HASH_RE.fullmatch(row.get("sha256", "")) or sha(p) != row["sha256"]:
                raise ValueError("hash mismatch or invalid digest")
        except (KeyError, ValueError, OSError) as exc:
            errors.append(f"{label}: {row!r}: {exc}")


def packet_check(root):
    root = Path(root).resolve()
    errors, warnings, scanned = [], [], []
    try:
        manifest_path = safe_file(root, "packet.json")
        m = load(manifest_path)
        errors.extend(_link_mod._guard.check_named(m,"packet.schema.json"))
        for rule, pattern in BAD_TEXT:
            if pattern.search(json.dumps(m)): errors.append("packet.json: status/history metadata: "+rule)
        pid=m.get("packet_id", "")
        if not isinstance(pid,str) or not re.fullmatch(r"[a-z0-9][a-z0-9_.-]{0,99}",pid) or re.search(r"(?:^|[_-])(review|verdict|accepted|approved|pass|proved|ready)(?:$|[_-])",pid):
            errors.append("packet_id must be a neutral lowercase identifier, without verdict/history terms")
        files = m["files"]
        if not isinstance(files, list) or not files:
            raise ValueError("empty input inventory")
        if not all(isinstance(row,dict) for row in files):
            raise ValueError("every inventory row must be an object")
        names = [r.get("path") for r in files]
        if len(names) != len(set(names)):
            errors.append("duplicate inventory path")
        actual = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()}
        expected = set(names) | {"packet.json"}
        if actual != expected:
            errors.append(f"inventory mismatch: extra={sorted(actual-expected)}, missing={sorted(expected-actual)}")
        for p in root.rglob("*"):
            if p.is_symlink():
                errors.append(f"symlink forbidden: {p.relative_to(root)}")
        for r in files:
            name = r.get("path", "")
            if set(r) != {"path", "sha256", "role"} or r.get("role") not in ROLES:
                errors.append(f"{name}: unexpected inventory metadata/role")
            try:
                p = safe_file(root, name)
                if not HASH_RE.fullmatch(r.get("sha256", "")) or sha(p) != r["sha256"]:
                    errors.append(f"{name}: input digest mismatch")
                if BAD_NAME.search(name):
                    errors.append(f"{name}: status/history-bearing filename")
                if p.suffix.lower() == ".pdf":
                    proc = subprocess.run(["pdftotext", "-layout", str(p), "-"], capture_output=True, text=True, timeout=45)
                    if proc.returncode:
                        raise ValueError("PDF text extraction failed")
                    content = proc.stdout
                    # PDF metadata is part of what a reviewer can see.
                    info = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True, timeout=30)
                    if info.returncode:
                        raise ValueError("PDF metadata extraction failed")
                    content += "\n" + info.stdout
                elif p.suffix.lower() in TEXT_EXT or p.name in {"lean-toolchain", "INPUT_SHA256SUMS", "SHA256SUMS"}:
                    content = p.read_text(encoding="utf-8")
                else:
                    warnings.append(f"{name}: binary/manual visual and metadata inspection required")
                    content = ""
                if p.suffix.lower() == ".json":
                    try:
                        payload = json.loads(content)
                        def metadata_keys(value, trail=""):
                            if isinstance(value, dict):
                                for key, val in value.items():
                                    if key.lower() in {"status", "verdict", "success", "passed", "recommendation", "verified_via", "outcome", "review_status", "acceptance_status"}:
                                        errors.append(f"{name}: status/result JSON key {trail+key!r}")
                                    metadata_keys(val, trail+key+".")
                            elif isinstance(value, list):
                                for n, val in enumerate(value): metadata_keys(val, trail+str(n)+".")
                        metadata_keys(payload)
                    except ValueError:
                        errors.append(f"{name}: invalid JSON input")
                for rule, pattern in BAD_TEXT:
                    match = pattern.search(content)
                    if match:
                        errors.append(f"{name}: {rule}: {match.group(0)!r}")
                scanned.append(name)
            except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
                errors.append(f"{name}: {exc}")
        return {"mode":"packet", "packet_id":m.get("packet_id"), "packet_manifest_sha256":sha(manifest_path),
                "lint_pass":not errors, "mathematical_correctness":"not_assessed", "blind_context_verified":False,
                "manual_attestations_required":["whole packet and linked-source exposure inspection", "new context and no inherited history", "reviewer exposure log"],
                "scanned_files":scanned, "errors":errors, "warnings":warnings}
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        return {"mode":"packet", "lint_pass":False, "errors":[str(exc)], "warnings":warnings}


def claims_check(rows, root, errors):
    if not isinstance(rows, list) or not rows:
        errors.append("claim ledger empty")
        return
    ids = [r.get("id") for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("duplicate claim IDs")
    adjacency = {}
    for c in rows:
        ident = c.get("id", "?")
        for key in ["id", "statement", "hypotheses", "quantifiers", "dependencies", "evidence_kind", "verification_state", "novelty_status", "scope_exclusions", "formal_coverage"]:
            if key not in c or (isinstance(c[key], str) and not c[key].strip()):
                errors.append(f"claim {ident}: missing {key}")
        if c.get("verification_state") not in {"unreviewed", "audited", "disputed", "blocked"}:
            errors.append(f"claim {ident}: unknown verification state")
        if c.get("formal_coverage") not in {"unformalized", "partial", "formalized"}:
            errors.append(f"claim {ident}: unknown formal coverage")
        if c.get("evidence_kind")=="PublishedEstablished" and c.get("publication_status")!="published":
            errors.append(f"claim {ident}: published evidence category conflicts with publication status")
        if c.get("evidence_kind") not in KINDS:
            errors.append(f"claim {ident}: unknown evidence category")
        deps = c.get("dependencies", [])
        adjacency[ident] = deps
        for dep in deps:
            if dep not in ids:
                errors.append(f"claim {ident}: unknown dependency {dep}")
        evidence(c.get("evidence", []), root, errors, f"claim {ident}")
        if c.get("evidence_kind") in {"finiteVerified", "computerAssistedProved"} and not c.get("finite_domain"):
            errors.append(f"claim {ident}: finite domain missing")
        if c.get("evidence_kind") == "PublishedEstablished" and not c.get("primary_publication"):
            errors.append(f"claim {ident}: publication locator missing")
        if c.get("novelty_status") == "proved_novel":
            errors.append(f"claim {ident}: novelty is not certified by a negative search")
    visiting, done = set(), set()
    def visit(i):
        if i in visiting:
            errors.append(f"claim dependency cycle through {i}")
            return
        if i in done: return
        visiting.add(i)
        for j in adjacency.get(i, []): visit(j)
        visiting.remove(i); done.add(i)
    for i in ids: visit(i)


def readiness_check(path):
    path=Path(path).resolve(); root=path.parent
    errors, blockers = [], []
    try:
        r = load(path)
        for k in ["schema_version", "paper", "version", "recorded_utc", "gates", "claims", "review_contexts", "blockers"]:
            if k not in r: errors.append(f"missing field {k}")
        if r.get("schema_version") != "1.0": errors.append("unsupported schema version")
        claims_check(r.get("claims"), root, errors)
        pdf=r.get("input_pdf")
        if not isinstance(pdf,dict): blockers.append("Input PDF is not bound to a readable frozen file")
        else:
            evidence([pdf], root, errors, "input PDF")
            if pdf.get("sha256") != r.get("pdf_sha256"): errors.append("Input PDF digest differs from stated pdf_sha256")
        sources=r.get("input_sources")
        if not sources: blockers.append("Frozen source inventory missing")
        else: evidence(sources,root,errors,"input sources")
        gates=r.get("gates", [])
        ids=[g.get("id") for g in gates]
        if sorted(ids) != STAGES: errors.append("exactly one S00 through S15 gate required")
        for g in gates:
            key=g.get("id", "?"); state=g.get("status")
            if state not in {"pass", "pending", "blocked", "not_applicable"}:
                errors.append(f"{key}: invalid status")
            if state in {"pending", "blocked"}: blockers.append(f"{key}: {g.get('notes', state)}")
            if state == "pass":
                if g.get("version") != r.get("version"): errors.append(f"{key}: stale version attestation")
                if not g.get("owner") or not g.get("acceptance"): errors.append(f"{key}: owner/acceptance missing")
                evidence(g.get("evidence", []), root, errors, key)
            if state == "not_applicable":
                if key != "S12" or not g.get("justification") or not g.get("approved_by"):
                    errors.append(f"{key}: unjustified not-applicable gate")
        for c in r.get("review_contexts", []):
            for key in ["context_id","reviewer_id","editor_id","reviewed_version"]:
                if not isinstance(c.get(key),str) or not c[key].strip(): errors.append("Missing/empty review identity: "+key)
            if c.get("exposure_evidence"): evidence(c["exposure_evidence"],root,errors,"review exposure")
            n=c.get("rounds_used", 0)
            if not isinstance(n,int) or isinstance(n,bool) or n not in {1,2}: errors.append("review context must have one or two rounds")
            if n == 2 and not c.get("retired"): errors.append(f"{c.get('context_id')}: two-round context not retired")
            if c.get("reviewer_id") == c.get("editor_id"): errors.append("reviewer and revision editor must differ")
            if c.get("initial_inherited_history") is not False: errors.append("initial review inherited history or unknown")
            if c.get("exposure") not in {"clean", "contaminated_disclosed"}: errors.append("missing exposure disposition")
            if c.get("exposure") == "contaminated_disclosed" and not c.get("replacement_context_id"):
                blockers.append(f"{c.get('context_id')}: clean replacement context still required")
        # A passed review gate must explicitly identify a clean, current-version context.
        byid={g.get("id"):g for g in gates}
        for key in ["S09", "S11"]:
            if byid.get(key, {}).get("status") == "pass":
                wanted=byid[key].get("review_context_id")
                match=[c for c in r.get("review_contexts", []) if c.get("context_id")==wanted and (key=="S11" or c.get("exposure")=="clean") and c.get("reviewed_version")==r.get("version")]
                if not match: errors.append(f"{key}: no appropriately exposed context bound to current version")
        if byid.get("S08", {}).get("status") == "pass" and any(c.get("verification_state") != "audited" for c in r.get("claims", [])):
            errors.append("S08: passed audit gate includes unreviewed/disputed/blocked claims")
        if byid.get("S12", {}).get("status") == "not_applicable" and any(c.get("formal_coverage") != "unformalized" for c in r.get("claims", [])):
            errors.append("S12: formalization claimed but gate marked not applicable")
        if byid.get("S15", {}).get("status") == "pass":
            for key in ["authors_confirmed", "journal_selected", "consent_confirmed", "disclosures_checked"]:
                if r.get("submission", {}).get(key) is not True: errors.append(f"submission: {key} not confirmed")
            if r.get("submission", {}).get("automatic_submission") is not False: errors.append("automatic submission must be disabled")
        check_links(r,root,errors,blockers)
        blockers += [str(b) for b in r.get("blockers", [])]
        return {"mode":"readiness", "paper":r.get("paper"), "version":r.get("version"), "record_valid":not errors,
                "technical_gates_recorded_closed":not errors and not any(b.startswith("Integrated record missing") for b in blockers) and all(byid.get(i, {}).get("status") in {"pass","not_applicable"} for i in STAGES[1:-1]),
                "venue_policy_compatible":not errors and not any(b.startswith("Integrated record missing") for b in blockers) and byid.get("S00", {}).get("status")=="pass",
                "ready_for_human_submission_decision":not errors and not blockers, "publication_authorized":False,
                "mathematical_correctness":"not_decided_by_this_program", "readiness_semantics":"Administrative evidence completeness only; human mathematical/policy/consent attestations are not independently authenticated by this program", "automatic_submission":False,
                "errors":errors, "blockers":blockers}
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        return {"mode":"readiness", "record_valid":False, "ready_for_human_submission_decision":False, "errors":[str(exc)]}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", choices=["packet", "readiness"]); p.add_argument("path")
    p.add_argument("--output", help="Write report to a separate output file; must not be inside a packet")
    a=p.parse_args()
    if a.output and a.mode=="packet" and Path(a.output).resolve().is_relative_to(Path(a.path).resolve()):
        p.error("scanner report must stay outside blind packet")
    out=packet_check(a.path) if a.mode=="packet" else readiness_check(a.path)
    content=json.dumps(out, indent=2, ensure_ascii=False)+"\n"
    if a.output: Path(a.output).write_text(content, encoding="utf-8")
    print(content, end="")
    ok=out.get("lint_pass", out.get("ready_for_human_submission_decision", False))
    return 0 if ok else 2

if __name__=="__main__": sys.exit(main())
