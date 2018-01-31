#!/usr/bin/python

import sys
import re

for line in sys.stdin:
	attribs = re.findall(r'\s(\w+)="(\d+)', line.strip())
	single = dict(attribs)
	typeId = int(single['PostTypeId'])
	if typeId == 2:
		print single['OwnerUserId'], single['Id'], "\t"
