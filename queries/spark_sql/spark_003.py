####
# This isn't much of an enhancement over _002, but it tries to write output.
# From command line spark-submit it at least creates the output file, but from
# an EMR step it just runs for over an hour. I'm trying to learn how to 
# troubleshoot that to see if it's stuck.  

from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext, Row

sc = SparkContext()
hiveCtx = HiveContext(sc)
if (exists("/home/philip")):
    FILENAME = "/home/philip/aws/data/mini/1982-micro.csv"
else:
    FILENAME = "s3://reed9999/data/events/20160101.export.csv"
events = hiveCtx.read.format("com.databricks.spark.csv").option("delimiter",
    "\t").load(FILENAME)
ev2 = events.take(2)

with open("/home/hadoop/output_003.txt", "w") as f:
    f.write(str(len(ev2)))
    f.write("\n")
    f.write(str(ev2))
