##############################################################################
# Create a new S3 bucket and populate it with the subset of data on which I want
# my next query to run
###############################################################################

import os
import boto3
GDELT_BUCKET_NAME = 'gdelt-open-data'
NEW_S3_BUCKET_NAME = 'reed9999'
client = boto3.client('s3')
create_bucket_config = {'LocationConstraint': 'us-west-2',}
try:
    client.create_bucket(Bucket=NEW_S3_BUCKET_NAME,
                         CreateBucketConfiguration=create_bucket_config)
except: #doesn't recognize BucketAlreadyOwnedByYou:
    print ("Apparently you already own a bucket called {}".format(
        NEW_S3_BUCKET_NAME))

src = {'Bucket': GDELT_BUCKET_NAME, 'Key': 'events/1979.csv'}
client.copy(src, NEW_S3_BUCKET_NAME, 'data/1979.csv')

print ("""INCOMPLETE -- for now it just copies one hard-coded file.
    Shouldn't be too hard to learn how to pass inclusions/exclusions or iterate
     or whatever.""")