#!/bin/bash


hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-input /data/assignments/ex2/part2/stackLarge.txt \
	-output /user/s1674939/assignment2/task4/temp \
	-mapper EC-Assignment2/task4/mapper.py \
	-reducer EC-Assignment2/task4/reducer.py \
	-file EC-Assignment2/task4/mapper.py EC-Assignment2/task4/reducer.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner



hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapred.reduce.tasks=1 \
	-input /user/s1674939/assignment2/task4/temp \
	-output /user/s1674939/assignment2/task4/output \
	-mapper EC-Assignment2/task4/mapper2.py \
	-reducer EC-Assignment2/task4/reducer2.py \
	-file EC-Assignment2/task4/mapper2.py EC-Assignment2/task4/reducer2.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
