#!/usr/bin/python

import sys
import re

attribDict = {}

for line in sys.stdin:
	attribs = re.findall(r'\s(\w+)="(\d+)', line.strip())
	single = dict(attribs)
	typeId = int(single['PostTypeId'])
	if typeId == 1:
		print single['ViewCount'], single['Id'], "\t"
	
	
	
		
		
		
