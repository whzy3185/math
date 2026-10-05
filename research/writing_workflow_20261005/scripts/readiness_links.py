"""Cross-record checks for administrative readiness. Never checks mathematical truth."""
from pathlib import Path
import json,hashlib,re,datetime,importlib.util
_spec=importlib.util.spec_from_file_location("schema_guard",Path(__file__).with_name("schema_guard.py"))
_guard=importlib.util.module_from_spec(_spec);_spec.loader.exec_module(_guard)
SHA=re.compile(r'[0-9a-f]{64}\Z')

def check_links(r,root,errors,blockers):
    errors.extend(_guard.check_named(r,'readiness.schema.json'))
    linked=r.get('linked_records',{})
    loaded={}
    for key in ['proof_obligations','review_response','version_registry','receipts','required_inventory']:
        ref=linked.get(key)
        if not isinstance(ref,dict):
            blockers.append('Integrated record missing: '+key);continue
        try:
            rel=ref['path'];p=Path(rel)
            if p.is_absolute() or '..' in p.parts or '\\' in rel:raise ValueError('unsafe linked path')
            f=root/p
            if any(q.is_symlink() for q in [f,*f.parents]) or not f.is_file() or not f.resolve().is_relative_to(root.resolve()):raise ValueError('missing/unsafe linked file')
            if hashlib.sha256(f.read_bytes()).hexdigest()!=ref['sha256']:raise ValueError('linked digest mismatch')
            loaded[key]=json.loads(f.read_text())
            if not isinstance(loaded[key],dict) or not loaded[key]:
                raise ValueError('linked record must be a nonempty object')
        except (KeyError,ValueError,OSError,TypeError) as e:
            loaded.pop(key,None);errors.append(f'{key}: {e}')
    for key,doc in loaded.items():errors.extend(key+': '+msg for msg in _guard.check_named(doc,key+'.schema.json'))
    version=r.get('version');paper=r.get('paper');gates={g.get('id'):g for g in r.get('gates',[])}
    def passed(g):return gates.get(g,{}).get('status')=='pass'
    ids={c.get('id') for c in r.get('claims',[])}
    inventory=loaded.get('required_inventory',{})
    if inventory:
        if inventory.get('paper')!=paper or inventory.get('version')!=version:errors.append('Required inventory paper/version mismatch')
        for key in ['obligation_ids','issue_ids','claim_ids']:
            vals=inventory.get(key)
            if not isinstance(vals,list) or not all(isinstance(x,str) and x for x in vals) or len(vals)!=len(set(vals)):
                errors.append('Invalid required inventory: '+key)
        if set(inventory.get('claim_ids',[]))!=ids:errors.append('Claim inventory mismatch')
    obligations=loaded.get('proof_obligations')
    if obligations:
        if obligations.get('paper')!=paper or obligations.get('version')!=version:errors.append('Proof obligations have wrong paper/version')
        rows=obligations.get('obligations',[]);oids=[o.get('id') for o in rows]
        if len(oids)!=len(set(oids)):errors.append('Duplicate proof obligation IDs')
        if sorted(oids)!=sorted(inventory.get('obligation_ids',[])):errors.append('Required proof obligation inventory changed or incomplete')
        covered=set()
        for o in rows:
            cid=o.get('claim_id');covered.add(cid)
            if cid not in ids:errors.append(f'Obligation {o.get("id")}: unknown claim')
            if o.get('status') not in ['discharged','open','disputed','not_applicable']:errors.append('Unknown obligation status')
            if o.get('status')=='not_applicable' and (not o.get('justification') or not o.get('approved_by')):
                errors.append('Not-applicable obligation lacks reason/approval')
            if o.get('status')=='discharged':
                for key in ['acceptance','checked_by','evidence']:
                    if not o.get(key):errors.append(f'Obligation {o.get("id")}: discharge lacks {key}')
            if o.get('status') in ['open','disputed'] and passed('S03'):errors.append('S03 passes with open/disputed proof obligation')
        if passed('S03') and covered!=ids:errors.append('S03 proof obligations do not cover every claim')
    response=loaded.get('review_response')
    if response:
        if response.get('paper')!=paper or response.get('new_version')!=version:errors.append('Review response has wrong paper/new version')
        if response.get('reviewer_id')==response.get('editor_id'):errors.append('Linked response editor equals reviewer')
        issues=response.get('issues',[])
        if sorted(i.get('issue_id') for i in issues)!=sorted(inventory.get('issue_ids',[])):errors.append('Required review issue inventory changed or incomplete')
        contexts0=r.get('review_contexts',[])
        if not any(c.get('reviewer_id')==response.get('reviewer_id') and c.get('editor_id')==response.get('editor_id') for c in contexts0):errors.append('Response reviewer/editor are not registered together')
        if passed('S11') and any(i.get('reviewer_closure')!='closed' for i in issues if i.get('severity')!='optional'):
            errors.append('S11 passes with unresolved required review issues')
    registry=loaded.get('version_registry')
    if registry:
        if registry.get('paper')!=paper:errors.append('Version registry has wrong paper')
        versions=registry.get('versions',[])
        vs=[v.get('version_id') for v in versions]
        if len(vs)!=len(set(vs)):errors.append('Duplicate version IDs')
        match=[v for v in versions if v.get('version_id')==version]
        if len(match)!=1:errors.append('Current version is not unique in version registry')
        else:
            v=match[0]
            if v.get('pdf_sha256')!=r.get('pdf_sha256'):errors.append('Version registry PDF does not match readiness PDF')
            for key in v.get('invalidated_gates',[]):
                # A new version can reclose an invalidated gate, but only via a dated current-version receipt.
                if passed(key):
                    receipts=loaded.get('receipts',{}).get('receipts',[])
                    if not any(z.get('gate')==key and z.get('version')==version and z.get('result')=='pass' for z in receipts):
                        errors.append(f'{key}: invalidated by version change without current receipt')
            regcontexts=v.get('review_contexts',[])
            regids=[c.get('context_id') for c in regcontexts]
            if len(regids)!=len(set(regids)):errors.append('Repeated context ID in version registry')
            if {c.get('context_id') for c in r.get('review_contexts',[])}!=set(regids):errors.append('Readiness and version registry contexts disagree')
            for c in r.get('review_contexts',[]):
                rows=[z for z in regcontexts if z.get('context_id')==c.get('context_id')]
                if rows and rows[0]!=c:errors.append('Context disposition differs between readiness and version registry')
    contexts=r.get('review_contexts',[]);cids=[c.get('context_id') for c in contexts]
    if len(cids)!=len(set(cids)):errors.append('Repeated context ID: aggregate rounds before recording; cannot split to evade cap')
    byreviewer={}
    for c in contexts:byreviewer.setdefault(c.get('reviewer_id'),[]).append(c)
    for reviewer, rows in byreviewer.items():
        if len({c.get('context_id') for c in rows})>1 and any(c.get('retired') for c in rows):
            errors.append('Retired reviewer executor relabelled with a new context ID: '+str(reviewer))
    # A registered round cannot be reused for a third assessment just by changing the paper version.
    recdoc=loaded.get('receipts')
    if recdoc:
        if recdoc.get('paper')!=paper or recdoc.get('version')!=version:errors.append('Receipt set has wrong paper/version')
        receipts=recdoc.get('receipts',[])
        rid=[z.get('receipt_id') for z in receipts]
        if len(rid)!=len(set(rid)):errors.append('Duplicate receipt IDs')
        for z in receipts:
            if z.get('version')!=version:errors.append('Stale receipt version')
            if not z.get('recorded_by') or not z.get('evidence'):errors.append('Receipt lacks attributed supporting evidence')
            try:datetime.datetime.fromisoformat(z['recorded_utc'].replace('Z','+00:00'))
            except (KeyError,ValueError,TypeError):errors.append('Receipt lacks valid UTC time')
        required={'S00':'venue_policy','S08':'mathematical_audit','S09':'blind_review','S11':'rereview','S12':'formal_audit','S13':'pdf_visual_qa','S14':'archive_replay','S15':'authorship_consent'}
        finite_ids={c['id'] for c in r.get('claims',[]) if c.get('evidence_kind') in ['finiteVerified','computerAssistedProved']}
        if finite_ids:required['S04']='computational_audit'
        for gate,typ in required.items():
            if not passed(gate):continue
            matches=[z for z in receipts if z.get('gate')==gate and z.get('type')==typ and z.get('result')=='pass']
            if not matches:errors.append(f'{gate}: missing typed {typ} receipt');continue
            z=matches[-1];d=z.get('details',{})
            if not isinstance(d,dict):errors.append(f'{gate}: details must be object');continue
            keys={'computational_audit':['finite_claim_ids','obligation_ids','arithmetic','fresh_run_scope','run_evidence','reduction_evidence'],'venue_policy':['venue','official_policy_urls','actual_ai_uses','compatibility_basis'],
                  'mathematical_audit':['claim_ids','coverage','review_report_sha256'],
                  'blind_review':['context_id','packet_manifest_sha256','packet_manifest','pdf_sha256','no_inherited_history','exposure'],
                  'rereview':['context_id','pdf_sha256','closed_issue_ids','review_report_sha256'],
                  'formal_audit':['declarations','lean_version','mathlib_commit','axiom_results','semantic_correspondence','build_exit_code'],
                  'pdf_visual_qa':['pdf_sha256','page_count','inspected_pages'],
                  'archive_replay':['url','archive_sha256','archive','anonymous_retrieval','entrypoint','replay_exit_code','fresh_output_sha256','fresh_output'],
                  'authorship_consent':['authors','journal','approval_scope','consent_evidence']}[typ]
            for k in keys:
                if k not in d or d[k] is None or d[k]=='' or d[k]==[]:errors.append(f'{gate}: receipt lacks {k}')
            for key,val in d.items():
                if key.endswith('_sha256') and (not isinstance(val,str) or not SHA.fullmatch(val)):
                    errors.append(f'{gate}: invalid scalar hash {key}')
            if typ in ['blind_review','rereview']:
                ctx=[c for c in contexts if c.get('context_id')==d.get('context_id')]
                if len(ctx)!=1 or ctx[0].get('reviewed_version')!=version:errors.append(f'{gate}: receipt context not current/registered')
                if gates[gate].get('review_context_id')!=d.get('context_id'):errors.append(f'{gate}: receipt/gate context mismatch')
            if typ=='rereview':
                closed=[i.get('issue_id') for i in loaded.get('review_response',{}).get('issues',[]) if i.get('reviewer_closure')=='closed']
                if sorted(d.get('closed_issue_ids',[]))!=sorted(closed):errors.append('Rereview closed issue IDs disagree with response')
            if typ in ['mathematical_audit','rereview'] and d.get('review_report_sha256') not in [e.get('sha256') for e in z.get('evidence',[]) if isinstance(e,dict)]:errors.append('Receipt report hash unbound to evidence')
            if typ=='blind_review' and (not isinstance(d.get('packet_manifest'),dict) or d['packet_manifest'].get('sha256')!=d.get('packet_manifest_sha256')):errors.append('Packet hash unbound to actual manifest')
            if typ=='archive_replay':
                for key,hashed in [('archive','archive_sha256'),('fresh_output','fresh_output_sha256')]:
                    if not isinstance(d.get(key),dict) or d[key].get('sha256')!=d.get(hashed):errors.append(f'Archive receipt {hashed} unbound to bytes')
            if typ=='computational_audit':
                if set(d.get('finite_claim_ids',[]))!=finite_ids:errors.append('S04 computational receipt omits finite claims')
                obs={o.get('id'):o for o in loaded.get('proof_obligations',{}).get('obligations',[])}
                bound=[obs.get(i,{}) for i in d.get('obligation_ids',[])]
                if not bound or any(o.get('status')!='discharged' for o in bound) or {o.get('claim_id') for o in bound}!=finite_ids:errors.append('S04 finite premise discharge is not bound to exact obligations')
            if typ=='authorship_consent':
                if not isinstance(d.get('authors'),list) or not d['authors'] or not all(isinstance(n,str) and n.strip() for n in d['authors']):errors.append('Named authors missing/invalid')
                if not isinstance(d.get('journal'),str) or not d['journal'].strip():errors.append('Consent journal missing/invalid')
                if not isinstance(d.get('consent_evidence'),list) or not d['consent_evidence']:errors.append('Consent evidence is not a nonempty list')
                policies=[z.get('details',{}).get('venue') for z in receipts if z.get('type')=='venue_policy' and z.get('result')=='pass']
                if d.get('journal') not in policies:errors.append('Policy venue and consent journal differ')
            if typ=='mathematical_audit' and set(d.get('claim_ids',[]))!=ids:errors.append('Mathematical audit receipt omits claims')
            if typ in ['blind_review','rereview','pdf_visual_qa'] and d.get('pdf_sha256')!=r.get('pdf_sha256'):errors.append(f'{gate}: receipt PDF hash mismatch')
            if typ=='blind_review' and (d.get('no_inherited_history') is not True or d.get('exposure')!='clean'):errors.append('Blind review receipt is not clean')
            if typ=='pdf_visual_qa':
                count=d.get('page_count');pages=d.get('inspected_pages')
                if not isinstance(count,int) or count<1 or pages!=list(range(1,count+1)):errors.append('PDF QA does not cover every page exactly')
            if typ=='archive_replay' and (d.get('anonymous_retrieval') is not True or (type(d.get('replay_exit_code')) is not int or d.get('replay_exit_code')!=0)):errors.append('Archive replay/access did not succeed')
            if typ=='formal_audit' and (type(d.get('build_exit_code')) is not int or d.get('build_exit_code')!=0):errors.append('Formal build did not succeed')
            if typ=='authorship_consent' and d.get('approval_scope')!='final manuscript and selected journal':errors.append('Authorship consent scope incomplete')
    # Verify every evidence reference nested in linked records, not only the top-level hash.
    def walk(x):
        if isinstance(x,dict):
            if 'path' in x and 'sha256' in x:
                try:
                    p=Path(x['path']);f=root/p
                    if p.is_absolute() or '..' in p.parts or any(p.is_symlink() for p in [f,*f.parents]) or not f.is_file() or not f.resolve().is_relative_to(root.resolve()):raise ValueError('unsafe/missing evidence')
                    if not SHA.fullmatch(x['sha256']) or hashlib.sha256(f.read_bytes()).hexdigest()!=x['sha256']:raise ValueError('evidence digest mismatch')
                except (TypeError,ValueError,OSError):errors.append('Linked record nested evidence missing/changed: '+str(x.get('path')))
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    for doc in loaded.values():walk(doc)

    _espec=importlib.util.spec_from_file_location("exact_bindings",Path(__file__).with_name("exact_bindings.py"))
    _exact=importlib.util.module_from_spec(_espec);_espec.loader.exec_module(_exact)
    _exact.validate_exact(r,loaded,root,errors)
