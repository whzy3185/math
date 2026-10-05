"""Typed receipt details and exact frozen-input/history joins."""
from pathlib import Path
import hashlib,json,datetime

def fingerprint(r):
 rows=[(x['path'],x['sha256']) for x in [r['input_pdf'],*r['input_sources']]]
 return hashlib.sha256(json.dumps(sorted(rows),separators=(',',':')).encode()).hexdigest()

def strict_ref(root,e):
 if not isinstance(e,dict) or set(e)-{'path','sha256','locator'} or not isinstance(e.get('path'),str) or not isinstance(e.get('sha256'),str):raise ValueError('invalid evidence reference')
 p=Path(e['path']);f=root/p
 if p.is_absolute() or '..' in p.parts or '\\' in e['path'] or not f.is_file() or any(q.is_symlink() for q in [f,*f.parents]) or not f.resolve().is_relative_to(root.resolve()):raise ValueError('unsafe/missing evidence file')
 if hashlib.sha256(f.read_bytes()).hexdigest()!=e['sha256']:raise ValueError('evidence hash mismatch')
 return f

def validate_exact(r,docs,root,errors):
 try:fp=fingerprint(r)
 except (KeyError,TypeError):errors.append('Cannot fingerprint complete input set');return
 reg=docs.get('version_registry',{});vs=reg.get('versions',[]);byid={v.get('version_id'):v for v in vs};ordered=[];visiting=set();done=set()
 def visit(vid):
  if vid in visiting:raise ValueError('version dependency cycle')
  if vid in done:return
  visiting.add(vid);parent=byid[vid].get('parent_version')
  if parent in byid:visit(parent)
  visiting.remove(vid);done.add(vid);ordered.append(byid[vid])
 try:
  for vid in byid:visit(vid)
 except ValueError as e:errors.append(str(e))
 history={}
 reviewer_history={}
 for v in ordered:
  for c in v.get('review_contexts',[]):
   cid=c.get('context_id');prev=history.get(cid)
   reviewer=c.get('reviewer_id')
   if any(old.get('context_id')!=cid and old.get('retired') for old in reviewer_history.get(reviewer,[])):errors.append('Retired reviewer executor relabelled across version history: '+str(reviewer))
   reviewer_history.setdefault(reviewer,[]).append(c)
   if prev:
    changed=c.get('reviewed_version')!=prev.get('reviewed_version') or c.get('report_sha256')!=prev.get('report_sha256')
    if changed and (prev.get('retired') or c.get('rounds_used',0)<=prev.get('rounds_used',0)):errors.append('Context reused after retirement or without round increment: '+str(cid))
    if c.get('rounds_used',0)<prev.get('rounds_used',0) or (prev.get('retired') and not c.get('retired')):errors.append('Context state reset: '+str(cid))
   history[cid]=c
 current=byid.get(r.get('version'),{})
 input_set={(x['path'],x['sha256']) for x in [r['input_pdf'],*r['input_sources']]}
 if current.get('source_fingerprint')!=fp:errors.append('Current version source fingerprint mismatch')
 if not input_set.issubset({(x.get('path'),x.get('sha256')) for x in current.get('files',[])}):errors.append('Version registry omits frozen input files')
 gates={g['id']:g for g in r.get('gates',[])};receipts=docs.get('receipts',{}).get('receipts',[]);latest={}
 for z in receipts:
  key=(z.get('gate'),z.get('type'))
  try:time=datetime.datetime.fromisoformat(z['recorded_utc'].replace('Z','+00:00'))
  except (KeyError,ValueError,TypeError):continue
  if key not in latest or time>latest[key][0] or (time==latest[key][0] and z.get('result')!='pass'):latest[key]=(time,z)
 for (g,typ),(_,z) in latest.items():
  if gates.get(g,{}).get('status')=='pass' and z.get('result')!='pass':errors.append('Passed gate has a newer nonpassing receipt: '+g)
 source_types={'computational_audit','mathematical_audit','blind_review','rereview','formal_audit','pdf_visual_qa','archive_replay','stage_attestation','authorship_consent'}
 for z in receipts:
  if z.get('result')!='pass':continue
  typ=z.get('type');d=z.get('details',{})
  if typ in source_types and d.get('source_fingerprint')!=fp:errors.append('Receipt not bound to exact frozen inputs: '+str(z.get('receipt_id')))
  def nonemptystr(k):
   if not isinstance(d.get(k),str) or not d[k].strip():errors.append(typ+': missing text '+k)
  def stringlist(k):
   if not isinstance(d.get(k),list) or not d[k] or not all(isinstance(v,str) and v.strip() for v in d[k]):errors.append(typ+': invalid list '+k)
  def refs(k):
   vals=d.get(k)
   if not isinstance(vals,list) or not vals:errors.append(typ+': missing evidence list '+k);return
   for v in vals:
    try:strict_ref(root,v)
    except (ValueError,OSError,TypeError) as e:errors.append(typ+': '+k+': '+str(e))
  if typ=='venue_policy':
   for k in ['venue','compatibility_basis']:nonemptystr(k)
   for k in ['official_policy_urls','actual_ai_uses']:stringlist(k)
  if typ=='authorship_consent':
   refs('consent_evidence')
  if typ=='computational_audit':
   refs('run_evidence');refs('reduction_evidence')
  if typ in {'archive_replay','blind_review','rereview'}:
   keys=['archive','fresh_output'] if typ=='archive_replay' else ['packet_manifest']
   for k in keys:
    try:strict_ref(root,d.get(k))
    except (ValueError,OSError,TypeError) as e:errors.append(typ+': '+k+': '+str(e))
  if typ in {'blind_review','rereview'}:
   try:
    f=strict_ref(root,d.get('packet_manifest'));packet=json.loads(f.read_text());members=packet['files']
    actual=set()
    for row in members:
     file=strict_ref(f.parent,{'path':row['path'],'sha256':row['sha256']});rel=str(file.relative_to(root));actual.add((rel,row['sha256']))
    if actual!=input_set:errors.append('Review packet inventory differs from exact frozen input set')
    if d.get('packet_manifest_sha256')!=hashlib.sha256(f.read_bytes()).hexdigest():errors.append('Review packet manifest digest mismatch')
   except (ValueError,OSError,TypeError,KeyError) as e:errors.append('Cannot validate review packet members: '+str(e))
  if typ=='rereview':
   context=next((c for c in r.get('review_contexts',[]) if c.get('context_id')==d.get('context_id')),None);resp=docs.get('review_response',{})
   if not context or resp.get('reviewer_id')!=context.get('reviewer_id') or resp.get('editor_id')!=context.get('editor_id'):errors.append('Closed response is not bound to the actual rereviewer/editor')
 for ob in docs.get('proof_obligations',{}).get('obligations',[]):
  if ob.get('status')=='not_applicable':
   alternative=ob.get('alternative_obligation_id');others=docs.get('proof_obligations',{}).get('obligations',[])
   if not any(x.get('id')==alternative and x.get('claim_id')==ob.get('claim_id') and x.get('status')=='discharged' for x in others):errors.append('Not-applicable theorem obligation has no discharged alternative')
