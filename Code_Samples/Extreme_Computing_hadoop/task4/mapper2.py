#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip()
	userId, answerId = line.split("\t", 1)
	print userId, "\t", answerId, "\t"
