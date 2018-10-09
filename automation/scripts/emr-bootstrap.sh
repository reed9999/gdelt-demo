#!/usr/bin/env bash
mkdir scripts
aws s3 cp s3://reed9999/queries/spark_sql/spark_001.py /home/hadoop/scripts/spark_001.py
aws s3 cp s3://reed9999/queries/spark_sql/spark_002.py /home/hadoop/scripts/spark_002.py
## For now, note the double underscore (my convention to get git to ignore) is taken off.
aws s3 cp s3://reed9999/queries/spark_sql/__spark_002_standalone.py /home/hadoop/scripts/spark_002_standalone
aws s3 cp s3://reed9999/queries/spark_sql/spark_003.py /home/hadoop/scripts/spark_003.py
pip install pyspark
