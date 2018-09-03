##############################################################################
# Start up a small AWS Elastic MapReduce (EMR) custer and load it with some
# predetermined steps.
# Python equivalent to scripts/emr-create-and-run-all.py
###############################################################################

import os
import boto3
#Following DRY violations- see sync-to-s3
S3_BUCKET = 'philip-hadoop-bucket'
SCRIPTS_DIR = os.path.join('automation', 'scripts')
QUERIES_DIR = os.path.join('queries')


AUTOTERMINATE_OR_NOT = False
DEMO_NUMBER="003 through 006"
# REGION='us-west-2'
REGION='ap-south-1'
INSTANCE_TYPE='m1.large'

emr_client = boto3.client('emr')
# The doc is quite opaque but a cluster here is called a "job flow," AFAICT
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html
# https://github.com/aws-samples/aws-python-sample/issues/8
response = emr_client.run_job_flow(
    Name='boto3 EMR creation test',
    # LogUri='string',
    # AdditionalInfo='string',
    # AmiVersion='string',
    ReleaseLabel='emr-4.6.0',
    Instances={
        'MasterInstanceType': 'm3.xlarge',
        'SlaveInstanceType': 'm1.large',
        'InstanceCount': 2,
        'Ec2KeyName' : 'MainKeyPair',
        # 'InstanceGroups': [not accepted because we specified the above]
        # 'InstanceFleets': [also not used for the same reason]
        # 'Placement': {
        #     'AvailabilityZone': 'string',
        #     'AvailabilityZones': [
        #         'string',
        #     ]
        # },
    },
    Steps=[
        {
            'Name': 'Load the gdelt_events table',
            'ActionOnFailure': 'TERMINATE_CLUSTER',
            'HadoopJarStep': {
                'Properties': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ],
                'Jar': 'command-runner.jar',
                # 'Args': [
                # ]
            }
        },
    ],
    BootstrapActions=[],
    # SupportedProducts=[ #incompatible with Applications stating versions
        # I think (cryptic error message)
        # Tez is all that's missing but I don't know if that's a problem.
    #     'tez',
    # ],
    Applications=[
        { 'Name': 'Hadoop', },
        { 'Name': 'Hive',},
        { 'Name': 'Mahout',},
        { 'Name': 'Hue',},
        { 'Name': 'Ganglia',},
        # { 'Name': 'Tez',},
    ],
    VisibleToAllUsers=True,
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
)
