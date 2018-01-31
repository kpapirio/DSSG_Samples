#!/bin/bash


hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapred.reduce.tasks=1 \
	-input /data/assignments/ex2/part2/stackLarge.txt \
	-output /user/s1674939/assignment2/task3/output \
	-mapper EC-Assignment2/task3/mapper3.py \
	-reducer EC-Assignment2/task3/reducer3.py \
	-file EC-Assignment2/task3/mapper3.py EC-Assignment2/task3/reducer3.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
