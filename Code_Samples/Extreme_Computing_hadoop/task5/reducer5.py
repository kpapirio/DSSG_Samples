#!/usr/bin/python

import sys
import random

total = 0
reservoir1 = ""

for line in sys.stdin:
	num, reservoir = line.split("\t", 1)
	total += int(num)
	if random.randint(0,total) < int(num):
		reservoir1 = reservoir 

print reservoir1

