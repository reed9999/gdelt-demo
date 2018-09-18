####
# This is just from me hacking around on the EMR cluster master but should work
# anywhere with PySpark except for the s3 filename.

from pyspark import SparkContext, SparkConf
from pyspark.sql import HiveContext, Row

sc = SparkContext()
hiveCtx = HiveContext(sc)
# FILENAME = "s3://reed9999/data/events/20160101.export.csv"
FILENAME = "/home/philip/aws/data/mini/1982-micro.csv"
events = hiveCtx.read.format("com.databricks.spark.csv").option("delimiter",
    "\t").load(FILENAME)
ev2 = events.take(2)