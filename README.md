# MapReduce_Hadoop

## What Is This?

This is a MapReduce python script that is used to analyze vehicular incidents in New York City over a period of time. The dataset was collected from the City of New York’s data website. The mapper and reducer scripts analyze the data and yield summary counts for each vehicle that describe the total count, per vehicle type, that the vehicle type was involved in an incident.

Please refer to https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-Vehicle-Collisions/h9gi-nx95 for more information about the dataset.

## Steps to Run Python Code on Hadoop

1. Make sure the python scripts are executable:
```
chmod +x mapper.py
chmod +x reducer.py
```

2. Change the current working directory to the project
```
cd hw4
```
3. Test the code in local VM
```
cat test.txt | ./mapper.py
cat test.txt | ./mapper.py | sort | ./reducer.py

```

4. Run the python code on Hadoop

```
hadoop jar /usr/hdp/2.6.3.0-235/hadoop-mapreduce/hadoop-streaming-2.7.3.2.6.3.0-235.jar -input /data/nyc/nyc-traffic.csv -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -output output
```

5. Check the output file

Display the ouput from HDFS:
```
hadoop fs -cat output/part-00000 | less
```
 
Copy the ouput file to local VM:
```
hadoop fs -get output/part* output/
```
 
Display the output from local VM:
```
cat output/part-00000 | less
```
 
6. Delete the output file and the job
```
hadoop fs -rm -r output
mapred job -kill job_*
```

7. Display job lists and kill jobs
```
mapred job -list
mapred job -kill <job id>
```



