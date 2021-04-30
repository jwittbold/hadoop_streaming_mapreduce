## Hadoop MapReduce Streaming

This project performs a series of map reduce jobs on a .csv file stored within the Hadoop file system (HDFS). The original .csv file consists of vehicle sales and subsequent incident records for a number of different vehicles. In order to reduce reduncancy in the data file, not all records contain full vehichle information, only the initial sale record holds vehicle make and model info. The goal of this project is to extract make and year for all accident records and then perform Map Reduce jobs to create a file containing the vehicle make and year as a composite key and the count of accidents for each of those vehicles. 

The original schema of data.csv stored within HDFS:
![Vehicle Record Schema](/screenshots/vehicle_record_schema.png)

To work with the Hadoop File System, you will either need to have it installed on your local machine or alternatively you may run it within a Hortonworks Hadoop Sandbox environment. I am working with a local installation of Hadoop on OS X, and if you're on a Mac and would like to install Hadoop and reproduce this project, here is a straight forward tutorial to get you started:

https://blog.petehouston.com/complete-guide-to-install-and-configure-apache-hadoop-3-on-macos/

