#!/usr/bin/env python3
"""Portable dependency-first finite source replay route, not a recorded fresh607 pass.
The default only prints the plan. --execute starts bounded sequential compilation.
"""
import argparse, fcntl, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'finite/formal'
TARGETS=['TargetA.AllTheorems','TargetA.Period8ConjectureConstant','TargetA.R2FiniteSeedIdentification']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def plan():
    ordered=[];visiting=set();done=set()
    def visit(name):
        if name in done:return
        if name in visiting:raise ValueError('Import cycle: '+name)
        path=SOURCE/(name.replace('.','/')+'.lean')
        if not path.is_file():raise ValueError('Missing project source: '+name)
        visiting.add(name)
        for imp in re.findall(r'^import\s+(\S+)',path.read_text(),re.M):
            if imp.startswith('TargetA.'):visit(imp)
        visiting.remove(name);done.add(name);ordered.append(name)
    for target in TARGETS:visit(target)
    return ordered

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--execute',action='store_true')
    ap.add_argument('--audit',action='store_true',help='After compilation, attempt the previously unsuccessful monolithic audit')
    ap.add_argument('--lean',default='lean')
    ap.add_argument('--cache-project',type=Path,default=ROOT/'dependencies')
    ap.add_argument('--out',type=Path,default=ROOT/'.repro/finite')
    ap.add_argument('--lock',type=Path,default=ROOT/'.repro/compiler.lock')
    ap.add_argument('--timeout',type=int,default=180)
    a=ap.parse_args();order=plan()
    if not a.execute:print(json.dumps({'mode':'PLAN_ONLY','modules':order,'fresh607_pass':False},indent=2));return 0
    if a.out.exists():ap.error('output path must be new; preserve earlier failed attempts')
    if a.timeout<=0:ap.error('timeout must be positive')
    a.lock.parent.mkdir(parents=True,exist_ok=True);lock=a.lock.open('a')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:sys.exit('compiler lock busy; no process started')
    version=subprocess.check_output([a.lean,'--version'],text=True).strip()
    if 'version 4.33.1,' not in version or '819816b2e0a3bf405af45ae5c7af2491d8f5bee6' not in version:sys.exit('Wrong compiler version')
    paths=[]
    for package in json.loads((ROOT/'dependencies/lake-manifest.json').read_text())['packages']:
        folder=a.cache_project.resolve()/'.lake/packages'/package['name'];lib=folder/'.lake/build/lib/lean'
        if not lib.is_dir() and package['name']=='Cli':continue
        if not lib.is_dir():sys.exit('Missing cache: '+package['name'])
        if subprocess.check_output(['git','-C',str(folder),'rev-parse','HEAD'],text=True).strip()!=package['rev']:sys.exit('Wrong dependency revision: '+package['name'])
        paths.append(str(lib))
    a.out.mkdir(parents=True);env=os.environ.copy();env['LEAN_PATH']=os.pathsep.join([str(a.out.resolve())]+paths)
    report={'status':'RUNNING','mode':'serial_dependency_first_fresh_source','lean_version':version,'prior_project_objects_used':False,'runs':[],'monolithic_audit_requested':a.audit,'fresh607_audit_pass':False}
    def save():(a.out/'replay.json').write_text(json.dumps(report,indent=2)+'\n')
    work=order+(['R2FiniteSeedAxiomAudit'] if a.audit else [])
    for module in work:
        relative=module.replace('.','/');source=SOURCE/(relative+'.lean');dest=a.out/relative;dest.parent.mkdir(parents=True,exist_ok=True)
        command=[a.lean,'--root='+str(SOURCE),str(source),'-o',str(dest)+'.olean','-i',str(dest)+'.ilean','-c',str(dest)+'.c','--json','-j','1']
        before=sha(source);start=time.monotonic();save()
        try:r=subprocess.run(command,env=env,cwd=SOURCE,capture_output=True,timeout=a.timeout);code=r.returncode;stdout,stderr=r.stdout,r.stderr;timeout=False
        except subprocess.TimeoutExpired as e:code=None;stdout,stderr=e.stdout or b'',e.stderr or b'';timeout=True
        Path(str(dest)+'.stdout.jsonl').write_bytes(stdout);Path(str(dest)+'.stderr.log').write_bytes(stderr)
        rec={'module':module,'source_sha256':before,'source_unchanged':before==sha(source),'wall_seconds':time.monotonic()-start,'exit_code':code,'timed_out':timeout}
        rec['status']='PASS' if code==0 and rec['source_unchanged'] and all(Path(str(dest)+'.'+x).is_file() for x in ['olean','ilean','c']) else 'FAIL'
        if module=='R2FiniteSeedAxiomAudit' and rec['status']=='PASS':
            from validate_axioms import validate
            messages=[str(json.loads(line).get('data','')) for line in stdout.decode().splitlines()]
            expected=re.findall(r'^#print axioms (\S+)',source.read_text(),re.M)
            try:rec['axiom_check']=validate('\n'.join(messages),expected);report['fresh607_audit_pass']=rec['axiom_check']['count']==607
            except ValueError as e:rec.update(status='FAIL',error=str(e))
        report['runs'].append(rec);save();print(module,rec['status'],round(rec['wall_seconds'],3),flush=True)
        if rec['status']!='PASS':report['status']='FAIL';save();return 1
    report['status']='PASS' if report['fresh607_audit_pass'] else 'SOURCE_COMPILE_PASS_WITHOUT_FRESH607_AUDIT';save();return 0
if __name__=='__main__':sys.exit(main())
