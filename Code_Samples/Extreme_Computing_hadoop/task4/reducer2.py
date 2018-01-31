#!/usr/bin/python

import sys

next = 0
D = {}
DString = {}

for line in sys.stdin:
	line = line.strip()
	userId, answerId = line.split("\t", 1)
	if userId != next:
		D[userId] = 1
		DString[userId] = answerId
	else:
		D[userId] += 1
		DString[userId] += ", " + answerId
	next = userId

if userId == next:
	D[userId] += 1
	DString[userId] += ", " + answerId
maxId =  max(D, key=lambda i:D[i])

print maxId, "-->", D[maxId], ',', DString[maxId]
