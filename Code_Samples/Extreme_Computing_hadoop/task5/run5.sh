#!/bin/bash


hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapred.reduce.tasks=1 \
	-input /data/assignments/ex2/part3/webLarge.txt \
	-output /user/s1674939/assignment2/task5/output \
	-mapper EC-Assignment2/task5/mapper5.py \
	-reducer EC-Assignment2/task5/reducer5.py \
	-file EC-Assignment2/task5/mapper5.py EC-Assignment2/task5/reducer5.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
