## Hadoop MapReduce Streaming

This project performs a series of map reduce jobs on a .csv file stored within the Hadoop file system (HDFS). The original .csv file consists of vehicle sales and subsequent incident records for a number of different vehicles. In order to reduce reduncancy in the data file, not all records contain full vehichle information, only the initial sale record holds vehicle make and model info. The goal of this project is to extract make and year for all accident records and then perform Map Reduce jobs to create a file containing the vehicle make and year as a composite key and the count of accidents as the value. 

The original schema of data.csv stored within HDFS:
![Vehicle Record Schema](/screenshots/vehicle_record_schema.png)

