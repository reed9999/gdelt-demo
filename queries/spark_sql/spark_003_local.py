####
# Since 003 didn't enhance much, I'm continuing to work as 003 locally.
# Weirdly I can't figure out how I was running Pyspark stuff locally. I don't 
# seem to have pyspark libs installed in any virtualenvs. Time to fix that. 

import os
from os.path import exists
import re 
from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext, Row
import boto3

IS_LOCAL = False
try:
    sc = SparkContext()
except :
    print("""Could not create new spark context. Hopefully this is the common error:
        'Cannot run multiple SparkContexts at once'""")
    raise


hiveCtx = HiveContext(sc)
if (exists("/home/philip")):
    IS_LOCAL = True
    FILENAME = "/home/philip/aws/data/mini/1982-micro.csv"
else:
    FILENAME = "s3://reed9999/data/events/20160101.export.csv"
events = hiveCtx.read.format("com.databricks.spark.csv").option("delimiter",
    "\t").load(FILENAME)
ev2 = events.take(2)


if not IS_LOCAL:
    with open("/home/hadoop/output_003.txt", "w") as f:
        f.write(str(len(ev2)))
        f.write("\n")
        f.write(str(ev2))
