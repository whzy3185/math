#!/usr/bin/env python3
"""Elementary synthetic demonstration: exact finite checks, not an infinite proof."""
import json
rows=[]
for n in range(21):
 actual=sum(2*k+1 for k in range(n))
 assert actual==n*n
 rows.append({'n':n,'sum':actual,'square':n*n})
print(json.dumps({'evidence_kind':'finiteVerified','domain':'integers 0 through 20 inclusive','arithmetic':'exact Python integers','assertions_checked':len(rows),'unbounded_claim_proved_by_this_run':False,'rows':rows},indent=2))
