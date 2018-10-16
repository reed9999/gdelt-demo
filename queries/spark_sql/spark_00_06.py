####
# Only change from 00_05 is that important sc.stop() but for documentary
# purposes it's a new file.  
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
# See https://forums.aws.amazon.com/message.jspa?messageID=688690
sc.stop()