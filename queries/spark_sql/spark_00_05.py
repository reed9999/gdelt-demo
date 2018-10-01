####
# What is the minimum case that I can get to hang on AWS EMR?
# Answering that question will help me troubleshoot and help me ask others 
# for help.

# When you run with spark-submit, pyspark is
# automatically added. 

from pyspark import SparkContext
from pyspark.sql import HiveContext

sc = SparkContext()
hiveCtx = HiveContext(sc)
BUCKET_NAME = "reed9999"
FILENAME = "s3://{}/data/trivial/".format(BUCKET_NAME)
events = hiveCtx.read.format("com.databricks.spark.csv").option("delimiter",
    ",").load(FILENAME)
