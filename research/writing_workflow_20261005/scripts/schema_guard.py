"""Validate the JSON Schema subset used by this toolkit; no external dependencies.
For arbitrary draft-2020-12 schemas use jsonschema. Unknown assertion keywords fail
closed here. This function checks record structure, never evidence truth.
"""
import re
from pathlib import Path
import json
ALLOWED={'$schema','title','description','type','properties','required','additionalProperties','items','minItems','maxItems','minLength','maxLength','minimum','maximum','pattern','enum','const','allOf','if','then'}
def validate(x,s,path='$'):
 errors=[]
 unknown=set(s)-ALLOWED
 if unknown:return [path+': unsupported schema keyword '+str(sorted(unknown))]
 def fits(t):
  return {'object':isinstance(x,dict),'array':isinstance(x,list),'string':isinstance(x,str),'integer':type(x) is int,'number':type(x) in [int,float],'boolean':type(x) is bool,'null':x is None}.get(t,False)
 typ=s.get('type')
 if typ and not any(fits(t) for t in (typ if isinstance(typ,list) else [typ])):return [path+': wrong type']
 if 'enum' in s and not any(type(x)==type(v) and x==v for v in s['enum']):errors.append(path+': not in enum')
 if 'const' in s and (type(x)!=type(s['const']) or x!=s['const']):errors.append(path+': wrong const')
 if isinstance(x,dict):
  for k in s.get('required',[]):
   if k not in x:errors.append(path+': missing '+k)
  props=s.get('properties',{})
  if s.get('additionalProperties') is False:
   for k in set(x)-set(props):errors.append(path+': unknown property '+k)
  for k,v in x.items():
   if k in props:errors+=validate(v,props[k],path+'.'+k)
 if isinstance(x,list):
  if len(x)<s.get('minItems',0) or len(x)>s.get('maxItems',float('inf')):errors.append(path+': wrong item count')
  if 'items' in s:
   for i,v in enumerate(x):errors+=validate(v,s['items'],path+f'[{i}]')
 if isinstance(x,str):
  if len(x)<s.get('minLength',0) or len(x)>s.get('maxLength',float('inf')):errors.append(path+': wrong string length')
  if 'pattern' in s and re.search(s['pattern'],x) is None:errors.append(path+': pattern mismatch')
 if type(x) in [int,float] and (x<s.get('minimum',float('-inf')) or x>s.get('maximum',float('inf'))):errors.append(path+': numeric bound')
 for sub in s.get('allOf',[]):errors+=validate(x,sub,path)
 if 'if' in s and not validate(x,s['if'],path):errors+=validate(x,s.get('then',{}),path)
 return errors

def check_named(x,name):
 schema=json.loads((Path(__file__).resolve().parents[1]/'schemas'/name).read_text())
 return validate(x,schema)
