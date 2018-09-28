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


###
# Eventually this should probably be refactored to the automation directory
# Code is taken from https://stackoverflow.com/q/31918960/
client = boto3.client('s3')
resource = boto3.resource('s3')
def download_dir(client, resource, dist, local='/tmp', bucket='reed9999',
    pattern='.*', ):

    paginator = client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                download_dir(client, resource, subdir.get('Prefix'), local, bucket)
        if result.get('Contents') is not None:
            for file in result.get('Contents'):
                if not os.path.exists(os.path.dirname(local + os.sep + file.get('Key'))):
                     os.makedirs(os.path.dirname(local + os.sep + file.get('Key')))
                if re.search(pattern, file.get('Key')):
                    resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file.get('Key'))

if IS_LOCAL:
    download_dir(client, resource, dist='events/', local='/tmp', bucket='gdelt-open-data',
        pattern='1985\.')
    print ("Downloaded")

if not IS_LOCAL:
    with open("/home/hadoop/output_003.txt", "w") as f:
        f.write(str(len(ev2)))
        f.write("\n")
        f.write(str(ev2))
