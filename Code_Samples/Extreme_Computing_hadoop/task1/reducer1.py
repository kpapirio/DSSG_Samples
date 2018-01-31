#!/usr/bin/python

import sys

prev = ""
total = 0
doc_prev = ""
value = 0
index = ""


for line in sys.stdin:        
    token, docID, count = line.strip().split()
    count = int(count)
    if prev == token:
        if total == 0 or total == 1:
		index += "{{({0}, {1})".format(doc_prev, value)
	else:
		index += ", ({0}, {1})".format(doc_prev, value)
        doc_prev = docID
        value = count
	total += 1
    else:
        if prev: 
            if total == 0 or total == 1:
		index += "{"
            else:
                index += ", "
            index += "({0}, {1})}}".format(doc_prev, value)
            print prev, ": ", total, ": ", index
	prev = token
        doc_prev = docID
        total = 1
        value = count
	index = ""

if prev == token: 
	index += "{{({0}, {1})}}".format(docID, count)
	print prev, ": ", total, ": ", index
