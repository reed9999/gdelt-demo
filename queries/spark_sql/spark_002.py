####
# This should work on the EMR cluster or locally.
# It apparently needs to be copied down (in theory, I could just spark-submit 
# a .py file on S3 I think, but that's not working for me). Thus run: .
#   aws s3 cp s3://philip-hadoop-bucket/queries/spark-sql/spark-002.py .
# (bucket and filename on s3 will change soon!)


from os.path import exists
from sys import argv
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