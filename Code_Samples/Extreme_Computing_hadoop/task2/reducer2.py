#!/usr/bin/python

import sys

top = 0

print "#Count", "Id"

for line in sys.stdin:
	line = line.strip()
	key, value = line.split(" ", 1)
	if top < 10:
		print(value + " " + key)
		top += 1
