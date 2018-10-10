#!/usr/bin/env bash

# Common setup tasks to configure my AWS Elastic MapReduce (EMR)
# I could separate out the Spark versus Hadoop setup but no real reason.

# SPARK SETUP
# Some of this is redundant if the GitHub cloning below works as expected.
mkdir scripts
aws s3 cp s3://reed9999/queries/spark_sql/spark_001.py /home/hadoop/scripts/spark_001.py
aws s3 cp s3://reed9999/queries/spark_sql/spark_002.py /home/hadoop/scripts/spark_002.py
## For now, note the double underscore (my convention to get git to ignore) is taken off.
aws s3 cp s3://reed9999/queries/spark_sql/__spark_002_standalone.py /home/hadoop/scripts/spark_002_standalone
aws s3 cp s3://reed9999/queries/spark_sql/spark_003.py /home/hadoop/scripts/spark_003.py
pip install pyspark


# HADOOP SETUP
sudo apt install git
git clone http://reed9999/gdelt-demo
ln -s gdelt-demo demo


