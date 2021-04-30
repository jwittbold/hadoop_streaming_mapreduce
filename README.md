## Hadoop MapReduce Streaming

This project performs a series of map reduce jobs on a .csv file stored within the Hadoop file system (HDFS). The original .csv file consists of vehicle sales and subsequent incident records for a number of different vehicles. In order to reduce reduncancy in the original data file, not all records contain full vehichle information, only the initial sale record holds vehicle make, model, and year info. The goal of this project is to obtain vehicle make, year, and total accident count for vehicles with accident records.

The original schema of data.csv stored within HDFS:
![Vehicle Record Schema](/screenshots/vehicle_record_schema.png)

Before we run the MapReduce jobs in HDFS we can test the output of our modules using a copy of data.csv stored within the same directory as our modules.  
First ```autoinc_mapper1.py``` reads the lines contained within data.csv and maps the output as a key/value pair, with the vehicle VIN as the key and a tuple containing incident type, make, and year as the value. We can test this within within our terminal by running: 

```cat data.csv | python autoinc_mapper1.py | sort```

Our output should look like this:
![Mapper1 Output](/screenshots/mapper1_output.png)


Once we have our initial set of desired vehicle records, we will pipe these records to our reducer ```autoinc_reducer1.py```, which will propagate vehicle make and year info into accident records 'A', and then limit our results to only accident records. We can test this by running the following: 

```cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py```

Our output should now only show four 'A' records:
![Reducer1 Output](/screenshots/reducer1_output.png)

Now that we have our desired set of vehicle records, we will pipe these results to our next mapper, ```autoinc_mapper2.py``` which creates a composite key from each vehicle make and year, and a count for each record. We can test this by running:

```cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py | sort ```


The output will consist of four records: 
![Mapper2 Output](/screenshots/mapper2_output.png)


The final step is to pipe our results to ```autoinc_redcuer2.py``` which will read in our composite key and count, and return only results for unique keys while increasing the count for duplicate key occurences. We can test this by running:
```cat data.csv | python autoinc_mapper1.py | sort | python autoinc_reducer1.py | python autoinc_mapper2.py | sort | python autoinc_reducer2.py | sort```

Our final result should be three records:
![Reducer2 Output](/screenshots/reducer2_output.png)


Now that we have tested our MapReduce modules, we can run them as a streaming MapReduce job within Hadoop.

## Using Hadoop
To work with the Hadoop File System, you will either need to have it installed on your local machine or alternatively you may run it within a Hortonworks Hadoop Sandbox environment. I am working with a local installation of Hadoop on OS X, and if you're on a Mac and would like to install Hadoop and reproduce this project, here is a straight-forward tutorial to get you started:

https://blog.petehouston.com/complete-guide-to-install-and-configure-apache-hadoop-3-on-macos/

If you would like to reproduce this project without installing Hadoop on your local machine, here is a link to get you started with Hortonworks Hadoop:
https://www.youtube.com/watch?v=735yx2Eak48

The following assumes you are up and running with Hadoop.
### Input file to HDFS
We will first need to load our file into the Hadoop File System, as well as create the directories in which to access and write our MapReduce jobs. If you followed the OS X Hadoop tutorial above, you may have already created the 'input' directory, otherwise, create it now by running:
  ```hdfs dfs -mkdir /input```

While we are at it, we can create our output directory:
  ```hdfs dfa -mkdir /output```

We can confirm that we have successfully created our directories with:
  ```hdfs dfs -ls /```

Now that we have our working directories, we must add our data.csv file to HDFS. We can easily accomplish this with:
  ```hdfs dfs -put data.csv /input```



