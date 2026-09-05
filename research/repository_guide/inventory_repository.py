#!/usr/bin/env python3
"""Mechanical inventory, not a proof verifier or a literature-reading receipt.

Reads every tracked file in the selected checkout, validates JSON syntax,
indexes all Markdown headings and potentially stale status labels, and records
all local/tracking branch tips without changing branches or other worktrees.
Generated CSV/JSON files are reproducible navigation artifacts.
"""

import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
from collections import Counter


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode().strip()


def family(path):
    if path.startswith('research/generalization/circulant_1s/extension_20260905/'):
        return 'current_even_jump'
    if path.startswith('research/paper_strengthening/manuscript_period8_jgt/'):
        return 'frozen_period8_manuscript'
    if path.startswith('research/paper_strengthening/reference_library/') or path.startswith('research/related_work/'):
        return 'literature'
    if path.startswith('research/paper_strengthening/'):
        return 'period8_strengthening'
    if path.startswith('research/generalization/'):
        return 'general_jump_historical_foundation'
    if path.startswith('formal/'):
        return 'formal_kernel'
    if path.startswith('research/paper/'):
        return 'historical_paper_packages'
    if path.startswith('research/analytic_inventory/') or path.startswith('research/proof_closure/'):
        return 'historical_analytic_program'
    if path.startswith('research/proofs/') or path.startswith('research/discovery/'):
        return 'historical_theorems_and_exploration'
    if path.startswith('research/logs/') or path.startswith('research/experiments/'):
        return 'historical_logs_and_experiments'
    if path.startswith('research/scripts/') or path.startswith('research/reproducibility/') or path.startswith('research/audit/'):
        return 'code_and_evidence'
    if path.startswith('research/repository_guide/') or path == 'README.md':
        return 'current_navigation'
    return 'other_research_records'


def write_csv(name, fields, rows):
    with (OUT/name).open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    paths = sorted(p for p in paths if p)
    # The guide itself is omitted to avoid inventory self-hashes and churn.
    population = [p for p in paths if not p.startswith('research/repository_guide/')]
    files, docs, errors = [], [], []
    json_count = text_count = byte_count = 0
    for name in population:
        path = ROOT/name
        raw = path.read_bytes()
        byte_count += len(raw)
        kind = family(name)
        content = None
        if b'\0' not in raw:
            try:
                content = raw.decode('utf-8')
                text_count += 1
            except UnicodeDecodeError:
                pass
        syntax = 'not_applicable'
        if path.suffix == '.json':
            try:
                json.loads(raw)
                syntax = 'json_valid'
                json_count += 1
            except (ValueError, UnicodeDecodeError) as exc:
                syntax = 'json_invalid'
                errors.append({'file': name, 'error': str(exc)})
        files.append({'path': name, 'family': kind, 'bytes': len(raw),
                      'sha256': hashlib.sha256(raw).hexdigest(),
                      'format': path.suffix or 'none', 'syntax': syntax,
                      'review_level': 'mechanical_inventory_only'})
        if path.suffix.lower() == '.md' and content is not None:
            headings = re.findall(r'^#{1,3}\s+(.+)', content, re.M)
            signals = []
            for number, line in enumerate(content.splitlines(), 1):
                if re.search(r'CANONICAL_CURRENT|MANUSCRIPT_READY|Current stage|当前阶段|current editorial authority|next authorized|final readiness|no .*remaining|all .*complete', line, re.I):
                    signals.append(f'{number}:{line[:180]}')
            docs.append({'path': name, 'family': kind,
                         'heading_count': len(headings), 'headings': ' | '.join(headings),
                         'historical_status_signals': ' | '.join(signals),
                         'reading_status': 'headings_and_status_scan_not_full_semantic_review'})
    refs = git('for-each-ref', '--format=%(refname)\t%(objectname)', 'refs/heads', 'refs/remotes/origin').splitlines()
    branches = []
    for row in refs:
        ref, sha = row.split('\t')
        if ref.endswith('/HEAD'):
            continue
        entries = git('ls-tree', '-r', '--name-only', sha).splitlines()
        unique = git('diff', '--name-status', 'HEAD...'+sha).splitlines()
        branches.append({'ref': ref, 'commit': sha, 'tracked_files': len(entries),
                         'commits_not_in_active': int(git('rev-list', '--count', 'HEAD..'+sha)),
                         'unique_side_changed_paths': unique,
                         'content_review': 'tree_and_history_inventory_only'})
    write_csv('FILE_MANIFEST.csv', list(files[0]), files)
    write_csv('DOCUMENT_CATALOG.csv', list(docs[0]), docs)
    summary = {'snapshot_commit': git('rev-parse', 'HEAD'),
               'active_branch': git('branch', '--show-current'),
               'working_tree_status': git('status', '--short'),
               'population': 'all tracked files excluding research/repository_guide; generated inventory does not hash itself',
               'files': len(files), 'bytes_read': byte_count, 'utf8_text_files': text_count,
               'markdown_documents': len(docs), 'valid_json_files': json_count, 'json_errors': errors,
               'files_by_family': dict(sorted(Counter(x['family'] for x in files).items())),
               'bytes_by_family': dict(sorted((f, sum(x['bytes'] for x in files if x['family']==f)) for f in {x['family'] for x in files})),
               'branches': branches,
               'coverage_limit': 'Tracked working-tree bytes are hashed; snapshot_commit identifies the Git base, not a guarantee that every working file matches it. All inventory bytes read; JSON syntax and Markdown headings indexed. Not a re-proof of all claims or a semantic reading of every log/certificate.'}
    (OUT/'INVENTORY_SUMMARY.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({k: summary[k] for k in ('snapshot_commit','files','bytes_read','markdown_documents','valid_json_files','json_errors','files_by_family')}, indent=2))


if __name__ == '__main__':
    main()
