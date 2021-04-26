#!/usr/bin/env bash

# exec &> job_log.txt  # if you want to log stderr and stdout to file
exec >> job_log.txt  # logs stdout to file

hadoop jar /usr/local/Cellar/hadoop/3.3.0/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
-file autoinc_mapper1.py -mapper autoinc_mapper1.py \
-file autoinc_reducer1.py -reducer autoinc_reducer1.py \
-input /input/data.csv \
-output /output/all_accidents 


hadoop jar /usr/local/Cellar/hadoop/3.3.0/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar \
-file autoinc_mapper2.py -mapper autoinc_mapper2.py \
-file autoinc_reducer2.py -reducer autoinc_reducer2.py \
-input /output/all_accidents \
-output /output/make_year_count 