#!/bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.partition.keypartitioner.options=-k2 \
	-D mapreduce.partition.keycomparator.options=-k2,2nr \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D stream.num.map.output.key.fields=3 \
	-D mapred.reduce.tasks=1 \
	-input /data/assignments/ex2/part2/stackLarge.txt \
	-output /user/s1674939/assignment2/task2/output \
	-mapper EC-Assignment2/task2/mapper2.py \
	-reducer EC-Assignment2/task2/reducer2.py \
	-file EC-Assignment2/task2/mapper2.py EC-Assignment2/task2/reducer2.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner




