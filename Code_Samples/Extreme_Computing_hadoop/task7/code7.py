#!/usr/bin/python

import sys
from bitarray import bitarray

# number of lines read in as argument from the command line
N = int(sys.argv[1])

#creates array of size that allows for 10 hashes and sets all bits to 0
m = N*10
bit = bitarray([False])*m

hashArray = []
check = []

for line in sys.stdin:
	line = line.strip()

	#7 hash functions
	for x in range(1,7):
		index = hash(line) % m
		hashArray.append(index)
	
	for y in hashArray:
		if bit[y] == 0:
			check.append("no")
		if bit[y]== 1:
			check.append("maybe")

	if "no" in check:
		for y in hashArray:
			if bit[y] != 1:
				bit[y] = 1
		print line
	check = []
	hashArray = []

