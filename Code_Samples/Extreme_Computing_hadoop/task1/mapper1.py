#!/usr/bin/python


import sys
import os

prev = ""
total = 0

docID = os.environ["mapreduce_map_input_file"].strip().split('/')[-1]

for line in sys.stdin:          
    tokens = line.strip().split()         
    for token in tokens:
        if prev == token:
            total += 1
        else:
        	if prev:
              		print prev, docID, total, " "
        	total = 1
            	prev = token
if prev == token:
   	print token, docID, total, " "
	

