#!/usr/bin/python

import sys
import random


reservoir = []
numLines=0

for line in sys.stdin:
	line = line.strip()
	if numLines < 100:
		reservoir.append(line)
	elif numLines >= 100 and 100/float(numLines+1) > random.random():
		upper = len(reservoir)-1
		randomIndex = random.randint(0,upper)
		reservoir[randomIndex] = line
	numLines += 1

for line in reservoir:
	print line, "\t"
	
