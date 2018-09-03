##############################################################################
# Create a new S3 bucket and populate it with the subset of data on which I want
# my next query to run
# I get the strong impression from https://stackoverflow.com/a/37181013/742573
# that there's no terribly elegant way to select files with wildcards, so
# the iteration here may seem a bit crude.
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

def copy_obj_to_new_bucket(src_obj_name):
    src = {'Bucket': GDELT_BUCKET_NAME, 'Key': src_obj_name}
    copy_resp = client.copy(src, NEW_S3_BUCKET_NAME, 'data/{}'.format(src_obj_name))

# These two lines are untested.
# for objname in ["events/{}.csv".format(x) for x in ['1979','1980','1981','1982']]:
#     copy_obj_to_new_bucket(objname)

list_resp = client.list_objects_v2(Bucket=GDELT_BUCKET_NAME,
                                   Prefix="events/201601")
contents = list_resp['Contents']
for objname in [x['Key'] for x in contents]:
    copy_obj_to_new_bucket(objname)