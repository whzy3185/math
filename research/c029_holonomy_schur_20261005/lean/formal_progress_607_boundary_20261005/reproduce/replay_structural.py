#!/usr/bin/env python3
"""Fresh bounded replay of the generic, typed, and boundary source profiles.
Uses only pinned third-party package caches and freshly produced project objects.
"""
import argparse, datetime, fcntl, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path
from validate_axioms import validate, tests

ROOT = Path(__file__).resolve().parents[1]
MODULES = ['C029OpenSchur', 'TargetA/R2TerminalSchur',
           'TargetA/R2RationalRecurrence', 'TargetA/R2GenericSchurBridge',
           'C029BoundaryIncidenceEstimate', 'C029InnerProductCrossEstimate',
           'C029AssembledQuadraticPositivity', 'C029FlattenedMatrixPosDef']
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--lean', default='lean', help='Official Lean 4.33.1 executable')
    p.add_argument('--cache-project', type=Path, default=ROOT/'dependencies',
                   help='Project containing the pinned .lake/packages cache')
    p.add_argument('--out', type=Path, default=ROOT/'.repro/structural')
    p.add_argument('--lock', type=Path, default=ROOT/'.repro/compiler.lock')
    p.add_argument('--timeout', type=int, default=90)
    args = p.parse_args()
    if args.timeout <= 0: p.error('timeout must be positive')
    if args.out.exists(): p.error('output path must be new; retain earlier failed evidence')
    args.lock.parent.mkdir(parents=True, exist_ok=True)
    lock = args.lock.open('a')
    try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError: sys.exit('compiler lock busy; no process started')
    version = subprocess.check_output([args.lean, '--version'], text=True).strip()
    if 'version 4.33.1,' not in version or '819816b2e0a3bf405af45ae5c7af2491d8f5bee6' not in version:
        sys.exit('Wrong compiler version: '+version)
    manifest = json.loads((ROOT/'dependencies/lake-manifest.json').read_text())
    cache = args.cache_project.resolve()/'.lake/packages'
    paths = []
    for package in manifest['packages']:
        folder = cache/package['name']
        if not folder.exists():
            if package['name'] == 'Cli': continue  # not imported by these modules
            sys.exit('Missing pinned package: '+package['name'])
        rev = subprocess.check_output(['git', '-C', str(folder), 'rev-parse', 'HEAD'], text=True).strip()
        if rev != package['rev']: sys.exit('Wrong dependency revision: '+package['name'])
        lib = folder/'.lake/build/lib/lean'
        if not lib.is_dir():
            if package['name'] == 'Cli': continue
            sys.exit('Missing dependency cache: '+package['name'])
        paths.append(str(lib))
    args.out.mkdir(parents=True)
    source = ROOT/'structural/src'
    before = {str(f.relative_to(source)):digest(f) for f in source.rglob('*.lean')}
    env = os.environ.copy()
    env['LEAN_PATH'] = os.pathsep.join([str(args.out.resolve())]+paths)
    report = {'status':'RUNNING','lean_version':version,'hard_wall_seconds_each':args.timeout,
              'third_party_cache_reused':True,'prior_project_objects_used':False,
              'source_sha256':before,'parser_selftests':tests(),'runs':[]}
    def save(): (args.out/'replay.json').write_text(json.dumps(report,indent=2)+'\n')
    save()
    for module in MODULES:
        src = source/(module+'.lean'); dest = args.out/module
        dest.parent.mkdir(parents=True,exist_ok=True)
        short_names = re.findall(r'^#print axioms (\S+)',src.read_text(),re.M)
        declared = set(json.loads((ROOT/'evidence/typed30_axioms.json').read_text())) | set(json.loads((ROOT/'evidence/structural37_axioms.json').read_text()))
        expected = []
        for name in short_names:
            candidates = [n for n in declared if n == name or n.endswith('.'+name)]
            if len(candidates) != 1: raise ValueError('Ambiguous expected name: '+name)
            expected.append(candidates[0])
        cmd = [args.lean,'--root='+str(source),str(src),'-o',str(dest)+'.olean',
               '-i',str(dest)+'.ilean','--json','-j','1']
        started=time.monotonic(); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
        timed_out=False
        try:
            run=subprocess.run(cmd,env=env,cwd=source,capture_output=True,timeout=args.timeout)
            stdout,stderr,code=run.stdout,run.stderr,run.returncode
        except subprocess.TimeoutExpired as e:
            stdout,stderr,code=e.stdout or b'',e.stderr or b'',None;timed_out=True
        Path(str(dest)+'.stdout.jsonl').write_bytes(stdout);Path(str(dest)+'.stderr.log').write_bytes(stderr)
        messages=[]; errors=[]
        for line in stdout.decode(errors='replace').splitlines():
            try:
                value=json.loads(line);messages.append(str(value.get('data',value.get('message',value))))
                if value.get('severity')=='error':errors.append(value)
            except json.JSONDecodeError: messages.append(line)
        rec={'module':module,'source_sha256':digest(src),'start_utc':now,
             'exit_code':code,'timed_out':timed_out,'wall_seconds':time.monotonic()-started}
        try:
            if code != 0 or errors: raise ValueError('compiler failed or timed out')
            if not all(Path(str(dest)+e).is_file() for e in ['.olean','.ilean']): raise ValueError('missing fresh output')
            rec['axiom_check']=validate('\n'.join(messages),expected)
            rec['output_sha256']={e:digest(Path(str(dest)+'.'+e)) for e in ['olean','ilean']}
            rec['status']='PASS'
        except Exception as e: rec.update(status='FAIL',error=str(e))
        report['runs'].append(rec);save();print(module,rec['status'],round(rec['wall_seconds'],3),flush=True)
        if rec['status']!='PASS': report['status']='FAIL';save();return 1
    after={str(f.relative_to(source)):digest(f) for f in source.rglob('*.lean')}
    report['sources_unchanged']=after==before
    report['status']='PASS' if after==before else 'FAIL';save()
    return 0 if report['status']=='PASS' else 1
if __name__=='__main__': sys.exit(main())
