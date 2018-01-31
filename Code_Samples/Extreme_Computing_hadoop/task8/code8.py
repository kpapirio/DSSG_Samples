#!/usr/bin/python

#Lossy Counting Algorithm

import sys

counter= {}
line_num = 0
s= 0.01
window = 1000
bcurrent = 1

for line in sys.stdin:
	line = line.strip()
	line_num += 1
	if line not in counter:
		counter[line]= [1, bcurrent-1]
	else:
		counter[line][0] += 1

	if line_num % window == 0 :
		for key, value in counter.items():
			if value[0]+value[1] < bcurrent:
				del counter[key]
		bcurrent += 1

for key, value in counter.items():
	if (s - s*0.1)*line_num <= value[0]:
		print key, value

