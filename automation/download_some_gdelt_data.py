#!/usr/bin/python3
####
# Just a utility script to download selected files.
# Because I can't keep 100s of Gb locally, I kept stopping these short so it's 
# an imperfect guide to what I have locally.

import os
from os.path import exists
import re 
import boto3

if (exists("/home/philip")):
    IS_LOCAL = True

###
# Eventually this should probably be refactored to the automation directory
# Code is taken from https://stackoverflow.com/q/31918960/
# My adaptation isn't great though because it downloads stray directories
# not matching the pattern.

client = boto3.client('s3')
resource = boto3.resource('s3')
def download_dir(client, resource, dist, 
    local='/home/philip/aws/data/original', 
    bucket='reed9999',
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
                    print ("Now downloading file: {}".format(file.get('Key')))
                    resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file.get('Key'))

if IS_LOCAL:
    already = [
        '198[2457]\.', 
        '200[6-9]08\.',         
    ]
    for patt in [
        # '197.\.', 
        # '198[^2457]\.', 
        # '200[6-9]08\.', 
        # '200[0-3]02\.', 
        # '200[34]0[79]27\.export', 
        '20060.\.', 
        '2015010.\.', 
        ]:
        print ("Now downloading according to pattern {}".format(patt))
        download_dir(client, resource, dist='events/', 
            bucket='gdelt-open-data', pattern=patt)
    print ("Downloaded")