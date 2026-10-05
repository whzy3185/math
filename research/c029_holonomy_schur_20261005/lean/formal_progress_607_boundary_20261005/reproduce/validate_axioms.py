"""Validate complete Lean #print axioms output; no theorem proving is done here."""
import re
STANDARD={'propext','Classical.choice','Quot.sound'}
LINE=re.compile(r"^'([^']+)' (?:depends on axioms: \[([^\]]*)\]|(does not depend on any axioms))$",re.M)
def validate(text,expected):
    expected=list(expected)
    if len(expected)!=len(set(expected)):raise ValueError('Duplicate expected name')
    got={}
    for match in LINE.finditer(text):
        name,values,empty=match.groups()
        if name in got:raise ValueError('Duplicate result '+name)
        axioms=set() if empty else {v.strip() for v in values.split(',') if v.strip()}
        if not axioms<=STANDARD:raise ValueError('Unexpected axiom '+str(axioms-STANDARD))
        got[name]=axioms
    remainder=LINE.sub('',text)
    if 'depends on axioms:' in remainder or 'does not depend on any axioms' in remainder:
        raise ValueError('Malformed axiom output')
    if set(got)!=set(expected):raise ValueError('Name/count mismatch missing='+str(set(expected)-set(got))+' extra='+str(set(got)-set(expected)))
    if 'sorryAx' in text or re.search(r'\berror:',text):raise ValueError('Compiler error or sorryAx')
    return {'count':len(got),'axiom_union':sorted(set().union(*got.values())),'axioms':{k:sorted(v) for k,v in got.items()}}
def tests():
    lines="'A' depends on axioms: [propext, Classical.choice, Quot.sound]\n'B' does not depend on any axioms\n"
    assert validate(lines,['A','B'])['axioms']['B']==[]
    assert validate("'A' depends on axioms: []",['A'])['axioms']['A']==[]
    assert validate("'A' depends on axioms: [propext,\n Classical.choice,\n Quot.sound]",['A'])['axiom_union']==sorted(STANDARD)
    cases=[(lines.replace('propext','evil'),['A','B']), (lines,['A','C']), (lines,['A']), (lines,['A','B','C']), (lines+"'A' does not depend on any axioms\n",['A','B']), (lines,['A','B','B']), (lines.replace('axioms: [','axioms: [' ,1).replace('Quot.sound]','Quot.sound'),['A','B'])]
    for text,names in cases:
        try:validate(text,names)
        except ValueError:continue
        raise AssertionError('Invalid case accepted')
    return {'valid_format_tests':4,'negative_tests':len(cases),'status':'PASS'}
if __name__=='__main__':print(tests())
