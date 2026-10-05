#!/usr/bin/env python3
"""Copy only an explicit hash-checked allowlist to a NEW packet directory.
No automatic sanitization: prepare neutral inputs explicitly, preserving originals.
Plan JSON: {packet_id, files:[{source, path, sha256, role}]}.
source paths are relative to --source-root; output paths are relative to --output.
"""
import argparse,json,shutil,sys
from pathlib import Path,PurePosixPath
from workflow_check import safe_file,sha,ROLES,packet_check
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('plan');p.add_argument('--source-root',required=True);p.add_argument('--output',required=True)
a=p.parse_args();src=Path(a.source_root).resolve();out=Path(a.output).resolve();plan=json.loads(Path(a.plan).read_text())
if out.exists():p.error('refusing to overwrite existing output')
rows=[];seen=set()
# Validate all source bytes and destination names before copying anything.
for f in plan['files']:
    source=safe_file(src,f['source']);rel=PurePosixPath(f['path'])
    if rel.is_absolute() or '..' in rel.parts or f['path'] in seen or f['path']=='packet.json' or '\\' in f['path']:
        p.error('unsafe or duplicate destination')
    if sha(source)!=f['sha256'] or f['role'] not in ROLES:p.error('source hash/role mismatch')
    seen.add(f['path']);rows.append((source,f))
out.mkdir(parents=True)
for source,f in rows:
    dest=out/f['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,dest)
inventory=[{k:f[k] for k in ['path','sha256','role']} for _,f in rows]
(out/'packet.json').write_text(json.dumps({'schema_version':'1.0','packet_id':plan['packet_id'],'files':inventory},indent=2)+'\n')
result=packet_check(out);print(json.dumps(result,indent=2));sys.exit(0 if result['lint_pass'] else 2)
