##############################################################################
# Uploads the contents of the designated directories to S3
# Python equivalent to scripts/sync-to-s3.sh
# Truthfully I'm not sure this adds that much value other than learning
# the Pythonic way to do it.
# But I believe sync isn't available in boto3
# Framework of this file is from https://github.com/boto/boto3/issues/358
##############################################################################

import os
# import boto3
from pathlib import Path
import awscli
from awscli.clidriver import create_clidriver

def aws_cli(*cmd):
    old_env = dict(os.environ)
    try:

        # Environment
        env = os.environ.copy()
        env['LC_CTYPE'] = u'en_US.UTF'
        os.environ.update(env)

        # Run awscli in the same process
        exit_code = create_clidriver().main(*cmd)

        # Deal with problems
        if exit_code > 0:
            raise RuntimeError('AWS CLI exited with code {}'.format(exit_code))
    finally:
        os.environ.clear()
        os.environ.update(old_env)

S3_BUCKET = 'philip-hadoop-bucket'
SCRIPTS_DIR = os.path.join('automation', 'scripts')
QUERIES_DIR = os.path.join('queries')
BASE_DIR = os.path.join(str(Path.home()), 'aws', 'gdelt-demo')
dirs_to_sync = [SCRIPTS_DIR, QUERIES_DIR]
for dir in dirs_to_sync:
    local_dir = os.path.join(BASE_DIR, dir)
    s3_uri = "s3://{bucket}/{destination}".format(bucket=S3_BUCKET,
        destination = dir)
    aws_cli(('s3', 'sync', local_dir, s3_uri))


### DRY abomination ahead
# Let's do the same for the newer favored bucket
S3_BUCKET = 'reed9999'
for dir in dirs_to_sync:
    local_dir = os.path.join(BASE_DIR, dir)
    s3_uri = "s3://{bucket}/{destination}".format(bucket=S3_BUCKET,
        destination = dir)
    aws_cli(('s3', 'sync', local_dir, s3_uri))
