#!/usr/bin/python

import sys


next = 0
next_2 = 0
next_user= 0

for line in sys.stdin:	
	line = line.strip()
	answerId, userId = line.split("\t")
	if answerId == next and next_user != "1":
		print next_user, "\t",  next
	if next == next_2 and next_user != "1":
		print next_user, "\t", next
	
	next_2 = next
	next = answerId
	next_user = userId

if answerId == next and userId != "1":
	print userId, "\t", next





















