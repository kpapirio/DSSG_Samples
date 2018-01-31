#!/usr/bin/python

import sys

next_Id = ""
total = 0
q_nums = ""
highest = 0
userHighest = 0
highestIds = ""


for line in sys.stdin:
	line = line.strip()
	userId, qId = line.split(" ", 1)
	if next_Id == userId:
		total += 1
		if q_nums == "":
			q_nums += qId
		else:
			q_nums += ", " + qId
	else:
		if next_Id:
			if total > highest:
				highest = total
				userHighest = userId
				highestIds = q_nums
		total = 1
		next_Id = userId
		q_nums = ""

print userHighest, "-->", highestIds




		
	

