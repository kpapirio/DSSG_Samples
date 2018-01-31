#!/usr/bin/python

import sys
import random

index = 0
reservoir = ""

for line in sys.stdin:
	if random.randint(0,index)==0:
		reservoir = line.strip()
	index += 1

print index, "\t", reservoir

