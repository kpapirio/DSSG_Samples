#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	attribs = re.findall(r'\s(\w+)="(\d+)', line.strip())
	single = dict(attribs)
	typeId = int(single['PostTypeId'])
	if typeId == 1:
		if 'AcceptedAnswerId' in single:
			print single['AcceptedAnswerId'],"\t", "1", "\t"		
	if typeId == 2:
		print single['Id'], "\t", single['OwnerUserId'], "\t"
	


	


		
