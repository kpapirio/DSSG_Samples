#!/bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
	-D mapreduce.map.output.key.field.separator=" " \
	-D stream.map.output.field.separator=" " \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.partition.keypartitioner.options="-k1,1" \
	-input /data/assignments/ex2/part1/large/ \
	-output /user/s1674939/assignment2/task1/output \
	-mapper EC-Assignment2/task1/mapper1.py \
	-combiner EC-Assignment2/task1/combiner1.py \
	-reducer EC-Assignment2/task1/reducer1.py \
	-file EC-Assignment2/task1/mapper1.py EC-Assignment2/task1/combiner1.py EC-Assignment2/task1/reducer1.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


