#!/usr/bin/python

import sys

prev = ""
total = 0
doc_prev = ""

for line in sys.stdin:           
    token, docID, count = line.strip().split()
    count = int(count)
    if prev == token:
        if doc_prev == docID:
            total += count
        else:
        	print prev, doc_prev, total, " "
		prev = token
          	doc_prev = docID
          	total = count
    else:
    	if prev: 
        	print prev, doc_prev, total, " "
	prev = token
        doc_prev = docID
        total = count
if prev == token:  
    print prev, docID, total, " "

